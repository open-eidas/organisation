#!/usr/bin/env bash
# Contrôle quotidien des sites OTSPI hébergés chez o2switch : code HTTP attendu, destination
# des redirections et durée de validité restante des certificats TLS.
# Sortie : un rapport lisible ; code de retour 1 si au moins un contrôle échoue.
# signataires.php n'est pas contrôlé : o2switch ne répond pas à cette adresse depuis les serveurs
# de GitHub Actions (le point d'accès reste joignable depuis un poste ordinaire).
set -uo pipefail

MIN_DAYS="${MIN_DAYS:-20}"
fail=0

# adresse | code attendu | destination attendue de la redirection (vide si aucune)
checks=(
  "https://www.otspi.org/|200|"
  "https://www.otspi.org/manifeste|200|"
  "https://www.otspi.org/.well-known/security.txt|200|"
  "https://otspi.org/faq.html|301|https://www.otspi.org/faq.html"
  "https://otspi.com/|301|https://www.otspi.org/"
  "https://otspi.eu/|301|https://www.otspi.org/"
  "https://otspi.fr/|301|https://www.otspi.org/"
  "https://about.otspi.org/|200|"
  "https://about.otspi.org/livre-blanc/otspi-livre-blanc.pdf|200|"
  "https://demo.open-eidas.eu/|200|"
  "https://manifesto-sign.otspi.org/|200|"
  "https://stats.otspi.org/matomo.js|200|"
  "https://open-eidas.eu/|301|https://www.otspi.org/"
  "https://www.open-eidas.eu/|301|https://www.otspi.org/"
)

echo "## Disponibilité"
for c in "${checks[@]}"; do
  IFS='|' read -r url want_code want_dest <<<"$c"
  res=$(curl -s -o /dev/null --max-time 30 --retry 2 --retry-delay 5 -w '%{http_code}|%{redirect_url}' "$url")
  code=${res%%|*}; dest=${res#*|}
  if [[ "$code" == "$want_code" && "$dest" == "$want_dest" ]]; then
    echo "OK     $url ($code)"
  else
    echo "ÉCHEC  $url : obtenu $code ${dest:+-> $dest}, attendu $want_code ${want_dest:+-> $want_dest}"
    fail=1
  fi
done

echo
echo "## Certificats (seuil : $MIN_DAYS jours)"
hosts=(www.otspi.org otspi.org otspi.com www.otspi.com otspi.eu www.otspi.eu otspi.fr www.otspi.fr
       about.otspi.org demo.open-eidas.eu manifesto-sign.otspi.org stats.otspi.org open-eidas.eu www.open-eidas.eu)
now=$(date -u +%s)
for h in "${hosts[@]}"; do
  pem=$(echo | timeout 20 openssl s_client -connect "$h:443" -servername "$h" 2>/dev/null | openssl x509 2>/dev/null)
  end=$(openssl x509 -noout -enddate <<<"$pem" 2>/dev/null | cut -d= -f2)
  if [[ -z "$end" ]]; then
    echo "ÉCHEC  $h : certificat illisible"
    fail=1
    continue
  fi
  if ! openssl x509 -noout -checkhost "$h" <<<"$pem" 2>/dev/null | grep -q "does match"; then
    echo "ÉCHEC  $h : le certificat ne couvre pas ce nom"
    fail=1
    continue
  fi
  days=$(( ($(date -u -d "$end" +%s) - now) / 86400 ))
  if (( days < MIN_DAYS )); then
    echo "ÉCHEC  $h : expire dans $days jours ($end)"
    fail=1
  else
    echo "OK     $h : $days jours"
  fi
done

exit "$fail"

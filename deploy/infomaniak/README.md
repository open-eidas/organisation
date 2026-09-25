# Sortie de GitHub Pages : portail sur Infomaniak

Ce dossier prépare l'hébergement du portail `about.otspi.org` chez Infomaniak (Suisse, décision d'adéquation RGPD), à la place de GitHub Pages (société américaine). Rien n'est actif tant que les étapes ci-dessous ne sont pas faites : le portail reste servi par GitHub Pages.

## Ce qui est prêt

- `htaccess` : redirection HTTPS, domaine canonique, page 404, en-têtes de sécurité, compression et durées de cache.
- `.github/workflows/deploy-infomaniak.yml` : construit le site, exporte et valide les PDF, ajoute le `.htaccess`, puis envoie tout par FTP. Déclenchement **manuel** uniquement.

## Étapes (à faire dans l'espace client Infomaniak et sur GitHub)

1. **Créer le site** `about.otspi.org` dans le Manager Infomaniak (hébergement web, nouveau site pour un sous-domaine).
2. **Créer un compte FTP dédié**, limité au seul répertoire de ce site (ne pas réutiliser celui de la vitrine). Relever l'hôte et le répertoire.
3. **Ajouter les secrets** du dépôt `otspi/organisation` : `ABOUT_FTP_HOST`, `ABOUT_FTP_USERNAME`, `ABOUT_FTP_PASSWORD`, et la variable `ABOUT_FTP_SERVER_DIR` si le répertoire n'est pas la racine du compte.
4. **Lancer le workflow** « Déploiement du portail sur Infomaniak (FTP) » à la main, puis contrôler le site avec l'adresse provisoire fournie par Infomaniak (ou en forçant la résolution : `curl --resolve about.otspi.org:443:<IP> https://about.otspi.org/`). Le certificat n'est délivré qu'après la bascule DNS.
5. **Basculer le DNS** (zone `otspi.org`, gérée chez Infomaniak) : remplacer l'enregistrement `about` (aujourd'hui un CNAME vers `otspi.github.io`) par l'adresse du nouvel hébergement. Baisser la durée de vie (TTL) de l'enregistrement quelques heures avant.
6. **Activer le certificat HTTPS** dans le Manager une fois le DNS propagé, puis vérifier la redirection et les PDF.
7. **Retirer GitHub Pages** : supprimer `docs/CNAME`, désactiver Pages dans les paramètres du dépôt, retirer `.github/workflows/deploy-pages.yml`, et ajouter `push` au déclenchement de `deploy-infomaniak.yml`.
8. **Mettre à jour la page de transparence** [Hébergements](../../docs/reunions/hebergements.md) et sa version anglaise.

## Précautions

- Le FTP d'Infomaniak est sans TLS : le mot de passe transite en clair entre GitHub et l'hébergeur. D'où le compte cantonné à un seul répertoire.
- `mirror --delete` supprime les fichiers distants absents du dépôt : vérifier `ABOUT_FTP_SERVER_DIR` avant le premier envoi.
- Les adresses `https://about.otspi.org/...` doivent rester valides : le site est identique, seul l'hébergeur change.

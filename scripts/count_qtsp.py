#!/usr/bin/env python3
# SPDX-License-Identifier: EUPL-1.2
"""Décompte des prestataires de services de confiance qualifiés (QTSP) des listes de confiance de l'EEE.

Source : liste des listes de confiance européenne (LOTL) et listes nationales qu'elle référence.
Est compté comme QTSP tout prestataire disposant d'au moins un service au statut « granted » ;
comme QTSP d'horodatage, tout prestataire disposant d'au moins un service de type
QTST (horodatage qualifié) au statut « granted ». Voir l'annexe C du livre blanc.

Usage :
    python3 scripts/count_qtsp.py                       # affiche le résultat en JSON
    python3 scripts/count_qtsp.py --output data/qtsp-count.json
    python3 scripts/count_qtsp.py --compare data/qtsp-count.json   # code de sortie 10 si les chiffres ont changé

Aucune dépendance en dehors de la bibliothèque standard.
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

LOTL = "https://ec.europa.eu/tools/lotl/eu-lotl.xml"
NS = {"t": "http://uri.etsi.org/02231/v2#"}
QTST = "http://uri.etsi.org/TrstSvc/Svctype/TSA/QTST"
GRANTED = "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted"
TIMEOUT = 90
ATTEMPTS = 4


def fetch(url):
    """Télécharge une URL avec plusieurs tentatives (certains serveurs nationaux coupent la connexion)."""
    last = None
    for attempt in range(1, ATTEMPTS + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (OTSPI figures)"})
            return urllib.request.urlopen(request, timeout=TIMEOUT).read()
        except Exception as error:  # noqa: BLE001 - toute erreur réseau justifie une nouvelle tentative
            last = error
            time.sleep(2 * attempt)
    raise RuntimeError(f"{url} : {last}")


def national_lists():
    root = ET.fromstring(fetch(LOTL))
    lists = []
    for pointer in root.iter("{%s}OtherTSLPointer" % NS["t"]):
        location = pointer.find("t:TSLLocation", NS).text
        mime = [e.text for e in pointer.iter() if e.tag.endswith("MimeType")]
        territory = [e.text for e in pointer.iter() if e.tag.endswith("SchemeTerritory")]
        if mime and "xml" in mime[0] and territory and territory[0] != "EU":
            lists.append((territory[0], location))
    return lists


def count(item):
    country, url = item
    try:
        root = ET.fromstring(fetch(url))
    except Exception as error:  # noqa: BLE001
        return country, None, str(error)[:200]
    providers = with_qtst = 0
    for tsp in root.iter("{%s}TrustServiceProvider" % NS["t"]):
        granted = qtst = False
        for service in tsp.iter("{%s}ServiceInformation" % NS["t"]):
            if service.find("t:ServiceStatus", NS).text == GRANTED:
                granted = True
                if service.find("t:ServiceTypeIdentifier", NS).text == QTST:
                    qtst = True
        providers += granted
        with_qtst += qtst
    return country, {"qtsp": providers, "qtsp_qtst": with_qtst}, None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", help="écrit le résultat dans ce fichier JSON")
    parser.add_argument("--compare", help="compare avec un fichier JSON existant")
    args = parser.parse_args()

    countries, errors = {}, {}
    with cf.ThreadPoolExecutor(8) as pool:
        for country, result, error in pool.map(count, national_lists()):
            if error:
                errors[country] = error
            else:
                countries[country] = result

    result = {
        "date": dt.date.today().isoformat(),
        "source": LOTL,
        "listes": len(countries),
        "qtsp": sum(c["qtsp"] for c in countries.values()),
        "qtsp_horodatage": sum(c["qtsp_qtst"] for c in countries.values()),
        "par_pays": dict(sorted(countries.items())),
        "erreurs": errors,
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        sys.stdout.write(text)

    if errors:
        sys.stderr.write(f"Listes en erreur (résultat incomplet) : {', '.join(sorted(errors))}\n")
        sys.exit(2)
    if args.compare:
        with open(args.compare, encoding="utf-8") as handle:
            previous = json.load(handle)
        if (previous["qtsp"], previous["qtsp_horodatage"]) != (result["qtsp"], result["qtsp_horodatage"]):
            sys.stderr.write(
                f"Chiffres modifiés : QTSP {previous['qtsp']} → {result['qtsp']}, "
                f"horodatage {previous['qtsp_horodatage']} → {result['qtsp_horodatage']}\n"
            )
            sys.exit(10)


if __name__ == "__main__":
    main()

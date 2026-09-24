#!/usr/bin/env python3
"""Génère le PDF de référence du livre blanc à partir du site MkDocs construit.

Le site est servi localement puis imprimé par Chrome (ou Chromium) en mode
headless ; la mise en page est portée par docs/stylesheets/print.css.

Usage :
    python scripts/export_pdf.py            # utilise le site déjà construit dans ./site
    python scripts/export_pdf.py --build    # construit d'abord le site (mkdocs build --strict)

La variable d'environnement CHROME permet d'imposer le binaire du navigateur.
"""

import argparse
import functools
import http.server
import os
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

CHROME_CANDIDATES = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")
PAGE_PATH = "livre-blanc/"
PDF_NAME = "otspi-livre-blanc.pdf"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for candidate in CHROME_CANDIDATES:
        path = shutil.which(candidate)
        if path:
            return path
    sys.exit("Chrome ou Chromium introuvable : définir la variable d'environnement CHROME.")


def serve(directory):
    handler = functools.partial(QuietHandler, directory=str(directory))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--site", default="site", type=Path, help="répertoire du site construit")
    parser.add_argument("--output", type=Path, help=f"chemin du PDF (défaut : <site>/{PAGE_PATH}{PDF_NAME})")
    parser.add_argument("--build", action="store_true", help="exécuter mkdocs build --strict au préalable")
    args = parser.parse_args()

    site = args.site.resolve()
    output = (args.output or site / PAGE_PATH / PDF_NAME).resolve()

    if args.build:
        subprocess.run(["mkdocs", "build", "--strict", "--site-dir", str(site)], check=True)
    if not (site / PAGE_PATH / "index.html").is_file():
        sys.exit(f"Page introuvable : {site / PAGE_PATH / 'index.html'} (lancer avec --build)")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.unlink(missing_ok=True)

    httpd = serve(site)
    url = f"http://127.0.0.1:{httpd.server_address[1]}/{PAGE_PATH}"
    try:
        with tempfile.TemporaryDirectory() as profile:
            cmd = [
                find_chrome(),
                "--headless=new",
                "--disable-gpu",
                "--no-first-run",
                "--no-default-browser-check",
                f"--user-data-dir={profile}",
                "--no-pdf-header-footer",
                # Laisse le temps au rendu des diagrammes Mermaid
                "--virtual-time-budget=20000",
                "--run-all-compositor-stages-before-draw",
                f"--print-to-pdf={output}",
                url,
            ]
            if os.environ.get("CI"):
                cmd.insert(1, "--no-sandbox")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    finally:
        httpd.shutdown()

    if result.returncode != 0 or not output.is_file() or output.stat().st_size == 0:
        sys.stderr.write(result.stderr)
        sys.exit("Échec de la génération du PDF.")

    print(f"PDF généré : {output} ({output.stat().st_size // 1024} Kio)")


if __name__ == "__main__":
    main()

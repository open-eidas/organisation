#!/usr/bin/env python3
"""Génère les PDF de référence du livre blanc (français et anglais) à partir du site MkDocs construit.

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
# Pages exportées : répertoire de la page dans le site construit → nom du PDF
DOCUMENTS = {
    "livre-blanc/": "otspi-livre-blanc.pdf",
    "white-paper/": "otspi-white-paper.pdf",
}


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


def print_pdf(url, output):
    """Imprime une page en PDF avec Chrome headless ; renvoie le résultat du processus."""
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            find_chrome(),
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",
            "--no-pdf-header-footer",
            "--generate-pdf-document-outline",
            # Laisse le temps au rendu des diagrammes Mermaid
            "--virtual-time-budget=20000",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={output}",
            url,
        ]
        if os.environ.get("CI"):
            cmd.insert(1, "--no-sandbox")
        return subprocess.run(cmd, capture_output=True, text=True, timeout=180)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--site", default="site", type=Path, help="répertoire du site construit")
    parser.add_argument("--build", action="store_true", help="exécuter mkdocs build --strict au préalable")
    args = parser.parse_args()

    site = args.site.resolve()
    if args.build:
        subprocess.run(["mkdocs", "build", "--strict", "--site-dir", str(site)], check=True)

    httpd = serve(site)
    try:
        for page_path, pdf_name in DOCUMENTS.items():
            if not (site / page_path / "index.html").is_file():
                sys.exit(f"Page introuvable : {site / page_path / 'index.html'} (lancer avec --build)")
            output = site / page_path / pdf_name
            output.unlink(missing_ok=True)
            result = print_pdf(f"http://127.0.0.1:{httpd.server_address[1]}/{page_path}", output)
            if result.returncode != 0 or not output.is_file() or output.stat().st_size == 0:
                sys.stderr.write(result.stderr)
                sys.exit(f"Échec de la génération du PDF : {pdf_name}")
            print(f"PDF généré : {output} ({output.stat().st_size // 1024} Kio)")
    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()

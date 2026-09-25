# SPDX-License-Identifier: EUPL-1.2
"""Aligne l'attribut lang de la balise <html> sur la métadonnée `lang` de la page.

Material fixe la langue du site entier (`theme.language`). Les pages rédigées dans une autre
langue, comme la version anglaise du livre blanc, déclarent `lang: en` : sans ce correctif, les
lecteurs d'écran et le PDF exporté les annonceraient en français.
"""

import re


def on_post_page(output, page, config):
    lang = (page.meta or {}).get("lang")
    if not lang:
        return output
    return re.sub(r'(<html\b[^>]*\blang=")[^"]*(")', rf"\g<1>{lang}\g<2>", output, count=1)

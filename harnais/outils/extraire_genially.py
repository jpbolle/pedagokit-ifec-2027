"""Extrait le texte d'un export Genially hors ligne (genially.html) vers un fichier .txt.

L'export Genially range tout le contenu dans `window.dataBase64` (JSON encodé en base64).
On décode, on parcourt le JSON et on garde les champs de texte, débarrassés des balises HTML,
dans l'ordre des diapositives.

Usage : python3 harnais/outils/extraire_genially.py <genially.html> <sortie.txt>
"""

import base64
import html
import json
import re
import sys


def textes(noeud, sortie):
    """Collecte récursivement les chaînes qui contiennent du texte lisible."""
    if isinstance(noeud, dict):
        for cle, valeur in noeud.items():
            if cle in ("Text", "text", "Html", "html", "Title", "title") and isinstance(valeur, str):
                propre = html.unescape(re.sub(r"<[^>]+>", " ", valeur))
                propre = re.sub(r"\s+", " ", propre).strip()
                if len(propre) > 1:
                    sortie.append(propre)
            else:
                textes(valeur, sortie)
    elif isinstance(noeud, list):
        for element in noeud:
            textes(element, sortie)


def main():
    source, cible = sys.argv[1], sys.argv[2]
    page = open(source, encoding="utf-8", errors="replace").read()
    trouve = re.search(r'window\.dataBase64="([^"]+)"', page)
    if not trouve:
        sys.exit("Pas de window.dataBase64 dans ce fichier : export Genially non reconnu.")
    donnees = json.loads(base64.b64decode(trouve.group(1)).decode("utf-8"))
    lignes = []
    textes(donnees, lignes)
    # Supprime les doublons consécutifs (titres répétés par Genially)
    dedoublonne = [l for i, l in enumerate(lignes) if i == 0 or l != lignes[i - 1]]
    open(cible, "w", encoding="utf-8").write("\n".join(dedoublonne) + "\n")
    print(f"{len(dedoublonne)} blocs de texte -> {cible}")


if __name__ == "__main__":
    main()

"""Vérifie une fiche de formation IFEC : limites de caractères, rubriques obligatoires vides.

Les limites du formulaire Annexe 2 s'entendent ESPACES COMPRIS ; au-delà, le texte est coupé.
Chaque rubrique de la fiche est un titre « ## Nom (max N) » suivi de son texte.

Usage : python3 harnais/outils/verifier_fiche.py fiches/G131/nom-sujet.md [autres fiches…]
Code de sortie 1 si une limite est dépassée ou une rubrique obligatoire est vide.
"""

import re
import sys

# Rubriques obligatoires du formulaire (Annexe 2) — le reste est facultatif
OBLIGATOIRES = {
    "Intitulé", "Mots-clés", "Objectifs pédagogiques généraux", "Objectifs pédagogiques spécifiques",
    "Répartition des heures", "Répartition flexible", "Modalités", "Régions",
    "Contenus abordés", "Méthodologie", "Niveau d'enseignement", "Publics cibles",
    "Années", "Discipline", "Formateurs",
}
SANS_CONTROLE = {"Notes internes"}


def rubriques(texte):
    """Découpe la fiche en (nom, limite, unité, contenu) ; ignore l'en-tête et les commentaires."""
    texte = re.sub(r"<!--.*?-->", "", texte, flags=re.S)
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    for i in range(1, len(morceaux), 2):
        titre, contenu = morceaux[i], morceaux[i + 1].strip()
        nom = re.sub(r"\s*\(.*\)\s*$", "", titre).strip()
        limite = re.search(r"\(max (\d+)( mots-clés)?\)", titre)
        yield nom, (int(limite.group(1)) if limite else None), bool(limite and limite.group(2)), contenu


def verifier(chemin):
    erreurs = 0
    print(f"\n=== {chemin}")
    for nom, limite, en_mots_cles, contenu in rubriques(open(chemin, encoding="utf-8").read()):
        if nom in SANS_CONTROLE:
            continue
        obligatoire = any(nom.startswith(o) for o in OBLIGATOIRES)
        if en_mots_cles:
            n = len([l for l in re.split(r"[\n;,]", contenu) if l.strip(" -*")])
            mesure = f"{n} mot(s)-clé(s)"
        else:
            n = len(contenu)
            mesure = f"{n} car."
        if not contenu:
            etat = "VIDE (obligatoire)" if obligatoire else "vide"
            erreurs += obligatoire
        elif limite and n > limite:
            etat = f"TROP LONG de {n - limite}"
            erreurs += 1
        elif limite and n > 0.95 * limite:
            etat = "ok (proche de la limite)"
        else:
            etat = "ok"
        borne = f" / {limite}" if limite else ""
        print(f"  {etat:<26} {nom} — {mesure}{borne}")
    print(f"  → {'AUCUN PROBLÈME' if not erreurs else f'{erreurs} problème(s)'}")
    return erreurs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    total = sum(verifier(c) for c in sys.argv[1:])
    sys.exit(1 if total else 0)

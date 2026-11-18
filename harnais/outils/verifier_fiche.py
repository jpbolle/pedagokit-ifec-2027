"""Vérifie une fiche de formation IFEC : limites de caractères, rubriques obligatoires vides.

Les limites du formulaire Annexe 2 s'entendent ESPACES COMPRIS ; au-delà, le texte est coupé.
Chaque rubrique de la fiche est un titre « ## Nom (max N) » suivi de son texte.

Usage : python3 harnais/outils/verifier_fiche.py fiches/G131/nom-sujet.md [autres fiches…]
Deux comptes séparés : les rubriques obligatoires encore « à remplir » (normal pendant la
rédaction) et les rubriques « TROP LONGUES » (à corriger tout de suite : elles seraient coupées).
Une rubrique obligatoire absente du fichier (fiche créée avec un ancien modèle) est signalée
« ABSENTE » : la recopier depuis fiches/_modele.md.
Code de sortie 1 si une limite est dépassée ou une rubrique obligatoire est vide ou absente.
"""

import re
import sys

# Rubriques obligatoires du formulaire (Annexe 2, IFEC-MP-2027-v2.5, p. 4-9) — le reste est facultatif
OBLIGATOIRES = {
    "Intitulé", "Mots-clés", "Objectifs pédagogiques généraux", "Objectifs pédagogiques spécifiques",
    "Nombre d'heures envisagées", "Répartition des heures", "Répartition flexible", "Modalités",
    "Nombre minimum de participants", "Régions",
    "Contenus abordés", "Méthodologie", "Niveau d'enseignement", "Type d'enseignement",
    "Publics cibles", "Années", "Filières", "Type de formation", "Discipline",
    "Nombre de formateurs", "Formateurs",
}
# Obligatoire seulement si « Spécialisé » ou « Pôles territoriaux » est coché dans Type d'enseignement
SPECIFICITES = "Spécificités du public spécialisé ou des pôles"
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
    a_remplir = trop_longs = 0
    print(f"\n=== {chemin}")
    liste = list(rubriques(open(chemin, encoding="utf-8").read()))
    noms = [nom for nom, *_ in liste]
    type_ens = next((c for nom, _, _, c in liste if nom == "Type d'enseignement"), "").lower()
    specificites_requises = "spécialisé" in type_ens or "pôle" in type_ens
    for nom, limite, en_mots_cles, contenu in liste:
        if nom in SANS_CONTROLE:
            continue
        obligatoire = nom in OBLIGATOIRES or (nom == SPECIFICITES and specificites_requises)
        if en_mots_cles:
            n = len([l for l in re.split(r"[\n;,]", contenu) if l.strip(" -*")])
            mesure = f"{n} mot(s)-clé(s)"
        else:
            n = len(contenu)
            mesure = f"{n} car."
        if not contenu:
            etat = "à remplir (obligatoire)" if obligatoire else "vide"
            a_remplir += obligatoire
        elif limite and n > limite:
            etat = f"TROP LONG de {n - limite}"
            trop_longs += 1
        elif limite and n > 0.95 * limite:
            etat = "ok (proche de la limite)"
        else:
            etat = "ok"
        borne = f" / {limite}" if limite else ""
        print(f"  {etat:<26} {nom} — {mesure}{borne}")
    requis = OBLIGATOIRES | ({SPECIFICITES} if specificites_requises else set())
    for absente in sorted(requis - set(noms)):
        print(f"  {'ABSENTE (obligatoire)':<26} {absente} — à recopier depuis fiches/_modele.md")
        a_remplir += 1
    if not a_remplir and not trop_longs:
        print("  → AUCUN PROBLÈME")
    else:
        print(f"  → {trop_longs} rubrique(s) TROP LONGUE(S) à raccourcir ; "
              f"{a_remplir} rubrique(s) obligatoire(s) encore à remplir")
    return a_remplir + trop_longs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    total = sum(verifier(c) for c in sys.argv[1:])
    sys.exit(1 if total else 0)

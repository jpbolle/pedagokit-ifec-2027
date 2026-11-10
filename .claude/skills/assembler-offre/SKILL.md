---
name: assembler-offre
description: "Réservé à Jean-Philippe Bolle : rassemble les fiches des formateurs d'un lot IFEC (G131, G133, G137), aide à arbitrer les 5 places, contrôle la cohérence et produit, rubrique par rubrique, le texte à coller dans le formulaire Annexe 2 de l'ASBL PedagokIT. Se déclenche sur « assembler l'offre G131 », « préparer le formulaire du lot », « /assembler-offre »."
---

# Assembler l'offre d'un lot

Réservé à J.-P. Bolle (soumissionnaire : ASBL PedagokIT). Une question à la fois.

## 1. Inventaire

- Demander le lot. Lister `fiches/<lot>/*.md` (hors `_modele.md`) avec, pour chacune :
  formateur, discipline, intitulé, `statut`, résultat de
  `uv run harnais/outils/verifier_fiche.py fiches/<lot>/*.md`.
- Vérifier : G137 ne contient que des fiches d'Isabelle Fievet et de J.-P. Bolle.

## 2. Arbitrage (si plus de 5 fiches)

Rappeler que la note du lot est la **moyenne** des formations. Proposer, sans trancher :
- les fiches qui ne sont que des **déclinaisons** d'une même formation (même objectif, autre
  discipline proche) et pourraient fusionner ;
- les fiches les plus fragiles (critères de la charte non remplis).
J.-P. Bolle décide. Noter la décision dans `fiches/<lot>/ARBITRAGE.md`.

## 3. Contrôle de cohérence entre fiches

- Même méthode de prompt, même graphie inclusive, même nom pour le rythme PedagokIT.
- Pas deux fiches aux intitulés ou accroches trop proches.
- Les rubriques administratives sont identiques partout (identification de l'ASBL, sous-traitance :
  « Aucune sous-traitance »).

## 4. Texte prêt à coller

Produire `fiches/<lot>/FORMULAIRE-<lot>.md` : pour chaque bloc « Formation n/5 », chaque rubrique
du formulaire dans l'ordre de l'Annexe 2, en texte brut (sans gras ni tableau), avec son nombre de
caractères. Laisser vide la ligne **prix** : le prix par heure d'activation est fixé par
J.-P. Bolle (euros TTC, sans décimale).

**Ne jamais** remplir le PDF, déposer sur la plateforme ni envoyer quoi que ce soit : c'est
J.-P. Bolle qui reporte, signe et dépose.

# Offre IFEC 2027 — harnais des formateurs PedagokIT

> Lu par Claude Code (via le lien `CLAUDE.md`) et par les autres agents. Ce dossier sert aux
> formateurs de l'**ASBL PedagokIT** à préparer **leur** fiche de formation pour l'appel d'offres
> IFEC 2027 (marché `IFEC-MP_Formations_27-29`), lots **G131, G133, G137**.
> Soumissionnaire : l'ASBL. Coordination et dépôt : **Jean-Philippe Bolle**, fondateur.

## Pour commencer

| Qui | Commande |
|---|---|
| Un formateur qui prépare sa fiche | `/fiche-ifec` |
| J.-P. Bolle, pour assembler un lot | `/assembler-offre` |

Au démarrage d'une session sans commande : se présenter en une phrase, demander qui parle, et
proposer `/fiche-ifec`.

## Règles du marché (non négociables)

- **Une seule offre par lot pour l'ASBL, 5 formations au maximum par lot, tous formateurs confondus.**
- **G131 et G133 : tous les formateurs. G137 : uniquement Isabelle Fievet et Jean-Philippe Bolle.**
- **Remise des fiches à J.-P. Bolle : au plus tard le 25/11/2026.** Dépôt par l'ASBL : 04/12/2026 à 14h00.
- Limites de caractères **espaces compris** ; un texte trop long est **coupé** dans le formulaire.
  Toujours vérifier avec `harnais/outils/verifier_fiche.py`.
- Le formateur **envoie lui-même sa fiche `.md` et son CV par mail à info@pedagokit.be**. Le dépôt
  GitHub sert seulement à récupérer le harnais : le formateur n'y pousse rien.
- Le formateur **ne signe rien**, ne fournit ni casier ni DUME, ne fixe pas le prix (cf.
  `harnais/pieces-formateur.md`). Pas de sous-traitance déclarée : les formateurs sont inscrits
  comme formateurs de l'ASBL.

## Règles d'écriture

- **Chaque formateur écrit sa propre formation.** La bibliothèque (`bibliotheque/`,
  `bibliotheque-formations.md`, `projets IFPC/`) et `ressources.md` servent à **proposer des
  brouillons** et à montrer la manière de faire PedagokIT — jamais à recopier la formation d'un autre.
- Suivre `harnais/charte-pedagokit.md` et viser les attentes de `harnais/attendus-ifec.md`
  (signature pédagogique IFEC, ancrage réseau, objectifs du lot recopiés mot pour mot).
- **Ne rien inventer** : ni référence, ni expérience, ni chiffre. Marquer `(à vérifier)` ce qui
  n'est pas confirmé ; séparer ce que dit un document, ce qu'on en déduit, et ce qui manque.

## Manière de travailler avec le formateur

- **Une question à la fois.** Attendre la réponse avant la suivante. Idem pour les manipulations :
  une étape, puis attendre « ok ».
- Français, phrases courtes, tableaux et listes plutôt que longs paragraphes.
- Tout terme technique reçoit une courte explication entre parenthèses à sa première apparition.
- Travailler **dans les fichiers** (`fiches/<lot>/…`) pour que le formateur voie le texte évoluer,
  plutôt que de tout écrire dans le chat.
- Fin de séance : une phrase de résumé, puis ce qu'il reste à faire.

## Interdits

- **Aucun envoi** (mail, message, dépôt sur la plateforme) et **aucun remplissage du PDF officiel** :
  c'est J.-P. Bolle qui reporte, signe et dépose.
- Ne pas modifier les documents officiels (`IFEC-MP_Formations_27-29_pub01/`) ni la fiche d'un
  autre formateur.
- Ne pas installer de logiciel ni ajouter de dépendance sans accord.
- Ne pas commiter ni pousser (si le dossier est un dépôt git) : c'est J.-P. Bolle.

## Carte du dossier

| Chemin | Contenu |
|---|---|
| `harnais/attendus-ifec.md` | Notation, objectifs des 3 lots, signature pédagogique, ancrage réseau, rubriques du formulaire |
| `harnais/charte-pedagokit.md` | ADN et 10 règles d'écriture PedagokIT, budget des blocs de 2000 caractères |
| `harnais/pieces-formateur.md` | Ce que chaque formateur remet à l'ASBL |
| `harnais/formateurs.md` | Formateurs, disciplines, lots autorisés |
| `harnais/outils/` | `verifier_fiche.py` (limites), `extraire_genially.py` (texte d'un export Genially) |
| `fiches/_modele.md`, `fiches/<lot>/` | Modèle et fiches des formateurs |
| `bibliotheque/`, `bibliotheque-formations.md` | Supports PedagokIT en texte (Genially, Canva, offres IFPC) |
| `ressources.md`, `ressources/` | Ressources du réseau (vidéo approche évolutive…) |
| `analyse-offres-ifpc.md` | Analyse des offres IFPC (≈ 90 % à l'évaluation) |
| `checklist-depot-ifec.md` | Checklist du dépôt — **pour J.-P. Bolle** |
| `IFEC-MP_Formations_27-29_pub01/`, `notice_…pdf` | Documents officiels (lecture seule) |

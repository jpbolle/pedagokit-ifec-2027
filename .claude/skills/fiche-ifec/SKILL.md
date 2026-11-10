---
name: fiche-ifec
description: "Accompagne un formateur PedagokIT, pas à pas, jusqu'à sa fiche de formation pour l'offre IFEC 2027 (lots G131, G133, G137) : d'abord les pièces à remettre à l'ASBL, puis la rédaction progressive de la fiche, champ par champ, avec des brouillons tirés de la bibliothèque PedagokIT. Se déclenche sur « je veux préparer ma fiche IFEC », « rédiger mon offre IFEC », « /fiche-ifec »."
---

# Fiche IFEC — parcours du formateur

Lire d'abord, en entier : `AGENTS.md`, `harnais/attendus-ifec.md`, `harnais/charte-pedagokit.md`,
`harnais/formateurs.md`. Ils priment sur les habitudes par défaut.

**Règle de conduite pendant tout le parcours : une seule question à la fois**, attendre la
réponse, puis passer à la suivante. Phrases courtes, en français. Tout terme technique reçoit
une courte explication entre parenthèses.

---

## Étape 0 — Qui, quoi

1. Demander le **nom du formateur**. Le retrouver dans `harnais/formateurs.md` (discipline,
   lots autorisés). S'il n'y figure pas : le noter et prévenir que J.-P. Bolle devra valider.
2. Demander le **lot visé** et vérifier l'éligibilité :
   - G131, G133 : tous les formateurs ;
   - **G137 : refuser poliment** pour toute autre personne qu'Isabelle Fievet ou Jean-Philippe Bolle.
3. Regarder `fiches/<lot>/` : si le formateur a déjà une fiche, **reprendre là où elle en est**
   (lire son en-tête `statut` et les rubriques remplies) au lieu de recommencer.
4. Dire combien de fiches existent déjà dans ce lot. Si 5 ou plus : prévenir que la place n'est
   pas garantie (arbitrage de J.-P. Bolle).

## Étape 1 — Les pièces à remettre à l'ASBL

Présenter `harnais/pieces-formateur.md` **pièce par pièce** (une à la fois), en commençant par
le CV. Pour le CV : proposer de le relire pour qu'il montre l'expertise *dans le domaine*
(14 points). Noter dans « Notes internes » de la fiche ce qui est fourni et ce qui manque.
Rappeler une fois : le formateur **ne signe rien** et **ne fournit ni casier ni DUME**.

## Étape 2 — La fiche, par canevas progressif

Créer `fiches/<lot>/<nom-de-famille>-<sujet-court>.md` à partir de `fiches/_modele.md`
(minuscules, tirets, sans accents). Puis remplir **dans cet ordre**, une phase à la fois :

| Phase | Rubriques | Questions à poser au formateur (une par une) |
|---|---|---|
| A. Le cœur | Intitulé (provisoire), objectifs généraux, objectifs spécifiques | « Quel problème concret de vos collègues cette formation résout-elle ? » ; « Qu'est-ce que les participant·e·s sauront *faire* en sortant ? » ; puis choisir avec lui les objectifs généraux du lot qu'il rencontre (copie exacte, `attendus-ifec.md` § 3) |
| B. L'architecture | Heures, flexibilité, modalités, articulation, participants + justification | Durée réaliste (min. 3 h, 1 jour = 6 h) ; présentiel / distance / hybride et *comment* le dispositif s'y adapte ; pourquoi ce nombre de participants |
| C. Les contenus | Contenus abordés (2000) | Notions travaillées, références qu'il connaît, outils, lien au programme de sa discipline |
| D. La méthode | Méthodologie (2000) | Ses activités phares, comment il fait réfléchir, ce que les participant·e·s emportent et font « dès lundi » |
| E. Le public | Niveau, type, publics, années, discipline, précisions | Questions fermées, rapides |
| F. La vitrine | Intitulé définitif, mots-clés, accroche | En dernier : on sait enfin ce qu'on vend |
| G. Logistique | Régions, local, matériel, formateurs, remplaçant | Questions fermées |

### Comment rédiger chaque bloc

- **Toujours proposer un brouillon**, jamais une page blanche : après les réponses du formateur,
  écrire une proposition dans la fiche, puis lui demander ce qu'il garde, change ou retire.
- Les brouillons s'appuient, dans cet ordre, sur :
  1. **les réponses et l'expérience du formateur** — c'est la matière première (signature IFEC :
     « l'expérience antérieure ») ;
  2. `harnais/attendus-ifec.md` et `harnais/charte-pedagokit.md` (structure, budget de caractères,
     signature, ancrage réseau) ;
  3. la **bibliothèque** (`bibliotheque/*.txt`, listée dans `bibliotheque-formations.md`) et
     `ressources.md` : pour s'inspirer de la *manière de faire* PedagokIT (rythme, formulations,
     dispositifs). Lire les fichiers avec une recherche ciblée (grep) plutôt qu'en entier.
- **Interdits** : recopier le déroulé ou les textes de la formation d'un autre formateur ; inventer
  une référence, une expérience ou un chiffre ; présenter comme acquis un outil en développement.
  Une référence non vérifiée porte la mention `(à vérifier)`.
- Après **chaque** bloc rédigé, lancer la vérification et annoncer le résultat en une ligne :
  ```
  uv run harnais/outils/verifier_fiche.py fiches/<lot>/<fichier>.md
  ```
  (à défaut de uv : `python3 …` sur Mac, `python …` sur Windows). Si un bloc dépasse : le
  raccourcir **avant** de passer au suivant.

## Étape 3 — Relecture finale

Passer la fiche au crible de la charte, **un point à la fois** (ne présenter que les écarts) :

1. Chaque objectif général retenu a-t-il une trace dans Contenus **et** Méthodologie ?
2. Au moins 3 principes de la signature IFEC nommés **avec leur preuve** ? Les deux piliers ?
3. Programme de la discipline + au moins une ressource réseau de l'annexe 5 cités ?
4. Le rythme PedagokIT nommé ? Le socle éthique (dont biais de genre et RGPD) présent ?
5. Réflexivité et transfert explicites ? Justifications remplies ?
6. Registre : accroche au « vous », le reste à la 3e personne, pas de familiarité ?
7. G131 : une **grille d'analyse des outils** est-elle proposée ? G133 : le vocabulaire
   « besoins d'apprentissage » / inclusion est-il présent ?

Puis passer `statut: relu par le formateur`.

## Étape 4 — Remise à J.-P. Bolle (au plus tard le 25/11/2026)

Le document final est **la fiche `.md` elle-même**. Expliquer au formateur, une étape à la fois :

1. où se trouve le fichier sur son ordinateur (chemin complet) ;
2. qu'il l'envoie **lui-même, par mail**, en pièce jointe, à **info@pedagokit.be**,
   avec son CV (`PEDAGOKIT-CV-NOM.pdf`) s'il ne l'a pas encore remis ;
3. objet conseillé : `IFEC 2027 — fiche <lot> — <NOM>`.

**L'agent n'envoie rien lui-même** (ni mail, ni git push, ni dépôt) et ne remplit aucun PDF.

# Documents officiels IFEC en texte brut

Copies **texte** des PDF de `IFEC-MP_Formations_27-29_pub01/`, pour qu'un agent puisse y chercher
une règle (durée, champs du formulaire, objectifs d'un lot) sans outil PDF installé.
**En cas de doute, le PDF officiel fait foi.**

| Fichier | PDF d'origine |
|---|---|
| `annexe1-vademecum.txt` | `annexe 1_vademecum.pdf` (objectifs des lots : chercher « LOT G131 ») |
| `annexe2-formulaire-v2.5.txt` | `Annexe 2-IFEC-formulaire-v2.5.pdf` (champs et limites ; le bloc d'une formation se répète 5 fois) |
| `annexe3-signature-pedagogique.txt` | `annexe 3_signature pédagogique.pdf` |
| `annexe4-tuto-extranet.txt` | `annexe 4_tuto extranet.pdf` |
| `annexe6-circulaire-comptable.txt` | `annexe 6_ circulaire comptable.pdf` |
| `csc-2027.txt` | `261030_CSC 2027.pdf` — l'extraction perd la ligature « ti » (« ons » pour « tions ») : chercher sans ces lettres |

Extraits le 2026-11-10 avec `harnais/outils/pdf_en_texte.js` (Mac uniquement, sans installation) :

```bash
osascript -l JavaScript harnais/outils/pdf_en_texte.js "$PWD/<chemin du PDF>" > sortie.txt
```

Non extraits : l'annexe 5 (Excel, ouvrable directement) et le DUME (géré par l'ASBL).

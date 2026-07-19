# Kopo Website Skill

Skill Claude pour générer des sites web conformes à la charte Kopo V1.4.

## Démarrage rapide

### Avec Claude
Mentionnez simplement votre besoin : « fais-moi une landing pour Kopo Cloud », « génère une page de mentions légales pour kopo.systems », etc. Claude détectera ce skill et l'appliquera automatiquement.

### En CLI (scaffolder Python)
```bash
python scripts/new_site.py --config exemple-config.json --out ./mon-site
```

## Architecture

- `assets/` : logos, illustrations, polices officielles
- `css/` : `shared.css` (toutes pages) + `landing.css` (sections marketing)
- `js/` : `shared.js` (Kobot interactif, reveal, nav, drawer mobile)
- `templates/` : trois variantes (`landing/`, `internal/`, `legal/`)
- `references/` : catalogue de sections + checklist de conformité
- `scripts/` : scaffolder Python `new_site.py`

## Deux styles cohabitent

| Style | Référence dans l'écosystème | Template |
|---|---|---|
| Marketing riche, hero immersif | KopoHome (kopo.systems) | `landing/` |
| Sobre, dense, grille 12 colonnes | Kopo Download (download.kopo.systems) | `internal/` |
| Une colonne 780px, hiérarchie H2 | (nouveau) | `legal/` |

## Conformité

Avant livraison, parcourir `references/checklist.md`. Les règles d'or :

1. Un seul élément en Cirrus plein par viewport
2. Satoshi exclusive, fallback Roboto système
3. Aligné à gauche, jamais justifié
4. Proportions invariantes du Kobot (22% / 7% / 7%)
5. 60-70% d'espace blanc minimum
6. Footer Nimbus systématique

## Licences

- Satoshi · Indian Type Foundry
- Lucide icons · ISC
- Assets Kopo · usage interne Kopo uniquement, marque déposée

Brest, France · contact@kopo.systems

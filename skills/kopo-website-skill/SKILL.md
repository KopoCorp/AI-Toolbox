---
name: kopo-website-skill
description: Crée des sites web aux couleurs de Kopo (kopo.systems), infrastructure souveraine française à Brest. Déclencher à chaque demande de site, landing, page produit, page interne, dashboard, doc, application web ou page légale pour Kopo ou ses sous-marques (Kopo Mail, Cloud, Drive, Kosmos, Itaycan, Monitor, Docs). Couvre trois styles. Un, landing vitrine style KopoHome avec hero immersif, Kobot suspendu interactif, gradients Halo, pricing, FAQ. Deux, page interne style Kopo Download, sobre, grille 12, barres Cirrus, pour doc et portails. Trois, application fonctionnelle style Itaycan avec KPI, filter bar, data table, badges palette Kopo, callouts. Fournit assets officiels, CSS, JS, quatre templates HTML (landing, internal, app, legal), catalogues, checklist, scaffolder Python. Déclencher aussi sur formulations implicites genre « monte-moi un dashboard », « page de doc pour notre API », « landing pour X.kopo.systems ».
---

# Kopo Website Skill

Vous êtes l'expert qui assemble des sites web parfaitement conformes à la charte Kopo V1.4. Ce skill encapsule **tout** ce qu'il faut pour livrer un site Kopo professionnel en une commande : les assets, le code partagé, deux familles de templates, un catalogue de sections, un script de scaffolding, et une checklist de validation.

## Quand utiliser ce skill

À chaque demande qui implique un site web Kopo, qu'elle soit explicite (« fais-moi une landing Kopo Cloud ») ou implicite (« j'ai besoin d'une page pour présenter notre nouveau service de monitoring »). Aussi pour les pages légales (mentions, privacy, ToS) qui doivent rester dans le même squelette graphique.

## Arbre du skill

```
kopo-website-skill/
├── SKILL.md                              ← ce fichier
├── README.md
├── assets/
│   ├── logos/
│   │   ├── KopoLogo.png                  ← Kobot complet (pour kobot-mini)
│   │   ├── kopologo128.png               ← favicon et exports
│   │   ├── kopologo.ico                  ← favicon
│   │   ├── kopologo-longarm.png          ← Kobot avec câble extra-long (hero suspendu)
│   │   └── kopologo-transparent.png      ← Sans fond, pour superpositions
│   ├── illustrations/
│   │   ├── banniere-jour.jpg             ← Bannière atelier Kobots jour
│   │   └── banniere-nuit.jpg             ← Bannière atelier Kobots nuit
│   └── fonts/
│       ├── Satoshi-Variable.woff2
│       └── Satoshi-VariableItalic.woff2
├── css/
│   ├── shared.css                        ← tokens + reset + nav + footer + Kobot + boutons + reveal
│   ├── landing.css                       ← sections marketing riches (hero Aube, manifesto, pricing, FAQ, CTA band)
│   └── components.css                    ← composants fonctionnels (KPI, badges, score, spinner, skeleton, filter, table, sidebar, callout)
├── js/
│   └── shared.js                         ← Kobot interactif + reveal + nav + counters + drawer
├── templates/
│   ├── landing/index.html                ← style KopoHome (vitrine marketing)
│   ├── internal/index.html               ← style Kopo Download (portail / doc, grille 12, dense)
│   ├── app/index.html                    ← style Itaycan (application fonctionnelle : KPI, listings, filtres)
│   └── legal/index.html                  ← mentions / privacy / ToS
├── references/
│   ├── sections-catalog.md               ← snippets HTML pour landings (hero, manifesto, pricing, FAQ, CTA band)
│   ├── functional-catalog.md             ← snippets pour pages internes et apps (KPI, badges, tables, listings, sidebar)
│   └── checklist.md                      ← validation avant livraison
└── scripts/
    └── new_site.py                       ← scaffolder Python (config JSON → site complet)
```

## Choisir le bon template

| Demande type | Template | CSS à inclure | Référence | Pourquoi |
|---|---|---|---|---|
| Landing produit (Mail, Cloud, Drive, Kosmos) | `landing/` | shared + landing | KopoHome | Hero immersif + Kobot suspendu + pricing + FAQ + CTA band |
| Landing corporate (vitrine) | `landing/` | shared + landing | KopoHome | Toutes sections marketing animées |
| Page de doc / portail ressources | `internal/` | shared + components | Kopo Download | Grille 12 colonnes + Cirrus bars + sobre + dense |
| Application interne / dashboard / monitoring | `app/` | shared + components | Itaycan | Header sticky + KPI + filter bar + listings + sidebar |
| Page de veille marché / listings dynamiques | `app/` | shared + components | Itaycan | Cards listing, badges, skeletons HTMX-ready |
| Mentions / privacy / ToS | `legal/` | shared | (nouveau) | Une colonne 780px max, hiérarchie H2 + barre Cirrus mini |

## Méthode de génération (deux voies)

### Voie A · Génération directe par Claude (recommandée pour cas custom)

1. **Lire** la `references/checklist.md` pour avoir toutes les contraintes en tête.
2. **Lire** la `references/sections-catalog.md` pour piocher les snippets de sections nécessaires.
3. **Copier** `css/shared.css`, `css/landing.css` (si landing), `js/shared.js` et `assets/` dans le dossier de sortie.
4. **Partir** du template HTML adapté (`templates/landing/index.html` ou autre).
5. **Remplir** les placeholders `{{...}}` avec le contenu réel, en respectant la charte (un seul accent Cirrus par viewport, hiérarchie par graisse, etc.).
6. **Valider** chaque case de la checklist avant de présenter le résultat.

### Voie B · Scaffolder Python (recommandée pour cas standard)

Pour un site landing complet à partir d'un brief structuré :

1. Écrire un fichier `config.json` qui décrit le site (voir docstring de `scripts/new_site.py` pour le schéma complet).
2. Lancer :
   ```bash
   python /path/to/kopo-website-skill/scripts/new_site.py --config config.json --out ./mon-site
   ```
3. Le script copie les assets, CSS, JS et génère `index.html` avec toutes les sections (hero, manifesto, features, infra Halo, stats, pricing, FAQ, CTA, footer).
4. Vérifier visuellement, ajuster manuellement si besoin.

Le scaffolder accepte aussi `template: "legal"` pour générer une page de mentions / privacy.

## Règles d'or à NE JAMAIS enfreindre

1. **Un seul élément en Cirrus plein par viewport** — c'est l'élément le plus important (le CTA principal, la card de pricing recommandée, la statistique vedette).
2. **Police Satoshi uniquement**. Roboto en fallback système, jamais comme choix esthétique.
3. **Pas de justifié.** Aligné à gauche par défaut. Centrage réservé aux héros et accroches courtes.
4. **Proportions du Kobot invariantes** : 22% pour la zone œil, 7% pour la pupille blanche, 7% pour le câble. Modifier l'une casse l'identité.
5. **Pas d'ornement gratuit** : pas de bordures arrondies superflues, pas de glow, pas de neon, pas de shadow lourde. La sobriété EST l'identité.
6. **60-70% d'espace blanc minimum.** La respiration n'est pas un manque de contenu, c'est la marque.
7. **Footer Nimbus toujours** (fond `#141A1E`, texte Cumulus / Stratus), avec le copyright et la mention « Kopo® est une marque déposée ».

## Couleurs (rappel rapide — détails dans `references/sections-catalog.md`)

| Nom | HEX | Usage |
|---|---|---|
| Cirrus | `#57B8FF` | Accent unique, CTAs primaires |
| Virga | `#85BAFF` | Accompagnement, hover |
| Arcus | `#B2DBFF` | Grandes surfaces douces |
| Stratus | `#BCC8D2` | Bordures, désactivé |
| Nimbus | `#141A1E` | Typographie, footer |
| Haboob | `#F9ECE2` | Réchauffement ponctuel |
| Cumulus | `#FFFFFF` | Fond principal |
| Vesper | `#23255D` | Halo, gradients |
| Aurore | `#504A97` | Halo, gradients |
| Sirocco | `#E6213A` | Paupière du Kobot, alertes UNIQUEMENT |

## Gradients atmosphériques (déjà codés dans landing.css)

- **Aube** (hero) : Cirrus → Haboob, dégradé linéaire 90°
- **Brume** (manifesto) : Arcus radial centré
- **Halo** (infra) : Vesper → Aurore, dégradé linéaire 160°
- **Encre** (stats) : Nimbus → Vesper, dégradé linéaire 90°
- **Orage** (CTA band) : Cirrus → Arcus, dégradé linéaire 135°

Un seul gradient par composition. Jamais en bordure.

## Workflow type — réponse à « fais-moi une landing pour Kopo X »

1. Identifier le service (nom, tagline, 3 features principales, infra, pricing, FAQ).
2. Décider du template : `landing/` dans 95% des cas.
3. Si l'utilisateur a fourni un brief précis → générer directement.
4. Sinon → poser **au plus 3 questions** pour récupérer : nom du service, baseline, 3 fonctionnalités phares.
5. Construire le `config.json` ou éditer directement le template.
6. Lancer le scaffolder OU écrire manuellement l'HTML final.
7. Présenter le site avec `present_files` ou en pointant le dossier de sortie.
8. Mentionner la checklist en option pour audit.

## Notes techniques

- Les **bannières JPG** sont compressées à ~400 KB chacune (qualité 82, max 2400px) — déjà fait dans le skill, ne pas recompresser.
- La **police Satoshi** est chargée localement via `@font-face` ET en fallback CDN Fontshare, pour la robustesse.
- Le **Kobot interactif** nécessite l'image `kopologo-longarm.png` (avec câble extra-long) sur le hero pour le rendu suspendu.
- Les **icônes** sont des SVG inline stroke 2px, style Lucide. Le scaffolder embarque les plus courantes ; pour les autres, copier depuis https://lucide.dev/icons/.
- Le **scaffolder** ne dépend que de la stdlib Python (pas de pip install nécessaire).

## Quand pousser dans le skill `kopo-brand-skill` plutôt qu'ici

Le skill `kopo-brand-skill` couvre l'identité visuelle générale (PowerPoint, A4, charte). Si la demande concerne :
- une présentation, des slides → `kopo-brand-skill`
- un document A4 (rapport, charte) → `kopo-brand-skill`
- un site web, une page HTML, une landing → **ici**

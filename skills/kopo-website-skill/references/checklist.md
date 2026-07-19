# Checklist de conformité Kopo Web

À cocher AVANT de livrer un site Kopo. Si une case échoue, corriger avant de présenter.

## Couleurs

- [ ] Couleurs exactes utilisées (HEX précis, pas d'approximation)
- [ ] **Un seul** élément en Cirrus plein par viewport (le plus important)
- [ ] Pas de couleur secondaire (Vesper / Aurore / Sirocco) combinée à une autre secondaire
- [ ] Sirocco utilisé UNIQUEMENT pour alertes / paupière du Kobot — jamais décoratif
- [ ] Haboob utilisé ponctuellement pour réchauffer une surface, pas en aplat large
- [ ] Pour les pages fonctionnelles : badges sémantiques (green/amber/red) pour les statuts opérationnels, pas badges colorés décoratifs

## Typographie

- [ ] Satoshi chargé localement (WOFF2) + fallback Fontshare CDN
- [ ] Aucune autre police que Satoshi (Roboto uniquement en fallback système)
- [ ] Hiérarchie construite par poids (Bold vs Regular), pas par taille
- [ ] Letter-spacing -0.02em sur les titres
- [ ] Alignement à gauche par défaut
- [ ] Pas de justifié (interdit absolu)
- [ ] Max-width 60ch sur les paragraphes pour la lisibilité

## Layout

- [ ] Grille 12 colonnes respectée sur les pages internes
- [ ] Container max-width 1440px (marketing) ou 1200px (interne)
- [ ] Padding section généreux : 9rem sur landing, 5rem sur interne
- [ ] 60-70% d'espace blanc minimum (respiration > remplissage)
- [ ] Marges responsive via `clamp()` ou variable `--container-px`

## Logo & Kobot

- [ ] Proportions invariantes du Kobot respectées (22% œil, 7% pupille, 7% câble)
- [ ] Sirocco uniquement pour le cerne de l'œil
- [ ] Kobot interactif (`data-interactive`) sur le hero — pupille suit la souris
- [ ] Sur hero landing : Kobot suspendu (`kobot-longarm` + `kobot-swing-anchor`)
- [ ] Mini-kobot dans nav et footer (`kobot-mini`, 40px)

## Composants

- [ ] Barre Cirrus (180×3px) sous chaque H2 sur pages internes
- [ ] Boutons : `btn-primary` (Nimbus → hover Cirrus), `btn-ghost` (outline Nimbus → hover Cirrus)
- [ ] Cards avec border `--stratus-soft`, hover → border Cirrus + lift 6px
- [ ] Icônes Lucide stroke 2px, tailles 16/20/24/32/64/80 uniquement
- [ ] Section-eyebrow en uppercase Cirrus letter-spacing 0.18em

## Animations & interactivité

- [ ] `reveal` + `IntersectionObserver` sur les blocs principaux
- [ ] Nav passe en `scrolled` (blur + fond) après 30px de scroll
- [ ] Compteurs animés (`data-count`) au scroll
- [ ] Pendule du Kobot draggable (mobile + desktop)
- [ ] Burger + drawer fullscreen sur mobile (<800px)
- [ ] Transitions standard : 0.2s pour hover, 0.4s pour reveal, 0.8s pour reveal long

## Footer

- [ ] Fond Nimbus, texte Cumulus / Stratus
- [ ] Grille 4 colonnes (1.5fr 1fr 1fr 1fr) → 2 colonnes en tablette → 1 en mobile
- [ ] Headings de colonne : 0.72rem uppercase, letter-spacing 0.18em, Stratus
- [ ] Copyright en bas avec border-top 1px rgba(255,255,255,0.12)
- [ ] Mention "© {YEAR} Kopo® · Tous droits réservés. Kopo est une marque déposée."

## Accessibilité

- [ ] `lang="fr"` sur `<html>`
- [ ] `aria-label` sur les icônes décoratives et boutons sans texte
- [ ] `aria-hidden="true"` sur les SVG décoratifs
- [ ] Contraste suffisant entre Nimbus et fonds clairs (vérifié natif)
- [ ] Focus visible sur les liens et boutons (outline natif Satoshi)
- [ ] `<meta name="viewport">` présent

## Responsive

- [ ] Breakpoint 800px : nav devient burger, hero passe en 1 colonne
- [ ] Breakpoint 768px : grille 12 → toutes colonnes en `span 12`
- [ ] Breakpoint 480px : footer en 1 colonne, stats 1 colonne
- [ ] Aucun débordement horizontal (vérifier `overflow-x: hidden` sur body)

## Performance

- [ ] Bannières JPG compressées (~400 KB max, qualité 82)
- [ ] Polices Satoshi en `font-display: swap`
- [ ] Pas de framework JS lourd
- [ ] Images avec `loading="lazy"` sauf le hero
- [ ] `backdrop-filter` n'est appliqué que sur la nav et le drawer

## Pages fonctionnelles (templates internal et app)

- [ ] `components.css` importé en complément de `shared.css`
- [ ] Header en `.nav-sticky` (sticky simple, pas de blur fancy)
- [ ] Si dense en données : `.data-table` avec `<thead>` distinct, `.num` sur les colonnes chiffrées
- [ ] Statuts opérationnels via `.kopo-badge.badge-virga` (OK), `.badge-haboob` (dégradé), `.badge-sirocco` (incident critique) — pas de vert, pas d'ambre, jamais hors charte
- [ ] LED visuel pour states live : `.led.on / .live / .warn / .alert`
- [ ] Loading states via `.skel` ou `.kopo-spinner`, jamais page blanche
- [ ] Score bars (`.score-bar` + `.score-fill`) pour les progressions / mesures
- [ ] Callouts (`.callout.info/warn/error/success`) pour les messages importants
- [ ] Filter bar (`.filter-bar`) avec labels en uppercase Stratus 0.7rem
- [ ] Tabular numbers (`font-variant-numeric: tabular-nums`) sur les colonnes de chiffres
- [ ] Mobile : tables en `overflow-x: auto` (déjà géré par `.data-table` au breakpoint 768px)
- [ ] KPI grid : 4 cartes en desktop, 2 en tablette, 1 en mobile

## Légal

- [ ] Mentions légales accessibles depuis le footer
- [ ] Privacy policy accessible depuis le footer
- [ ] Pour KoBot Discord : ToS + Privacy obligatoires
- [ ] Copyright Kopo + marque déposée mentionnés

# Catalogue des composants fonctionnels Kopo

À utiliser pour les templates `internal/` et `app/`. Pour les sections marketing (hero, manifesto, pricing, FAQ, CTA band), voir `sections-catalog.md`.

Tous ces composants reposent sur `css/components.css` qui doit être inclus en complément de `css/shared.css`.

## 1. KPI Grid (4 cartes de mesure)

```html
<div class="kpi-grid">
  <div class="kpi-card">
    <div class="kpi-label">{{LABEL_UPPERCASE}}</div>
    <div class="kpi-value">{{NUMBER}}<span class="unit">{{UNIT}}</span></div>
    <div class="kpi-delta up">↑ {{DELTA}}</div>
  </div>
  <!-- répéter 3 fois -->
</div>
```

Les modifieurs `kpi-delta` : `.up` (vert), `.down` (Sirocco), `.flat` (Stratus).

## 2. Badges (palette Kopo stricte, aucune couleur hors charte)

Le mapping sémantique repose sur la palette officielle. Le bleu Kopo signifie « bon / actif » par convention de marque, et c'est délibéré.

```html
<!-- Actif / OK / sain (Cirrus = principal, Virga = secondaire plus doux) -->
<span class="kopo-badge badge-cirrus">Actif</span>
<span class="kopo-badge badge-virga">En ligne</span>

<!-- Info / nouveau / disponible (Arcus dilué, texte Vesper) -->
<span class="kopo-badge badge-arcus">Nouveau</span>

<!-- Désactivé / brouillon / neutre (Stratus) -->
<span class="kopo-badge badge-stratus">Brouillon</span>

<!-- Attention douce / beta / en attente (Haboob = beige chaud avec contour) -->
<span class="kopo-badge badge-haboob">Beta</span>
<span class="kopo-badge badge-haboob">Dégradé</span>

<!-- Majeur / premium / éditorial (Aurore = mauve crépusculaire) -->
<span class="kopo-badge badge-aurore">Majeur</span>
<span class="kopo-badge badge-aurore">Premium</span>

<!-- Éditorial fort (Vesper = mauve nuit) -->
<span class="kopo-badge badge-vesper">Privé</span>

<!-- Erreur / alerte critique (Sirocco — usage RARE et intentionnel) -->
<span class="kopo-badge badge-sirocco">Hors ligne</span>
```

**Règles** :
- Un seul `badge-cirrus` par ligne / item — c'est l'accent principal de la composition.
- `badge-sirocco` est réservé aux incidents critiques (service down, perte de données). Ne JAMAIS l'utiliser pour une simple baisse ou un statut « warning ».
- Pour les statuts « beta / dégradé / en attente », `badge-haboob` est le bon choix : il signale sans alarmer.
- `badge-aurore` pour distinguer (« majeur », « premium », « nouveau »).

## 3. Score bar (progress visuel)

```html
<div style="display:flex; align-items:center; gap:0.75rem;">
  <div class="score-bar" style="flex:1;">
    <div class="score-fill" style="width: 72%"></div>
  </div>
  <span style="font-size:0.85rem; font-weight:600; min-width:32px; text-align:right;">7.2</span>
</div>
```

Variantes : `score-fill.aurore` (violet), `score-fill.red` (alerte).

## 4. LED de statut (live, dégradé, alerte)

```html
<span class="led on" aria-label="En ligne"></span>      <!-- Cirrus -->
<span class="led live" aria-label="Live"></span>        <!-- Cirrus pulse -->
<span class="led warn" aria-label="Dégradé"></span>     <!-- Haboob beige -->
<span class="led alert" aria-label="Hors ligne"></span> <!-- Sirocco pulse -->
<span class="led" aria-label="Inconnu"></span>          <!-- Stratus -->
```

Les LED suivent la même hiérarchie que les badges : Cirrus pour OK, Haboob pour attention douce, Sirocco pour incident critique uniquement.

## 5. Spinner Kopo (chargement)

```html
<div class="kopo-spinner" aria-label="Chargement"></div>
```

40×40 par défaut. Pour une taille personnalisée :
```html
<div class="kopo-spinner" style="width:24px; height:24px;"></div>
```

## 6. Skeleton (placeholder loading)

```html
<div class="skel" style="height:1rem; width:60%;"></div>
<div class="skel" style="height:1.5rem; width:40%; margin-top:0.5rem;"></div>
```

S'utilise dans une carte qui attend ses vraies données :
```html
<div class="kopo-card kopo-card-padded">
  <div class="skel" style="height:0.7rem; width:30%;"></div>
  <div class="skel" style="height:1.8rem; width:50%; margin-top:0.5rem;"></div>
</div>
```

## 7. Filter bar (dense form de filtres)

```html
<div class="filter-bar">
  <div>
    <label for="f-status">Statut</label>
    <select id="f-status">
      <option value="">Tous</option>
      <option>Actif</option>
      <option>Désactivé</option>
    </select>
  </div>
  <div>
    <label for="f-search">Recherche</label>
    <input id="f-search" type="search" placeholder="ID, nom..." />
  </div>
  <div>
    <label for="f-from">Depuis</label>
    <input id="f-from" type="date" />
  </div>
</div>
```

La grille s'adapte automatiquement (`minmax(140px, 1fr)`). Empile en colonnes étroites.

## 8. Data table (tableau dense)

```html
<table class="data-table">
  <thead>
    <tr>
      <th>Nom</th>
      <th>Statut</th>
      <th>Score</th>
      <th class="num">Prix</th>
      <th class="num">Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Serveur prod-01</strong><br><span class="muted">srv-01.kopo.systems</span></td>
      <td><span class="kopo-badge badge-virga">Actif</span></td>
      <td>
        <div style="display:flex; align-items:center; gap:0.5rem;">
          <div class="score-bar" style="width:80px;"><div class="score-fill" style="width:92%"></div></div>
          <span style="font-size:0.8rem; font-weight:600;">9.2</span>
        </div>
      </td>
      <td class="num">42 800 €</td>
      <td class="num muted">12 mars 2026</td>
    </tr>
    <!-- répéter -->
  </tbody>
</table>
```

Modifier : `data-table.compact` pour des lignes plus serrées.

## 9. Listing card (carte média + titre + prix, façon Itaycan)

```html
<div class="listing-card">
  <div class="visual">
    <!-- image, icône, ou aplat Halo -->
    <img src="..." alt="..." style="width:100%; height:100%; object-fit:cover;" />
  </div>
  <div class="body">
    <h3 class="title">{{TITLE}}</h3>
    <div class="price">{{PRICE}} €</div>
    <div class="meta">
      <span>{{META_1}}</span>
      <span>·</span>
      <span>{{META_2}}</span>
    </div>
    <div class="footer-row">
      <span class="kopo-badge badge-virga">Actif</span>
      <a href="#" style="color:var(--cirrus); font-weight:500;">Détails →</a>
    </div>
  </div>
</div>
```

À placer dans un conteneur `.listing-grid` qui adapte le nombre de colonnes selon la largeur.

## 10. App shell (sidebar + main)

```html
<div class="app-shell">
  <aside class="app-sidebar">
    <h4>Tableau de bord</h4>
    <ul>
      <li><a href="#" class="active">{{ICON}} Vue d'ensemble</a></li>
      <li><a href="#">{{ICON}} Activité</a></li>
    </ul>
    <h4>Configuration</h4>
    <ul>
      <li><a href="#">{{ICON}} Paramètres</a></li>
      <li><a href="#">{{ICON}} Utilisateurs</a></li>
    </ul>
  </aside>
  <div class="app-main">
    <!-- contenu de la page -->
  </div>
</div>
```

`active` sur le lien courant. En `<900px`, la sidebar passe au-dessus du contenu en bloc plein.

## 11. Callout / Alert (palette Kopo stricte)

```html
<!-- Info / contexte / note (bordure et icône Cirrus) -->
<div class="callout info">
  <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><circle cx="12" cy="8" r=".5"/></svg>
  <div class="body">
    <strong>À noter</strong>
    Cette information complète le contexte.
  </div>
</div>

<!-- Tip / suggestion (bordure et icône Aurore) -->
<div class="callout tip"> ... </div>

<!-- Attention douce (bordure brun-Haboob, fond Haboob clair) -->
<div class="callout warn"> ... </div>

<!-- Erreur critique (bordure et icône Sirocco — usage rare) -->
<div class="callout error"> ... </div>
```

Quatre variantes seulement. Pas de `success` séparé : un événement positif relève de `info`. Le vert n'existe pas dans la charte Kopo, et c'est volontaire.

## 12. Breadcrumb

```html
<nav class="breadcrumb" aria-label="Fil d'Ariane">
  <a href="/">Accueil</a>
  <span class="sep">/</span>
  <a href="/section">Section</a>
  <span class="sep">/</span>
  <span class="current">Page courante</span>
</nav>
```

## 13. Code block (pour documentation)

```html
<div class="code-block">
  <span class="lang">bash</span>
<pre>
docker run -d \
  --name kopo-monitor \
  -p 8080:8080 \
  kopo/monitor:latest
</pre>
</div>
```

Pour de l'inline :
```html
Lancez la commande <span class="code-inline">systemctl status kopo</span> pour vérifier.
```

## 14. Section avec grille 12 colonnes (style Kopo Download)

```html
<section id="{{ID}}" class="container" style="padding: 4rem 0;">
  <span class="section-eyebrow">{{LABEL_UPPERCASE}}</span>
  <h2 style="font-size:1.75rem; font-weight:700; letter-spacing:-0.02em;">{{TITLE}}</h2>
  <div class="cirrus-bar"></div>

  <div class="grid-12" style="gap:32px; margin-top:24px;">
    <div class="col-span-7">
      <p>{{PARAGRAPHE_PRINCIPAL}}</p>
      <a href="#" class="btn btn-primary">{{CTA}}</a>
    </div>
    <div class="col-span-5">
      <!-- visuel, code block, callout, ou aperçu -->
    </div>
  </div>
</section>
```

Alterner avec `<section class="section-alt">` (fond #F7F8FA) pour rythmer.

## 15. Page title row (titre + actions de toolbar)

```html
<div class="page-title-row">
  <div>
    <h1>{{PAGE_TITLE}}</h1>
  </div>
  <div class="toolbar-actions">
    <button class="btn btn-outline">{{ACTION_2}}</button>
    <button class="btn btn-primary">{{ACTION_1}}</button>
  </div>
</div>
```

## Règles d'or pour pages fonctionnelles

- **Densité OK, désordre non.** L'aération de marque s'applique encore : utiliser `gap` et `padding` généreux dans les conteneurs, même si le contenu est dense.
- **Un seul Cirrus actif par viewport** : si KPI cards + bouton primaire + LED live, choisir lequel mérite Cirrus, le reste en neutre.
- **Aucune couleur hors charte.** Pas de vert, pas d'ambre, pas de bleu marine, pas de rouge autre que Sirocco. Le bleu Kopo signifie « bon », point.
- **Sirocco rare et intentionnel** : uniquement pour les incidents critiques (service down, perte). Une simple latence élevée → Haboob, pas Sirocco.
- **Tabular numbers** : tous les chiffres en colonnes doivent porter `font-variant-numeric: tabular-nums` (déjà sur `.data-table .num`).
- **Loading states** : pas de page blanche, toujours skeletons ou spinner pendant le fetch.
- **Pas de tableau pleine largeur sans `overflow-x: auto`** sur mobile (déjà géré par `.data-table` en breakpoint).
- **Hero optionnel** : sur une page d'app interne, le `page-title-row` avec h1 + barre Cirrus suffit. Ne mettre un hero Halo que si la page mérite un accent éditorial fort (page d'accueil de l'app, par exemple).

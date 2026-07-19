# Kopo functional component catalog

Use for the `internal/` and `app/` templates. For marketing sections (hero, manifesto, pricing, FAQ, CTA band), see `sections-catalog.md`.

All these components rely on `css/components.css`, which must be included alongside `css/shared.css`. User-facing strings stay in French (Kopo sites are French).

## 1. KPI Grid (4 metric cards)

```html
<div class="kpi-grid">
  <div class="kpi-card">
    <div class="kpi-label">{{LABEL_UPPERCASE}}</div>
    <div class="kpi-value">{{NUMBER}}<span class="unit">{{UNIT}}</span></div>
    <div class="kpi-delta up">↑ {{DELTA}}</div>
  </div>
  <!-- repeat 3 more times -->
</div>
```

`kpi-delta` modifiers: `.up`, `.down` (Sirocco), `.flat` (Stratus).

## 2. Badges (strict Kopo palette, no off-brand colors)

The semantic mapping relies on the official palette. Kopo blue means "good / active" by brand convention, and that is deliberate.

```html
<!-- Active / OK / healthy (Cirrus = primary, Virga = softer secondary) -->
<span class="kopo-badge badge-cirrus">Actif</span>
<span class="kopo-badge badge-virga">En ligne</span>

<!-- Info / new / available (diluted Arcus, Vesper text) -->
<span class="kopo-badge badge-arcus">Nouveau</span>

<!-- Disabled / draft / neutral (Stratus) -->
<span class="kopo-badge badge-stratus">Brouillon</span>

<!-- Soft warning / beta / pending (Haboob = warm beige with outline) -->
<span class="kopo-badge badge-haboob">Beta</span>
<span class="kopo-badge badge-haboob">Dégradé</span>

<!-- Major / premium / editorial (Aurore = twilight mauve) -->
<span class="kopo-badge badge-aurore">Majeur</span>
<span class="kopo-badge badge-aurore">Premium</span>

<!-- Strong editorial (Vesper = night mauve) -->
<span class="kopo-badge badge-vesper">Privé</span>

<!-- Error / critical alert (Sirocco — RARE and intentional use) -->
<span class="kopo-badge badge-sirocco">Hors ligne</span>
```

**Rules**:
- One `badge-cirrus` per row / item — it's the composition's main accent.
- `badge-sirocco` is reserved for critical incidents (service down, data loss). NEVER use it for a mere dip or a "warning" status.
- For "beta / degraded / pending" statuses, `badge-haboob` is the right choice: it signals without alarming.
- `badge-aurore` to distinguish ("majeur", "premium", "nouveau").

## 3. Score bar (visual progress)

```html
<div style="display:flex; align-items:center; gap:0.75rem;">
  <div class="score-bar" style="flex:1;">
    <div class="score-fill" style="width: 72%"></div>
  </div>
  <span style="font-size:0.85rem; font-weight:600; min-width:32px; text-align:right;">7.2</span>
</div>
```

Variants: `score-fill.aurore` (purple), `score-fill.red` (alert).

## 4. Status LED (live, degraded, alert)

```html
<span class="led on" aria-label="En ligne"></span>      <!-- Cirrus -->
<span class="led live" aria-label="Live"></span>        <!-- Cirrus pulse -->
<span class="led warn" aria-label="Dégradé"></span>     <!-- Haboob beige -->
<span class="led alert" aria-label="Hors ligne"></span> <!-- Sirocco pulse -->
<span class="led" aria-label="Inconnu"></span>          <!-- Stratus -->
```

LEDs follow the same hierarchy as badges: Cirrus for OK, Haboob for soft warning, Sirocco for critical incidents only.

## 5. Kopo spinner (loading)

```html
<div class="kopo-spinner" aria-label="Chargement"></div>
```

40×40 by default. For a custom size:
```html
<div class="kopo-spinner" style="width:24px; height:24px;"></div>
```

## 6. Skeleton (loading placeholder)

```html
<div class="skel" style="height:1rem; width:60%;"></div>
<div class="skel" style="height:1.5rem; width:40%; margin-top:0.5rem;"></div>
```

Used inside a card waiting for its real data:
```html
<div class="kopo-card kopo-card-padded">
  <div class="skel" style="height:0.7rem; width:30%;"></div>
  <div class="skel" style="height:1.8rem; width:50%; margin-top:0.5rem;"></div>
</div>
```

## 7. Filter bar (dense filter form)

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

The grid adapts automatically (`minmax(140px, 1fr)`). Stacks in narrow columns.

## 8. Data table (dense table)

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
    <!-- repeat -->
  </tbody>
</table>
```

Modifier: `data-table.compact` for tighter rows.

## 9. Listing card (media + title + price card, Itaycan style)

```html
<div class="listing-card">
  <div class="visual">
    <!-- image, icon, or Halo flat fill -->
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

Place inside a `.listing-grid` container which adapts the column count to the width.

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
    <!-- page content -->
  </div>
</div>
```

`active` on the current link. Below `900px`, the sidebar moves above the content as a full-width block.

## 11. Callout / Alert (strict Kopo palette)

```html
<!-- Info / context / note (Cirrus border and icon) -->
<div class="callout info">
  <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><circle cx="12" cy="8" r=".5"/></svg>
  <div class="body">
    <strong>À noter</strong>
    Cette information complète le contexte.
  </div>
</div>

<!-- Tip / suggestion (Aurore border and icon) -->
<div class="callout tip"> ... </div>

<!-- Soft warning (Haboob-brown border, light Haboob background) -->
<div class="callout warn"> ... </div>

<!-- Critical error (Sirocco border and icon — rare use) -->
<div class="callout error"> ... </div>
```

Four variants only. No separate `success`: a positive event belongs to `info`. Green does not exist in the Kopo palette, and that is deliberate.

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

## 13. Code block (for documentation)

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

Inline:
```html
Lancez la commande <span class="code-inline">systemctl status kopo</span> pour vérifier.
```

## 14. Section with 12-column grid (Kopo Download style)

```html
<section id="{{ID}}" class="container" style="padding: 4rem 0;">
  <span class="section-eyebrow">{{LABEL_UPPERCASE}}</span>
  <h2 style="font-size:1.75rem; font-weight:700; letter-spacing:-0.02em;">{{TITLE}}</h2>
  <div class="cirrus-bar"></div>

  <div class="grid-12" style="gap:32px; margin-top:24px;">
    <div class="col-span-7">
      <p>{{MAIN_PARAGRAPH}}</p>
      <a href="#" class="btn btn-primary">{{CTA}}</a>
    </div>
    <div class="col-span-5">
      <!-- visual, code block, callout, or preview -->
    </div>
  </div>
</section>
```

Alternate with `<section class="section-alt">` (background #F7F8FA) for rhythm.

## 15. Page title row (title + toolbar actions)

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

## Golden rules for functional pages

- **Density is fine, clutter is not.** The brand's breathing room still applies: use generous `gap` and `padding` in containers, even with dense content.
- **A single active Cirrus per viewport**: if there are KPI cards + a primary button + a live LED, choose which one deserves Cirrus; the rest stays neutral.
- **No off-palette color.** No green, no amber, no navy, no red other than Sirocco. Kopo blue means "good", period.
- **Sirocco rare and intentional**: only for critical incidents (service down, loss). Mere high latency → Haboob, not Sirocco.
- **Tabular numbers**: every numeric column must use `font-variant-numeric: tabular-nums` (already on `.data-table .num`).
- **Loading states**: no blank page — always skeletons or a spinner during fetch.
- **No full-width table without `overflow-x: auto`** on mobile (already handled by `.data-table` at the breakpoint).
- **Hero optional**: on an internal app page, the `page-title-row` with h1 + Cirrus bar is enough. Only use a Halo hero when the page deserves a strong editorial accent (the app's home page, for example).

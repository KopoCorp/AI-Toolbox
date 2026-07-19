# Catalogue des sections Kopo (snippets HTML)

Ce fichier contient les **briques HTML prêtes à coller** dans les templates. Chaque snippet respecte la charte V1.4 (palette, typographie, espacement, accentuation unique). Substituer les placeholders `{{...}}` aux vraies valeurs.

## 1. Carte de feature (3 cartes en grille — pour `{{FEATURES_CARDS}}`)

```html
<article class="service-card reveal delay-1">
  <div class="icon-circle">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <!-- SVG inline ou icône Lucide. Stroke 2px, jamais filled. -->
      {{ICON_SVG}}
    </svg>
  </div>
  <div class="num">01</div>
  <h3>{{FEATURE_TITLE}}</h3>
  <p>{{FEATURE_DESC}}</p>
  <a href="#" class="arrow-link">En savoir plus
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path d="M5 12h14M13 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
    </svg>
  </a>
</article>
```

Reproduire 3 fois avec `delay-1`, `delay-2`, `delay-3` et incrémenter le numéro (`01`, `02`, `03`).

## 2. Bloc infra-feature (sur gradient Halo — pour `{{INFRA_FEATURES}}`)

```html
<div class="infra-feature reveal delay-1">
  <div class="icon-circle">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      {{ICON_PATH}}
    </svg>
  </div>
  <h3>{{INFRA_TITLE}}</h3>
  <p>{{INFRA_DESC}}</p>
</div>
```

## 3. Bloc statistique (pour `{{STATS_BLOCKS}}`)

```html
<div class="stat-block reveal delay-1">
  <div class="stat-value"><span data-count="{{NUM}}" data-decimals="0">0</span><span class="unit">{{UNIT}}</span></div>
  <div class="stat-label">{{LABEL}}</div>
</div>
```

Le compteur s'anime au scroll. `data-decimals` accepte 0, 1 ou 2.

## 4. Card de pricing (pour `{{PRICING_CARDS}}`)

Carte standard :

```html
<div class="price-card reveal delay-1">
  <span class="price-tier">{{TIER_NAME}}</span>
  <div class="price-amount">{{AMOUNT}}<span class="currency">€</span><span class="period"> / mois</span></div>
  <p class="price-desc">{{DESCRIPTION}}</p>
  <ul class="price-features">
    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> {{FEATURE_1}}</li>
    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> {{FEATURE_2}}</li>
    <li class="muted"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line></svg> {{FEATURE_DESACTIVE}}</li>
  </ul>
  <a href="#cta" class="btn btn-outline">{{CTA_LABEL}}</a>
</div>
```

Carte mise en avant : ajouter la classe `featured` et utiliser `btn-primary`. Une SEULE carte `featured` par page (règle d'unicité d'accent).

```html
<div class="price-card featured reveal delay-2">
  <!-- ... pareil ... -->
  <a href="#cta" class="btn btn-primary">{{CTA_LABEL}}</a>
</div>
```

## 5. Item de FAQ (accordéon natif — pour `{{FAQ_ITEMS}}`)

```html
<details class="faq-item reveal">
  <summary class="faq-question">
    {{QUESTION}}
    <svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
  </summary>
  <div class="faq-answer">{{ANSWER}}</div>
</details>
```

## 6. Section de contenu pour page interne (pour `{{CONTENT_SECTIONS}}`)

```html
<section id="{{ID}}">
  <div class="container">
    <span class="section-label">{{LABEL_UPPERCASE}}</span>
    <h2>{{TITLE}}</h2>
    <div class="cirrus-bar"></div>
    <div class="grid-12" style="gap:32px;margin-top:24px;">
      <div class="col-span-7">
        <p>{{PARAGRAPHE}}</p>
        <a href="{{HREF}}" class="btn btn-primary">{{CTA}}</a>
      </div>
      <div class="col-span-5">
        <!-- visuel, capture, ou bloc info -->
      </div>
    </div>
  </div>
</section>
```

Alterner avec `<section class="section-alt">` pour le fond `#F7F8FA` (Stratus dilué).

## 7. Colonne de footer (pour `{{FOOTER_COLUMNS}}`)

```html
<div>
  <h4>{{HEADING}}</h4>
  <ul>
    <li><a href="{{HREF}}">{{LINK_1}}</a></li>
    <li><a href="{{HREF}}">{{LINK_2}}</a></li>
  </ul>
</div>
```

3 colonnes après le bloc brand suffisent (la grille footer est en `1.5fr 1fr 1fr 1fr`).

## 8. SVG inline · icônes courantes (style Lucide, stroke 2px)

Toutes les icônes ci-dessous prennent `currentColor`, donc pilotables par CSS.

```html
<!-- mail -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,6 12,13 2,6"/></svg>

<!-- cloud -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19a4.5 4.5 0 100-9h-1.8A7 7 0 104 14.9"/></svg>

<!-- shield -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l8 4v6c0 5-3.5 9.5-8 10-4.5-.5-8-5-8-10V6l8-4z"/></svg>

<!-- lock -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>

<!-- server -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="8" rx="1"/><rect x="2" y="13" width="20" height="8" rx="1"/><line x1="6" y1="7" x2="6.01" y2="7"/><line x1="6" y1="17" x2="6.01" y2="17"/></svg>

<!-- check -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>

<!-- arrow-right -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>

<!-- terminal -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>

<!-- database -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>

<!-- globe -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15 15 0 010 20M12 2a15 15 0 000 20"/></svg>
```

Pour toute autre icône, utiliser le set Lucide complet : https://lucide.dev/icons/

## 9. Règles d'or pour assembler une page Kopo

- **Une seule** carte/bouton/élément en `Cirrus` plein par viewport.
- **Manifesto facultatif** — l'inclure quand le ton est éditorial ; le retirer pour les produits techniques purs.
- **Stats** : 3 ou 4 blocs maximum, valeurs animées au scroll via `data-count`.
- **Pricing** : 3 paliers Découverte / Standard (`featured`) / Avancé. Si un seul prix, utiliser une carte centrée pleine largeur.
- **FAQ** : 4 à 6 questions courantes. Plus → externaliser dans une page FAQ dédiée.
- **CTA band** : toujours finir par un bandeau qui ramène vers l'action principale (essayer, contact, démo).
- **Footer Nimbus 4 colonnes** : brand + 3 colonnes de liens. Ne pas surcharger.

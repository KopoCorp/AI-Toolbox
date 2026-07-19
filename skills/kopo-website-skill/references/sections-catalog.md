# Kopo section catalog (HTML snippets)

This file contains the **ready-to-paste HTML bricks** for the templates. Every snippet follows the V1.4 brand rules (palette, typography, spacing, single accent). Replace the `{{...}}` placeholders with real values. User-facing strings stay in French (Kopo sites are French).

## 1. Feature card (3 cards in a grid — for `{{FEATURES_CARDS}}`)

```html
<article class="service-card reveal delay-1">
  <div class="icon-circle">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <!-- Inline SVG or Lucide icon. 2px stroke, never filled. -->
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

Repeat 3 times with `delay-1`, `delay-2`, `delay-3` and increment the number (`01`, `02`, `03`).

## 2. Infra-feature block (on the Halo gradient — for `{{INFRA_FEATURES}}`)

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

## 3. Statistic block (for `{{STATS_BLOCKS}}`)

```html
<div class="stat-block reveal delay-1">
  <div class="stat-value"><span data-count="{{NUM}}" data-decimals="0">0</span><span class="unit">{{UNIT}}</span></div>
  <div class="stat-label">{{LABEL}}</div>
</div>
```

The counter animates on scroll. `data-decimals` accepts 0, 1 or 2.

## 4. Pricing card (for `{{PRICING_CARDS}}`)

Standard card:

```html
<div class="price-card reveal delay-1">
  <span class="price-tier">{{TIER_NAME}}</span>
  <div class="price-amount">{{AMOUNT}}<span class="currency">€</span><span class="period"> / mois</span></div>
  <p class="price-desc">{{DESCRIPTION}}</p>
  <ul class="price-features">
    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> {{FEATURE_1}}</li>
    <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> {{FEATURE_2}}</li>
    <li class="muted"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line></svg> {{FEATURE_DISABLED}}</li>
  </ul>
  <a href="#cta" class="btn btn-outline">{{CTA_LABEL}}</a>
</div>
```

Highlighted card: add the `featured` class and use `btn-primary`. ONE `featured` card per page only (single-accent rule).

```html
<div class="price-card featured reveal delay-2">
  <!-- ... same ... -->
  <a href="#cta" class="btn btn-primary">{{CTA_LABEL}}</a>
</div>
```

## 5. FAQ item (native accordion — for `{{FAQ_ITEMS}}`)

```html
<details class="faq-item reveal">
  <summary class="faq-question">
    {{QUESTION}}
    <svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
  </summary>
  <div class="faq-answer">{{ANSWER}}</div>
</details>
```

## 6. Content section for internal pages (for `{{CONTENT_SECTIONS}}`)

```html
<section id="{{ID}}">
  <div class="container">
    <span class="section-label">{{LABEL_UPPERCASE}}</span>
    <h2>{{TITLE}}</h2>
    <div class="cirrus-bar"></div>
    <div class="grid-12" style="gap:32px;margin-top:24px;">
      <div class="col-span-7">
        <p>{{PARAGRAPH}}</p>
        <a href="{{HREF}}" class="btn btn-primary">{{CTA}}</a>
      </div>
      <div class="col-span-5">
        <!-- visual, screenshot, or info block -->
      </div>
    </div>
  </div>
</section>
```

Alternate with `<section class="section-alt">` for the `#F7F8FA` background (diluted Stratus).

## 7. Footer column (for `{{FOOTER_COLUMNS}}`)

```html
<div>
  <h4>{{HEADING}}</h4>
  <ul>
    <li><a href="{{HREF}}">{{LINK_1}}</a></li>
    <li><a href="{{HREF}}">{{LINK_2}}</a></li>
  </ul>
</div>
```

3 columns after the brand block are enough (the footer grid is `1.5fr 1fr 1fr 1fr`).

## 8. Inline SVG · common icons (Lucide style, 2px stroke)

All icons below use `currentColor`, so they can be driven by CSS.

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

For any other icon, use the full Lucide set: https://lucide.dev/icons/

## 9. Golden rules for assembling a Kopo page

- **A single** solid-`Cirrus` card/button/element per viewport.
- **Manifesto optional** — include it when the tone is editorial; drop it for purely technical products.
- **Stats**: 3 or 4 blocks maximum, values animated on scroll via `data-count`.
- **Pricing**: 3 tiers Découverte / Standard (`featured`) / Avancé. If there is a single price, use one centered full-width card.
- **FAQ**: 4 to 6 common questions. More → move to a dedicated FAQ page.
- **CTA band**: always end with a band leading back to the main action (try, contact, demo).
- **Nimbus footer, 4 columns**: brand + 3 link columns. Don't overload it.

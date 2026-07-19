---
name: kopo-website-skill
description: Builds websites in the visual identity of Kopo (kopo.systems), French sovereign infrastructure based in Brest. Trigger on any request for a site, landing page, product page, internal page, dashboard, doc, web app or legal page for Kopo or its sub-brands (Kopo Mail, Cloud, Drive, Kosmos, Itaycan, Monitor, Docs). Covers three styles. One, KopoHome-style showcase landing with immersive hero, interactive hanging Kobot, Halo gradients, pricing, FAQ. Two, Kopo Download-style internal page, sober, 12-column grid, Cirrus bars, for docs and portals. Three, Itaycan-style functional application with KPIs, filter bar, data table, Kopo-palette badges, callouts. Provides official assets, CSS, JS, four HTML templates (landing, internal, app, legal), catalogs, checklist, Python scaffolder. Also trigger on implicit phrasings, often in French, such as « monte-moi un dashboard », « page de doc pour notre API », « landing pour X.kopo.systems ».
---

# Kopo Website Skill

You are the expert who assembles websites fully compliant with the Kopo V1.4 brand guidelines. This skill packages **everything** needed to deliver a professional Kopo site in one command: the assets, the shared code, two template families, a section catalog, a scaffolding script, and a validation checklist.

Note: Kopo websites are written in French — keep all user-facing copy (headings, buttons, microcopy) in French unless the brief says otherwise.

## When to use this skill

On every request involving a Kopo website, whether explicit ("build me a Kopo Cloud landing") or implicit ("I need a page to present our new monitoring service"). Also for legal pages (legal notices, privacy, ToS) that must stay within the same visual skeleton.

## Skill tree

```
kopo-website-skill/
├── SKILL.md                              ← this file
├── README.md
├── assets/
│   ├── logos/
│   │   ├── KopoLogo.png                  ← full Kobot (for kobot-mini)
│   │   ├── kopologo128.png               ← favicon and exports
│   │   ├── kopologo.ico                  ← favicon
│   │   ├── kopologo-longarm.png          ← Kobot with extra-long cable (hanging hero)
│   │   └── kopologo-transparent.png      ← no background, for overlays
│   ├── illustrations/
│   │   ├── banniere-jour.jpg             ← Kobot workshop banner, day
│   │   └── banniere-nuit.jpg             ← Kobot workshop banner, night
│   └── fonts/
│       ├── Satoshi-Variable.woff2
│       └── Satoshi-VariableItalic.woff2
├── css/
│   ├── shared.css                        ← tokens + reset + nav + footer + Kobot + buttons + reveal
│   ├── landing.css                       ← rich marketing sections (Aube hero, manifesto, pricing, FAQ, CTA band)
│   └── components.css                    ← functional components (KPI, badges, score, spinner, skeleton, filter, table, sidebar, callout)
├── js/
│   └── shared.js                         ← interactive Kobot + reveal + nav + counters + drawer
├── templates/
│   ├── landing/index.html                ← KopoHome style (marketing showcase)
│   ├── internal/index.html               ← Kopo Download style (portal / doc, 12-col grid, dense)
│   ├── app/index.html                    ← Itaycan style (functional app: KPIs, listings, filters)
│   └── legal/index.html                  ← legal notices / privacy / ToS
├── references/
│   ├── sections-catalog.md               ← HTML snippets for landings (hero, manifesto, pricing, FAQ, CTA band)
│   ├── functional-catalog.md             ← snippets for internal pages and apps (KPI, badges, tables, listings, sidebar)
│   ├── design-excellence.md              ← anti "AI look": two-pass process, microcopy, UX, motion craft
│   ├── kobot-animation.md                ← animatable SVG Kobot: canonical anatomy, gestures/states, invariants
│   └── checklist.md                      ← validation before delivery
└── scripts/
    └── new_site.py                       ← Python scaffolder (JSON config → complete site)
```

## Choosing the right template

| Typical request | Template | CSS to include | Reference | Why |
|---|---|---|---|---|
| Product landing (Mail, Cloud, Drive, Kosmos) | `landing/` | shared + landing | KopoHome | Immersive hero + hanging Kobot + pricing + FAQ + CTA band |
| Corporate landing (showcase) | `landing/` | shared + landing | KopoHome | All animated marketing sections |
| Doc page / resource portal | `internal/` | shared + components | Kopo Download | 12-column grid + Cirrus bars + sober + dense |
| Internal app / dashboard / monitoring | `app/` | shared + components | Itaycan | Sticky header + KPIs + filter bar + listings + sidebar |
| Market-watch page / dynamic listings | `app/` | shared + components | Itaycan | Listing cards, badges, HTMX-ready skeletons |
| Legal notices / privacy / ToS | `legal/` | shared | (new) | Single 780px-max column, H2 hierarchy + mini Cirrus bar |

## Generation method (two paths)

### Path A · Direct generation by Claude (recommended for custom cases)

1. **Read** `references/checklist.md` to load all constraints.
2. **Read** `references/design-excellence.md` and produce the two-pass plan (hero thesis, signature element, critique) BEFORE writing any HTML.
3. **Read** `references/sections-catalog.md` to pick the section snippets you need.
4. **Copy** `css/shared.css`, `css/landing.css` (if landing), `js/shared.js` and `assets/` into the output folder.
5. **Start** from the matching HTML template (`templates/landing/index.html` or other).
6. **Fill** the `{{...}}` placeholders with real content, following the brand rules (a single Cirrus accent per viewport, hierarchy by weight, etc.).
7. **Validate** every checklist item before presenting the result, then run the final self-critique from `design-excellence.md`.

### Path B · Python scaffolder (recommended for standard cases)

For a complete landing site from a structured brief:

1. Write a `config.json` describing the site (see the docstring of `scripts/new_site.py` for the full schema).
2. Run:
   ```bash
   python /path/to/kopo-website-skill/scripts/new_site.py --config config.json --out ./my-site
   ```
3. The script copies assets, CSS, JS and generates `index.html` with all sections (hero, manifesto, features, Halo infra, stats, pricing, FAQ, CTA, footer).
4. Check visually, adjust manually if needed.

The scaffolder also accepts `template: "legal"` to generate a legal notices / privacy page.

## Golden rules — NEVER break these

1. **A single solid-Cirrus element per viewport** — it marks the most important thing (the main CTA, the recommended pricing card, the star statistic).
2. **Satoshi only.** Roboto as system fallback, never as an aesthetic choice.
3. **No justified text.** Left-aligned by default. Centering reserved for heroes and short taglines.
4. **Invariant Kobot proportions**: 22% for the eye zone, 7% for the white pupil, 7% for the cable. Changing any of them breaks the identity.
5. **No gratuitous ornament**: no superfluous rounded borders, no glow, no neon, no heavy shadow. Sobriety IS the identity.
6. **60–70% whitespace minimum.** Breathing room is not missing content — it is the brand.
7. **Nimbus footer always** (background `#141A1E`, Cumulus / Stratus text), with the copyright and the notice « Kopo® est une marque déposée ».

## Colors (quick reference — details in `references/sections-catalog.md`)

| Name | HEX | Usage |
|---|---|---|
| Cirrus | `#57B8FF` | Single accent, primary CTAs |
| Virga | `#85BAFF` | Support, hover |
| Arcus | `#B2DBFF` | Large soft surfaces |
| Stratus | `#BCC8D2` | Borders, disabled |
| Nimbus | `#141A1E` | Typography, footer |
| Haboob | `#F9ECE2` | Occasional warmth |
| Cumulus | `#FFFFFF` | Main background |
| Vesper | `#23255D` | Halo, gradients |
| Aurore | `#504A97` | Halo, gradients |
| Sirocco | `#E6213A` | Kobot's eyelid, alerts ONLY |

## Atmospheric gradients (already coded in landing.css)

- **Aube** (hero): Cirrus → Haboob, linear 90°
- **Brume** (manifesto): centered radial Arcus
- **Halo** (infra): Vesper → Aurore, linear 160°
- **Encre** (stats): Nimbus → Vesper, linear 90°
- **Orage** (CTA band): Cirrus → Arcus, linear 135°

One gradient per composition. Never on borders.

## Typical workflow — answering "build me a landing for Kopo X"

1. Identify the service (name, tagline, 3 main features, infra, pricing, FAQ).
2. Pick the template: `landing/` in 95% of cases.
3. If the user gave a precise brief → generate directly.
4. Otherwise → ask **at most 3 questions** to get: service name, baseline, 3 flagship features.
5. Build the `config.json` or edit the template directly.
6. Run the scaffolder OR write the final HTML manually.
7. Present the site with `present_files` or by pointing to the output folder.
8. Offer the checklist as an optional audit.

## Technical notes

- The **JPG banners** are compressed to ~400 KB each (quality 82, max 2400px) — already done in the skill, do not recompress.
- The **Satoshi font** is loaded locally via `@font-face` AND as a Fontshare CDN fallback, for robustness.
- The **interactive Kobot** requires the `kopologo-longarm.png` image (extra-long cable) on the hero for the hanging render.
- The **Kobot can also be embedded as an animatable SVG** (blink, wave, loading, descent, error expressions…): canonical anatomy and full method in `references/kobot-animation.md`. Prefer it whenever the Kobot must react to a state (loading, 4xx/5xx errors, maintenance); the PNGs remain for static uses (nav, footer, exports).
- **Icons** are inline SVG, 2px stroke, Lucide style. The scaffolder embeds the most common ones; for others, copy from https://lucide.dev/icons/.
- The **scaffolder** depends only on the Python stdlib (no pip install needed).

## When to route to the `kopo-brand-skill` instead

The `kopo-brand-skill` covers the general visual identity (PowerPoint, A4, brand book). If the request is about:
- a presentation, slides → `kopo-brand-skill`
- an A4 document (report, brand book) → `kopo-brand-skill`
- a website, an HTML page, a landing → **here**

# Kopo Web compliance checklist

Check BEFORE delivering a Kopo site. If any item fails, fix it before presenting.

## Colors

- [ ] Exact colors used (precise HEX, no approximation)
- [ ] **A single** solid-Cirrus element per viewport (the most important one)
- [ ] No secondary color (Vesper / Aurore / Sirocco) combined with another secondary
- [ ] Sirocco used ONLY for alerts / the Kobot's eyelid — never decorative
- [ ] Haboob used sparingly to warm a surface, never as a large flat fill
- [ ] On functional pages: semantic badges from the Kopo palette for operational statuses, no decorative colored badges

## Typography

- [ ] Satoshi loaded locally (WOFF2) + Fontshare CDN fallback
- [ ] No font other than Satoshi (Roboto only as system fallback)
- [ ] Hierarchy built with weight (Bold vs Regular), not size
- [ ] Letter-spacing -0.02em on headings
- [ ] Left-aligned by default
- [ ] No justified text (absolute rule)
- [ ] Max-width 60ch on paragraphs for readability

## Layout

- [ ] 12-column grid respected on internal pages
- [ ] Container max-width 1440px (marketing) or 1200px (internal)
- [ ] Generous section padding: 9rem on landing, 5rem on internal
- [ ] 60–70% whitespace minimum (breathing room > filling)
- [ ] Responsive margins via `clamp()` or the `--container-px` variable

## Logo & Kobot

- [ ] Invariant Kobot proportions respected (22% eye, 7% pupil, 7% cable)
- [ ] Sirocco only for the eye ring
- [ ] Interactive Kobot (`data-interactive`) on the hero — pupil follows the mouse
- [ ] On landing hero: hanging Kobot (`kobot-longarm` + `kobot-swing-anchor`)
- [ ] Mini-kobot in nav and footer (`kobot-mini`, 40px)

## Components

- [ ] Cirrus bar (180×3px) under every H2 on internal pages
- [ ] Buttons: `btn-primary` (Nimbus → hover Cirrus), `btn-ghost` (Nimbus outline → hover Cirrus)
- [ ] Cards with `--stratus-soft` border, hover → Cirrus border + 6px lift
- [ ] Lucide icons, 2px stroke, sizes 16/20/24/32/64/80 only
- [ ] Section eyebrow in uppercase Cirrus, letter-spacing 0.18em

## Animations & interactivity

- [ ] `reveal` + `IntersectionObserver` on main blocks
- [ ] Nav switches to `scrolled` (blur + background) after 30px of scroll
- [ ] Animated counters (`data-count`) on scroll
- [ ] Kobot pendulum draggable (mobile + desktop)
- [ ] Burger + fullscreen drawer on mobile (<800px)
- [ ] Standard transitions: 0.2s for hover, 0.4s for reveal, 0.8s for long reveal

## Animated Kobot (if embedded as SVG — see `kobot-animation.md`)

- [ ] Canonical anatomy respected (IDs, articulation groups, `clip-oeil` + `fenetre` clips)
- [ ] No deformation of the Kobot: only its environment and limbs move
- [ ] Vertical animations relative to `var(--drop)`; combinable states tested together
- [ ] Blink via clipped eyelids (r=118), never by deforming the eye
- [ ] Cable vertical, extended beyond the window when swinging
- [ ] `prefers-reduced-motion` → static Kobot, eyes open
- [ ] Every animation has contextual MEANING (system state, user reaction) — no gratuitous motion
- [ ] One animated Kobot per page

## Footer

- [ ] Nimbus background, Cumulus / Stratus text
- [ ] 4-column grid (1.5fr 1fr 1fr 1fr) → 2 columns on tablet → 1 on mobile
- [ ] Column headings: 0.72rem uppercase, letter-spacing 0.18em, Stratus
- [ ] Copyright at the bottom with border-top 1px rgba(255,255,255,0.12)
- [ ] Notice « © {YEAR} Kopo® · Tous droits réservés. Kopo est une marque déposée. »

## Accessibility

- [ ] `lang="fr"` on `<html>`
- [ ] `aria-label` on decorative icons and buttons without text
- [ ] `aria-hidden="true"` on decorative SVGs
- [ ] Sufficient contrast between Nimbus and light backgrounds (natively verified)
- [ ] Visible focus on links and buttons
- [ ] `<meta name="viewport">` present

## Responsive

- [ ] 800px breakpoint: nav becomes burger, hero switches to 1 column
- [ ] 768px breakpoint: 12-col grid → all columns `span 12`
- [ ] 480px breakpoint: footer in 1 column, stats in 1 column
- [ ] No horizontal overflow (check `overflow-x: hidden` on body)

## Performance

- [ ] JPG banners compressed (~400 KB max, quality 82)
- [ ] Satoshi fonts with `font-display: swap`
- [ ] No heavy JS framework
- [ ] Images with `loading="lazy"` except the hero
- [ ] `backdrop-filter` only on the nav and the drawer

## Functional pages (internal and app templates)

- [ ] `components.css` imported alongside `shared.css`
- [ ] Header as `.nav-sticky` (simple sticky, no fancy blur)
- [ ] If data-dense: `.data-table` with distinct `<thead>`, `.num` on numeric columns
- [ ] Operational statuses via `.kopo-badge.badge-virga` (OK), `.badge-haboob` (degraded), `.badge-sirocco` (critical incident) — no green, no amber, never off-palette
- [ ] Visual LED for live states: `.led.on / .live / .warn / .alert`
- [ ] Loading states via `.skel` or `.kopo-spinner`, never a blank page
- [ ] Score bars (`.score-bar` + `.score-fill`) for progress / measurements
- [ ] Callouts (`.callout.info/warn/error/success`) for important messages
- [ ] Filter bar (`.filter-bar`) with labels in uppercase Stratus 0.7rem
- [ ] Tabular numbers (`font-variant-numeric: tabular-nums`) on numeric columns
- [ ] Mobile: tables in `overflow-x: auto` (already handled by `.data-table` at the 768px breakpoint)
- [ ] KPI grid: 4 cards on desktop, 2 on tablet, 1 on mobile

## Legal

- [ ] Legal notices reachable from the footer
- [ ] Privacy policy reachable from the footer
- [ ] For KoBot Discord: ToS + Privacy mandatory
- [ ] Kopo copyright + registered trademark mentioned

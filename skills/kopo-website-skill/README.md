# Kopo Website Skill

Agent skill for generating websites compliant with the Kopo V1.4 brand guidelines.

## Quick start

### With an AI agent
Just state your need: "build me a landing for Kopo Cloud", "generate a legal notices page for kopo.systems", etc. The agent will detect this skill and apply it automatically.

### CLI (Python scaffolder)
```bash
python scripts/new_site.py --config exemple-config.json --out ./my-site
```

## Architecture

- `assets/`: official logos, illustrations, fonts
- `css/`: `shared.css` (all pages) + `landing.css` (marketing sections) + `components.css` (functional components)
- `js/`: `shared.js` (interactive Kobot, reveal, nav, mobile drawer)
- `templates/`: four variants (`landing/`, `internal/`, `app/`, `legal/`)
- `references/`: section catalogs + compliance checklist + design/animation method guides
- `scripts/`: Python scaffolder `new_site.py`

## Coexisting styles

| Style | Reference in the ecosystem | Template |
|---|---|---|
| Rich marketing, immersive hero | KopoHome (kopo.systems) | `landing/` |
| Sober, dense, 12-column grid | Kopo Download (download.kopo.systems) | `internal/` |
| Functional app: KPIs, listings, filters | Itaycan | `app/` |
| Single 780px column, H2 hierarchy | (new) | `legal/` |

## Compliance

Before delivery, go through `references/checklist.md`. The golden rules:

1. A single solid-Cirrus element per viewport
2. Satoshi exclusively, Roboto system fallback
3. Left-aligned, never justified
4. Invariant Kobot proportions (22% / 7% / 7%)
5. 60–70% whitespace minimum
6. Nimbus footer, always

## Licenses

- Satoshi · Indian Type Foundry
- Lucide icons · ISC
- Kopo assets · Kopo internal use only, registered trademark

Brest, France · contact@kopo.systems

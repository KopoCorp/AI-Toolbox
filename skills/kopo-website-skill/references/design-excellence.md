# Design Excellence — avoid the "AI look", aim for studio quality

Distilled from the [anthropics/frontend-design](https://github.com/anthropics/skills) and [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) skills, adapted to the Kopo V1.4 brand. The brand rules (colors, Satoshi, Kobot) are non-negotiable — this file governs everything the brand does not fix: composition, motion, content, finishing touches.

## 1 · Two-pass process (mandatory for any custom site)

### Pass 1 — Design plan (before writing any HTML)

Write a mini-plan (5–10 lines):

- **Hero thesis**: open with the most characteristic thing in the subject's world. For a monitoring service → live data; for Kopo Mail → the arriving envelope; for a doc → search. The hero is not "title + subtitle + CTA" by default — it is an argument.
- **Signature element**: ONE unique element, specific to the brief, that no other Kopo site has (a visualization, a Kobot interaction, a novel section structure). Concentrate the boldness there, keep everything else sober — consistent with the "one solid Cirrus per viewport" rule.
- **Layout in one sentence per section** + ASCII wireframe if complex.

### Pass 2 — Critique before coding

Re-read the plan and ask: "is any element a default choice I would make for any similar project?" If yes, rework it. Only then start coding.

## 2 · "AI slop" anti-patterns to ban

- Generic centered hero (title/subtitle/two-buttons) with no idea specific to the subject.
- Identical stacked sections (icon + title + paragraph × 6). Vary the rhythm: one dense section, one airy, one full-width.
- Effects scattered everywhere (every block moving differently) → orchestrate a few deliberate moments instead of sprinkling.
- Decorative structure: numbering, dividers, labels only when order or relationship carries real meaning.
- Emoji as icons. Always Lucide SVG, 2px stroke.
- Hollow marketing copy ("Innovative solutions for your business"). Be specific: numbers, names, concrete verbs.

## 3 · Writing IS design (microcopy)

- Write from the user's side of the screen: name things by what people control and recognize.
- Active voice on actions: « Enregistrer les modifications », not « Soumettre ».
- Consistent vocabulary across a whole flow (don't alternate « espace » / « workspace » / « projet »).
- Conversational register, specific rather than clever. Sentence case (no English-style Title Case).
- Errors and empty states = directional moments: say what to do next (« Réessayer », « Créer votre premier projet »), never a bare statement of failure.
- Site copy stays in French (Kopo's audience), even though these instructions are in English.

## 4 · UX — rules complementing the checklist

### Forms
- Visible label above the field, never placeholder-only. Associated `for` attribute.
- Semantic types (`email`, `tel`, `url`) + `inputmode` for the mobile keyboard + browser autofill not blocked.
- Validate on blur, error below the affected field (not at the top of the form), `role="alert"` on the message.
- During an async submit: disabled button + loading state, then visible confirmation (toast or check).
- Required fields marked. Show/hide toggle on passwords.

### Interactions
- Any destructive action → confirmation first.
- Touch targets ≥ 44×44 px, ≥ 8 px gap between adjacent targets.
- Immediate pressed state (e.g. `scale(0.98)`), disabled with reduced opacity + `cursor: not-allowed`.
- Browser history respected (deep links, URL reflecting state for apps).

### Content
- Line height 1.5–1.75 on body text; body ≥ 16 px on mobile.
- Modular type scale (no arbitrary sizes) — already enforced by shared.css, do not bypass it.

## 5 · Motion craft (beyond the standard 0.2s/0.4s/0.8s durations)

- **Hover**: displacement ≤ 2 px (it must read as feedback, not motion). Never animate width/height/margin — only `transform` and `opacity`.
- **Scroll reveals**: y offset of 8–16 px max — an appearance, not a slide.
- **Stagger**: maximum ~8 staggered children, 20–40 ms delay per item. Beyond that, the last ones feel laggy.
- **Exits faster than entrances** (≤ 250 ms) so navigation stays snappy.
- **Parallax**: decorative layers only, never on text or controls; 5–15% delta.
- **Split-text animation**: reserved for short headlines (< 8 words), never on a paragraph.
- **Skeletons**: gradient sweep (already how `.skel` works), loop < 1.5 s — no opacity pulsing.
- **`prefers-reduced-motion`**: every reveal/pendulum/counter must have a static fallback. No scroll-jacking, ever.
- The Kobot's pendulum and pupil are the only permanently "alive" elements allowed. Don't give them competitors.

## 6 · Quality floor (unannounced, always present)

Responsive down to mobile, visible keyboard focus everywhere, `prefers-reduced-motion` respected, AA contrast (4.5:1 normal text — careful with Stratus text on Cumulus, reserved for large labels), 100% keyboard navigation with logical tab order, semantic HTML (`nav`, `main`, `article`), skip-link on dense pages.

## 7 · Final self-critique

Before delivering, look at the render (screenshot or browser) and remove any decoration that doesn't serve the brief. The question is not "what can I add?" but "what can I remove without losing anything?". Sobriety IS the Kopo identity.

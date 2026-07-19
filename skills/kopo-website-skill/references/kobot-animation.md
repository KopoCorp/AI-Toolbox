# Animated Kobot — SVG methodology

The Kobot can be embedded as an **animatable vector SVG** instead of the static PNGs. This file gives the canonical anatomy and the method for building compliant animations. **Do not invent another structure**: every animation is built on this anatomy.

## 1 · Canonical SVG anatomy

Every component of the logo is an independent, identified SVG element, grouped by articulation. This decomposition is what makes motion possible without ever touching the shapes.

```html
<svg id="kobot-svg" viewBox="0 0 1024 1424" xmlns="http://www.w3.org/2000/svg"
     role="img" aria-label="Kobot, mascotte Kopo">
  <defs>
    <!-- Eye clip SLIGHTLY wider (r=118) than the Sirocco ring (r=112.5)
         so the eyelids cover it without a red fringe -->
    <clipPath id="clip-oeil"><circle cx="512" cy="512" r="118"/></clipPath>
    <!-- The "window": same shape as the background, clips the suspension -->
    <clipPath id="fenetre"><rect x="0" y="0" width="1024" height="1024" rx="512" ry="512"/></clipPath>
  </defs>

  <!-- Background: rounded rect. rx=512 → perfect circle, smaller rx → rounded square -->
  <rect id="fond" x="0" y="0" width="1024" height="1024" rx="512" ry="512" fill="#57B8FF"/>

  <g id="suspension" clip-path="url(#fenetre)">           <!-- pivot: 512,0 -->
    <!-- Cable extended ABOVE the window (y=-200): never a gap at the top while swinging -->
    <rect id="cable" x="474.5" y="-200" width="75" fill="#FFFFFF"/>
    <g id="kobot">
      <g id="bras-droit-grp">                             <!-- pivot: 512,512 -->
        <path id="bras-droit" fill="#141A1E" d="M512,512 L773.46,208.74 A420,387.5 0 0 1 773.46,815.26 Z"/>
        <g id="main-droite-grp">                          <!-- pivot: 512,512 -->
          <circle id="main-droite" fill="#141A1E" cx="937" cy="512" r="50"/>
        </g>
      </g>
      <g id="bras-gauche-grp">
        <path id="bras-gauche" fill="#141A1E" d="M512,512 L250.54,815.26 A420,387.5 0 0 1 250.54,208.74 Z"/>
        <g id="main-gauche-grp">
          <circle id="main-gauche" fill="#141A1E" cx="87" cy="512" r="50"/>
        </g>
      </g>
      <ellipse id="corps" fill="#FFFFFF" cx="512" cy="512" rx="337.5" ry="312.5"/>
      <circle id="point-gauche" fill="#141A1E" cx="276.9" cy="876.6" r="50"/>
      <circle id="point-centre" fill="#141A1E" cx="512" cy="926.6" r="50"/>
      <circle id="point-droit"  fill="#141A1E" cx="747.5" cy="876.6" r="50"/>
      <g id="zone-oeil-grp">
        <circle id="zone-oeil" fill="#E6213A" cx="512" cy="512" r="112.5"/>
        <circle id="oeil" fill="#FFFFFF" cx="512" cy="512" r="35"/>
        <g clip-path="url(#clip-oeil)">
          <rect id="paupiere-haut" fill="#FFFFFF" x="386" y="394" width="252" height="118"/>
          <rect id="paupiere-bas"  fill="#FFFFFF" x="386" y="512" width="252" height="118"/>
        </g>
      </g>
    </g>
  </g>
</svg>
```

Structural points to remember:

- **viewBox 1024×1424**: extended vertically so the Kobot can descend without clipping.
- **Articulation hierarchy**: the hand is a group INSIDE the arm's group → rotating the arm carries the hand, and the hand can rotate on top of it (it "slides" along the arm's arc).
- **Two clips**: `#clip-oeil` confines the eyelids, `#fenetre` makes the Kobot disappear behind the edge of the background (porthole effect for falls/descents).
- Optional expression elements (cross, "?", spiral): add them inside `#zone-oeil-grp` or `#kobot`, **hidden by default** (`opacity: 0`), revealed by class.

## 2 · Logo invariants (NEVER broken by an animation)

1. **The Kobot does not deform.** No scale, no squashing, no distortion of the shapes. Only these move: its environment (background, cable, position) and its limbs (arms, hands, eyelids, pupil).
2. **Eye zone 22%, pupil 7%, cable 7%**: never scaled or redrawn.
3. **Blinking is done with eyelids** (clipped white covers), never by deforming the eye.
4. **The cable stays vertical** and always reaches the edge of its support (extend it beyond the window if needed).
5. **Sirocco reserved for the eye ring.** No other red element, even in an error expression.
6. **A single Cirrus element per composition** — in the SVG, that's the background.

## 3 · Animation method

### 3.1 · Everything is driven by classes on `#kobot-svg`

Two families, two contracts:

- **Gestures** (one-shot): add the class, remove it when the duration ends. Implemented with `animation` + `@keyframes`.
- **States** (continuous): add/remove freely, they **stack** (a Kobot can be `descendu` + `carre` + `balance` and blink at the same time). Implemented with `transition` on properties or CSS variables.

```js
const kobot = document.getElementById('kobot-svg');
// Gesture
kobot.classList.add('coucou');
setTimeout(() => kobot.classList.remove('coucou'), 1650);
// State (e.g. during an API call)
kobot.classList.add('charge');
kobot.classList.remove('charge');
```

### 3.2 · State lives in CSS variables

THIS is the key to composability: state positions are variables, and every keyframe references them.

```css
#kobot-svg { --drop: 0px; --squircle: 512px; }
#kobot-svg.descendu { --drop: 330px; }   /* the kobot descends… */
#cable { height: calc(712px + var(--drop)); }   /* …the cable stretches by the same amount */
#fond, #fenetre rect { rx: var(--squircle); height: calc(1024px + var(--drop)); }
#kobot-svg.carre { --squircle: 110px; }  /* circle → square morph via corner radius */

/* A gesture that respects the current state: keyframes relative to --drop */
@keyframes rebond {
  0%   { transform: translateY(var(--drop)); }
  35%  { transform: translateY(calc(var(--drop) - 70px)); }
  100% { transform: translateY(var(--drop)); }
}
```

Rule: **any new vertical animation of `#kobot` must reference `var(--drop)`**, otherwise it teleports the Kobot when he is lowered.

### 3.3 · Required transform-origins

| Element | Origin | Why |
|---|---|---|
| `#suspension` | `512px 0px` | pendulum around the cable's attachment point |
| `#bras-*-grp`, `#main-*-grp` | `512px 512px` | rotation around the center: arms sweep their arc, hands slide along the arm |
| Expressions inside the eye | `512px 512px` | centered rotation (e.g. spiral) |

### 3.4 · Physical coherence

- Background, cable and Kobot move **together**: a descent stretches the cable AND the background (same durations, same easings).
- Credible gravity: acceleration on falls (`cubic-bezier(0.55, 0, 1, 0.45)`), damped landing (`cubic-bezier(0.34, 1.3, 0.64, 1)` for a slight bounce).
- Exits leave through the clip window (the Kobot disappears behind the edge of the background), never via a dry `opacity: 0`.
- Avoid visual overlaps: if a limb sweeps an occupied zone (e.g. spinning arms over the anchor dots), temporarily hide the affected elements (`opacity: 0`).

### 3.5 · Base vocabulary (reference durations)

| Class | Type | Duration | Effect |
|---|---|---|---|
| `cligne` | Gesture | 0.55 s | Eyelids close then reopen the eye |
| `coucou` | Gesture | 1.65 s | Right arm waves, the hand slides along the arc |
| `regarde` | Gesture | 2.25 s | The pupil roams the eye zone |
| `rebond` | Gesture | 0.75 s | Small jump in place (relative to `--drop`) |
| `alerte` | Gesture | 1.05 s | Horizontal shake of the whole Kobot |
| `charge` | State | continuous | Arms spinning 360°, anchor dots hidden |
| `balance` | State | continuous | ±4° pendulum around the attachment (2.6 s; `lent` variant 4.6 s) |
| `descendu` | State | toggle | 330 px descent, cable and background follow |
| `carre` | State | toggle | Background circle → rounded square |
| `dodo` / `miclos` | State | toggle | Eyelids closed / half-closed |

Creating new gestures/states is encouraged (that's the point of the method), while honoring §2 and §3.

### 3.6 · Bringing it to life (behavior)

- **Natural blinking**: ~6 s interval with ~50% probability, disabled when a state already occupies the eye (`dodo`, `miclos`, expression).
- **Reactivity**: clicking the Kobot triggers `coucou`. The pupil can follow the mouse (see `shared.js`).
- **Context-driven storytelling**: tie expressions to real situations — `charge` during a fetch, `dodo` + slow `balance` for maintenance, a questioning expression for a 404, a cross in the eye for a denial. The Kobot **tells the state of the system**; it does not decorate.
- One animated Kobot per page. He is a character, not a pattern.

## 4 · Accessibility and performance

- `role="img"` + `aria-label` on the SVG.
- `prefers-reduced-motion: reduce` → kill all SVG animations and transitions (fallback: static Kobot, eyes open).
- Animate only `transform` and `opacity` on limbs. `rx`/`height` transitions are tolerated on `#fond`/`#cable` only (state morphing, low frequency).
- No JS library: classes + pure CSS are enough.

## 5 · Checklist before shipping a new animation

- [ ] No deformation of the Kobot (no scale on body/eye/arms)
- [ ] Verticals relative to `var(--drop)`; combinable states tested together
- [ ] Transform-origins compliant (§3.3)
- [ ] Blink via clipped eyelids, eye clip ≥ 118 to avoid the Sirocco fringe
- [ ] Cable never detached from the edge (extended beyond the window when swinging)
- [ ] Sirocco only inside the eye; a single Cirrus (the background)
- [ ] `prefers-reduced-motion` respected
- [ ] The animation has contextual MEANING (system state, user reaction) — no gratuitous motion

# Frontend production plan — Triumph Manipulator Landing (v0)

**Not:** a real sprint commitment or resource estimate in hours.

---

## 1. Implementation order

1. **Layout shell** — header/footer, meta, OpenGraph placeholders (**SAFE UNKNOWN** copy).
2. **hero** + tokens (establishes type scale).
3. **trust_block** + **geo_trust** (static content first).
4. **process_steps** + **services_grid**.
5. **cases** (lazy media, LQIP **optional**).
6. **faq** (accordion JS + a11y).
7. **lead_form** (validation + submit wiring to **TBD** backend).
8. **final_cta** + **sticky_cta**.
9. Cross-section regression pass.

---

## 2. QA checkpoints

| Checkpoint | Validates |
|------------|-----------|
| **FE-Q1** | HTML outline / landmark regions |
| **FE-Q2** | Responsive snapshots at 4 widths |
| **FE-Q3** | CTA label consistency hero ↔ sticky ↔ final |
| **FE-Q4** | Form empty / invalid / success states |
| **FE-Q5** | `prefers-reduced-motion` path |

---

## 3. Responsive verification

- Physical device or browserstack for **iOS Safari** + one Android — **SAFE UNKNOWN** vendor access.

---

## 4. Reusable sections

- **process_steps**, **faq**, **lead_form** patterns likely reusable on future service landings — extract SCSS mixins after first ship.

---

## 5. Frontend freeze

- After **G6-equivalent** approval intent (tech + design), tag **frontend handoff revision** as frozen for this URL.
- **Any** blueprint semantic change (CTA, geo, claims) → **invalidates** freeze → partial rerun from affected partials.

---

## 6. Delivery candidate

- **Definition:** static build folder + source map policy + README with build command — **no** assertion this repo contains the Gulp project for Triumph.

**Status:** **Not produced** in this reference execution — documentation only.

---

*Frontend production plan v0 — reference execution only*

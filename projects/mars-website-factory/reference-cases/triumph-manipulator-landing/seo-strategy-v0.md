# SEO strategy — Triumph Manipulator Landing (v0)

**Honesty:** **No** ranking promises, **no** indexing guarantees, **no** fabricated search volumes.

---

## 1. Intent model

| Intent class | Query shape (illustrative) | Page role |
|--------------|----------------------------|-----------|
| **Transactional service** | “manipulator rental”, “hire crane truck [city]” | Primary capture |
| **Local / situational** | “move industrial machine [district]” | Same URL if scope unified; else **future** child URLs |
| **Informational overlap** | “what is manipulator truck” | Optional FAQ entries — **supporting**, not keyword stuffing |

Align with [seo-intent-model-v0.md](../../seo-intent-model-v0.md) vocabulary in downstream work.

---

## 2. Geo logic

- **Single source of truth** for service area: must match **`geo_trust`** block content and footer contact region.
- **SAFE UNKNOWN:** city list, excluded zones, GMB / local listings ownership.
- **Internal linking:** If multi-city pages are added later, use hub/spoke pattern per [page-blueprint-contract-v0.md](../../page-blueprint-contract-v0.md) — **no** thin doorway clusters.

---

## 3. Service structure (on-page SEO)

- **One clear H1** — service + primary geo modifier **at most once** (avoid spammy concatenation).
- **H2/H3** follow user scan: process, scope, proof, FAQ.
- **FAQ** — genuine Q&A only; **FAQPage** schema **candidate** only if visible on-page answers exist ([Page Blueprint Contract v0](../../page-blueprint-contract-v0.md)).

---

## 4. Trust SEO (E-E-A-T-oriented, documentation sense)

- **About / legal** support pages — **SAFE UNKNOWN** if absent; do not fake Organization JSON-LD fields.
- **Authoritative** copy: operator competence, safety methodology — **without** fake credentials.

---

## 5. Commercial SEO

- Snippet-oriented titles: service + location **only if** location is true service area.
- **No** misleading price snippets in meta unless prices are published and maintained.

---

## 6. Internal structure assumptions

- **v0 reference:** single landing URL in scope.
- **Future:** sibling URLs for districts or verticals → **invalidates** this page’s `internal_linking_strategy` and requires IA revision.

---

## 7. AI visibility notes

- Not an **`ai_visibility_page`**; no special entity-table pack required.
- If AI surfaces summarize the business, clarity and factual tone on-page help — **not** a controllable outcome; **no** claim of AI optimization results.

---

*SEO strategy v0 — reference execution only*

# HomeGateway v4.ai — typography atmosphere v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** канон **типографической атмосферы** — Exo 2 operational direction, hierarchy, calm technological feel.

**Не является:** font files, @font-face implementation, full type scale spec.

**Связанные:** [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) · [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md) · [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md)

---

## Canonical direction

**Primary family: Exo 2** — technological, aerospace-leaning, calm at operational sizes.

| Role | Family (draft) |
|------|----------------|
| **UI / headings / body** | Exo 2 |
| **Mono (data, IDs, timestamps)** | Exo 2 monospaced variant or dedicated mono — **SAFE UNKNOWN** until Phase 4 |

Exo 2 supports **Latin and Cyrillic** — aligned with Russian operator-facing copy.

**Fallback stack (draft):** `'Exo 2', system-ui, sans-serif`

---

## Why Exo 2

| Quality | HG fit |
|---------|--------|
| Geometric precision | Aerospace / instrument sensibility |
| Calm at 13–15px body | Long-session readability |
| Distinct from Inter/SaaS default | Anti-SaaS identity |
| Not display-sci-fi | Readable — unlike Orbitron-style fonts |

---

## Why typography must feel technological but calm

| Goal | Type behavior |
|------|---------------|
| **Scan speed** | Clear hierarchy; no decorative distortion |
| **Operator trust** | Consistent weights; no random size jumps |
| **Cockpit identity** | Compact headings; disciplined uppercase |
| **Anti-anxiety** | No ultra-thin hairlines on glass |

Technology = **precision and hierarchy** — not **costume letterforms**.

---

## Why «sci-fi fonts» are forbidden

| Font class | Problem |
|------------|---------|
| Orbitron, Audiowide, etc. | Poor body readability |
| Wide tracking display faces | Fatigue in lists |
| Glyph-heavy futuristic | Movie prop aesthetic |
| Comic / rounded playful | Wrong emotional target |

Sci-fi **movie titles** ≠ operational **instrument labels**.

---

## Why readability dominates decoration

| Rule | Rationale |
|------|-----------|
| Body 13–15px minimum (draft) | Rail + block lists |
| Line-height 1.4–1.5 body | Glass backgrounds |
| Contrast on glass first | WCAG AA intent — human verify Phase 4 |
| Label always with signal color | Not color-only |

Decoration is **spacing and weight** — not ornamental caps.

---

## Heading feeling

| Level | Use | Atmosphere |
|-------|-----|------------|
| **Zone / view title** | `main_area` header | Compact, medium weight — command label |
| **Block title** | block-screen | Semi-bold; short |
| **Section band** | Tactical groups | Small caps optional — restrained |

Headings **anchor** space — not shout.

---

## Tactical labels

| Element | Style |
|---------|-------|
| Signal level label | Small semi-bold + icon |
| `info_area` section | Uppercase muted — tracking slight |
| Due-today badge | Compact — not exclamation spam |
| OVERDUE band header | Distinct but not billboard |

Aligns with [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md).

---

## Uppercase usage

| Allowed | Forbidden |
|---------|-----------|
| Section labels (TACTICAL, OVERDUE) | Entire paragraph uppercase |
| Nav mode short labels (optional) | Body copy uppercase |
| Meta chips | Block titles all-caps |

Uppercase = **instrument annotation** — not shouting.

---

## Mono usage

| Content | Mono |
|---------|------|
| Timestamps, run IDs | Yes |
| Client/project codes (if any) | Yes |
| Body paragraphs | No |
| Signal row primary title | No — proportional |

Mono supports **data trust** — not hacker aesthetic.

---

## Spacing philosophy

| Principle | Application |
|-----------|-------------|
| **Tight but breathable** | Rail rows — compact without collision |
| **Zone rhythm** | More space between zones than between rows |
| **2K density** | More rows visible — not larger vanity type |
| **Tabular nums** | Dates and counts align in lists |

---

## Readability hierarchy (draft scale)

| Token | Size (illustrative) | Weight |
|-------|---------------------|--------|
| `display-zone` | 18–20px | 500–600 |
| `title-block` | 15–16px | 600 |
| `body` | 14–15px | 400 |
| `meta` | 12–13px | 400, secondary color |
| `label-tactical` | 11–12px | 600, muted |

Exact px — Phase 3 freeze with static MVP.

---

## Typography vs priority tiers

| Tier | Typography |
|------|------------|
| P0 | Semi-bold label; signal color on badge text |
| P1 | Standard body |
| P2 | Muted secondary |
| P3 | Meta size; lowest contrast |

---

## Anti-patterns

| Anti-pattern | Mitigation |
|--------------|------------|
| Inter-only SaaS sameness | Exo 2 committed |
| Thin 100 weight on glass | Min 400 body |
| Exclamation in every row | Calm copy discipline |
| Mixed font families | Exo 2 + one mono only |

---

## SAFE UNKNOWN

- Mono family choice (Exo 2 tabular vs JetBrains Mono) — Phase 4.
- Fluid type scaling mobile — TBD; desktop 2K primary.
- Font loading strategy — workspace charter.

---

*Last updated: 2026-05-24 — Typography atmosphere.*

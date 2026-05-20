# V2 — Semantic QA gate

**Purpose:** Pass/fail checklist for **meaning, content, and structure** vs **`design/v2/`** before a section is considered aligned.

## Preconditions

- Active scope = **one** `design/v2/NN.png` + mapped partial(s).
- Read [section-order.md](../semantics/section-order.md), [semantic-locks.md](../semantics/semantic-locks.md), [content-authority.md](../semantics/content-authority.md).

---

## Gate checks

| # | Check | Fail if |
|---|--------|---------|
| S1 | **Screen file** matches claimed scope (`NN.png`) | Working off wrong PNG or `full.png` only |
| S2 | **Role** matches [section-map.md](../semantics/section-map.md) row | Wrong block type (e.g. fleet catalog for `02`) |
| S3 | **Entity counts** match locks (3 cases, 8 cards, matrix rows, etc.) | Fewer/more substantive items without approval |
| S4 | **LOCKED copy** matches visible mock | Paraphrase, “SEO” rewrite, translation drift |
| S5 | **No V1 / archive semantics** (`design/v1/`, strip maps) | V1 phrases, strip order, legacy-only claims |
| S6 | **No generative marketing** in PLACEHOLDER zones | Fake brands, chats, reviews, INN |
| S7 | **Quarantine** | **`equipment-prices`** wired into **`index.html`** or treated as canonical V2 homepage section **without** a **new** operator gate (post–2026-05-16 baseline) |
| S8 | **Third screen** language | “Third screen” used without PNG vs DOM clarification **when reading pre-cleanup docs** |
| S9 | **Single-machine locks** | Fleet / multi-tonnage pitch inside `02`, `04`, `06`, `07` brand column |
| S10 | **Conflicts** | Any PNG vs `src/` disagreement unresolved (must **stop and report**) |

---

## Outcome

- **PASS:** All checks green; note any **SAFE UNKNOWN** as doc follow-up, not silent fix.  
- **FAIL:** List failed IDs; no merge to “frozen” until fixed or operator waives in writing.

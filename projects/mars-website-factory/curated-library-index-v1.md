# Curated library index v1 (Wave 6)

**Status:** **documented** — first **compact** operational reusable-block surface.  
**Workspace:** [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/).  
**Tiers:** [block-quality-tiers-v1.md](block-quality-tiers-v1.md).

**Not:** a component marketplace, **not** machine-readable npm package, **not** full block-registry dump.

---

## Library rows (reference workspace)

| block_id | Quality tier | Operational status | Extraction source | Implementation | Replacement | Forge |
|----------|--------------|-------------------|-------------------|----------------|-------------|-------|
| `hero` | battle-tested | stable | Wave 3 golden slice | ready | yes | Lite/Standard |
| `lead_form` | battle-tested | stable | Wave 3 golden slice | ready | yes (re-bind form) | Standard |
| `cta_band` | validated | stable | Wave 3 golden slice | ready | yes | Lite |
| `pricing` | validated | **re-extracted Wave 6** | Triumph V2 `equipment-prices` | ready | yes | Standard |
| `social_proof` | experimental | stable — **synthetic** | Wave 4 demo (not production extract) | ready | yes | Lite |
| `sticky_cta` | validated | stable | Wave 4 + `sticky_cta.js` | ready | yes (destroy module) | Standard |
| `contact_block` | validated | stable | Wave 4 golden slice | ready | yes | Lite |
| `faq` | validated | stable | Triumph V2 `faq-cta-footer` (FAQ only) | ready | yes (static) | Lite |
| `cases` | validated | **new Wave 6** | Triumph V2 `trust-cases-social-proof` (list only) | ready | yes (static) | Standard |

**Counts:** 9 blocks · 3 real production extractions (`faq`, `pricing`, `cases`) · 1 experimental (`social_proof`).

---

## Extraction maturity summary

| Wave | Real extracts | Notes |
|------|---------------|-------|
| Wave 5 | `faq` | First operational extraction REPORT |
| Wave 6 | `pricing` (replaces synthetic), `cases` (new) | Commercial card + case-study patterns |

**Not extracted (by design):** Triumph CTA/footer tails, trust-reviews carousel, client images, Font Awesome review logos, legal INN panel.

---

## Forge compatibility (default)

| block_id | Mode | Risk |
|----------|------|------|
| `hero`, `cta_band`, `social_proof`, `contact_block`, `faq` | Lite | layout/commercial if tokens touched |
| `lead_form`, `pricing`, `sticky_cta`, `cases` | Standard | conversion + modal + sticky z-index |

---

## Client template default

[workspaces/_template-client-v1/](../../workspaces/_template-client-v1/) ships **hero only**. Add blocks from this table per handoff — prefer **validated+** tiers for first client freeze.

---

## When to add a row

1. Extraction REPORT in `operational-examples/`.  
2. Reference workspace build PASS.  
3. Tier assigned in this file.  
4. [registry-sync-discipline-v1.md](registry-sync-discipline-v1.md) check if registry semantics changed.

**Do not** add rows for one-off project sections.

---

*Wave 6 — curated library surface.*

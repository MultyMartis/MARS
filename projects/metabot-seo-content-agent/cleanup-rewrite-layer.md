# Cleanup rewrite layer

**Purpose:** Post-generation **editorial** pass to strip or replace low-quality, generic, or off-brand phrasing before the user sees final `/text` output (and possibly other paths — **SAFE UNKNOWN**).

---

## Why it exists

- LLMs often emit **template-y** SEO/marketing words; niche keyword validators scale poorly.
- A **universal senior SEO editor** approach plus **rewrite** layers aligns with architecture: improve quality without exploding custom validators.

---

## Documented scope

- **Cleanup rewrite for `/text`** is listed as **working** in operations.
- Works together with **chunking** for long outputs — merge order **SAFE UNKNOWN**.

---

## Limits

- Does **not** replace **strict QA** (`/seoqa --strict`) or **factcheck** (`/factcheck --strict`) — [seoqa-and-factcheck.md](seoqa-and-factcheck.md).
- Residual **quality issues** remain — [known-issues.md](known-issues.md).

---

## SAFE UNKNOWN

- Number of rewrite passes (single vs multi-hop).
- Whether rewrite runs inline in same OpenRouter call or separate model.

---

*See [full-run-pipeline.md](full-run-pipeline.md), [lessons-learned.md](lessons-learned.md).*

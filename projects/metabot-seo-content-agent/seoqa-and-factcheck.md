# SEO QA and factcheck

---

## Separation

| Layer | Role |
|-------|------|
| **SEO QA** | Structure, intent alignment, spam patterns, FAQ / snippet discipline — “senior SEO editor” lens. |
| **Factcheck** | Factual claims vs allowed sources; **separate** prompt and runtime path from SEO QA. |

Mixing the two in one monolithic prompt is **avoided** by design (factcheck separation).

---

## Strict mode

- **`--strict`** enables **stricter** validation and enforcement in runtime — exact rules **SAFE UNKNOWN** (prompt text, thresholds).
- **Strict QA runtime enforcement** is a documented working feature for the canonical commands below.

---

## Canonical strict usage

Use these forms for **guaranteed** strict behavior:

- `/seoqa --strict from:task_id`
- `/factcheck --strict from:task_id`

---

## Non-canonical paths

- **Reuse strict inheritance** without explicit `--strict` on other commands is **not** currently required.  
- Do **not** assume `/text` or `/run` outputs are strict-QA’d unless you explicitly run `/seoqa --strict` (or product evolves to change this — **verify in n8n**).

---

## Cleanup rewrite interaction

- **Cleanup rewrite** (especially for `/text`) reduces undesirable generic marketing phrasing but is **not** a substitute for full **strict QA** — [cleanup-rewrite-layer.md](cleanup-rewrite-layer.md).

---

## Quality backlog

- Undesired phrases may still appear, e.g. *order now*, *professional*, *improvement*, *helps*, *affects*, *visibility* — tracked under **quality issues** in [known-issues.md](known-issues.md).

---

## SAFE UNKNOWN

- Model choice for QA vs factcheck.
- Whether strict mode emits structured JSON, plain text, or signals back to Sheets.

---

*See [telegram-commands.md](telegram-commands.md), [lessons-learned.md](lessons-learned.md).*

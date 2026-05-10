# Memory and task reuse

---

## Memory writes

- After meaningful progress (e.g. completed outline or text — **exact triggers SAFE UNKNOWN**), the system writes to **memory** in **Google Sheets**.
- **Purpose:** improve continuity, reduce repeated user context, support senior-editor behavior across sessions.

**SAFE UNKNOWN:**

- Memory record shape (single row vs multi-row history).
- Retention policy and pruning.
- PII handling rules for stored briefs.

---

## Task reuse (`from:`)

- Users reference prior work with **`from:task_id`** (syntax as implemented in Telegram parser).
- **Canonical strict paths:** `/seoqa --strict from:task_id`, `/factcheck --strict from:task_id` — [seoqa-and-factcheck.md](seoqa-and-factcheck.md).
- **Note:** Inheriting strict behavior **without** explicit `--strict` is **not** currently required across all commands — do not assume strict QA unless the command line includes it.

---

## Relation to MARS memory contracts

MARS documents **memory-write policy** and types under `memory/` — conceptual alignment only. MetaBOT’s Sheets-backed memory is **external**; it does **not** automatically satisfy MARS `memory-write-policy-v0` unless a future bridge is designed and evidenced.

---

## SAFE UNKNOWN

- Whether memory is **per-user**, **per-chat**, or **global**.
- Deduplication when the same topic is run twice.

---

*See [task-lifecycle.md](task-lifecycle.md), [storage-layer.md](storage-layer.md).*

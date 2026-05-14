# MARS — Artifact lifecycle rules

**Status:** **documented** — governance-only, **Phase S4**. **Human** labeling and merge/deprecate **discipline**. **No** storage engine, **no** automated lifecycle manager, **no** object store assumptions.

**Purpose:** Clarify how **artifacts** (documents, code, exports, registry rows, design files) **should evolve** so **artifact lifecycle ambiguity** and silent duplication **decrease**.

---

## 1. Lifecycle labels (governance vocabulary)

| Label | Meaning |
|-------|---------|
| **Draft** | Work-in-progress; may be incomplete or internally inconsistent; not advertised as operator SoT. |
| **Operational draft** | Used day-to-day but still expected to change; boundaries should be stated in-file or in index. |
| **Stabilized** | Intended as current truth for its scope; contradictions should be fixed or explicitly flagged. |
| **Deprecated** | Superseded; keep pointer to replacement; do not expand content here without a deliberate migration task. |
| **Historical** | Preserved for audit or narrative; not current operational truth. |
| **Imported legacy** | Derived from Web-GPT or other imports; may not match current product—see [AGENTS.md](../AGENTS.md) three-way split. |
| **Experimental** | May change or disappear; must not silently redefine governance or registry SoT. |
| **Runtime-scoped** | Tied to **proven** in-tree runtime or adapter demo paths; **not** proof that full MARS runtime exists. |
| **Governance-scoped** | Normative **documentation** only; does not execute work. |

Multiple labels can apply in prose (e.g. “governance-scoped **draft**”).

---

## 2. When to deprecate

- Content is **wrong**, **misleading**, or **dangerously ambiguous** for current operators **and** merge is not immediate.  
- Two documents cover the same **SoT** topic—pick one successor, mark the other **deprecated** with link.  
- **Entropy** signals per [documentation-entropy-rules.md](documentation-entropy-rules.md): overlapping “how we work” pages.

---

## 3. When to merge

- Two pages differ slightly; **one** combined page reduces load—per S3 survivability docs.  
- **Index-first:** sometimes merge = “one paragraph + link” into [governance/README.md](README.md) rather than a new file.

---

## 4. When to archive

- Material still valuable for **history** but should not drive execution—move narrative to **historical**, trim active indexes.  
- **Migration** completed: old handoff artifacts may be **historical** with pointer to new SoT.

**Archive** here means **documentation posture** (label + index), not a cloud archive product.

---

## 5. When **not** to duplicate

- Same **normative** rule in three places—prefer **one** normative file + links.  
- **Registry row** duplicates **agent card** prose—cross-link per [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md).  
- **Lifecycle log** entries that restate entire contracts—log **pointers**, not full copies.

---

## 6. Avoiding artifact drift

- After substantive edits, update **indexes** and **cross-links** when behavior of the artifact changes.  
- State **lane** and **scope** in REPORT when artifacts span governance and delivery.  
- For **experimental** code trees, qualify in README or adjacent doc; do not let demo behavior **become** implied governance—[operational-survivability.md](operational-survivability.md).

---

## 7. SAFE UNKNOWN

- Whether your team will use git tags, folders, or filenames to **encode** lifecycle mechanically.  
- Retention policy for **chat exports**—not governed here beyond honesty about lossiness in [context-continuity-rules.md](context-continuity-rules.md).

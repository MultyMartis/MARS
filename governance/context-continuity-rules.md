# MARS — Context continuity rules

**Status:** **documented** — governance-only, Phase S3. **No** claim of automatic persistence of chat reasoning; **no** shared memory product.

**Purpose:** Improve **long-term continuity** across chats, sessions, and people using **documentation discipline** compatible with Cursor **Parallel Chat** work mode and **REPORT** closeouts.

---

## 1. Migration expectations

- **Chat migration export** (or any handoff artifact) is **lossy** for tacit reasoning. Treat exports as **hints**, not **SoT**.  
- After migration, **re-ground** from files: [AGENTS.md](../AGENTS.md), task-scoped contract, relevant registry row.  
- **Parallel Cursor Chat Work Mode:** each chat keeps **separate** assistant context; continuity is **human** + **repo artifacts**, not cross-chat sync.

---

## 2. Self-report discipline (REPORT)

When a task requests reporting ([AGENTS.md](../AGENTS.md) task closeout):

- Use a clear heading: `# REPORT — <task/stage name>`.  
- Include **changed files**, **summary**, **git status**, **UNKNOWN** / **SECURITY RISK** if applicable.  
- State **lane** and **scope** in plain language so a future reader need not replay the chat.

This is **not** automation — it is a **human-readable** checkpoint.

---

## 3. Continuity boundaries

| In scope for continuity | Out of scope |
|-------------------------|--------------|
| Committed docs, registries, lifecycle notes | Full chat transcripts as normative |
| Explicit **SAFE UNKNOWN** lists | Assumed “team knowledge” |
| Scoped REPORT closeouts | Promises that the next assistant “remembers” |

---

## 4. SAFE UNKNOWN during migrations

During repo, branch, or chat migration:

- Mark **unknown** any registry row, external ID, or path not re-verified in the new context.  
- Do **not** fill gaps with “probably still true” without a file citation.  
- Prefer one lifecycle line: **migration pending verification** for (topic).

---

## 5. Avoiding fake persistence assumptions

- **Do not** assume assistants, CI, or hooks **enforce** governance unless a **named** human process exists — [enforcement/README.md](enforcement/README.md) is documentation cues only.  
- **Do not** assume `logs/lifecycle-log.md` replaces contracts — see [registry-source-of-truth.md](registry-source-of-truth.md).  
- **Do not** treat experimental `mars-runtime/` behavior as automatically documented — update governance **or** qualify as demo-only.

---

## 6. Minimum migration package (human-maintained)

For a meaningful handoff, the **next** operator should receive **at least**:

1. **Lane** (production vs MARS core) per [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md).  
2. **Branch / scope** (what folders are in play).  
3. **Authoritative files touched or to touch** (paths).  
4. **Open UNKNOWNs** and who resolves them.  
5. **Last REPORT** or lifecycle pointer if work was mid-stream.

Anything less is **high risk** for silent rework — not forbidden, but honest about gaps.

---

## 7. Lane continuity discipline

- Stay in **one** lane per chat unless the task explicitly bridges — reduces contradictory instructions.  
- If bridging is required, **name both** lanes and the **reason** in REPORT or lifecycle.

---

## 8. Alignment summary

| Artifact | Role in continuity |
|----------|-------------------|
| Chat export | Optional context — verify against repo |
| REPORT | Scoped snapshot for humans |
| Governance / registry | Claim and identity survival |
| Lifecycle log | Decision and milestone trail — not auto-sync |

---

## 9. SAFE UNKNOWN

If a migration package is incomplete, the correct output is **SAFE UNKNOWN** for missing verification — not inferred continuity.

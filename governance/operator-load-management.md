# MARS — Operator load management

**Status:** **documented** — governance-only, Phase S3. **No** productivity framework, **no** metrics dashboard, **no** automated workload balancing.

**Purpose:** Give **human operators** simple language for overload and **small** mitigations that fit MARS (documentation-first, lane discipline).

---

## 1. Warning signs (operator-level)

- Dread opening the repo because “any file might matter.”  
- Inability to name **one** authoritative file for the current question.  
- Frequent context switching between **governance**, **delivery**, and **runtime** in one sitting without a task reason.  
- Repeated re-explanation of the same boundaries to collaborators or assistants.

---

## 2. Lane overload indicators

Aligned with [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md):

- Edits under `workspaces/*` mixed with broad `governance/` rewrites **without** explicit scope.  
- “Small fix” in production assets spawning registry-wide changes.  
- Same chat title used for unrelated lanes for days.

---

## 3. Workflow fragmentation indicators

- Same task described in **chat**, **README**, and **lifecycle** with **different** verbs or scope.  
- Handoffs that reference paths that moved or were never canonical.  
- No single **REPORT** or note closing a slice of work — next person starts blind.

---

## 4. Prompt sprawl indicators

- Long custom prompts that **re-derive** [AGENTS.md](../AGENTS.md) on every task.  
- Multiple near-duplicate agent instruction blocks in different repos or packs.  
- Instructions that **contradict** governance “for speed.”

**Mitigation:** shorten prompts; **link** AGENTS + one governance file + one task path; fix contradictions in **source** docs once.

---

## 5. Governance fatigue indicators

- Every small change feels like it requires a **constitution** edit.  
- New rules added faster than old ones are **used** or **deprecated** ([documentation-entropy-rules.md](documentation-entropy-rules.md)).  
- Enforcement docs treated as mandatory reading for **every** delivery task.

---

## 6. Context overload indicators

- Mandatory reading list grows faster than **completed** reconciliations.  
- Indexes rot (links broken, descriptions wrong) because nobody owns a quick pass.  
- Assistants summarize “the whole repo” instead of **one** contract.

---

## 7. Lightweight mitigation patterns

| Pattern | When to use |
|---------|-------------|
| **Split phases** | One slice: e.g. “registry rows only” then “contracts only” — not simultaneous renames across everything. |
| **Stabilize before expand** | See [stabilization-vs-expansion.md](stabilization-vs-expansion.md) — pause new subsystems until drift is quiet. |
| **Indexes over new philosophy** | Navigation problem → index row in `governance/README.md` or pack index. |
| **Limit simultaneous architecture shifts** | Cap parallel “big ideas” (new ontology + new registry + new runtime demo) to **one** stream unless staffed and scoped. |
| **Explicit deferral** | Write “deferred / not in this pass” in lifecycle or REPORT — reduces ambient guilt-load. |

---

## 8. SAFE UNKNOWN

If overload comes from **unclear ownership** of a file or lane, record **SAFE UNKNOWN** and who must decide — do not invent a new process layer.

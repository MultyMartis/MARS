# MARS — Onboarding survivability

**Status:** **documented** — governance-only, Phase S3. **Not** “onboarding solved by software”; **not** a learning management system.

**Purpose:** Keep **new operators** productive without **information overload**, **false runtime assumptions**, or **architecture shock**.

---

## 1. Minimum read set (new operator)

Read **in this order** before treating any other file as mandatory:

1. [../README.md](../README.md) — what the repo is and is not.  
2. [../AGENTS.md](../AGENTS.md) — honesty rules, **documented** vs **planned** vs **legacy imported**, **SAFE UNKNOWN**.  
3. [governance/README.md](README.md) — map to governance addenda (pick **only** topics relevant to the task).  
4. [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md) — if work uses Cursor with **multiple chats** or mixed lanes.

**Stop after four** unless the task explicitly requires deeper files.

---

## 2. Safe onboarding sequence (lightweight)

| Step | Action |
|------|--------|
| A | Confirm **lane** (production vs MARS core) per parallel chat doc. |
| B | Open **one** registry or contract file needed for the task (e.g. `agents/registry.md`), not the whole tree. |
| C | Note **SAFE UNKNOWN** anywhere scope is unclear — do not infer runtime from filenames. |
| D | Close with a **REPORT**-style summary when the task asked for reporting ([AGENTS.md](../AGENTS.md) task closeout). |

---

## 3. Optional (read when relevant)

- [execution-model.md](execution-model.md) — how work runs **today** vs **planned** surfaces.  
- [master-build-map.md](master-build-map.md) — roadmap / stage posture.  
- [registry-architecture.md](registry-architecture.md), [registry-source-of-truth.md](registry-source-of-truth.md) — when touching registries or identity.  
- [enforcement/README.md](enforcement/README.md) — anti-drift cues for **writers**.  
- [operational-survivability.md](operational-survivability.md), [documentation-entropy-rules.md](documentation-entropy-rules.md) — when adding or reorganizing docs.

---

## 4. Historical (do not treat as current product truth without reconciliation)

- [../web-gpt-sources/](../web-gpt-sources/) — **legacy imported** design pack; may contradict current governance.  
- Old phase notes, superseded contracts (if marked), and long narrative archives under projects — **input**, not automatic **SoT**.

---

## 5. Governance-critical vs runtime-critical vs Website Factory–specific

| Class | Meaning | Examples |
|-------|---------|----------|
| **Governance-critical** | Affects claims, boundaries, identity, precedence — wrong edits mislead the whole repo | `governance/*`, `agents/registry.md`, key `workflows/*` contracts |
| **Runtime-critical** | Only when the task **is** an experimental runtime task — evidence in `mars-runtime/` | Adapters, demo runners — **do not** assume full product |
| **Website Factory–specific** | Delivery and factory packs under `projects/mars-website-factory/` | Runbooks, factory lane rules — **not** universal MARS core unless promoted via governance |

New operators: default to **governance-critical** literacy, **not** deep Website Factory or runtime unless the assignment says so.

---

## 6. Reducing false assumptions

- **No** “because `mars-runtime/` exists, MARS is live” — see [runtime-registry-boundaries.md](runtime-registry-boundaries.md).  
- **No** “registry row implies deployed tool” — see [registry-source-of-truth.md](registry-source-of-truth.md).  
- **No** “chat agreed, so it is canonical” — only committed docs and registries count for survivability.

---

## 7. SAFE UNKNOWN

If onboarding instructions in a pack disagree with `governance/` or `AGENTS.md`, treat **governance + AGENTS** as the honesty baseline until a **human** reconciles them — state **SAFE UNKNOWN** for the conflicting slice.

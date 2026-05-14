# MARS — Execution boundary clarification

**Status:** **documented** — governance-only, **Phase S4**. Reduces **adapter-vs-system** and “**where did execution happen?**” confusion.

**Purpose:** Separate **governance semantics**, **runtime code**, **Cursor execution**, **external systems**, **Website Factory** operations, **adapters**, **bridges**, and **operational workflows** (human + docs)—without claiming new infrastructure.

---

## 1. Where execution **really** happens **today** (documented)

Per [execution-model.md](execution-model.md) and [AGENTS.md](../AGENTS.md):

- **Primary:** **human** operators using **Cursor** (or compatible tooling) on a **developer-controlled** machine: edits, commands, reviews.  
- **Optional upstream:** planning/prompt packaging (e.g. Web-GPT **legacy** materials)—still **human-gated**.

**No** in-repo MARS **daemon** is asserted as the executor of the full prompt → work → log chain.

---

## 2. What is **only modeled**

- **Control Plane**, **workflow runs**, **task state machines** in `../control-plane/`, `../workflows/` — **documented architecture** / **planned implementation** unless specific code is proven as product runtime.  
- **Execution Bridge** as **concept**—see [execution-model.md](execution-model.md) and `../mars-runtime/execution-bridge-v0.md` for **contract** intent; bridge **does not** imply a live bridge service.

---

## 3. What is **experimental** or **narrow**

- Code under `mars-runtime/` or similar **may** exist for **demos** or **narrow** tests—treat as **runtime-scoped** artifacts per [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md).  
- **Experimental** does **not** upgrade governance or registry SoT automatically.

---

## 4. What is **external**

- **n8n**, hosting, CI services, ticketing, chat platforms — **outside** MARS governance unless explicitly integrated **and** evidenced for a **named** path—[external-system-boundaries.md](external-system-boundaries.md).  
- **MetaBOT** and other multi-workflow products — **external**; do not treat as MARS core runtime.

---

## 5. What is **governance-only**

- Files under `governance/**` describe **how to work and speak** about the system; they **do not** execute tasks.  
- [enforcement/](enforcement/README.md) cues are **human-readable**; **not** CI, **not** a policy engine.

---

## 6. Website Factory operations

- `projects/mars-website-factory/**` is **operational** documentation and packs for a **factory** lane; it is **not** “the MARS runtime.”  
- Factory runbooks may **reference** execution contracts; expanding factory scope is **not** required to understand S4 semantics.

---

## 7. Adapters and bridges

| Term | Boundary note |
|------|-----------------|
| **Adapter** | Code or doc that **adapts** an external interface or legacy agent shape to a **documented** MARS-facing surface. Adapters **do not** imply full orchestration. |
| **Bridge** | **Handoff** concept between semantics and a **concrete runner**—see [execution-model.md](execution-model.md). A bridge description **≠** a running bridge **service**. |
| **Operational workflows** | **Human** procedures plus **documentation**; may **include** external tools; still **not** MARS-autonomous unless proven. |

---

## 8. Cursor’s role (execution layer)

- Cursor is the **documented** IDE/agent layer for **filesystem** and **shell** work **in this repo**.  
- Cursor **does not** replace governance SoT or lifecycle logs; it **implements** what humans instruct, subject to project rules.

---

## 9. SAFE UNKNOWN

- Your org’s **exact** split between Lane A and Lane B chats for edge paths—default to [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md) and explicit task **lane** fields.  
- Any **undocumented** bridge from a **specific** external workflow to a **specific** repo folder without a cited runbook or contract.

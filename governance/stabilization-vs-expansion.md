# MARS — Stabilization vs expansion

**Status:** **documented** — governance-only, Phase S3. **Not** a stage-gate tool; **not** automated governance.

**Purpose:** Reduce **architecture runaway** and **speculative layering** by naming when to **pause expansion** and **stabilize** what exists.

---

## 1. When MARS should stabilize

Prefer a **stabilization** pass when:

- **Drift** is visible: registries disagree with READMEs or contracts ([registry-source-of-truth.md](registry-source-of-truth.md)).  
- **Onboarding** fails at “where do I look?” — see [onboarding-survivability.md](onboarding-survivability.md).  
- **Multiple** parallel docs describe the same boundary — [documentation-entropy-rules.md](documentation-entropy-rules.md).  
- **Operator load** signs appear — [operator-load-management.md](operator-load-management.md).  
- A **migration** left UNKNOWNs unowned — [context-continuity-rules.md](context-continuity-rules.md).

**Stabilize** means: reconcile, deprecate banners, fix links, narrow claims — **not** new subsystems.

---

## 2. When expansion is justified

Expansion (new contract, new registry kind, new pack, new experimental path) is reasonable when:

- A **scoped** need is documented (who, what lane, what failure without it).  
- **Precedence** and identity rules are extended, not contradicted silently ([identity-and-naming-rules.md](identity-and-naming-rules.md)).  
- **Survivability** docs are updated in the **same** pass or immediately after (README index / governance row) — avoid orphan concepts.

---

## 3. Signals of governance debt

- New terms without updates to **terminology** or **identity** docs.  
- “Temporary” maps that live for months.  
- Forbidden-claim patterns appearing in new prose ([enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md)).

---

## 4. Signals of survivability debt

- Indexes wrong or missing for active packs.  
- REPORT discipline dropped — handoffs rely on chat only.  
- Mandatory reading list grows without retiring duplicates.

---

## 5. Indicators that expansion should pause

- More than **one** large architecture initiative active **without** clear ownership.  
- Runtime demo paths changing **faster** than governance qualifiers.  
- New folders created “for clarity” that duplicate existing governance topics.

---

## 6. Explicit discouragements

- **Endless architecture layering** — each layer must earn its **one** clear audience and file home.  
- **Speculative AGI structures** — not in scope for MARS honesty posture; keep narrative testable and scoped.  
- **Uncontrolled subsystem creation** — new `*-v0` contracts only with maintenance intent.  
- **Fake future planning** — roadmaps may exist ([master-build-map.md](master-build-map.md)), but docs must not read as **done** futures ([AGENTS.md](../AGENTS.md)).

---

## 7. SAFE UNKNOWN

If it is unclear whether a change is **stabilization** or **expansion**, default to **stabilize** (clarify, merge, index) and mark **SAFE UNKNOWN** for the ambiguous slice until a human decides.

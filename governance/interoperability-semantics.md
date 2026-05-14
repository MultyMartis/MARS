# MARS — Interoperability semantics

**Status:** **documented** — governance-only, **Phase S6**. **Not** a shared execution platform, **not** coordination middleware.

**Purpose:** Define **safe** interoperability expectations for MARS: how systems and artifacts may connect **without** implying orchestration, shared runtime, or autonomous coordination.

---

## 1. What interoperability is **not**

| Phrase | Clarification |
|--------|-----------------|
| **Interoperability ≠ orchestration** | Connecting A to B **does not** mean MARS schedules, branches, or owns retries across them. |
| **Interoperability ≠ shared runtime** | Common file formats or envelopes **do not** prove a single MARS execution kernel. |
| **Interoperability ≠ autonomous coordination** | No silent multi-system “agreement” or agent handshakes without human-visible initiation per [human-execution-guarantees.md](human-execution-guarantees.md). |

---

## 2. Safe forms (allowed semantics)

| Form | Rule of thumb |
|------|----------------|
| **Explicit exports** | Operator-generated files (CSV, JSON snippets, markdown) with stated provenance and review step. |
| **Task envelopes** | Human-readable (or narrow experimental) bundles separating governance contract, human instructions, external payloads—[task-envelope-standard.md](task-envelope-standard.md). |
| **Report artifacts** | REPORT-style outputs committed or pasted after human edit; tooling may **suggest** sections only. |
| **Manual imports** | Human drags/pastes/applies external content; no “always sync” implication. |
| **Explicit bridges** | Named handoff steps in runbooks or docs; optional **bridge helper** under explicit invocation—[adapter-and-bridge-boundaries.md](adapter-and-bridge-boundaries.md). |
| **Documented adapters** | Narrow mappers with honest limits; labeled experimental when appropriate—[operational-helper-classification.md](operational-helper-classification.md). |

---

## 3. Unsafe forms (red-line semantics)

| Form | Why unsafe |
|------|------------|
| **Implicit coordination** | Side effects depend on undeclared ordering or hidden triggers. |
| **Hidden state propagation** | Meaning moves through caches, env vars, or opaque stores without reviewable trail—[tooling-escalation-warnings.md](tooling-escalation-warnings.md). |
| **Silent retries** | Network or API loops without explicit logs, caps, and human awareness. |
| **Cross-system assumptions** | Treating external IDs, tickets, or workflow names as MARS canonical truth—[external-system-boundaries.md](external-system-boundaries.md). |
| **Invisible ownership transfer** | Artifacts or tasks “move” accountability without a human acknowledging scope in chat or REPORT. |

---

## 4. Alignment with controlled operationalization

Interoperability in S6 is **semi-structured**: enough shape to reduce chaos, not enough machinery to pretend MARS is a control plane—[controlled-operationalization.md](controlled-operationalization.md).

---

## 5. SAFE UNKNOWN

Whether a **specific** integration path is “safe semi-structured” vs implicit orchestration is **SAFE UNKNOWN** until triggers, payloads, and ownership are documented and reviewed.

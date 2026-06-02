# Lessons Learned — SITE-001 / Run 5 Initialization (v1)

**Source:** Real operational target SITE-001 (Автосалон СИБКАР)  
**Validity:** Treated as **valid architectural evidence** because bottleneck appeared during supervised Run 5 initialization, not as hypothetical design exercise.

---

## Lesson 1 — Bottleneck is acquisition, not audit logic

**Observation:** OCPilot audit methodology, baseline (`ocstore-3038-rs2`), charter, and Run 5 plan were **ready**. Progress stopped because **no site artifact package** existed in repo or external bulk — comparison and version proof require operator-mediated file delivery.

**Implication:** Investment priority shifts from expanding audit checklists to a **supervised access acquisition layer** that produces a **Snapshot Package** consumable by pilots.

---

## Lesson 2 — Current operator path does not scale

**As-is flow (documented operational reality):**

```
Operator
  ↓
WinSCP (or equivalent manual channel)
  ↓
Screenshots / ad-hoc exports
  ↓
Files dropped for OCPilot
  ↓
OCPilot (analysis on evidence)
```

**Friction:** High human context switching; inconsistent manifests; credentials live outside repo but acquisition has no standard contract; agent cannot assume tree layout or completeness.

---

## Lesson 3 — Desired flow is site → snapshot → consumer

**Target flow (architecture only — not implemented):**

```
SITE (external)
  ↓
External Access Runtime (EAR)
  ↓
Snapshot Package
  ↓
Consumer System (OCPilot, WPilot, future Factory / Landing Pilot)
```

**Implication:** EAR **collects**; consumers **analyze**. Separation prevents pilots from owning FTP/SSH/PMA mechanics independently.

---

## Lesson 4 — Readiness ≠ evidence on disk

**Observation:** **READY FOR AUDIT** correctly means intake, baseline, and charter gates passed. It does **not** mean site files are present. Run 5 initialization proved the gap explicitly ([RUN-5-FIRST-FINDINGS.md](../../sites/site-001/reports/RUN-5-FIRST-FINDINGS.md)).

**Implication:** Future status vocabulary may need a distinct state for **evidence package received** — **SAFE UNKNOWN** whether OCPilot adopts new registry states; not decided in this freeze.

---

## Lesson 5 — Shared patterns exist; shared runtime does not

[shared/external-access-patterns/](../../../shared/external-access-patterns/README.md) documents **human-supervised channel patterns**. EAR is the **next layer**: structured snapshot output and connection semantics — still documentation-first in v1.

---

## Lesson 6 — Secrets discipline held; acquisition did not

External `secrets/` placement is correct. Failure mode was **not** credential leakage in git but **missing standardized acquisition** from approved channels.

---

## Lesson 7 — Consumers must never ingest raw credentials

Snapshot consumers (OCPilot first) should receive **references, manifests, and sanitized metadata** — not live passwords. Reinforces EAR security model design.

---

## Non-lessons (explicit)

- **Not** proven: live site is compromised, wrong version, or misconfigured — **SAFE UNKNOWN** until snapshot.
- **Not** required: autonomous agents, hidden FTP bots, or governance changes.
- **Not** a mandate to implement EAR in any specific language or repo layout beyond docs in v1.

---

## Recommended architectural response

Design **EAR v1** as documented under [shared/external-access-runtime/](../../../shared/external-access-runtime/) — target **Mode 2 (Connected Read Only)**; defer **Mode 3 (Read Write)**.

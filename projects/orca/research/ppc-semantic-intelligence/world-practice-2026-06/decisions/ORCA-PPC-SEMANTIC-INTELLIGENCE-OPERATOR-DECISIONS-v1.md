# ORCA PPC Semantic Intelligence — Operator Decisions v1

**Recorded:** 2026-06-22  
**Authority:** MARS operator decisions — versioned governance record  
**Scope:** ORCA PPC Semantic Intelligence research intake and Corvonero clean-room boundary

---

## D1 — Research status

**Decision:** `ADOPT SELECTIVELY AS BASIS FOR ORCA TARGET ARCHITECTURE`

The world-practice research source is **not** promoted in full automatically. Findings enter ORCA only through selective promotion backlog items and future Architecture Decision Records.

---

## D2 — Corvonero clean-room v1

**Decision:** `FREEZE AS DIAGNOSTIC — RE-RUN SEMANTIC ADMISSION AFTER GUIDELINE AND BENCHMARK`

- Do **not** manually clean the 1892 accepted phrases from diagnostic run v1.
- Preserve diagnostic artifacts for failure-mode evidence.
- Next semantic admission run requires upgraded ORCA Semantic Intelligence (guideline + benchmark + pilot thresholds).

---

## D3 — Production-blocker metrics

**Decision:** Initial pilot thresholds (versioned — changes require new operator decision)

| Metric | Threshold |
|--------|-----------|
| Commercial Precision on auto-accept | **≥ 0.95** |
| Protected-strata false-positive rate (per class) | **≤ 0.01** |

**Protected classes:** career; educational; DIY/how-to; regulatory; navigational.

---

## D4 — Abstention policy

**Decision:** `ABSTAIN IS MANDATORY WHEN COMMERCIAL INTENT IS NOT SUFFICIENTLY SUPPORTED`

Rules:

- The system must not invent a commercial interpretation.
- Ambiguity cannot automatically resolve to ACCEPT.
- `NEEDS OPERATOR DECISION` may be a workflow status.
- The semantic classification itself must explicitly contain `ABSTAIN`.

---

## D5 — Gold dataset scope

**Decision:** Dual-scope benchmark program

| Scope | Size | Role |
|-------|------|------|
| Universal ORCA benchmark | 1 200–2 000 phrases | Program-wide source of truth |
| Corvonero pilot | 300–500 phrases | Bounded pilot within universal program |
| Blind test | Independent subset | Required |
| Protected hard-negative strata | Dedicated strata | Required |

Corvonero pilot is a **bounded pilot** within the wider ORCA benchmark program — not a substitute for universal benchmark governance.

---

## D6 — Canonical research path

**Decision:** Canonical locus fixed

**Path:** `projects/orca/research/ppc-semantic-intelligence/world-practice-2026-06/`

**Canonical source:** `ORCA-PPC-SEMANTIC-CORE-WORLD-PRACTICE-RESEARCH-v1.md`

No relocation. Single copy in repository.

---

## D7 — Corvonero restart boundary

**Decision:** Downstream production **prohibited** until guideline, benchmark, and pilot thresholds pass

**Prohibited until gate pass:**

- Campaign architecture
- Advertising groups
- Advertisements
- Final negatives
- Bids
- Match-type production
- Commander export
- Import
- Launch

**Additional requirement:** Semantic Core must receive explicit operator sign-off before Campaign Production.

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `decisions/orca-ppc-semantic-intelligence-operator-decisions-v1.json` |
| Corvonero freeze | `projects/orca/projects/corvonero-direct-v2-clean-room/PROJECT.md` |
| Promotion backlog | `promotion/ORCA-PPC-SEMANTIC-INTELLIGENCE-PROMOTION-BACKLOG-v1.md` |

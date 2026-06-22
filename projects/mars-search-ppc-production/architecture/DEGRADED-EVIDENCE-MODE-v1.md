# Degraded-Evidence Mode v1

**Parent:** [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Allow controlled continuation when specific evidence is genuinely unavailable (e.g. CAPTCHA blocking paid SERP during business hours).

**Silent degradation is forbidden.**

---

## Required degraded-mode record

| Field | Required |
|-------|----------|
| Missing evidence type | Yes |
| Reason | Yes |
| Attempted collection evidence | Yes |
| Impact assessment | Yes |
| Alternative evidence used | If any |
| Operator approval | Yes |
| Affected stages | Yes |
| Expiration / recheck condition | Yes |

Register in project manifest: `degraded_evidence_approvals.<stage_id>`.

---

## Applicable stages

Primary: **SPPC-10** (Daytime Paid SERP Intelligence).

Strategy (SPPC-13) must report:

```text
BLOCKED OR DEGRADED — PAID COMPETITIVE EVIDENCE MISSING
```

when paid SERP is incomplete and no approved degradation exists.

---

## Completion status

When degradation approved:

`COMPLETED WITH APPROVED DEGRADATION`

---

## Prohibited

- Treating off-hours SERP as advertising-market truth  
- Continuing to Commander without documenting degradation impact  
- Auto-approving degradation in chat without operator record  

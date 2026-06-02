# Freeze — SITE-001 Pre–Runtime Bridge

**Freeze ID:** `site-001-pre-runtime-bridge`  
**Created:** 2026-06-01  
**Lane:** B — OCPilot  
**Classification:** human-reviewed operational snapshot; **not** live site state; **not** automation output.

---

## Purpose

Preserve OCPilot operational state at the moment Run 5 (first read-only site audit) **paused** pending **External Access Runtime (EAR)** architecture — formerly referred to in operator discussion as **Runtime Bridge**.

This freeze does **not** change registry status. **SITE-001 remains READY FOR AUDIT.**

---

## Contents

| Document | Role |
|----------|------|
| [OCPILOT-STATE-SUMMARY-v1.md](OCPILOT-STATE-SUMMARY-v1.md) | Program and SITE-001 status at freeze |
| [LESSONS-LEARNED-v1.md](LESSONS-LEARNED-v1.md) | Valid architectural evidence from Run 5 initialization |
| [AUDIT-BLOCKERS-v1.md](AUDIT-BLOCKERS-v1.md) | What blocks audit execution until EAR direction exists |

---

## Rules

- No credentials, dumps, or secrets in this folder.
- No claim that EAR or Runtime Bridge **exists** as implementation — documentation and freeze only.
- Link to live work: [sites/site-001/](../../sites/site-001/), [shared/external-access-runtime/](../../../shared/external-access-runtime/).

---

## Related

- EAR foundation: [shared/external-access-runtime/README.md](../../../shared/external-access-runtime/README.md)
- OCPilot index: [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md)
- Run 5 initialization evidence: [sites/site-001/reports/RUN-5-FIRST-FINDINGS.md](../../sites/site-001/reports/RUN-5-FIRST-FINDINGS.md)

# Forge WordPress FW-06 — Pilot Intake Input v1

**Document type:** Stage input for FW-06  
**Version:** v1  
**Date:** 2026-06-22  
**Prerequisite:** FW-05 synthetic capability **PROVEN WITH LIMITATIONS**

---

## Purpose

Define intake criteria for first **client** Forge WordPress pilot after synthetic validation.

---

## Synthetic evidence (FW-05)

- Case FWS-0001 completed at `workspaces/forge-wordpress-synthetic/FWS-0001/`
- Outcome: PROVEN WITH LIMITATIONS — see [capability/reports/FORGE-WORDPRESS-FW-05-SYNTHETIC-VALIDATION-REPORT-v1.md](capability/reports/FORGE-WORDPRESS-FW-05-SYNTHETIC-VALIDATION-REPORT-v1.md)
- Lessons: [FORGE-WORDPRESS-FW-05-LESSONS-LEARNED-v1.md](capability/reports/FORGE-WORDPRESS-FW-05-LESSONS-LEARNED-v1.md)

---

## Pilot intake gates

| Gate | Requirement |
|------|-------------|
| Real frontend Production Pass | Website Factory certified `dist/` handoff |
| Operator visual approval | WV6 on client frontend before WP work |
| Project eligibility | Explicit charter; not automatic from FP-0002 |
| Environment readiness | Laragon enabled MLI-01; full Profile A validation via MLI-03 + FW-05R |
| FW-05R | **HOLD** until MLI-03 WordPress runtime profile |
| Client risk | Documented; no production deploy from Forge |
| WPilot target | Registered DEV target only via WPilot ops |
| ACF | Operator license if Pro workflow required |

---

## Probable candidate (not authorized)

FP-0002 Shpigovsky — **not** auto-eligible; requires separate FW-06 charter and frontend production pass.

---

## FW-06 authorized actions

1. Pilot charter document
2. Environment enablement checklist (operator)
3. Intake of approved frontend package
4. Full validator chain on Profile A
5. WPilot handoff to real DEV target (via WPilot, not Forge deploy)

---

## Explicit exclusions

- No `agents/registry.md` entry without operator charter
- No OPERATIONAL claim without FW-06+ evidence
- No production mutation

---

*FW-06 pilot intake input v1 — prepared after FW-05.*

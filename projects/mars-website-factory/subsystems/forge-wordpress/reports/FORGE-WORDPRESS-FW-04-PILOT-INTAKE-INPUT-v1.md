# Forge WordPress — FW-04 Pilot Intake Input v1

**Document type:** Next-stage input package  
**Version:** v1  
**Date:** 2026-06-22  
**Authorized use:** Input to **FW-04 — Pilot Intake** only

**Not pilot execution.**

---

## 1. Pilot selection criteria

| Criterion | Weight |
|-----------|--------|
| Factory frontend PRODUCTION PASS | **Required** |
| PIXEL_PERFECT or declared TEMPLATE_ART | **Required** |
| Scope bounded (Mode A static-first) | Preferred |
| Operator capacity for Local setup | **Required** |
| WPilot DEV available for handoff test | Preferred |
| No production deadline pressure | Preferred |

---

## 2. Frontend readiness requirements

- VL0–VL6 complete per production mode  
- Operator visual approval on record  
- `npm run build` reproducible  
- Handoff manifest (FW-C-01) complete  
- Known deviations documented  

---

## 3. Project identity requirements

- FP-ID assigned (execution case)  
- `project_id` creation — **FW-04/05 charter** (not FW-03)  
- Passport fields per FW-C-02  
- Implementation mode selected (A/B/C/D)  

---

## 4. Tooling readiness

Apply [FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md](../FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md) 12-point checklist.

---

## 5. Environment readiness

- Local or approved fallback installed  
- PHP 8.1+, WP-CLI, PHPCS verified  
- Playwright browsers installed  

---

## 6. Validation readiness

- WV runner priority list agreed  
- STORAGE paths for baselines  
- Validator roles assigned (human)  

---

## 7. WPilot readiness

- DEV target identified  
- Handoff contract FW-C-03 understood  
- No expectation of Forge production deploy  

---

## 8. Human approvals

G1 intake, G3 mode/WAD, G6 visual, G9 release, G10 handoff — assign before FW-05.

---

## 9. Stop conditions

- Frontend not PRODUCTION PASS  
- Tooling checklist incomplete  
- Missing operator  
- Production-only hosting with no DEV  
- Scope includes forbidden builder-as-primary without Mode B charter  

---

## 10. Candidate comparison (illustrative)

| Candidate | Frontend | Tooling | Mode | Eligibility |
|-----------|----------|---------|------|-------------|
| **FP-0002 Shpigovsky** | In progress — reports exist | Audit: gaps | Mode A likely | **NOT ELIGIBLE YET** — FW-04 must verify VL pass + tooling |
| Future greenfield | TBD | TBD | A | TBD |

---

## 11. FP-0002 evidence needed (FW-04)

- VL6 PRODUCTION PASS or explicit gap list  
- Approved HOME + key pages visual sign-off  
- `workspaces/.../FP-0002-SHPIGOVSKY/FRONTEND/` build status  
- Design completeness per Factory governance  
- Operator charter for first WP pilot  

**Current status:** WordPress **NOT STARTED**; eligibility **TBD** — not approved in FW-03.

---

## Related

- [FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md](../FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md)
- [roadmap.md](../roadmap.md)

---

*FW-04 input v1 — not intake execution.*

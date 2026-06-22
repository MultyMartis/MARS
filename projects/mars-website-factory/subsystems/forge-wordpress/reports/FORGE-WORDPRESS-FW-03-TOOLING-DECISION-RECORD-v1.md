# Forge WordPress — FW-03 Tooling Decision Record v1

**Document type:** Stage decision record  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

---

## 1. Adopted

| Decision | Choice |
|----------|--------|
| Default local environment | **Local by Flywheel** (Laragon fallback) |
| Lightweight environment | **WordPress Playground** + static reference |
| Legacy environment | **Remote DEV** via WPilot boundary |
| Repository model | Factory `FRONTEND/` + `WORDPRESS/` under FP workspace |
| Build integration | **Gulp preserved** — dist → theme assets |
| Visual regression default | **Playwright** + pixelmatch |
| WV runners (priority) | wv0, wv2, wv6, wv5, wv9 |
| Packaging stop | Release Candidate — **not** deploy |

---

## 2. Rejected defaults

| Item | Reason |
|------|--------|
| Docker/DDEV mandatory | Audit: not installed; Windows friction |
| wp-env default | Docker dependency |
| Playground sole environment | Incomplete dev surface |
| Vite auto-migration | Gulp is Factory authority |
| Percy default | SaaS cost; deferred |

---

## 3. Deferred

| Item | Trigger |
|------|---------|
| PHPStan mandatory | Custom plugin complexity |
| PHPUnit mandatory | Non-trivial logic |
| WPScan | Security charter |
| Docker profile | Team/CI charter |
| Custom MARS runner CLI | FW-05 implementation |

---

## 4. Implications

| Area | Implication |
|------|-------------|
| **Windows** | Operator must install Local + PHP stack — **not currently on audit machine** |
| **Gulp** | No pipeline replacement; sync built assets to theme |
| **Shared hosting** | PHP/MySQL parity; no container-only features |
| **WPilot** | Forge packages; WPilot operates DEV+ |
| **MARS STORAGE** | Visual baselines and ZIP artifacts |

---

## 5. Unresolved risks

| Risk | Mitigation |
|------|------------|
| Local not installed on operator PC | FW-04 checklist item 1 |
| PHP/WP-CLI absent | Block FW-05 until install |
| Visual threshold unknown | Pilot calibration FW-05 |
| FP-0002 frontend completeness | FW-04 eligibility review |
| Playwright browsers not verified | `playwright install` before WV6 |

---

## Related

- [FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](../FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md)
- [reports/FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md](FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md)

---

*FW-03 decision record v1.*

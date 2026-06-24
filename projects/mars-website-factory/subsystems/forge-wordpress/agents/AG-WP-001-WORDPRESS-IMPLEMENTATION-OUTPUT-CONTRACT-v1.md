# AG-WP-001 — WordPress Implementation Output Contract v1

**Document type:** Output contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Output maturity:** DRAFT · REVIEWABLE · OPERATOR APPROVED · DEPLOYMENT ELIGIBLE

---

## 1. Architecture outputs

| Output | Maturity default | Description |
|--------|------------------|-------------|
| Implementation mode decision | REVIEWABLE → OPERATOR APPROVED | Classic / hybrid / block — see mode decision doc |
| Theme architecture | REVIEWABLE | Template map, asset model, supports |
| Functionality-plugin architecture | REVIEWABLE | CPT, rules, integrations |
| Content model | REVIEWABLE | Types, fields, ownership |
| Editor governance model | REVIEWABLE | Curated editor boundaries |
| Plugin register | REVIEWABLE | Approved plugins with rationale |
| Security model | REVIEWABLE | Escaping, capabilities, secrets policy |
| Asset-loading model | REVIEWABLE | Enqueue strategy, build sync |

---

## 2. Source outputs

| Output | Maturity default | Location pattern |
|--------|------------------|------------------|
| Theme source | DRAFT → REVIEWABLE | `WORDPRESS/theme-source/` per project |
| Functionality plugin source | DRAFT → REVIEWABLE | `WORDPRESS/functionality/` |
| ACF JSON or equivalent | DRAFT → REVIEWABLE | Version-controlled field config |
| Approved custom blocks | DRAFT → REVIEWABLE | If mode requires |
| Templates / template parts | DRAFT → REVIEWABLE | Per template map |
| Navigation integration | DRAFT → REVIEWABLE | Menus, walkers |
| Form integration | DRAFT → REVIEWABLE | Processing boundaries |
| Build instructions | REVIEWABLE | Reproducible from approved frontend |

---

## 3. Validation outputs

| Output | Gate | Notes |
|--------|------|-------|
| PHPCS/WPCS report | Gate C | WV2 alignment |
| PHP syntax report | Gate C | All theme/plugin PHP |
| PHPUnit/integration report | Gate D/E | Where applicable |
| Playwright report | Gate E/F | Functional routes |
| Visual regression report | Gate F | Against Production Pass baselines |
| Accessibility checks | Gate G | Keyboard, labels, contrast |
| Security/plugin checks | Gate H | Provenance, versions |
| Performance baseline | Gate F/H | Local baseline only |
| Rollback package | All R2+ | Snapshot + manifest |

---

## 4. Handoff outputs

| Output | Maturity | Recipient |
|--------|----------|-----------|
| Operator review package | REVIEWABLE | Operator |
| Known deviations | REVIEWABLE | Operator + WPilot (future) |
| Unresolved SAFE UNKNOWN | REVIEWABLE | Operator |
| Deployment eligibility statement | OPERATOR APPROVED only | Operator |
| WPilot handoff contract | DEPLOYMENT ELIGIBLE | WPilot phase |
| Final Git checkpoint | OPERATOR APPROVED | MARS Git |

---

## 5. Maturity rules

| State | Meaning |
|-------|---------|
| **DRAFT** | Agent-generated; not for operator sign-off |
| **REVIEWABLE** | Complete enough for human review |
| **OPERATOR APPROVED** | Human signed; may proceed to next phase |
| **DEPLOYMENT ELIGIBLE** | All required gates passed; staging handoff allowed per charter — **not** automatic production |

Agent **cannot** mark OPERATOR APPROVED or DEPLOYMENT ELIGIBLE without human action.

---

## 6. Standards alignment

- FW-S-01–08 baseline standards
- [FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](../standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md)
- [AG-WP-001-QA-AND-ACCEPTANCE-GATES-v1.md](AG-WP-001-QA-AND-ACCEPTANCE-GATES-v1.md)

---

*Output contract v1 — distinguishes draft from deployment eligibility.*

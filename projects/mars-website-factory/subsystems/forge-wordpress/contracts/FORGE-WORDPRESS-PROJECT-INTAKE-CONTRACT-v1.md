# Forge WordPress Project Intake Contract v1

**Document type:** Intake contract  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Authority:** Forge WordPress subsystem — FWP-01 gate

**Prerequisite:** [WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md)

**Honesty:** Human-operated classification — **not** automated eligibility engine.

---

## 1. Purpose

Define **project eligibility**, environment facts, and **intake outcome** classification before Forge WordPress architecture work (FWP-02+).

Use artifact: [FORGE-WORDPRESS-PROJECT-INTAKE-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-PROJECT-INTAKE-TEMPLATE-v1.md).

---

## 2. Eligibility prerequisites

| Prerequisite | Status |
|--------------|--------|
| B1 handoff contract satisfied | Required |
| LOC-ZONE project declared | Required |
| `production_mode` declared | Required |
| Frontend reproducible build | Required |
| Operator assigned | Required |

---

## 3. Supported implementation modes

Per [FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md](../FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md):

| Mode | Intake default |
|------|----------------|
| **A** — Factory-native | Default for new Factory frontend |
| **B** — Hybrid | Requires hybrid justification |
| **C** — Legacy | Existing site + audit only |
| **D** — Specialized | **REQUIRES SPECIALIZED CHARTER** — not inferable from intake |

---

## 4. Intake questionnaire (required fields)

### 4.1 WordPress target

| Field | Required | Values / notes |
|-------|----------|----------------|
| **new site / existing site** | Yes | Greenfield vs migration/integration |
| **hosting status** | Yes | Provider, plan tier, constraints |
| **local/DEV availability** | Yes | Local WP, staging URL, or **SAFE UNKNOWN** |
| **WordPress version** | Yes | Target minimum (e.g. 6.4+) |
| **PHP version** | Yes | Host constraint |
| **plugin baseline** | If existing | Inventory or `greenfield` |
| **existing builder** | If existing | Elementor, WPBakery, etc. — Mode C signal |
| **existing content** | If existing | Volume, migration scope |
| **migration needs** | Yes | `none` \| `partial` \| `full` \| **SAFE UNKNOWN** |

### 4.2 Feature scope

| Field | Required | Notes |
|-------|----------|-------|
| **multilingual** | Yes | `no` \| WPML \| Polylang \| **SAFE UNKNOWN** |
| **ecommerce** | Yes | `no` \| WooCommerce \| **SAFE UNKNOWN** → Mode D |
| **integrations** | Yes | CRM, analytics, forms backend — list or `none` |
| **legal/compliance** | Yes | Cookie, privacy, regional rules |

### 4.3 Operations boundary

| Field | Required | Notes |
|-------|----------|-------|
| **WPilot target status** | Yes | `planned` \| `existing DEV` \| `not applicable` |
| **credentials boundary** | Yes | **No credentials in repo** — local token policy only |
| **backup status** | If existing | Last backup date or **SAFE UNKNOWN** |
| **rollback readiness** | If existing | Hosting backup, WPilot capability note |

---

## 5. Intake outcome classification

Exactly **one** primary outcome per intake review:

| Outcome | Definition | Next action |
|---------|------------|-------------|
| **ACCEPTED** | All prerequisites met; Mode A/B/C selected; proceed FWP-02 | Frontend Readiness |
| **ACCEPTED WITH CONDITIONS** | Proceed with documented conditions (e.g. reduced WV6 scope, pending staging URL) | Conditions tracked in WAD |
| **RETURN TO WEBSITE FACTORY** | B1 handoff incomplete or frontend not ready | Return packet per handoff contract |
| **REQUIRES SPECIALIZED CHARTER** | Mode D features (Woo, multisite, headless, complex ERP) | Stop — charter before FWP-02 |
| **REJECTED** | Out of scope, incompatible stack, or operator decline | Close intake; document reason |
| **SAFE UNKNOWN** | Critical facts missing — cannot classify | Hold intake; list unknowns |

---

## 6. Mode selection at intake

| Signal | Likely mode |
|--------|-------------|
| New Factory frontend, no legacy builder | **A** |
| Factory shell + block zones justified | **B** |
| Existing Elementor/WPBakery/The7 site | **C** |
| WooCommerce / multisite / headless | **D** → charter |

WAD may revise mode at FWP-03 — intake records **initial** classification.

---

## 7. Blocking conditions

| Condition | Outcome |
|-----------|---------|
| No PRODUCTION PASS | RETURN TO WEBSITE FACTORY |
| Mode D scope without charter | REQUIRES SPECIALIZED CHARTER |
| Production credentials in handoff | REJECTED — security |
| Undeclared legacy builder on "greenfield" claim | REJECTED or reclassify Mode C |
| PHP below project minimum | ACCEPTED WITH CONDITIONS or REJECTED |

---

## 8. Human gate

| Gate | Owner | Evidence |
|------|-------|----------|
| **G1** | Operator | Signed `PROJECT-INTAKE` artifact |

---

## Related documents

- [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](../FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) FWP-01
- [FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md](../FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md)
- [templates/FORGE-WORDPRESS-PROJECT-INTAKE-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-PROJECT-INTAKE-TEMPLATE-v1.md)

---

*Project intake contract v1 — FWP-01 gate; not runtime.*

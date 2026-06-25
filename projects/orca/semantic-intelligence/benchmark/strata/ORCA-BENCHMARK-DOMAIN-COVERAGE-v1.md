# ORCA Benchmark Domain Coverage v1

**Coverage set ID:** `orca-benchmark-domain-coverage`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-domain-coverage-v1.json`](orca-benchmark-domain-coverage-v1.json)

---

## Purpose

Ensure the universal benchmark spans **≥ 7 B2B service domains** so semantic admission evaluation is not overfit to a single vertical (e.g. ERP-only).

---

## Domain catalog (8 domains)

| domain_id | Label | Min share (B2) | Example verticals |
|-----------|-------|---------------:|---------------------|
| `DOMAIN_ERP_ACCOUNTING` | ERP and accounting systems | 12% | 1C, ERP implementation, bookkeeping automation |
| `DOMAIN_WEB_DEVELOPMENT` | Web development and digital products | 10% | site development, CMS, e-commerce build |
| `DOMAIN_DIGITAL_MARKETING_PPC` | Digital marketing and PPC services | 10% | context ads, SEO, analytics setup |
| `DOMAIN_IT_INFRASTRUCTURE_CLOUD` | IT infrastructure and cloud | 12% | hosting, cloud migration, backup |
| `DOMAIN_BUSINESS_CONSULTING` | Business and management consulting | 10% | process audit, CRM consulting |
| `DOMAIN_INDUSTRIAL_EQUIPMENT` | Industrial and commercial equipment | 10% | kitchen equipment, POS, warehouse tech |
| `DOMAIN_LEGAL_COMPLIANCE` | Legal and compliance services | 8% | licensing, tax compliance, contracts |
| `DOMAIN_HR_RECRUITING` | HR systems and recruiting services | 8% | HR software, outstaffing, payroll |

---

## Rules

1. **B2:** All domains present; each meets `min_share_pct` unless operator waiver with audit.
2. **B0:** Minimum 5 domains represented.
3. **Corvonero pilot:** May overweight `DOMAIN_ERP_ACCOUNTING` and `DOMAIN_DIGITAL_MARKETING_PPC` — does not remove universal domain requirements at B2.
4. Domain is **metadata** (`benchmark.domain_id`); not a substitute for `primary_intent` or `commercial_eligibility`.

---

## UNKNOWN

Historical CRM vertical splits for Corvonero corpus: **SAFE UNKNOWN** — not provable from repo; pilot sampling must document actual source mix at execution time.

# ATLAS Corvonero Domain Register v1

**Status:** **documented** — canonical Domain roster for Corvonero tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Organization anchor:** ORG-0009 **Центр автоматизации «Корво Неро»**  
**Is not:** WHOIS attestation, registrar proof.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **active** | **1** (DOM-CORV-01) |
| Domain OWNS edges | **0** *(by design — registrant SAFE UNKNOWN)* |
| Attestation | **Complete** — AT-CORV-DOM-01 |

---

## 2. Population roster — full table

| domain_id | canonical_name | hostname_class | primary_org_candidate | primary_website_candidate | evidence_tier | owner / registrar | lifecycle_state | attestation | notes |
|-----------|----------------|----------------|----------------------|---------------------------|---------------|-------------------|-----------------|-------------|-------|
| DOM-CORV-01 | corvonero.ru | **apex** | ORG-0009 Корво Неро *(display)* | WEB-CORV-01 lk.corvonero.ru *(subdomain site)* | **E0** | **SAFE UNKNOWN** | **active** | AT-CORV-DOM-01 | Apex zone; `lk.corvonero.ru` treated as subdomain surface — separate DOM for `lk.*` **not** minted per intake charter |

---

## 3. Hostname policy note

| Hostname | Entity | Policy |
|----------|--------|--------|
| `corvonero.ru` | DOM-CORV-01 | Apex Domain entity |
| `lk.corvonero.ru` | WEB-CORV-01 | Website on subdomain; linked via **POINTS_TO** (DOM-CORV-01 → WEB-CORV-01) — not separate DOM entity in this pass |

**Rationale:** Operator intake specifies single DOM candidate `corvonero.ru` with subdomain relationship to `lk.corvonero.ru`. Differs from Triumph `blog.gktriumph.ru` separate-DOM pattern — documented steward choice for Corvonero tranche.

---

## 4. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| CORV-DOM-D-01 | `corvonero.ru` hostname uniqueness | **Pass** | No |
| CORV-DOM-D-02 | vs DOM-0001..0004 / DOM-ZPM-01 / DOM-SHPIG-01 | **Distinct** | No |

**Duplicate review summary:** **Pass**

---

## 5. Evidence index

| Ref | Artifact | Domains supported |
|-----|----------|-------------------|
| EV-CORVONERO-OP-01 | [CORVONERO-BUSINESS-INTAKE-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md) | DOM-CORV-01 — apex stem from site URL |
| EV-CORVONERO-OP-02 | Operator statement — lk.corvonero.ru | Subdomain structure corroboration |

---

*ATLAS Corvonero Domain Register v1 — DOM-CORV-01 **active**; owner **SAFE UNKNOWN**.*

# ATLAS Corvonero Commercial Relationship Register v1

**Status:** **documented** — canonical Organization ↔ Organization commercial edge for Corvonero tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Vendor anchor:** ORG-0003 **i-SEO**  
**Client anchor:** ORG-0009 **Центр автоматизации «Корво Неро»**  
**Parent:** [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md)  
**Is not:** Agreement Layer (AGR-*), Polygon commercial edge.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Relationship type | **CLIENT_OF** only |
| Lifecycle **active** | **1** (REL-0042) |
| Attestation | **Complete** — AT-CORV-REL-01 |

**Identifier note:** REL-0042 is next sequential org↔org commercial id after REL-0041 (Wave 6B). Distinct from REL-CORV-* slug namespace used for project/website/domain families.

---

## 2. Relationship roster — full table

| relationship_id | source_id | target_id | relationship_type | evidence_tier | lifecycle_state | attestation | notes |
|-----------------|-----------|-----------|-------------------|---------------|-----------------|-------------|-------|
| REL-0042 | ORG-0009 Центр автоматизации «Корво Неро» | ORG-0003 i-SEO Studio | **CLIENT_OF** | **E0** | **active** | AT-CORV-REL-01 | Real i-SEO client; vendor context ORG-0003 — **not** ORG-0001 Полигон |

---

## 3. Commercial graph extension

```text
ORG-0009 Корво Неро ──CLIENT_OF──► ORG-0003 i-SEO   [REL-0042 — Corvonero tranche]
```

**Explicit non-edges:**

| Pair | Status |
|------|--------|
| ORG-0009 → ORG-0001 **CLIENT_OF** | **Not created** — operator restriction |
| ORG-0009 → ORG-0001 any REL-* | **Not created** |

---

## 4. Evidence index

| Ref | Artifact | Role |
|-----|----------|------|
| EV-CORVONERO-OP-01 | [CORVONERO-BUSINESS-INTAKE-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md) | «реальный клиент i-SEO» — E0 commercial signal |
| ORG-0003 | Attested vendor (Wave 1) | Vendor endpoint |

---

*ATLAS Corvonero Commercial Relationship Register v1 — REL-0042 **active**.*

# ROC-02 — Catalog Entry (FP-0001)

**Class:** ROC-02  
**Record plane:** RT-G05 Registry  
**Factory Project:** FP-0001  
**Registry entry:** REG-0001  
**Created:** 2026-06-07  

---

## Catalog entry composition

One discoverability slot per logical Factory Project. Hosted within [POC-02 registry facet](../../POC-02-registry-binding-carrier.md).

| Class | Carrier |
|-------|---------|
| ROC-03 Registry entry identity | [ROC-03-registry-entry-identity.md](ROC-03-registry-entry-identity.md) |
| ROC-04 Logical identity reference | [ROC-04-logical-identity-reference.md](ROC-04-logical-identity-reference.md) |
| ROC-05 Manifest pointer | [ROC-05-manifest-pointer.md](ROC-05-manifest-pointer.md) |
| ROC-06 Distinction summary | [ROC-06-distinction-summary.md](ROC-06-distinction-summary.md) |
| ROC-07 Discoverability status | [ROC-07-discoverability-status.md](ROC-07-discoverability-status.md) |
| ROC-09 Enrollment bind metadata | [ROC-09-enrollment-bind-metadata.md](ROC-09-enrollment-bind-metadata.md) |
| ROC-10 Amendment narrative | [ROC-10-amendment-narrative.md](ROC-10-amendment-narrative.md) |

---

## Two-identifier discipline (R-R3)

| ID type | Value |
|---------|-------|
| Registry entry ID (ROC-03) | **REG-0001** |
| Logical Factory Project ID (ROC-04) | **FP-0001** |

**Rule:** ROC-03 **≠** ROC-04 (ES-03, RA-03).

---

*Exactly one ROC-02 per logical Factory Project identity (ROC-RULE-02).*

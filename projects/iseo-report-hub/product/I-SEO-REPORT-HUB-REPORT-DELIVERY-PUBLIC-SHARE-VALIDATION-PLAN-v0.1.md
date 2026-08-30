# I-SEO Report Hub — Report Delivery / Public Share Validation Plan v0.1

**Status:** VALIDATION POLICY ONLY — no execution beyond optional read-only baseline in charter wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Delivery / Public Share Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Baseline validation (charter / pre-DB-10)

Confirm before any share schema/code wave:

| Check | Expected |
|-------|----------|
| DB target | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **8** |
| tables | **15** |
| report_exports | **4** (html **2**, pdf **2**) |
| ids 1–2 metadata | NULL / legacy |
| ids 3–4 metadata | filled; id **4** `source_html_export_id=3` |
| Artifact checksums | v1/v2 HTML/PDF match known SHA-256 |
| Public share | **none**; `/share` not a working delivery surface |
| Auth downloads | still the only delivery path |

Charter wave itself must leave DB/artifacts/routes unchanged.

---

## 2. DB-10 migration validation

After DB-10 apply:

| Check | Expected |
|-------|----------|
| `report_export_shares` exists | yes |
| schema_migrations | **9** (confirm in wave) |
| tables | **16** (confirm in wave) |
| columns / indexes / FKs | match plan |
| share row count | **0** |
| report_exports count / metadata | **unchanged** |
| artifacts | unchanged |
| public route | still absent |
| no token plaintext column | confirmed |

---

## 3. Token creation validation (implementation)

| Check | Expected |
|-------|----------|
| Eligible export id **4** | create allowed for permitted roles |
| Token entropy | ≥ 32 bytes random |
| DB stores hash only | plaintext absent from DB |
| token_hash unique | enforced |
| Plaintext URL | shown once at create; not reloadable |
| Default expiry | ~30 days |
| Audit | `share_created` |
| CSRF / role gate | required |
| Ineligible create | denied (HTML, legacy, non-ready) |

---

## 4. Public route validation

| Check | Expected |
|-------|----------|
| Active token | streams PDF |
| Content-Type | `application/pdf` |
| Content-Disposition | attachment |
| No export id required in URL | opaque token only |
| No storage path in response | yes |
| Auth session | not required |
| access_count | increments on success |
| Audit | `share_accessed` |

---

## 5. Expired / revoked denial

| Check | Expected |
|-------|----------|
| Revoked token | generic 404/410; audit `share_denied_revoked` |
| Expired token | generic 404/410; audit `share_denied_expired` |
| No public reason detail | yes |

---

## 6. Checksum / missing artifact denial

| Check | Expected |
|-------|----------|
| Missing file | denial; audit `share_denied_missing_artifact` |
| Checksum mismatch | denial; audit `share_denied_checksum_mismatch` |
| No partial corrupt delivery | yes |

---

## 7. Legacy / non-PDF denial

| Check | Expected |
|-------|----------|
| Export id **1** HTML v1 | not shareable |
| Export id **2** PDF v1 legacy | not shareable in MVP |
| Export id **3** HTML v2 | not shareable in MVP |
| Export id **4** PDF v2 | shareable |
| Non-ready status | denied |

---

## 8. Audit / access count

| Check | Expected |
|-------|----------|
| Successful access | `access_count` +1; `last_accessed_at` set |
| Failed access | count not incremented (or only success path increments — enforce consistently) |
| Plaintext token | never in audit payload |
| Optional IP/UA | hashed only if stored |

---

## 9. Security headers

On successful public download verify:

- `Content-Type: application/pdf`
- `Content-Disposition: attachment…`
- `X-Content-Type-Options: nosniff`
- `Cache-Control` private/no-store (or agreed conservative equivalent)
- `X-Robots-Tag: noindex, nofollow`

---

## 10. No public listing

| Check | Expected |
|-------|----------|
| `GET /share` | no directory of tokens/exports |
| `GET /share/report/` | no listing |
| Storage URL browse | not exposed |
| Public docroot | no export files added |

---

## 11. No secrets

| Check | Expected |
|-------|----------|
| `.env` / `.env.local` | unchanged unless separate charter |
| Docs / Git | no DB passwords, no plaintext tokens |
| Logs | no plaintext tokens / avoid full share URLs |
| Auth downloads | still work without share feature regressions |

---

## 12. STOP conditions

STOP validation / wave if:

- wrong DB target;
- plaintext token persisted;
- public path or absolute storage path exposed;
- artifacts regenerated unexpectedly;
- `report_exports` rows mutated without charter;
- HTML public share shipped in MVP without new decision;
- foreign WIP / unsafe staging for i-SEO;
- push without authorization;
- package install without charter.

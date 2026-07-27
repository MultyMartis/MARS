# I-SEO Report Hub — Report Delivery / Public Share Security Model v0.1

**Status:** SECURITY POLICY ONLY — no tokens / routes / DB changes in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Delivery / Public Share Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md)

---

## 1. Purpose

Зафиксировать security model для tokenized public share: generation, storage, expiry/revoke, delivery hardening, headers, denial, audit, abuse baseline, privacy risks, non-goals.

---

## 2. Token generation

| Rule | Requirement |
|------|-------------|
| Entropy | Cryptographically secure random, **≥ 32 bytes** |
| Encoding | URL-safe opaque string (e.g. base64url / hex) |
| URL shape | `/share/report/{token}` — token only; **no** export id |
| Secrets in URL | Token is the only capability secret; no other client secrets |

---

## 3. Token hashing / storage

| Rule | Requirement |
|------|-------------|
| DB stores | **token hash only** — never plaintext token |
| Hash | SHA-256 of token (or stronger app-level keyed hash if later chartered) |
| Uniqueness | Unique index on `token_hash` |
| Compare | Timing-safe comparison where practical |
| Display | Plaintext token / full URL shown **once** at creation |
| Re-display | Not available later from DB |
| Logs | **Do not** log plaintext token; avoid logging full share URL where avoidable |

---

## 4. Expiry / revoke

| Rule | Requirement |
|------|-------------|
| Default expiry | **30 days** from creation |
| Shorter expiry | Allowed later via create form / API |
| Revoke | Supported for `admin_owner` / `seo_lead_reviewer` |
| Expired / revoked public response | Generic **404** or **410** — **no** reason detail |
| Status | Persist `revoked`; expiry may be status or computed from `expires_at` |

---

## 5. Delivery path hardening

| Rule | Requirement |
|------|-------------|
| Storage root | Existing exports root under runtime storage — **outside** public docroot |
| Path resolution | Relative path only; reject `..`, absolute paths, symlink escape |
| No raw path exposure | Never put storage absolute path in URL, HTML, headers, or error bodies |
| No public copy | Do not write artifact into `public/` |
| No directory listing | No index of `/share` or storage |
| Checksum | Recompute / verify against `report_exports.checksum_sha256` **before** stream |
| MIME | Expect PDF for MVP; reject non-PDF eligibility at policy layer |
| Size / magic | Reuse existing PDF hardening (`%PDF`, size bounds) where applicable |

---

## 6. Response headers (public success)

| Header | Value / intent |
|--------|----------------|
| `Content-Type` | `application/pdf` |
| `Content-Disposition` | `attachment; filename="<safe-basename>.pdf"` |
| `X-Content-Type-Options` | `nosniff` |
| `Cache-Control` | Conservative: `private, no-store` (or equivalent no-cache for token route) |
| `X-Robots-Tag` | `noindex, nofollow` |

HEAD support: optional; **not** MVP.

---

## 7. Denial behavior

Public denials (unknown token, expired, revoked, ineligible export, missing artifact, checksum mismatch, max access exceeded later):

- generic **404** or **410**;
- no distinction that helps attackers enumerate valid tokens vs revoked vs expired beyond what is unavoidable;
- no storage path, DB id dump, stack trace, or SQL detail;
- audit specific deny reason **internally** only.

Internal create/revoke denials use normal auth/CSRF/role errors (not public surface).

---

## 8. Logging / audit

Required audit events:

- `share_created`
- `share_revoked`
- `share_accessed`
- `share_denied_expired`
- `share_denied_revoked`
- `share_denied_missing_artifact`
- `share_denied_checksum_mismatch`

Optional hashed telemetry fields:

- `last_access_ip_hash`
- `last_user_agent_hash`

Access count increments only on successful delivery.

Do not store plaintext IP/UA if hashed fields are used; do not log tokens.

---

## 9. Abuse baseline

MVP baseline (implementation wave must include minimal controls):

- rely on opaque high-entropy tokens (no enumerable export ids in public URL);
- rate-limit / abuse consideration for `/share/report/{token}` (exact limiter implementation chartered in implementation wave — at minimum document intent: throttle repeated invalid token probes);
- no public listing endpoints;
- revoke + expiry always available;
- checksum gate stops corrupted/tampered artifact delivery.

Not MVP: WAF product, captcha, geo-block, IP allowlists.

---

## 10. Privacy risks

| Risk | Mitigation |
|------|------------|
| URL forwarding / chat leakage | Expiry + revoke; short operational guidance; no re-display |
| Token in access logs / referrers | Avoid logging full URL; Cache-Control private/no-store; noindex |
| Over-sharing HTML source | PDF-only MVP |
| Legacy unstyled / unrecorded exports | Deny legacy / null template metadata |
| Path disclosure | Stream-only; generic errors |
| Client identity confusion | Token is capability link, not login — document as such |

---

## 11. Role model (security view)

| Capability | Roles |
|------------|-------|
| Create / revoke | `admin_owner`, `seo_lead_reviewer` |
| Internal share UI | Internal authenticated roles only |
| Public download | Token bearer only — no session required |

CSRF required on internal create/revoke POSTs. Public GET is token-authenticated capability URL.

---

## 12. Explicit non-goals

- no client portal auth;
- no email transport security design in this wave;
- no one-time link enforcement in MVP;
- no secrets in `.env` beyond existing app secrets (no share-signing secret required if hash-of-random-token model is used);
- no production CDN public bucket;
- no directory browse;
- no absolute path in any client-visible surface;
- no implementation / token minting in this charter wave.

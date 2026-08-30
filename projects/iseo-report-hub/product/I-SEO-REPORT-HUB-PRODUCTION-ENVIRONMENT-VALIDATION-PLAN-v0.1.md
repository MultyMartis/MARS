# I-SEO Report Hub — Production Environment Validation Plan v0.1

**Status:** FUTURE VALIDATION PLAN ONLY — no server access; no deploy; no commands against production hosts in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Charter 01  
**Related:** [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-REQUIREMENTS-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-REQUIREMENTS-v0.1.md)

---

## 1. Purpose

Describe **future** validation steps after operator Decision 01 (and optionally Validation 01 wave), so production implementation does not proceed on assumptions.

This document does **not** authorize SSH, DNS, certificate, or deploy actions now.

---

## 2. Pre-decision validation (docs / local only)

May run before Decision 01 without production host:

| Check | Intent |
|-------|--------|
| Confirm local MVP gates A–D still documented PASS | Baseline for functional parity |
| Confirm artifact checksums still match attested set | Export integrity continuity |
| Optional local MySQL read-only probe | Resolve SAFE UNKNOWN if MySQL available |
| Confirm no production secrets in Git | Preflight hygiene |
| Confirm public route design unchanged | `/share/report/{64hex}` |

If local MySQL refused: record SAFE UNKNOWN; do not invent live counts.

---

## 3. Server access validation (future)

After operator provides host access charter:

| Check | Pass criteria |
|-------|---------------|
| SSH/panel access works for designated operators only | Least privilege; no shared root habit undocumented |
| OS identity recorded | Linux distro/version (or approved alternative) |
| Firewall baseline | 22/80/443 (or approved set) only as needed |
| Timezone set explicitly | Matches operator decision |

---

## 4. PHP / extensions validation (future)

| Check | Pass criteria |
|-------|---------------|
| `php -v` | Matches Decision 01 pin (prefer 8.3.x) |
| Required extensions | `pdo`, `pdo_mysql`, `mbstring`, `json`, `openssl`, `fileinfo`, `session` present |
| Recommended extensions | `intl`, `curl`, `dom`/`xml`, `iconv`, `gd` present or waiver documented |
| `display_errors` | Off in production pool |
| PHP-FPM pool user | Not running as root; can write only shared storage/logs |

---

## 5. DB connectivity validation (future)

| Check | Pass criteria |
|-------|---------------|
| Connect as app user to **production** DB name | Success; not `iseo_report_hub_dev` |
| Charset | utf8mb4 |
| Privileges | CRUD on app tables; no unnecessary SUPER/FILE |
| Network | Not publicly writable from internet without need |

---

## 6. Public docroot validation (future)

| Check | Pass criteria |
|-------|---------------|
| Webserver docroot | Points to `…/public` only |
| Direct URL to storage path | **404** / forbidden |
| Front controller | App routes resolve |
| Directory listing | Disabled |

---

## 7. Storage outside public validation (future)

| Check | Pass criteria |
|-------|---------------|
| Export storage path | Outside docroot |
| Symlink/shared storage | Writable by app user; not web-served |
| Sample artifact | Readable by app; not by anonymous HTTP path guess |

---

## 8. HTTPS / domain validation (future)

| Check | Pass criteria |
|-------|---------------|
| Domain resolves to intended host | Matches Decision 01 |
| TLS certificate valid | Trusted chain; not expired |
| HTTP→HTTPS redirect | Enforced |
| `APP_URL` | HTTPS base matches certificate host |
| HSTS | Optional later; document if enabled |

---

## 9. Headless browser / PDF validation (future)

Only if Decision 01 selects on-host generation (mode P1):

| Check | Pass criteria |
|-------|---------------|
| Browser binary exists | Chromium/Chrome/Edge or approved equivalent |
| Headless PDF smoke | Produces valid `%PDF` from known HTML fixture |
| Fonts | RU text renders without tofu/missing glyphs for template |
| Permissions | App user can invoke binary |
| Resource limits | Job fails safely under timeout without hanging pool |

If P2/P3 selected: validate upload/serve path instead; do not claim headless on host.

---

## 10. Migration dry-run plan (future)

| Step | Rule |
|------|------|
| 1 | Empty or controlled prod DB |
| 2 | Backup dump first |
| 3 | Dry-run / review migration list (schema_migrations expected path) |
| 4 | Apply once under charter |
| 5 | Verify migration count / critical tables |
| 6 | **No** local fixture bootstrap against prod |

---

## 11. Backup / restore validation (future)

| Check | Pass criteria |
|-------|---------------|
| DB dump created | Restorable to scratch DB |
| Storage backup | Artifacts recoverable |
| Retention | Policy documented |
| Restore drill evidence | Recorded before real client use |
| Code rollback | Previous release symlink works |

---

## 12. Public share route validation (future)

| Check | Pass criteria |
|-------|---------------|
| Valid token | Streams PDF with hardened headers |
| Malformed/invalid | 404 |
| Revoked/expired/max_access | 410 |
| No listing | `/share` not an index of shares |
| No `/r/{token}` | Absent |
| HTTPS only | Client URL uses HTTPS |

Use **non-production** or disposable tokens in controlled tests; never publish live client tokens in reports.

---

## 13. Auth / CSRF validation (future)

| Check | Pass criteria |
|-------|---------------|
| Unauthenticated internal routes | Redirect/deny |
| Login | Works with production admin (securely created) |
| CSRF | Write actions reject missing/invalid token |
| Session cookie | Secure + HttpOnly on HTTPS |

---

## 14. Logging / token URL sensitivity validation (future)

| Check | Pass criteria |
|-------|---------------|
| Access log path permissions | Restricted operators only |
| Rotation | Configured |
| Sample share hit | Demonstrates token appears in path ⇒ treat as secret material |
| App logs | No plaintext tokens dumped unnecessarily |
| Operator reports | No live tokens |

---

## 15. Rollback validation (future)

| Check | Pass criteria |
|-------|---------------|
| Release rollback | Previous code live within agreed RTO |
| DB rollback plan | Explicit (forward-fix vs restore dump) |
| Active shares | Revoke or pause procedure tested if delivery impacted |

---

## 16. STOP conditions for future validation/implementation

STOP if:

- Decision 01 incomplete on host/domain/HTTPS/PDF/deploy/backup;
- Docroot not `/public`;
- Storage served publicly;
- Secrets in Git or pasted into tickets;
- Prod pointed at `iseo_report_hub_dev`;
- No backup before migration;
- Headless claimed but unvalidated when P1 in scope;
- Live client tokens written into docs/evidence.

---

## 17. Out of scope for this charter wave

- Any production SSH/DNS/TLS/deploy commands
- Any DB mutation
- Any share token creation
- Any package install
- Any app-source/runtime edits

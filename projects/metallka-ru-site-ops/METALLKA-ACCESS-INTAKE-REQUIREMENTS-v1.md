# METALLKA — Access Intake Requirements v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** ACCEPTED (Phase 2A — preparation)  
**Date:** 2026-07-25  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Site:** `https://metallka.ru/`  

**Purpose:** Define **non-secret** facts the operator will eventually need to provide or confirm before / during Gate A.

```text
Do NOT request username/password in this document.
Credentials must NOT be sent to Web-GPT chat and must NOT be stored in tracked files.
```

This document does **not** authorize production access, secret creation, or local bootstrap.

Related: [METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md](METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md)

---

## 1. Secret policy (exact rule)

| Rule | Status |
|------|--------|
| Credentials must **not** be sent to Web-GPT / Cursor chat | **MANDATORY** |
| Credentials must **not** be stored in tracked Git files | **MANDATORY** |
| Future approved local contour follows MARS / WPilot local-storage policy | **MANDATORY** |
| Exact secret filenames | **DECISION REQUIRED** until access phase |
| Create local dirs/files in Phase 2A | **FORBIDDEN** |

### 1.1 Naming recommendation only (do not create)

| Role | Recommended path (future) |
|------|---------------------------|
| Potential future site metadata root | `X:\AI MARS\local\sites\metallka-ru-production\` |
| Potential future token root | `X:\AI MARS\local\tokens\` |
| Suggested site alias | `metallka-ru-production` |

Policy basis: `projects/wpilot/local-storage-policy.md` (Git ignore `/local/`).  
ISEO precedent pattern (metadata vs secrets separation): `projects/iseo-su-site-ops/ISEO-SU-LOCAL-ACCESS-MODEL-v1.md` — **patterns only**.

Exact filenames for `site-profile.json`, `secrets.local.md`, or WPilot token files remain **DECISION REQUIRED** until an authorized access-preparation phase.

---

## 2. Category A — Hosting

Non-secret confirmations needed later:

| Item | What to confirm | Notes |
|------|-----------------|-------|
| Provider | Hosting brand / product | e.g. Beget / other / SAFE UNKNOWN |
| Control panel type | Panel product / URL class | URL only — no password |
| Operator panel access | Yes / No / Uncertain | Capability only |
| Backups exist | Yes / No / Uncertain | Mechanism TBD in discovery |
| Staging exists | Yes / No / Uncertain | Separate from production |

Do **not** paste panel passwords into chat or programme markdown.

---

## 3. Category B — WordPress Admin

| Item | What to confirm | Notes |
|------|-----------------|-------|
| Admin URL | Public admin path if known | e.g. `/wp-admin/` — metadata only |
| Operator has login | Yes / No / Uncertain | Capability only |
| 2FA exists | Yes / No / Uncertain | Note class only — **no** backup codes |
| Access role / class | Admin / Editor / other / Uncertain | Role class, not credentials |

**Do not request username or password in this document or in Phase 2A REPORT.**

---

## 4. Category C — FTP / SFTP

Need only **metadata** initially:

| Item | What to confirm |
|------|-----------------|
| Protocol | FTP or SFTP (or uncertain) |
| Host class | Hosting FTP/SFTP hostname class (not password) |
| Port | Only if non-standard |
| Expected docroot | Path shape if known (sanitize account segments later) |
| Operator already has credentials | Yes / No / Uncertain |

Secrets must later be placed **only** in an approved local secret contour (not yet created).

---

## 5. Category D — Database

| Item | What to confirm |
|------|-----------------|
| DB panel / phpMyAdmin / direct DB access exists | Yes / No / Uncertain |
| Credentials | **Not requested yet** |

DB access for Gate A is optional and requires separate authorization if used.

---

## 6. Category E — Existing source

Ask later (non-secret):

| Item | What to confirm |
|------|-----------------|
| Roman / developer Git or source backup | Exists / Absent / Uncertain |
| Old developer files | Exists / Absent / Uncertain |
| Theme source archive | Exists / Absent / Uncertain |
| Custom plugin source | Exists / Absent / Uncertain |

Until source authority is attested, production runtime remains **provisional authority** (programme charter §6).

---

## 7. Category F — Backup authority

Need to establish (facts, not execution in Phase 2A):

| Item | What to confirm |
|------|-----------------|
| Who can create backup | Operator / host / other |
| How restore works | Hosting-native / other |
| Hosting-native mechanism | Beget or other — class only |
| Retention | Known / SAFE UNKNOWN |
| Rollback responsibility | Named operator role |

Gate A does **not** require creating a backup unless separately directed. Later mutation gates will require backup proof.

---

## 8. Operator confirmation checklist (after Phase 2A — no secrets)

Compact list for the operator. Confirm only:

1. Hosting provider.  
2. Whether operator has hosting panel access.  
3. Whether WP Admin access exists.  
4. Whether FTP or SFTP access exists.  
5. Whether there is known staging / dev.  
6. Whether a hosting backup can be created / restored.  
7. Whether source / Git / theme archive exists outside production.  
8. Whether operator authorizes Gate A later (via the project approval string).

Credentials themselves must be handled separately through an approved local secret workflow (future phase — not Phase 2A).

---

## 9. Explicit exclusions

- Asking for passwords, tokens, cookies, or 2FA backup codes in chat  
- Creating local secret directories or files in Phase 2A  
- Treating capability confirmation as access authorization  
- Filling SAFE UNKNOWN from ISEO / triumph / FP-0002 analogy  

---

*Access Intake Requirements v1 · Phase 2A · no secrets · no access.*

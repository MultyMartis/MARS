# ISEO-SU ACCESS CLASSIFICATION v1

**Programme:** ISEO-SU-SITE-OPS  
**Phase:** 2B — read-only production audit executed  
**Status:** ACCEPTED as documentary model  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Last updated:** 2026-07-24 (Phase 2B)

Purpose: define **access classes without storing access data**.  
No passwords, tokens, cookies, or secret-bearing connection strings are stored here.

Local-only credentials: `X:\AI MARS\local\sites\iseo-su-production\` (Git-ignored).

---

## Capability vs authorization (post–Phase 2B)

| Access capability | Exists? | Authorization status |
|-------------------|---------|----------------------|
| Hosting / Beget panel | Yes | Panel login by agent still **NOT AUTHORIZED** (A3 panel). Filesystem read via SFTP used under A5. |
| FTP or SFTP | Yes | **A5 USED** in Phase 2B (read-only SFTP). Further use needs per-task charter. |
| WordPress administrator | Yes (dedicated MARS account configured locally) | **A4 AUTHORIZED for Phase 2B read-only**; Admin UI via HTTP client blocked by JS challenge; compensated with REST + SFTP. Further Admin use needs charter + preferably browser HITL. |
| WPilot | Not installed | A6 **NOT AUTHORIZED** |
| Database / phpMyAdmin | Metadata URL known | **NOT AUTHORIZED** |

phpMyAdmin metadata URL (non-secret): `https://mayday.beget.com/phpMyAdmin/` — do not open without DB charter.

Beget panel host (from local profile, non-secret): `cp.beget.com`.

---

## Class summary

| Class | Name | Current project status |
|-------|------|------------------------|
| **A0** | PUBLIC / NO AUTH | Used in Phase 2B for limited classification GETs + public REST under audit charter |
| **A1** | OPERATOR SCREENSHOT ONLY | Allowed when manually supplied |
| **A2** | SANITIZED EXPORT | Allowed when manually supplied |
| **A3** | HOSTING READ-ONLY | Panel login **NOT AUTHORIZED**; filesystem aspect covered via A5 |
| **A4** | WORDPRESS READ-ONLY | **Phase 2B executed (partial Admin UI)**; default returns to charter-gated |
| **A5** | FTP/SFTP READ-ONLY | **Phase 2B executed**; default returns to charter-gated |
| **A6** | WPILOT READ-ONLY | **NOT AUTHORIZED** |
| **A7** | CONTROLLED WRITE | **NOT AUTHORIZED** |
| **A8** | EMERGENCY ROLLBACK | **NOT AUTHORIZED** |

---

## A0 — PUBLIC / NO AUTH

Document public pages/URLs. Phase 2B used bounded public GET/REST for architecture classification under explicit operator authorization for this task. Not a standing crawl license.

---

## A1 — OPERATOR SCREENSHOT ONLY

Unchanged — allowed when manually supplied and redacted.

---

## A2 — SANITIZED EXPORT

Unchanged — allowed when manually supplied.

---

## A3 — HOSTING READ-ONLY

Beget **panel** browse/login by agent remains blocked unless separately chartered.  
Do not confuse with A5 SFTP file listing.

---

## A4 — WORDPRESS READ-ONLY

Phase 2B: dedicated MARS admin credentials used only for read attempts.  
No settings saves, updates, installs, activations, exports of secrets, or token creation.  
Residual: Admin UI JS challenge → prefer browser HITL for Admin-only screens.

---

## A5 — FTP/SFTP READ-ONLY

Phase 2B: SFTP listing + bounded file reads.  
Forbidden: upload, delete, chmod, mirror entire site, timestamp tricks.

---

## A6 — WPILOT READ-ONLY

Blocked until Phase 4B decision + install/token charters. Plugin currently **absent**.

---

## A7 — CONTROLLED WRITE

Not authorized. Operator full Beget backup does not replace task scope, validation, rollback, HITL, evidence.

---

## A8 — EMERGENCY ROLLBACK

Not invoked.

---

## Phase 2B posture note

Phase 2B temporarily exercised A4/A5 under an explicit charter. After closeout, treat A3–A8 as **requiring a new charter** before reuse.

---

*Access classification v1 · updated 2026-07-24 Phase 2B · no access secrets stored.*

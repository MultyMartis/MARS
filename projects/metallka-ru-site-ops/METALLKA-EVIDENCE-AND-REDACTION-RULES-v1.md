# METALLKA — Evidence and Redaction Rules v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** ACCEPTED (Phase 2A — preparation)  
**Date:** 2026-07-25  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Site:** `https://metallka.ru/`  

**Purpose:** Define what may be retained as Gate A / Phase 2B evidence and what must be redacted or never stored.

```text
REPORT must never contain secret material.
```

Related: [METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md](METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md)  
Precedent pattern (not metallka facts): `projects/iseo-su-site-ops/ISEO-SU-EVIDENCE-REDACTION-GUIDE-v1.md`

---

## 1. Allowed evidence

May be recorded in programme docs / reports when sanitized:

| Category | Examples |
|----------|----------|
| Versions | WordPress, PHP, theme, plugin versions |
| Plugin / theme names | Active / inactive inventory names |
| File paths | Sanitized paths (account segments redacted) |
| Hashes | SHA-256 of inspected files (non-secret content) |
| Screenshots | Without secrets in frame / address bar |
| Page IDs | Numeric WP IDs |
| Template names | Theme / page template slugs |
| Non-sensitive configuration | Permalink structure, language, timezone class |
| HTTP status | Status codes from authorized inspection |
| Response headers | Non-secret header names/values (redact auth) |
| Sanitized excerpts | Short structural excerpts without secrets |
| File inventory | Directory / file name inventories |
| Source / runtime comparisons | Authority notes without secret payloads |

---

## 2. Must redact / must not store

| Category | Examples |
|----------|----------|
| Passwords | Panel, FTP/SFTP, WP, DB, mail |
| FTP / SFTP credentials | Username+password pairs, private keys |
| Tokens | WPilot tokens, application passwords, reset tokens |
| Token hashes | Credential hashes from options / DB |
| Cookies | `wordpress_logged_in_*`, session cookies |
| Session IDs | Any session identifier strings |
| WP salts | `AUTH_KEY`, `SECURE_AUTH_KEY`, and related constants |
| API keys | Any key-like string |
| SMTP password | Mail auth secrets |
| DB password | MySQL / MariaDB credentials |
| Private keys | SSH / TLS private material |
| Webhook secrets | CRM / form webhook secrets |
| Personal user data not required | Emails, phones, user dumps |
| Secret values from `wp-config` | DB creds, salts, custom secret constants |
| Access logs with sensitive query strings | Unsanitized logs containing `token=`, `key=`, `pwd=` |

If unsure whether a string is a secret: **redact it**.

---

## 3. REPORT / chat / Git rules

| Surface | Rule |
|---------|------|
| Programme REPORT | Never contain secret material |
| Cursor / Web-GPT chat | Never paste credentials or token values |
| Tracked Git files | No secrets; `/local/` remains Git-ignored when used later |
| Screenshots | Crop; blur secrets; check address bar and toasts |
| `wp-config.php` | Do not paste full file into docs or chat |
| DB dumps / full archives | Not Phase 2A / Gate A evidence defaults |

---

## 4. Path sanitization

Replace account-identifying home path segments:

```text
/home/ACCOUNT/...  →  /home/[REDACTED]/...
```

Retain useful shape (domain folder, `public_html`, `wp-content/...`) when needed for ops.

---

## 5. Incident if a secret is exposed

1. Stop further paste / copy.  
2. Notify the operator immediately.  
3. Treat as security incident: rotate / revoke exposed credential.  
4. Do not re-paste the value into chat or Git.  
5. Record only sanitized incident note (what class leaked — not the value).  

---

## 6. Phase 2A note

No production evidence is collected in Phase 2A. These rules apply to **future** Gate A / Phase 2B work and to any operator-supplied screenshots / exports after Phase 2A.

---

*Evidence and Redaction Rules v1 · Phase 2A preparation.*

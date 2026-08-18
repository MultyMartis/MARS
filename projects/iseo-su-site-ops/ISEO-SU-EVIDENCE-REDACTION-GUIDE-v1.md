# ISEO-SU EVIDENCE REDACTION GUIDE v1

**Audience:** Operator preparing Phase 2 evidence  
**Programme:** ISEO-SU-SITE-OPS  
**Status:** ACTIVE  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  

Goal: share enough structure to map the hybrid site **without** leaking secrets into chat or Git.

---

## 1. Must redact (always)

Before sending screenshots, exports, or pasted text, remove or obscure:

| Category | Examples |
|----------|----------|
| Passwords | Panel, FTP, WP, DB, mail |
| Tokens | API tokens, application passwords, WPilot tokens, reset tokens |
| Cookies / session IDs | Browser cookie strings, `wordpress_logged_in_*`, session notices with IDs |
| Auth headers | `Authorization: …`, `X-WPilot-Token: …` |
| Unnecessary usernames | Panel login names, WP usernames when not needed |
| Unnecessary private emails | Personal or client emails in screenshots |
| FTP/DB hosts when not needed | Hostnames that are only useful with credentials |
| IPs when not needed | Server/client IPs in panel headers |
| License keys | Theme/plugin license strings |
| API keys / webhook secrets | Any key-like string |
| SMTP credentials | User/password/host auth material |
| WordPress salts | `AUTH_KEY`, `SECURE_AUTH_KEY`, and related constants |
| Account-identifying home paths | `/home/ACCOUNT/…` → `/home/[REDACTED]/…` |
| Secret-bearing URLs | Magic login links, URLs with `token=`, `key=`, `pwd=` |
| Sensitive notices | Billing failures, security alerts with account data |

If unsure whether a string is a secret: **redact it**.

---

## 2. May retain (usually safe)

| Category | Examples |
|----------|----------|
| Product names | Hosting brand, panel product name |
| Version numbers | WordPress, PHP, plugin versions |
| Plugin / theme names | Active theme, plugin list |
| Folder names | `wp-content`, `css`, `blog` (no account segment) |
| Route names | `/blog/`, `/calculator/` style paths |
| Docroot shape | `/home/[REDACTED]/i-seo.su/public_html` |
| Public URLs | `https://i-seo.su/...` without query secrets |
| Non-secret config **filenames** | `.htaccess`, `nginx.conf` **names only** |

**Database table prefix:** not requested in Phase 2 by default. If ever needed later, treat as sensitive operational metadata and share only under explicit request.

---

## 3. Screenshot workflow

1. Capture only the needed panel/screen region.  
2. Blur/black-out secrets before upload.  
3. Check the browser address bar for tokens.  
4. Check notifications/toasts for emails or keys.  
5. Prefer cropped lists (plugins, folders) over full desktop shots.  
6. Do not include password managers or open credential files in frame.

---

## 4. Text / export workflow

1. Copy only names, versions, paths (sanitized), and public URLs.  
2. Do **not** paste `wp-config.php`.  
3. Do **not** paste `.env`, token files, or DB dumps.  
4. Do **not** send full hosting archives in Phase 2.  
5. Replace account segments with `[REDACTED]`.  
6. If a line contains both useful and secret data, keep the useful part only.

---

## 5. What to do if a secret was sent by mistake

1. Stop further paste.  
2. Tell the operator/agent immediately.  
3. Do **not** commit the secret to Git.  
4. Rotate/revoke the exposed credential in the source system when applicable.  
5. Replace the shared artefact with a redacted version.  
6. Record only that a quarantine event occurred — **not** the secret value.

---

## 6. Phase 2 reminder

Allowed now: operator facts, redacted screenshots, sanitized inventories, operator-listed public URLs.  
Not allowed: live logins by Cursor, crawls, FTP, WP admin access, tokens, REST, database access.

---

*Evidence redaction guide v1 · 2026-07-22.*

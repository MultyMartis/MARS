# ISEO-SU METRIKA VISITOR IP PARAM BASELINE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-METRIKA-VISITOR-IP-PARAM-01  
**Site:** https://i-seo.su/  
**Updated:** 2026-08-24  
**Authority:** current baseline for this analytics-only addon

---

## 1. Status

**ACTIVE / ENABLED** — toggleable Metrika visitor IP parameter addon deployed on production.  
Analytics-only. **Not** an automatic blocking / blacklist / CAPTCHA system.

## 2. Purpose

Send the real server-seen visitor IP to the existing Yandex Metrika counter as custom visit parameter `ipaddress`, so the operator can later investigate spam manually inside Metrika.

## 3. Current Metrika Counter

| Field | Value |
|-------|-------|
| Active counter ID | **54287016** |
| Denis example ID | `39163020` — **not used** |
| Init | Inline near `</body>`: `ym(54287016, "init", { clickmap:true, trackLinks:true, accurateTrackBounce:true, webvisor:true })` |
| Loader | `https://mc.yandex.ru/metrika/tag.js` |
| Duplicate counter | **No** — addon does not re-init Metrika |

## 4. Architecture

| Component | Production path | Role |
|-----------|-----------------|------|
| Feature config | `/metrika-visitor-ip-config.php` | Global enable/disable + counter id |
| Read-only endpoint | `/metrika-visitor-ip.php` | Returns JSON IP while enabled; **204** when disabled |
| Addon JS | `/js/metrika-visitor-ip.js` | One fetch + one `ym(..., 'params', {ipaddress})` |
| Loader hook | `/js/common.js` (tail) | Async loads addon JS once; fail-open |

MARS mirror: `production-source/metrika-ip/` (+ loader in `production-source/js/common.js`).

Flow:

```
browser → GET /metrika-visitor-ip.php (same-origin, no-store)
       → { enabled:true, ipaddress:"…" }
       → ym(54287016, 'params', { ipaddress: "…" })
```

## 5. Real IP Authority

**PRIMARY:** PHP `$_SERVER['REMOTE_ADDR']`  
Validated with `filter_var(..., FILTER_VALIDATE_IP)` (IPv4 + IPv6).  
Invalid → treat as disabled response (204).

Same authority pattern as existing `iseo_form_client_ip()` (forms).

## 6. Proxy Trust Rules

| Header | Used for IP authority? |
|--------|------------------------|
| `X-Forwarded-For` | **NO** |
| `X-Real-IP` | **NO** (observed equal to REMOTE_ADDR on Beget; not trusted as client-controlled authority) |
| `CF-Connecting-IP` | **NO** (absent) |
| `Forwarded` | **NO** |

No proven separate CDN trust boundary requiring header preference. **Untrusted forwarded headers are not used.**

## 7. Parameter

| Field | Value |
|-------|-------|
| Name | `ipaddress` |
| Value | Exact validated server IP (no anonymization) |
| API | `ym(54287016, 'params', { ipaddress: <ip> })` |
| Frequency | Once per page load (guard flag) |

## 8. Feature Switch

In `metrika-visitor-ip-config.php`:

```php
"enabled" => true,   // or false
```

Semantic alias: **METRIKA_VISITOR_IP_ENABLED**.

## 9. Enable Procedure

1. Set `"enabled" => true` in production `/metrika-visitor-ip-config.php`.  
2. Mirror the same value in MARS `production-source/metrika-ip/metrika-visitor-ip-config.php`.  
3. Verify `GET /metrika-visitor-ip.php` returns JSON with `ipaddress`.  
4. No template edits required.

## 10. Disable Procedure

**One config change:**

1. Set `"enabled" => false` in `/metrika-visitor-ip-config.php`.  
2. Done.

Expected: endpoint **204** / no IP; no `ipaddress` params call; **normal Metrika stays ON** (init / clickmap / Webvisor / goals unchanged).

## 11. Failure Behavior

Fail-open for the website: endpoint/network/`ym` failure → silent stop; no retries loop; no blocking render; forms unaffected.

## 12. Cache Safety

IP is **not** embedded in static HTML.  
Endpoint sends `Cache-Control: no-store, no-cache, must-revalidate, private, max-age=0` + `Pragma: no-cache`.  
Per-request identity preserved — no Visitor A → Visitor B IP leak via page cache.

## 13. Public Page Coverage

Loaded wherever `js/common.js` runs with the public Metrika counter (verified representatives: `/`, `/services.html`, `/services/**`, `/cases/**`, `/blog/`, blog post, `/offers`, `/tariff-calc`, `/glossary/`, glossary single).  
Not intended for wp-admin / internal admin surfaces.

## 14. Test Evidence

See `ISEO-SU-METRIKA-VISITOR-IP-PARAM-EVIDENCE-v1.md` and task REPORT.  
Full visitor IPs are **not** stored in Git evidence (masked).

## 15. Production Source Authority

| Role | Path |
|------|------|
| Addon locus | `projects/iseo-su-site-ops/production-source/metrika-ip/` |
| Shared JS loader | `projects/iseo-su-site-ops/production-source/js/common.js` |

Production ↔ source must stay aligned for these files.

## 16. Rollback

1. Set `"enabled" => false` (preferred soft kill), **or**  
2. Restore scoped pre-change backups of `js/common.js` and remove the three addon files from docroot / `js/`.  
Scoped backups live under local task dir (Git-ignored): `X:\AI MARS\local\sites\iseo-su-production\_metrika-visitor-ip-01\backups\`.

## 17. Future Editing Rules

- Do **not** re-init Metrika or change counter options for this feature.  
- Do **not** trust client-supplied forwarded IP headers without a new infrastructure proof charter.  
- Do **not** persist visitor IP history in MARS/Git/DB for this addon.  
- Do **not** couple this addon to form anti-spam / auto-ban.  
- IP blocking remains **manual / out of scope**.

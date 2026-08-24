# ISEO-SU METRIKA VISITOR IP PARAM EVIDENCE v1

**Task:** ISEO-SU-SITE-OPS-METRIKA-VISITOR-IP-PARAM-01  
**Date:** 2026-08-24  
**Rule:** No full visitor IP in committed evidence (masked only).

---

## 1. Production Metrika Discovery

Public HTML on representative URLs contains the standard Yandex tag loader and init block near `</body>`.  
Counter example `39163020` **absent**. Active ID **54287016** present on static and WordPress contours.

## 2. Counter ID

**54287016**

## 3. Existing Initialization

```
ym(54287016, "init", {
  clickmap:true,
  trackLinks:true,
  accurateTrackBounce:true,
  webvisor:true
});
```

Goals already call `ym(54287016, 'reachGoal', …)` from `js/common.js`.  
No pre-existing `params` / `ipaddress` usage found before this task.

`js/common.js` is loaded across marketing HTML and WP templates that enqueue it — used as the single public loader hook for the addon.

## 4. Addon Files

| File | SHA-256 (full) |
|------|----------------|
| `metrika-visitor-ip-config.php` | `5a8f4d2f2bcf2145c5611f4160b05e0cd22ef7c582ecb405a02acf3b0a9e41ba` |
| `metrika-visitor-ip.php` | `5c9129ef2fdc84cef9fd06a32ca6a0f63ca654dc253a11d59a55662be1881936` |
| `js/metrika-visitor-ip.js` | `27825bf462a9de7bd12cb482192b6bca81d20000cf0116458625500c4e941fa6` |
| `js/common.js` (with loader) | `57816837184001f2cc2c0e2a7207975dad8f687138ceef47f3f09286f3095731` |

Deploy stamp: `20260824T064723Z` (local receipt).

## 5. IP Detection

Endpoint uses **REMOTE_ADDR** + `FILTER_VALIDATE_IP` (IPv4/IPv6).  
Diagnostic probe (removed after use) showed `REMOTE_ADDR` and `HTTP_X_REAL_IP` equal; `X-Forwarded-For` / CF headers absent.

Test session server-detected IP (masked): **46.\*\*\*.\*\*\*.198**  
RIPE prefix path consistent with client ISP transit (E-Light-Telecom), not treated as Beget shared anycast visitor IP.

Independent general-internet IPv4 (ipify, masked **178.\*\*\*.\*\*\*.69**) differed due to dual-stack / split egress on the test host; the TCP path to `i-seo.su` used the 46.\* address.  
**Authority for Metrika remains the server-seen REMOTE_ADDR for that request.**

## 6. Proxy Trust Decision

**UNTRUSTED FORWARDED HEADERS USED: NO**  
No CDN trust charter; REMOTE_ADDR primary (matches existing form IP helper).

## 7. Enabled Test

| Check | Result |
|-------|--------|
| Endpoint HTTP | 200 JSON `{enabled:true, ipaddress:…}` |
| Cache-Control | `no-store, no-cache, must-revalidate, private, max-age=0` |
| Addon JS HTTP | 200 |
| common.js contains loader | YES |
| Server IP masked | 46.\*\*\*.\*\*\*.198 |

## 8. Metrika Params Send

Playwright instrumentation on `https://i-seo.su/`:

| Check | Result |
|-------|--------|
| `ym(..., 'params', {ipaddress})` | **PASS** (1 call) |
| Counter | 54287016 |
| Value matched server IP | **YES** |
| Addon script loaded | YES |
| Metrika network activity | present (`mc.yandex` hits) |
| TECHNICAL PARAM SEND | **proven** |
| VISIBLE IN METRIKA UI | **not observed in this task** (processing delay possible) |

## 9. Disabled Test

Set `"enabled" => false` on production config (scoped backup + checksum).

| Check | Result |
|-------|--------|
| Endpoint | **204** empty |
| `ipaddress` params calls | **0** |
| HTML still contains `ym(54287016` init | **YES** |
| `mc.yandex` activity | still present |
| Page / forms render | normal (no form submit in this wave) |

## 10. Re-enabled Final State

Restored `"enabled" => true`.  
Array line confirmed `true`. Endpoint returns JSON IP. Params send restored (1 call).  
**FEATURE FINAL STATE: ON**

## 11. Cache Safety

IP not in HTML on regression sample. Endpoint no-store/private.  
**CACHE CROSS-VISITOR RISK: NO**

## 12. Site Regression

Representative URLs all HTTP 200; Metrika init present; server test IP **not** visible in HTML; no PHP fatal markers in responses.

## 13. Production / Source Alignment

SHA-256 match for config/endpoint/addon JS/common.js between production verify downloads and `production-source/`.  
**ALIGNED**

## 14. Scoped Backups

Local (Git-ignored): `X:\AI MARS\local\sites\iseo-su-production\_metrika-visitor-ip-01\backups\`  
Includes pre-upload `js/common.js` and config toggle backups. Operator full site backup already taken before task (not re-requested).

## 15. Final Decision

**ACCEPT** — addon active, kill switch verified, Metrika param send proven technically, forms/Metrika init untouched beyond minimal common.js loader.

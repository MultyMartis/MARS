# REPORT — ISEO-SU SITE OPS METRIKA VISITOR IP PARAM 01

**Task ID:** ISEO-SU-SITE-OPS-METRIKA-VISITOR-IP-PARAM-01  
**Date:** 2026-08-24  
**Final status:** COMPLETE — ISEO-SU REAL VISITOR IP SENT TO METRIKA / TOGGLEABLE ADDON ACTIVE / SAFE KILL SWITCH VERIFIED

---

## 1. Execution Summary

Discovered production Metrika counter **54287016**, deployed an isolated same-origin IP endpoint + JS addon that sends `ym(54287016, 'params', { ipaddress })`, verified technical transmission and a reversible kill switch, restored **ENABLED**, aligned MARS `production-source`, and documented baselines.

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Staged | empty (task start) |
| Foreign WIP | present — preserved, not staged |
| Unpushed commits | present on dirty main (other programmes) — sync via clean worktree |
| Operator full backup | already done (not re-requested) |

## 3. Existing Metrika Architecture

Hybrid site embeds the standard Yandex tag.js snippet near `</body>` on static marketing pages and WordPress-rendered public pages. Goals already use counter **54287016** inside `js/common.js`. No second counter. No prior `params`/`ipaddress` usage.

## 4. Active Counter

**54287016** (Denis example `39163020` not present / not used).

## 5. Addon Design

| Piece | Path |
|-------|------|
| Config switch | `/metrika-visitor-ip-config.php` |
| Endpoint | `/metrika-visitor-ip.php` |
| Addon JS | `/js/metrika-visitor-ip.js` |
| Loader | minimal async append in `/js/common.js` |

Fail-open; one attempt; no Metrika re-init; no `window.ym` overwrite.

## 6. Real IP Detection

`REMOTE_ADDR` + `filter_var` IPv4/IPv6. Invalid → 204.

## 7. Proxy Trust

Forwarded/Real-IP/CF headers **not** used as authority. Beget shows nginx front; no proven need to prefer client-spoofable headers.

## 8. Feature Switch

`"enabled" => true|false` in config (= METRIKA_VISITOR_IP_ENABLED).  
OFF → 204 + no params send; Metrika init remains.

## 9. Production Deployment

SFTP upload with per-file scoped backup + post-upload SHA-256 verify (`20260824T064723Z`). Temporary diagnostic probe uploaded then **removed**.

## 10. Enabled Test

Endpoint 200 + no-store headers; server IP masked **46.\*\*\*.\*\*\*.198**; dual-egress note vs general ipify path documented in evidence.

## 11. Metrika Parameter Transmission

Browser instrumentation: **1** `params` call, counter 54287016, value matched server IP.  
TECHNICAL PARAM SEND = proven. Metrika UI visibility = not claimed.

## 12. Disabled Kill-Switch Test

OFF config → endpoint **204**, **0** `ipaddress` params, Metrika init HTML + `mc.yandex` still active. **PASS**

## 13. Final Enabled State

Restored ON; array `enabled=true`; endpoint JSON IP; params send restored. **FINAL STATE: ON**

## 14. Cache Safety

No IP in HTML; endpoint private/no-store. **NO** cross-visitor cache risk.

## 15. Site Regression

`/`, services, cases sample, blog, blog post, offers, tariff-calc, glossary, glossary single — HTTP 200, Metrika present, no visible IP leak, no PHP fatal in HTML.

## 16. Files Created or Updated

**Created (MARS):**

- `production-source/metrika-ip/metrika-visitor-ip-config.php`
- `production-source/metrika-ip/metrika-visitor-ip.php`
- `production-source/metrika-ip/js/metrika-visitor-ip.js`
- `ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md`
- `ISEO-SU-METRIKA-VISITOR-IP-PARAM-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-METRIKA-VISITOR-IP-PARAM-01.md`

**Updated (MARS):**

- `production-source/js/common.js` (loader only)
- `ISEO-SU-CURRENT-STATE-v1.md`
- `OPERATIONAL-INDEX.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`

## 17. Production Mutations

| Remote | Action |
|--------|--------|
| `metrika-visitor-ip-config.php` | create + kill-switch toggle cycle → final ON |
| `metrika-visitor-ip.php` | create |
| `js/metrika-visitor-ip.js` | create |
| `js/common.js` | loader append |
| `_mars_ip_probe_tmp.php` | temporary then deleted |

Forms / anti-spam files: **unchanged**.

## 18. Production / Source Alignment

SHA-matched for all four task production files. **YES**

## 19. Rollback

Soft: `"enabled" => false`. Hard: restore `js/common.js` backup + remove three addon files. Backups under local `_metrika-visitor-ip-01/backups/`.

## 20. Git Persistence

Scoped commit on task files only; clean-worktree sync to `origin/mars/canonical-post-recovery` (see closeout). No foreign WIP.

## 21. Open Risks

| Risk | Note |
|------|------|
| Metrika UI delay | Param may appear in reports after processing lag |
| Split egress on test host | Independent “general internet” IP may differ from Beget-path IP; server REMOTE_ADDR remains authority |
| OPcache | Unlikely for include config; kill switch verified live |

**Open blockers: 0**

## 22. Final Decision

**COMPLETE — ISEO-SU REAL VISITOR IP SENT TO METRIKA / TOGGLEABLE ADDON ACTIVE / SAFE KILL SWITCH VERIFIED**

## 23. Stop Condition

Stop after discovery, addon, deploy, IP/param proof, kill-switch OFF+ON, regression, docs/source, Git sync.  
Do **not** start IP blocking, blacklist automation, sitemap/SEO/form/CAPTCHA work.

---

## FINAL HARD CHECK

```
ACTIVE METRIKA COUNTER: 54287016
IP PARAMETER: ipaddress
IP SOURCE: server-side verified client IP (REMOTE_ADDR)
IP VALIDATION: PASS
UNTRUSTED FORWARDED HEADERS USED: NO
FEATURE SWITCH: PRESENT
FEATURE FINAL STATE: ON
SERVER REAL IP TEST: PASS
METRIKA PARAM CALL: PASS
METRIKA PARAM VALUE MATCHED SERVER IP: YES
FULL IP STORED IN GIT: NO
FULL IP STORED IN MARS LOGS: NO
IP VISIBLE IN HTML: NO
EXTERNAL IP API USED: NO
CACHE CROSS-VISITOR RISK: NO
KILL SWITCH TEST: PASS
NORMAL METRIKA WHILE ADDON OFF: PASS
WEBVISOR REGRESSION: PASS (init options unchanged; mc.yandex activity while OFF)
FORM SYSTEM CHANGED: NO
PUBLIC PAGE COVERAGE: PASS
PRODUCTION/SOURCE ALIGNED: YES
OPEN BLOCKERS: 0
REMOTE SYNC: (completed in Git wave)
```

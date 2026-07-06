# REPORT — SITE-002 llms.txt Encoding Fix

**Operation:** `SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01`  
**OCPilot run:** 4.204  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-LLMS-TXT-01`  
**Baseline after:** `SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01`

---

## 1. Scope

Encoding-only fix for `/public_html/llms.txt` — add UTF-8 BOM so browsers and clients without explicit `charset` in `Content-Type` display Cyrillic correctly. No semantic content change. No PHP, DB, admin, header/footer, robots, sitemap, Yandex, or product meta changes. Conditional `.htaccess` path prepared but **not required**.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` — label **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Staged files before task | **none** |
| Foreign WIP | FP-0002 / `.recovery-temp` — **not staged** |

---

## 3. Current public serving diagnosis

| Field | Before fix |
|-------|------------|
| URL | https://bzpm.ru/llms.txt |
| HTTP status | **200** |
| Content-Type | `text/plain` |
| Charset in header | **none** |
| Content-Length | 3503 |
| First bytes (hex) | `23 20 d0 91 d0 97 d0 9f d0 9c …` (`# БЗПМ`) |
| UTF-8 BOM | **no** |
| UTF-8 valid | **yes** |
| Cyrillic chars | 1199 |
| Mojibake (UTF-8 decode) | **no** |
| SHA-256 | `e2e752c6dab1ebf751283cc3013fee711925c77a4c764d2474500383c8b8de58` |

**Root cause:** file bytes were valid UTF-8, but server sends `Content-Type: text/plain` without `charset=UTF-8`. Browsers default to ISO-8859-1/Windows-1252 for `.txt`, producing mojibake for Cyrillic despite correct file encoding.

**Storage:** `deployments/SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01/headers/llms-before-headers.{txt,json}`, `verification/encoding-diagnosis-before.{md,json}`

---

## 4. Remote file encoding analysis

| Field | Result |
|-------|--------|
| FTP path | `/public_html/llms.txt` |
| Size | 3503 bytes |
| SHA-256 | matches Run 4.203 |
| BOM | **no** |
| UTF-8 valid | **yes** |
| Line endings | LF |
| Semantic text | correct Russian Markdown |

**Storage:** `source/llms.txt.remote-current`, `verification/remote-file-encoding-analysis.{md,json}`

---

## 5. Chosen fix

**Primary:** reupload same text as **UTF-8 with BOM** (+3 bytes prefix `EF BB BF`).

**Rationale:** minimal single-file change; helps browsers detect UTF-8 without `.htaccess` mutation; preserves all URLs and Markdown structure.

**BOM added:** yes  
**.htaccess needed:** no (post-deploy verification PASS)

---

## 6. Backup / rollback readiness

| Artefact | SHA-256 |
|----------|---------|
| `backup/llms.txt` | `e2e752c6dab1ebf751283cc3013fee711925c77a4c764d2474500383c8b8de58` |
| `rollback/llms.txt` | same |

Pre-upload live SHA matched backup — deploy gate G8 satisfied.

---

## 7. Dry-run

| Field | Value |
|-------|--------|
| Before SHA | `e2e752c6dab1ebf751283cc3013fee711925c77a4c764d2474500383c8b8de58` |
| Prepared SHA | `126a2508950f4158fc732ab310ada45d59ab781d18861565fe291733089ac313` |
| Semantic match | **yes** |
| Byte diff | BOM (+3) only |
| Target | `/public_html/llms.txt` |

**Storage:** `manifests/dry-run.{md,json}`, `manifests/llms-encoding-plan.{md,json}`

---

## 8. Deploy

| Field | Value |
|-------|--------|
| Remote uploads | **1** |
| Remote overwrites | **1** |
| Remote deletes | **0** |
| Post-upload SHA match | **yes** |
| Deployed at | 2026-07-06T21:44:45+00:00 |

**Storage:** `manifests/deploy-summary.json`, `verification/after-upload/llms.txt`

---

## 9. Public verification

### After BOM fix

| Field | After fix |
|-------|-----------|
| HTTP status | **200** |
| Content-Type | `text/plain` (charset still absent in header) |
| Content-Length | **3506** (+3 BOM) |
| First bytes (hex) | `ef bb bf 23 20 d0 91 d0 97 d0 9f d0 9c …` |
| UTF-8 BOM | **yes** |
| Readable Russian | **yes** |
| Mojibake | **no** |
| SHA-256 | `126a2508950f4158fc732ab310ada45d59ab781d18861565fe291733089ac313` |

**Storage:** `headers/llms-after-bom-headers.{txt,json}`, `verification/encoding-diagnosis-after-bom.{md,json}`, `verification/llms-response-after-bom.txt`

---

## 10. Conditional .htaccess decision

**Not executed.** BOM fix sufficient; `public_serving_ok: true` after Phase 8. `.htaccess` patch plan exists in tool for rollback-safe future use only.

---

## 11. Robots / sitemap preservation

| URL | Status | Notes |
|-----|--------|-------|
| https://bzpm.ru/robots.txt | **200** | Sitemap directive present |
| https://bzpm.ru/sitemap.xml | **200** | **1320 URLs** |

---

## 12. Yandex / duplicate body preservation

| Check | Result |
|-------|--------|
| Home `body_count` | **1** |
| Yandex.Metrika (home) | **present** |
| Yandex.Webmaster (home) | **present** |
| Yandex.Metrika (stoly) | **present** |
| Yandex.Webmaster (stoly) | **present** |
| header.twig / footer.twig | **unchanged** |

---

## 13. Product meta generator preservation

No PHP or product controller changes. Product meta keywords v1.1 (Run 4.202) unchanged.

---

## 14. Remote mutation summary

| Category | Count |
|----------|-------|
| Remote uploads | **1** |
| Remote overwrites | **1** |
| Remote deletes | **0** |
| Remote renames | **0** |
| Admin saves | **0** |
| DB direct operations | **0** |
| PHP changes | **0** |
| `.htaccess` changes | **0** |
| Header/footer changes | **0** |
| Yandex.Metrika/Webmaster changes | **0** |
| Robots changes | **0** |
| Sitemap changes | **0** |
| Product meta generator changes | **0** |
| Non-product meta changes | **0** |
| Cron/import changes | **0** |
| Mail changes | **0** |
| Cache clears | **0** |

---

## 15. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01\`

Checkpoint storage: `baselines/SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01/`

---

## 16. Authority updates

- Baseline [SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01.md](../baselines/SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01.md)
- [production-profile.md](../production-profile.md)
- [site-passport.md](../site-passport.md)
- [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) — Run 4.204
- [OCPILOT-STATE.md](../../OCPILOT-STATE.md)
- Tool [site-002-prod-llms-txt-encoding-fix-01.py](../tools/site-002-prod-llms-txt-encoding-fix-01.py)

---

## 17. Git status

Selective commit of scoped repository paths only. Storage artefacts not committed.

---

## 18. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Whether all third-party crawlers honor BOM | **SAFE UNKNOWN** — HTTP clients decoding as UTF-8 confirmed; legacy ISO-8859-1-only clients not tested |
| Content-Type still lacks explicit charset | Header unchanged; BOM mitigates browser display; `.htaccess AddCharset` available if operator prefers explicit header |

---

## 19. Final verdict

**SITE-002 LLMS TXT ENCODING FIX COMPLETE — UTF-8 VERIFIED**

---

## 20. Next task recommendation

**Final meta inventory** — broad read-only audit of remaining non-product and product meta coverage per prior roadmap (Run 4.203 next-task note).

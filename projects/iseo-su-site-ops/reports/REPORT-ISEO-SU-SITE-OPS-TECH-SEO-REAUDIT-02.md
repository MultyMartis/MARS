# REPORT — ISEO-SU-SITE-OPS TECH SEO REAUDIT 02

**Task ID:** `ISEO-SU-SITE-OPS-FULL-SITE-TECH-SEO-REAUDIT-02`  
**Final status:** `COMPLETE — ISEO-SU FULL SITE + TECH SEO RE-AUDIT 02 / READ-ONLY / REMEDIATION PLAN READY`  
**Crawl contour:** `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-reaudit-02\20260904-163451\`

---

## 1. Verdict

Production `https://i-seo.su/` is **healthy at the availability / crawl / form-security layer**. Previous critical-class issues (broken sitemap children, mass link-to-redirect, static completeness gap) remain **closed**. New city (5) / niche (7) landings are live, indexable, in static sitemap, consent-complete, without low-height overlap regression. USA / UAE / Webinar are live and intentionally **out of sitemap/menu**. Residual work is mostly **known SEO backlog** (canonical / title / meta / SM-NONINDEX) plus **HIGH** relative CSS 404s on blog author pages and one broken `logo.svg`. **No CRITICAL findings.** Menu placement for new pages is deferred to Nikita — **not** treated as implementation defect.

---

## 2. Scope

Read-only full-site + tech SEO re-audit after City W02/W02A, USA/UAE W03, Niche W04, small-height rollout, webinar rebuild + date update. No production/source/DB/sitemap/menu mutations.

---

## 3. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD (start) | `0cd709b96ee9cb36f2893de9d6bc73b5b26f3b86` |
| Origin tip (start) | `adbdbe4258dccb376bf452ba2effcbc6a787a47f` |
| Staged | empty |
| Unpushed at start | YES (local ahead) |
| Dirty tree | large foreign WIP — untouched |
| Mutations | 0 production / 0 source implementation |

---

## 4. Crawl

| Field | Value |
|-------|-------|
| Timestamp | `20260904-163451` |
| Seed | `https://i-seo.su/` |
| TOTAL URLS | **1053** |
| HTML 200 | **705** |
| Method | BFS + sitemap seeds; redirects followed to final URL |

Raw: `pages.json`, `pages-full.json`, `inlinks.json`, `crawl-summary.json`.

---

## 5. URL Health

| Status class | Count |
|--------------|------:|
| HTML 200 | 705 |
| 3XX (via redirect_chain / URL≠final) | **9** |
| Page 4XX | **0** |
| Page 5XX | **0** |

No redirect loops detected in sample.

---

## 6. Broken Links

| Class | Count |
|-------|------:|
| BROKEN internal → 4xx/5xx | **0** |
| LINK-TO-REDIRECT | **0** (prior 129 → **CLOSED**) |

---

## 7. Assets

| Class | Count | Notes |
|-------|------:|-------|
| BROKEN IMAGE | **1** | `/img/logo.svg` 404 |
| BROKEN CSS | **6** | relative `/blog/author/css/...` |
| BROKEN JS | **0** | |
| Huge images | **5** | case slides ~1.5–1.7 MB |

---

## 8. New Pages

All **14 SEO landings + webinar**: HTTP **200**.

| Family | Sitemap | Menu | Inlinks (typ.) | Layout safe | Consent |
|--------|---------|------|----------------|-------------|---------|
| City ×5 | yes | no | ~5 | yes / no 100vh | OK |
| Niche ×7 | yes | no | ~1 (hub) | yes | OK |
| USA / UAE | no | no | 0 | yes | OK |
| Webinar | no | no | 0 | yes | OK |

USA/UAE/Webinar: **INTENTIONAL / OPERATOR POLICY**.

---

## 9. Sitemap

| Item | Result |
|------|--------|
| `sitemap.xml` | 200; children static+WP |
| Static URL count | **139** |
| Local completeness validator | **PASS** (gap 0) |
| Static/WP overlap | 0 |
| Sitemap URL 4xx/5xx | 0 |
| SM-CHILD-404 | **CLOSED** |
| Intentional absences | USA, UAE, Webinar |

---

## 10. Robots

`robots.txt` 200; Sitemap directive present; no accidental block of new landings observed.

---

## 11. Indexability

| Class | Count |
|-------|------:|
| INDEXABLE | **650** |
| NOINDEX | **55** |
| Suspicious SM-NONINDEX | ~54 |

---

## 12. Canonical

| Metric | Current | Prior (approx) | Delta |
|--------|--------:|---------------:|-------|
| Missing (all HTML) | 206 | — | — |
| Missing (indexable) | ~156 | 162 | **IMPROVED** |
| Mismatch | ~120 | ~117 | SAME / slight WORSE |
| To 404 / redirect | 0 | — | OK |

---

## 13. Titles

| Issue | Count |
|-------|------:|
| Missing / empty | 0 |
| Duplicate groups | 10 |
| Long >70 | 25 |

---

## 14. Meta Descriptions

| Issue | Count |
|-------|------:|
| Missing | 23 |
| Duplicate families | present |

---

## 15. H1

| Issue | Count |
|-------|------:|
| Missing (indexable sample) | 5 (report-hub family) |
| Multiple H1 | 0 |

---

## 16. Internal Linking

City hub ↔ cities OK. Niche hub → niches OK. USA/UAE/Webinar 0-inlink = policy. Broader orphan-like set includes authors / slash variants — REVIEW.

---

## 17. Menu / Navigation Decision

| Page family | In menu | Classification |
|-------------|---------|----------------|
| City | NO | OPERATOR/SEO DECISION |
| Niche | NO | OPERATOR/SEO DECISION |
| USA/UAE | NO | OPERATOR/SEO DECISION |
| Webinar | NO | OPERATOR/SEO DECISION |

**MENU/NAVIGATION CHANGED: NO** — Nikita decides later.

---

## 18. Duplicate Content

Shared commercial blocks = EXPECTED TEMPLATE REUSE. SEO-risk: title/description/H1 template dups — REVIEW.

---

## 19. Images

Broken: `logo.svg`. Alt: DECORATIVE vs CONTENT MISSING vs REVIEW. Huge case JPGs listed.

---

## 20. OG / Social

Widespread incomplete OG on static family (often only `og:image`) — pattern, not 650 equal HIGH defects.

---

## 21. Forms / Consent

| Check | Result |
|-------|--------|
| Handlers | **12** |
| Live uncovered lead consent | **0** |
| Crawl FP “uncovered” | 5 = search/tool UIs |
| test_mode | **OFF** |
| Recipient | **nikel007i33@yandex.ru** |
| HMAC / consent guard | active |

---

## 22. Webinar Landing

HTTP 200; date **10 сентября 2026**; time **19:00 МСК**; old date on live **0**; no sitemap/menu; form+consent OK; no overlap.

---

## 23. Schema

JSON-LD sample: **0** invalid JSON. No invented schema requirements.

---

## 24. Responsive

New 14 landings: safe first-screen, no low-height overlap regression. Author CSS 404 may affect WP author mobile.

---

## 25. Performance Red Flags

5 multi-MB case images; broken relative CSS 404 noise. Not full Lighthouse.

---

## 26. Comparison With Previous Audit

| Item | Status |
|------|--------|
| SM-CHILD-404 | **CLOSED** |
| Static 139 completeness | **PASS / CLOSED** |
| LINK-TO-REDIR 129→0 | **CLOSED** |
| Blog relative IMG mass | mostly closed; residual assets |
| CANON-MISSING | **IMPROVED** |
| CANON-MISMATCH | **SAME / slight WORSE** |
| META-MISSING 23 | **SAME** |
| Low-height overlap | **0 regression** |
| New landings | **NEW / HEALTHY** |

---

## 27. Findings by Severity

| Severity | Approx |
|----------|-------:|
| CRITICAL | **0** |
| HIGH | **6** (CSS-BROKEN) |
| MEDIUM | ~186 |
| LOW | ~137 |
| OPERATOR/SEO DECISION | ~15 |
| INFORMATIONAL | ~15 |

CSV: `audits/tech-seo/ISEO-SU-TECH-SEO-REAUDIT-02-FINDINGS.csv` (359 rows / 17 finding_id families).

---

## 28. Recommended Remediation Queue

**A. Safe technical:** relative author CSS; `logo.svg`; optional huge JPG compress.  
**B. SEO decision:** canonical backlog; SM-NONINDEX; title-dup; meta missing/dup.  
**C. Menu decision:** city/niche/USA/UAE/webinar — Nikita.  
**D. Content review:** alt, OG, weak inlinks (non-policy).  
**E. No action:** USA/UAE/Webinar outside sitemap/menu; search UIs without PII consent.

---

## 29. Artifacts

| Artifact | Path |
|----------|------|
| Evidence | `ISEO-SU-TECH-SEO-REAUDIT-02-EVIDENCE-v1.md` |
| SEO RU | `reports/ISEO-SU-TECH-SEO-REAUDIT-02-FOR-SEO-TEAM-RU.md` |
| This report | `reports/REPORT-ISEO-SU-SITE-OPS-TECH-SEO-REAUDIT-02.md` |
| Findings CSV | `audits/tech-seo/ISEO-SU-TECH-SEO-REAUDIT-02-FINDINGS.csv` |
| Raw storage | `X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-reaudit-02\20260904-163451\` |

---

## 30. Production Mutations

**PRODUCTION MUTATIONS: 0**  
**SOURCE MUTATIONS: 0**  
**MENU/NAVIGATION CHANGED: NO**

---

## 31. Final Decision

**COMPLETE — ISEO-SU FULL SITE + TECH SEO RE-AUDIT 02 / READ-ONLY / REMEDIATION PLAN READY**

Proceed next only with an explicit remediation charter. Do not change menu until Nikita decides.

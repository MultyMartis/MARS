# REPORT — SITE-002 HTML Body Duplicate Fix

**OCPilot run:** 4.190  
**Operation ID:** SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Parent checkpoint:** SITE-002-STABLE-PROD-SEO-ROBOTS-01  
**New checkpoint:** SITE-002-STABLE-PROD-HTML-BODY-FIX-01  
**Mode:** controlled single-file Production Twig fix — duplicate `<body>` / preloader / overlay removal

---

## 1. Scope

Fix invalid HTML on Production: operator observed duplicate `<body class="page--home">`, duplicate global preloader, and duplicate `page_overlay` in page source. Single targeted change to live `header.twig` only.

| Allowed | Forbidden (not touched) |
|---------|-------------------------|
| HTTP fetch live HTML (4 URLs) | robots.txt / sitemap |
| Fresh FTP download + backup + upload `header.twig` | Meta / SEO edits |
| Remove duplicate body/preloader/overlay block only | footer.twig overwrite |
| Preserve Yandex.Metrika + Webmaster blocks exactly | Product/PDP / catalog load-more code |
| Post-deploy HTML structure verification | DB / admin / cron / mail |

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-task) | `bbbe70543ad5f8e82b285532688bdd6cd45cb71f` |
| Staged files | **none** |
| Parent checkpoint | `SITE-002-STABLE-PROD-SEO-ROBOTS-01` |

**Foreign WIP:** FP-0002, forge-wordpress, `.recovery-temp/` — not staged, not touched.

---

## 3. Live HTML before

Fetched 4 URLs at 2026-07-05T20:30:00+00:00. **Duplicate confirmed site-wide.**

| URL | HTTP | `<body` | `</body>` | zpm-preloader | page_overlay | Metrika | Webmaster |
|-----|------|---------|-----------|---------------|--------------|---------|-----------|
| https://bzpm.ru/ | 200 | **2** | 1 | 10 | **2** | yes | yes |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie | 200 | **2** | 1 | 10 | **2** | yes | yes |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly | 200 | **2** | 1 | 10 | **2** | yes | yes |
| https://bzpm.ru/guarantee | 200 | **2** | 1 | 10 | **2** | yes | yes |

Storage: `deployments/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01/html-before/` (raw + masked)

---

## 4. Source discovery

Fresh FTP read-only download at 2026-07-05T20:30:00+00:00.

| Remote path | `<body` count | Preloader | Overlay | Yandex | Classification |
|-------------|---------------|-----------|---------|--------|----------------|
| `…/common/header.twig` | **2** (L96, L113) | yes ×2 | yes ×2 | Webmaster (head ~L21) | **CHANGE_TARGET** |
| `…/common/footer.twig` | 0 | no | no | Metrika (~L233–245) | READ_ONLY |

No other theme template outputs `<body>` or global preloader. Duplicate is **within header.twig**, not from include composition.

Storage: `deployments/…/manifests/source-discovery.json`

---

## 5. Root cause

| Question | Answer |
|----------|--------|
| First body/preloader source | `header.twig` L96–109 — canonical block immediately after `</head>` |
| Duplicate source | Same file L113–126 — exact copy of body + preloader + overlay |
| Same file or include? | **Same file** — accidental paste/merge duplicate |
| Yandex in changed file? | Webmaster meta in `<head>` (~L21) — **outside** removed block |
| Minimal fix | Remove L110–126 gap (blank lines + second body/preloader/overlay) |

---

## 6. Files changed

| Remote path | Action |
|-------------|--------|
| `/public_html/catalog/view/theme/default/template/common/header.twig` | Upload prepared copy — 17 lines removed, 0 added |

**Not changed:** `footer.twig`, robots.txt, controllers, JS, CSS, DB, admin.

---

## 7. Backup and rollback readiness

| Artefact | SHA-256 |
|----------|---------|
| source / backup / rollback (pre-fix) | `8e41c9bfc3ab6c31a519f3e0b754ac11cacb0f93ca2e71e0c8b9eddf16a50ecb` |
| prepared / after-upload (post-fix) | `4fac43f8823e9e4c8c60b4d541455eec29a06256f73fbdd73a08f0875d09d8c7` |

Pre-upload gate: live hash matched backup before upload.

Rollback: upload `deployments/…/rollback/header.twig` to remote header path.

---

## 8. Dry-run diff

| Metric | Value |
|--------|-------|
| Files to upload | 1 |
| Lines removed | 17 |
| Lines added | 0 |
| body count before → after | 2 → 1 |
| preloader class refs before → after | 10 → 5 |
| page_overlay before → after | 2 → 1 |
| Yandex block hash | **unchanged** |

Storage: `deployments/…/manifests/dry-run.md`, `dry-run.json`

---

## 9. Deploy

| Metric | Value |
|--------|-------|
| Timestamp | 2026-07-05T20:30:35+00:00 |
| Remote uploads | 1 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Upload hash verified | **yes** |

---

## 10. Post-deploy verification

Fetched 4 URLs at 2026-07-05T20:30:40+00:00.

| URL | HTTP | `<body` | `</body>` | zpm-preloader | page_overlay | Metrika | Webmaster | Load More |
|-----|------|---------|-----------|---------------|--------------|---------|-----------|-----------|
| https://bzpm.ru/ | 200 | **1** | 1 | 5 | **1** | yes | yes | n/a |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie | 200 | **1** | 1 | 5 | **1** | yes | yes | n/a |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly | 200 | **1** | 1 | 5 | **1** | yes | yes | visible |
| https://bzpm.ru/guarantee | 200 | **1** | 1 | 5 | **1** | yes | yes | n/a |

- No Twig fatal errors in rendered HTML
- `robots.txt` HTTP 200 — not modified (hash not re-checked against baseline in this run; content path unchanged)
- Load More marker present on `/stoly` — no regression signal in HTML

Storage: `deployments/…/html-after/`, `verification/html-structure-after.json`

---

## 11. Yandex code preservation

| Code | Location | Status |
|------|----------|--------|
| Yandex.Webmaster | `header.twig` `<head>` ~L21 | **preserved** — hash unchanged |
| Yandex.Metrika | `footer.twig` body-end | **unchanged** — file not uploaded |

Yandex block hash before/after in header.twig: **identical** (`a000ad0669f404ef7c78b5e8f1436d74bcf44f03446edf2d3c3d2b168664d0ee`).

Masked operator WIP record: `deployments/…/verification/yandex-blocks-before.md`

---

## 12. Rollback status

**Not required** — deploy and verification PASS.

Rollback files ready at `deployments/…/rollback/header.twig`.

---

## 13. Remote mutation summary

| Category | Count |
|----------|-------|
| Remote uploads | 1 |
| Remote overwrites | 1 exact file |
| Remote deletes | 0 |
| Remote renames | 0 |
| Yandex.Metrika changes | 0 |
| Yandex.Webmaster changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| Meta changes | 0 |
| Product/PDP changes | 0 |
| DB operations | 0 |
| Admin saves | 0 |
| Cron/import changes | 0 |
| Mail changes | 0 |
| Cache clears | 0 |

---

## 14. Storage artefacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01\`

| Folder | Contents |
|--------|----------|
| `html-before/` / `html-after/` | Live HTML snapshots |
| `source/` / `backup/` / `rollback/` / `prepared/` | header.twig lifecycle |
| `verification/` | Structure JSON/MD, Yandex masked record, pre/after-upload |
| `manifests/` | operation.json, discovery, root-cause, dry-run, deploy-result |

Checkpoint storage: `production/baselines/SITE-002-STABLE-PROD-HTML-BODY-FIX-01/`

---

## 15. Authority updates

| Document | Updated |
|----------|---------|
| `OPERATIONAL-INDEX.md` | Run 4.190 added |
| `OCPILOT-STATE.md` | Run 4.190 + new checkpoint |
| `production-profile.md` | HTML body fix + checkpoint |
| `site-passport.md` | Current checkpoint |
| `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | Duplicate body incident + fix |
| `baselines/SITE-002-STABLE-PROD-HTML-BODY-FIX-01.md` | Issued |

---

## 16. Git status

Selective commit of OCPilot docs + tool only. Storage and live Twig/HTML artefacts excluded from git.

---

## 17. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Operator visual HITL (homepage/category animation) | **not performed** — automated HTML PASS only |
| Load More first-click functional test | HTML marker only — full click test **SAFE UNKNOWN** |
| robots.txt byte-identical to Run 4.188 deploy | **SAFE UNKNOWN** — HTTP 200 confirmed, hash not compared |
| Origin of duplicate paste in header.twig | **SAFE UNKNOWN** — likely manual/merge; pre-fix duplicate present since at least initial Production baseline capture |

---

## 18. Final verdict

**SITE-002 HTML BODY DUPLICATE FIX COMPLETE — LIVE HTML VALIDATED**

---

## 19. Next task recommendation

Proceed with **`SITE-002-PROD-SITEMAP-ENABLE-01`** — valid sitemap generation and robots.txt `Sitemap:` directive (separate scoped operation; do not batch with meta fixes unless chartered).

# REPORT — SITE-002 Legacy Category Cleanup Charter 01

**Operation:** `SITE-002-PROD-LEGACY-CATEGORY-CLEANUP-CHARTER-01`  
**OCPilot run:** **4.301**  
**Date:** 2026-07-27  
**Environment:** LEGACY_CATEGORY_CLEANUP_CHARTER_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-LEGACY-CATEGORY-CLEANUP-CHARTER-01\`

**Final verdict:** `SITE-002 LEGACY CATEGORY CLEANUP CHARTER COMPLETE — APPLY PLAN READY`

**Classifications:**
- Cleanup readiness: `LEGACY_CLEANUP_CHARTER_READY`
- Next action: `READY_FOR_CHILD_LEGACY_REDIRECT_DISABLE_APPLY` + `KEEP_PARENT_153_TEMPORARILY`
- Primary option: **A** (child legacy 154/159/165 redirect + disable)
- Apply executed: **no**

---

## 1. Scope

Read-only charter for future controlled cleanup of empty legacy electromechanical category duplicates after confirmed post-import persistence (Run **4.299**) and monitor baseline refresh to **1854** (Run **4.300**).

Not an apply. No production mutation.

## 2. Operator approval

Operator authorized this charter after Run **4.300**. Allowed: research, risk, plan, rollback model, HITL gates. Forbidden: DB/FTP writes, category/redirect/seo_url/product changes, importer/scheduler/baseline changes, Client Ops changes.

## 3. Client Ops boundary

- **Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway drafts, reporting envelope.
- Monitor artifacts read **only** as SITE-002 state evidence (`2026-07-27_15-24-48`).

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `cd917b59` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `cd917b59` | **yes** |
| Staged | empty |
| Untracked foreign tools | 3 verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority unsafe | **NO** |

Evidence: Storage `preflight/`.

## 5. Reports read / current state

| Source | Key fact |
|--------|----------|
| 4.297 importer patch | GUID→path→collision guard; auto-create off |
| 4.299 persistence | CONFIRMED; critical on 378/379/380/376; legacy empty; sitemap 1854 |
| 4.300 baseline refresh | 1737→1854; `NO_ACTION_REQUIRED`; needs 0 |
| Cleanup | **not applied** |

Evidence: Storage `reports-read/`.

## 6. DB read-only

### Hard emptiness

| Check | Result |
|-------|--------|
| 154 / 159 / 165 direct products | **0** |
| 153 subtree products | **0** |
| Products on 153/154/159/165 | **0** |
| Active map rows → 153/154/159/165 | **0** |
| Map 7/7 GUID→canonical | **OK** |
| Critical products on expected leaves | **yes** (4707/4708→378, 4710→379, 4712→380, 4709→376) |
| Category 153 children | **17** (all empty of products) |

### Category snapshot (selected)

| ID | Name | status | children | direct | subtree | SEO keyword |
|---:|------|-------:|---------:|-------:|--------:|-------------|
| 153 | Электромеханическое оборудование | 1 | 17 | 0 | 0 | `elektromehanicheskoe-oborudovanie` |
| 154 | Мясорубки | 1 | 0 | 0 | 0 | `myasorubki` |
| 159 | Пилы для мяса | 1 | 0 | 0 | 0 | `pily-dlya-myasa` |
| 165 | Хлеборезки | 1 | 0 | 0 | 0 | `hleborezki` |
| 378 | Мясорубки (canonical) | 1 | 0 | 2 | 2 | `myasorubki-tehnologicheskoe` |
| 379 | Пилы для мяса (canonical) | 1 | 0 | 1 | 1 | `pily-dlya-myasa-tehnologicheskoe` |
| 380 | Хлеборезки (canonical) | 1 | 0 | 1 | 1 | `hleborezki-tehnologicheskoe` |

Evidence: Storage `db-readonly/`.

## 7. Legacy candidate analysis

| ID | Public nested URL | HTTP | Products | Sitemap | robots | Ready? |
|---:|-------------------|-----:|----------|---------|--------|--------|
| 154 | `/katalog/elektromehanicheskoe-oborudovanie/myasorubki` | 200 | none | yes | index,follow | **YES** redirect+disable |
| 159 | `/katalog/elektromehanicheskoe-oborudovanie/pily-dlya-myasa` | 200 | none | yes | index,follow | **YES** redirect+disable |
| 165 | `/katalog/elektromehanicheskoe-oborudovanie/hleborezki` | 200 | none | yes | index,follow | **YES** redirect+disable |
| 153 | `/katalog/elektromehanicheskoe-oborudovanie` | 200 | none | yes | index,follow | **NO** — leave temporarily |

Flat aliases `/katalog/myasorubki|pily-dlya-myasa|hleborezki` currently **301** → nested legacy (seo_pro). Future apply must cover **both** flat and nested.

Evidence: Storage `legacy-candidates/`.

## 8. Canonical target analysis

| Legacy → Canonical | Target URL | HTTP | Products | Sitemap | Ready redirect target |
|--------------------|------------|-----:|----------|---------|-----------------------|
| 154 → 378 | `.../myasopererabatyvayuschee/myasorubki-tehnologicheskoe` | 200 | 2 | yes | **yes** |
| 159 → 379 | `.../myasopererabatyvayuschee/pily-dlya-myasa-tehnologicheskoe` | 200 | 1 | yes | **yes** |
| 165 → 380 | `.../elektromehanicheskoe/hleborezki-tehnologicheskoe` | 200 | 1 | yes | **yes** |

Parent **153** options 362 vs 375 evaluated — **no blind redirect**; leave temporarily (17 sibling empty children remain under 153).

Evidence: Storage `canonical-targets/`.

## 9. Sitemap check

| Metric | Value |
|--------|------:|
| Unique URLs | **1854** |
| Duplicates | **0** |
| Legacy 153/154/159/165 present | **yes (4)** |
| Canonical 376/378/379/380 present | **yes (4)** |
| Critical product URLs | **5/5** |

Evidence: Storage `sitemap/`.

## 10. Public HTTP check

- Legacy nested leaves/parent: **200**, empty PLPs, self-canonical, `index, follow`
- Canonical hubs/leaves: **200**; leaves show products
- Critical PDPs 4707/4708/4709/4710/4712: **200**; no «Товар не найден»
- PHP Notice/Warning/Fatal: **0**
- Public `БЗПМ`: **0**
- Literal `\n`: **0**

Evidence: Storage `public-http/`.

## 11. Internal links

- Entrypoint scan (home, `/katalog/`, hubs 153/362/375): **no strong nav links** to legacy leaf URLs.
- Observed “hits” for `hleborezki` on canonical 375 are **substring false positives** (`hleborezki-tehnologicheskoe`).
- Full 1854-URL outbound crawl: **SAFE UNKNOWN** (not performed).
- Search Console / analytics backlinks: **SAFE UNKNOWN**.

Evidence: Storage `internal-links/`.

## 12. SEO risk

- Keeping empty indexed 200 legacy leaves = **duplicate/thin content** vs populated canonical leaves.
- Disable without redirect = avoidable **404** — reject.
- **301 + disable** preferred for 154/159/165.
- noindex-first acceptable only as ultra-cautious interim (Option B) — not primary.
- Parent 153: keep temporarily.

Evidence: Storage `seo-risk/`.

## 13. Future apply plan

**Primary: Option A — child legacy cleanup only (NOT EXECUTED).**

1. Deploy `.htaccess` **301** rules (site convention from Lari Run 4.235) for 6 old URLs → canonical 378/379/380.
2. Verify 301→200 on all old URLs **before** disable.
3. Set `oc_category.status=0` for **154/159/165** only.
4. Leave **153** `status=1`.
5. Do not touch mapping table, products, importer, seo_url keywords, Client Ops.
6. Expect sitemap ≈ **1851**; schedule separate monitor baseline refresh charter.

HITL gates G1–G8 and URL map: Storage `future-apply-plan/`.

## 14. Future rollback plan

1. Restore `status=1` for 154/159/165.
2. Restore `.htaccess` from pre-apply backup (remove new rules).
3. Minimal cache clear if needed.
4. Verify legacy 200 + canonical/PDP health.
5. Monitor follow-up / baseline only via separate charter if needed.

Evidence: Storage `future-rollback-plan/`.

## 15. Monitor state

| Field | Value |
|-------|-------|
| run_id | `2026-07-27_15-24-48` |
| baseline | **1854** |
| current | **1854** |
| added / removed | **0 / 0** |
| needs | **0** |
| classification | `NO_ACTION_REQUIRED` |

Evidence: Storage `monitor-state/`.

## 16. Decision

| Field | Value |
|-------|--------|
| Cleanup readiness | `LEGACY_CLEANUP_CHARTER_READY` |
| Recommended next | `READY_FOR_CHILD_LEGACY_REDIRECT_DISABLE_APPLY` |
| Parent 153 | `KEEP_PARENT_153_TEMPORARILY` |
| Apply in this task | **no** |

## 17. Regression

All production/Client Ops/dirty-main mutation checks: **0**.  
Evidence: Storage `regression/`.

## 18. Production mutation summary

- DB writes: 0
- FTP writes: 0
- import runs: 0
- scheduler changes: 0
- monitor baseline changes: 0
- category/product changes: 0
- importer/source changes: 0
- image changes: 0
- redirect changes: 0
- Client Ops changes: 0
- n8n changes: 0
- Telegram changes: 0
- dirty main changes: 0

## 19. Git/worktree summary

| Item | Value |
|------|--------|
| Authority | `X:\AI MARS STORAGE\git-sync-e01\repo` @ `cd917b59` (pre-commit) |
| Branch | `site-002-git-authority-realign-after-wave-e` tracking origin content |
| Dirty main | inspected read-only; foreign WIP preserved |
| Commit scope | report + listed docs only |

## 20. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-LEGACY-CATEGORY-CLEANUP-CHARTER-01\`

Subfolders: preflight, reports-read, db-readonly, legacy-candidates, canonical-targets, sitemap, public-http, internal-links, seo-risk, monitor-state, future-apply-plan, future-rollback-plan, decision, regression, reports, manifests, logs.

## 21. SAFE UNKNOWN / blockers

- Full-site internal link crawl of all sitemap URLs: not done.
- External backlink / Search Console traffic to legacy URLs: not available.
- Mega-menu JS-only link completeness: partial (server HTML scanned).
- Exact post-disable sitemap count: predicted ~1851; confirm after future apply.
- **No blockers** for Option A charter readiness.

## 22. Final verdict

`SITE-002 LEGACY CATEGORY CLEANUP CHARTER COMPLETE — APPLY PLAN READY`

## 23. Next recommendation

1. Operator HITL: approve separate **Option A apply** charter for 154/159/165 (`.htaccess` 301 + `status=0`).
2. Keep parent **153** until a dedicated full legacy-branch charter.
3. After apply: separate monitor baseline refresh when sitemap drops as expected.
4. Do **not** change importer/mapping/Client Ops as part of cleanup.

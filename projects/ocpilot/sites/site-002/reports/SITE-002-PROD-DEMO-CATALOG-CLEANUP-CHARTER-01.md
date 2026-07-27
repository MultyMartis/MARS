# REPORT — SITE-002 Demo Catalog Cleanup Charter 01

**Operation:** `SITE-002-PROD-DEMO-CATALOG-CLEANUP-CHARTER-01`  
**OCPilot run:** **4.302**  
**Date:** 2026-07-27  
**Environment:** DEMO_CATALOG_CLEANUP_CHARTER_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-DEMO-CATALOG-CLEANUP-CHARTER-01\`

**Final verdict:** `SITE-002 DEMO CATALOG CLEANUP CHARTER ATTENTION — OPERATOR REVIEW REQUIRED`

**Classifications:**
- Inventory: `DEMO_CATALOG_INVENTORY_COMPLETE`
- Cleanup readiness: `READY_FOR_PARTIAL_DEMO_DELETE_APPLY`
- Apply executed: **no**

---

## 1. Scope

Read-only full inventory/charter for future **physical deletion** of old DEMO/manual categories (and any DEMO products) from SITE-002 Production.

Not an apply. No production mutation. No redirects. No `status=0` as final measure in this plan.

## 2. Operator clarification

Operator revised direction after Run **4.301**:

- Previous Option A (**301 + disable** for 154/159/165) is **superseded** — not the target plan.
- Do **not** 301 garbage demo sections as the cleanup end-state.
- Do **not** leave empty demo pages.
- Do **not** treat `status=0` alone as final cleanup.
- Prepare full controlled cleanup inventory of DEMO categories/products.
- Apply = separate HITL task after this charter.

Evidence: Storage `reports-read/operator-correction.md`.

## 3. Client Ops boundary

- **Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway, reporting envelope.
- Monitor artifacts read **only** as SITE-002 state evidence (`2026-07-27_15-24-48`).

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `e7bb0e85` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `e7bb0e85` | **yes** |
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
| 4.301 legacy cleanup charter | Option A redirect plan — **superseded by operator** |
| This run 4.302 | Full demo cleanup inventory; **no apply** |

Evidence: Storage `reports-read/`.

## 6. Full category inventory

| Metric | Value |
|--------|------:|
| Total categories | **244** |
| Legacy 153 branch (root + children) | **18** |
| Canonical tech 362 branch | inventoried |
| DELETE_READY (Group A) | **17** |
| KEEP_PARENT_PENDING | **1** (153) |
| KEEP_CANONICAL_1C | mapped IDs present |
| AMBIGUOUS_OPERATOR_REVIEW | **119** (empty/unclear outside strict 153 leaves) |

### Group A — DELETE_READY (all children of 153)

`154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170`

All: status=1, direct=0, subtree=0, no `oc_mars_1c_category_map` row, empty public PLPs.

Superseded by canonical 1C (known):

| Legacy | Name | Canonical |
|-------:|------|----------:|
| 154 | Мясорубки | 378 |
| 159 | Пилы для мяса | 379 |
| 165 | Хлеборезки | 380 |

### Parent 153

`KEEP_PARENT_PENDING` — empty subtree, still a root hub in sitemap/menu history; delete **after** children, only with explicit operator approval (tile/menu role).

Evidence: Storage `category-inventory/`.

## 7. Full product inventory

| Metric | Value |
|--------|------:|
| Total products | **1598** |
| With `xml_id` | **1598** |
| Without `xml_id` | **0** |
| DELETE_READY products | **0** |
| Still assigned to legacy 153 branch | **0** |
| Critical 4707/4708/4709/4710/4712 on expected leaves | **yes** |

**Finding:** No demo/manual products qualify for delete under strict rules. All products have 1C `xml_id`. Group B is empty.

Evidence: Storage `product-inventory/`, `db-readonly/critical-products.csv`.

## 8. Demo candidate rules

Categories/products use:

- `DELETE_READY` / `KEEP_CANONICAL_1C` / `KEEP_PARENT_PENDING` / `AMBIGUOUS_OPERATOR_REVIEW` / `DO_NOT_TOUCH`

Hard gate: any 1C/canonical evidence → not DELETE_READY.

Evidence: Storage `demo-candidates/classification-rules.md`.

## 9. Demo candidates

| Set | Count | Notes |
|-----|------:|-------|
| Category DELETE_READY | 17 | Entire empty 153 child set |
| Product DELETE_READY | 0 | — |
| Parent pending | 1 | 153 |
| Ambiguous categories | 119 | Empty leaves outside 153 — need operator triage |
| Ambiguous products | 0 | — |

Evidence: Storage `demo-candidates/`.

## 10. Canonical crosscheck

| Check | Result |
|-------|--------|
| Map rows on Group A IDs | **0** |
| Critical products OK | **yes** (4707/4708→378, 4710→379, 4712→380, 4709→376) |
| Group A crosscheck FAIL | **0** |
| Canonical tech IDs | DO_NOT_TOUCH / KEEP_CANONICAL_1C |

Evidence: Storage `canonical-crosscheck/`.

## 11. Sitemap check

| Metric | Value |
|--------|------:|
| Unique URLs | **1854** |
| Legacy branch URLs (`/katalog/elektromehanicheskoe-oborudovanie*`) | **18** |
| Group A child PLPs | **17** |
| Expected after Group A | **1837** |
| Expected after Group A + parent 153 | **1836** |

Legacy demo URLs are **currently in sitemap** as indexed empty PLPs.

Evidence: Storage `sitemap/` (prefix-matched; substring false positives discarded).

## 12. Public HTTP check

- Home, `/katalog/`, sitemap: **200**
- All 17 Group A nested PLPs + parent 153: **200**, empty
- Canonical hubs/leaves (362/375/376/378/379/380): **200**
- Critical PDPs sampled: **200**
- PHP Notice/Warning/Fatal: **0** on checked set
- Public `БЗПМ`: **0**
- Literal `\n`: **0**

Evidence: Storage `public-http/`.

## 13. Monitor state

| Field | Value |
|-------|-------|
| run_id | `2026-07-27_15-24-48` |
| baseline | **1854** |
| current | **1854** |
| added / removed | **0 / 0** |
| needs | **0** |
| classification | `NO_ACTION_REQUIRED` |

Evidence: Storage `monitor-state/`.

## 14. Future delete plan

**NOT EXECUTED.**

### Group A — Safe delete-ready categories

Physical remove IDs **154–170** (17 children of 153).

Tables (dry-run SELECT counts in Storage): `oc_category`, `oc_category_description`, `oc_category_to_store`, `oc_category_path`, `oc_category_to_layout`, `oc_seo_url`, `oc_product_to_category` (expect 0), optional filter/coupon.

Order: backup → product_to_category → seo_url → path → store/layout/description → category rows (children only).

**No 301** for these demo URLs (operator intent). Expect **404** after delete unless a later SEO charter decides otherwise.

Sitemap Δ ≈ **−17** → **1837**; then schedule baseline refresh.

### Group B — Products

**Empty** — no DELETE_READY products.

### Group C — Keep

Mapped 1C categories; all `xml_id` products; critical SKUs; live entrypoints with products.

### Group D — Operator review

- Parent **153**
- **119** ambiguous empty categories outside 153 subtree

HITL gates G1–G10: Storage `delete-plan/future-hitl-gates.csv`.

Evidence: Storage `delete-plan/`.

## 15. Future rollback plan

Physical delete requires **scoped SQL backup** of every row to be removed; restore in reverse dependency order; HTTP recheck; monitor follow-up.

`status=0` toggle is **not** the rollback model for this charter’s target end-state.

Evidence: Storage `rollback-plan/`.

## 16. Decision

| Field | Value |
|-------|--------|
| Inventory | `DEMO_CATALOG_INVENTORY_COMPLETE` |
| Cleanup readiness | `READY_FOR_PARTIAL_DEMO_DELETE_APPLY` |
| Verdict | `SITE-002 DEMO CATALOG CLEANUP CHARTER ATTENTION — OPERATOR REVIEW REQUIRED` |

Why ATTENTION: Group A is ready, but parent **153** and **119** ambiguous empties need operator decisions before a “full demo tree” claim.

## 17. Regression

All mutation checks **0**. Client Ops / n8n / Telegram / dirty main untouched.

Evidence: Storage `regression/`.

## 18. Production mutation summary

- DB writes: **0**
- FTP writes: **0**
- delete operations: **0**
- import runs: **0**
- scheduler changes: **0**
- monitor baseline changes: **0**
- category/product changes: **0**
- redirect changes: **0**
- importer/source changes: **0**
- image changes: **0**
- Client Ops changes: **0**
- n8n changes: **0**
- Telegram changes: **0**
- dirty main changes: **0**

## 19. Git/worktree summary

| Item | Value |
|------|--------|
| Authority | `X:\AI MARS STORAGE\git-sync-e01\repo` @ `e7bb0e85` |
| Dirty main | read-only inspect; **0** mutations |
| Commit scope | report + listed docs only (this closeout) |

## 20. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-DEMO-CATALOG-CLEANUP-CHARTER-01\`

Includes: `preflight/`, `reports-read/`, `db-readonly/`, `category-inventory/`, `product-inventory/`, `demo-candidates/`, `canonical-crosscheck/`, `sitemap/`, `public-http/`, `monitor-state/`, `delete-plan/`, `rollback-plan/`, `decision/`, `regression/`, `manifests/operation.json`, `logs/`.

## 21. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Full outbound internal-link crawl of all 1854 URLs | **SAFE UNKNOWN** (not performed) |
| Search Console / analytics demand for legacy URLs | **SAFE UNKNOWN** |
| Business meaning of 119 ambiguous empty categories | **needs operator** |
| Whether parent 153 appears in live megamenu tiles as required entry | **needs operator confirm** (profile still documents legacy elektro history) |
| Exact image filesystem cleanup for deleted category images | **out of scope** this charter |

No inventory blockers.

## 22. Final verdict

`SITE-002 DEMO CATALOG CLEANUP CHARTER ATTENTION — OPERATOR REVIEW REQUIRED`

## 23. Next recommendation

1. HITL approve **Group A** physical delete of category IDs **154–170** (SQL backup mandatory).
2. Decide parent **153** (delete in wave 2 vs keep temporarily).
3. Triage **119** ambiguous empty categories (batch review CSV).
4. After apply: separate **monitor baseline refresh** charter (1854 → ~1837 or ~1836).
5. Do **not** execute Run 4.301 Option A redirects.

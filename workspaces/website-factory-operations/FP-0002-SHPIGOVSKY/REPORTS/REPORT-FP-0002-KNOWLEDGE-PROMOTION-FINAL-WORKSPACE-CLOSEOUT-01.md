# REPORT — FP-0002 KNOWLEDGE PROMOTION + FINAL WORKSPACE CLOSEOUT 01

**Factory Project:** FP-0002 — Шпиговский  
**Phase:** PRODUCTION / MAINTENANCE — STABLE  
**Wave:** documentation / Forge knowledge / Git-tail closeout only  
**Date:** 2026-09-09  
**Production mutation:** **NONE**

---

## 1. Verdict (docs wave)

**PASS** for documentation and knowledge promotion at write time.

Git SHA of **this** report’s first closeout commit cannot be known inside that commit (`CLOSEOUT_PENDING` below). Follow-up SHA recording uses the same pattern as Blog Hub §18.1.

Cleanup of completed FP-0002 worktrees/branches is recorded after those operations in the agent chat REPORT (same title). If this file is read from origin after both commits, fetch current origin for the tip.

---

## 2. Current canonical origin (at docs write)

| Role | SHA |
|------|-----|
| Start / last known origin tip before this wave | `33d13bed6e4686809ac23ddd463ca4eae62f68df` |
| Blog Hub implementation | `074777b544e810d7ab9894987fd1983d1c6afab1` |
| This closeout docs/knowledge commit | `CLOSEOUT_PENDING` |
| Final origin tip | fetch `origin/mars/canonical-post-recovery` |

Do **not** treat these SHAs as permanent recovery authority.

### 2.1 Follow-up — SHA recording (2026-09-09)

A commit cannot contain its own SHA. The original `CLOSEOUT_PENDING` cells above are the **wave-time placeholder**, not unfinished work.

SHA-recording follow-up (docs/knowledge commit already on canonical origin):

- `55ee8ba8fc4bf6ca469f9f09038502af48839e3e` — `docs(fp0002): promote production-maintenance knowledge and closeout current ops.`

Fetch `origin/mars/canonical-post-recovery` for the tip after this SHA-recording commit. Do not rewrite Git history to backfill the table.

---

## 3. Current FP-0002 production baseline (compact)

- Live: `https://shpigovsky.ru/`
- Phase: **PRODUCTION / MAINTENANCE — STABLE**
- Core: **`0.3.32-blog-hub-announcement-01`**
- Indexing: **OPEN — HUMAN-APPROVED**; P18G guard + watchdog **ACTIVE**
- Robots: **Olya-owned**; hashes in reports are evidence only
- Specialists hub: `https://shpigovsky.ru/specialisty/` (Page `#1030`, dedicated Hub template, automatic CPT listing, existing cards, reusable blocks, Admin enable/disable, breadcrumbs **intentionally absent**, `has_archive=false`)
- Singles: `/specialisty/{slug}/`
- `/specyalisty/`: **DEPRECATED / REDIRECT-ONLY**
- SEO title / Meta Description: editor-owned **source truth**; one SEO owner
- Open Graph: `open-graph.meta` — separate owner; SEO reuse; articles `og:type=article`; else `website`
- Schema.org: `structured-data.schema-org` — one JSON-LD owner; Yandex-oriented; no fake Product/Offer/ratings/Physician; authenticated Yandex validator **not evidenced**
- Contacts maps: full Yandex Constructor Admin input; per-row scroll toggle default/legacy **false**; no global unsafe scripts
- Blog Hub: `article_hub_announcement` → `get_the_excerpt()`; `article_lead` remains hero; SEO/OG/Schema remain separate
- Editorial DB: **Olya / Admin = production truth**

---

## 4. Documentation updates (this wave)

Scoped to CURRENT operational + Forge knowledge docs. Historical P-reports / V9 architecture **not rewritten**.

See git commit for exact paths. Intended set:

- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/README.md`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/BASELINE-FP-0002-PRODUCTION-MAINTENANCE-STABLE.md`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-NEXT-WEBGPT-HANDOFF.md`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/REPORT-FP-0002-BLOG-HUB-DEDICATED-ANNOUNCEMENT-FIELD-01.md` (§18.1 only)
- this file
- Forge WordPress `OPERATIONAL-INDEX.md`, `knowledge/README.md`, assimilation index, harvest map
- Forge standards: anti-pattern AP-030–034, SEO §5–6, plugin governance, coding §4.1, Admin UX §10.8, ACF field modeling

---

## 5. Agent / handoff

`REPORTS/FP-0002-NEXT-WEBGPT-HANDOFF.md` is the compact next-agent brief: fetch origin first, clean worktree, Olya truth, robots/indexing ownership, specialists URLs, SEO/OG/Schema split, maps, Blog Hub announcement, open items pointer, next-wave startup pattern.

---

## 6. WP Forge knowledge promotion

| Lesson | Status | Canonical path | FP-0002 evidence |
|--------|--------|----------------|------------------|
| Dedicated editorial owners (hero ≠ hub card ≠ SEO ≠ OG ≠ Schema) | **newly promoted** | ACF-FIELD-MODELING · AP-030 | Blog Hub `article_hub_announcement` (field name is project example, not universal law) |
| SEO fields feed OG/Schema; each output is a separate owner | **newly promoted** | SEO-AND-SITEMAP §5 · PLUGIN GOVERNANCE §5.2 · AP-031 | SEO + OG + Schema waves |
| Yandex Schema.org discipline (truthful types, JSON-LD, no fabrication) | **newly promoted** | SEO-AND-SITEMAP §6 · AP-032 | Yandex Schema wave |
| Trusted Admin embeds: narrow handling, no global scripts | **newly promoted** | CODING-AND-SECURITY §4.1 · AP-033 | Contacts Yandex Constructor + scroll toggle |
| Bounded Admin compatibility shim vs plugin surgery | **newly promoted** | ADMIN-UX §10.8 · AP-034 | Specialists Hub Admin UX (ACFE/ACF) |
| Page hub + CPT singles, `has_archive=false` | **already existed** | CONTENT-MODEL-CPT · harvest map §2 | Specialists Hub / P11 |
| Admin/editorial DB is production truth | **already existed** | SOURCE-RUNTIME-AUTHORITY | P18D-FU01 / maintenance SOP |

---

## 7. Open-items reconciliation

| Item | Old | Final | Evidence |
|------|-----|-------|----------|
| GSC sitemap submit | OPEN / AUTH | **OPERATOR / EXTERNAL — OPEN** | no GSC proof |
| Yandex Webmaster sitemap | OPEN / AUTH | **OPERATOR / EXTERNAL — OPEN** | no Webmaster proof |
| Legal Cookie sign-off | OPEN | **OPERATOR / EXTERNAL — OPEN** | P18H |
| `lead_retention_days=730` | OPEN | **OPERATOR / EXTERNAL — OPEN** | P18H; config still 0 unless Admin later |
| Standing editorial ops | — | **OPTIONAL** | normal ops |
| Anti-spam tune from real spam | — | **OPTIONAL** | no new charter |
| Legal Disallow vs noindex | OPEN | **OPERATOR / EXTERNAL — OPEN** | Olya robots |
| Yandex Schema validator | ATTENTION | **OPTIONAL / EXTERNAL** | Schema wave |
| Facebook OG debugger | ATTENTION | **OPTIONAL / EXTERNAL** | OG wave |
| Specialists / SEO / maps / Schema / OG / Blog Hub tech | various | **CLOSED** | accepted wave reports |

---

## 8. Documentation tails closed

- Blog Hub §18 `CLOSEOUT_PENDING`: **kept as wave-time placeholder**; §18.1 records `33d13bed`
- Current specialists URL `/specialisty/` in CURRENT ops docs
- Knowledge hub `specyalisty` row: historical spelling, not current contract
- Harvest map: current-URL note; historical rows not rewritten
- This report’s own SHA: **kept as wave-time placeholder**; §2.1 records `55ee8ba8`

Historical V9 / P-reports left as historical.

---

## 9–16. Git tails / worktrees / branches

Executed **after** docs push. Authoritative inventory and cleanup results live in the agent chat REPORT of the same title. Required end state:

- completed FP-0002 temp worktrees = 0 (except this closeout tree until removed)
- completed local wave branches = 0 (except justified non-ancestor persistence branches)
- remote temp wave branches = 0
- local-only completed commits = 0
- unpushed FP-0002 commits = 0 after push
- staged FP-0002 files = 0 after closeout
- shared main foreign WIP **preserved**

---

## 17. Production smoke

Read-only smoke after cleanup is recorded in the agent chat REPORT. No production writes.

---

## 18. Protected truths

- Olya editorial = production truth
- Robots = Olya policy; SHA in reports is evidence
- Indexing = human-owned OPEN
- Specialists canonical `/specialisty/`
- SEO / OG / Schema = three technical owners; SEO may feed the other two
- Blog Hub announcement = `article_hub_announcement`

---

## 19. Residuals

Operator/external open items 1–4, 7–9. Authenticated Yandex Schema validator and Facebook OG debugger not evidenced. Persistence branches `fp0002/v9-06e29c-*` / `fp0002/v9-06e36-*` are **not** completed-wave tails (not ancestors of current origin) — do not force-delete.

---

## 20. Next-task posture

```text
CURRENT ORIGIN
→ FRESH PRODUCTION TRUTH
→ CURRENT OLYA TRUTH
→ NEW CLEAN WORKTREE
```

---

## 21. Mutation statement

- **Documentation / Forge knowledge:** mutated in this wave (clean closeout worktree)
- **Git/worktree cleanup:** authorized for completed FP-0002 temps after proof
- **Production WordPress / Olya / robots / indexing / maps / schema / OG / content:** **NOT mutated**
- **Shared main foreign WIP:** **preserved**

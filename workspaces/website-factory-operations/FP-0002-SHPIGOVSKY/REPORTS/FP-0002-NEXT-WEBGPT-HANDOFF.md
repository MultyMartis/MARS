# FP-0002 — NEXT WEB-GPT HANDOFF

Compact current-ops brief for the next Web-GPT / Cursor agent. Historical wave detail stays in `REPORTS/`. Do **not** dump chronology here.

## Project
- name: **FP-0002 / Шпиговский**
- production: `https://shpigovsky.ru/`
- phase: **PRODUCTION / MAINTENANCE — STABLE**
- latest production core: **`0.3.32-blog-hub-announcement-01`**
- this file: knowledge + workspace closeout (docs/Git only; **no production mutation**)

## Fetch-current-origin rule

1. `git fetch origin mars/canonical-post-recovery`
2. Record **current** `origin/mars/canonical-post-recovery` full SHA
3. Do **not** treat any SHA in this file as a permanent recovery authority
4. Shared main `X:\AI MARS` may hold **FOREIGN WIP** — never clean/reset/stash/checkout-over it

## Exact next-wave startup pattern

```text
CURRENT ORIGIN
→ FRESH PRODUCTION TRUTH (read-only intake)
→ CURRENT OLYA / ADMIN TRUTH
→ NEW CLEAN WORKTREE from origin/mars/canonical-post-recovery
→ bounded charter
```

Do not reuse completed FP-0002 wave worktrees. Do not implement from a dirty shared main.

## Current source / editorial / runtime truth model

| Layer | Owner |
|-------|--------|
| Git source | `origin/mars/canonical-post-recovery` after fetch |
| Editorial / Admin DB | **Olya and other legitimate Admin changes = production truth** — not “drift” by default |
| Runtime files on host | last accepted deploy of current core |
| Robots.txt | **Olya SEO policy**; hashes in reports are evidence only; live file always wins |
| Indexing (`blog_public`) | **human-owned**; OPEN as of last accepted state; never a technical safety switch |

## Current production baseline (compact)

- specialists hub canonical: `https://shpigovsky.ru/specialisty/` (Page `#1030`, template `specialists-hub.php`, automatic CPT listing, existing card styles, reusable blocks, Admin enable/disable, breadcrumbs **intentionally absent**, `has_archive=false`)
- specialist singles: `/specialisty/{slug}/`
- `/specyalisty/`: **DEPRECATED / REDIRECT-ONLY / HISTORICAL**
- SEO title + Meta Description: **editor-owned source truth**; one SEO owner; output across supported public entity/template types
- Open Graph: one owner `open-graph.meta`; reuses SEO title/description + canonical URL; page-aware image; `og:type=article` on articles else safe `website`; **separate from SEO meta and Schema.org**
- Schema.org: one owner `structured-data.schema-org`; Yandex-oriented JSON-LD `@graph`; truthful types (`MedicalClinic`, branches, WebPage/ContactPage/CollectionPage/Service/Person/Article, ItemList, BreadcrumbList where appropriate); **no** fake Product/Offer/ratings/Physician; no manual JSON-LD UI; authenticated Yandex validator **not yet evidenced**
- Contacts maps: **full Yandex Constructor code** remains Admin input; map render restored; per-row scroll toggle; default/legacy = **false**; frontend normalization; **no global unsafe script allowance**
- Blog Hub: dedicated `article_hub_announcement` (`Анонс статьи для хаба`) → `get_the_excerpt()` fallback; `article_lead` remains article **hero** owner; SEO/OG/Schema descriptions remain separate; native Excerpt is legacy fallback only
- forms / SMTP / native anti-spam / privacy / consent-gated Metrika: **ACTIVE** as previously accepted
- P18G indexing guard + watchdog: **ACTIVE**

## Known protected systems

Do not mutate unless a new charter names them: WordPress content, Olya editorial state, robots, indexing, forms, SMTP, maps, schema, Open Graph, specialist/blog/SEO fields, redirects, production files. Olya remains active in Admin.

## Current open items

See `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`. Remaining items are **OPERATOR / EXTERNAL / OPTIONAL** (GSC/Yandex sitemap UI, legal sign-off, retention, anti-spam tuning from real spam, legal Disallow vs noindex, optional authenticated Yandex Schema validator, optional Facebook OG debugger). Completed technical waves are **CLOSED**.

## Canonical paths

- project: `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`
- status: `PROJECT-STATUS.md`
- open items: `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
- robots runbook: `DOCS/OPERATIONS-INDEXING-ROBOTS-OWNERSHIP-v1.md`
- 2026-08-24 snapshot baseline (not current core): `REPORTS/BASELINE-FP-0002-PRODUCTION-MAINTENANCE-STABLE.md`
- this closeout: `REPORTS/REPORT-FP-0002-KNOWLEDGE-PROMOTION-FINAL-WORKSPACE-CLOSEOUT-01.md`

## Current Git recovery point (historical-at-write; fetch first)

- branch: `origin/mars/canonical-post-recovery`
- blog hub implementation: `074777b544e810d7ab9894987fd1983d1c6afab1`
- blog hub SHA-recording follow-up (closes `CLOSEOUT_PENDING` in that report): `33d13bed6e4686809ac23ddd463ca4eae62f68df`
- knowledge/workspace closeout: **this wave’s commit after push** — fetch origin for the tip

## Important safeguards

- never overwrite Olya editorial DB
- never replace Olya robots with generic templates
- never auto-close indexing
- no `git add .` / `git add -A` / `git commit -a` / `git clean` / `git reset --hard` on shared main
- no external CAPTCHA currently
- structured data and OG must stay separate technical owners; SEO fields may feed both
- trusted Admin embeds: narrow handling only — never global script allowlists

## Where to read first

1. this handoff
2. `PROJECT-STATUS.md`
3. `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
4. wave report **only** if the new task touches that subsystem

Historical P07–P18 and V9 reports remain in `REPORTS/` / `WORDPRESS/`. Do not replay them for normal maintenance.

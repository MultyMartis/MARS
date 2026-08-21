# Forge WordPress — Robots ownership lessons (ROBOTS-001…006)

**Date:** 2026-08-21  
**Source:** FP-0002 PROD-MAINT Olya robots restoration  
**Status:** Documentation / reusable lessons — not a runtime product

---

## ROBOTS-001 — Separate SEO robots from global indexability

SEO robots policy (crawl rules, Clean-param, sitemap, bot-specific groups) and human OPEN/CLOSED indexability are **different concerns**. Do not conflate them in dashboards, guards, or deploy baselines.

## ROBOTS-002 — Do not replace editor SEO robots with a generic deploy baseline

A human/editor SEO `robots.txt` must not be silently replaced by a short generic “OPEN” template during indexability open/close or packaging.

## ROBOTS-003 — Reopen must restore SEO policy intact

When global indexing is reopened, restore the previous canonical SEO robots policy. Temporary close may overlay `Disallow: /`, but must not destroy the SEO source of truth.

## ROBOTS-004 — Read-only validation never writes robots

WPilot probes, crawler checks, watchdogs, and MARS validation must not rewrite `robots.txt` as a side effect.

## ROBOTS-005 — Disallow ≠ Clean-param

Disallowing parameterized URLs is not automatically equivalent to duplicate management. For Yandex, evaluate Clean-param / Webmaster GET-parameter tools; Disallow takes priority and can defeat Clean-param.

## ROBOTS-006 — Prove `/wp-` Allows against live assets

Before broad `Disallow: /wp-` rules, verify theme/plugin CSS, JS, fonts, webp/uploads remain crawlable via more-specific Allow rules against the live resource inventory.

---

## Prevention map

| Lesson | Code / docs hook |
|--------|------------------|
| 001–003 | `IndexingControl` SEO policy asset + CLOSE backup |
| 004 | Watchdog alert-only; WPilot `write_enabled=false` |
| 005–006 | FP-0002 Olya robots review evidence pack |

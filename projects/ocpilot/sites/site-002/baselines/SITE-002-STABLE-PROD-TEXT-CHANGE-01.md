# SITE-002 — STABLE PRODUCTION — Text Change 01

**Status:** **ACTIVE** — first controlled Production change verified  
**Environment:** PRODUCTION (`site-002-prod`)  
**URL:** https://bzpm.ru/  
**Date:** 2026-07-04  
**OCPilot run:** 4.173  
**Operation ID:** SITE-002-PROD-TEXT-CHANGE-01  
**Parent baseline:** SITE-002-STABLE-PROD-INITIAL-01

---

## Scope

First controlled Production mutation for SITE-002. The operation changed exactly one text fragment in one Twig template on the warranty page.

| Field | Value |
|-------|-------|
| Page | https://bzpm.ru/guarantee |
| Remote target | `/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| Changed files | 1 |
| Change type | single text replacement |
| Old text | `понятный порядок действий` |
| New text | `чёткий порядок действий` |
| Uploads | 1 |
| Deletes / renames | 0 / 0 |
| Database operations | 0 |
| Admin saves | 0 |

---

## Verification

| Gate | Result |
|------|--------|
| Fresh Production file downloaded | PASS |
| Backup created | PASS |
| Precondition `match_count == 1` | PASS |
| Dry-run exact scope | PASS |
| Rollback file prepared | PASS |
| Final pre-upload hash unchanged | PASS |
| Remote hash after upload | PASS |
| HTTP `/guarantee` | PASS — 200 |
| New text visible | PASS |
| Old target phrase absent | PASS |
| Desktop screenshot 1440×1200 | PASS |
| Mobile screenshot 390×844 | PASS |

---

## Hashes

| Item | SHA-256 |
|------|---------|
| Source / rollback | `f10dedc1ce196eebcf7024c916a581e4599b624fe2aee5c1a115afc817089556` |
| Prepared / remote after upload | `0bf5aee97f1c1b52b9715b4f6cdeaa5116aff9f7e2377fe27a80b9b2bf166fe6` |

---

## Storage binding

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-TEXT-CHANGE-01\
```

Operation evidence:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-TEXT-CHANGE-01\
```

---

## Rollback authority

Rollback readiness was verified before deploy by preparing `rollback/guarantee.twig` from the fresh Production source and matching its SHA-256 to the source hash.

Rollback procedure remains scoped to this one file:

1. Upload `rollback/guarantee.twig` to `/public_html/catalog/view/theme/default/template/information/guarantee.twig`.
2. Download the remote file again.
3. Verify remote SHA-256 equals `f10dedc1ce196eebcf7024c916a581e4599b624fe2aee5c1a115afc817089556`.
4. Verify HTTP 200 on `/guarantee`.
5. Confirm `понятный порядок действий` is present again.

---

## Boundaries

This checkpoint proves only:

```text
single-file text-only FTP deploy with backup and rollback readiness
```

It does **not** prove generic deploy tooling for CSS, JS, controllers, database changes, OpenCart admin changes, cache clearing, or bulk operations.

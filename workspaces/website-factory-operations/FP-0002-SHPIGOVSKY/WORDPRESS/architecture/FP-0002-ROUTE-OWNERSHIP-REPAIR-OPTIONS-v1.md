# FP-0002 Route Ownership Repair Options v1

**Date:** 2026-07-04  
**Phase:** ROUTE-OWNERSHIP-INVESTIGATION  
**Status:** OPTIONS ONLY — none applied

---

## Option 1 — Source resolver repair

| Field | Value |
|---|---|
| Layer | request resolver |
| Exact intended change | Add bounded `request` / `parse_request` / `pre_get_posts` handler so `/uslugi/{parent}/{child}/` resolves to Service CPT when hierarchy matches |
| Objects affected | None directly; resolution path only |
| Runtime writes later | None for objects; optional rewrite flush if rules also change |
| Source changes later | Yes — `shpigovsky-core` |
| DB checkpoint | Recommended before any runtime apply |
| Risks | Extra request-path complexity; must stay bounded to service hierarchy only |
| Rollback | Revert plugin source + redeploy |
| Expected URL outcome | Service 74 → HTTP 200 |
| Architecture compatibility | Acceptable fallback per contract §4.3 (“only if native resolution fails”) |
| Recommended | No (heavier than Option 2) |

---

## Option 2 — Rewrite rule repair

| Field | Value |
|---|---|
| Layer | rewrite rules |
| Exact intended change | In `ServicePermalinks::register_rewrite_rules`, change depth-2 query from `service=$matches[2]` to `service=$matches[1]/$matches[2]`; update permalink contract; deliver source; authorized soft rewrite flush |
| Objects affected | None (rules only) |
| Runtime writes later | `rewrite_rules` option only |
| Source changes later | Yes — `ServicePermalinks.php` + contract doc |
| DB checkpoint | Required before flush |
| Risks | Low; must verify Page `/uslugi/` still wins exact hub; depth-1 controls remain 200; no content drift |
| Rollback | Restore prior plugin source + restore rewrite_rules snapshot / re-flush prior rules |
| Expected URL outcome | Service 74 → HTTP 200 with existing permalink |
| Architecture compatibility | Aligns with hierarchical CPT lookup and `post_type_link` full-path generation |
| Recommended | **Yes** |

---

## Option 3 — Path ownership cleanup

| Field | Value |
|---|---|
| Layer | path ownership policy / migration object cleanup |
| Exact intended change | Later migrate/retire Page ID 6 so Service ID 73 solely owns `/uslugi/zavisimosti/` |
| Objects affected | Page ID 6 (status/slug/redirect policy TBD) |
| Runtime writes later | Page/object writes; possible redirect |
| Source changes later | No (content/migration) |
| DB checkpoint | Required |
| Risks | Touches historical page; menu/link references; must not be done as silent delete |
| Rollback | Restore Page 6 from checkpoint |
| Expected URL outcome | Does **not** alone fix Service 74 leaf-only rewrite mapping |
| Architecture compatibility | Required later for clean ownership; not primary 74 fix |
| Recommended | No as primary; schedule after Option 2 |

---

## Option 4 — Change service parent/path model

| Field | Value |
|---|---|
| Layer | object model |
| Exact intended change | Flatten hierarchy or change parent/slug model |
| Rejected | **Yes** |
| Reason | Architecture requires depth-2 parent/child services; object state is valid |

---

## Option 5 — Redirect workaround

| Field | Value |
|---|---|
| Layer | redirect/canonical |
| Exact intended change | Redirect leaf-only or alternate path to Service 74 |
| Rejected | **Yes** for canonical service route |
| Reason | Generated permalink is already correct; 404 is resolver mismatch, not missing URL. Redirect would mask the bug and not establish CPT ownership. |

---

## Comparison

| Option | Layer | Runtime writes later | Source changes later | Risk | Recommended |
|---|---|---:|---:|---|---:|
| Source resolver repair | request resolver | 0–1 flush | Yes | Medium | No |
| Rewrite rule repair | rewrite rules | rewrite_rules only | Yes | Low | **Yes** |
| Path ownership cleanup | ownership / migration | Page writes | No | Medium | Later |
| Change parent/path model | object model | Object writes | Maybe | High | Rejected |
| Redirect workaround | redirect | Redirect writes | No | High drift | Rejected |

## Mutations in this document

None applied.

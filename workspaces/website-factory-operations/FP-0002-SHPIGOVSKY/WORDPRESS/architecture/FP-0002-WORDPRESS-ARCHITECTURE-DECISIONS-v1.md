# FP-0002 WordPress Architecture Decisions v1

**Task:** V9-06A.1 | **Date:** 2026-07-03

| ID | Decision | Status | Value |
|----|----------|--------|-------|
| ADR-001 | Service CPT (`service`) | APPROVED | Hierarchical CPT for all `/uslugi/*` except hub Page |
| ADR-002 | Service taxonomy | REJECTED | Use `post_parent` hierarchy |
| ADR-003 | Native Pages for hubs/institutional | APPROVED | Pages for home, hub, o-centre, contacts, reviews, legal |
| ADR-004 | Native Posts for blog | APPROVED | No article CPT |
| ADR-005 | Header/footer ownership | APPROVED | Theme global shell once |
| ADR-006 | Global settings | APPROVED | ACF Pro Options Page — bounded |
| ADR-007 | ACF Pro | **APPROVED (OD-001)** | **Required** for FP-0002 |
| ADR-008 | Repeaters | APPROVED | ACF Pro bounded repeaters + server validation |
| ADR-009 | Template variants | APPROVED | Layout meta on service; page templates for hubs |
| ADR-010 | Service navigation | APPROVED | HYBRID_BOUNDED menus + home query |
| ADR-011 | URL/rewrite model | APPROVED | Hub Page + CPT `CPT_REWRITE_PLUS_POST_TYPE_LINK_FILTER` |
| ADR-012 | Blog model | APPROVED | posts_page + home.php; categories none at launch |
| ADR-013 | Legal model | APPROVED | Native Pages + legal template; DEMO tokens flagged |
| ADR-014 | Form model | APPROVED | Theme UI + plugin handler; no WPilot |
| ADR-015 | SEO boundary | APPROVED | Theme fallbacks; defer plugin |
| ADR-016 | Migration strategy | APPROVED | CREATE_NEW_SERVICE → validate → switch → retire Page |
| ADR-017 | Review entity | APPROVED | Page repeater — no review CPT |
| ADR-018 | Specialist entity | REJECTED | Section content only |
| ADR-019 | Flexible content | REJECTED | Forbidden |
| ADR-020 | FW-07C-2D timing | DEFERRED | Superseded by V9-06D object skeleton |
| ADR-021 | Menu locations | APPROVED | primary, footer_services, footer_o_centre, legal |
| ADR-022 | Alcohol special page | APPROVED | `layout=alcohol-special` variant |
| ADR-023 | Genotyping route | REJECTED | Must not publish |
| ADR-024 | V9-04 all-Pages model | REJECTED | Superseded by V9-06A architecture |
| ADR-025 | BoundedMeta primary path | **REJECTED (OD-001)** | ACF Pro is primary; BoundedMeta deferred as research |
| ADR-026 | Services hub entity | APPROVED | Native Page at `/uslugi/` — not a Service |
| ADR-027 | Service archive | APPROVED | `has_archive=false` |
| ADR-028 | Route classification model | APPROVED | Primary class + secondary subtype (V9-06A.1) |

---

## Operator decisions (integrated V9-06A.1)

| ID | Question | Approved value | Status |
|----|----------|----------------|--------|
| OD-001 | ACF Pro | **Required**; no Flexible Content; bounded repeaters only | **INTEGRATED** |
| OD-002 | `/specyalisty/` | **301 → `/uslugi/zavisimosti/specialistam/`** after target ready | **INTEGRATED** |
| OD-003 | Blog categories at launch | **NONE** | **INTEGRATED** |
| OD-004 | Blog article metadata | Date **visible**; author **hidden**; no public author archive | **INTEGRATED** |

---

*Decision log — planning authority. V9-06A.1 reconciliation complete.*

## V9-06B.2 dependency decisions

| ID | Decision | Status | Value |
|----|----------|--------|-------|
| ADR-029 | Operator-managed ACF PRO admission | APPROVED | ACF PRO v6.8.5 admitted as external dependency; public API use allowed after admission |
| ADR-030 | ACF Extended PRO use | NOT APPROVED BY DEFAULT | Keep active but not used unless explicitly authorized |
| ADR-031 | ACF plugin update/delivery policy | APPROVED | ACF PRO/ACFE PRO automatic update, replacement, deletion, and package delivery forbidden |

## V9-06C source implementation decisions

| ID | Decision | Status | Value |
|----|----------|--------|-------|
| ADR-032 | Content model source implementation | COMPLETE_SOURCE_ONLY | `service` CPT, permalink source, ACF groups, options page, admin UX and validation hooks implemented in canonical source |
| ADR-033 | ACF JSON source generation | COMPLETE_SOURCE_ONLY | 13 deterministic JSON groups generated under `WORDPRESS/acf-json/`; runtime ACF JSON writes remain 0 |
| ADR-034 | Runtime delivery boundary | NOT_STARTED | V9-06C did not deliver theme/plugin/ACF JSON to `X:\MARS-Localhost` |
| ADR-035 | WordPress object creation boundary | NOT_STARTED | Pages, Services, Posts, Menus, Options and runtime ACF field groups were not created |


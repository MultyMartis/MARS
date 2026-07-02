# FP-0002 WordPress Architecture Decisions v1

**Task:** V9-06A | **Date:** 2026-07-03

| ID | Decision | Status | Recommendation |
|----|----------|--------|----------------|
| ADR-001 | Service CPT (`service`) | APPROVED_RECOMMENDATION | Hierarchical CPT for all `/uslugi/*` except hub Page |
| ADR-002 | Service taxonomy | REJECTED | Use `post_parent` hierarchy |
| ADR-003 | Native Pages for hubs/institutional | APPROVED_RECOMMENDATION | Pages for home, hub, o-centre, contacts, reviews, legal |
| ADR-004 | Native Posts for blog | APPROVED_RECOMMENDATION | No article CPT |
| ADR-005 | Header/footer ownership | APPROVED_RECOMMENDATION | Theme global shell once |
| ADR-006 | Global settings | APPROVED_RECOMMENDATION | ACF options page — bounded |
| ADR-007 | ACF Free/Pro | MIXED | Free + plugin BoundedMeta; Pro optional |
| ADR-008 | Repeaters | APPROVED_RECOMMENDATION | BoundedMeta in plugin OR ACF Pro if operator chooses |
| ADR-009 | Template variants | APPROVED_RECOMMENDATION | Layout meta on service; page templates for hubs |
| ADR-010 | Service navigation | APPROVED_RECOMMENDATION | HYBRID_BOUNDED menus + home query |
| ADR-011 | URL/rewrite model | APPROVED_RECOMMENDATION | Hub Page + hierarchical CPT `uslugi/%service%` |
| ADR-012 | Blog model | APPROVED_RECOMMENDATION | posts_page + home.php; tags off |
| ADR-013 | Legal model | APPROVED_RECOMMENDATION | Native Pages + legal template; DEMO tokens flagged |
| ADR-014 | Form model | APPROVED_RECOMMENDATION | Theme UI + plugin handler; no WPilot |
| ADR-015 | SEO boundary | APPROVED_RECOMMENDATION | Theme fallbacks; defer plugin |
| ADR-016 | Migration strategy | APPROVED_RECOMMENDATION | Create-new service; retire old Pages |
| ADR-017 | Review entity | APPROVED_RECOMMENDATION | Page repeater — no review CPT |
| ADR-018 | Specialist entity | REJECTED | Section content only |
| ADR-019 | Flexible content | REJECTED | Forbidden |
| ADR-020 | FW-07C-2D timing | DEFERRED | Superseded by V9-06D object skeleton |
| ADR-021 | Menu locations | APPROVED_RECOMMENDATION | Extend to primary, footer_services, footer_o_centre, legal |
| ADR-022 | Alcohol special page | APPROVED_RECOMMENDATION | `layout=alcohol-special` variant — not collapsed to placeholder |
| ADR-023 | Genotyping route | REJECTED | Must not publish |
| ADR-024 | V9-04 all-Pages model | REJECTED | Superseded by this architecture for implementation planning |

---

## Operator decisions required

| ID | Question | Options |
|----|----------|---------|
| OD-001 | ACF Pro purchase vs BoundedMeta | Pro UX / Free+plugin |
| OD-002 | `/specyalisty/` retirement | 301 target or hard retire |
| OD-003 | Blog categories at launch | None / bounded set |
| OD-004 | Author/date visibility on articles | Show / hide |

---

*Decision log — planning authority.*

# Forge WordPress — CMS Anti-Patterns v1

**ID:** FW-S-31  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Namespace:** `AP-CMS-*` (does not reuse `AP-001`–`AP-018` numbers)  
**Parent registry:** [FW-S-21](FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md)

CMS modeling anti-patterns. Map to FP-0002 evidence where a production lesson exists. Client facts are generalized.

---

## AP-CMS-001 — Everything becomes a Page

| | |
|--|--|
| Symptom | Services/people/cases are child Pages; editors fight parent/template/generic body |
| Cause | “Pages already exist and have URLs” |
| Risk | Bad Admin UX; late CPT migration under production |
| Prevention | Entity detection + CPT matrix in P1b |
| Replacement | CPT + hub Page |
| Related | AP-001 |
| Evidence | P11 specialists Pages → CPT |

## AP-CMS-002 — Everything becomes an ACF repeater

| | |
|--|--|
| Symptom | 40–100 rows on a page; staff/services/reviews as repeaters |
| Cause | Repeaters are faster than registering a CPT |
| Risk | Unusable Admin; no search/sitemap/relations |
| Prevention | [REPEATER VS ENTITY](FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) |
| Replacement | CPT / taxonomy / relationship |
| Evidence | Reviews-as-options is **J** only when no public singles |

## AP-CMS-003 — Everything is editable

| | |
|--|--|
| Symptom | Hundreds of fields; CSS/margins/class names in ACF; editor confusion |
| Cause | “The client might want to change it” |
| Risk | Impossible validation; presentation internals exposed |
| Prevention | Static vs editable criteria |
| Replacement | Edit business content, not implementation details |

## AP-CMS-004 — Same business value stored in multiple locations

| | |
|--|--|
| Symptom | Header phone ≠ footer phone ≠ contacts |
| Cause | Per-partial ACF |
| Risk | Operator cannot set it once |
| Prevention | Ownership map |
| Replacement | [GLOBAL SETTINGS](FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) |
| Related | AP-007, AP-008 |
| Evidence | Site Settings SoT; contacts helpers |

## AP-CMS-005 — Internal destination stored as absolute manual URL

| | |
|--|--|
| Symptom | Staging hostname in buttons; broken links after cutover |
| Cause | URL field used for internal targets |
| Risk | Domain mutation of content; slug drift |
| Prevention | Post Object / relationship + `get_permalink()` |
| Replacement | [RELATIONSHIP MODELING](FORGE-WORDPRESS-RELATIONSHIP-MODELING-STANDARD-v1.md) |

## AP-CMS-006 — Editor exposed to raw CSS / classes

| | |
|--|--|
| Symptom | “Extra class”, color pickers, arbitrary font size |
| Cause | Page-builder habits |
| Risk | Design system collapse |
| Prevention | Semantic variants only |
| Replacement | Enums; theme-owned tokens |

## AP-CMS-007 — Giant flat ACF editor

| | |
|--|--|
| Symptom | Endless scroll; mixed Hero + GTM + gallery |
| Cause | One group, no tabs, no conditionals |
| Risk | Missed fields; editor refusal |
| Prevention | [ADMIN IA](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md) |
| Replacement | Tabs, groups, CPT split, Options split |
| Evidence | Profile groups with section notices; Site Settings sections |

## AP-CMS-008 — Nested repeater as a pseudo-database

| | |
|--|--|
| Symptom | Repeater-in-repeater with relationships inside |
| Cause | Avoiding CPT registration |
| Risk | Data you cannot query, search, or migrate cleanly |
| Prevention | Promotion checklist |
| Replacement | Entities + relationships |

## AP-CMS-009 — Demo content as production fallback

| | |
|--|--|
| Symptom | Lorem / demo images after fields cleared |
| Cause | Template fallbacks left as SoT |
| Risk | False content on production |
| Prevention | Empty → hide; class E fallback forbidden |
| Replacement | ACF SoT + empty-safe FE |
| Related | AP-009 |
| Evidence | E46-FIX05; P07 Lorem; P12 demo removed |

## AP-CMS-010 — Frontend component without empty-state contract

| | |
|--|--|
| Symptom | Blank cards, empty icon rows, headings with no text |
| Cause | Template always prints the shell |
| Risk | Broken UI; QA misses “empty Admin” |
| Prevention | Component contract empty-state slot |
| Replacement | [COMPONENT DATA CONTRACT](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md) |

## AP-CMS-011 — GUI field-schema change without source / version control

| | |
|--|--|
| Symptom | Production ACF UI drift; JSON not committed; renamed fields orphan meta |
| Cause | “Just add a field on live” |
| Risk | Environments diverge; silent data loss |
| Prevention | Local JSON in Git; migration plan for renames |
| Replacement | [ACF FIELD MODELING](FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) §11–12 |
| Related | R-ACF-01, R-VC-06 |

## AP-CMS-012 — WYSIWYG used instead of structured data

| | |
|--|--|
| Symptom | Phone, button label, or feature row in TinyMCE |
| Cause | One WYSIWYG “for flexibility” |
| Risk | Inconsistent cards; HTML in titles; no validation |
| Prevention | WYSIWYG policy |
| Replacement | Structured fields; basic toolbar only where rich text is real |

## AP-CMS-013 — Hardcoded design copied into content fields unnecessarily

| | |
|--|--|
| Symptom | Editors asked to paste layout HTML or keep invariant labels in ACF |
| Cause | Confusing presentation with content |
| Risk | Broken markup; unneeded translation surface |
| Prevention | Static vs editable |
| Replacement | Theme partials + few business fields |

## AP-CMS-014 — Relation modeled as free text

| | |
|--|--|
| Symptom | “Related specialist” as name/URL string |
| Cause | Faster than relationship field |
| Risk | Typos; no integrity; migration pain |
| Prevention | Object references |
| Replacement | [RELATIONSHIP MODELING](FORGE-WORDPRESS-RELATIONSHIP-MODELING-STANDARD-v1.md) |

## AP-CMS-015 — No editor workflow validation before launch

| | |
|--|--|
| Symptom | Only frontend pixel QA; client cannot perform basic tasks |
| Cause | CMS treated as a developer convenience |
| Risk | Post-launch Admin redesign |
| Prevention | Editor acceptance gate |
| Replacement | [EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md) |
| Evidence | FW-S-05 editor simulation; real wp-admin save tests |

---

*FW-S-31 v1 — 15 CMS anti-patterns. Add IDs in this namespace; do not reuse AP-001–018.*

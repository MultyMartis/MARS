# Forge WordPress — Editor UX Standard v1

**ID:** FW-S-26  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Extends:** [FW-S-05 Admin UX](FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md)  
**Companion:** [ADMIN IA](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md)

```text
CMS ARCHITECTURE IS VALIDATED THROUGH REAL EDITOR WORKFLOWS,
NOT ONLY FRONTEND OUTPUT.
```

FW-S-05 remains the curated-editor / role / Gutenberg-zone standard. This document is the **CMS-facing** editor contract: labels, help, roles, Gutenberg policy summary, and acceptance by workflow.

---

## 1. Labels and instructions

Admin labels are written for **editors**, not programmers.

| BAD | GOOD |
|-----|------|
| `hero_desc` | Описание |
| `cta_tgt` | Куда ведёт кнопка |
| `rel_ids` | Связанные услуги |

Field **names** may stay machine-oriented. Field **labels** use the project locale (Russian editors → Russian chrome, including ACF and plugin strings — [I18N](FORGE-WORDPRESS-I18N-STANDARD-v1.md)).

Instructions should answer:

- what appears here;  
- **where** it appears;  
- acceptable format;  
- optional vs required;  
- recommended length if meaningful;  
- empty behavior (“Пустое поле на сайте не показывается”).

Examples:

- «Показывается в шапке и подвале»  
- «Используется на карточке специалиста»  
- «Текст для SEO, на странице не отображается»

---

## 2. Adding a new specialist (canonical walkthrough)

The editor should succeed without knowing PHP or ACF keys:

1. **Специалисты → Добавить**  
2. Name = native title  
3. Photo = featured image (notice: no duplicate ACF portrait)  
4. Role / experience / profile fields in **Основное / Контент**  
5. Relations (services) if the design needs them  
6. SEO optional with fallback  
7. Publish / order in the list table  
8. Preview card + single  

If this requires a developer, Admin IA failed.

Generalize: “add a service”, “add an article”, “hide an optional section”, “change the global phone” must be equally obvious.

---

## 3. Editor role model (architecture-ready)

| Role | Sees | Must not see |
|------|------|----------------|
| **CLIENT EDITOR** | Pages/CPTs/posts per map; Site Settings content tabs (contacts, social, ordinary SEO fields) | Plugin install, theme file editor, raw head/body injection, Options dump, migration tools |
| **ADMINISTRATOR** | Full Admin; dangerous tabs | Still should not need public runners in webroot |
| **TECHNICAL OPERATOR** | Capability-gated tools, WPilot, deploy | Not a substitute for client editing |

Future WP Forge should restrict dangerous settings from normal client editors. **Implementation of custom roles is not required in this knowledge wave**, but screens must already **separate** Advanced fields so a later capability gate is possible.

Default: client cannot install plugins or use Site Editor unless Mode B is chartered (FW-S-05).

---

## 4. Gutenberg policy (editor view)

See [ACF FIELD MODELING](FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) §8.

Tell the editor in ADMIN-UX-MAP: which types use blocks, which use ACF, which are frozen. Do not surprise them with a full inserter on a PIXEL_PERFECT landing.

---

## 5. Preview and context

Where feasible, field help names the frontend surface. Known preview gaps (staging-only, modal JS) are listed in ADMIN-UX-MAP — not discovered at launch.

Empty settings must not render FE leftovers (FW-S-05 acceptance extra 14).

---

## 6. Editor acceptance gate

Before CMS architecture is **complete**, simulate actual workflows. Checklist template: [EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md).

Minimum set:

- change phone globally — all chrome updates;  
- add a new service;  
- add a specialist;  
- hide an optional section;  
- reorder items (`menu_order` or repeater);  
- add an article;  
- choose an internal CTA (object, not pasted URL);  
- change a social link — empty hides icon;  
- change SEO description.

If the editor must know implementation internals, architecture is not done (AP-CMS-015).

---

*FW-S-26 v1 — editor language, editor workflows, role boundaries.*

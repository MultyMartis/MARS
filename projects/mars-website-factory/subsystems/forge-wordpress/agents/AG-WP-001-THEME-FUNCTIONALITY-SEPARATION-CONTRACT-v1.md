# AG-WP-001 — Theme and Functionality Separation Contract v1

**Document type:** Separation contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Aligns with:** FW-S-03, FW-S-04, [FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md](../standards/FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md), [FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](../standards/FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md)

---

## 1. Theme responsibilities

- Visual presentation
- Templates and template parts
- Asset loading (CSS/JS enqueue)
- Layout and styling
- Presentational JS (sliders, modals UI — unless delegated to functionality)
- Theme supports (`add_theme_support`)
- Editor styles where operator-approved
- Template hierarchy mapping from approved frontend

---

## 2. Functionality plugin responsibilities

- Custom post types and taxonomies
- Business rules and domain logic
- Reusable non-presentational logic
- Third-party integrations (forms API, CRM, analytics hooks)
- Form processing where applicable
- REST/API extensions
- Project settings and options pages
- Durable data behaviour independent of active theme

**Naming:** `{project-slug}-functionality` or documented equivalent.

---

## 3. Forbidden theme coupling

| Anti-pattern | Why forbidden |
|--------------|---------------|
| Critical business data disappears on theme switch | Data must live in plugin/CPT/meta |
| CPT registration **only** in theme | Breaks on theme change |
| Integration credentials in theme | Security + portability |
| Irreversible content transformation in templates | Migration risk |
| Arbitrary admin logic mixed with presentation | Unmaintainable |

---

## 4. Allowed theme references

Theme may **call** functionality plugin APIs (template tags, hooks) — plugin must not depend on theme classes.

---

## 5. Exception process

Exceptions require:

1. Written rationale in architecture decision record
2. Risk class assessment
3. **Explicit operator approval**
4. Documented rollback if exception fails

---

## 6. AG-WP-001 enforcement

During architecture proposal (workflow phase 4–5), agent must produce **both** theme plan and functionality plan. Single combined "theme does everything" proposal is **rejected** unless exception approved.

---

*Separation contract v1 — presentation vs durability.*

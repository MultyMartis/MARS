# Forge WordPress — i18n Standard v1

**ID:** FW-S-18  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Class:** A  
**Evidence:** FP-0002 E39 foundation; P13 locale packs; D8-G English Admin labels as failure

---

## 1. Rule

All custom theme/plugin/Admin modules use WordPress i18n **from the first commit of that module**.

Anti-pattern: hardcoded mixed-language Admin strings, then a mass gettext refactor.

---

## 2. Requirements

| Item | Requirement |
|------|-------------|
| Text domain | One plugin domain + one theme domain; declared |
| Functions | `__`, `_e`, `esc_html__`, `_n`, `_x` as appropriate |
| POT | Generated and Git-tracked |
| Locale packs | At least project locale (typically `ru_RU`) |
| en_US | Source strings may be English **or** Russian; be consistent; ship the other locale as translations |
| load | `load_plugin_textdomain` / `load_theme_textdomain` |

Russian-editor sites: **Russian Admin chrome** is a product requirement, not a later polish.

---

*FW-S-18 v1.*

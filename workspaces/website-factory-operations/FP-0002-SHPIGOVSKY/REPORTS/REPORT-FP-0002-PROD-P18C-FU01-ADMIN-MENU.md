# REPORT — FP-0002 PROD-P18C-FU01 Admin Menu Exposure

**Date:** 2026-08-19  
**Core:** `0.3.13-p18c-fu01`  
**Parity:** `4/4 SOURCE ↔ PRODUCTION MATCH`  
**Evidence:** `REPORTS/evidence/prod-p18c-fu01-admin-menu/`

P18C underlying SMTP/forms/leads code already existed. The editor could not discover **Почта и формы** in the normal left menu. This follow-up corrects runtime reachability. It does **not** rewrite the historical P18C report as if the bug never existed.

---

## 1. Status

**PASS**

## 2. Admin Reality

**P18C-FU01 ADMIN REALITY VERIFIED**

- Visible parent «Настройки сайта» WP slug = `fp02-site-settings-general` (not `fp02-site-settings`).
- Olya `admin` and `mars`: Administrators, `manage_options` true.
- Unauthenticated: `manage_options` false.
- Modules `admin.mail-forms` and `admin.leads` enabled; P18C hashes were already in production.

## 3. Root Cause

**SMTP / FORMS ADMIN MENU ROOT CAUSE PROVEN** — class **C** (parent slug mismatch) + **J** (callback/page existed, menu link not on the visible parent).

ACF `redirect => true` promotes the first child slug as the WordPress top-level menu. P18C registered `add_submenu_page( OptionsPage::PARENT_SLUG )` against the logical slug `fp02-site-settings`, creating an orphan submenu. P18C QA rendered `MailFormsSettings::render_page()` directly and never inspected `$submenu` of the visible parent.

`acf_get_options_page()` still returns the logical slug; `acf_get_options_pages()[parent]['menu_slug']` is the mutated visible slug. Custom menus must register **after** ACF (`admin_menu` 100) on `OptionsPage::visible_menu_slug()`.

## 4. Fix

| Item | Value |
|------|--------|
| Files | `MailFormsSettings.php`, `OptionsPage.php`, `SystemDashboard.php`, `shpigovsky-core.php` |
| Registration owner | **one:** `MailFormsSettings` |
| Parent slug | `OptionsPage::visible_menu_slug()` → `fp02-site-settings-general` |
| Hook | `admin_menu` priority **100** (after ACF 99) |
| Position | 3 (after SEO и интеграции) |
| Capability | `manage_options` |
| Core | `0.3.13-p18c-fu01` |

No SMTP architecture change. No credentials. No suppression/indexing change.

## 5. Site Settings Menu

**`НАСТРОЙКИ САЙТА → ПОЧТА И ФОРМЫ` VISIBLE**

Label and H1: **Почта и формы**. One path only.

## 6. Settings Page

SMTP fields, write-only empty password, sender, recipients repeater, Metrika goal (counter remains SEO). State **NOT CONFIGURED**.

## 7. Leads

**`ЗАЯВКИ` ADMIN SECTION REACHABLE** — top-level menu, list renders, no PHP/DB error.

## 8. Runtime State

| Item | State |
|------|--------|
| SMTP | **NOT CONFIGURED** |
| Mail | **SUPPRESSED** |
| Indexing | **CLOSED** (`blog_public=0`, robots `Disallow: /`) |

## 9. Dashboard

Aligned: **SMTP SETTINGS READY — CREDENTIALS REQUIRED** is true now that the page is discoverable. Wave label `P18C-FU01 Admin menu exposure`.

## 10. Regression

- Consultation form still present on WP origin privacy; persist QA accepted `MAIL_SUPPRESSED`; QA row deleted.
- No real mail sent.
- Indexing unchanged.
- ACF Site Settings children preserved.

## 11. Source / Production Parity

**4/4 MATCH**

## 12. WP Forge Knowledge

**ADMIN FEATURE ACCEPTANCE NOW REQUIRES DISCOVERABILITY THROUGH NORMAL EDITOR NAVIGATION**

Sequence: REGISTERED → VISIBLE → ACCESSIBLE → EDITABLE → SAVE/RELOAD → OPERATOR DISCOVERABLE. Anti-pattern **AP-029**.

## 13. Git

Isolated worktree from `origin/mars/canonical-post-recovery`. Dirty main foreign WIP untouched. See `GIT-CHECKPOINT.json`.

## 14. Operator Next Action

1. Open **Настройки сайта → Почта и формы**
2. Enter SMTP host, port, encryption, username, password, recipients
3. Save
4. Do not open indexing
5. Report **SMTP SETTINGS SAVED**

## 15. Acceptance

**FP-0002 P18C-FU01 COMPLETE — SMTP / FORMS SETTINGS ARE NOW DISCOVERABLE THROUGH NORMAL WORDPRESS ADMIN NAVIGATION — OLYA/ADMIN CAN OPEN AND USE `НАСТРОЙКИ САЙТА → ПОЧТА И ФОРМЫ` — LEADS ADMIN IS REACHABLE — SMTP REMAINS UNCONFIGURED UNTIL OPERATOR INPUT — MAIL SUPPRESSION REMAINS ACTIVE — INDEXING REMAINS CLOSED — WP FORGE NOW TREATS ADMIN DISCOVERABILITY AS PART OF FEATURE DEFINITION OF DONE**

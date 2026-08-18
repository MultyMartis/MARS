# ROOT CAUSE — SMTP / FORMS ADMIN MENU

**Required:** `SMTP / FORMS ADMIN MENU ROOT CAUSE PROVEN`  
**Wave:** P18C-FU01  
**Date:** 2026-08-19  
**Evidence:** `ADMIN-REALITY-BEFORE.json`

## Class

**C — parent slug mismatch** (primary)  
**J — page exists / callback works, visible menu link missing** (operator symptom)  
**G — registration order is a contributing hazard** (custom `admin_menu` at 21 vs ACF at 99)

Not A (unregistered), D (intentionally hidden by hygiene), E (capability), F (module not loaded), H (duplicate slug), or I (source vs runtime missing). Modules were enabled; hashes matched P18C; `manage_options` held by `admin` (Olya) and `mars`.

## What production actually registered

| Surface | Fact |
|---------|------|
| Logical ACF parent | `fp02-site-settings` (`OptionsPage::PARENT_SLUG`) |
| Visible WP top-level «Настройки сайта» | slug **`fp02-site-settings-general`** |
| Logical parent in `$menu` | **null** (no top-level item) |
| `Почта и формы` under logical parent | **yes** (orphan `$submenu['fp02-site-settings']`) |
| `Почта и формы` under visible parent | **no** |
| Direct `MailFormsSettings::render_page()` | **works** (fields, write-only password, recipients, Metrika) |
| `Заявки` top-level | **yes** (`fp02-form-leads`, pos 56) |

ACF `redirect => true` rewrites the parent options page `menu_slug` to the first child (`fp02-site-settings-general`). All ACF Site Settings children attach there. P18C called `add_submenu_page( OptionsPage::PARENT_SLUG, … )` with the **logical** slug, so WordPress stored an orphan submenu that never appears under the editor-facing parent.

P18C QA called `render_page()` directly and never inspected `$submenu` of the **visible** parent. That is why the report could claim `Настройки сайта → Почта и формы` while Olya could not see the item.

## Why `admin_menu` priority 21 is unsafe even with the right slug

ACF registers options menus at priority **99**. WordPress `add_menu_page()` **replaces** `$submenu[ $menu_slug ]` with the auto-duplicate parent row. A custom `add_submenu_page()` at 21 would be wiped when ACF later creates the visible parent. FU01 registers at **100**.

## Fix owner

One registration owner remains `MailFormsSettings`. Parent resolution is owned by `OptionsPage::visible_menu_slug()`. No second ACF options page, no extra top-level SMTP/Forms/Mailer menu.

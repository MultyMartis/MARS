# Forge WordPress — Typography Pipeline Standard v1

**ID:** FW-S-14  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Evidence:** FP-0002 P08 PARTIAL (write-time / source strings) → P16 canonical render-time

---

## 1. Anti-pattern (AP-004)

**Broad stored DB typography rewriting** of WYSIWYG/options/post_content.

Risks: HTML/shortcode/embed corruption; irreversible content mutation; URL/email/slug damage; fights the editor.

P08 migrated some specialist fields and source PHP strings; **mass DB rewrite was correctly STOPPED**.

---

## 2. Canonical pattern

```text
ONE safe, idempotent, HTML-aware, RENDER-TIME typography owner
```

- Functionality plugin module (e.g. filters on `the_title`, `the_content`, `the_excerpt`, ACF `format_value` for text/textarea/wysiwyg, document title parts).
- Process **text nodes only** after a conservative HTML split.
- **Exclude:** `script`, `style`, `code`, `pre`, `textarea`, `svg`, and similar.
- **Do not mutate:** URLs, emails, slugs, `post_name`, attributes that are URLs.
- Russian (when locale needs it): NBSP after prepositions/particles; «ёлочки»; dashes — project rule set versioned in code.
- Idempotent: running twice does not stack entities like `&amp;nbsp;`.
- Admin stored copy stays as typed (presentational only on FE).
- TOC heading IDs: assign **before** typography (`the_content` earlier priority).
- Smart Search / matchers: normalize NBSP → space before compare.
- DOCX importer: write raw `post_content`; pipeline applies on render.
- SEO meta: plain Unicode processing + `esc_attr` / `esc_html` as appropriate — do not write HTML entities into meta.

---

## 3. Source strings

PHP/theme visible strings may be authored already typographed **or** passed through the same helper. Prefer one helper to avoid drift.

---

## 4. When a stored rewrite is ever allowed

Only a chartered, dry-run, field-allowlist, MANUAL_REVIEW gate, with backups — and usually **still prefer render-time**. FP-0002 P16 persisted **0** DB typography rows.

---

*FW-S-14 v1.*

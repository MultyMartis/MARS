# FP-0002 V9-06E0 — Legal Authority Audit v1

**Phase:** V9-06E0  
**Date:** 2026-07-06  
**Evidence:** `validation/v9-06e0-legal-native-content-review/legal-authority-audit.json`

---

## Authority layers

| Layer | Location | Status |
|-------|----------|--------|
| Production authoritative (Shpigovsky) | — | **NONE VERIFIED** |
| MARS reference templates | `workspaces/website-factory-reference-v1/legal/*.md` | Structure + variables; not operator-approved copy |
| V9 static demo pages | `workspaces/fp-0002-shpigovsky-v8/src/pages/*.html` | `data-content-status=demo-placeholder`; robots noindex |
| V9 legal contract | `workspaces/fp-0002-shpigovsky-v9/forge-intake/legal/` | DEMO token register; production gate documented |
| WP runtime native | DB `mars_wp_fp0002` | ID 3 garbled; 22–24 empty; 25 placeholder |

Per V9-02 `FP-0002-V9-LEGAL-AUTHORITY-MAP-v1.md`: **PROJECT_SPECIFIC_EXAMPLE: None verified for FP-0002 Shpigovsky legal entity.**

---

## Privacy page authority conflict

| Role | Page ID | Slug | Status |
|------|--------:|------|--------|
| Canonical route (D3 / footer fallback) | 3 | privacy-policy | draft + garbled seed |
| WP Settings → Privacy Policy | 25 | privacy-policy-page | publish + placeholder |

**Conflict:** WordPress core privacy tools reference **#25** while public footer links target **#3** slug.

---

## Legal template mapping

| Route | WP ID | V9 source | ACF group |
|-------|------:|-----------|-----------|
| `/privacy-policy/` | 3 | `src/pages/privacy-policy.html` | `group_fp02_page_legal` |
| `/user-agreement/` | 22 | `src/pages/user-agreement.html` | same |
| `/consent-personal-data/` | 23 | `src/pages/consent-personal-data.html` | same |
| `/cookie-files-policy/` | 24 | `src/pages/cookie-files-policy.html` | same |

Frontend rendering: `page-templates/legal.php` + skeleton `template-parts/legal/document-page.php` — **body not implemented**.

---

## Checks

| Check | Result |
|-------|--------|
| Authoritative Shpigovsky copy in repo | **FAIL** |
| Reference templates available | **PARTIAL** |
| Garbled seed in DB (ID 3) | **CONFIRMED** |
| Demo-only V8/V9 static legal | **CONFIRMED** |
| Privacy setting alignment | **NEEDS_REPAIR** |

---

## Verdict

**PARTIAL** — authority state is documented; operator must supply or approve legal copy before E1 seed.

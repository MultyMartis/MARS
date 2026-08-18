# Forge WordPress — Search Indexing Control Standard v1

**ID:** FW-S-32  
**Status:** ACTIVE — PRODUCTION PROVEN (FP-0002 P18B)  
**Date:** 2026-08-19  
**Class:** C / D / E / G  
**Evidence:** FP-0002 MetaCODE Dashboard indexing control; `blog_public` + physical/`robots.txt` + core meta robots

---

## 1. Rule

```text
SEARCH ENGINE INDEXING IS A BUSINESS/LAUNCH APPROVAL GATE,
NOT A SIDE EFFECT OF DEPLOYMENT.
```

Default launch automation **stops before** opening indexing unless explicit human approval exists.

Do **not** require auto-open at launch. Do **not** open indexing because HTTPS, DNS, or the domain “works”.

---

## 2. Human approval

Allowed ways to open indexing:

1. Named business owner explicitly requests it; or  
2. That owner clicks the Admin control; or  
3. The operator explicitly charters opening it.

For FP-0002 the approval owner is **Olya** or an explicit operator command.

```text
INDEXING OPEN REQUIRES EXPLICIT HUMAN ACTION
```

---

## 3. One semantic owner

Define a single operation:

```text
SET SITE INDEXABILITY = OPEN / CLOSED
```

That operation must keep **all current owners** consistent:

| Surface | Closed | Open |
|---------|--------|------|
| `blog_public` | `0` | `1` |
| robots.txt | `Disallow: /` | crawl allowed (WP-style `/wp-admin/` disallow only) |
| Site-level meta robots | `noindex` (core) | indexable except explicit exclusions (search, thank-you, private) |

Do **not** change only `blog_public` while a static `robots.txt` or a custom module still forces the opposite.

Search-result / private exclusions may remain `noindex` when the site is OPEN.

---

## 4. Dashboard control (recommended baseline)

If the project has a staging / pre-launch lifecycle, the operations Dashboard must show:

- **INDEXING CLOSED** or **INDEXING OPEN** from **runtime**, not a decorative flag.

When CLOSED: prominent Russian (or site locale) warning **before** the status table; primary action **Открыть индексацию**.

When OPEN: clear positive state (not alarm styling); secondary action **Закрыть индексацию**.

Recommended flow:

```text
button → confirmation → POST → capability + nonce
→ mutation → verification → result notice
```

Safety:

- Administrators / `manage_options` (or a named technical capability)
- WordPress nonce
- POST only (no GET mutation; no `admin_post_nopriv`)
- Confirmation required
- Reversible
- Status derived from real `blog_public` / robots / meta
- Do **not** auto-submit sitemaps or configure Search Console / Yandex Webmaster

---

## 5. Relation to launch SOP

SMTP proof and form delivery remain **recommended before** opening indexing (AP-015).  
The control exists so a human can still **wait** after those gates.

Opening the control is **not** authorization to launch indexing during an implementation wave unless the charter says so.

---

*FW-S-32 v1.*

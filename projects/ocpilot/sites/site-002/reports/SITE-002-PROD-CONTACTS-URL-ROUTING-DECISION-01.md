# REPORT — SITE-002 Contacts URL Routing Decision

**Operation ID:** SITE-002-PROD-CONTACTS-URL-ROUTING-DECISION-01  
**OCPilot Run:** 4.238 — SITE-002 Contacts URL Routing Decision  
**Date:** 2026-07-09  
**Environment:** DOCUMENTATION_ONLY (`https://bzpm.ru/`)  
**Baseline before:** SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01  
**Related review:** SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01 (Run 4.237)  
**Checkpoint after:** unchanged

---

## 1. Scope

Documentation-only operator routing decision after Run 4.237 contacts URL routing review.

**Allowed:** decision report; addendum to Run 4.237 report; OCPilot authority updates; selective git commit.

**Forbidden (not performed):** FTP upload; DB write; OpenCart admin save; `oc_seo_url` change; `.htaccess` redirect; header/footer/corp link edits; `llms.txt` change; sitemap controller patch; cache clear; production mutation of any kind.

---

## 2. Related discovery

Run 4.237 discovery facts remain valid:

| Finding | Value |
|---------|-------|
| `/contact` | **200** — live contacts page |
| `/kontakty` | **404** |
| `/contacts` | **404** |
| `index.php?route=information/contact` | **200** → `/contact` |
| Route owner | Native OpenCart `information/contact` |
| `oc_seo_url` | `information/contact` → keyword `contact` (id **846**) |
| `kontakty` SEO keyword | **Absent** |
| Internal links | All point to `/contact` — **no** broken `/kontakty` links |
| `llms.txt` | `https://bzpm.ru/contact` |
| Sitemap | Does **not** emit native `information/contact` |

Source: [SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01.md](SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01.md)

---

## 3. Operator decision

The operator clarified routing authority for SITE-002 Production contacts:

- **`/contact` remains the canonical contacts URL.**
- **`/kontakty` 404 is not considered a bug.**
- **No migration** from `/contact` to `/kontakty`.
- **No DB SEO keyword update** (`contact` → `kontakty`).
- **No 301** `/contact` → `/kontakty`.
- **No header/footer/corp link changes** toward `/kontakty`.
- **No `llms.txt` change** for `/kontakty`.
- **No sitemap patch** specifically for `/kontakty`.

---

## 4. Corrected interpretation

Run 4.237 discovery facts are **accepted**. Its **implementation recommendation (Option E — migrate to `/kontakty`) is rejected** by operator clarification in this run.

`/contact` was always the intended normal canonical URL for the contacts page. `/kontakty` is not a required project URL. A `/kontakty` 404 is acceptable when internal links, canonical tags, and `llms.txt` consistently use `/contact`.

---

## 5. Rejected implementation recommendation

The following Run 4.237 recommendations are **rejected** and must **not** be implemented:

| Rejected item | Run 4.237 reference |
|---------------|---------------------|
| Option E hybrid migration to `/kontakty` | §9–§10 |
| DB UPDATE `oc_seo_url` id 846 — keyword `contact` → `kontakty` | §10 step 1 |
| 301 `/contact` → `/kontakty` in `.htaccess` | §10 step 2 |
| header/footer + corp twig link updates to `/kontakty` | §10 step 3 |
| `google_sitemap.php` patch for `/kontakty` | §10 step 4 |
| `llms.txt` URL update to `/kontakty` | §10 step 5 |
| Charter `SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-01` | §10 |

**No contacts routing implementation task is currently planned.**

---

## 6. Current canonical contacts URL

| Field | Value |
|-------|-------|
| Canonical URL | `https://bzpm.ru/contact` |
| HTTP status | **200** |
| Route | `information/contact` |
| SEO keyword | `contact` (`oc_seo_url` id **846**) |
| Canonical tag | `https://bzpm.ru/contact` |
| Internal links | header, footer, 5 corp pages → `/contact` |
| `llms.txt` | `https://bzpm.ru/contact` |
| `/kontakty` | **404** — accepted, not a production bug |

---

## 7. Future optional SEO hygiene

Current sitemap does **not** emit native `information/contact` (contacts is not an `oc_information` row; `google_sitemap.php` lists `oc_information` pages only).

This may be considered later as a **separate low-priority** task:

**`SITE-002-PROD-CONTACT-SITEMAP-INCLUSION-01`** — add `/contact` to sitemap feed if SEO hygiene requires it.

This is **not** required to resolve `/kontakty`, because `/kontakty` is **not** canonical and is **not** targeted for implementation.

---

## 8. Production mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| FTP writes | 0 |
| FTP reads/listings | 0 |
| FTP downloads | 0 |
| Admin saves | 0 |
| DB SELECTs | 0 |
| DB direct writes | 0 |
| Mail sends | 0 |
| Form submits | 0 |
| SMTP changes | 0 |
| Live code changes | 0 |
| Category data changes | 0 |
| Product data changes | 0 |
| SEO URL changes | 0 |
| Redirect changes | 0 |
| Sitemap changes | 0 |
| Robots changes | 0 |
| llms.txt changes | 0 |
| Header/footer changes | 0 |
| Yandex.Metrika/Webmaster changes | 0 |
| Cron/import runs | 0 |
| Monitor runs triggered | 0 |
| Cache clears | 0 |
| Local cleanup/delete/move | 0 |
| public БЗПМ introduced | no |

---

## 9. Authority updates

Updated in-repo:

- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/OPERATIONAL-INDEX.md` — Run **4.238**; Run **4.237** annotated
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/sites/site-002/tools/README.md`
- Addendum appended to `SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01.md`

**Checkpoint unchanged:** `SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01`

Storage manifest (optional): `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CONTACTS-URL-ROUTING-DECISION-01\manifests\operation.json`

---

## 10. Git status

Selective commit for documentation paths only. Storage artefacts and foreign WIP **not** staged.

---

## 11. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| External backlinks to `/kontakty` | **SAFE UNKNOWN** — unchanged from Run 4.237 |
| Search Console indexed URL counts for `/contact` vs `/kontakty` | **SAFE UNKNOWN** — operator data |
| Sitemap inclusion benefit for `/contact` | **Deferred** — optional future hygiene only |
| Run 4.235 post-1C Lari reparent verification | **Still pending** — unrelated to this decision |

**Blockers for this decision:** **None** — operator decision is explicit.

---

## 12. Final verdict

**SITE-002 CONTACTS URL ROUTING DECISION COMPLETE — /CONTACT KEPT AS CANONICAL**

---

## 13. Next task recommendation

1. **No contacts routing implementation** — Run 4.237 Option E charter is **rejected**; do not launch `SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-01`.
2. **Optional later:** `SITE-002-PROD-CONTACT-SITEMAP-INCLUSION-01` — sitemap emission for `/contact` only, if SEO hygiene is desired.
3. **Inherited pending:** Run 4.235 post-1C Lari reparent verification.

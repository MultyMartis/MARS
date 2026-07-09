# REPORT — SITE-002 Contacts URL Routing Review

**Operation ID:** SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01
**OCPilot Run:** 4.237 — SITE-002 Contacts URL Routing Review
**Date:** 2026-07-09
**Environment:** PRODUCTION (`https://bzpm.ru/`) — read-only
**Baseline before:** SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01
**Checkpoint after:** unchanged (discovery only)

---

## 1. Scope

Read-only discovery for `/kontakty` routing on SITE-002 Production:

- public HTTP snapshot of contact URL candidates and regression URLs;
- sitemap and internal link inventory;
- DB read-only inspection of `oc_information` / `oc_seo_url`;
- FTP source map for routing, templates, header/footer, sitemap feed;
- routing analysis and implementation charter for a follow-up mutation task.

**No production mutation** — no FTP upload, DB write, redirect, SEO URL change, cache clear, admin save, form submit, import, or monitor run.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` @ `93bd183c` |
| Staged changes before task | **None** scoped to this operation |
| Foreign WIP | Present elsewhere — **not staged** |
| STOP tokens | **None** |

---

## 3. Public HTTP snapshot

| URL | Status | Final URL | Title | H1 | Canonical | Contact signs |
|-----|--------|-----------|-------|-----|-----------|---------------|
| `/kontakty` | **404** | `/kontakty` | Страница не найдена | Страница не найдена | — | footer shell only |
| `/contact` | **200** | `/contact` | Контакты | Контакты | `https://bzpm.ru/contact` | phone, address, map, form, requisites |
| `/contacts` | **404** | `/contacts` | Страница не найдена | Страница не найдена | — | footer shell only |
| `index.php?route=information/contact` | **200** | `/contact` | Контакты | Контакты | `https://bzpm.ru/contact` | full contacts page |
| `information_id=7` | **200** | `/user-agreement` | Пользовательское соглашение | … | — | not contacts |
| `information_id=4` | **200** | `/about_us` | О нас | О нас | — | not contacts |
| `route=information/information` (no id) | **404** | — | Информационная страница не найдена! | — | — | — |

Regression URLs (`/`, `/katalog`, neutral hub, nested lari, `sitemap.xml`, `robots.txt`, `llms.txt`) — all **200** as expected. **0** public **БЗПМ** on probed pages.

### Answers

| Question | Answer |
|----------|--------|
| Is `/kontakty` currently 404? | **Yes** |
| Working contacts page under another URL? | **Yes — `/contact` (200)** |
| Native `information/contact` working? | **Yes** — resolves to `/contact` |
| Information page that should be contacts? | **No** — ids 4/7 are О нас / Пользовательское соглашение |
| Redirect from `/kontakty`? | **No** — direct 404 |
| Best current canonical contacts URL | **`/contact`** (live canonical tag + SEO keyword) |
| Recommended target canonical | **`/kontakty`** (Russian SEO slug; not live today) |

Storage: `deployments/SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01/http-snapshots/`

---

## 4. Sitemap and internal links

### Sitemap (`1408` URLs)

| Pattern | In sitemap? |
|---------|-----------|
| `/kontakty` | **No** |
| `/contact` | **No** |
| `/contacts` | **No** |
| `information/contact` | **No** |

**Cause:** `google_sitemap.php` emits products, categories, manufacturers, and **`oc_information` pages only** — it does **not** emit the native `information/contact` route. Corp pages like `/delivery` appear because they are `oc_information` records with SEO keywords; contacts is a separate controller.

### Internal links (live HTML crawl)

| Finding | Detail |
|---------|--------|
| Links to `/kontakty` | **None found** |
| Links to `/contact` | **Yes** — header, footer, all 5 corp pages |
| Header/footer broken? | **No** — `/contact` works |
| `/kontakty` in sitemap? | **No** |
| Should sitemap include contacts after fix? | **Yes** — requires feed patch or architectural change |

Representative links:

- `header.twig`: `href="/contact"` — Контакты
- `footer.twig`: `href="/contact"` — Контакты
- Corp twigs (`payment`, `delivery`, `dealers`, `guarantee`, `custom_equipment`): inline `<a href="/contact/">Контакты</a>`
- `llms.txt`: `https://bzpm.ru/contact`

Storage: `sitemap/`, `links-inventory/`

---

## 5. DB information / SEO URL structure

**Prefix:** `oc_`
**DB SELECTs:** 7 (read-only via SSH mysql)

### Information pages matching contact title probe

| information_id | Title | Status |
|----------------|-------|--------|
| 4 | О нас | 1 |
| 7 | Пользовательское соглашение | 1 |

**No** `Контакты` row in `oc_information`.

### SEO URL records (contact-related)

| seo_url_id | keyword | query |
|------------|---------|-------|
| **846** | `contact` | `information/contact` |

**`kontakty` keyword rows: 0**

### Answers

| # | Question | Answer |
|---|----------|--------|
| 1 | Контакты information page exists? | **No** |
| 2 | Active? | n/a |
| 3 | information_id? | n/a — owner is native route |
| 4 | SEO keyword `kontakty`? | **No** |
| 5 | `/kontakty` missing because SEO URL absent? | **Yes** |
| 6 | Route mismatch? | **No** — route works; pretty slug is English `contact` |
| 7 | Native `information/contact` separate? | **Yes** — dedicated controller/template |
| 8 | Fix type | **SEO URL + link updates + optional 301 + sitemap feed patch** |

Storage: `db-readonly/`

---

## 6. FTP / source discovery

**FTP downloads:** 15 files
**FTP listings:** included in download loop

| Remote path | Role | kontakty | contact link | Change likely? |
|-------------|------|----------|--------------|----------------|
| `catalog/controller/information/contact.php` | native contact controller | no | route refs | maybe |
| `catalog/view/.../information/contact.twig` | contact UI (cards, map, form) | no | no | maybe |
| `catalog/controller/startup/seo_url.php` | SEO routing | no | no | no |
| `catalog/controller/startup/seo_pro.php` | SEO PRO | no | no | no |
| `catalog/controller/extension/feed/google_sitemap.php` | sitemap feed | no | no | **yes** — add contact URL |
| `common/header.twig` | header nav | no | **yes** `/contact` | **yes** → `/kontakty` |
| `common/footer.twig` | footer nav | no | **yes** `/contact` | **yes** → `/kontakty` |
| `.htaccess` | redirects | no | no | maybe 301 `/contact` |
| corp `information/*.twig` (5) | inline cross-links | no | **yes** `/contact/` | **yes** → `/kontakty/` |

Native contact template includes: address card, phone, Yandex map link, requisites, contact form (`information/contact` POST).

Storage: `ftp-source/`

---

## 7. Routing analysis

1. **Target canonical URL:** `/kontakty` (recommended for Russian SEO; not live today).
2. **Current live canonical:** `/contact` via `oc_seo_url` id **846**.
3. **Owner:** OpenCart native **`information/contact`** — **not** an `oc_information` page.
4. **Why `/kontakty` fails:** missing `oc_seo_url.keyword = kontakty`; no redirect configured.
5. **Why sitemap omits contacts:** `google_sitemap.php` never calls `information/contact`.
6. **Internal links:** all point to working `/contact`; **no** broken `/kontakty` links found.

Storage: `routing-analysis/contacts-routing-analysis.json`

---

## 8. Target final state

| Field | Value |
|-------|-------|
| Canonical URL | `https://bzpm.ru/kontakty` |
| HTTP status | **200** |
| Route | `information/contact` |
| SEO query | `information/contact` |
| SEO keyword | `kontakty` |
| Legacy `/contact` | **301 → `/kontakty`** (recommended) |
| Header/footer | `/kontakty` |
| Corp inline links | `/kontakty/` |
| Sitemap | include `/kontakty` (feed patch required) |
| `llms.txt` | update to `/kontakty` |
| Contact form | unchanged native POST |

---

## 9. Implementation strategy options

| Option | Description | Fit |
|--------|-------------|-----|
| **A** | Add `oc_seo_url` `kontakty` → `information/contact` | Core fix |
| **B** | SEO URL for `information_id=N` | **Not applicable** — no contacts information page |
| **C** | 301 only `/kontakty` → `/contact` | **Wrong direction** — preserves English slug |
| **D** | Source route patch | **Not needed** — route exists |
| **E** | **Hybrid (recommended)** | SEO keyword swap + 301 `/contact` + link updates + sitemap patch + `llms.txt` |

---

## 10. Recommended implementation charter

**Charter:** `SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-01`
**Storage:** `deployments/SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01/implementation-charter/`

**Recommended wave (Option E):**

1. **DB:** UPDATE `oc_seo_url` id **846** — keyword `contact` → `kontakty` (query unchanged `information/contact`).
2. **Redirect:** `.htaccess` 301 `/contact` → `/kontakty` (if old slug must keep resolving during transition).
3. **Links:** header.twig, footer.twig, 5 corp information twigs — `/contact` → `/kontakty`.
4. **Sitemap:** patch `google_sitemap.php` to emit `information/contact` URL once.
5. **llms.txt:** update Контакты URL.
6. **Cache:** clear SEO URL / SEO PRO cache.
7. **Verify:** `/kontakty` 200, form intact, 0 БЗПМ, regression URLs stable.

---

## 11. Risks and no-go conditions

| Risk | Mitigation |
|------|------------|
| SEO PRO duplicate keyword on `kontakty` | Pre-check `oc_seo_url` uniqueness before INSERT/UPDATE |
| Accidental Yandex block edit in header/footer | Surgical link-only diff; avoid Metrika/Webmaster lines |
| Contact form mail regression | No controller/template logic change unless required |
| Indexed `/contact` URLs | 301 + Search Console monitoring |
| Operator rejects slug migration | Charter documents rollback to keyword `contact` |

**No-go:** duplicate keyword conflict unresolved; header/footer authority ambiguous; native form mail flow broken.

---

## 12. Production mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| FTP writes | 0 |
| FTP reads/listings | 15 |
| FTP downloads | 15 |
| Admin saves | 0 |
| DB SELECTs | 7 |
| DB direct writes | 0 |
| Mail sends | 0 |
| Form submits | 0 |
| SMTP changes | 0 |
| Live code changes | 0 |
| Category/product changes | 0 |
| SEO URL changes | 0 |
| Redirect changes | 0 |
| Sitemap/robots/llms changes | 0 |
| Header/footer changes | 0 |
| Yandex changes | 0 |
| Cron/import runs | 0 |
| Monitor runs | 0 |
| Cache clears | 0 |
| Local cleanup/delete/move | 0 |
| public БЗПМ introduced | no |

---

## 13. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01\`

- `manifests/operation.json`
- `http-snapshots/` — 14 URL captures + status CSV/JSON/MD
- `sitemap/contacts-sitemap-analysis.*`
- `links-inventory/internal-contact-links.*`
- `db-readonly/information-pages.*`, `seo-url-records.*`, `contact-route-candidates.md`
- `ftp-source/source-map.*` + 15 downloaded sources
- `routing-analysis/contacts-routing-analysis.*`
- `implementation-charter/SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-CHARTER.*`
- `logs/final-summary.json`

---

## 14. Authority updates

Updated in-repo:

- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/OPERATIONAL-INDEX.md` — Run **4.237**
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/sites/site-002/tools/README.md`

**Checkpoint unchanged:** `SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01`

---

## 15. Git status

Selective commit planned for discovery docs + tool only. Storage and downloaded production sources **not** committed.

---

## 16. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| DB structure | **Resolved** — prefix `oc_`, seo_url id 846, no kontakty row |
| Contacts owner | **Resolved** — native `information/contact` |
| Sitemap auto-inclusion after SEO URL only | **Likely insufficient** — feed patch needed (confirmed in source) |
| External backlinks to `/kontakty` | **SAFE UNKNOWN** — not crawled beyond site HTML |
| Search Console indexed URL counts | **SAFE UNKNOWN** — operator data |

---

## 17. Final verdict

**SITE-002 CONTACTS URL ROUTING REVIEW COMPLETE — IMPLEMENTATION CHARTER READY**

---

## 18. Next task recommendation

**SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-01** — controlled production wave per implementation charter (Option E):

1. SEO URL keyword `contact` → `kontakty` for `information/contact`;
2. 301 `/contact` → `/kontakty`;
3. header/footer + corp inline link updates;
4. `google_sitemap.php` contact URL emission;
5. `llms.txt` URL update;
6. verification + rollback bundle.

Inherited pending (unchanged): post-1C Lari reparent verification (Run 4.235).

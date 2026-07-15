# SITE-002 — Info Page Hero / Corporate Intro Images Discovery 01

**Operation:** `SITE-002-PROD-INFO-PAGE-HERO-IMAGES-DISCOVERY-01`  
**Site:** SITE-002 · ЗПМ · `https://bzpm.ru/`  
**Historical TEST:** `https://zpm.new-site.space/`  
**Mode:** controlled read-only discovery  
**Date (UTC):** 2026-07-12  
**Production mutations:** **0**  
**Verdict:** **PARTIAL**

---

## 1. Scope

| Item | Value |
|------|--------|
| Primary URLs | `/custom-equipment`, `/payment-methods`, `/delivery`, `/dealers`, `/guarantee` |
| Related (documented, not expanded) | `/about` — same `.zpm-corp-intro` pattern |
| Goal | Find lost first-screen intro images; map source authority; prepare selective restore charter |
| Forbidden this run | FTP upload / overwrite / DB writes / admin saves / cache clear / template rollback wholesale |
| Pattern authority | TEST-era `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01` (2026-06-29) |

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume `X:` label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `dc3c17736c235f6b4c81f6ac6acecdea5a8a5f68` |
| Staged | empty (task scope) |
| Unpushed commits | present on branch (foreign to this task — not touched) |
| Foreign WIP | ignored |
| Secrets | Production FTP read from Storage secrets (RETR only) |

**STOP tokens:** none triggered for this read-only wave.

---

## 3. Target page inventory

| URL | Route | Live HTTP | Intro markup live? | Asset HTTP |
|-----|-------|-----------|--------------------|------------|
| `/custom-equipment` | `information/custom_equipment` | 200 | **yes** | 200 |
| `/payment-methods` | `information/payment` | 200 | **yes** | 200 |
| `/delivery` | `information/delivery` | 200 | **no** (text-only lead) | 200 (file exists, unused) |
| `/dealers` | `information/dealers` | 200 | **yes** | 200 |
| `/guarantee` | `information/guarantee` | 200 | **yes** | 200 |
| `/about` (related) | `information/about` | 200 | yes | 200 |

---

## 4. Current source authority

### Controllers (Production FTP RETR)

| Page | Remote controller | Role |
|------|-------------------|------|
| Custom | `/public_html/catalog/controller/information/custom_equipment.php` | `Pageintro` H1 + `$data['page_lead']` HTML |
| Payment | `.../payment.php` | same |
| Delivery | `.../delivery.php` | same |
| Dealers | `.../dealers.php` | same |
| Guarantee | `.../guarantee.php` | same |

Lead copy lives in **controller** as `$data['page_lead']`. H1/breadcrumb intro uses **Pageintro** (header), not the main media block.

### Twig (Production FTP RETR)

| Page | Remote twig |
|------|-------------|
| Custom | `/public_html/catalog/view/theme/default/template/information/custom_equipment.twig` |
| Payment | `.../payment.twig` |
| Delivery | `.../delivery.twig` |
| Dealers | `.../dealers.twig` |
| Guarantee | `.../guarantee.twig` |

### CSS

| Item | Evidence |
|------|----------|
| File | `/public_html/assets/css/style.css` |
| Marker | `SITE-002 — Corporate intro image blocks (zpm-corp-intro)` — **present on Production** |
| Classes | `.zpm-corp-intro__grid`, `__media`, `__body` — **present** |
| Layout | desktop `1fr 2fr` (image left / text right); ≤1024px stacked image above text |

### Current hero / introduction block location

Inside `<main>`, first section:

- **With image (4 pages):**  
  `section.zpm-corp-page-lead.zpm-corp-intro` → `.zpm-corp-intro__grid` → `__media` + `__body` containing rendered `page_lead`
- **Delivery only:**  
  `section.zpm-corp-page-lead` (no `zpm-corp-intro`) → `.container.zpm-corp-page-lead__body` → text only

---

## 5. Old hero image discovery results

### Pattern origin (TEST, 2026-06-28/29)

Documented in:

- [SITE-002-CORPORATE-INTRO-BLOCKS-01.md](SITE-002-CORPORATE-INTRO-BLOCKS-01.md)
- [SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01.md](../baselines/SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01.md)
- Knowledge Map §29
- Work pack: `reports/corporate-intro-blocks-work/`

Canonical path pattern:

`/assets/img/corporate/{page}-intro.jpg`

| Logical page | Filename | Alt (from historical twig) |
|--------------|----------|----------------------------|
| About | `about-intro.jpg` | (about intro block; hero stays `about-page-img.jpg`) |
| Delivery | `delivery-intro.jpg` | Подготовка оборудования к отправке |
| Payment | `payment-intro.jpg` | Согласование заказа и документов |
| Warranty | `warranty-intro.jpg` | Проверка оборудования сервисным инженером |
| Dealers | `dealers-intro.jpg` | Деловая встреча с партнёром |
| Custom | `custom-intro.jpg` | Проектирование оборудования на заказ |

### Local staging assets (repo)

`projects/ocpilot/sites/site-002/reports/corporate-intro-blocks-work/assets/img/corporate/`

| File | Bytes | SHA256 (trunc.) | Present |
|------|-------|-----------------|---------|
| `about-intro.jpg` | 1003429 | `0729c3a0…` | yes |
| `custom-intro.jpg` | 829576 | `1c1edc5f…` | yes |
| `dealers-intro.jpg` | 903056 | `90d58f0c…` | yes |
| `payment-intro.jpg` | 962586 | `c89bb396…` | yes |
| `warranty-intro.jpg` | 861186 | `9cba7c87…` | yes |
| `delivery-intro.jpg` | — | — | **missing** (never staged; operator upload on TEST closeout) |

All present local JPGs are **1672×941**.

### Production vs local hash truth

| Asset | Prod SHA | Local work | Notes |
|-------|----------|------------|-------|
| `about-intro.jpg` | `0729c3a0…` | MATCH | canonical |
| `custom-intro.jpg` | `1c1edc5f…` | MATCH | canonical |
| `dealers-intro.jpg` | `90d58f0c…` | MATCH | canonical |
| `warranty-intro.jpg` | `9cba7c87…` | MATCH | canonical |
| `payment-intro.jpg` | `85fd1d8d…` | **DIFF** | prod is newer/live authority |
| `delivery-intro.jpg` | `c89bb396…` | no local file | **byte-identical to local_work `payment-intro.jpg`** |

**Naming history (SAFE fact, not fantasy):** early local staging labeled a warehouse/shipping photo as `payment-intro.jpg`. That same byte payload is what now lives on Production/TEST as `delivery-intro.jpg`. Live `payment-intro.jpg` was later replaced with a different image (people + drawings). Visually, current prod `delivery-intro.jpg` **is delivery-appropriate** (crated stainless equipment, forklift, loading bay).

### TEST (`zpm.new-site.space`)

| Page | Intro markup | Asset |
|------|--------------|-------|
| 4 non-delivery targets | present | HTTP 200, hashes align with prod |
| `/delivery` | **absent** (same regression) | `delivery-intro.jpg` HTTP 200, same SHA as prod |

### Regression cause (documented)

`delivery-summary` restyle work (`reports/delivery-summary-work/…/delivery.twig`) used **text-only** lead. Subsequent Production captures (forms discovery/integration, contacts routing) show the same text-only lead. Corp-intro CSS remained; **markup was dropped for `/delivery` only**.

---

## 6. Per-page mapping table

| URL | Owner | Current markup | Old image found? | Path | Usage | Live state | Must change | Risk |
|-----|-------|----------------|------------------|------|-------|------------|-------------|------|
| `/custom-equipment` | `custom_equipment.php` + `.twig` | media+text grid | yes | `custom-intro.jpg` | left 1/3 | OK | none | low |
| `/payment-methods` | `payment.php` + `.twig` | media+text grid | yes (prod authority) | `payment-intro.jpg` | left 1/3 | OK | none | prod ≠ local_work hash |
| `/delivery` | `delivery.php` + `.twig` | **text-only lead** | file on prod (yes); unique local staging file (no) | `delivery-intro.jpg` | should be left 1/3 | **markup missing** | **selective twig restore** | asset OK visually; confirm operator visual OK |
| `/dealers` | `dealers.php` + `.twig` | media+text grid | yes | `dealers-intro.jpg` | left 1/3 | OK | none | low |
| `/guarantee` | `guarantee.php` + `.twig` | media+text grid | yes | `warranty-intro.jpg` | left 1/3 | OK | none | low |

JSON: Storage `…/mapping/per-page-mapping.json`

---

## 7. Current vs old layout diff

### Target pattern (historical + 4 live pages)

```html
<section class="zpm-corp-page-lead zpm-corp-intro" aria-label="Вводная информация">
  <div class="container">
    <div class="zpm-corp-intro__grid">
      <div class="zpm-corp-intro__media">
        <img src="/assets/img/corporate/{page}-intro.jpg" alt="…" loading="lazy" />
      </div>
      <div class="zpm-corp-intro__body zpm-corp-page-lead__body">
        {{ page_lead|raw }}
      </div>
    </div>
  </div>
</section>
```

### Current `/delivery` (Production)

```html
<section class="zpm-corp-page-lead" aria-label="Вводная информация">
  <div class="container zpm-corp-page-lead__body">
    {{ page_lead|raw }}
  </div>
</section>
```

### Diff conclusions

| Question | Answer |
|----------|--------|
| Image side | **Left** (not background, not right) |
| Wrapper needed | yes — `__grid` / `__media` / `__body` |
| CSS lost? | **No** — CSS block still in Production `style.css` |
| Can restore without breaking copy? | **Yes** — keep `{{ page_lead|raw }}` unchanged; controllers untouched |
| Adaptive | existing ≤1024px stack; no new CSS required if marker remains |
| Edit surface | **Twig only** for `/delivery` (CSS already present; asset already on disk) |

---

## 8. Implementation options

### Option A — Preferred (selective markup restore)

**When:** operator accepts current prod `delivery-intro.jpg` as canonical visual for `/delivery`.

| Item | Plan |
|------|------|
| Files to change | **1** — `delivery.twig` lead section only |
| Uploads | none required (asset already at `/assets/img/corporate/delivery-intro.jpg`) |
| CSS | none (already live) |
| Controllers / JS / forms | none |
| Responsive | reuse existing `.zpm-corp-intro` rules |
| Rollback | restore pre-change `delivery.twig` backup |

### Option B — Stop (missing authentic asset)

**When:** operator rejects current `delivery-intro.jpg` (historical payment-name collision / wants distinct original).

| Missing | Action |
|---------|--------|
| Authentic unique `delivery-intro.jpg` not in repo staging | Operator supplies file from Beget backup / original export |
| Stop | no Production mutation until asset approved |

### Option C — Review pack then stop

Prepare visual review of all 6 corporate intro JPGs (Storage `http/assets/` + `test-assets/`) before any restore. Recommended if operator believed **all** pages lost images (4/5 are already live).

**This discovery recommends: Option A after short Option C visual confirm on `/delivery` asset only.**

---

## 9. Recommended next operation

**`SITE-002-PROD-INFO-PAGE-HERO-IMAGES-RESTORE-01`**

Charter: Storage  
`…/implementation-plan/SITE-002-PROD-INFO-PAGE-HERO-IMAGES-RESTORE-01-CHARTER.md`

Primary work: selective `delivery.twig` lead → `.zpm-corp-intro` grid using existing `delivery-intro.jpg`.  
Do **not** wholesale-restore old corp templates. Do **not** regenerate images.

---

## 10. Production mutation summary

| Action | Count |
|--------|-------|
| FTP upload | 0 |
| FTP overwrite | 0 |
| DB write | 0 |
| Admin save | 0 |
| Cache clear | 0 |
| **Total mutations** | **0** |

FTP used: **RETR only** (5 controllers + 5 twig + `style.css`).

---

## 11. Storage artefacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-HERO-IMAGES-DISCOVERY-01\`

| Path | Content |
|------|---------|
| `source-readonly/` | FTP RETR controllers/twig/css |
| `http/pages/` | live HTML captures |
| `http/assets/` | prod intro JPGs |
| `test-assets/` | TEST intro JPGs |
| `mapping/per-page-mapping.json` | mapping table |
| `manifests/discovery-result.json` | full machine result |
| `logs/discovery.log` | run log |
| `implementation-plan/` | restore charter |

---

## 12. Changed files (local docs/tools)

| Path | Role |
|------|------|
| `projects/ocpilot/sites/site-002/tools/site-002-prod-info-page-hero-images-discovery-01.py` | read-only discovery tool |
| `projects/ocpilot/sites/site-002/reports/SITE-002-PROD-INFO-PAGE-HERO-IMAGES-DISCOVERY-01.md` | this report |
| `projects/ocpilot/sites/site-002/baselines/SITE-002-INFO-PAGE-HERO-IMAGES-DISCOVERY-01.md` | discovery baseline (not prod checkpoint) |

Git commit: **not required** this wave.

---

## 13. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact Beget backup copy of a *different* historical delivery photo | **SAFE UNKNOWN** — not found in current X: contour |
| Why local staging never contained `delivery-intro.jpg` | Documented as operator post-deploy upload on TEST; file not copied into repo pack |
| Whether operator wants to replace prod `delivery-intro.jpg` despite visual fitness | **Operator decision** |
| Whether 4 already-live pages need visual refresh | Out of restore scope unless operator expands charter |
| Unpushed commits on canonical branch | Foreign to this task — untouched |

**Blockers for Option A:** none technical — only operator approval of charter + visual OK on `delivery-intro.jpg`.

---

## 14. Final verdict

**PARTIAL**

- Discovery of pattern, paths, CSS, and 5-page authority: **COMPLETE**
- 4/5 target pages already restored/live with images: **COMPLETE**
- `/delivery` markup gap: **identified**
- Authentic uniquely named local staging file `delivery-intro.jpg`: **absent**, but Production already hosts a delivery-appropriate JPEG at the correct URL

**Next:** run restore charter `SITE-002-PROD-INFO-PAGE-HERO-IMAGES-RESTORE-01` after operator approval (Option A preferred).

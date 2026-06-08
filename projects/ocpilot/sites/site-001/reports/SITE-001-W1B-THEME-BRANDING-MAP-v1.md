# SITE-001 W1B Theme Branding Map v1

**Type:** W1B read-only theme discovery — **no site modifications performed**  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Active theme:** `auto` — `catalog/view/theme/auto/`  
**Discovery method:** FTP read-only full-tree scan + key-template line verification + storefront HTTP spot-check (post-W1A)  
**Companion:** [SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md](SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md)

**Explicit exclusions observed:** No admin writes; no theme edits; no logo uploads; no contact value changes.

---

## Executive summary

Post-**W1A** storefront meta on homepage reflects **СИБКАР** (admin `config_meta_*`), but **theme `auto` still hardcodes legacy brand and contacts** in header, footer, homepage body, about/contact templates, and product review blocks.

| Metric | Value |
|--------|-------|
| Theme files total | **135** |
| Text files scanned | **125** |
| Binary / skipped | **10** (theme `image/*.png` payment icons) |
| Pattern hits (raw scan) | **129** |
| **Visible W1B execution targets** | **7 primary twig/html files** + **3 secondary product templates** |
| Email in theme | **0** — no `mailto:` or hardcoded email in `catalog/view/theme/auto/` |
| SIBCAR / СИБКАР in theme | **0** — target strings not yet present in theme files |

**Primary execution surface:** `header.twig`, `footer.twig`, `home.twig`, `contact.twig`, `about.twig`, `header_cup.html`, `header_cup_home.html`.

---

## 1. Scan inventory

### 1.1 Method

| Step | Detail |
|------|--------|
| Access | FTP read-only to TEST web root (`polygonws.beget.tech`, chroot = site `public_html`) |
| Root path | `/` (FTP login lands at OpenCart root; not `/sibcar.new-site.space/public_html/`) |
| Theme tree | `/catalog/view/theme/auto/` — recursive LIST + RETR |
| Extensions scanned | `.twig`, `.html`, `.tpl`, `.php`, `.css`, `.js`, `.json`, `.xml`, `.txt`, `.scss`, `.less` |
| Brand search terms | `Хмельницкий`, `АЦ Хмельницкий`, `Автоцентр Хмельницкий`, `ООО АЦ Хмельницкий`, `SIBCAR`, `СИБКАР` |
| Contact search terms | `phone`, `telephone`, `tel:`, `wa.me`, `whatsapp`, `email`, `mailto` |
| Evidence artefact | `.recovery-temp/site-001-w1b-theme-scan.json` (local; not in git) |

### 1.2 Files with legacy brand or contact hits (ranked)

| File | Hits | W1B role |
|------|------|----------|
| `template/common/header.twig` | 28 | **Primary** — header branding, phone, WhatsApp, logo alt |
| `template/common/footer.twig` | 20 | **Primary** — footer branding, copyright, phone, WhatsApp, logo alt |
| `template/information/contact.twig` | 14 | **Primary** — H1, legal line, phone, WhatsApp |
| `template/common/home.twig` | 6 | **Primary** — homepage H1 + body brand |
| `template/information/about.twig` | 7 | **Primary** — about body brand |
| `template/common/header_cup.html` | 1 | **Primary** — cup banner brand label |
| `template/common/header_cup_home.html` | 1 | **Primary** — cup banner brand label |
| `template/product/category_backup.twig` | 10 | **Secondary** — hardcoded review quotes |
| `template/product/product.twig` | 8 | **Secondary** — telephone form keys only |
| `template/product/productnew.twig` | 6 | **Secondary** — breadcrumb suffix brand |
| `template/product/productnew_Backup.twig` | 2 | **Secondary** — backup template |
| Account/checkout/mail twigs | 60+ `telephone` keys | **Out of W1B visible scope** — OC form field labels |

### 1.3 Post-W1A storefront verification (HTTP read-only)

| Surface | W1A result | Theme layer (W1B) |
|---------|--------------|-------------------|
| Homepage `<title>` / meta | **СИБКАР** | N/A (admin) |
| Homepage H1 | **АЦ Хмельницкий** | `home.twig` L31 |
| Header phone | `+7 (383) 388-55-23` | `header.twig` |
| Footer copyright | `© … АЦ Хмельницкий` | `footer.twig` L111 |
| Logo alt | `АЦ Хмельницкий` | `header.twig`, `footer.twig` |

---

## 2. Grouped findings

### W1B-A — Header branding

| ID | File | Line | Type | Current value | Replacement scope | Target (per W1 pack) |
|----|------|------|------|---------------|-------------------|----------------------|
| W1B-A-01 | `template/common/header.twig` | 96 | Address (geographic) | `Новосибирск, ул. Богдана Хмельницкого 101` | **Policy** — street name not brand; operator address decision | LE-0005 legal or retain showroom |
| W1B-A-02 | `template/common/header.twig` | 219 | Address (duplicate block) | Same as W1B-A-01 | Same | Same |
| W1B-A-03 | `template/common/header.twig` | 238 | Address (mobile block) | Same as W1B-A-01 | Same | Same |
| W1B-A-04 | `template/common/header_cup.html` | 20 | Visible brand label | `<h3>Хмельницкий</h3>` | W1B text replace | `СИБКАР` |
| W1B-A-05 | `template/common/header_cup_home.html` | 20 | Visible brand label | `<h3>Хмельницкий</h3>` | W1B text replace | `СИБКАР` |

**Note:** Header logo **image paths** (`img/logo.svg`, `img/logo_white.svg`) carry legacy artwork — file swap is **W1D**; alt-text swap is **W1B-F**.

---

### W1B-B — Footer branding

| ID | File | Line | Type | Current value | Replacement scope | Target (per W1 pack) |
|----|------|------|------|---------------|-------------------|----------------------|
| W1B-B-01 | `template/common/footer.twig` | 81 | Legal entity line | `ООО «АЦ Хмельницкий»` | W1B text replace | `ООО «СибКар»` |
| W1B-B-02 | `template/common/footer.twig` | 111 | Copyright | `2025 © ООО «АЦ Хмельницкий»` | W1B text replace | `© … СИБКАР` / `ООО «СибКар»` per operator style |

---

### W1B-C — Phones

| ID | File | Line | Type | Current value | Replacement scope | Target (per W1 pack) |
|----|------|------|------|---------------|-------------------|----------------------|
| W1B-C-01 | `template/common/header.twig` | 140 | `tel:` link | `href="tel:+73833885523"` | W1B contact replace | `+70000000000` `[DEMO]` |
| W1B-C-02 | `template/common/header.twig` | 143 | Display phone | `+7 (383) 388-55-23` | W1B contact replace | `+7 (000) 000-00-00` `[DEMO]` |
| W1B-C-03 | `template/common/header.twig` | 250 | `tel:` link (scroll header) | `tel:+73833885523` | W1B | Demo normalized |
| W1B-C-04 | `template/common/header.twig` | 253 | Display phone (scroll) | `+7 (383) 388-55-23` | W1B | Demo display |
| W1B-C-05 | `template/common/header.twig` | 315 | `tel:` link (mobile menu) | `tel:+73833885523` | W1B | Demo normalized |
| W1B-C-06 | `template/common/header.twig` | 318 | Display phone (mobile) | `+7 (383) 388-55-23` | W1B | Demo display |
| W1B-C-07 | `template/common/footer.twig` | 15 | `tel:` link | `tel:+73833885523` | W1B | Demo normalized |
| W1B-C-08 | `template/common/footer.twig` | 18 | Display phone | `+7 (383) 388-55-23` | W1B | Demo display |
| W1B-C-09 | `template/information/contact.twig` | 45 | `tel:` link | `tel:+73833885523` | W1B | Demo normalized |
| W1B-C-10 | `template/information/contact.twig` | 49 | Display phone | `+7 (383) 388-55-23` | W1B | Demo display |

**Admin mismatch (documented):** `config_telephone` = `+73833886890` (unchanged in W1A) ≠ theme `+73833885523`. W1B should align visible theme phone with operator-approved target; optional admin `config_telephone` sync is separate decision.

---

### W1B-D — WhatsApp

| ID | File | Line | Type | Current value | Replacement scope | Target (per W1 pack) |
|----|------|------|------|---------------|-------------------|----------------------|
| W1B-D-01 | `template/common/header.twig` | 130 | WhatsApp URL | `https://wa.me/79539979910` | W1B — **blocked on C-04** | `[HOLD]` or operator URL |
| W1B-D-02 | `template/common/header.twig` | 167 | WhatsApp URL (duplicate) | Same | W1B — C-04 | `[HOLD]` |
| W1B-D-03 | `template/common/header.twig` | 240 | WhatsApp URL (scroll header) | Same | W1B — C-04 | `[HOLD]` |
| W1B-D-04 | `template/common/header.twig` | 305 | WhatsApp URL (mobile) | Same | W1B — C-04 | `[HOLD]` |
| W1B-D-05 | `template/common/footer.twig` | 26 | WhatsApp URL | Same | W1B — C-04 | `[HOLD]` |
| W1B-D-06 | `template/information/contact.twig` | 101 | WhatsApp URL | Same | W1B — C-04 | `[HOLD]` |

**Note:** WhatsApp number `79539979910` differs from main storefront phone `73833885523`.

---

### W1B-E — Email

| Finding | Detail |
|---------|--------|
| Theme email occurrences | **NONE** in `catalog/view/theme/auto/` |
| `mailto:` links | **0** |
| Hardcoded `@domain` strings | **0** in scanned theme text files |
| Store email source | Admin `config_email` (`demo@sibcar.local` after W1A) — used by `contact.php` controller, **not theme** |
| Contact page email display | **Not rendered** in `contact.twig` sampled markup |

**W1B-E verdict:** No theme email replacements required. Email visibility changes belong to **W1C** (controllers) or future operator decision.

---

### W1B-F — Logo alt / title attributes

| ID | File | Line | Type | Current value | Replacement scope | Target (per W1 pack) |
|----|------|------|------|---------------|-------------------|----------------------|
| W1B-F-01 | `template/common/header.twig` | 107 | Logo `alt` | `alt="АЦ Хмельницкий"` (white logo) | W1B text replace | `alt="СИБКАР"` |
| W1B-F-02 | `template/common/header.twig` | 230 | Logo `alt` | `alt="АЦ Хмельницкий"` (color logo) | W1B text replace | `alt="СИБКАР"` |
| W1B-F-03 | `template/common/footer.twig` | 8 | Logo `alt` | `alt="АЦ Хмельницкий"` | W1B text replace | `alt="СИБКАР"` |
| W1B-F-04 | `template/common/header.twig` | 130 | Link `title` | `title="Написать в WhatsApp"` | **Not logo** — messenger UI; retain or localize | — |
| W1B-F-05 | `template/information/contact.twig` | 45 | Link `title` | `title="Позвонить"` | **Not logo** — phone UI | — |

**Logo file dependency:** SVG/PNG artwork replacement is **W1D** (C-03). W1B-F updates **alt text only** — can execute without new logo files.

---

## 3. Additional W1B theme body content (execution pack scope)

Not in taxonomy W1B-A..F but **in W1B execution scope** per [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) §3.2:

| ID | File | Line | Current value | Target |
|----|------|------|---------------|--------|
| W1B-X-01 | `template/common/home.twig` | 31 | H1: `АЦ Хмельницкий — авто с пробегом…` | `СИБКАР` |
| W1B-X-02 | `template/common/home.twig` | 259 | Body: `Автосалон «Хмельницкий»…` | `Автосалон «СИБКАР»` |
| W1B-X-03 | `template/information/contact.twig` | 21 | H1: `Контакты «АЦ Хмельницкий»` | `СИБКАР` |
| W1B-X-04 | `template/information/contact.twig` | 55 | Legal: `ООО «АЦ Хмельницкий»` | `ООО «СибКар»` |
| W1B-X-05 | `template/information/about.twig` | 24 | Body intro `«АЦ Хмельницкий»` | `СИБКАР` |
| W1B-X-06 | `template/information/about.twig` | 33 | H2 `«АЦ Хмельницкий»` | `СИБКАР` |
| W1B-X-07 | `template/information/about.twig` | 38 | Body `«АЦ Хмельницкий»` | `СИБКАР` |

**W1C overlap:** Custom controller meta (`about.php`, `contact.php` titles/descriptions) remains **W1C** — theme twig edits alone will not fix `<title>` on `/contact/`.

---

## 4. Secondary / deferred surfaces

| Surface | Finding | Wave |
|---------|---------|------|
| `product/category_backup.twig` | Hardcoded review quotes mention `АЦ Хмельницкий` (×5 slides) | W1B optional or W1F QA |
| `product/productnew.twig` | Breadcrumb suffix `в Хмельницкий` | W1B optional |
| Account/checkout twigs | `telephone` form field labels only — not legacy brand | **Out of scope** |
| `system/storage/modification/` | Not scanned | W6 / post-change grep |
| Theme `stylesheet.css` | No brand strings | — |

---

## 5. Replacement map (action table)

| Group | Occurrences | Files | Replace with | Wave | Risk |
|-------|-------------|-------|--------------|------|------|
| W1B-A Header branding | 5 address + 2 cup labels | `header.twig`, `header_cup*.html` | `СИБКАР`; address per operator | W1B | **Medium** (address policy) |
| W1B-B Footer branding | 2 | `footer.twig` | `ООО «СибКар»`, copyright `СИБКАР` | W1B | **High** (legal line) |
| W1B-C Phones | 10 | `header.twig`, `footer.twig`, `contact.twig` | Demo phone `[DEMO]` | W1B | **High** |
| W1B-D WhatsApp | 6 URLs | `header.twig`, `footer.twig`, `contact.twig` | **C-04 HOLD** | W1B | **High** |
| W1B-E Email | 0 | — | N/A | — | **Low** |
| W1B-F Logo alt | 3 | `header.twig`, `footer.twig` | `alt="СИБКАР"` | W1B | **Medium** |
| W1B-X Body/H1 | 7 | `home.twig`, `about.twig`, `contact.twig` | `СИБКАР` / `ООО «СибКар»` | W1B | **High** |

---

## 6. Estimated files affected (W1B execution)

| Tier | Count | Files |
|------|-------|-------|
| **Must edit** | **7** | `header.twig`, `footer.twig`, `home.twig`, `contact.twig`, `about.twig`, `header_cup.html`, `header_cup_home.html` |
| **Optional / QA** | **3** | `category_backup.twig`, `productnew.twig`, `productnew_Backup.twig` |
| **No edit expected** | **118** | Remaining theme files (no visible legacy brand) |

**Estimated FTP writes:** 7–10 files. **Cache clear required** after edit (oc3x_storage_cleaner per W1A precedent).

---

## 7. Risk assessment

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R-W1B-01 | Partial rebrand — W1A meta updated but theme/header/footer still legacy | **Expected** | W1B scoped edit + post-change HTTP verify |
| R-W1B-02 | Phone admin vs theme mismatch persists if only theme edited | **Medium** | Sync `config_telephone` in same session or document delta |
| R-W1B-03 | WhatsApp C-04 unresolved — link may remain legacy or be removed | **High** | Operator decision before editing W1B-D rows |
| R-W1B-04 | Address `ул. Богдана Хмельницкого` conflated with brand | **Medium** | Apply geographic exception per execution pack §1.1 |
| R-W1B-05 | Logo SVG still shows legacy artwork after alt-text change | **Low** until W1D | W1B-F is accessibility text; W1D replaces assets |
| R-W1B-06 | Modification cache serves stale twig | **Medium** | Clear system + modification cache (W1A method) |
| R-W1B-07 | Contact/about `<title>` meta unchanged after twig-only edit | **Medium** | Plan **W1C** for controller meta |
| R-W1B-08 | Product template review quotes remain legacy | **Low** | Optional in W1B or catch in W1F grep |

---

## 8. Related documents

| Document | Role |
|----------|------|
| [SITE-001-W0.5-ADMIN-DISCOVERY-v1.md](SITE-001-W0.5-ADMIN-DISCOVERY-v1.md) | Prior theme inventory (pre-W1A) |
| [SITE-001-W1A-EXECUTION-v1.md](SITE-001-W1A-EXECUTION-v1.md) | W1A complete; footer/header legacy confirmed |
| [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) | W1B target map and demo contacts |
| [SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md](SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md) | Execution authorization gate |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — W1B read-only theme branding map; FTP scan 135 files |

*SITE-001 W1B Theme Branding Map v1 — discovery only; no site modifications.*

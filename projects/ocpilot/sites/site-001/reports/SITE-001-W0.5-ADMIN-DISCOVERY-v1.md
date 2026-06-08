# SITE-001 W0.5 Admin Discovery v1

**Type:** W0.5 read-only admin-level discovery — **no site modifications performed**  
**Date:** 2026-06-07  
**Site:** SITE-001 — Автосалон СИБКАР (Phase 1 target)  
**Environment:** **TEST** — `https://sibcar.new-site.space/`  
**Admin URL:** `https://sibcar.new-site.space/admin/`  
**Platform:** ocStore / OpenCart **3.0.3.8 (rs.2)**  
**Discovery methods:** OpenCart admin (read-only HTML inspection), FTP read-only (theme/controllers/assets), public HTTP verification (About/Contact)  
**Companion:** [SITE-001-BRAND-REPLACEMENT-MAP-v1.md](SITE-001-BRAND-REPLACEMENT-MAP-v1.md) (W0 public crawl)

**Explicit exclusions observed:** No admin writes; no DB writes; no FTP uploads; no cache clear; no content/settings edits; no backups created. Remote MySQL from workstation **blocked** (Beget localhost-only).

---

## Executive summary

W0.5 admin discovery **confirms** all primary `config_*` store settings, active theme **`auto`**, admin `config_logo` path, and a consolidated legacy-brand inventory. W0 **SAFE UNKNOWN** gaps for admin store keys, theme name, and `config_logo` are **closed**.

**Key operational finding:** `config_telephone` in admin (`+73833886890`) **does not match** the phone hardcoded in theme templates and storefront (`+73833885523`). W1 store-settings replacement alone will **not** update visible header/footer/contact phone without a follow-on template wave.

**Decision:** **AUTHORIZED WITH NOTES** — W1 Store Settings Replacement **discovery prerequisites are satisfied**; execution still requires operator write charter, fresh backup, and Brand Replacement Pack per [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md).

---

## Section A — Confirmed Store Settings

**Source:** Admin → System → Settings → Edit store (store_id **0**), read-only inspection 2026-06-07.  
**Multi-store:** Admin store list shows **only store_id 0** (single store).

| Key | Confirmed value | Legacy brand present? | Notes |
|-----|-----------------|----------------------|-------|
| `config_name` | `АЦ Хмельницкий` | **YES** — `АЦ Хмельницкий` | |
| `config_owner` | `ООО «АЦ Хмельницкий»` | **YES** — `АЦ Хмельницкий` | Legal entity line |
| `config_address` | `Новосибирск, улица Богдана Хмельницкого, 101` | **Partial** — street name `Хмельницкого` (geographic, not brand) | |
| `config_email` | `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | **YES** — legacy punycode domain | Maps to legacy `.рф` production domain |
| `config_telephone` | `+73833886890` | **NO** brand string | **Differs from storefront** — see Section D |
| `config_meta_title` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| АЦ Хмельницкий` | **YES** — `АЦ Хмельницкий` | |
| `config_meta_description` | `Автоцентр Хмельницкий в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` | **YES** — `Автоцентр Хмельницкий` | |
| `config_meta_keyword` | `АЦ Хмельницкий, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` | **YES** — `АЦ Хмельницкий` | |
| `config_logo` | `catalog/logo_balck.png` | **NO** in path string | Typo filename `balck`; see Section C |
| `config_icon` | `catalog/favicon-16-black.png` | **NO** | OC admin favicon setting |
| `config_theme` | `auto` | **NO** | Confirmed via admin theme selector |
| `config_fax` | *(empty)* | — | |
| `config_open` | *(empty)* | — | Hours appear hardcoded in theme, not admin |
| `config_comment` | *(empty)* | — | |

### Additional mail-related settings (admin, store_id 0)

| Key | Confirmed value | Legacy brand present? |
|-----|-----------------|----------------------|
| `config_mail_smtp_hostname` | `ssl://smtp.beget.com` | NO |
| `config_mail_smtp_username` | `send@ац-хмельницкий.рф` | **YES** — `АЦ`, `Хмельницкий` (Cyrillic domain) |
| `config_mail_smtp_port` | `465` | NO |
| `config_mail_alert_email` | *(empty)* | — |
| `config_image` | `catalog/no_image.png` | NO — contact map placeholder |

**Brand-bearing `config_*` keys (summary):** `config_name`, `config_owner`, `config_meta_title`, `config_meta_description`, `config_meta_keyword`, `config_email` (legacy domain), `config_mail_smtp_username`.

---

## Section B — Theme Inventory

| Item | Finding | Evidence |
|------|---------|----------|
| **Active OC theme** | **`auto`** | Admin `config_theme` selector; `oc_setting` equivalent |
| **Theme filesystem path** | `catalog/view/theme/auto/` | FTP listing |
| **Alternate theme present** | `default` (not active) | FTP `catalog/view/theme/` |
| **Template engine** | Twig + custom HTML partials | `template/common/*.twig`, `header_cup*.html` |
| **Public asset root (custom)** | `/css/`, `/img/`, `/favicon/`, `/libs/` | FTP web root; not under theme folder |
| **Theme overrides / customizations** | **Yes — extensive** | Custom controllers `catalog/controller/information/about.php`, `contact.php`; custom twig `template/information/about.twig`, `contact.twig`; hardcoded phones/logos in `header.twig`, `footer.twig`, `home.twig` |
| **Modification cache** | **SAFE UNKNOWN** (not inspected) | `system/storage/modification/` — not opened in W0.5 |

### Theme `auto` — notable template files

| Path | Role |
|------|------|
| `catalog/view/theme/auto/template/common/header.twig` | Header logos, phone, WhatsApp |
| `catalog/view/theme/auto/template/common/footer.twig` | Footer logo, phone, WhatsApp, copyright brand |
| `catalog/view/theme/auto/template/common/home.twig` | Homepage H1 and body copy |
| `catalog/view/theme/auto/template/information/about.twig` | About page body |
| `catalog/view/theme/auto/template/information/contact.twig` | Contact page H1, phone, legal line |
| `catalog/view/theme/auto/template/common/header_cup*.html` | Variant header partials |

---

## Section C — Logo Inventory

### Admin `config_logo`

| Field | Value |
|-------|-------|
| **Admin key** | `config_logo` |
| **Stored path (OC-relative)** | `catalog/logo_balck.png` |
| **Full server path** | `image/catalog/logo_balck.png` |
| **Public URL** | `https://sibcar.new-site.space/image/catalog/logo_balck.png` |
| **Admin thumbnail** | `image/cache/catalog/logo_balck-100x100.png` |

### Storefront logo files (theme — primary visible logos)

| File | Server path | Public URL | Referenced in |
|------|-------------|------------|---------------|
| `logo.svg` | `img/logo.svg` | `/img/logo.svg` | `header.twig` (scroll header) |
| `logo_white.svg` | `img/logo_white.svg` | `/img/logo_white.svg` | `header.twig`, `footer.twig` |
| `logo - hmel.svg` | `img/logo - hmel.svg` | `/img/logo%20-%20hmel.svg` | **Legacy asset on disk** — not referenced in sampled templates |
| `logo_balck.png` | `image/catalog/logo_balck.png` | `/image/catalog/logo_balck.png` | **Admin `config_logo` only** — not used in sampled header/footer |
| `logo.png` | `image/catalog/logo.png` | `/image/catalog/logo.png` | OC default orphan (W0) |
| `vin_logo.svg` | `img/vin_logo.svg` | `/img/vin_logo.svg` | VIN-related UI (not primary brand logo) |

### Favicon set

| Path | Notes |
|------|-------|
| `favicon/favicon.svg` + PNG sizes | Web root `/favicon/*` — used in HTML `<link rel="icon">` |
| `config_icon` → `catalog/favicon-16-black.png` | Admin setting under `image/catalog/` |

### Logo reference summary

| Reference location | Asset used | Alt text / brand |
|--------------------|--------------|------------------|
| `header.twig` | `img/logo_white.svg`, `img/logo.svg` | `alt="АЦ Хмельницкий"` |
| `footer.twig` | `/img/logo_white.svg` | `alt="АЦ Хмельницкий"` |
| Admin OC setting | `catalog/logo_balck.png` | — |
| Copyright footer | Text | `© … АЦ Хмельницкий` (footer.twig) |

**SVG embedded text:** Direct HTTP fetch of `/img/logo.svg` returned **HTTP 500** in W0 — SVG path text content remains **SAFE UNKNOWN** until W3 asset review or FTP binary inspection.

---

## Section D — Admin Contact Inventory

Values below are **admin-configured** unless noted as **template-hardcoded**.

| Contact type | Admin / configured value | Legacy brand? | Display on storefront |
|--------------|-------------------------|---------------|----------------------|
| **Primary telephone** | `config_telephone`: `+73833886890` | NO | **Template-hardcoded** `+7 (383) 388-55-23` / `tel:+73833885523` in header, footer, contact twig — **not from admin** |
| **Fax** | *(empty)* | — | Not shown |
| **Email (store)** | `config_email`: `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | Legacy domain | Not visible on public contact page body; used as mail `setTo` in `contact.php` |
| **SMTP username** | `send@ац-хмельницкий.рф` | **YES** | Outbound mail identity |
| **Physical address** | `config_address`: `Новосибирск, улица Богдана Хмельницкого, 101` | Street name only | Header/footer/contacts via `config_address` on contact page + templates |
| **Business hours** | `config_open`: *(empty)* | — | **Template-hardcoded** `Ежедневно c 9:00-21:00` (W0) |
| **WhatsApp** | **Not in admin** | — | **Template-hardcoded** `https://wa.me/79539979910` |
| **Telegram / Viber / VK** | **Not configured** | — | Not found |
| **Contact form recipient** | `config_email` (above) | Legacy domain | Form POST handler in `contact.php` |

**Critical note for W1:** Replacing `config_telephone` alone will update `contact.php` `$data['telephone']` but **will not** change header/footer/contact twig hardcoded `388-55-23` — requires **W2/template** work.

---

## Section E — Legacy Brand Inventory

### E.1 — Admin `config_*` and mail settings

| Location | Strings found |
|----------|---------------|
| `config_name` | `АЦ Хмельницкий` |
| `config_owner` | `ООО «АЦ Хмельницкий»` |
| `config_meta_title` | `АЦ Хмельницкий` |
| `config_meta_description` | `Автоцентр Хмельницкий` |
| `config_meta_keyword` | `АЦ Хмельницкий` |
| `config_email` | `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` (legacy punycode) |
| `config_mail_smtp_username` | `send@ац-хмельницкий.рф` |

### E.2 — Information pages (admin → Catalog → Information)

| ID | Title | SEO URL | Brand refs? | Terms detected |
|----|-------|---------|-------------|----------------|
| 9 | Автокредит | `autocredit` | **YES** | Хмельницкий, АЦ, Автосалон |
| 10 | Трейдин | `tradein` | **YES** | Хмельницкий, АЦ, Автосалон |
| 16 | Условия автокредитования | `loan-terms` | **YES** | Хмельницкий, АЦ, Автосалон |
| 13 | Политика конфиденциальности | `privacy-policy` | **YES** | Хмельницкий, АЦ, Автосалон |
| 5 | Пользовательское соглашение | `user-agreement` | **YES** | Хмельницкий, АЦ, Автосалон |
| 3 | Политика Cookie файлов | `cookie-files-policy` | **YES** | Хмельницкий, АЦ, Автосалон |
| 8 | Акции | `promos` | **YES** | Хмельницкий, АЦ, Автосалон |
| 12 | Выкуп авто | `carbuyback` | **YES** | Хмельницкий, АЦ, Автосалон |
| 11 | Рассрочка | `instalment` | **YES** | Хмельницкий, АЦ, Автосалон |
| 7 | Отзывы | `reviews` | **YES** | Хмельницкий, АЦ, Автосалон |
| 6 | Доставка | `delivery` | **NO** | — |
| 4 | О нас | `about_us` | **NO** in admin content | W0: orphan title «Вавилон» on storefront — verify at W2 |
| 16 | OpenCart | *(system)* | N/A | Default OC page |

### E.3 — Custom controllers (not in Information admin UI)

| Page | Route / SEO | Source file | Brand refs? |
|------|-------------|-------------|-------------|
| **About** | `/about` → `information/about` | `catalog/controller/information/about.php` + `about.twig` | **YES** — title, description, keywords, body |
| **Contacts** | `/contact/` → `information/contact` | `catalog/controller/information/contact.php` + `contact.twig` | **YES** — title, description, keywords, H1, legal line |

### E.4 — Theme templates (sampled)

| File | Brand strings |
|------|---------------|
| `header.twig` | `alt="АЦ Хмельницкий"` on logos |
| `footer.twig` | `ООО «АЦ Хмельницкий»`, `© … АЦ Хмельницкий` |
| `home.twig` | H1 `АЦ Хмельницкий`, body `Хмельницкий` |
| `contact.twig` | H1 `АЦ Хмельницкий`, `ООО «АЦ Хмельницкий»` |
| `about.twig` | Multiple `АЦ Хмельницкий` / `Хмельницкий` in body |

### E.5 — Consolidated variant list

| Variant | Contexts found |
|---------|----------------|
| `Хмельницкий` | Meta, pages, templates, SMTP domain |
| `хмельницкий` | Keywords, privacy/autocredit body |
| `АЦ Хмельницкий` | Primary short brand — config, meta, titles, H1, alt text |
| `АЦ «Хмельницкий»` | Loan-terms / legal phrasing (W0 + information pages) |
| `Автоцентр Хмельницкий` | `config_meta_description`, keywords |
| `ООО «АЦ Хмельницкий»` | `config_owner`, footer, contact twig |
| `Автосалон «Хмельницкий»` | Privacy / information body (W0) |
| `ац Хмельницкий` | Keywords (lowercase «ац») |
| `ул. Богдана Хмельницкого` / `Хмельницкого` | Address — **geographic**; policy decision required |
| `send@ац-хмельницкий.рф` | SMTP username |
| `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | `config_email` |
| `logo - hmel.svg` | Legacy filename on disk |
| `Вавилон` | `/about_us` orphan (W0) — unrelated legacy title |

**Not found** in admin + sampled templates: Latin `Hmelnickiy`, `ac-hmelnickiy`, `Khmelnitskiy`.

---

## Section F — SAFE UNKNOWN Remaining

| Topic | Status after W0.5 | Severity for W1 discovery | Verification path |
|-------|-------------------|---------------------------|-------------------|
| `oc_setting` full SQL inventory | **PARTIAL** — main `config_*` confirmed via admin; remote SQL **denied** | Low for W1 store keys | SSH localhost MySQL or phpMyAdmin read-only export |
| Extension-specific `oc_setting` keys | **NOT INVENTORIED** | Medium — W5 scope | Admin extensions + SQL grep |
| **Canonical phone number** | **UNRESOLVED** — admin `86890` vs template `85523` | **High** — operator must pick target before W1/W2 | Operator Brand Replacement Pack |
| Logo SVG embedded paths/text | **NOT READ** | Low — W3 scope | FTP download / W3 asset review |
| `system/storage/modification/` cached strings | **NOT SCANNED** | Medium — post-change W6 | FTP read-only grep |
| Product/category descriptions brand density | **NOT SAMPLED** | Low for W1 | Catalog grep W4+ |
| Callibri / SmartWidgets injected brand | **NOT INSPECTED** | Medium | Extension admin or runtime DOM |
| Backup restorability | **NOT VERIFIED** | High for **execution**, not discovery | Operator Beget restore drill |
| Write charter on access brief | **NO** | High for **execution** | Operator update brief |
| Brand Replacement Pack v1 approved | **NOT SATISFIED** | High for **execution** | Operator sign-off |

### W0 gaps closed by W0.5

| W0 gap | W0.5 status |
|--------|-------------|
| `oc_setting` exact `config_*` values | **CLOSED** (admin-confirmed) |
| Active theme directory name | **CLOSED** → `auto` |
| `config_logo` / `config_icon` admin paths | **CLOSED** |
| Admin store name vs storefront | **CLOSED** — consistent legacy brand |
| Delivery information page | **CLOSED** — exists (ID 6, `delivery`, no brand in admin content) |

---

## Final Decision — Can W1 Store Settings Replacement begin?

### Outcome: **AUTHORIZED WITH NOTES**

| Criterion | Status |
|-----------|--------|
| `config_*` values confirmed in admin | **PASS** |
| Active theme identified | **PASS** — `auto` |
| Logo path identified | **PASS** — admin + storefront refs catalogued |
| Legacy brand inventory exists | **PASS** |
| No critical SAFE UNKNOWN for **discovery** | **PASS WITH NOTES** — phone canonical source unresolved; extension `oc_setting` partial |

### Notes (required before / during W1 execution)

1. **Phone mismatch:** Admin `config_telephone` ≠ theme-hardcoded display phone — W1 must be paired with operator decision and W2 template updates for visible phone/WhatsApp.
2. **Mail identity:** `config_email` and `config_mail_smtp_username` carry legacy domains — include in W1 scope or separate mail wave.
3. **About/Contact** are **custom PHP/twig**, not Information-module pages — meta in controllers will **not** change via Information admin alone (W2+).
4. **Execution gates unchanged:** write charter **NO**, fresh backup not recorded, Change Request not bound — see [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) §6 (C-01..C-11).

**W1 store-settings replacement discovery is complete.** Supervised W1 **execution** may proceed once operator closes execution gates and approves target phone/mail strings.

---

## Related documents

| Document | Role |
|----------|------|
| [SITE-001-BRAND-REPLACEMENT-MAP-v1.md](SITE-001-BRAND-REPLACEMENT-MAP-v1.md) | W0 public-layer map |
| [SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) | Prior gate — execution NOT AUTHORIZED |
| [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) | W0–W7 wave plan |
| [project-access-brief.md](../project-access-brief.md) | Permissions |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-07 | **CREATED** — W0.5 read-only admin discovery; decision **AUTHORIZED WITH NOTES** |

*SITE-001 W0.5 Admin Discovery v1 — discovery only; no site modifications.*

# SITE-001 W1 Execution Pack v1

**Type:** Phase 1 Brand Replacement — **planning and execution specification only**  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST** — `https://sibcar.new-site.space/`  
**Platform:** ocStore / OpenCart **3.0.3.8 (rs.2)** · active theme **`auto`**  
**Phase:** W1 — Brand Replacement (Hmelnickiy → SIBCAR / СИБКАР)

**Explicit exclusions:** No site modifications performed in authoring this pack. No FTP uploads. No admin writes. No logo uploads. No TEST environment changes.

**Inputs:**

| Document | Role |
|----------|------|
| [SITE-001-BRAND-REPLACEMENT-MAP-v1.md](SITE-001-BRAND-REPLACEMENT-MAP-v1.md) | W0 public-layer discovery |
| [SITE-001-W0.5-ADMIN-DISCOVERY-v1.md](SITE-001-W0.5-ADMIN-DISCOVERY-v1.md) | Admin-confirmed `config_*`, theme, contacts |
| [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) | Gate checklist C-01..C-11 |
| [ATLAS-OCPILOT-SNAPSHOT-v1.md](../../../atlas/audit/ATLAS-OCPILOT-SNAPSHOT-v1.md) | ATLAS ↔ OCPilot crosswalk |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](../../../atlas/population/ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | LE-0005 legal source (EV-W1C-CC-01) |

**Operator decisions (this pack):**

| Parameter | Value |
|-----------|-------|
| Display brand | **СИБКАР** |
| Secondary / Latin | **SIBCAR** |
| Legal entity source | **ATLAS LE-0005** (attested AT-W1C-01) |
| Contacts (Phase 1 TEST) | **TEMP DEMO VALUES** — see §4 |

---

## Executive summary

This pack consolidates W0 + W0.5 discovery into an operator-approved **target brand map**, **legacy search dictionary**, **W1 wave plan** (W1A–W1F), **demo contact block**, **legal entity block**, and **rollback targets** for supervised Phase 1 execution on TEST.

**Critical operational notes:**

1. **Phone mismatch:** Admin `config_telephone` (`+73833886890`) ≠ theme-hardcoded storefront phone (`+73833885523`). W1A alone will not fix visible header/footer phone — **W1B required**.
2. **Mail identity:** Legacy Cyrillic and punycode domains in `config_email` and `config_mail_smtp_username` — replace in W1A; SMTP delivery may fail until Beget mailbox is provisioned for demo or production address.
3. **Address policy:** Showroom address (ул. Богдана Хмельницкого, 101) ≠ ATLAS legal address (ул. Доватора, 11). This pack maps legal address from LE-0005; operator may override for showroom display.
4. **Demo contacts:** All phone/email/messenger values in §4 are **temporary** and **must be replaced before production**.

---

## 1. Target Brand Map

**Legend:** `→` = replace old with new. `[DEMO]` = temporary demo value — **REPLACE BEFORE PRODUCTION**. `[LEGAL]` = attested LE-0005. `[HOLD]` = do not change in W1.

### 1.1 Brand name strings

| Old value | New value | Location(s) | Wave |
|-----------|-----------|-------------|------|
| `АЦ Хмельницкий` | `СИБКАР` | `config_name`; meta titles; H1; header/footer alt text; copyright; information pages; custom controllers | W1A, W1B, W1C, W1E |
| `Автоцентр Хмельницкий` | `Автосалон СИБКАР` | `config_meta_description`; `/about` keywords; body copy | W1A, W1C |
| `АЦ «Хмельницкий»` | `СИБКАР` | `/loan-terms` (information_id 16); legal phrasing in body | W1C |
| `ац Хмельницкий` | `СИБКАР` | `/about`, `/contact/` meta keywords (lowercase «ац») | W1C, W1E |
| `Автосалон «Хмельницкий»` | `Автосалон «СИБКАР»` | `/privacy-policy`, `/user-agreement`, cookie policy bodies | W1C |
| `Хмельницкий` *(brand context)* | `СИБКАР` | Privacy quoted form; homepage body; about/contact templates | W1B, W1C |
| `ООО «АЦ Хмельницкий»` | `ООО «СибКар»` `[LEGAL]` | `config_owner`; `footer.twig`; `contact.twig` legal line | W1A, W1B |
| `Вавилон` | `СИБКАР` *(or page title «О нас»)* | `/about_us` (information_id 4) — orphan title | W1C |
| `Автосалон №1 в Новосибирске` | `[OPERATOR]` — retain, rewrite, or remove | Homepage marketing block | W1B *(optional)* |

**Geographic exception — do NOT auto-replace as brand:**

| Old value | Policy | New value (if legal address adopted) |
|-----------|--------|--------------------------------------|
| `ул. Богдана Хмельницкого` / `улица Богдана Хмельницкого, 101` / `Хмельницкого` *(street)* | **Not a brand string** — geographic. Operator chose legal source LE-0005 for address fields. | `630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11` `[LEGAL]` |

### 1.2 Legacy domains and email

| Old value | New value | Location(s) | Wave | Notes |
|-----------|-----------|-------------|------|-------|
| `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | `demo@sibcar.local` `[DEMO]` | `config_email`; contact form `setTo` in `contact.php` | W1A | Punycode legacy `.рф` domain |
| `send@ац-хмельницкий.рф` | `demo@sibcar.local` `[DEMO]` | `config_mail_smtp_username` | W1A | Cyrillic legacy domain — **SMTP may not deliver** until real mailbox configured |
| `xn----7sbqmagfghm8fkh5f.xn--p1ai` | `[HOLD]` — out of W1 scope | `robots.txt` Host + Sitemap URL | — | DNS/SEO wave; do not change without operator plan |
| `ац-хмельницкий.рф` | `[HOLD]` | Legacy production domain (inferred from punycode + SMTP) | — | |
| `info_sibcar@mail.ru` | `[PRODUCTION TARGET]` — not applied in W1 demo | ATLAS attested email (LE-0005 / EV-W1C-CC-01) | Post-W1 | Use when exiting demo phase |

### 1.3 Legacy contact references

| Old value | New value | Location(s) | Wave | Notes |
|-----------|-----------|-------------|------|-------|
| `+7 (383) 388-55-23` | `+7 (000) 000-00-00` `[DEMO]` | `header.twig`, `footer.twig`, `contact.twig` | W1B | **Visible** storefront phone |
| `+73833885523` | `+70000000000` `[DEMO]` | `tel:` links, JSON attrs in templates | W1B | Normalized form |
| `+73833886890` | `+70000000000` `[DEMO]` | `config_telephone` (admin) | W1A | Admin-only until W1B syncs display |
| `https://wa.me/79539979910` | `[DEMO — OPERATOR DECISION]` | `header.twig`, `footer.twig` | W1B | **Different number** from main phone; no demo URL specified — hold or remove link until production messenger confirmed |
| `Ежедневно c 9:00-21:00` | `[RETAIN]` or operator-supplied hours | Theme hardcoded (not in `config_open`) | W1B *(optional)* | Not legacy brand |

### 1.4 SEO / meta strings

| Old value | New value | Location(s) | Wave |
|-----------|-----------|-------------|------|
| `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| АЦ Хмельницкий` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| СИБКАР` | `config_meta_title`; homepage `<title>` | W1A, W1E |
| `Автоцентр Хмельницкий в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` | `Автосалон СИБКАР в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` | `config_meta_description` | W1A, W1E |
| `АЦ Хмельницкий, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` | `СИБКАР, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` | `config_meta_keyword` | W1A, W1E |
| `alt="АЦ Хмельницкий"` | `alt="СИБКАР"` | `header.twig`, `footer.twig` logo img tags | W1B, W1D |
| `© … АЦ Хмельницкий` | `© … СИБКАР` | `footer.twig` | W1B |
| `<meta name="author" content="MCA">` | `[HOLD]` | All pages — vendor meta, not brand | — |
| `<meta name="yandex-verification" content="69e51badedb26226">` | `[HOLD]` | All pages | — | Do not change without Yandex re-verification plan |

### 1.5 Logo and asset filenames

| Old value | New value | Location(s) | Wave | Notes |
|-----------|-----------|-------------|------|-------|
| `catalog/logo_balck.png` | Operator-supplied SIBCAR logo path | `config_logo` (admin) | W1D | Typo filename `balck`; not used in sampled header/footer |
| `img/logo.svg` | New SIBCAR SVG (operator asset) | `header.twig` | W1D | SVG embedded text **SAFE UNKNOWN** |
| `img/logo_white.svg` | New SIBCAR white SVG | `header.twig`, `footer.twig` | W1D | |
| `img/logo - hmel.svg` | Delete or archive | Disk only — **not referenced** in templates | W1D | Legacy filename |
| `favicon/favicon.svg` + PNG set | New SIBCAR favicon set | Web root `/favicon/*` | W1D | |
| `catalog/favicon-16-black.png` | New favicon (operator asset) | `config_icon` | W1D | |
| `/img/preview.jpg` | New OG preview or remove broken ref | `<meta property="og:image">` | W1E | Currently **404** |

### 1.6 Information page titles (confirmed admin inventory)

| Page | SEO URL | ID | Old brand in title/body | New display pattern |
|------|---------|-----|---------------------------|---------------------|
| About (custom) | `/about` | — *(controller)* | АЦ Хмельницкий | СИБКАР |
| Contacts (custom) | `/contact/` | — *(controller)* | АЦ Хмельницкий | СИБКАР |
| Автокредит | `/autocredit` | 9 | Хмельницкий, АЦ | СИБКАР |
| Трейдин | `/tradein` | 10 | Хмельницкий, АЦ | СИБКАР |
| Условия автокредитования | `/loan-terms` | 16 | АЦ «Хмельницкий» | СИБКАР |
| Политика конфиденциальности | `/privacy-policy` | 13 | Хмельницкий, АЦ | СИБКАР / ООО «СибКар» |
| Пользовательское соглашение | `/user-agreement` | 5 | Хмельницкий, АЦ | СИБКАР / ООО «СибКар» |
| Политика Cookie | `/cookie-files-policy` | 3 | Хмельницкий, АЦ | СИБКАР / ООО «СибКар» |
| Акции | `/promos` | 8 | Хмельницкий, АЦ | СИБКАР |
| Выкуп авто | `/carbuyback` | 12 | Хмельницкий, АЦ | СИБКАР |
| Рассрочка | `/instalment` | 11 | Хмельницкий, АЦ | СИБКАР |
| Отзывы | `/reviews` | 7 | Хмельницкий, АЦ | СИБКАР |
| О нас | `/about_us` | 4 | Title «Вавилон» (orphan) | СИБКАР |
| Доставка | `/delivery` | 6 | No brand in admin content | No change expected |

---

## 2. Legacy Search Dictionary

Comprehensive grep/search list for pre-change baseline, post-change verification, and W1F QA. Search **case-insensitive** unless noted.

### 2.1 Russian — brand strings

```
Хмельницкий
хмельницкий
Хмельницкого
хмельницкого
АЦ Хмельницкий
АЦ «Хмельницкий»
ац Хмельницкий
ац «Хмельницкий»
Автоцентр Хмельницкий
автоцентр Хмельницкий
Автосалон Хмельницкий
Автосалон «Хмельницкий»
автосалон «Хмельницкий»
ООО «АЦ Хмельницкий»
ООО "АЦ Хмельницкий"
АЦ Хмельницкого
Вавилон
```

### 2.2 Russian — domain and mail

```
ац-хмельницкий
ац-хмельницкий.рф
@ац-хмельницкий.рф
send@ац-хмельницкий.рф
```

### 2.3 English / Latin transliterations

*(Not found in W0/W0.5 sampled surfaces — include in full-file grep anyway)*

```
Hmelnickiy
hmelnickiy
Hmelnickiy
Khmelnitskiy
khmelnitskiy
Khmelnitsky
khmelnitsky
AC Hmelnickiy
ac-hmelnickiy
ac_hmelnickiy
achmelnickiy
auto-center-hmelnickiy
autocenter-hmelnickiy
```

### 2.4 Punycode / IDN domain variants

```
xn----7sbqmagfghm8fkh5f.xn--p1ai
xn----7sbqmagfghm8fkh5f
```

### 2.5 Slug and URL variants

```
/about_us          ← orphan «Вавилон» title
hmel
logo - hmel
logo-hmel
logo_hmel
logo_balck         ← admin config_logo typo
```

### 2.6 File name variants

```
logo - hmel.svg
logo_balck.png
logo_black.png     ← possible corrected spelling on disk
favicon-16-black.png
/catalog/logo*
/img/logo*
/favicon/*
/image/catalog/logo*
```

### 2.7 Phone and messenger patterns (legacy)

```
388-55-23
3885523
73833885523
+73833885523
3833885523
388-68-90
3886890
73833886890
79539979910
wa.me/79539979910
```

### 2.8 Address strings (legacy showroom)

```
Богдана Хмельницкого
ул. Богдана Хмельницкого
улица Богдана Хмельницкого, 101
Новосибирск, ул. Богдана Хмельницкого 101
```

### 2.9 Search scope (filesystem + DB)

| Layer | Paths / tables |
|-------|----------------|
| Admin settings | `oc_setting` WHERE `key` LIKE `config_%` |
| Information pages | `oc_information_description` (IDs 3,5,7,8,9,10,11,12,13,16) |
| Theme templates | `catalog/view/theme/auto/template/**/*.twig`, `header_cup*.html` |
| Custom controllers | `catalog/controller/information/about.php`, `contact.php` |
| Language files | `catalog/language/ru-ru/**/*.php`, `admin/language/ru-ru/mail/*.php` |
| Images | `img/`, `image/catalog/`, `favicon/` |
| Web root | `robots.txt` |
| Modification cache | `system/storage/modification/` *(post-change W6)* |
| Extensions | `oc_setting` extension-prefixed keys *(SAFE UNKNOWN — grep required)* |

---

## 3. Phase W1 Scope

Exact files and settings expected to change. **Environment: TEST only.**

### 3.1 W1A — Store settings (Admin → System → Settings → Store)

| Target | Key / action | Old (confirmed) | New |
|--------|--------------|-----------------|-----|
| Store name | `config_name` | `АЦ Хмельницкий` | `СИБКАР` |
| Owner / legal line | `config_owner` | `ООО «АЦ Хмельницкий»` | `ООО «СибКар»` |
| Address | `config_address` | `Новосибирск, улица Богдана Хмельницкого, 101` | `630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11` |
| Email | `config_email` | `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | `demo@sibcar.local` `[DEMO]` |
| Telephone | `config_telephone` | `+73833886890` | `+70000000000` `[DEMO]` |
| Meta title | `config_meta_title` | *(see §1.4)* | *(see §1.4)* |
| Meta description | `config_meta_description` | *(see §1.4)* | *(see §1.4)* |
| Meta keywords | `config_meta_keyword` | *(see §1.4)* | *(see §1.4)* |
| SMTP username | `config_mail_smtp_username` | `send@ац-хмельницкий.рф` | `demo@sibcar.local` `[DEMO]` |

**Not changed in W1A:** `config_logo`, `config_icon`, `config_theme`, `config_fax`, `config_open`, `config_comment`, Yandex verification meta.

**Access method:** OpenCart admin UI (store_id **0**, single store confirmed).

### 3.2 W1B — Theme hardcoded contacts and brand strings

| File | Expected changes |
|------|------------------|
| `catalog/view/theme/auto/template/common/header.twig` | Phone display + `tel:` link; WhatsApp link; logo `alt` text |
| `catalog/view/theme/auto/template/common/footer.twig` | Phone; WhatsApp; copyright brand; logo `alt`; legal entity line |
| `catalog/view/theme/auto/template/common/home.twig` | H1 brand; body copy «Хмельницкий» |
| `catalog/view/theme/auto/template/information/contact.twig` | H1; legal line `ООО «АЦ Хмельницкий»`; phone if hardcoded |
| `catalog/view/theme/auto/template/information/about.twig` | Body brand strings |
| `catalog/view/theme/auto/template/common/header_cup*.html` | Verify and grep — brand/contact refs possible |

**Access method:** FTP/SFTP file edit (requires write charter).

### 3.3 W1C — Information pages and custom controllers

| Surface | Path / route | Method |
|---------|--------------|--------|
| Custom About | `catalog/controller/information/about.php` + `about.twig` | FTP — title, description, keywords, body |
| Custom Contact | `catalog/controller/information/contact.php` + `contact.twig` | FTP — title, description, keywords, H1, legal |
| Information module pages | Admin → Catalog → Information (IDs 3,5,7,8,9,10,11,12,13,16) | Admin UI HTML editor |
| Orphan About | `/about_us` (ID 4) | Admin — fix title «Вавилон» |

**Not in W1C:** `/delivery` (ID 6 — no brand in admin content).

### 3.4 W1D — Logos and favicons

| Asset | Action | Prerequisite |
|-------|--------|--------------|
| `img/logo.svg` | Replace file | Operator SVG staged in external `materials/` |
| `img/logo_white.svg` | Replace file | Operator SVG staged |
| `img/logo - hmel.svg` | Archive/delete | Optional cleanup |
| `image/catalog/logo_balck.png` | Replace + update `config_logo` if path changes | Operator PNG |
| `favicon/*` | Replace full set | Operator favicon pack |
| `image/catalog/favicon-16-black.png` | Replace + `config_icon` | Operator asset |
| `/img/preview.jpg` | Create or remove OG reference | Operator OG image |

**Blocker:** Logo assets **not staged** in repo/external materials index (C-03).

### 3.5 W1E — Meta / SEO

| Surface | Scope |
|---------|-------|
| Store meta (if not done in W1A) | Confirm `config_meta_*` reflected on homepage |
| Per-page meta | Custom controllers (`about.php`, `contact.php`); information pages |
| Template-level meta | Grep theme for hardcoded `<title>`, `<meta name="description">` |
| OG tags | Fix `/img/preview.jpg` 404; update `og:image` if new asset available |
| `robots.txt` | **Out of W1E** — legacy Host/Sitemap remain until DNS wave |

### 3.6 W1F — QA

| Check | Method |
|-------|--------|
| Legacy dictionary grep (§2) | FTP + DB read-only grep — target **0 matches** for brand terms |
| Visual spot-check | Homepage, `/about`, `/contact/`, `/privacy-policy`, footer on 3+ pages |
| Admin settings read-back | Confirm `config_*` values match target map |
| Phone/email display | Header, footer, contact page show demo values |
| Mail send test | **Optional** — may fail with `demo@sibcar.local` SMTP |
| Cache refresh | Clear theme/modification cache; hard-refresh browser |
| Screenshot set | Post-change evidence under external `materials/phase1-post-change/` |

---

## 4. Demo Contact Package

> ### ⚠ TEMPORARY DEMO DATA — REPLACE BEFORE PRODUCTION
>
> All values in this block are **explicit placeholders** for TEST Phase 1 execution only.  
> They **must not** ship to production. Replace with operator-confirmed production contacts before any production deployment or DNS cutover.

| Field | Demo value (W1) | Production target (reference) | Status |
|-------|-----------------|-------------------------------|--------|
| **Phone (display)** | `+7 (000) 000-00-00` | **SAFE UNKNOWN** in ATLAS | `[DEMO]` |
| **Phone (normalized / tel:)** | `+70000000000` | **SAFE UNKNOWN** | `[DEMO]` |
| **Email (store / forms)** | `demo@sibcar.local` | `info_sibcar@mail.ru` (LE-0005 attested) | `[DEMO]` |
| **SMTP username** | `demo@sibcar.local` | Operator-provisioned mailbox on Beget | `[DEMO]` — delivery not guaranteed |
| **WhatsApp** | `[HOLD]` — remove link or operator-supplied demo URL | **SAFE UNKNOWN** | Decision required before W1B |
| **Telegram** | Not present on site | **SAFE UNKNOWN** | — |
| **Viber** | Not present on site | **SAFE UNKNOWN** | — |
| **VK** | Not present on site | **SAFE UNKNOWN** | — |
| **Business hours** | Retain `Ежедневно c 9:00-21:00` unless operator overrides | **SAFE UNKNOWN** in ATLAS | Optional |
| **Physical / legal address** | `630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11` | Same — attested LE-0005 | `[LEGAL]` — not demo |

**Replacement checklist (pre-production):**

- [ ] Confirm production phone(s) with operator
- [ ] Confirm WhatsApp / messenger URLs
- [ ] Replace `demo@sibcar.local` with `info_sibcar@mail.ru` or operator mailbox
- [ ] Provision SMTP credentials on hosting for production email
- [ ] Re-run §2 legacy search dictionary — zero legacy contacts
- [ ] Update this pack to v1.1 with production contact block

---

## 5. Legal Entity Package

**Source:** ATLAS **LE-0005** · evidence **EV-W1C-CC-01** · attestation **AT-W1C-01** (active)  
**Evidence file:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx`

| Field | Value | Status |
|-------|-------|--------|
| **Legal entity ID** | LE-0005 | Attested |
| **Organization anchor** | ORG-0006 SIBCAR | Attested |
| **Legal name (full, RU)** | Общество с ограниченной ответственностью «СибКар» | Attested |
| **Legal name (short, RU)** | ООО «СибКар» | Attested — **use in footer / legal blocks** |
| **Legal name (full, EN)** | Limited Liability Company «SibCar» | Attested |
| **Legal name (short, EN)** | LLC «SibCar» | Attested |
| **INN** | 5405512542 | Attested |
| **KPP** | 540501001 | Attested |
| **OGRN** | 1265400004220 | Attested |
| **Legal address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | Attested |
| **Actual address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | Attested |
| **Tax system** | УСН Доходы 6% | Attested |
| **OKVED (primary)** | 45.11 — Торговля легковыми автомобилями и грузовыми автомобилями малой грузоподъемности | Attested |
| **Signatory** | Карандашов Максим Петрович | Attested |
| **Signatory title (exact)** | **MISSING** — CC lists «Руководитель» without explicit должность string | SAFE UNKNOWN |
| **Chief accountant** | Карандашов Максим Петрович | Attested |
| **Email (corporate)** | info_sibcar@mail.ru | Attested — **production target, not W1 demo** |
| **Phone / fax** | **MISSING** | SAFE UNKNOWN in ATLAS |
| **Registration date** | **MISSING** | SAFE UNKNOWN |
| **Postal address (separate)** | **MISSING** | SAFE UNKNOWN |
| **Bank** | АО «ТБанк» | Attested — **not for W1 site footer unless operator expands scope** |
| **Settlement account** | 40702810410002059263 | Attested |
| **BIC** | 044525974 | Attested |
| **Correspondent account** | 30101810145250000974 | Attested |
| **Websites / domains on CC** | **MISSING** | SAFE UNKNOWN |

**On-site legal block target (W1B/W1C):**

```
ООО «СибКар»
ИНН 5405512542 · ОГРН 1265400004220 · КПП 540501001
630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11
```

*(Exact formatting — operator approval at execution session.)*

---

## 6. Execution Waves

Recommended order: **W1A → W1B → W1C → W1D → W1E → W1F**.  
Each wave: operator-supervised session, backup note, scoped rollback (§7).

### W1A — Store settings

| Item | Detail |
|------|--------|
| **Scope** | Admin → System → Settings → Store (store_id 0): `config_name`, `config_owner`, `config_address`, `config_email`, `config_telephone`, `config_meta_*`, `config_mail_smtp_username` |
| **Method** | OpenCart admin UI |
| **Verification** | Admin read-back; homepage `<title>` / meta via view-source |
| **Dependencies** | Fresh backup (C-08); write charter (C-05) |
| **Known gap** | Visible phone unchanged until W1B |

### W1B — Theme hardcoded contacts

| Item | Detail |
|------|--------|
| **Scope** | `header.twig`, `footer.twig`, `home.twig`, `contact.twig`, `about.twig`, `header_cup*.html` |
| **Method** | FTP/SFTP edit |
| **Verification** | Storefront header/footer phone, alt text, copyright, H1 |
| **Dependencies** | W1A complete (consistent admin phone); write charter theme flag |

### W1C — Information pages

| Item | Detail |
|------|--------|
| **Scope** | 10 information pages (IDs 3,5,7,8,9,10,11,12,13,16) + custom `about.php`/`contact.php` + twig bodies |
| **Method** | Admin HTML editor + FTP for controllers/twig |
| **Verification** | Load each URL; grep page HTML for §2 dictionary |
| **Dependencies** | Legal block text from §5 approved by operator |

### W1D — Logos

| Item | Detail |
|------|--------|
| **Scope** | `/img/logo*.svg`, `/favicon/*`, `config_logo`, `config_icon`, optional `logo - hmel.svg` cleanup |
| **Method** | FTP upload + admin image path update |
| **Verification** | Visual header/footer; favicon in browser tab; `alt` text from W1B |
| **Dependencies** | **C-03 logo assets staged** — **BLOCKER if not met** |

### W1E — Meta / SEO

| Item | Detail |
|------|--------|
| **Scope** | Residual per-page meta in controllers; OG image fix; confirm store meta propagation |
| **Method** | FTP + admin |
| **Verification** | View-source on homepage + 3 service pages; social preview if OG fixed |
| **Dependencies** | W1A–W1C complete |

### W1F — QA

| Item | Detail |
|------|--------|
| **Scope** | Full §2 dictionary grep; visual pass; screenshot evidence; cache clear |
| **Method** | Read-only grep + operator walkthrough |
| **Verification** | Zero legacy brand hits; demo contacts visible; legal block correct |
| **Output** | `# REPORT — SITE-001 W1 QA` session note |

---

## 7. Rollback Targets

**Pre-requisite for all waves:** Dated file + DB backup immediately before W1A, stored at  
`C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups/` with label e.g. `pre-w1-2026-06-08`.

### W1A rollback — Store settings

| Modified | Revert method |
|----------|---------------|
| `oc_setting` rows: `config_name`, `config_owner`, `config_address`, `config_email`, `config_telephone`, `config_meta_title`, `config_meta_description`, `config_meta_keyword`, `config_mail_smtp_username` | **T1:** Re-enter pre-change values in admin (from W0.5 export snapshot). **T2:** DB restore of `oc_setting` slice from pre-W1 backup. **T3:** Full Beget file + DB restore. |

### W1B rollback — Theme templates

| Modified | Revert method |
|----------|---------------|
| `catalog/view/theme/auto/template/common/header.twig` | Restore file from pre-W1 backup or git/snapshot copy |
| `footer.twig`, `home.twig`, `contact.twig`, `about.twig`, `header_cup*.html` | Same — per-file restore |

### W1C rollback — Information pages

| Modified | Revert method |
|----------|---------------|
| `oc_information_description` rows (IDs 3,5,7,8,9,10,11,12,13,16) | Admin re-edit from pre-change export **or** DB row restore |
| `catalog/controller/information/about.php`, `contact.php` | File restore from backup |
| Associated twig files | File restore from backup |

### W1D rollback — Logos

| Modified | Revert method |
|----------|---------------|
| `/img/logo.svg`, `/img/logo_white.svg` | Restore original files from backup |
| `/favicon/*` | Restore original favicon set |
| `image/catalog/logo_balck.png`, `favicon-16-black.png` | Restore originals |
| `config_logo`, `config_icon` admin values | Re-enter paths from W0.5 snapshot |

### W1E rollback — Meta / SEO

| Modified | Revert method |
|----------|---------------|
| Controller meta strings | File restore |
| OG image path / new `preview.jpg` | Remove new file; restore meta from backup |
| Any residual template meta | File restore |

### W1F rollback — QA

| Modified | Revert method |
|----------|---------------|
| *(read-only wave)* | No rollback — if QA fails, roll back failing wave (W1A–W1E) per above |

**Full TEST restore (T2):** Beget panel → restore files + MySQL to pre-W1 snapshot if multi-wave rollback impractical.

---

## 8. Final Authorization

### Question: Can W1 execution begin?

## **AUTHORIZED WITH NOTES**

### Rationale

| Criterion | Status |
|-----------|--------|
| W0 public discovery | **PASS** |
| W0.5 admin discovery — `config_*` confirmed | **PASS** |
| Active theme identified (`auto`) | **PASS** |
| Legacy brand inventory | **PASS** |
| Target brand map (operator: СИБКАР / SIBCAR) | **PASS** — this pack |
| Legal entity source LE-0005 | **PASS** — attested |
| Demo contact pack defined | **PASS** — with REPLACE BEFORE PRODUCTION warnings |
| Legacy search dictionary | **PASS** — §2 |
| Rollback targets defined | **PASS** — §7 |

### Notes — required before first write session

| # | Gate | Status | Action |
|---|------|--------|--------|
| C-05 | Write charter on [project-access-brief.md](../project-access-brief.md) | **FAIL** | Operator: enable file/DB/theme edits on TEST + named approver |
| C-06 | Change Request + Rollback Plan instances | **FAIL** | Bind to this pack; use templates in `templates/` |
| C-08 | Fresh file + DB backup | **FAIL** | Take backup **immediately before W1A**; do not rely on 2026-05-31 claim |
| C-03 | Logo assets staged | **FAIL** | Blocks **W1D only** — W1A/B/C/E may proceed without logos |
| C-04 | Production phones / messengers | **DEFERRED** | Demo placeholders approved for TEST; WhatsApp link needs decision before W1B |
| C-09 | Pre-change screenshot set | **RECOMMENDED** | External `materials/phase1-pre-change-freeze/` |
| C-11 | Decision v1.1 sign-off | **THIS DOCUMENT** | Program owner acknowledges **AUTHORIZED WITH NOTES** |

### Wave-start matrix

| Wave | Authorized to begin? | Blocker |
|------|---------------------|---------|
| **W1A** Store settings | **YES** *(after C-05, C-06, C-08)* | Write charter; fresh backup |
| **W1B** Theme contacts | **YES** *(after W1A + C-05)* | Write charter; WhatsApp decision |
| **W1C** Information pages | **YES** *(after C-05)* | Write charter |
| **W1D** Logos | **NO** until C-03 | Logo assets not staged |
| **W1E** Meta/SEO | **YES** *(after W1A–W1C)* | — |
| **W1F** QA | **YES** *(after W1A–W1E)* | — |

### Production gate

**NOT AUTHORIZED** for production deployment until:

1. All `[DEMO]` contacts replaced with production values (§4 checklist).
2. Logo assets applied (W1D complete).
3. Operator confirms address policy (showroom vs legal).
4. Separate production change authorization issued.

---

## Related documents

| Document | Role |
|----------|------|
| [SITE-001-W0.5-ADMIN-DISCOVERY-v1.md](SITE-001-W0.5-ADMIN-DISCOVERY-v1.md) | Confirmed admin values |
| [SITE-001-BRAND-REPLACEMENT-MAP-v1.md](SITE-001-BRAND-REPLACEMENT-MAP-v1.md) | W0 discovery matrix |
| [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) | Checklist C-01..C-11 |
| [project-access-brief.md](../project-access-brief.md) | Write permissions gate |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](../../../atlas/population/ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | LE-0005 register row |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — W1 Execution Pack v1; authorization **AUTHORIZED WITH NOTES** |

*SITE-001 W1 Execution Pack v1 — planning only; no site modifications performed.*

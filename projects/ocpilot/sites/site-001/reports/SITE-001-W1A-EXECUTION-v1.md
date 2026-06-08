# SITE-001 W1A Execution v1

**Type:** Supervised W1A execution report — Store Settings replacement  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Authorization:** [SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md](SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md) — **AUTHORIZED WITH NOTES**  
**Scope:** W1A only — admin Store Settings; 6 fields per operator constraint  
**Admin route used:** `System → Settings` — `index.php?route=setting/setting` (store_id **0**)

**Binding documents:**

| Document | Role |
|----------|------|
| [SITE-001-W1A-EXECUTION-SPEC-v1.md](SITE-001-W1A-EXECUTION-SPEC-v1.md) | Target values |
| [SITE-001-W0.5-ADMIN-DISCOVERY-v1.md](SITE-001-W0.5-ADMIN-DISCOVERY-v1.md) | Before-value baseline |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Rollback reference T1 |

---

## Execution summary

| Step | Status | Notes |
|------|--------|-------|
| 1. Record before-values | **DONE** | Admin read-back + storefront HTTP |
| 2. Apply changes | **DONE** | 6 in-scope `config_*` keys |
| 3. Save settings | **DONE** | Admin success alert confirmed |
| 4. Clear caches | **DONE** | oc3x_storage_cleaner + modification refresh |
| 5. Open storefront | **DONE** | Homepage + contact page |
| 6. Verify pages | **DONE** | See verification table |
| 7. Capture after-values | **DONE** | Admin read-back + storefront HTTP |
| 8. Produce execution report | **DONE** | This document |

**Production:** **NOT TOUCHED** — TEST URL only.

---

## Before values (admin — store_id 0)

| Key | Value |
|-----|-------|
| `config_name` | `АЦ Хмельницкий` |
| `config_owner` | `ООО «АЦ Хмельницкий»` |
| `config_email` | `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` |
| `config_meta_title` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| АЦ Хмельницкий` |
| `config_meta_description` | `Автоцентр Хмельницкий в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` |
| `config_meta_keyword` | `АЦ Хмельницкий, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` |

**Excluded fields (unchanged — confirmed):**

| Key | Value (unchanged) |
|-----|-------------------|
| `config_address` | `Новосибирск, улица Богдана Хмельницкого, 101` |
| `config_telephone` | `+73833886890` |
| `config_mail_smtp_username` | `send@ац-хмельницкий.рф` |

---

## After values (admin — store_id 0)

| Key | Value |
|-----|-------|
| `config_name` | `СИБКАР` |
| `config_owner` | `ООО «СибКар»` |
| `config_email` | `demo@sibcar.local` |
| `config_meta_title` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| СИБКАР` |
| `config_meta_description` | `Автосалон СИБКАР в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` |
| `config_meta_keyword` | `СИБКАР, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` |

**Excluded fields (unchanged — confirmed):**

| Key | Value (unchanged) |
|-----|-------------------|
| `config_address` | `Новосибирск, улица Богдана Хмельницкого, 101` |
| `config_telephone` | `+73833886890` |
| `config_mail_smtp_username` | `send@ац-хмельницкий.рф` |

**Admin read-back mismatches:** **0**

---

## Storefront before / after

### Homepage (`/`)

| Field | Before | After |
|-------|--------|-------|
| `<title>` | …\| **АЦ Хмельницкий** | …\| **СИБКАР** |
| `<meta name="description">` | **Автоцентр Хмельницкий**… | **Автосалон СИБКАР**… |
| `<meta name="keywords">` | **АЦ Хмельницкий**, … | **СИБКАР**, … |

### Contact page (`/contact/`)

| Field | Before | After |
|-------|--------|-------|
| `<title>` | Контакты **АЦ Хмельницкий**… | **Unchanged** — legacy brand remains |
| `<meta name="description">` | …**АЦ Хмельницкий**… | **Unchanged** |
| `<meta name="keywords">` | …**Хмельницкий**… | **Unchanged** |

*Contact meta is controller-hardcoded per W0.5 — deferred to **W1C/W2**.*

### Footer (homepage + contact)

| Check | After W1A |
|-------|-----------|
| Legacy brand in footer template | **YES** — `ООО «АЦ Хмельницкий»`, `© … АЦ Хмельницкий` (theme — **W1B**) |
| Legacy phone in header/footer | **YES** — `+7 (383) 388-55-23` (theme — **W1B**) |

---

## Pages checked

| URL | HTTP | Primary check | Result |
|-----|------|---------------|--------|
| `https://sibcar.new-site.space/` | 200 | title, meta description, meta keywords | **PASS** — СИБКАР in meta layer |
| `https://sibcar.new-site.space/contact/` | 200 | title, meta, footer | **PARTIAL** — meta/H1 legacy; footer legacy |

---

## Cache actions

| Action | Method | Result |
|--------|--------|--------|
| Twig / system cache | oc3x_storage_cleaner `clearcache` key=system | **OK** — «Успешно очищено!» |
| Modification cache | oc3x_storage_cleaner `clearcache` key=modification | **OK** |
| Image cache | oc3x_storage_cleaner `clearcache` key=image | **OK** |
| Modification refresh | `marketplace/modification/refresh` | **OK** — HTTP 200 |

---

## Unexpected findings

| # | Finding | Severity | Action |
|---|---------|----------|--------|
| F-01 | Admin route `setting/store/edit&store_id=0` rejects POST without full multi-store fields (`config_url` required) — save silently fails validation | **Info** | Used canonical single-store route `setting/setting` instead; values persist correctly |
| F-02 | Homepage `<h1>`, header/footer logos, copyright, phone, WhatsApp remain legacy | **Expected** | **W1B** theme wave |
| F-03 | Contact page title/meta/H1 remain legacy (custom `contact.php` / twig) | **Expected** | **W1C/W2** |
| F-04 | `config_mail_smtp_username` still legacy Cyrillic domain — outbound mail identity unchanged | **Expected** | Out of W1A scope per operator constraint |
| F-05 | Partial debug run during session briefly set `config_name` alone via `setting/setting` before full W1A POST — superseded by final 6-field save with verified read-back | **Low** | Final state verified; no rollback needed |

---

## Rollback required

**NO**

All in-scope admin keys match target values. Excluded keys unchanged. No production impact. Rollback available per [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) T1 if operator requests.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — W1A Store Settings execution on TEST |

*SITE-001 W1A Execution v1 — supervised session 2026-06-08.*

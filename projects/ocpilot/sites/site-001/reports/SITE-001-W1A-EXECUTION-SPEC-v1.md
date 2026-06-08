# SITE-001 W1A Execution Spec v1

**Type:** Wave-scoped execution specification — **documentation only**; no site modification  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Wave:** **W1A** — Store Settings only  
**Method:** OpenCart admin → System → Settings → Store (store_id **0**)

**Binding documents:**

| Document | Role |
|----------|------|
| [SITE-001-W1-EXECUTION-PACK-v1.md](SITE-001-W1-EXECUTION-PACK-v1.md) | Parent target map §1, §3.1 |
| [SITE-001-W0.5-ADMIN-DISCOVERY-v1.md](SITE-001-W0.5-ADMIN-DISCOVERY-v1.md) | Confirmed old values |
| [SITE-001-W1-CHANGE-REQUEST-v1.md](SITE-001-W1-CHANGE-REQUEST-v1.md) | CR-SITE-001-W1-2026-06-08 |
| [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md) | Write scope and gates |

**Brand:** **СИБКАР** / **SIBCAR**  
**Legal entity source:** **ATLAS LE-0005**

---

## Scope boundaries (W1A)

| In scope | Out of scope |
|----------|--------------|
| Admin → System → Settings → Store (`oc_setting` keys below) | Theme templates (`*.twig`, `header_cup*.html`) — **W1B** |
| Brand, legal owner, address, email, meta fields, SMTP username | `config_telephone` — **DO NOT change in W1A** |
| | WhatsApp links — **W1B**; operator decision (C-04) |
| | `config_logo`, `config_icon`, logos — **W1D** (C-03) |
| | Information pages — **W1C** |
| | Production host, DNS, `config.php`, catalog |

**Explicit operator constraint (this package):** Phones, WhatsApp, and theme templates are **not** modified in W1A.

---

## Execution table

| Key | Old Value | New Value | Source | Risk |
|-----|-----------|-----------|--------|------|
| `config_name` | `АЦ Хмельницкий` | `СИБКАР` | W0.5 §A; execution pack §1.1, §3.1 | **LOW** — admin read-back |
| `config_owner` | `ООО «АЦ Хмельницкий»` | `ООО «СибКар»` | W0.5 §A; execution pack §1.1; ATLAS **LE-0005** | **LOW** — legal line; verify spelling |
| `config_email` | `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | `demo@sibcar.local` `[DEMO]` | W0.5 §A; execution pack §1.2 | **MEDIUM** — legacy punycode removed; contact form routing unchanged until W1C |
| `config_meta_title` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| АЦ Хмельницкий` | `Купить авто с пробегом в Новосибирске — проверенные автомобили б/у \| СИБКАР` | W0.5 §A; execution pack §1.4 | **LOW** — verify homepage `<title>` after save |
| `config_meta_description` | `Автоцентр Хмельницкий в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` | `Автосалон СИБКАР в Новосибирске предлагает надёжные автомобили с пробегом. Большой выбор, честные цены, оформление кредита, рассрочки и обмен по системе Trade-in.` | W0.5 §A; execution pack §1.4 | **LOW** |
| `config_meta_keyword` | `АЦ Хмельницкий, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` | `СИБКАР, автомобили с пробегом Новосибирск, купить б/у авто, Trade-in Новосибирск, автокредит` | W0.5 §A; execution pack §1.4 | **LOW** |
| `config_address` | `Новосибирск, улица Богдана Хмельницкого, 101` | `630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11` | W0.5 §A; execution pack §1.1; ATLAS **LE-0005** `[LEGAL]` | **MEDIUM** — legal vs showroom address policy; operator approved LE-0005 source |
| `config_mail_smtp_username` | `send@ац-хмельницкий.рф` | `demo@sibcar.local` `[DEMO]` | W0.5 §A (mail settings); execution pack §1.2 | **MEDIUM** — SMTP may not deliver until real mailbox configured |

---

## Explicitly excluded from W1A (no change)

| Key | Current value (W0.5) | Deferred to | Notes |
|-----|----------------------|-------------|-------|
| `config_telephone` | `+73833886890` | **W1B** or later | Operator: **DO NOT change phones in W1A**. Storefront still shows theme-hardcoded `+7 (383) 388-55-23` until W1B. |
| WhatsApp URL | `https://wa.me/79539979910` (theme) | **W1B** | Operator decision (C-04) required before change |
| Theme templates | — | **W1B** | No FTP/file edits in W1A |

**Not changed in W1A (unchanged from execution pack §3.1):** `config_logo`, `config_icon`, `config_theme`, `config_fax`, `config_open`, `config_comment`, Yandex verification meta.

---

## Verification checklist (post-save)

| # | Check | Expected |
|---|-------|----------|
| V-01 | Admin read-back — all in-scope keys | Match **New Value** column above |
| V-02 | Homepage view-source — `<title>` | Contains `СИБКАР`; no `АЦ Хмельницкий` |
| V-03 | Homepage view-source — meta description | Contains `Автосалон СИБКАР` |
| V-04 | Storefront header/footer phone | **Unchanged** (legacy theme phone) — expected until W1B |
| V-05 | Admin `config_telephone` | **Unchanged** `+73833886890` |
| V-06 | Environment URL | `https://sibcar.new-site.space/` only |

---

## Rollback reference

Per [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) **T1:** re-enter pre-change values from W0.5 snapshot for each key in the execution table above.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — W1A Store Settings spec; phones/WhatsApp/theme excluded per operator constraint |

*SITE-001 W1A Execution Spec v1 — specification only; no site access performed.*

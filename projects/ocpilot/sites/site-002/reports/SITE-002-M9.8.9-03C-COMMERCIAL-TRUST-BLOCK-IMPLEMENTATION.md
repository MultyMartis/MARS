# REPORT — M9.8.9-03C COMMERCIAL TRUST BLOCK IMPLEMENTATION FROM APPROVED STRUCTURE

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`  
**Task:** M9.8.9-03C — commercial trust block rework (approved visual structure)  
**Date:** 2026-06-20  
**Commit / push:** **NO** (per charter)

**PRE-TASK RULE:** Knowledge Map + Stable Checkpoint + M9.8.9-03B redesign + M9.8.9-03 implementation + site-passport — read and applied.

---

## 1. What Changed

M9.8.9-03 (trust strip + dealer split) replaced on **category PLP only** with a single unified commercial card:

- Header zone: label + dynamic H2 + lead text
- Main grid (~25% / ~35% / ~40%): one certificate + 6 benefit facts + lead form
- Footer row: 4 compact service theses

Uses existing ZPM design tokens (`--radius-main`, `--border-color`, `--main-light-color`, `--accent-color-02`, `.zpm-form`, `.btn`, Font Awesome `fal` icons). No new design system. M9.8.9-03 CSS block superseded by M9.8.9-03C block in `style.css`.

**Out of scope (unchanged):** homepage, `/katalog`, PDP, megamenu, footer, filters, product grid, 1C, price logic, `main.js`.

---

## 2. Structure Implemented

```
section.zpm-commercial-trust.zpm-dealers[data-commercial-trust][data-dealers]
└── .container
    └── .zpm-commercial-trust__card
        ├── .zpm-commercial-trust__header
        │   ├── label «Поможем с выбором»
        │   ├── H2 (dynamic)
        │   └── lead text (Excel price list promise)
        ├── .zpm-commercial-trust__main (25/35/40 grid)
        │   ├── .zpm-commercial-trust__cert-col — 1 visible cert + «Все сертификаты»
        │   ├── .zpm-commercial-trust__benefits — 2×3 FA icon grid
        │   └── .zpm-commercial-trust__form-col — titled form card + note
        └── .zpm-commercial-trust__services — 4 compact cards (desktop row)
```

**Mobile stack order:** label → H2 → text → certificate → benefits → form → 4 service cards.

---

## 3. Dynamic Category Title

`category.php` passes `$data['commercial_trust_heading']` into `blockcommercialtrust.twig`.

| Category name (DB) | H2 on live |
|--------------------|------------|
| Столы | Нужна помощь с выбором столов? |
| Моечные ванны | Нужна помощь с выбором моечных ванн? |
| Подтоварники и подставки | Нужна помощь с выбором подтоварников и подставок? |
| Тележки сервировочные | Нужна помощь с выбором тележек? |
| Зонты вытяжные | Нужна помощь с выбором зонтов? |
| **Fallback** (other categories) | Подберём оборудование под вашу задачу |

Verified on live TEST for Столы, Моечные ванны, Подтоварники (automated probe `title_match: true`).

---

## 4. Certificate Behaviour

| Item | Result |
|------|--------|
| Visible on PLP | **1** certificate (`certificat_00.jpg` / `thumb_00.png`) |
| Demo duplicates | **Not shown** (removed second visible thumb from M9.8.9-03) |
| Slider markup | **Retained** — `.swiper.js-commercial-trust-certs` with **one slide** (ready for future certs) |
| Fancybox group | `data-fancybox="certificates-plp"` — **3 links**: visible cert, «Все сертификаты», visually hidden `certificat_01.jpg` |
| Unique files in group | **2** (`certificat_00`, `certificat_01`) — no duplicate slides |
| «Все сертификаты» | **Kept** — opens fancybox group |
| Homepage / katalog | **Unchanged** — legacy `certificates.twig` slider |

Fancybox open on click — **not auto-tested**; operator visual HITL recommended.

---

## 5. Form Changes

| Field | Before (M9.8.9-03) | After (M9.8.9-03C) |
|-------|--------------------|----------------------|
| Section context | «Дилерам и оптовикам» + bullets | Form card title «Получить прайс-лист в Excel» |
| Message label | Вопрос | **Комментарий** |
| Message placeholder | Напишите ваш вопрос | Опишите задачу или интересующие позиции |
| Submit | Отправить | **Отправить заявку** |
| Footer note | — | «Отправим актуальный прайс-лист…» |

**Preserved:** `POST`, `dialog=7`, field IDs/names, phone mask, email validation, privacy checkbox, `zpm-dealers` + `data-dealers` for existing JS, single form instance per PLP.

Form POST end-to-end — **not auto-tested**; operator HITL recommended.

---

## 6. Files Changed

### Live (deployed to TEST FTP — 2026-06-20)

| Remote path | Action | SHA256 pre → post |
|-------------|--------|-------------------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | **REPLACED** | `3c7fec65…` → `c20798e8…` |
| `catalog/controller/product/category.php` | **MODIFIED** | `10c2bdc8…` → `b4594c74…` |
| `assets/css/style.css` | **MODIFIED** (M9.8.9-03 → 03C CSS block) | `b7269752…` → `6cf6a703…` |

**Not changed:** `category.twig`, `main.js`, homepage/katalog templates, filters, PDP.

### Repo (work artefacts + report)

| Path | Role |
|------|------|
| `reports/m9.8.9-03c-work/blockcommercialtrust.twig` | Source template |
| `reports/m9.8.9-03c-work/m9.8.9-03c-commercial-trust.css` | CSS block |
| `reports/m9.8.9-03c-work/m9.8.9-03c-deploy-run.py` | FTP capture / backup / deploy / SHA verify |
| `reports/m9.8.9-03c-work/m9.8.9-03c-qa-probe.py` | Live HTML QA |
| `reports/m9.8.9-03c-work/manifest-complete-20260619-171729.json` | Post-deploy manifest |
| `reports/m9.8.9-03c-work/qa-live-probe.json` | QA results |
| `reports/m9.8.9-03c-work/live-capture/*` | Pre-deploy FTP capture |
| `backups/blockcommercialtrust.twig.pre-m9.8.9-03c.bak` | Rollback |
| `backups/category.php.pre-m9.8.9-03c.bak` | Rollback |
| `backups/style.css.pre-m9.8.9-03c.bak` | Rollback |

---

## 7. QA Results

Automated live probe — 2026-06-20 (`m9.8.9-03c-qa-probe.py`):

| Page | commercial trust | dynamic title | 1 cert visible | 6 benefits | 4 services | form dialog=7 | legacy certs | Pass |
|------|:----------------:|:-------------:|:--------------:|:----------:|:----------:|:-------------:|:------------:|:----:|
| **Столы** | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0 | ✅ |
| **Моечные ванны** | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0 | ✅ |
| **Подтоварники** | ✅ | ✅ | ✅ | ✅ | ✅ | 1 | 0 | ✅ |
| Homepage (control) | ❌ expected | n/a | n/a | n/a | n/a | 1 | 1 + slider | ✅ |
| `/katalog` (control) | ❌ expected | n/a | n/a | n/a | n/a | 1 | 1 + slider | ✅ |

**Additional checks (automated):** unified card ✅ · label «Поможем с выбором» ✅ · form title ✅ · «Комментарий» label ✅ · no «Вопрос» ✅ · submit «Отправить заявку» ✅ · form note ✅ · fancybox group 2 unique files ✅.

**Operator HITL still recommended:** Fancybox zoom, form submit, mobile visual at 390px, console errors.

---

## 8. Rollback

1. `backups/blockcommercialtrust.twig.pre-m9.8.9-03c.bak` → `catalog/view/theme/default/template/sections/blockcommercialtrust.twig`  
   *(or `backups/…pre-m9.8.9-03…` for M9.8.9-03 strip version)*
2. `backups/category.php.pre-m9.8.9-03c.bak` → `catalog/controller/product/category.php`
3. `backups/style.css.pre-m9.8.9-03c.bak` → `assets/css/style.css`
4. Clear Twig template cache on FTP
5. Manifest reference: `reports/m9.8.9-03c-work/manifest-complete-20260619-171729.json`

Full rollback to pre-M9.8.9-03 state: use M9.8.9-03 backups documented in [SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-IMPLEMENTATION.md](SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-IMPLEMENTATION.md).

---

## 9. Risks

| Risk | Severity | Notes |
|------|----------|-------|
| Twig cache clear returned 0 files | Low | Pages render correctly post-deploy; flush manually if stale block seen |
| Form submit not auto-tested | Medium | Endpoint unchanged from M9.8.9-03; HITL submit on one PLP |
| Fancybox not auto-tested | Low | Same library/group pattern as prior pass |
| Category title map incomplete | Low | Unknown categories use safe fallback copy |
| Swiper not initialized for cert slider | Low | Single slide — static display OK; init only needed when multiple certs added |
| Copy claims (production, guarantee) | Low | Factual commercial copy per charter; operator may refine wording |
| `fa-user-headset` icon | Low | FA Pro 5.15 — verify glyph renders on live (fallback: swap to `fa-headset` if missing) |

---

## Deploy safety log

| Step | Status |
|------|--------|
| FTP capture (3 files) | ✅ `reports/m9.8.9-03c-work/live-capture/` |
| Backup `.pre-m9.8.9-03c.bak` | ✅ twig · category.php · style.css |
| Manifest + SHA verify | ✅ `manifest-complete-20260619-171729.json` — `all_deploy_ok: true` |
| Twig cache clear | Attempted (0 entries deleted) |

---

## Git status (this pass)

| Item | Value |
|------|-------|
| Live code | Deployed to TEST only |
| Repo | Work artefacts + this report |
| Commit | **Not performed** |
| Push | **Not performed** |

---

*Implementation complete. Awaiting operator visual QA on TEST before optional git registration.*

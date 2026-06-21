# REPORT — SITE-001 Visual Change Failure Audit

**Type:** Technical failure audit — read-only  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Scope:** W3-V · W3V2 · W3UX-C1 · W3ATMOSPHERE-01 (active layers)  
**Site modifications:** **NONE** — HTTP fetch + CSS/HTML inspection only

**Evidence (local, not in git):**

- `.recovery-temp/site-001-visual-failure-audit.py` — live probe output (2026-06-09)
- `.recovery-temp/site-001-visual-failure-audit-deep.py` — cascade / body-bg analysis
- `.recovery-temp/site-001-visual-failure-audit-pdp3.py` — used PDP probe
- `.recovery-temp/site-001-w3atmosphere-01-result.json` — execution-time verification (2026-06-09 11:56 UTC)

**Operator directive honored:** no new design · no new atmosphere CSS · no FTP · no cache clear · no implementation.

---

## Executive summary

Визуальные волны **технически применены** на TEST. Live `/css/main.css` и `/css/media.css` — те же файлы, что редактировались при W3V2/W3ATMOSPHERE; маркеры и байтовые размеры совпадают с execution reports. CSS загружается **последним** в каскаде; пост-W3ATMOSPHERE override-правил **нет**.

Оператор не видит «смысленного» изменения **не потому что CSS не доехал**, а из‑за **смешанной причины**:

1. **Изменения слишком слабые по дизайну** — инкрементальные сдвиги палитры/теней поверх уже частично обновлённого TEST (W3-V → W3V2 → W3ATMOSPHERE).
2. **Несовпадение ожиданий** — оператор ожидает трансформацию уровня Phase 1 → «другой сайт»; CSS-only atmosphere charter этого не обещает.
3. **Вторичный риск browser cache** — `Cache-Control: max-age=604800` (7 суток) может показывать старый CSS у клиентов, посетивших TEST до upload (сервер отдаёт актуальный файл).

**Root cause verdict:** **mixed cause** — primary: **changes too weak** + **expectation mismatch**; secondary: **possible client cache**; ruled out: CSS not loaded, wrong file, cascade override, selectors globally wrong, extra CSS after main/media.

---

## 1. Live CSS loading order

### Homepage (`/`)

| # | Stylesheet | Media |
|---|------------|-------|
| 1 | `css/normalize.css` | all |
| 2 | Google Fonts — Exo 2 | all |
| 3 | Google Fonts — Inter 600 | all |
| 4 | `/libs/fancybox/fancybox.css` | all |
| 5 | `/libs/swiper/swiper-bundle.min.css` | all |
| 6 | `/libs/fontawesome/css/all.min.css` | all |
| 7 | **`/css/main.css`** | all |
| 8 | **`/css/media.css`** | all |

**После `main.css` / `media.css`:** ничего. ✓

### Used catalog (`/cars/`)

Тот же порядок, плюс **до** main.css:

- `catalog/view/javascript/jquery/swiper/css/swiper.min.css` (screen)
- `catalog/view/javascript/jquery/swiper/css/opencart.css` (screen)

Оба — OC Swiper widgets; **не** перекрывают atmosphere-селекторы (header/footer/body/cards). **`/css/main.css` и `/css/media.css` остаются последними.** ✓

### About (`/about`)

Идентично homepage (8 stylesheets). ✓

### Used PDP (live probe)

**URL:** `https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799`  
(SEO slug в корне; не `/cars/...` — важно для QA-маршрутизации)

| # | Stylesheet |
|---|------------|
| 1–6 | normalize · fancybox · swiper · fontawesome |
| 7 | **`/css/main.css`** |
| 8 | **`/css/media.css`** |

**После main/media:** ничего. ✓

### Consistency

Порядок **не идентичен** на всех страницах (catalog добавляет 2 OC swiper CSS), но **theme CSS всегда последний** — критичное условие выполнено.

---

## 2. CSS markers found / not found

### `/css/main.css` (live HTTP 200)

| Check | Expected (W3ATMOSPHERE execution) | Live | Match |
|-------|-----------------------------------|------|-------|
| Bytes | 129 060 | **129 060** | ✓ |
| Lines | 7 771 | **7 770** | ✓ (±1 newline) |
| `SITE-001 W3ATMOSPHERE-01` | yes | **yes** | ✓ |
| `SITE-001 W3V2` | yes | **yes** | ✓ |
| `W3-V` block | yes | **yes** | ✓ |
| `W3UX` block | yes | **yes** | ✓ |
| `--w3color-canvas` / `#EEF1F5` | yes | **yes** | ✓ |
| `--w3v2-brand-red` | yes | **yes** | ✓ |
| `W3VIS` block | no (rolled back) | **no** | ✓ |
| W3ATMOSPHERE block position | end of file | lines **7418–7768** (last override layer) | ✓ |
| `Last-Modified` | post-upload | **Tue, 09 Jun 2026 04:57:16 GMT** | ✓ |

### `/css/media.css` (live HTTP 200)

| Check | Expected | Live | Match |
|-------|----------|------|-------|
| Bytes | 32 601 | **32 601** | ✓ |
| Lines | 2 293 | **2 292** | ✓ |
| `SITE-001 W3ATMOSPHERE-01` | yes | **yes** | ✓ |
| `SITE-001 W3V2` | yes | **yes** | ✓ |
| W3ATMOSPHERE responsive block | end of file | line **2292** (file terminus) | ✓ |
| `Last-Modified` | post-upload | **Tue, 09 Jun 2026 04:57:18 GMT** | ✓ |

### Файлы — те же, что редактировались?

| Question | Verdict |
|----------|---------|
| 1. `/css/main.css` from TEST — тот же файл? | **YES** — byte-exact match с W3ATMOSPHERE-01 execution |
| 2. `/css/media.css` from TEST — тот же файл? | **YES** — byte-exact match |
| 3. Другой theme CSS path? | **NO evidence** — HTML ссылается только на `/css/main.css` + `/css/media.css` |

---

## 3. Selector hit/miss table

Селекторы из W3ATMOSPHERE / W3V2; проверка class/id **в live HTML** (не computed styles).

| Selector / marker | Homepage `/` | Catalog `/cars/` | About `/about` | Used PDP `audi-a1-...` | CSS last rule wins |
|-------------------|:------------:|:----------------:|:--------------:|:----------------------:|:------------------:|
| `body` | HIT | HIT | HIT | HIT | W3ATM line 7485 `--w3color-canvas` |
| `.singe_bar__wrap` | HIT | HIT | HIT | HIT | W3ATM line 7524 |
| `nav` | HIT | HIT | HIT | HIT | W3ATM gradient group ~7510 |
| `footer` | HIT | HIT | HIT | HIT | W3ATM line 7530 |
| `.footer_top` | HIT | HIT | HIT | HIT | W3ATM transparent override |
| `.catalog_item` | MISS* | HIT | MISS* | MISS* | W3ATM line 7593 `.catalog_item > a` |
| `.catalog_item > a` (DOM) | — | **HIT**† | — | — | W3ATM line 7593 (12px card recipe) |
| `.catalog_item > div` (DOM direct child) | — | **MISS**‡ | — | — | Rule exists; DOM uses `<a>` child |
| `.partner_banks__item` | HIT | HIT | HIT | — | W3ATM grouped card rule |
| `.four_blocks` | HIT | MISS* | HIT | MISS* | W3ATM line 7600 (overrides legacy 5234) |
| `.search_form` | MISS* | HIT | MISS* | MISS* | W3ATM line 7639 |
| `.callback_btn` / `.phone_btn` | HIT | HIT | HIT | HIT | W3ATM line 7744 |
| `.offcanvas_nav` | HIT | HIT | HIT | HIT | W3ATM nav group |
| `.car_main_info__btns` | MISS* | MISS* | MISS* | **HIT** | W3ATM CTA group |
| `.used_car__credit` | MISS* | MISS* | MISS* | **HIT** | W3ATM dark band gradient |
| `.car_vin_check` | MISS* | MISS* | MISS* | **HIT** | W3ATM card recipe |
| `.popup__FORM_wrap` | HIT | HIT | HIT | HIT | W3ATM line 7663 |
| `.wsp_footer__legal_details` | MISS* | MISS* | MISS* | — | Footer legal variant not on all pages |

\* MISS = элемент отсутствует на странице (ожидаемо, не ошибка CSS).  
† DOM: `<div class="catalog_item"><a href="...">` — стили карточки идут на **`> a`**, не на `> div`.  
‡ Legacy base CSS использует `.catalog_item > div`; live markup — **`> a`**. W3ATMOSPHERE покрывает **`> a`** — каталог **не** в зоне selector-miss для cards.

---

## 4. Override conflicts

### Cascade position

| Layer | Approx. lines in `main.css` | Role |
|-------|----------------------------|------|
| Base theme | 1–~6900 | Legacy literals: `rgb(170,3,3)` ×56, `rgb(33,36,43)` ×48, `border-radius:4px` ×68 |
| W3-V | ~6900–7168 | Shadow/radius bridge |
| W3V2 | ~7169–7417 | Token + override block |
| **W3ATMOSPHERE-01** | **7418–7768** | **Last writer** for atmosphere selectors |

**Post-W3ATMOSPHERE rules:** **0** для `body`, `nav`, `four_blocks`. Блок — terminal override layer. ✓

### Known conflict patterns (non-blocking but visually dampening)

| Zone | Issue | Impact on visibility |
|------|-------|----------------------|
| **Body background** | Base `rgb(243,243,245)` (#F3F3F5) → W3V2 `#F7F8FA` → W3ATM `#EEF1F5` | Δ luminance **~2–4%** — почти неразличимо без A/B |
| **Nav/footer** | Already dark `rgb(33,36,43)` since Phase 1 theme; W3 waves add gradient refinement | Оператор видит «тот же тёмный хедер» |
| **Cards** | Legacy `4px` radius + flat border at line 3220/5234; W3ATM `12px` + soft shadow at 7593/7600 | Видимо на `/cars/`, но **тонко** (radius + лёгкая тень) |
| **Legacy literals** | 56× red, 48× dark остаются в base layer | Перебиты только там, где есть W3ATM selector; **patchy zones** остаются (N-01) |
| **W3VIS** | Rolled back 2026-06-09 | PDP hero/CTA hierarchy changes **отсутствуют** — оператор мог ожидать их |

### Media query overrides

| MQ | Effect | Conflicts desktop? |
|----|--------|-------------------|
| `@media (max-width: 991px)` | W3ATM card radius/shadow parity | **No** — additive |
| `@media (max-width: 767px)` | `body` canvas, header shadow, footer gradient, search_form | **No** — reinforces W3ATM |

**Desktop styles не сбрасываются mobile MQ.** ✓

### Extra CSS after theme files?

**None** on any probed page. ✓

---

## 5. Cache status

| Signal | Value | Assessment |
|--------|-------|------------|
| `Cache-Control` on `/css/main.css` | `max-age=604800` (7 days) | Aggressive browser caching |
| `ETag` | `"6a279d2c-1f824"` | Present |
| `Last-Modified` | 2026-06-09 04:57:16 GMT | Matches execution day |
| Cache-bust fetch `?audit=<ts>` | 129 060 bytes, W3ATM present | Server serves **current** CSS |
| OC modification cache (execution) | Cleared 2026-06-09 | No evidence of stale **server** CSS |
| CDN | **SAFE UNKNOWN** — no CDN headers observed | — |

**Server-side cache:** **NOT stale** — live file = post-W3ATMOSPHERE artifact.  
**Client-side browser cache:** **POSSIBLE RISK** — оператор, не сделавший hard refresh после upload, может видеть pre-W3ATMOSPHERE CSS до 7 суток. Требует operator verification (Ctrl+F5 / disable cache in DevTools).

---

## 6. Why operator sees no meaningful change

### Technical facts (CSS **is** working)

1. Правильные файлы на TEST, правильный размер, маркеры на месте.
2. W3ATMOSPHERE — последний слой каскада; конфликтующих post-rules нет.
3. Ключевые селекторы (header, footer, body, catalog `> a`, PDP widgets) **присутствуют в HTML** на соответствующих маршрутах.
4. Нет `<style>` injection и нет CSS после main/media.

### Perceptual facts (why it **looks** the same)

| Factor | Explanation |
|--------|-------------|
| **Incremental waves** | W3-V (2026-06-09) → W3V2 → W3UX-C1 → W3ATMOSPHERE — каждая волна сдвигает палитру на **единицы % luminance**, не на контрастный скачок |
| **Already-grey baseline** | До W3ATM body base уже `rgb(243,243,245)` — не белый лист; canvas `#EEF1F5` — косметический шаг |
| **Dark chrome unchanged in perception** | Nav/footer были тёмными с Phase 1; gradients и 1px seams **не читаются** как «новый дизайн» |
| **Card delta subtle** | 4px → 12px radius + soft graphite shadow — заметно в A/B, **слабо** в памяти оператора |
| **W3VIS rollback** | Более заметные PDP/hero изменения **сняты** по operator directive |
| **W3WF-01 not executed** | Impact map уже фиксировал LOW–MEDIUM delta vs current TEST — оператор мог ожидать большего от **следующей** волны, которой ещё не было |
| **Screenshot baseline** | Execution screenshots: TEST domain, desktop 1280 / tablet 768 / mobile 375 — если operator screenshot с **другого URL/viewport**, сравнение некорректно (**VERIFY**) |

### Screenshot / domain / viewport check (item 8)

| Check | Status |
|-------|--------|
| TEST domain `sibcar.new-site.space` | **Confirmed** in all execution reports and live probe |
| Production domain | **Not probed** — if operator viewed PROD, changes would be absent (**SAFE UNKNOWN** without operator confirmation) |
| Viewport parity | Execution used 1280/768/375; operator screenshot viewport **UNKNOWN** |
| QA evidence path | `projects/ocpilot/sites/site-001/qa/w3atmosphere-01-screenshots/` (24 files before/after) |

---

## 7. Root cause verdict

| Category | Ruled in/out | Evidence |
|----------|--------------|----------|
| CSS not loaded | **RULED OUT** | HTTP 200; markers; byte match |
| CSS overridden | **RULED OUT** | W3ATM terminal block; no post-rules; main/media last |
| Selectors wrong | **PARTIAL / MINOR** | `.catalog_item > div` ≠ DOM; **`> a` covers catalog**; page-specific MISS = absent markup |
| Changes too weak | **PRIMARY** | 2–4% canvas Δ; soft shadows; dark chrome already present |
| Cache issue | **SECONDARY (client)** | Server fresh; 7-day browser cache risk |
| Mixed cause | **VERDICT** | **YES** — weak deltas + expectation gap + optional client cache |

---

## 8. Exact corrective action

**No implementation in this audit.** Recommended operator/OCPilot sequence:

### A. Immediate verification (operator, 10 min)

1. Open **exactly** `https://sibcar.new-site.space/` (not production).
2. Hard refresh: Ctrl+Shift+R / clear site data for `sibcar.new-site.space`.
3. DevTools → Network → disable cache → reload → confirm `/css/main.css` **129 060 bytes** and response contains `W3ATMOSPHERE-01`.
4. Side-by-side: `qa/w3atmosphere-01-screenshots/before-desktop-homepage.png` vs `after-desktop-homepage.png` at **1280px** width.

### B. Expectation reset (program, before any new wave)

1. **STOP** all new design / atmosphere CSS waves (per operator directive) until expectation workshop complete.
2. Acknowledge: CSS-only atmosphere charter **cap ~6/10** vs Phase 1; **not** «другой сайт».
3. W3VIS rollback means **no PDP hero transformation** — do not expect it from W3ATMOSPHERE.

### C. If operator confirms fresh CSS but still «no change» (next authorized wave only)

Choose **one** path — **not** both:

| Path | Action | Outcome |
|------|--------|---------|
| **C1 — Honest consolidation** | W3WF-01 per Website Factory brief (legacy literal purge, `--wf-*`) | LOW–MEDIUM delta vs **current** TEST; closes patchy zones |
| **C2 — Structural expectation** | New charter **outside** CSS-only atmosphere (typography, spacing, hero, layout) | Required if operator wants «совсем иначе» |

### D. Explicitly **forbidden** as corrective action

- Новая atmosphere-волна «на глаз»
- Ещё один incremental token tweak без A/B acceptance bar
- Production deploy
- Cache clear on server **unless** operator verification proves stale server artifact (currently **not indicated**)

---

## Audit checklist (task items 1–10)

| # | Check | Result |
|---|-------|--------|
| 1 | main.css = edited TEST file? | **PASS** |
| 2 | media.css = edited TEST file? | **PASS** |
| 3 | W3V2 / W3ATMOSPHERE markers live? | **PASS** |
| 4 | W3ATMOSPHERE selectors in live HTML? | **PASS** (page-specific MISS expected) |
| 5 | New rules overridden by older? | **PASS** — terminal W3ATM layer |
| 6 | Media queries override desktop? | **PASS** — reinforce only |
| 7 | Stale CSS cache? | **Server NO** · **Browser POSSIBLE** |
| 8 | Screenshots same domain/viewport? | **Execution YES** · **Operator UNKNOWN** |
| 9 | CSS after main/media? | **PASS** — none |
| 10 | Changes too weak even if applied? | **YES** — primary perceptual cause |

---

## Authorization state

| Action | Status |
|--------|--------|
| New design / atmosphere CSS | **STOPPED** per operator directive |
| Implementation / FTP / cache clear | **NOT AUTHORIZED** by this audit |
| Git commit / push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |

**Next gate:** Operator hard-refresh verification + expectation workshop → then choose C1 or C2 above.

# LIVE SEMANTIC ACCEPTANCE B–F v1 — Phase 3E.1.1

**Status:** B–F delivered and storage-verified; **operator visual acceptance PENDING**  
**Verdict remains:** `COMPLETE — PARSER READY; OPERATOR SEMANTIC ACCEPTANCE PENDING`

Fixture A: **OPERATOR VISUAL PASS** (earlier; not resent).

---

## Contour (unchanged)

| Item | Value |
|------|-------|
| Operational.dev | `xSnXPy8cEHoZw6xG` active, 45 nodes |
| Admin.dev | `wLrLp4WQHm1VJmxz` active, 59 nodes |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` inactive |
| Parser | `sm-parser-v3.3` |
| Message format | `sm-msg-v2.3` |
| Gmail intake | sole `Gmail Fetch Leads` |
| AI / OpenRouter | OFF |
| Eligible recipients | 2 (admin + moderator) |
| Access roles | Андрей=admin/active; Мопс=moderator/active; Оля/Никита=revoked |

Parser code not redesigned this wave. No workflow copies. No role changes.

---

## Pacing / rate-limit

| Item | Result |
|------|--------|
| Injection mode | one fixture at a time |
| Inter-fixture pause | ≥55s after storage+dup polls |
| Sheets rate-limit during B–F | **none** |
| Prior rapid-seq failure (Phase 3E.1) | documented; remediated by pacing |
| Retries needed | none for B–D,F; E storage OK (harness nameVisible false-positive only) |

---

## Delivery matrix (runtime)

| Key | Marker | RAW | CLEAN | LEAD_DELIVERIES | sendOk | dup polls | website_state | resolved_service |
|-----|--------|-----|-------|-----------------|--------|-----------|---------------|------------------|
| A | (prior) | — | — | — | 2 | 0 | provided | Audit — **visual PASS** |
| B | `PHASE_3E1_B_NO_SITE_WEBSITE_DEVELOPMENT` | 1 | 1 | 2 | 2 | 0 | explicitly_absent | WebsiteDevelopment |
| C | `PHASE_3E1_C_WEBSITE_THEN_SEO` | 1 | 1 | 2 | 2 | 0 | explicitly_absent | WebsiteDevelopmentSEO |
| D | `PHASE_3E1_D_TELEGRAM_ALTERNATIVE_CONTACT` | 1 | 1 | 2 | 2 | 0 | alternative_contact | NeedsClarification |
| E | `PHASE_3E1_E_TEST_NAME_PRESERVATION` | 1 | 1 | 2 | 2 | 0 | provided | Audit (form-context fallback) |
| F | `PHASE_3E1_F_ONE_LINE_FALLBACK` | 1 | 1 | 2 | 2 | 0 | provided | SEO |

Delivery statuses for B–F: `delivered` ×2 each. Buttons on all: `✅ Обработано` / `🚫 Спам`.

Synthetic Gmail `Add Gmail PROCESSED` may return Bad Request for non-Gmail ids — expected; not a parser defect.

---

## Operator visual acceptance packet

### Fixture A (already PASS)

- Valid site; interest `Аудит`; comment/form separated; `🧪 Тестовая заявка`; two lifecycle buttons; no duplicate delivery.

### Fixture B — explicit no site + website development

| Field | Expected / observed |
|-------|---------------------|
| Marker | `PHASE_3E1_B_NO_SITE_WEBSITE_DEVELOPMENT` |
| Source website field | `нет сайта` |
| Source comment | `хочу сайт` |
| website_state | `explicitly_absent` |
| Resolved service | `Разработка сайта` |
| Visible site | `Сайт: отсутствует` (no URL) |
| Visible comment | `хочу сайт` (separate) |
| Form context | `Бесплатный аудит` (+ source page) |
| Quality | `Тестовая заявка` |
| Next step | exclude from production statistics |
| First reply | omitted (probable test); does **not** ask for existing site |
| Recipients | exactly 2 (admin+moderator); duplicates=0 |

**Visual checks:** no-site presentation; Website Development; no request for current site.

### Fixture C — no site + website then SEO

| Field | Expected / observed |
|-------|---------------------|
| Marker | `PHASE_3E1_C_WEBSITE_THEN_SEO` |
| Source website field | `сайта пока нет` |
| Source comment | `надо сделать сайт, а потом его продвигать` |
| website_state | `explicitly_absent` |
| Resolved service | `Разработка сайта + SEO` |
| Request summary | both stages (site then SEO) |
| Visible site | `Сайт: отсутствует` |
| Visible comment | customer text only (no form-title concat) |
| Missing info | business / scope / region·goals (not existing URL) |
| Recipients | 2; duplicates=0 |

**Visual checks:** Website Development + SEO; both stages acknowledged; no existing-site ask.

### Fixture D — Telegram alternative contact

| Field | Expected / observed |
|-------|---------------------|
| Marker | `PHASE_3E1_D_TELEGRAM_ALTERNATIVE_CONTACT` |
| Source website field | `t.me/synth_delta_contact` |
| website_state | `alternative_contact` |
| alternative_contact_type | `telegram` |
| Visible site | **not** under `Сайт`; Telegram block separate |
| Resolved service | `Требует уточнения` |
| Comment | Telegram preference + unclear task |
| Recipients | 2; duplicates=0 |

**Visual checks:** Telegram as contact, not website.

### Fixture E — name `test` preserved

| Field | Expected / observed |
|-------|---------------------|
| Marker | `PHASE_3E1_E_TEST_NAME_PRESERVATION` |
| client_name_raw / normalized | `test` / `test` |
| Visible name | `test` (not deleted) |
| is_probable_test | true → `🧪 Тестовая заявка` |
| Not auto-spam | lifecycle still pending + both buttons |
| Resolved service | `Аудит` (form-context fallback; allowed) |
| First reply | omitted (test) |
| Recipients | 2; duplicates=0 |

**Visual checks:** name `test` visible; test badge visible.

### Fixture F — one-line collapsed fields

| Field | Expected / observed |
|-------|---------------------|
| Marker | `PHASE_3E1_F_ONE_LINE_FALLBACK` |
| Name / contact | extracted separately |
| website_state | `provided` |
| Comment | `нужно SEO-продвижение` (no `Отправлено со` bleed) |
| Resolved service | `SEO` |
| First reply | omitted (test); does not re-ask site |
| Recipients | 2; duplicates=0 |

**Visual checks:** fields separated; SEO service; no source-label contamination of comment.

---

## Regression checklist (runtime)

1–12 semantic invariants for B–F: PASS (API/card previews)  
13 valid-site reply does not ask for site: PASS (A prior; F no ask)  
14–15 form/source separation: PASS  
16 buttons present: PASS on all pending B–F  
17 exactly two recipient copies: PASS  
18 later polls zero duplicates: PASS (3 polls × fixture)  
19–21 RAW=1 / CLEAN=1 / LEAD_DELIVERIES=2: PASS  
22 callbacks unchanged: PASS (no Admin patch)  
23–25 `/leads` `/my_status` `/moderator_pending`: not re-exercised this wave; Admin graph untouched — **SAFE UNKNOWN** until operator spot-check  
26 AI calls=0  
27 client messages=0  
28 workflows created=0  

---

## Safety counters

- AI provider calls = 0  
- automatic client messages = 0  
- workflows created = 0  
- access-role changes = 0  
- Fixture A resent = 0  
- lifecycle buttons pressed by harness = 0  
- parser redesign = 0  

---

## Operator stop point

Do **not** mark PHASE 3E.1 fully COMPLETE until Telegram cards B–F are visually confirmed by the operator (Андрей / Мопс).

Remaining actions:

1. Open Telegram cards for markers B–F  
2. Confirm the five visual check groups above  
3. Optionally spot-check `/leads`, `/my_status`, `/moderator_pending`  
4. Do not press lifecycle buttons unless intentional for a separate charter  

After confirmation, allowed upgrade: `PHASE 3E.1 COMPLETE — PARSER 3.3 AND LEAD SEMANTIC MODEL READY`.

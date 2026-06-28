# CORVONERO Phase 7A — LP-01 Implementation Inputs v1

**Page:** LP-01 — Программист / специалист 1С  
**Phase:** 7A staging build  
**Status:** Tracking sheet — values marked **SAFE UNKNOWN** until operator supplies

These items are **not** public-copy authority. They do not authorize copy changes.

---

## Messenger URLs

| Channel | Required for publication | Staging treatment | URL value | Verified |
|---------|-------------------------|-------------------|-----------|----------|
| MAX | Yes — or hide channel by operator decision | Label + icon; link disabled / «awaiting URL» in builder notes | **SAFE UNKNOWN** | [ ] |
| Telegram | Yes — or hide channel by operator decision | Label + icon; link disabled / «awaiting URL» in builder notes | **SAFE UNKNOWN** | [ ] |
| WhatsApp | Yes — or hide channel by operator decision | Label + icon; link disabled / «awaiting URL» in builder notes | **SAFE UNKNOWN** | [ ] |

**Rules for Roman at staging:**

- Show all three visually.
- Do not use `#` as a publicly clickable destination.
- Do not invent deep links or bind all channels to phone without explicit confirmation.
- Before publication: each channel needs **VERIFIED URL** or explicit operator decision to hide.

---

## Form and legal

| Input | Staging | Before publication | Value | Verified |
|-------|---------|-------------------|-------|----------|
| Privacy policy URL | Prepare placeholder in builder notes | Required live link in consent + footer | **SAFE UNKNOWN** | [ ] |
| Personal-data consent checkbox text | Optional hidden/disabled at staging | Required approved legal wording | **SAFE UNKNOWN** | [ ] |
| Form recipient (email/CRM/integration) | Do not route to production recipient | Required verified recipient | **SAFE UNKNOWN** | [ ] |
| Form success message | May use handoff implementation text in builder preview only | Operator-approved live text | See Tilda handoff v3 implementation text | [ ] |
| Form error message | May use handoff implementation text in builder preview only | Operator-approved live text | See Tilda handoff v3 implementation text | [ ] |
| Spam protection | Not required for unpublished draft | Required at publish | **SAFE UNKNOWN** | [ ] |
| Test submission authorization | **NOT AUTHORIZED** in Phase 7A unless separately approved | Required before go-live | N/A | [ ] |

**Handoff implementation text (not public-copy authority):**

- Success: «Спасибо! Мы получили заявку и перезвоним по указанному телефону.»
- Error: «Не удалось отправить заявку. Проверьте телефон или позвоните нам: +7 (383) 390-29-28.»

---

## Legal entity verification (ATLAS LE-0006)

Source: `projects/atlas/population/ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md` — **E0 partial** (operator intake; no E2 registry extract).

| Field | Canonical evidence | LP-01 visible minimum | Match check |
|-------|-------------------|----------------------|-------------|
| Legal name | ИП Никифоров Роман Вадимович | ИП Никифоров Роман Вадимович | [ ] |
| ИНН | 540200831636 | Not required visible on LP-01 staging | [ ] |
| ОГРНИП | 324547600100482 | Not required visible on LP-01 staging | [ ] |
| Registration date | 2024-06-14 | Not on page | — |
| Phone | +7 (383) 390-29-28 | +7 (383) 390-29-28 | [ ] |
| Brand | Центр автоматизации «Корво Неро» | Footer brand line | [ ] |

**Do not publish legal details that conflict with canonical evidence.** Full requisites in footer beyond visible minimum line — operator decision at publish.

**VAT:** Do not mention.

---

## SEO and assets

| Input | Staging | Before publication | Value | Verified |
|-------|---------|-------------------|-------|----------|
| OG image | Prepare slot in page settings | Required asset | **SAFE UNKNOWN** | [ ] |
| Favicon | Reuse site default if available | Confirm matches site | Site default | [ ] |
| Canonical URL | Prepare `/programmist-1s/` | Self-referencing at publish | `/programmist-1s/` | [ ] |
| Indexation | **Disabled** | Operator decision at publish | Disabled (staging) | [ ] |
| Sitemap inclusion | Off while unpublished | At publish | Deferred | [ ] |
| OG title | Match page Title | At publish | Per manifest | [ ] |
| OG description | Match meta Description | At publish | Per manifest | [ ] |

---

## Tilda access

| Input | Value | Verified |
|-------|-------|----------|
| Tilda project access (Roman) | Operator-provided | [ ] |
| Tilda draft page name | **RECORD AFTER BUILD** | [ ] |
| Tilda page ID | **RECORD AFTER BUILD** | [ ] |
| Preview method | Editor preview or private preview URL if available | [ ] |

---

## Analytics (deferred — names only)

Do not create or modify production Metrika goals in Phase 7A.

| Event name | Trigger | Installed |
|------------|---------|-----------|
| `lp01_phone_click` | tel: link click | [ ] Deferred |
| `lp01_cta_discuss_click` | «Обсудить задачу» | [ ] Deferred |
| `lp01_cta_estimate_click` | «Получить оценку» | [ ] Deferred |
| `lp01_callback_submit` | Form submit success | [ ] Deferred |
| `lp01_max_click` | MAX icon/label click | [ ] Deferred |
| `lp01_telegram_click` | Telegram icon/label click | [ ] Deferred |
| `lp01_whatsapp_click` | WhatsApp icon/label click | [ ] Deferred |

Call tracking number: **SAFE UNKNOWN** — use canonical phone until operator provides DID.

---

## Protected surfaces (do not modify in Phase 7A)

| URL | Action |
|-----|--------|
| `https://lk.corvonero.ru/` (existing pages) | Do not replace or break |
| `https://corvonero.ru/` | Do not modify |
| Tilda global styles affecting other pages | Avoid |

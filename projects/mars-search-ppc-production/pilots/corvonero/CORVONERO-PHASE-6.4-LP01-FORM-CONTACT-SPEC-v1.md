# CORVONERO Phase 6.4 — LP-01 Form and Contact Specification v1

**Landing page:** LP-01  
**Platform (planned):** Tilda  
**Status:** Planning specification — **not implemented**

---

## Form fields

| Field ID | Label (RU) | Type | Required | Validation |
|----------|------------|------|----------|------------|
| `name` | Имя | text | **No** | Optional; max length reasonable for Tilda default |
| `phone` | Телефон | tel | **Yes** | Russian phone format; mask recommended at implementation |

**Prohibited:** company, email, comment, configuration as required hidden fields in LP-01 v1.

---

## CTA buttons (page-wide)

| Label | Role | Typical placement |
|-------|------|-------------------|
| **Обсудить задачу** | Primary commercial CTA | First screen, trust block, final CTA |
| **Получить оценку** | Secondary — price/scope intent | Service scope, configurations, pricing |
| **Заказать звонок** | Callback / form-adjacent | Work format, process, form submit |

All three labels must appear on the page. Do not invent additional CTA wording.

---

## Messengers

| Channel | Label | Link status | Notes |
|---------|-------|-------------|-------|
| **MAX** | MAX | **LINK_REQUIRED** | URL: `REQUIRED_FROM_OPERATOR_OR_CLIENT` |
| **Telegram** | Telegram | **LINK_REQUIRED** | URL/username: `REQUIRED_FROM_OPERATOR_OR_CLIENT` |
| **WhatsApp** | WhatsApp | **LINK_REQUIRED** | URL/phone binding: `REQUIRED_FROM_OPERATOR_OR_CLIENT` |

**Rules:**

- Represent all three visually (icon + label minimum).
- Do not fabricate deep links or phone bindings.
- Until links provided: use placeholder href `#` with `data-placeholder="messenger-link"` or disable click with operator-visible TODO — **not** fake working URLs.

---

## Phone

| Requirement | Specification |
|-------------|---------------|
| Number | +7 (383) 390-29-28 |
| Click-to-call | `tel:+73833902928` on mobile and desktop |
| Visibility | First screen + contact block + footer |
| Format display | +7 (383) 390-29-28 |

---

## Consent / privacy

| Requirement | Status |
|-------------|--------|
| Consent checkbox before submit | **Required** |
| Legal text | `REQUIRED_FROM_OPERATOR_OR_CLIENT` — do not invent PD processing wording |
| Privacy policy link | `CURRENT_LINK_SAFE_UNKNOWN` — link to published policy when confirmed |

---

## Form states

### Success

**Message (draft — operator may edit tone):**  
«Спасибо! Мы получили заявку и перезвоним по указанному телефону.»

### Error

**Message (draft):**  
«Не удалось отправить заявку. Проверьте телефон или позвоните нам: +7 (383) 390-29-28.»

---

## Mobile behavior

- Form fields full-width; minimum tap target 44px.
- Phone field triggers numeric/tel keyboard.
- Primary CTA sticky or repeated after first screen — recommended, not mandatory in v1 spec.
- Click-to-call phone prominent in header or first screen.
- Messenger icons in row; wrap on narrow viewports.

---

## Analytics event names (planning recommendations)

| Event name | Trigger |
|------------|---------|
| `lp01_form_submit` | Successful form submission |
| `lp01_form_error` | Form validation or server error |
| `lp01_phone_click` | tel: link click |
| `lp01_cta_discuss_task` | «Обсудить задачу» click |
| `lp01_cta_get_estimate` | «Получить оценку» click |
| `lp01_cta_request_call` | «Заказать звонок» click |
| `lp01_messenger_click` | Messenger icon click (parameter: channel) |

**Note:** Event wiring is launch-prep — not implemented in Phase 6.4.

---

## Call tracking (planning)

- Dedicated call-tracking number: **SAFE UNKNOWN** — use canonical +7 (383) 390-29-28 until operator provides tracking DID.
- Document swap procedure at launch prep.

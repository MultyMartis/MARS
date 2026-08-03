# WEBSITE FORM FORMATS v1

**Product:** i-SEO Sales Manager Bot  
**Purpose:** registry of known website form email formats for parser alignment and multi-form test planning  
**Rule:** synthetic field examples only — **no real client data**

---

## 1. How to use this registry

| Column | Meaning |
|--------|---------|
| `form_slug` | Normalized page key (`SOURCE-PAGE-NORMALIZATION-v1`) |
| `form_title` | Human label from email subject or form name |
| `service_default` | Expected `service` when no override |
| `field_labels` | Russian labels expected in email body |
| `parser_notes` | v3.2+ behavior specific to this form |
| `fixture_id` | Harness / test reference |
| `status` | `defined` · `placeholder` · `retired` |

Add one form per iteration — see `evidence/phase3d4/MULTI-FORM-TEST-PLAN-v1.md`.

---

## 2. Defined forms

### 2.1 free-audit

| Field | Value |
|-------|-------|
| **form_slug** | `free-audit` |
| **form_title** | Заявка на бесплатный аудит |
| **service_default** | Audit |
| **typical source_page raw** | `/free-audit/` |
| **status** | **defined** · Phase 3D.4 accepted |
| **fixture_id** | supplied-form-synth-alpha (see `SUPPLIED-FORM-END-TO-END-v1.md`) |

**Expected field labels (RU):**

| Label | Maps to |
|-------|---------|
| От кого / Имя | `client_name` |
| Способ связи | contact method hint |
| Контакт | primary contact value |
| Телефон | `phone` |
| Email / E-mail / Почта | `email` |
| Адрес сайта / Сайт | `site` (not `t.me` — v3.2) |
| Комментарий / Сообщение | `request_text` + comment semantics |
| Отправлено со страницы | `source_page` |

**Parser notes (v3.2):**

- «Заявка на бесплатный аудит» reinforces Audit service.
- `t.me/…` in site field → messenger, not site.
- «в тг» in comment reinforces Telegram preference.
- Page normalizes to `free-audit`.

**Synthetic minimal example:**

```text
От кого: Synth User
Способ связи: email
Контакт: synth@example.com
Адрес сайта: synth-example.ru
Комментарий: нужен аудит главной
Отправлено со страницы: /free-audit/
```

---

## 3. Placeholder forms (not yet implemented)

### 3.1 seo

| Field | Value |
|-------|-------|
| **form_slug** | `seo` |
| **form_title** | *(TBD — SEO consultation form)* |
| **service_default** | SEO |
| **typical source_page raw** | `/seo/` |
| **status** | **placeholder** |
| **fixture_id** | — |

**Expected field labels:** same core set as §2.1 (audit labels may differ — confirm on first real sanitized sample).

**Parser notes:** defer until first iteration chartered.

---

### 3.2 direct

| Field | Value |
|-------|-------|
| **form_slug** | `direct` |
| **form_title** | *(TBD — Yandex Direct / context ads form)* |
| **service_default** | Direct |
| **typical source_page raw** | `/direct/` or `/kontekstnaya-reklama/` |
| **status** | **placeholder** |
| **fixture_id** | — |

---

### 3.3 site-build

| Field | Value |
|-------|-------|
| **form_slug** | `site-build` |
| **form_title** | *(TBD — site development form)* |
| **service_default** | Site |
| **typical source_page raw** | `/sozdanie-sajta/` |
| **status** | **placeholder** |
| **fixture_id** | — |

---

### 3.4 callback

| Field | Value |
|-------|-------|
| **form_slug** | `callback` |
| **form_title** | *(TBD — callback / call-me form)* |
| **service_default** | Other |
| **typical source_page raw** | `/callback/` or `/zayavka/` |
| **status** | **placeholder** |
| **fixture_id** | — |

**Parser notes:** expect phone-first contact; minimal comment.

---

### 3.5 calculator

| Field | Value |
|-------|-------|
| **form_slug** | `calculator` |
| **form_title** | *(TBD — audit/SEO calculator widget)* |
| **service_default** | Audit or SEO (context-dependent) |
| **typical source_page raw** | `/kalkulyator/` |
| **status** | **placeholder** |
| **fixture_id** | — |

**Parser notes:** may include calc flags in RAW; service disambiguation required.

---

## 4. Cross-form parser rules (all forms)

Applies to every record once implemented:

1. `sm-parser-v3.2` contact method inference (`CONTACT-METHOD-INFERENCE-v1`).
2. Messenger/site split for `t.me` (`MESSENGER-SITE-SEMANTIC-FIX-v1`).
3. Comment preference keywords (`COMMENT-SEMANTICS-v1`).
4. Source page slug normalization (`SOURCE-PAGE-NORMALIZATION-v1`).
5. Placeholder rejection (`44`, `#ERROR!`, `UNKNOWN`, …).

---

## 5. Change control

- Update this registry **before** parser patches for a new form.
- One form slug per deployment iteration.
- Do not store real submissions in git — use synthetic fixtures under `implementation/parser-fixtures/`.

---

*Related: evidence/phase3d4/MULTI-FORM-TEST-PLAN-v1.md · evidence/phase3d4/SUPPLIED-FORM-END-TO-END-v1.md.*

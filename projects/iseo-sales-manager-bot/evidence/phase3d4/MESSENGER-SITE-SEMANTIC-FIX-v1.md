# MESSENGER SITE SEMANTIC FIX v1

**Phase:** 3D.4  
**Parser version:** **`sm-parser-v3.2`**

---

## 1. Problem

Website-form payloads sometimes place a Telegram contact (`t.me/…`, `@handle`) in the **«Адрес сайта»** field. Parser v3.1 treated any URL-like token as `site`, producing cards with:

```text
Сайт: t.me/example_handle
```

Managers copied the wrong field; contact method inference was confused.

---

## 2. Fix rule (v3.2)

| Input pattern | v3.1 assignment | v3.2 assignment |
|---------------|-----------------|-----------------|
| `https://t.me/username` | `site` | **`messenger`** (Telegram) |
| `t.me/username` | `site` | **`messenger`** |
| `@username` in site field | often `site` or dropped | **`messenger`** |
| `example.ru`, `www.example.ru` | `site` | **`site`** (unchanged) |
| `https://example.ru/path` | `site` | **`site`** (unchanged) |

**Site field** must represent a **web property**, not a messenger deep link.

---

## 3. Detection signals

Messenger (Telegram) classification when **any** of:

- host is `t.me` or `telegram.me`
- value starts with `@` and matches handle grammar
- «Способ связи» explicitly says Telegram / «в тг» / «telegram» (see COMMENT-SEMANTICS-v1)

Site classification when:

- host is a non-messenger domain with optional scheme
- path is not exclusively a messenger deep link

---

## 4. Card semantics (after fix)

**Before (v3.1):**

```text
Сайт: t.me/synth_user_01
Контакты: — 
```

**After (v3.2):**

```text
Сайт: —
Контакты: t.me/synth_user_01 (мессенджер)
```

Synthetic example only — no real handles.

---

## 5. CONFIG alignment

| Key | Value |
|-----|-------|
| `parser_version` | **`sm-parser-v3.2`** |

---

## 6. Acceptance

| Fixture class | Result |
|---------------|--------|
| t.me in site field → messenger | PASS |
| Real domain in site field → site | PASS |
| Both site + messenger present | PASS — both fields populated correctly |
| Regression: audit form multiline labels | PASS |
| Regression: formula/placeholder rejection | PASS |

Harness reference: extended F-AF suite + supplied-form end-to-end (`SUPPLIED-FORM-END-TO-END-v1.md`).

---

*Related: CONTACT-METHOD-INFERENCE-v1 · COMMENT-SEMANTICS-v1 · knowledge/WEBSITE-FORM-FORMATS-v1.md.*

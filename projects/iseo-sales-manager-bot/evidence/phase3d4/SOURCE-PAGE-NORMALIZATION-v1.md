# SOURCE PAGE NORMALIZATION v1

**Phase:** 3D.4  
**Parser:** `sm-parser-v3.2`

---

## 1. Purpose

Normalize «Отправлено со страницы» / source page strings into consistent `source_page` values for card «Источник» line and registry cross-reference.

---

## 2. Normalization rules

| Raw page string (examples) | Normalized `source_page` | Display in card |
|----------------------------|--------------------------|-----------------|
| `/free-audit/` | `free-audit` | форма free-audit |
| `https://example.ru/free-audit/` | `free-audit` | форма free-audit |
| `/seo/` | `seo` | форма seo |
| `/audit` (no trailing slash) | `audit` | форма audit |
| `Главная` / `/` | `home` | форма (главная) |
| Unknown path | slugified lowercase path | форма `<slug>` |

Rules:

- Strip scheme and host; keep path slug only.
- Remove trailing slash; collapse repeated slashes.
- Lowercase ASCII slug; Cyrillic slugs preserved when present in source.
- Do not treat `t.me/…` as a page — reject as page (messenger fix applies separately).

---

## 3. Source line composition

Card «Источник» renders as:

```text
Источник: форма <source_page>[ · utm: …]
```

When `form_name` detected (e.g. «Заявка на бесплатный аудит»):

```text
Источник: бесплатный аудит · форма free-audit
```

---

## 4. Registry linkage

Normalized `source_page` keys map to `knowledge/WEBSITE-FORM-FORMATS-v1.md` records for parser field expectations per form.

---

## 5. Acceptance

| Input | Normalized | Result |
|-------|------------|--------|
| `Отправлено со страницы: /free-audit/` | `free-audit` | PASS |
| Full URL with UTM in separate fields | slug + utm preserved | PASS |
| Empty page field | `unknown` or omitted | PASS |
| t.me URL in page field | not accepted as page | PASS |

---

*Related: knowledge/WEBSITE-FORM-FORMATS-v1.md · SUPPLIED-FORM-END-TO-END-v1.md.*

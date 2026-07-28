# I-SEO Report Hub — Report Delivery Client Handoff UX Copy Pack v0.1

**Status:** COPY / POLICY ONLY — no live tokens; no real client data; no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-28  
**Authority:** Operator I-SEO Report Hub Report Delivery Client Handoff UX Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-DESIGN-v0.1.md)

---

## 1. Purpose

Стандартные тексты для ручной отправки клиенту после создания public share link. Язык по умолчанию — **русский**.

Правила:

- no live token in this doc;
- no real client/project names from production;
- placeholders only;
- never include storage paths, `token_hash`, admin URLs, or credentials.

---

## 2. Placeholders

| Placeholder | Meaning |
|-------------|---------|
| `{client_name}` | Client display name |
| `{project_name}` | Project display name |
| `{period}` | Reporting period label (e.g. July 2026 / 2026-07) |
| `{share_url}` | Public share URL shown **once** at create |
| `{expires_at}` | Human-readable expiry datetime |
| `{specialist_name}` | i-SEO specialist display name (optional) |

Example (fixture-safe, not live):

- `{client_name}` → `Demo Client`
- `{project_name}` → `Demo Project`
- `{period}` → `июль 2026`
- `{share_url}` → `https://example.test/share/report/[REDACTED_64HEX_TOKEN]`
- `{expires_at}` → `27 августа 2026, 18:00`
- `{specialist_name}` → `Специалист i-SEO`

---

## 3. Short message (Telegram / WhatsApp / messenger)

```
Здравствуйте! Подготовили отчет по проекту {project_name} за {period}. Скачать PDF можно по ссылке: {share_url}. Ссылка будет доступна до {expires_at}.
```

Optional closing line:

```
Если будут вопросы по отчету — напишите, пожалуйста. {specialist_name}
```

---

## 4. Formal email

**Subject:**

```
Отчет по проекту {project_name} за {period}
```

**Body:**

```
Здравствуйте!

Направляем отчет по проекту {project_name} за {period}.

PDF-файл доступен по защищенной ссылке:
{share_url}

Ссылка действует до {expires_at}.

Если потребуется пояснение по отчету или комментарии по следующему периоду, напишите нам.

С уважением,
{specialist_name}
```

If `{specialist_name}` is empty, end with team signature placeholder:

```
С уважением,
команда i-SEO
```

---

## 5. Internal operator note

Not for client. Use for specialist checklist / chat with team.

```
HANDOFF / INTERNAL
Client: {client_name}
Project: {project_name}
Period: {period}
Export: check id/key/template on handoff panel (styled PDF only)
Share: check id/status/expiry on handoff panel
Expires: {expires_at}
URL: available only on create-success screen (once)
Sent channel: [Telegram | Email | Other]
Sent at: [operator fills manually]
Warnings:
- do not send revoked/expired link
- do not send HTML or legacy export
- do not reconstruct URL from DB
- if URL lost → revoke + recreate share
```

---

## 6. Warnings (must surface near copy UI)

| Warning | When |
|---------|------|
| Public URL is shown only once at share creation | Always on success + revisit |
| If URL was not copied, revoke and create a new share | Revisit without once URL |
| Do not send revoked or expired links | Status not active / past expiry |
| Do not send HTML or legacy PDF exports | Not shareable |
| Never paste storage paths into client messages | Always |
| Never display or copy `token_hash` | Always |

---

## 7. English notes (optional)

English variants are **not** MVP default. If needed later:

- Short: “Hello! Your report for {project_name} ({period}) is ready: {share_url}. Link available until {expires_at}.”
- Keep Russian as primary for current i-SEO clients unless operator requests bilingual pack.

---

## 8. Implementation binding

Implementation 01 should:

1. Render these templates with real context fields at share create success.
2. Provide one-click copy per variant.
3. Leave `{share_url}` blank/disabled when once URL is no longer available.
4. Never persist rendered client messages containing plaintext tokens in DB in no-migration MVP.

# Telegram SIMPLE Templates

**Status:** FROZEN DOCUMENTATION SEMANTICS / PHASE 0A  
**Runtime:** NOT IMPLEMENTED  
**Credentials / chat IDs:** none in this document

---

## 1. Purpose

Deterministic human-readable Telegram rendering from the normalized `mars.client_ops.report` envelope.

- No AI involved in SIMPLE.
- Internal operator routing only for Phase 1.
- Future client copy requires separate approval and separate templates.

---

## 2. Template structure

```text
{site_name} · {site_status}
{event_title}

Baseline: {baseline_count}
Current: {current_count}
Added: {added_urls}
Removed: {removed_urls}
Onboarding needed: {onboarding_needed_count}

Action: {action_text_lower_or_as_documented}
Run: {run_datetime_local}
```

Frozen example shape:

```text
ЗПМ · ATTENTION
Post-1C monitor

Baseline: 1737
Current: 1817
Added: 80
Removed: 0
Onboarding needed: 4

Action: проверить новые ветки каталога
Run: 2026-07-23 12:30
```

---

## 3. Rendering rules

| Rule | Detail |
|------|--------|
| Deterministic | Render only from normalized envelope fields |
| Status match | Header status must equal `run.normalized_status` / site_status exactly |
| Counts exact | Counts must match envelope metrics exactly |
| Action | Derive from `action.text` / `action.code`; do not invent |
| Baseline wording | Use Baseline / Current / Added / Removed — **never** `Sitemap: 1737` as if live-only |
| No secrets | No credentials, tokens, chat IDs |
| No paths | No raw artifact / Storage / runtime-checkout paths |
| No stacks | No stack traces or production infrastructure details |
| No unsupported interpretation | Do not add causal claims beyond envelope |
| Mobile-friendly | Short lines; no wide tables; avoid walls of text |

### Date/time rendering

- Source: prefer `observed_at` (fallback: parse `run.run_id` if documented mapping exists).
- Display format for MVP examples: `YYYY-MM-DD HH:mm` in the observation timezone implied by source (SITE-002 evidence uses +07:00 / Barnaul workstation context).
- Do not invent timezone labels in the message body unless envelope later adds an explicit field.

---

## 4. Send / suppression policy (MVP)

| site_status | Send during MVP? |
|-------------|------------------|
| ATTENTION | **Always send** |
| FAILED | **Always send** |
| BLOCKED | **Always send** |
| OK | **Send during initial validation period** |

- Suppression of routine OK after validation period is a **later operator policy decision**.
- Suppression must **not** be producer-controlled.
- Phase 1 target: **internal operator routing only**.

---

## 5. Deterministic examples

### OK

```text
ЗПМ · OK
Post-1C monitor

Baseline: 1737
Current: 1737
Added: 0
Removed: 0
Onboarding needed: 0

Action: none
Run: 2026-07-20 18:05
```

### ATTENTION

```text
ЗПМ · ATTENTION
Post-1C monitor

Baseline: 1737
Current: 1817
Added: 80
Removed: 0
Onboarding needed: 4

Action: проверить новые ветки каталога
Run: 2026-07-23 12:30
```

### FAILED

```text
ЗПМ · FAILED
Post-1C monitor

Baseline: 1737
Current: 0
Added: 0
Removed: 0
Onboarding needed: 0

Action: проверить сбой монитора / источника
Run: 2026-07-23 12:30
```

Note: FAILED example counts are illustrative only when source evidence supports them; exporters must not invent zeros if metrics are unknown — prefer BLOCKED when metrics are untrustworthy.

### BLOCKED

```text
ЗПМ · BLOCKED
Post-1C monitor

Baseline: 1737
Current: 1817
Added: 80
Removed: 0
Onboarding needed: 4

Action: состояние сайта не подтверждено — проверить исходные артефакты
Run: 2026-07-23 12:30
```

BLOCKED explains that **site state could not be verified**, not that the site itself failed.

---

## 6. Prohibited content

- Raw Storage / runtime paths
- Credentials, tokens, webhook URLs with secrets
- Chat IDs
- Stack traces
- Production host/panel internals
- AI speculation inside SIMPLE block
- Client-facing marketing copy (Phase 1)

---

## 7. Future client-safe copy boundary

Client Telegram copy is **out of Phase 1**. Requires:

- separate operator approval
- separate templates
- separate routing configuration

Do not reuse internal SIMPLE text for clients without that gate.

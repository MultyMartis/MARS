# SANDBOX TEST PLAN v1

**Product:** i-SEO Sales Manager Bot  
**Status:** documented fixtures — **no live Gmail/client contact**

---

## 1. Rules

1. Use synthetic payloads and sandbox Sheets tabs only.
2. Do **not** process real unread Gmail.
3. Do **not** message real clients.
4. Do **not** enable production labels on fixtures.
5. Capture evidence (screenshots / sanitized outputs) per fixture class.
6. AI tests may call provider only in .dev with AI ON — still no client send.

---

## 2. Fixture catalog

| ID | Fixture | Expect |
|----|---------|--------|
| F01 | Phone only | `contact_type=phone`; quality needs_data/poor; reply without name |
| F02 | Email only | email primary; no phone invent |
| F03 | Telegram only | messenger primary |
| F04 | Named audit lead | service Audit; name present |
| F05 | Unnamed audit lead | Audit; missing name questions |
| F06 | SEO lead with site | service SEO; site in card |
| F07 | Direct lead | service Direct |
| F08 | Site lead | service Site |
| F09 | Unknown service | service Other |
| F10 | Calculator lead | `calc_detected`; service from calc/page |
| F11 | Malformed lead | parse_status partial/failed; unusable or error path |
| F12 | Repeated Gmail message id | `duplicate_status=reprocessed`; not “повторный клиент” |
| F13 | Repeat phone | `repeat` + history human date |
| F14 | Same site different contact | `possible` / site_only — not hard repeat |
| F15 | AI valid JSON | merge ok; mode AI |
| F16 | AI invalid JSON | fallback; template reply |
| F17 | AI timeout | fallback |
| F18 | AI forbidden promise | fallback |
| F19 | Sheets failure | ERRORS; no fake success Telegram |
| F20 | Telegram formatting edge (`<`, `&`, long text) | No entity crash; truncated safely |
| F21 | CLEAN ok, Telegram fail | No PROCESSED; ERROR label; incoming preserved; ERRORS row; retry → `reprocessed` |

---

## 3. AI mode matrix

| Mode | Fixtures |
|------|----------|
| AI OFF | F01–F14, F19–F21 |
| AI ON | F15–F18 (+ spot F04/F06) |

Confirm **zero** OpenRouter calls on AI OFF runs (n8n execution evidence).

---

## 4. Admin command tests

| Test | Expect |
|------|--------|
| Unknown command | Exact Russian unknown string |
| Non-admin user | Deny |
| `/ai_on` `/ai_off` | CONFIG flips + audit |
| `/health` AI off | AI probe skipped |
| `/test_lead` in prod env | Refused by default |
| `/test_lead` in dev | Fixture appears in sandbox tabs |

---

## 5. Pass criteria (sandbox exit)

1. All F01–F21 classified Pass/Fail with notes.
2. No client-facing send path exists in graph.
3. RAW has no AI pretence columns filled.
4. CLEAN stores `first_reply_text`.
5. Dedupe distinctions correct for F12–F14.
6. Fallback works for F16–F18.
7. Telegram cards match UX contract samples.

---

## 6. Evidence location (recommended later)

`projects/iseo-sales-manager-bot/evidence/phase-3-sandbox/` — create only when Phase 3 runs (not Phase 2).

---

*Related: N8N-CHANGE-PLAN-v1 · AI-OFF-ON-CONTRACT-v1 · TELEGRAM-UX-CONTRACT-v1.*

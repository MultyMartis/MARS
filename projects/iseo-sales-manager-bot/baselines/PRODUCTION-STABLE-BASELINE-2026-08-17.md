# Sales Manager v2 — Production Stable Baseline 2026-08-17

**STATUS:** PRODUCTION STABLE  
**BASELINE DATE:** 2026-08-17  
**Designation:** Sales Manager v2 — Production Stable Baseline 2026-08-17  
**Product:** i-SEO Sales Manager  
**Evidence:** [evidence/stable-baseline-20260817/](../evidence/stable-baseline-20260817/)  
**Freeze report:** [reports/REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md](../reports/REPORT-iseo-sales-manager-bot-production-stable-baseline-freeze-2026-08-17.md)

This document is the **canonical production truth** for the accepted live contour after operator acceptance of `📄 Исходная заявка`. Historical Phase 2/3A architecture packs and historical reports remain historical; they do not override this baseline where they conflict.

---

## 1. Production workflow identities

| Workflow | ID | Role | Activation |
|----------|----|------|------------|
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | Gmail intake → RAW/CLEAN → Telegram cards | **active** |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | Admin commands, callbacks, reminders, raw source | **active** |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | Inactive reference | **inactive** |
| Sales-Manager-v1 | `cJGoQUqIIHull4p7` | Legacy inactive | **inactive** |

Named Sales Manager workflow count at freeze: **4**. Workflow copy delta for this freeze: **0**. Do not create workflow copies.

Host: `n8n.ai-metacode.com`

---

## 2. AI state

| Signal | Value |
|--------|-------|
| CONFIG `ai_enabled` | `false` |
| Ops node `OpenRouter AI` | **disabled** |
| Processing mode | Deterministic / AI OFF |

---

## 3. Reminder state

| Key | Value |
|-----|-------|
| `pending_reminders_enabled` | `true` |
| `pending_reminder_time` | `10:00` |
| `pending_reminder_timezone` | `Europe/Moscow` |
| Weekday policy | **Monday–Friday only** (`weekend_or_non_weekday` fail-close) |
| Candidate selection | All still-actionable real **pending** leads (Monday includes weekend backlog) |
| Exclude | processed · spam · tests · archive/legacy non-production |
| Lifecycle mutation on reminder | **none** |
| Reminder Schedule Gate hash | `F59DEE0535143CCD` |

### Pending natural observation (freeze-time)

At freeze capture (MSK still **2026-08-16 Sunday** evening):

**STABLE_BASELINE_WITH_PENDING_NATURAL_REMINDER_OBSERVATION**

Expected first natural Monday window: **2026-08-17 10:00 Europe/Moscow**.

This is **not** a reason to classify the contour as unstable when schedule, weekday gate, and reminder regression pass and no production failure is known. Do **not** manually trigger the reminder during freeze.

---

## 4. Gmail intake contract

For **new** Gmail leads:

1. Ops `Gmail Fetch Leads` uses **full message mode** (`simple=false`), not snippet-only authority.
2. Parse Lead `captureFullSourceBody()` captures the full visible body **before** labeled field extraction / normalization.
3. Prefer complete plain text (`textPlain`); HTML fallback uses structure-preserving HTML→text (`<br>` / block closers → newlines; URLs kept).
4. Durable authority for future callback: stored full source in RAW `raw_text` / `source_body_full` path.
5. Snippet is **not** the primary full-source authority when a real body exists; lossy-snippet classification remains.

Parser hash at freeze: `ABF87EE55E3A03C7` · CONFIG `parser_version`: `sm-parser-v3.3`

---

## 5. RAW / CLEAN model

| Layer | Role |
|-------|------|
| **RAW / full source** | Durable original visible Gmail/intake body (wording, order, line/paragraph structure) |
| **CLEAN** | Normalized operational lead for manager card + lifecycle |
| **Telegram CLEAN card** | Interpreted operational representation |

Production model:

`Gmail → durable RAW/full source → CLEAN normalized lead → Telegram manager card`

---

## 6. Raw-source contract (`📄 Исходная заявка`)

| Rule | Contract |
|------|----------|
| Authority | Original visible Gmail/intake source body |
| Rendering | Literal (`buildLiteralRawResponse`) — original wording/order/line structure |
| Cleanup | Minimal privacy / Telegram-safe only |
| Forbidden | Field reconstruction (`Имя:` / `Телефон:` / `Сайт:` artificial labels) |
| Forbidden | CLEAN substitution for the raw body |
| IP | Intentionally omitted from Telegram raw view |
| Lookup | Filtered RAW-by-`lead_id` (not broad RAW read) |
| Legacy | Lossy legacy source classified; READ-only Gmail get by `source_message_id`; no ingestion replay; no Gmail state mutation; bounded recovered-source cache allowed where proven |
| Lifecycle | Viewing raw source does **not** mutate lead lifecycle |

Handle Callback hash at freeze: `896596A542F9F746`

---

## 7. Callback identity and lifecycle actions

Telegram card actions (production):

- ✅ Обработано
- 🚫 Спам
- 📄 Исходная заявка

Lifecycle actions (processed / spam) remain on the Admin callback contour. Raw callback is read/display only relative to manager status.

---

## 8. Dedupe / delivery guards

Operational contour retains:

- `Classify Duplicate` and related dedupe classification
- Telegram delivery / `tg_attempts` style guards (`Telegram Result Gate`, delivery stamp/finalize nodes)

No change in this freeze phase.

---

## 9. Known operational boundaries

1. First natural Monday reminder after weekday-gate enablement may still await natural execution/acceptance at freeze time — record as pending observation, not instability.
2. Acceptance-only TMP tooling may exist under `X:\AI MARS STORAGE\incoming\…` for forensics; it is **not** authoritative production runtime.
3. Sales-Manager-v2 remains inactive reference; do not reactivate without a new explicit phase.
4. MARS repo documents the contour; n8n remains execution truth.

---

## 10. Stable acceptance evidence

| Item | Result |
|------|--------|
| Operator live raw UX acceptance | **Accepted** (visual) on safe lead ref `LEAD_4CC52CE3F311` |
| Literal PII/body in Git | **Not stored** |
| Live preflight | `SM_STABLE_PREFLIGHT_PASS` |
| No functional drift | `SM_STABLE_NO_DRIFT_PASS` |
| Regression R1–R27 | `SM_STABLE_REGRESSION_PASS` |
| Freeze boundary | `SM_STABLE_FREEZE_BOUNDARY_PROVEN` |

Supporting phase evidence (historical, not rewritten): lossless Gmail source 2026-08-17, literal raw 2026-08-16, weekend reminder/raw UX 2026-08-16.

---

## 11. Freeze boundary

After this baseline:

- Ordinary work treats the live contour as **stable**.
- Any behavior change starts as a **new explicit phase**.
- No experimental reconstruction paths; no TMP acceptance wrappers as production dependencies.
- Do not leave active TMP workflows as production runtime.

---

## 12. Release marker

Canonical marker = **this document + Git commit hash** on `origin/mars/canonical-post-recovery`.  
No subsystem-specific Sales Manager Git tag convention is established for stable freezes; **no Git tag** is created for this freeze.

---

*Frozen 2026-08-17. Supersedes “planned / Phase 3A next” statements in older project index/README where they contradict live PRODUCTION STABLE status.*

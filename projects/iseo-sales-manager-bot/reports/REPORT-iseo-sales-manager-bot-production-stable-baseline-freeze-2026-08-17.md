# REPORT тАФ Sales Manager v2 Production Stable Baseline Freeze

**Date:** 2026-08-17  
**Phase:** Sales Manager v2 тАФ Production Stable Baseline Freeze  
**Contour:** Operational.dev + Admin.dev (Sales-Manager-v2 inactive)  
**Readiness:** PRODUCTION_STABLE_BASELINE_FROZEN

## 1. Verdict

The accepted i-SEO Sales Manager production contour is frozen as **PRODUCTION STABLE**. Live preflight, no-drift, and non-destructive regression all passed. Canonical baseline docs and sanitized evidence were committed and pushed via a clean worktree without touching foreign MAIN WIP. First natural Monday reminder remains a pending observation only (MSK was still Sunday evening at freeze capture).

## 2. Stable Designation

Sales Manager v2 тАФ Production Stable Baseline 2026-08-17

**STATUS:** PRODUCTION STABLE

## 3. Production Live State

| Workflow | ID | State |
|----------|-----|-------|
| Operational.dev | `xSnXPy8cEHoZw6xG` | **active** ┬╖ 45 nodes |
| Admin.dev | `wLrLp4WQHm1VJmxz` | **active** ┬╖ 100 nodes |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | **inactive** reference |
| Sales-Manager-v1 | `cJGoQUqIIHull4p7` | inactive |

Named count: **4** ┬╖ workflow copy delta: **0** ┬╖ AI: **OFF** ┬╖ host: `n8n.ai-metacode.com`

| Hash | Value |
|------|-------|
| Parse Lead | `ABF87EE55E3A03C7` |
| Handle Callback Action | `896596A542F9F746` |
| Reminder Schedule Gate | `F59DEE0535143CCD` |
| Format Telegram Lead Card | `BE07964BF2433AF6` |
| Ops connection | `0CB507230FD6ADD6990CC7B9FEFB796542F6537004CE8AFBA6FC488BC5B4AE7A` |
| Admin connection | `F7D43E1C33AE926CF5E8A5B4BD7DD981DB73D8DAD66416CE452A5797858C8B42` |

CONFIG (live): `ai_enabled=false` ┬╖ `pending_reminders_enabled=true` ┬╖ `pending_reminder_time=10:00` ┬╖ `pending_reminder_timezone=Europe/Moscow` ┬╖ tests/archive excluded ┬╖ `parser_version=sm-parser-v3.3` ┬╖ `message_format_version=sm-msg-v2.2` ┬╖ `pending_reminder_version=sm-pending-reminder-v1.0`

**Gate:** `SM_STABLE_PREFLIGHT_PASS` ┬╖ `SM_STABLE_PRODUCTION_STATE_CAPTURED`

## 4. Stable Functional Scope

- Gmail тЖТ durable RAW/full source тЖТ CLEAN тЖТ Telegram manager card
- Card actions: тЬЕ ╨Ю╨▒╤А╨░╨▒╨╛╤В╨░╨╜╨╛ ┬╖ ЁЯЪл ╨б╨┐╨░╨╝ ┬╖ ЁЯУД ╨Ш╤Б╤Е╨╛╨┤╨╜╨░╤П ╨╖╨░╤П╨▓╨║╨░
- Filtered RAW-by-lead lookup ┬╖ literal raw renderer ┬╖ legacy READ-only Gmail fallback
- Dedupe + Telegram delivery/`tg_attempts` guards retained
- Reminders MonтАУFri 10:00 Europe/Moscow; all actionable pending (Monday weekend backlog); no lifecycle mutation on reminder or raw click

## 5. Gmail Intake and Full-Source Contract

- Ops `Gmail Fetch Leads`: **`simple=false`** (full message mode)
- Parse Lead `captureFullSourceBody()` before labeled extraction
- Prefer plain text; HTML fallback preserves block/line structure and URLs
- Snippet is not primary full-source authority when a body exists
- Durable source stored for future callback use

**Gate:** `SM_STABLE_NO_DRIFT_PASS` (ND1тАУND5)

## 6. RAW / CLEAN Model

| Layer | Role |
|-------|------|
| RAW / full source | Original visible Gmail/intake body |
| CLEAN | Normalized operational lead |
| CLEAN card | Interpreted operational representation |
| `ЁЯУД ╨Ш╤Б╤Е╨╛╨┤╨╜╨░╤П ╨╖╨░╤П╨▓╨║╨░` | Literal source тАФ no reconstruction, no CLEAN substitute |

## 7. Telegram Card and Actions

Buttons present on production send path: ╨Ю╨▒╤А╨░╨▒╨╛╤В╨░╨╜╨╛ ┬╖ ╨б╨┐╨░╨╝ ┬╖ ╨Ш╤Б╤Е╨╛╨┤╨╜╨░╤П ╨╖╨░╤П╨▓╨║╨░. Processed and spam lifecycle paths remain in Admin Handle Callback. Raw path uses `buildLiteralRawResponse` (no `RS_LABEL_DEFS`).

## 8. Raw Source Acceptance

Operator manually accepted the current `ЁЯУД ╨Ш╤Б╤Е╨╛╨┤╨╜╨░╤П ╨╖╨░╤П╨▓╨║╨░` UX on live exact spam lead ref **`LEAD_4CC52CE3F311`**: separate Telegram message, Gmail-style line breaks and blank paragraphs, original labels, full `t.me/TopPfBot`, `╨Ю╤В╨┐╤А╨░╨▓╨╗╨╡╨╜╨╛ ╤Б╨╛ ╤Б╤В╤А╨░╨╜╨╕╤Ж╤Л`, no artificial `╨Ш╨╝╤П:`/`╨в╨╡╨╗╨╡╤Д╨╛╨╜:`/`╨б╨░╨╣╤В:`, IP omitted, no lifecycle mutation. **Literal PII/body not stored in Git evidence.**

## 9. Reminder Baseline

| Item | Value |
|------|-------|
| Enabled | **true** |
| Schedule | **MonтАУFri 10:00 Europe/Moscow** |
| Weekday gate | active (`weekend_or_non_weekday`) |
| Selection | all still-actionable real pending (Monday weekend backlog) |
| Natural acceptance at report time | **PENDING** тАФ MSK at freeze capture was **2026-08-16 Sunday 20:36**; window **2026-08-17 10:00** not yet reached |
| Label | `STABLE_BASELINE_WITH_PENDING_NATURAL_REMINDER_OBSERVATION` |
| Manual trigger this phase | **0** |

Not classified as contour instability.

## 10. AI State

**OFF** тАФ CONFIG `ai_enabled=false`; Ops `OpenRouter AI` disabled.

## 11. Acceptance Matrix

See [baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md](../baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md). All rows **PASS** except Natural Monday reminder live acceptance = **PENDING OBSERVATION тАФ NOT YET A FAILURE**. No synthetic fills.

**Gate:** `SM_STABLE_ACCEPTANCE_MATRIX_COMPLETE`

## 12. Known Non-Blocking Observations

1. First natural Monday reminder pending observation (expected).
2. Historical already-spam card acceptance used TMP callback filling because production formatter correctly omitted some state-changing callbacks for already-spam entities тАФ acceptance-only, not a production defect.

**Gate:** `SM_STABLE_KNOWN_STATE_DOCUMENTED`

## 13. Workflow Snapshot

Sanitized snapshot: [evidence/stable-baseline-20260817/WORKFLOW-SNAPSHOT.json](../evidence/stable-baseline-20260817/WORKFLOW-SNAPSHOT.json)

Proves: Operational.dev active ┬╖ Admin.dev active ┬╖ Sales-Manager-v2 inactive ┬╖ AI OFF ┬╖ reminder enabled MonтАУFri 10:00 MSK ┬╖ full-source Gmail ┬╖ literal raw ┬╖ filtered lookup ┬╖ legacy fallback nodes present ┬╖ active TMP leftovers **0**.

**Gate:** `SM_STABLE_WORKFLOW_SNAPSHOT_CAPTURED`

## 14. Documentation Reconciliation

Updated current/canonical docs:

- `README.md`, `OPERATIONAL-INDEX.md` тЖТ PRODUCTION STABLE + pointer to baseline
- New canonical baselines under `baselines/PRODUCTION-STABLE-*2026-08-17.md`
- Supersession banners on `architecture/LEAD-DATA-MODEL-v1.md`, `TELEGRAM-UX-CONTRACT-v1.md`, `CONFIGURATION-MODEL-v1.md`
- On canonical remote copies: supersession for stale `PENDING-REMINDER-v1.md` (`enabled=false`) and `DAILY-PENDING-REMINDER-CONTRACT-v1.md` historical soak notes

Historical reports **not** rewritten.

**Gate:** `SM_STABLE_DOCS_RECONCILED`

## 15. Regression

Non-destructive harness R1тАУR27: **27/27 PASS** ┬╖ preflight PASS ┬╖ no-drift PASS ┬╖ freeze boundary PASS. No production Telegram sends, no synthetic leads, no reminder trigger.

Evidence: [evidence/stable-baseline-20260817/REGRESSION.json](../evidence/stable-baseline-20260817/REGRESSION.json)

**Gate:** `SM_STABLE_REGRESSION_PASS`

## 16. Stable Freeze Boundary

- No experimental `RS_LABEL_DEFS` reconstruction in production Handle
- Literal renderer active ┬╖ Gmail `simple=false`
- Active TMP workflow leftovers: **0** (CFG TMP created and deleted during CONFIG read)
- STORAGE local harness is non-authoritative

**Gate:** `SM_STABLE_FREEZE_BOUNDARY_PROVEN`

## 17. Git Canonicalization

| Item | Value |
|------|-------|
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-sm-stable-baseline-20260817\repo` |
| Scoped commit | `35819a63bed132f2ccdb9e2d468e3ec3de9d23fe` (freeze) · tip `edfa536bf338d427a40b2a2e8efdba0fddca44ec` |
| Message | `freeze(iseo-sales-manager): production stable baseline 2026-08-17` |
| Pushed branch | `origin/mars/canonical-post-recovery` |
| Canonical tip after push | `edfa536bf338d427a40b2a2e8efdba0fddca44ec` |
| Foreign MAIN WIP | **untouched** (no pull/reset/clean/stash/restore on dirty MAIN) |

**Gates:** `SM_STABLE_CANONICAL_COMMIT_CREATED` ┬╖ `SM_STABLE_CANONICAL_PUSH_PASS`

## 18. Release Marker

**No Git tag created.** MARS has various product tags, but no established Sales Manager / i-SEO subsystem stable-freeze tag convention. Stable marker = **canonical baseline document + commit hash**.

**Gate:** `SM_STABLE_RELEASE_MARKER_DECISION_PROVEN`

## 19. Privacy / Secrets

No credentials, chat IDs, webhook secrets, full Gmail bodies, or lead PII committed. See [evidence/stable-baseline-20260817/PRIVACY-REVIEW.md](../evidence/stable-baseline-20260817/PRIVACY-REVIEW.md).

**Gate:** `SM_STABLE_PRIVACY_PASS`

## 20. Production Post-State

- Operational.dev **active**
- Admin.dev **active**
- Sales-Manager-v2 **inactive**
- AI **OFF**
- Reminder **enabled** MonтАУFri 10:00 Europe/Moscow
- Workflow copy delta **0**
- Designation: **Sales Manager v2 тАФ Production Stable Baseline 2026-08-17**

## 21. Readiness

PRODUCTION_STABLE_BASELINE_FROZEN

## 22. Final Verdict

COMPLETE тАФ SALES MANAGER V2 IS FROZEN AS `PRODUCTION STABLE BASELINE 2026-08-17`; THE ACCEPTED GMAIL FULL-SOURCE, RAW/CLEAN, TELEGRAM CARD, LITERAL `╨Ш╨б╨е╨Ю╨Ф╨Э╨Р╨п ╨Ч╨Р╨п╨Т╨Ъ╨Р`, LIFECYCLE, DEDUPE AND WEEKDAY REMINDER CONTOURS ARE DOCUMENTED, REGRESSION-CHECKED, CANONICALIZED AND PUSHED WITHOUT TOUCHING FOREIGN MARS WIP

## 23. Next Recommendation

Treat this baseline as stable. Any further Sales Manager behavior change starts as a new explicit phase. Observe the first natural Monday 10:00 MSK reminder if it has not yet occurred.

Do not begin another phase automatically.

---

### Success gates

| Gate | Result |
|------|--------|
| SM_STABLE_PREFLIGHT_PASS | PASS |
| SM_STABLE_NO_DRIFT_PASS | PASS |
| SM_STABLE_BASELINE_DOCUMENTED | PASS |
| SM_STABLE_ACCEPTANCE_MATRIX_COMPLETE | PASS |
| SM_STABLE_KNOWN_STATE_DOCUMENTED | PASS |
| SM_STABLE_WORKFLOW_SNAPSHOT_CAPTURED | PASS |
| SM_STABLE_PRODUCTION_STATE_CAPTURED | PASS |
| SM_STABLE_DOCS_RECONCILED | PASS |
| SM_STABLE_FREEZE_BOUNDARY_PROVEN | PASS |
| SM_STABLE_REGRESSION_PASS | PASS |
| SM_STABLE_CANONICAL_COMMIT_CREATED | PASS |
| SM_STABLE_CANONICAL_PUSH_PASS | PASS |
| SM_STABLE_RELEASE_MARKER_DECISION_PROVEN | PASS |
| SM_STABLE_PRIVACY_PASS | PASS |

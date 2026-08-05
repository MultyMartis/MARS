# FIRST REPLY QUALITY LINTER v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3E.2.1 (Task U)  
**Engine:** First Reply Engine v2.1  
**Implementation:** `lintFirstReply()` in `first-reply-engine-v2.mjs`  
**Fail policy:** any failure → `quality_linter_ok=false` → `first_reply_ready=false` → `first_reply_mode=lint_blocked` → empty `first_reply_text`

---

## Purpose

Post-compose gate before a draft is marked copy-ready. Prevents robotic system phrases, broken structure, and theme/service contradictions from reaching Оля's copy block.

**AI:** OFF. Pure string/regex checks — same class as parser guards.

---

## Required checks

| # | Check | Failure code | Notes |
|---|-------|--------------|-------|
| 1 | Non-empty body (when contact present, not test) | `empty_reply` | Suppressed modes skip compose |
| 2 | Forbidden system phrases | `forbidden_phrase:*` | See [HUMAN-REPLY-STYLE-v1.md](HUMAN-REPLY-STYLE-v1.md) |
| 3 | Max length | `max_chars_exceeded` | Hard cap 900 chars (`FIRST_REPLY_MAX_CHARS`) |
| 4 | Question group count | `too_many_question_groups` | Max 3 (`FIRST_REPLY_MAX_QUESTION_GROUPS`) |
| 5 | Closing block present | `missing_closing` | Must contain `С уважением,` |
| 6 | Unsupported promises | `unsupported_promise` | гарантир, топ-1, 100%, точная стоимость, etc. |
| 7 | Telegram auto-send implication | `telegram_auto_promise` | «напишем вам в Telegram» |
| 8 | Duplicate sentences | `duplicated_sentence` | Naive line-level dedupe (len > 20) |
| 9 | Cart theme acknowledgement | `cart_theme_not_acknowledged` | Theme `conversion_cart` requires конверси/корзин in text |
| 10 | Cart vs generic audit | `generic_audit_used_for_cart_theme` | Blocks page-priority / «результат аудита» for cart |
| 11 | Known website re-ask | `asks_known_website` | `website_state=provided` + URL ask patterns |
| 12 | Absent website re-ask (dev) | `asks_absent_website` | Dev/combo + «пришлите сайт» when explicitly absent |
| 13 | Internal marker leak | `internal_marker_in_draft` | Test harness only when marker injected |

---

## Warnings (non-blocking)

| Warning | Condition |
|---------|-----------|
| `reply_longer_than_target` | Length > 700 (`FIRST_REPLY_TARGET_MAX`) but ≤ 900 |

Warnings populate `first_reply_warnings` but do **not** block `first_reply_ready`.

---

## Outcomes

| Result | Fields |
|--------|--------|
| **PASS** | `quality_linter_ok=true`, `first_reply_ready=true`, `first_reply_text` populated |
| **FAIL** | `quality_linter_ok=false`, `first_reply_ready=false`, `first_reply_mode=lint_blocked`, `first_reply_omitted_reason=quality_linter_failed`, failures in `quality_linter_failures` and `first_reply_reason_codes` as `lint:<code>` |

Manager card should show lint-blocked state — operator copies manually only when `first_reply_ready=true`.

---

## Harness anchors (Phase 3E.2.1 / 3E.2.2)

Phase 3E.2.2 harness H35 requires linter `ok:true` with empty failures for SEO traffic-decline and related human-copy cases.

| ID | Assertion |
|----|-----------|
| H28 / H28b | Forbidden «учли» / system narration absent |
| H29 | ≤3 question groups |
| H30 | No duplicate questions |
| H31 | No duplicate sentences |
| H32 | No unsupported promises |
| H33 | Known-info guards silent in customer text |
| H40 | `quality_linter_ok === true` on happy-path fixtures |

Full matrix: `evidence/phase3e2-1/HARNESS-RESULTS-v1.md`.

---

## Related

- [HUMAN-REPLY-STYLE-v1.md](HUMAN-REPLY-STYLE-v1.md)
- [MEANINGFUL-COMMENT-BRANCHING-v1.md](MEANINGFUL-COMMENT-BRANCHING-v1.md)
- [FIRST-REPLY-ENGINE-v2.md](FIRST-REPLY-ENGINE-v2.md)
- [MANAGER-CARD-v2.4-CONTRACT-v1.md](MANAGER-CARD-v2.4-CONTRACT-v1.md)

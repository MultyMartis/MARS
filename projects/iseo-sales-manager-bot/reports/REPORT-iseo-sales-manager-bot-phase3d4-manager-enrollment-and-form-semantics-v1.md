# REPORT — ISEO SALES MANAGER BOT PHASE 3D.4 MANAGER ENROLLMENT AND MULTI-FORM SEMANTIC UX

**Date:** 2026-08-03  
**Project:** `projects/iseo-sales-manager-bot/`  
**Worktree:** `X:\AI MARS STORAGE\worktrees\iseo-sm-phase3d4-20260803-222440\projects\iseo-sales-manager-bot\`

## 1. Verdict

**COMPLETE — SEMANTICS DEPLOYED, OLYA LIVE CALLBACK PENDING**

Phase 3D.4 delivers Olya manager-action enrollment (CONFIG only, not Admin), role-aware manager `/start`/`/help`, parser **`sm-parser-v3.2`** and formatter **`sm-msg-v2.1`** semantic fixes, free-audit form registry, and full evidence pack. Synthetic harness **30/30 PASS**; live patch and CONFIG enrollment **ok**. Human Telegram confirmation from Olya for `/start`, `/help`, and first live callback tap remains **pending**.

---

## 2. Environment / Preflight

| Check | Result |
|-------|--------|
| Worktree | `X:\AI MARS STORAGE\worktrees\iseo-sm-phase3d4-20260803-222440\` |
| Volume | `X:` label **AI WS** |
| Branch | `tmp/iseo-sm-phase3d4-20260803-222440` |
| Scope | `projects/iseo-sales-manager-bot/` only |
| Host | external n8n (Operational.dev + Admin.dev) |

---

## 3. Scope

1. Olya identity resolution and CONFIG enrollment (`manager_action_user_ids` only).
2. Role authorization model (admin / manager / unauthorized).
3. Role-aware manager `/start` and `/help`.
4. Parser v3.2: messenger/site split, contact inference, comment «в тг», source page normalization.
5. Formatter v2.1: reduced emoji density on manager cards.
6. Supplied free-audit form end-to-end semantics (synthetic).
7. Website form registry + multi-form test plan (one form per iteration).
8. Admin regression (admin count 1, manager count 2, Olya not admin).
9. Documentation, guides, evidence — no new workflow; AI OFF; no client contact.

---

## 4. Olya Role and Identity

| Field | Value |
|-------|-------|
| Olya identity hash | **E6714550214106BA** |
| Operator identity hash | **3FBE21323E22BFC1** |
| Distinct identities | **yes** |
| Pre-enroll denied `/start` exec | **17177** (unique) |
| Chat type | private |
| `admin_user_ids` | **not enrolled** |
| `manager_action_user_ids` | **enrolled** |
| Raw Telegram ID in docs | **none** |

Evidence: `evidence/phase3d4/OLYA-IDENTITY-RESOLUTION-v1.md`, `ROLE-AUTHORIZATION-MODEL-v1.md`.

---

## 5. Start / Help

| Path | Actor | Harness | Live |
|------|-------|---------|------|
| Admin `/start` | operator | PASS | PASS |
| Admin `/help` | operator | PASS | PASS |
| Manager `/start` | Olya hash | PASS | **PENDING** |
| Manager `/help` | Olya hash | PASS | **PENDING** |
| Unauthorized | unknown | PASS (deny) | — |

Manager texts expose button usage and copy blocks only — no Admin command list.

Evidence: `evidence/phase3d4/MANAGER-START-HELP-ACCEPTANCE-v1.md`.

---

## 6. Callbacks

| Case | Actor | Method | Result |
|------|-------|--------|--------|
| processed apply | Olya hash | synthetic harness | **PASS** |
| processed idempotent | Olya hash | synthetic harness | **PASS** |
| spam apply | Olya hash | synthetic harness | **PASS** |
| conflict | Olya hash | synthetic harness | **PASS** |
| unauthorized | unknown | harness | **PASS** |
| live pending card tap | Olya | human Telegram | **PENDING** |

Synthetic rows excluded from production `/stats`. No production business lead mutated for acceptance.

Evidence: `evidence/phase3d4/OLYA-MANAGER-ACTION-ACCEPTANCE-v1.md`.

---

## 7. Supplied-Form Comparison (free-audit, synthetic)

| Aspect | Before (v3.1 + sm-msg-v2) | After (v3.2 + sm-msg-v2.1) |
|--------|---------------------------|----------------------------|
| `t.me/…` in site field | shown as **Сайт** | moved to **мессенджer** |
| Contact | often missing | `@handle` populated |
| Source page | verbose `/free-audit/` | `free-audit` normalized |
| Comment «в тг» | ignored | reflected in summary |
| Emoji density | section prefixes possible | title + lifecycle only |
| Quality | needs_data | ok (synthetic fixture) |

Evidence: `evidence/phase3d4/SUPPLIED-FORM-END-TO-END-v1.md`.

---

## 8. Semantic Fixes (parser v3.2)

| Fix | Document |
|-----|----------|
| `t.me` not site | `MESSENGER-SITE-SEMANTIC-FIX-v1.md` |
| Contact method inference | `CONTACT-METHOD-INFERENCE-v1.md` |
| «в тг» preference | `COMMENT-SEMANTICS-v1.md` |
| Source page slug | `SOURCE-PAGE-NORMALIZATION-v1.md` |

CONFIG `parser_version=sm-parser-v3.2`.

---

## 9. Emoji Reduction (sm-msg-v2.1)

- Section labels without prefix emoji.
- Standard cards: max 2 emoji (title + lifecycle).
- Copy `<code>` / `<pre>` and inline keyboard unchanged.

Evidence: `evidence/phase3d4/EMOJI-DENSITY-REDUCTION-v1.md`.

---

## 10. Admin Regression

| Metric | Expected | Result |
|--------|----------|--------|
| `admin_user_ids` count | 1 | **PASS** |
| `manager_action_user_ids` count | 2 | **PASS** |
| Olya on admin list | no | **PASS** |
| Olya `/status` | deny | **PASS** (harness) |
| Operator Admin commands | pass | **PASS** |
| New workflows | 0 | **PASS** |

Evidence: `evidence/phase3d4/ADMIN-REGRESSION-v1.md`.

---

## 11. Multi-Form Registry

- Registry: `knowledge/WEBSITE-FORM-FORMATS-v1.md`
- **Defined:** `free-audit` (Phase 3D.4 accepted)
- **Placeholders:** seo, direct, site-build, callback, calculator
- **Policy:** one form per iteration — `evidence/phase3d4/MULTI-FORM-TEST-PLAN-v1.md`

---

## 12. Final Contour

| Workflow | ID | Active |
|----------|-----|--------|
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | **false** |
| Operational.dev | xSnXPy8cEHoZw6xG | **true** |
| Admin.dev | wLrLp4WQHm1VJmxz | **true** |

| Setting | Value |
|---------|-------|
| Gmail intake workflows | **1** |
| `environment` | production |
| `ai_enabled` | **false** |
| `parser_version` | **sm-parser-v3.2** |
| `message_format_version` | **sm-msg-v2.1** |

Evidence: `evidence/phase3d4/FINAL-WORKFLOW-STATE-v1.md`.

---

## 13. Harness and Live Acceptance

| Suite | Result |
|-------|--------|
| F-MU01–F-MU30 (manager UX regression) | **30/30 PASS** |
| F-3D4-01–F-3D4-12 (Phase 3D.4 semantics) | **PASS** |
| Live n8n patch | **ok** |
| CONFIG enrollment | **ok** |
| Synthetic Olya callbacks | **PASS** |

Receipt: `evidence/phase3d4/PHASE3D4-ACCEPTANCE-RECEIPT-v1.md`.

---

## 14. Operational Counters (this phase)

| Metric | Value |
|--------|-------|
| AI calls | **0** |
| Client messages | **0** |
| Workflows created | **0** |

---

## 15. Changed / Created Files

### Created — evidence/phase3d4/ (14)

1. `OLYA-IDENTITY-RESOLUTION-v1.md`
2. `ROLE-AUTHORIZATION-MODEL-v1.md`
3. `MANAGER-START-HELP-ACCEPTANCE-v1.md`
4. `OLYA-MANAGER-ACTION-ACCEPTANCE-v1.md`
5. `EMOJI-DENSITY-REDUCTION-v1.md`
6. `MESSENGER-SITE-SEMANTIC-FIX-v1.md`
7. `CONTACT-METHOD-INFERENCE-v1.md`
8. `COMMENT-SEMANTICS-v1.md`
9. `SOURCE-PAGE-NORMALIZATION-v1.md`
10. `SUPPLIED-FORM-END-TO-END-v1.md`
11. `MULTI-FORM-TEST-PLAN-v1.md`
12. `ADMIN-REGRESSION-v1.md`
13. `FINAL-WORKFLOW-STATE-v1.md`
14. `PHASE3D4-ACCEPTANCE-RECEIPT-v1.md`

### Created — knowledge/

15. `WEBSITE-FORM-FORMATS-v1.md`

### Created — reports/

16. `REPORT-iseo-sales-manager-bot-phase3d4-manager-enrollment-and-form-semantics-v1.md`

### Modified

17. `README.md`
18. `OPERATIONAL-INDEX.md`
19. `architecture/TELEGRAM-UX-CONTRACT-v1.md`
20. `architecture/ADMIN-COMMAND-CONTRACT-v1.md`
21. `implementation/TELEGRAM-FORMATTER-SPEC-v1.md`
22. `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`
23. `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md`
24. `implementation/TEST-HARNESS-SPEC-v1.md`
25. `guides/OLYA-LEAD-WORK-GUIDE-v1.md`
26. `guides/OPERATOR-RUNBOOK-v1.md`

---

## 16. Git

| Field | Value |
|-------|-------|
| Commit hash | **TBD** |
| Push hash | **TBD** |
| Commit / push | not performed in this documentation pass |

---

## 17. Pending / Next

1. **Olya live Telegram:** `/start`, `/help`, first real callback on pending card — human confirmation.
2. **Next form iteration:** per registry — seo or next prioritized slug; one form only.
3. **Registry promotion:** separate governance gate (unchanged).
4. **PHASE 3E AI ON:** separate charter only.

---

## 18. Not Claimed

- Live Olya Telegram confirmation complete.
- Second website form implemented.
- Registry status promotion to active.
- AI ON in production.
- Git commit/push (TBD).

---

*Phase 3D.4 documentation pack — 2026-08-03.*


## Git

- Commit: `221aca19898abaf9e5b91533daf28e511caaac18`
- Push tip: `221aca19898abaf9e5b91533daf28e511caaac18`
- Branch: `mars/canonical-post-recovery`


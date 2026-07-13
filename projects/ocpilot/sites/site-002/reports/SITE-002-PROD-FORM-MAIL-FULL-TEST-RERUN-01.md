# REPORT — SITE-002 Form Mail Full Test Rerun 01

**Operation:** `SITE-002-PROD-FORM-MAIL-FULL-TEST-RERUN-01`  
**OCPilot run:** `4.266 — SITE-002 Form Mail Full Test Rerun 01`  
**Date:** 2026-07-14  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits\SITE-002-PROD-FORM-MAIL-FULL-TEST-RERUN-01\`

---

## 1. Scope

Full controlled rerun of SITE-002 website form mail tests after the empty-lead guard (Runs 4.264 / 4.265). Verify valid forms succeed with expected user fields in admin mail expectations; service-only / whitespace payloads return HTTP 400; no recipient restore; patch only if a live gap appears.

## 2. Operator request

Re-run test submits from all known forms and check whether empty admin mail `ЗПМ: новая заявка — Заявка с сайта` reappears. Do **not** change recipients; keep temporary recipient only `client.leads@polygon-ws.ru`; do **not** restore `info@bzpm.ru`.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` label | `AI WS` |
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| HEAD | `ffa92154` (= `origin/mars/canonical-post-recovery`) |
| Expected prior commit present | **yes** (`ffa92154` empty-lead follow-up; `2bec4794` empty-lead fix) |
| Staged / unpushed | none vs origin |
| Dirty main | foreign WIP present — **not mutated** |
| Authority safe for scoped commit | **yes** |

Artifacts: Storage `preflight/authority-git.txt` · `preflight/dirty-main-readonly.txt`

## 4. Current handler guard

FTP download `/public_html/catalog/controller/checkout/anketa.php`:

| Field | Value |
|-------|--------|
| SHA256 | `d86c812b3925720d561007fc304413375b544777810f20307fda6842082c716e` |
| Matches Run 4.264/4.265 | **yes** |
| Empty-lead guard present | **yes** (`has_user_field` + reject message) |

Allowlist user fields remain: `name|contact|phone|email|company|message|comment|text|project_description|subject` (non-empty after `trim`). Service keys (page/referrer/utm/dialog) do not satisfy the guard.

Artifact: Storage `verification/current-empty-guard-confirmation.md` · `source-before/`

## 5. Form inventory

Live crawl with UTM `utm_source=mars_test&utm_medium=form_full_rerun`:

| Page | Anketa dialogs seen |
|------|---------------------|
| `/about` | 7 (CTA), 2, 1, 3 |
| `/custom-equipment` | 11 (+ footer 1/2/3) |
| `/payment-methods` | 9 (+ footer) |
| `/delivery` | 8 (+ footer) |
| `/dealers` | 7 (+ footer) |
| `/guarantee` | 10 (+ footer) |
| `/contact` | footer 1/2/3 only (no dedicated corp CTA) |
| Sample PDP | dialog 1 (`to_ask`), 2, 3 |

**Deferred note (not fixed):** `/about` CTA posts `dialog=7` → subject/label «Форма дилерам и оптовикам» (mislabel). Classification still possible; reported only.

Artifacts: `form-inventory/form-inventory.json` · `.csv` · `verification/form-inventory-summary.md`

## 6. Test plan

Marker: `MARS-TEST-SITE002-FULL-FORM-RERUN-01`  
Endpoint: `POST /index.php?route=checkout/anketa`  
Recipient expected: `client.leads@polygon-ws.ru`  
Recipient forbidden: `info@bzpm.ru`

Artifacts: `test-plan/test-plan.md` · `test-plan.json`

## 7. Valid form submission results

All controlled valid POSTs: **HTTP 200** + `ok: true`.

| ID | Local (+07) | Dialog | Expected subject | Pass |
|----|-------------|--------|------------------|------|
| valid-about | 2026-07-14 04:06:07 | 7 | ЗПМ: новая заявка — Форма дилерам и оптовикам | yes |
| valid-custom | 04:06:16 | 11 | … — Оборудование на заказ | yes |
| valid-payment | 04:06:24 | 9 | … — Вопрос по оплате | yes |
| valid-delivery | 04:06:36 | 8 | … — Вопрос по доставке | yes |
| valid-dealers | 04:06:45 | 7 | … — Форма дилерам и оптовикам | yes |
| valid-guarantee | 04:06:54 | 10 | … — Гарантийное обращение | yes |
| valid-callback | 04:07:03 | 2 | … — Запрос на обратный звонок | yes |
| valid-product | 04:09:08 | 1 | … — Вопрос по товару | yes |

Payload includes name `MARS Test SITE-002`, phone `+7 000 000-00-00`, and per-form marker in message. Visual mailbox content: **SAFE UNKNOWN** (operator checklist).

Artifacts: `test-submissions/valid-results.json` · `.csv` · `raw-responses/`

## 8. Negative test results

| ID | Local (+07) | Expected | Actual | Pass | Email expected |
|----|-------------|----------|--------|------|----------------|
| neg-service-only (dialog=0, no user fields) | 04:07:06 | 400 | **400** | yes | no |
| neg-whitespace-only | 04:07:08 | 400 | **400** | yes | no |
| neg-service-dialog7 (dialog=7, no user fields) | 04:07:10 | 400 | **400** | yes | no |

`stop_for_patch: false` — no empty-mail gap demonstrated post-guard.

Artifacts: `negative-tests/results.json` · `.csv` · `raw-responses/`

## 9. Mailbox operator checklist

Exact checklist for `client.leads@polygon-ws.ru`:

- Storage `mailbox-operator-checklist/checklist.md` · `checklist.csv`
- Also `mail-expectations/mail-expectations.md`

**Operator please confirm:**

1. All 8 valid subjects arrived with user fields + markers.  
2. After **04:07:06–04:07:10 +07**, no new empty `ЗПМ: новая заявка — Заявка с сайта`.  
3. `info@bzpm.ru` not restored / not in To/Cc.

## 10. Patch decision

**NO PATCH** — guard SHA unchanged; negatives blocked; valids succeeded.

Artifact: `patch-if-needed/decision.md`

## 11. Production mutation summary

| Kind | Count |
|------|-------|
| FTP writes | **0** |
| DB writes | **0** |
| Admin saves | **0** |
| Import runs triggered | **0** |
| Scheduler changes | **0** |
| Recipient changes | **0** |
| Valid test submissions | **8** |
| Negative test submissions | **3** |
| Mail sends expected | **8** (valid only) |

## 12. Recipient status

- Remains **only** `client.leads@polygon-ws.ru`
- `info@bzpm.ru` **not restored** (this task did not change recipients)

## 13. Git / worktree summary

| Check | Result |
|-------|--------|
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| Preflight HEAD | `ffa92154` = origin |
| Dirty main | untouched |
| Commit message (this wave) | `ocpilot: rerun SITE-002 form mail tests` |

## 14. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits\SITE-002-PROD-FORM-MAIL-FULL-TEST-RERUN-01\`

Includes: preflight, source-before, form-inventory, test-plan, test-submissions, negative-tests, mail-expectations, mailbox-operator-checklist, patch-if-needed, verification, reports, manifests, logs.

## 15. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Operator mailbox visual confirmation of 8 mails | **SAFE UNKNOWN** — checklist issued |
| Confirmation that no empty post-negative mail arrived | **SAFE UNKNOWN** — needs operator |
| Some mail discovery reports listed in charter (`SITE-002-MAIL-*-01.md` under reports/) | Paths may live as baselines / alternate names — used prior audit + handler mirror as authority |
| `/about` dialog=7 mislabel | Deferred (does not block classification) |

**Blockers:** none for HTTP/guard verification.

## 16. Final verdict

**`SITE-002 FORM MAIL FULL TEST RERUN PARTIAL — MAILBOX OPERATOR CONFIRMATION NEEDED`**

HTTP/backend: valid forms OK; empty/service-only/whitespace blocked; no production mutation; no recipient change. Mailbox body/subject receipt remains operator-confirmed.

## 17. Next recommendation

1. Operator: run mailbox checklist; answer the three questions in §9.  
2. If empty `Заявка с сайта` appears **after** 04:07:06 +07 with post-patch guard still present → reopen as guard-gap (unexpected).  
3. Optional later charter: fix `/about` dialog=7 mislabel (dedicated dialog / label).  
4. When test window closes: restore production recipients by **separate** approved recipient-change task (not this run).

# REPORT — ISEO SALES MANAGER BOT PHASE 3E.1 PARSER 3.3 AND LEAD SEMANTIC MODEL V1

## 1. Verdict

**COMPLETE — PARSER READY; OPERATOR SEMANTIC ACCEPTANCE PENDING**

Parser 3.3 + Lead Semantic Model v1 deployed to Operational.dev; harness 46/46 PASS; live semantic fixtures parsed; operator visual confirmation still required.

## 2. Operator-approved scope

ISEO-SALES-MANAGER-BOT — PHASE 3E.1 PARSER 3.3 AND LEAD SEMANTIC MODEL V1.  
Access roles unchanged. AI OFF. No reminders. No Sales-Manager-v2 activation. No new workflows.

## 3. Environment

- Repo root: `X:\AI MARS`
- Volume: `AI WS` (X:)
- Clean worktree: `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3e1-20260805-054425\repo`
- Private tooling: `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\phase3e1-local\`

## 4. Canonical baseline

- Base: `origin/mars/canonical-post-recovery` @ `b69291e5` (Phase 3D.8.3 tip alignment)
- Branch used for implementation: `mars/iseo-sm-phase3e1-parser33`

## 5. Parser 3.2 baseline

Pre-patch live Parse Lead stamped `sm-parser-v3.2`; message format `sm-msg-v2.2`/formatter still carried `sm-msg-v2.1` literals with Phase 3D.8.3 short buttons. Sanitized baseline captured under phase3e1-local backups (not committed raw).

## 6. Parser 3.3 architecture

Two-contour deterministic parser:

1. HTML → plain-text structure extraction
2. Normalized-text / one-line fallback with label boundaries

Semantic model adds website states, form/comment/source separation, intent precedence, quality, missing-info, first-reply templates. AI remains OFF.

## 7. HTML extraction

`htmlToPlainText` + labeled field extraction; `<br>`, blocks, table cells, bold labels, nested links supported.

## 8. Text fallback

Marker-bounded extraction for collapsed and multiline forms; comment ends at `Отправлено со страницы` / `IP`.

## 9. Raw-value preservation

`client_name_raw=test` preserved; `is_probable_test` set separately; no destructive wipe of synthetic-looking customer values.

## 10. Website state model

States: `provided` | `explicitly_absent` | `alternative_contact` | `invalid_or_placeholder` | `missing` with required precedence.

## 11. Alternative contacts

`t.me` / Telegram / WhatsApp in site field → alternative contact fields; not shown under Сайт.

## 12. Comment boundaries

Comment stripped of trailing source-page / IP markers; form title not concatenated into canonical comment.

## 13. Form/source separation

`form_offer`, `source_page_title`, `source_topic`, `comment_*`, `explicit_client_intent`, `resolved_service` separated.

## 14. Intent precedence

`client comment → structured fields → form offer → source page → subject/title`.

## 15. Resolved service

Taxonomy: Audit, SEO, WebsiteDevelopment, WebsiteDevelopmentSEO, AISearch, Direct, Other, NeedsClarification (+ Russian labels). Compat `service` column retained.

## 16. Request summary

Deterministic summaries without unsupported facts.

## 17. Lead quality

`sufficient` / `needs_clarification` / `insufficient` / `test` — website-development without site can be data-sufficient.

## 18. Missing information

Service-aware; does not ask for known site; development asks business/scope not existing URL.

## 19. First-reply rules

Deterministic templates; never re-ask provided/absent site; Telegram not called a website; test replies omitted; always “Ответ клиенту автоматически не отправляется.”

## 20. Telegram card

`sm-msg-v2.3`: test badge, comment vs form context, site states, short buttons unchanged.

## 21. Storage migration

Additive plan documented. Live interim: semantic snapshot packed into existing `quality_comment`; no destructive column removal. Full additive headers deferred safely.

## 22. Historical compatibility

No bulk reparse. Archive continues to read legacy Parser 3.2 rows via compat fields.

## 23. Regression fixtures

P33 catalog + harness cases covering operator patterns 1–10 and required semantic cases.

## 24. Harness

`implementation/harness/phase3e1-harness.mjs` → **46/46 PASS**.

## 25–30. Live fixtures A–F

### Initial rapid / sequential wave (Phase 3E.1)

| Key | website_state | resolved_service | Live notes |
|---|---|---|---|
| A | provided | Audit | Card + delivery to 2 recipients |
| B | explicitly_absent | WebsiteDevelopment | Card formatted; Sheets rate-limit interrupted full path |
| C | explicitly_absent | WebsiteDevelopmentSEO | Parse OK; Sheets rate-limit on rapid seq |
| D | alternative_contact | NeedsClarification | Parse OK |
| E | provided | NeedsClarification (test) | Parse OK |
| F | provided | SEO | Parse OK |

### Paced B–F wave (Phase 3E.1.1)

| Key | Marker | website_state | resolved_service | RAW/CLEAN/DELIV | sendOk | dup |
|---|---|---|---|---|---|---|
| A | (prior) | provided | Audit | — | 2 | 0 — **operator visual PASS**; not resent |
| B | `PHASE_3E1_B_NO_SITE_WEBSITE_DEVELOPMENT` | explicitly_absent | WebsiteDevelopment (`Разработка сайта`) | 1/1/2 | 2 | 0 |
| C | `PHASE_3E1_C_WEBSITE_THEN_SEO` | explicitly_absent | WebsiteDevelopmentSEO (`Разработка сайта + SEO`) | 1/1/2 | 2 | 0 |
| D | `PHASE_3E1_D_TELEGRAM_ALTERNATIVE_CONTACT` | alternative_contact (`telegram`) | NeedsClarification | 1/1/2 | 2 | 0 |
| E | `PHASE_3E1_E_TEST_NAME_PRESERVATION` | provided | Audit (form-context fallback); name `test` preserved; test badge | 1/1/2 | 2 | 0 |
| F | `PHASE_3E1_F_ONE_LINE_FALLBACK` | provided | SEO; comment `нужно SEO-продвижение` (no source bleed) | 1/1/2 | 2 | 0 |

Sheets pacing: ≥55s between fixtures; **no rate-limit** during B–F paced wave. Evidence: `evidence/phase3e1/LIVE-SEMANTIC-ACCEPTANCE-B-F-v1.md`.

## 31. Operator semantic acceptance

- Fixture A: **PASS** (operator visual)
- Fixtures B–F: **runtime/storage PASS**; **operator visual PENDING**

Verdict remains: `COMPLETE — PARSER READY; OPERATOR SEMANTIC ACCEPTANCE PENDING` until B–F Telegram cards confirmed.

## 32. Delivery regression

Multi-recipient path intact for successful inject (A: `sendOk=2`). Connection hash unchanged. No new workflows.

## 33. Lifecycle regression

Buttons `✅ Обработано` / `🚫 Спам`; callbacks `sm:p:` / `sm:s:` unchanged.

## 34. Final access state

Андрей=admin/active; Мопс=moderator/active; Оля=revoked; Никита=revoked. Access-role changes=0.

## 35. Final workflow state

- Ops active 45; Admin active 59; v2 inactive 19
- parser `sm-parser-v3.3`; msg `sm-msg-v2.3`
- OpenRouter disabled; sole Gmail Fetch Leads; no residual P3E1 synth nodes

## 36. Safety counters

- AI provider calls=0
- automatic client messages=0
- workflows created=0
- access-role changes=0
- reminder implementation changes=0
- historical bulk reparses=0
- real-client test messages=0
- duplicate lead deliveries=0 (polls clean for controlled injects)

## 37. Files created

See `evidence/phase3e1/*`, architecture contracts, harness, runtime libs, report.

## 38. Files changed

README, OPERATIONAL-INDEX, product baselines, Telegram UX, patch/migration/harness specs, research/parser-3.3 markers.

## 39. Security validation

No credentials, Telegram IDs, workbook IDs, raw emails, or unsanitized exports committed. Synthetic fixtures only.

## 40. Commit

`feat(iseo-sales-manager-bot): add parser 3.3 semantic lead model` — `8cf81b41`  
`test(iseo-sales-manager-bot): complete parser 3.3 live fixtures` — `47cda75c`

## 41. Push

Pushed non-force to `origin/mars/canonical-post-recovery` (`a33ccac3..47cda75c` for B–F evidence wave; prior parser wave `b69291e5..8cf81b41`).

## 42. Risks

- Sheets rate-limit under rapid sequential synthetic injects — **mitigated** for B–F by paced one-at-a-time inject (≥55s)
- Multi-item webhook inject collapses after Parse Lead (graph design); sequential inject required for N cards
- Full additive Sheets columns not yet applied live (packed `quality_comment` interim)
- Synthetic Gmail label ops fail by design

## 43. SAFE UNKNOWN

Whether operator Telegram visual acceptance of fixtures B–F is confirmed — pending human review. (Fixture A already PASS.) Optional spot-check of `/leads`, `/my_status`, `/moderator_pending` after B–F cards (Admin untouched this wave).

## 44. Remaining operator visual actions

Exact checks (do not press lifecycle buttons unless intentional):

**B:** `Сайт: отсутствует`; interest `Разработка сайта`; reply/next step does not ask for current site.  
**C:** interest `Разработка сайта + SEO`; both stages acknowledged.  
**D:** Telegram shown as contact, not under `Сайт`.  
**E:** client name `test` visible; `🧪 Тестовая заявка` badge.  
**F:** fields separated from one-line body; interest `SEO`; comment without source-label contamination.

Also confirm: exactly one card per recipient (Андрей + Мопс) per fixture; no duplicates after polls.

## 45. Stop condition

Parser 3.3 implemented; semantic model implemented; harness PASS; Fixture A visual PASS; paced B–F delivered once each with RAW/CLEAN/LEAD_DELIVERIES complete; acceptance packet prepared; this report updated. **STOP** for operator visual confirmation of B–F before claiming `PHASE 3E.1 COMPLETE — PARSER 3.3 AND LEAD SEMANTIC MODEL READY`.

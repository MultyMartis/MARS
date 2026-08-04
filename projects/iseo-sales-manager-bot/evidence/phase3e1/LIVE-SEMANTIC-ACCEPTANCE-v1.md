# LIVE SEMANTIC ACCEPTANCE v1 — Phase 3E.1

**Status:** parser/semantic live evidence collected; Fixture A **operator visual PASS**; B–F paced delivery complete — see [LIVE-SEMANTIC-ACCEPTANCE-B-F-v1.md](LIVE-SEMANTIC-ACCEPTANCE-B-F-v1.md). **Full operator visual acceptance still PENDING** for B–F.

## Contour

- Operational.dev `xSnXPy8cEHoZw6xG` active, 45 nodes, sole `Gmail Fetch Leads`
- Admin.dev `wLrLp4WQHm1VJmxz` active, 59 nodes, message+callback_query
- Sales-Manager-v2 `h8I2Tl2yl4uzhUnB` inactive
- AI OFF / OpenRouter disabled
- parser `sm-parser-v3.3` / message `sm-msg-v2.3`

## Batch inject (6 items)

All six fixtures parsed live with expected semantics:

| Key | website_state | resolved_service |
|---|---|---|
| A | provided | Audit |
| B | explicitly_absent | WebsiteDevelopment |
| C | explicitly_absent | WebsiteDevelopmentSEO |
| D | alternative_contact | NeedsClarification |
| E | provided | NeedsClarification (probable test) |
| F | provided | SEO |

Note: multi-item inject collapses after Parse Lead in current graph (Normalize CONFIG path). Sequential inject used for card/delivery proof.

## Sequential inject (initial rapid wave)

- A: formatted sm-msg-v2.3 card + delivered to 2 eligible recipients (`sendOk=2`), buttons `✅ Обработано` / `🚫 Спам` — later **operator visual PASS**
- B: formatted card with `Сайт: отсутствует`, interest `Разработка сайта`, comment `хочу сайт` (Telegram send interrupted by Sheets rate-limit/error path)
- C–F: semantic parse confirmed; Sheets API rate-limit (`too many requests`) blocked full append/send under rapid sequential inject

## Paced B–F wave (Phase 3E.1.1)

Re-delivered B–F one-at-a-time with ≥55s pauses and unique markers. Each fixture: RAW=1, CLEAN=1, LEAD_DELIVERIES=2, sendOk=2, duplicates=0, no Sheets rate-limit. Full packet: [LIVE-SEMANTIC-ACCEPTANCE-B-F-v1.md](LIVE-SEMANTIC-ACCEPTANCE-B-F-v1.md).

Synthetic Gmail label ops may fail (`Add Gmail PROCESSED` bad request) — expected for non-Gmail synthetic ids; not a parser defect.

## Operator comparison (sanitized)

Prepared from deterministic local pipeline + live card previews (redacted):

- Valid site never asked again in reply templates (A/F business rules)
- Explicit no-site + `хочу сайт` → Website Development; site not shown as URL
- Site-then-SEO comment → Website Development + SEO
- `t.me` → alternative_contact; not under Сайт
- `test` / `тест бота` → probable test badge; reply omitted
- One-line form keeps comment boundary (no `Отправлено со` bleed)

## Safety counters

- AI provider calls = 0
- automatic client messages = 0
- workflows created = 0
- access-role changes = 0
- historical bulk reparses = 0

## Operator action required

Confirm in Telegram (eligible: Андрей, Мопс):

1. Site / no-site / Telegram-alt display
2. Comment vs form offer separation
3. Resolved service sensibility
4. Test badge on synthetic cards
5. No duplicate cards after polls
6. Reply draft consistency where shown

Do **not** claim PHASE 3E.1 COMPLETE until operator visual acceptance.

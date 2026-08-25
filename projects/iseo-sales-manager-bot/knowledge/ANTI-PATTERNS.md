# Anti-Patterns

## Do Not Claim Runtime From Docs

Do not claim MARS executes the bot. n8n is execution truth. Docs and evidence describe the system; they do not run it.

## Do Not Treat Sheets As Target Architecture

Google Sheets are current production persistence. For new projects and successors, prefer PostgreSQL as system of record and keep Sheets as export/report unless explicitly chartered otherwise.

## Do Not Enable Or Describe AI As Active

Stable production is AI OFF: `ai_enabled=false`, OpenRouter disabled. Do not claim AI routing, AI parsing, or AI scoring is live.

## Do Not Use Gmail Snippets As Source Authority

`simple=true` and snippet-only fetches are lossy. Use full message mode and capture visible body before parsing.

## Do Not Reconstruct RAW From CLEAN

RAW source must be literal source. Do not create fake `Имя:`, `Телефон:`, `Сайт:` source blocks from normalized fields.

## Do Not Substitute CLEAN For Raw UX

The `📄 Исходная заявка` action must not show a CLEAN card or normalized summary as if it were the original request.

## Do Not Expose IP In Raw Telegram UX

IP is intentionally omitted from raw-source Telegram display.

## Do Not Use Broad Sheet Reads For Callback Lookup

Use filtered RAW-by-`lead_id` lookup. Broad reads can trigger 429s and make callbacks fragile.

## Do Not Mutate Lifecycle From Reminders

Reminder notifications do not process, spam, archive, or otherwise resolve leads.

## Do Not Mutate Lifecycle From Raw Clicks

Viewing source is read-only.

## Do Not Claim Natural Monday Reminder PASS

Natural Monday reminder acceptance remains PENDING OBSERVATION unless a later evidence-backed doc supersedes it.

## Do Not Replay Gmail Ingestion For Legacy Fallback

Legacy fallback is READ-only by `source_message_id`; it must not create a new lead, mark Gmail state, or change lifecycle.

## Do Not Store Secrets Or Raw PII In Docs

Reference CONFIG keys and n8n credential roles only. Never write token values, passwords, API keys, raw email bodies, phone numbers, or private lead content.

## Do Not Create Workflow Copies Casually

The stable contour has active Operational.dev and Admin.dev. Workflow copies require an explicit phase and evidence trail.

## Do Not Turn Admin.dev Into A Task Bot

Admin.dev handles callbacks, reminders, raw source, and commands. It does not automatically manage delivery, DND, assignments, or a to-do list in the stable baseline.


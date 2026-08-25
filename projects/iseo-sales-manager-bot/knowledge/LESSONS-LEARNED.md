# Lessons Learned

These lessons are generalized from the stable baseline and project history. They avoid raw PII and secret values.

## 1. Snippet-Only Gmail Intake

**SYMPTOM:** Raw-source view lacked the full request.  
**ROOT CAUSE:** Gmail fetch used lossy simple/snippet data.  
**FIX:** Use `simple=false`; capture full body before parse.  
**GENERAL LESSON:** Source UX needs source authority, not preview text.  
**REUSABLE RULE:** Never build `📄 Исходная заявка` from snippets when a full body exists.

## 2. RAW Reconstructed From CLEAN

**SYMPTOM:** Raw view looked like normalized labels instead of the original message.  
**ROOT CAUSE:** CLEAN fields were used to rebuild source.  
**FIX:** Render literal RAW with minimal cleanup only.  
**GENERAL LESSON:** Normalized data cannot prove original wording.  
**REUSABLE RULE:** RAW and CLEAN must remain separate authorities.

## 3. Broad RAW Sheet Reads

**SYMPTOM:** RAW lookup caused rate-limit or reliability risk.  
**ROOT CAUSE:** Callback path read too much sheet data.  
**FIX:** Filter RAW by `lead_id`.  
**GENERAL LESSON:** Callback paths need scoped reads.  
**REUSABLE RULE:** Never solve lookup uncertainty with broad sheet scans.

## 4. Legacy Lossy Source

**SYMPTOM:** Older records had incomplete stored source.  
**ROOT CAUSE:** Historical intake did not persist full visible body.  
**FIX:** Classify lossy source and use READ-only Gmail fallback by `source_message_id` when eligible.  
**GENERAL LESSON:** Legacy recovery must not mutate production history.  
**REUSABLE RULE:** Fallback reads may recover display; they must not replay ingestion.

## 5. Raw Click Mutated State Risk

**SYMPTOM:** Source viewing risked being treated like a lifecycle action.  
**ROOT CAUSE:** Callback semantics were not separated clearly enough.  
**FIX:** Define raw callback as read-only.  
**GENERAL LESSON:** Every button needs an explicit state contract.  
**REUSABLE RULE:** Read actions must not change lead lifecycle.

## 6. Reminder Lifecycle Drift

**SYMPTOM:** Reminder work could be confused with status processing.  
**ROOT CAUSE:** Notification and lifecycle boundaries were implicit.  
**FIX:** Reminder contract states notification only.  
**GENERAL LESSON:** Scheduled nudges are not manager actions.  
**REUSABLE RULE:** Reminders must not mutate lifecycle.

## 7. Weekend Backlog Ambiguity

**SYMPTOM:** Monday reminder candidates were unclear.  
**ROOT CAUSE:** Weekday gate and backlog rule were not explicit enough.  
**FIX:** Mon-Fri at 10:00 Europe/Moscow; Monday includes weekend pending backlog.  
**GENERAL LESSON:** Schedule rules need timezone and backlog semantics.  
**REUSABLE RULE:** Always document weekday, timezone, and backlog behavior together.

## 8. Premature PASS Claim

**SYMPTOM:** Natural Monday reminder could be over-claimed before live observation.  
**ROOT CAUSE:** Regression readiness was conflated with natural acceptance.  
**FIX:** Mark as PENDING OBSERVATION.  
**GENERAL LESSON:** Do not convert expected future observation into evidence.  
**REUSABLE RULE:** PASS requires observed evidence or an explicit synthetic-test label.

## 9. AI Boundary Confusion

**SYMPTOM:** Docs could imply AI behavior existed.  
**ROOT CAUSE:** Planned AI capability and live disabled AI were mixed.  
**FIX:** State `ai_enabled=false` and OpenRouter disabled.  
**GENERAL LESSON:** Architecture ideas are not production facts.  
**REUSABLE RULE:** If AI is off, describe deterministic behavior only.

## 10. Workflow Copy Drift

**SYMPTOM:** Multiple workflow names risked confusing runtime authority.  
**ROOT CAUSE:** Active, inactive, and legacy workflows were not separated.  
**FIX:** Identify active Operational.dev/Admin.dev and inactive references.  
**GENERAL LESSON:** Runtime identity is part of stability.  
**REUSABLE RULE:** List active workflow IDs before changing or debugging n8n.

## 11. Acceptance TMP Tooling Drift

**SYMPTOM:** Temporary acceptance helpers could be mistaken for runtime.  
**ROOT CAUSE:** Evidence tooling lived near production context.  
**FIX:** Classify TMP tooling as acceptance-only.  
**GENERAL LESSON:** Test scaffolding must not become hidden architecture.  
**REUSABLE RULE:** Document TMP as forensic support, not production dependency.

## 12. Secret Leakage Risk

**SYMPTOM:** Docs could accidentally capture tokens or raw bodies.  
**ROOT CAUSE:** Operational debugging naturally touches sensitive material.  
**FIX:** Reference only CONFIG keys and credential roles.  
**GENERAL LESSON:** Documentation should preserve contracts, not secrets.  
**REUSABLE RULE:** No secret values or raw PII in Git docs.

## 13. Sheets Future Confusion

**SYMPTOM:** Current Sheets persistence could be mistaken for preferred architecture.  
**ROOT CAUSE:** Stable reality and successor design were not separated.  
**FIX:** State Sheets are current reality; PostgreSQL is preferred for successors.  
**GENERAL LESSON:** Production truth and target architecture can differ.  
**REUSABLE RULE:** Preserve current facts while recommending DB-first for new builds.

## 14. Exactly-Once / Duplicate Processing

**SYMPTOM:** Same Gmail message risked multiple business deliveries.  
**ROOT CAUSE:** Weak or missing message-id / delivery guards.  
**FIX:** Dedupe on `gmail_message_id` / `source_message_id` plus Telegram delivery guards.  
**GENERAL LESSON:** Ingest idempotency and delivery idempotency are both required.  
**REUSABLE RULE:** Classify duplicate before CLEAN write and gate Telegram success.

## 15. Re-Delivery ≠ Re-Ingestion

**SYMPTOM:** Operators re-sent cards in ways that looked like new intake.  
**ROOT CAUSE:** Recovery tooling blurred delivery and ingestion.  
**FIX:** Explicit re-delivery paths that do not create new RAW rows.  
**GENERAL LESSON:** Forensic re-send must not mint new business leads.  
**REUSABLE RULE:** Re-delivery uses existing `lead_id`; re-ingestion requires new source message.

## 16. `raw_text present` ≠ Retrievable Source

**SYMPTOM:** Field presence suggested source was usable when content was empty/lossy.  
**ROOT CAUSE:** Presence checks were treated as usefulness checks.  
**FIX:** Classify source quality; empty/lossy paths have explicit UX states.  
**GENERAL LESSON:** Metadata presence is not content quality.  
**REUSABLE RULE:** Validate source usefulness before promising raw view.

## 17. Already-Spam Historical Cards

**SYMPTOM:** Acceptance on already-spam cards needed TMP callback filling.  
**ROOT CAUSE:** Production formatter correctly omits some actions for settled spam.  
**FIX:** Treat as acceptance-only tooling; do not change live pending-card behavior.  
**GENERAL LESSON:** Historical settled entities are not the production UX baseline.  
**REUSABLE RULE:** Accept live behavior on real pending cards, not only spam history.

## 18. Test / Synthetic Contamination

**SYMPTOM:** Synthetic leads could pollute production acceptance or reminders.  
**ROOT CAUSE:** Test rows not excluded from actionable selectors.  
**FIX:** Exclude tests/archive from reminders and acceptance claims.  
**GENERAL LESSON:** Production acceptance requires real eligible leads.  
**REUSABLE RULE:** Never use synthetic data as production acceptance evidence.

## 19. Stable Freeze Before Feature Work

**SYMPTOM:** Continuous feature churn after acceptance risked undocumented drift.  
**ROOT CAUSE:** No freeze boundary after operator acceptance.  
**FIX:** 2026-08-17 PRODUCTION STABLE freeze; further changes require new phase.  
**GENERAL LESSON:** Accepted contours need a hard stop.  
**REUSABLE RULE:** Freeze baseline before starting the next behavior phase.

## 20. Whitespace Collapse Before Durable Store

**SYMPTOM:** Original line structure / URL lines lost before callback.  
**ROOT CAUSE:** Aggressive normalization before RAW persist.  
**FIX:** Capture full visible body with structure-preserving conversion first.  
**GENERAL LESSON:** Forensic source must precede operational cleanup.  
**REUSABLE RULE:** Do not collapse source whitespace before durable RAW storage.


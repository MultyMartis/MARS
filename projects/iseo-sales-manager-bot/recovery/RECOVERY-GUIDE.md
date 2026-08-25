# Recovery Guide

## Scenario 1 — Gmail Intake Loses Full Source

**DETECTION:** Raw response is snippet-like, truncated, or missing original structure.  
**SAFE ACTION:** Check Gmail fetch mode and parser source capture. Restore full body mode.  
**DATA AT RISK:** RAW source fidelity for affected new leads.  
**RECOVERY:** Classify lossy records; for legacy/affected records, use READ-only Gmail fallback by `source_message_id` when eligible.  
**VALIDATION:** New safe intake stores full visible source in RAW.  
**ESCALATE:** If Gmail body is unavailable or credentials fail.

## Scenario 2 — Raw Callback Shows CLEAN

**DETECTION:** `📄 Исходная заявка` displays normalized labels/card content.  
**SAFE ACTION:** Stop using CLEAN as raw source.  
**DATA AT RISK:** Source UX truth, not necessarily lifecycle.  
**RECOVERY:** Restore RAW-by-`lead_id` lookup and literal renderer.  
**VALIDATION:** Raw click displays original wording and does not mutate status.  
**ESCALATE:** If RAW is missing for current records.

## Scenario 3 — Sheets 429 On Callback

**DETECTION:** n8n/Sheets errors or slow raw callback during broad reads.  
**SAFE ACTION:** Avoid broad sheet reads.  
**DATA AT RISK:** Callback availability.  
**RECOVERY:** Use filtered lookup by `lead_id`; retry conservatively.  
**VALIDATION:** Raw callback returns source for one scoped lead.  
**ESCALATE:** If Sheets API quota remains exhausted.

## Scenario 4 — Duplicate Lead Or Duplicate Card

**DETECTION:** Same Gmail source appears as multiple leads or cards.  
**SAFE ACTION:** Do not delete records. Inspect dedupe keys and delivery stamps.  
**DATA AT RISK:** Manager trust and lifecycle consistency.  
**RECOVERY:** Mark one record authoritative through explicit forensic decision; repair events if chartered.  
**VALIDATION:** Same source no longer re-ingests as new.  
**ESCALATE:** If source identity cannot be proven.

## Scenario 5 — Telegram Callback Cannot Resolve Lead

**DETECTION:** Button click returns error or mutates wrong/no lead.  
**SAFE ACTION:** Stop guessing from broad data.  
**DATA AT RISK:** Lifecycle correctness.  
**RECOVERY:** Inspect callback token and card message identity; restore `lead_id` resolution.  
**VALIDATION:** Processed/spam/raw actions target intended lead.  
**ESCALATE:** If callback data is irrecoverably ambiguous.

## Scenario 6 — Reminder Missed

**DETECTION:** Expected reminder not observed at natural window.  
**SAFE ACTION:** Check CONFIG, timezone, weekday gate, n8n schedule, and execution logs.  
**DATA AT RISK:** Manager awareness; lifecycle should remain intact.  
**RECOVERY:** Fix schedule/config path. Do not mutate lead statuses to compensate.  
**VALIDATION:** Next natural or explicitly chartered synthetic reminder behaves correctly.  
**ESCALATE:** If n8n scheduler or credentials fail.

## Scenario 7 — Reminder Includes Wrong Leads

**DETECTION:** Processed/spam/test/archive lead appears in reminder.  
**SAFE ACTION:** Pause reminder delivery if repeated and harmful.  
**DATA AT RISK:** Manager noise and trust.  
**RECOVERY:** Fix candidate query and status exclusions.  
**VALIDATION:** Candidate list includes only still-actionable pending real leads.  
**ESCALATE:** If lifecycle statuses are inconsistent.

## Scenario 8 — AI Unexpectedly Enabled

**DETECTION:** CONFIG `ai_enabled` is true or OpenRouter node runs.  
**SAFE ACTION:** Disable AI path.  
**DATA AT RISK:** Deterministic stable behavior.  
**RECOVERY:** Restore AI OFF baseline and inspect affected outputs.  
**VALIDATION:** Processing is deterministic and OpenRouter disabled.  
**ESCALATE:** If AI changed production data.

## Scenario 9 — Sheets Unavailable

**DETECTION:** RAW/CLEAN/CONFIG reads or writes fail.  
**SAFE ACTION:** Fail closed for writes and risky admin actions.  
**DATA AT RISK:** Intake persistence, lifecycle, reminders.  
**RECOVERY:** Restore Sheets access; replay only from proven safe sources with explicit charter.  
**VALIDATION:** RAW/CLEAN writes and CONFIG reads succeed.  
**ESCALATE:** If data loss is suspected.

## Scenario 10 — Unauthorized Telegram Access

**DETECTION:** Unknown user can trigger admin/callback behavior.  
**SAFE ACTION:** Disable risky admin path or tighten authorization.  
**DATA AT RISK:** Lifecycle integrity and confidentiality.  
**RECOVERY:** Fix authorization config/check. Audit events.  
**VALIDATION:** Unauthorized user receives safe denial.  
**ESCALATE:** If secret/token compromise is suspected.


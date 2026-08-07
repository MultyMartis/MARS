# PHASE-1B-D6G1 — Scheduled Silence Forensic, Server-Side Completion Dispatch and Windows Poller Removal

## Verdict summary

Today’s scheduled SITE-002 import **did run** (`mars-20260807-080002-5bbdaf1c`) and wrote a terminal ATTENTION result, but Windows completion polling failed (FTP secret parse + visible `powershell.exe` poller). No Telegram was delivered until server-side completion dispatch was implemented. Normal delivery is now **server-side and completion-driven**; the Windows completion poller is **DISABLED_AND_RETIRED**.

## Root cause labels

- Primary: `COMPLETION_POLLER_FAILED` + `COMPLETION_POLLER_TERMINAL_NOT_VISIBLE`
- Contributing: `WATCHDOG_FALSE_SKIP`
- Architecture latent: workstation dependency for normal reporting
- Multi-cause gate: `SILENCE_MULTI_CAUSE`

## Implemented

- `mars_1c_completion_dispatch.php` + wrapper v1.3.0 hook after atomic terminal write
- Idempotent delivered marker + Data Table/event_id
- Failure durability statuses PENDING/SENDING/SENT/FAILED_RETRYABLE/FAILED_FINAL (one immediate attempt; bounded recover sweep)
- Secrets via non-Git local config
- Server watchdog + tokenized HTTP gateway
- Admin report UI label (Отчёт)
- Windows poller disabled; Windows watchdog disabled

## Acceptance

Manual admin import `mars-20260807-114238-7cb452ec` with poller disabled → server SENT → n8n `24972` → factual Russian ATTENTION (offers missing).

Evidence: `evidence/phase-1b-d6g1-scheduled-silence-server-dispatch/`

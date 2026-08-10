# REOPEN ACK ROUTING REPAIR — Phase 3H.7.2

## Root cause
`Aggregate Card Sync Result` treated any successful non-spam `applied` as processed, overwriting Handle reopen ack when `new_status=pending`.

## Fix
- Aggregate routes by event_type / last_manager_action / action / new_status
- Handle reopen text → «Лид возвращён в обработку.»
- Idempotent processed/spam texts → contract already-* strings

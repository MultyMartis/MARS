# REOPEN IDEMPOTENCY — Phase 3H.7.1

Handle Callback reopen path:
- if already pending → answer `Заявка уже находится в обработке.` + event `manager_reopen_duplicate_ignored`
- reopen events added once on applied transition
- sheet harness reopen event counts = 1 per fixture lead

# Current Import Lifecycle (pre-D6G → D6G)

1. Trigger: SCHEDULED (Beget) or ADMIN_MANUAL (OpenCart)
2. Canonical runner `mars_1c_import_wrapper.php` v1.2.0
3. Shared singleton lock
4. Unique run_id + run-state.json
5. Catalog phase → Offers phase
6. Authoritative terminal.json (SUCCESS / ATTENTION_OFFERS_INPUT_MISSING / ATTENTION_COMPLETED_WITH_WARNINGS / FAILED)
7. dispatch-inbox marker
8. Windows completion poller/dispatcher → n8n → Telegram
9. Separate no-import watchdog after expected window

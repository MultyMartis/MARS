# Rollback plan (not executed)

1. Disable producer task
2. Restore prior workflow version dc8746bf-df9c-425d-9b3f-4ace452ac5ef (or prior known good)
3. Restore producer runtime to e1d2a178… if needed
4. Revert runtime-state wrapper secret alias / EXPECTED_VERSION if required
5. Validate wrapper syntax + kill switch ENABLED
6. Reactivate workflow if needed
7. Enable producer; verify no Running tasks

Preserve: Data Table rows, Telegram messages, forensic evidence, PENDING historical row.

Token: D6F1A_ROLLBACK_PLAN_READY

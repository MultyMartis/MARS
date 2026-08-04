# STABLE REACTIVATION CODE v1

- Revoked moderators retain the same accessCode(telegram_user_id).
- /moderator_add CODE restores the existing ACCESS_CONTROL row.
- No duplicate user row; no new approval code.
- Lead delivery resumes only after role/status become active moderator.
- No historical lead backfill.
- Idempotent repeat add remains safe.
- This phase does not restore Olya or Nikita.

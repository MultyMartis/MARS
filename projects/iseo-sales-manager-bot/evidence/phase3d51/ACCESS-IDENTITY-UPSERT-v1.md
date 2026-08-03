# ACCESS IDENTITY UPSERT v1

Rules enforced:

1. Match exact telegram_user_id
2. Update same row when found
3. Username changes do not create a second row
4. Username collision never merges different IDs
5. Preserve first_seen_at on update
6. Refresh username / display_name / last_seen_at
7. One Telegram user ID → one ACCESS_CONTROL row
8. Ambiguous duplicate active identities → stop for forensic review

Live repair: append path used (registry was empty). Re-run path uses A:O range update by ID.

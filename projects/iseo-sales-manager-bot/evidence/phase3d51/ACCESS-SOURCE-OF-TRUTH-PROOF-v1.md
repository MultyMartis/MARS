# ACCESS SOURCE OF TRUTH PROOF v1

Precedence after Phase 3D.5.1:

1. Explicit ACCESS_CONTROL row always wins
2. Revoked/blocked registry row denies access (CONFIG cannot re-authorize)
3. Admin bootstrap only when registry read fails technically AND sender is bootstrap Admin
4. No moderator fail-open on registry technical failure
5. manager_action_user_ids is **not** an active authorization source

Harness proofs: tests 17–24, 29 PASS (34/34).

Live Admin.dev Check User Authorization code includes `ADMIN_BOOTSTRAP` and removes moderator CONFIG fallback.

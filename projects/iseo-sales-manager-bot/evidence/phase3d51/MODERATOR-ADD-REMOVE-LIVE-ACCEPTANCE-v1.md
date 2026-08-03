# MODERATOR ADD/REMOVE LIVE ACCEPTANCE v1

Synthetic pending user (not Olya):

1. public/pending row
2. `/moderator_pending` lists opaque code
3. `/moderator_add CODE` → moderator/active
4. callback allowed
5. `/moderator_remove CODE` → revoked
6. callback denied
7. idempotent add/remove
8. no workflow edit / no CONFIG edit

Acceptance synth_add_remove PASS.

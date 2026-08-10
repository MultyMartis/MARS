# ARCHIVE / CURRENT SEPARATION

Expand v1.2 excludes delivery_key/reason containing `archive` or `pending_view`.
Archive /leads cards are not authoritative current production sync targets.
Callbacks from archive may mutate lead state but sync must target the four current production cards only.

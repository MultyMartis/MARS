# PG shadow read tests

After synthetic cleanup, read-only smoke counts (wave run `20260903T093419Z`):

| Relation | Count (approx, shadow) |
|---|---|
| leads | 65 |
| inbound_events | 59 |
| deliveries | 264 |
| access_rules is_active | 1 |

No mutation of migrated real shadow business rows in success path.  
Synthetic `v3test_%` rows deleted after tests.

`get_active_config` / access recipient listing available to `iseo_runtime` via migration `0005`.

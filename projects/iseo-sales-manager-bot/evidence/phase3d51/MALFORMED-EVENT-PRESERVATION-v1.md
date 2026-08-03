# MALFORMED EVENT PRESERVATION v1

Live pre-repair ACCESS_EVENTS contained **2 well-formed seed rows** (Phase 3D.5 bootstrap). No numeric role/status rows were present in the live tab at forensic time.

Policy applied:

- Do **not** delete historical ACCESS_EVENTS rows
- Append compensating `registry_identity_migrated` events with outcome `mapping_repaired`
- Distinguish original seed events vs compensating repair events

Operator XLSX export remains stale evidence of the empty ACCESS_CONTROL defect; production Google Sheet is authoritative after repair.

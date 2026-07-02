# FP-0002 V8 O-Centre DEC-01 Desktop Mobile Map v1

**Decision:** `ONE_SHARED_FILE`

- Desktop node `1:2440` and mobile node `1:5697` share image ref `d3ac7d00af36`.
- Both visible at opacity 0.1 as section background fill.
- Different rendered bounds are CSS layout/crop concerns — not separate canonical resources.
- Hidden 40×41 screenshot nodes excluded from production.

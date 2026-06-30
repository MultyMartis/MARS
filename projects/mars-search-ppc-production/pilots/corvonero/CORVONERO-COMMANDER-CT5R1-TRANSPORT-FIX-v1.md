# CORVONERO COMMANDER CT-5R1 TRANSPORT FIX v1

## Root cause

- **Callout serialization:** `payload-builder.mjs` joined callouts with `;;` instead of Commander-native `||`.
- **URL construction:** `payload-builder.mjs` injected per-ad UTM query parameters; operator policy requires clean landing URLs only.

## Architectural decision

- Clean landing URL: authority / payload input
- Global UTM: not represented in individual ad URL
- Callouts: structured array in authority; `||` serialization only at transport patch boundary

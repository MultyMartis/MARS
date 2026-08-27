# SOAK-RESET-v1

## Previous soak

| Field | Value |
|-------|--------|
| Prior T+0 commit | `a6b3dceb` |
| Status after this wave | **INVALID** |

## Reason

```
SOAK RESET REQUIRED — DUPLICATE ALL KEYBOARD REGRESSION PATCH
```

Production Admin.dev behavior changed (keyboard slot emission + exact-size Telegram nodes). Prior 48h soak hours must not be counted.

## After PASS

```
READY FOR NEW 48H SOAK T+0
```

Do **not** auto-start the new soak in this repair task unless the operator explicitly authorizes restart.

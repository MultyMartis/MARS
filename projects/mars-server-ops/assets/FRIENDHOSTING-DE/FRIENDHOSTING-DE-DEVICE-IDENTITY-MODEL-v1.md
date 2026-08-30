# FRIENDHOSTING-DE — Per-device VLESS identity model v1

**inventory_ref:** FRIENDHOSTING-DE  
**Status:** **CANONICAL**  
**Secrets:** no UUIDs / URIs / QR payloads in this file  

---

## 1. Model

```text
One shared inbound (:8443 VLESS + TLS + RAW)
  × one independent VLESS identity per physical device
```

| Rule | Detail |
|------|--------|
| Shared UUID across devices | **No longer canonical** |
| Preferred operator UX | 3X-UI native QR / copy-link |
| Local files | Backup / registry / recovery only |
| Display pattern | `<DEVICE>-FRIENDHOSTING-DE-RAW-8443` |

**Why shared UUID is retired:** revocation, rotation, and lost-device response require independent identity. Shared credentials force all-or-nothing blast radius.

---

## 2. Current safe labels

| Label | Physical status |
|-------|-----------------|
| WSP-ONE | **PASS** (accepted workstation path) |
| MCA-PHONE | **PASS** |
| Unit-01 | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| Unit-02 | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| Unit-03 | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| Unit-MichaelPhone | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |

Live client count on server: **6**.

---

## 3. Legacy

| Identity | Status |
|----------|--------|
| MCA-ONE-FRIENDHOSTING-DE-RAW-8443 | **RETIRED / REMOVED FROM SERVER** (P3.1, 2026-08-30) |
| Local MCA-ONE folder | PRESERVED + MARKED RETIRED (local contour) |

---

## 4. Procedures (pointers)

| Action | Where |
|--------|-------|
| Revoke lost device | [../../runbooks/FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md](../../runbooks/FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md) |
| Rotate compromised device | same runbook |
| Create / export client | [../../runbooks/FRIENDHOSTING-3XUI-OPERATOR-RUNBOOK-v1.md](../../runbooks/FRIENDHOSTING-3XUI-OPERATOR-RUNBOOK-v1.md) |

### Replacement-device (summary)

1. Create new client on same `:8443` inbound with new label/UUID.  
2. Export via 3X-UI QR/link.  
3. Test egress `92.42.99.126` + required apps.  
4. Disable/delete old client only after PASS.  
5. Update local registry; do not change transport/SNI/port.

### Lost-device (summary)

1. Disable/delete **only** that client.  
2. Confirm remaining clients and `:8443` health.  
3. Mark local secrets REVOKED; destroy/archive per local policy.

---

## 5. Related reports

- [../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01.md](../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01.md)  
- [../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01.md](../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01.md)

---

*Identity model v1 · 2026-08-30.*

# FriendHosting — Device VLESS identity revocation & rotation

**inventory_ref:** FRIENDHOSTING-DE  
**Scope:** Per-device VLESS clients on accepted inbound `:8443` (VLESS + TLS + RAW)  
**Status:** documented human-operated procedure — **not** automation  
**Secrets:** never paste UUIDs/URIs into Git, chat, or REPORT bodies  

**Related:** [SERVER-INVENTORY-v1.md](../SERVER-INVENTORY-v1.md) · local registry `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\`

---

## 1. Model

| Rule | Detail |
|------|--------|
| One inbound | Shared accepted `:8443` endpoint |
| One UUID per device | Independent revoke/rotate |
| Legacy fallback | **RETIRED** (P3.1 closeout 2026-08-30) — `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` removed from server; local folder PRESERVED+MARKED |
| Local secrets | Device folders under `...\FRIENDHOSTING-GERMANY\clients\<DEVICE>\` |

---

## 2. Device revocation (lost / retired device)

1. Identify exact client **display email** (e.g. `Unit-02-FRIENDHOSTING-DE-RAW-8443`) from inventory/report — **not** by guessing UUID.
2. Pre-change: confirm SSH `:3333`, Xray `:8443`, other devices still needed.
3. Optional scoped backup of `/etc/x-ui/x-ui.db` (+ note timestamp).
4. In 3X-UI (or equivalent DB edit with charter): **disable or delete only that client**.
5. Restart/reload x-ui if required by panel; confirm Xray still listens `:8443`.
6. Confirm remaining clients still listed/enabled (esp. other devices). Legacy MCA-ONE fallback no longer exists after P3.1.
7. Update local registry status for that device (`REVOKED`); archive or destroy local `.vless.txt` / `.json` per local secret policy.
8. Do **not** rotate unrelated device UUIDs.

---

## 3. Planned rotation (compromised or scheduled re-key)

1. **Add** a replacement client on the same `:8443` inbound (new UUID, new display label if needed).
2. Create local profile artifacts for the replacement.
3. Import/test replacement on the target device (egress `92.42.99.126`, HTTPS, real apps as required).
4. After PASS: **disable** the old client only.
5. Validate Xray + remaining identities.
6. Archive old local secret files; update registry.

Never “rotate everyone” because one device failed.

---

## 4. What not to do

- Do not change port, TLS, SNI, or transport while rotating a single device.
- Do not revive the retired shared MCA-ONE identity as canonical.
- Do not copy FriendHosting UUIDs onto EQVPS/VEESP without a separate identity charter.
- Do not commit client URI/UUID files to Git.

---

*FriendHosting P3 per-device identity · amended after P3.1 retirement · documentation consolidation 01 · 2026-08-30*

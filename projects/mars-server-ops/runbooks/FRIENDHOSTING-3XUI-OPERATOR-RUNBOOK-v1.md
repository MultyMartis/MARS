# FriendHosting — 3X-UI operator runbook v1

**inventory_ref:** FRIENDHOSTING-DE  
**Panel version behaviour:** 3X-UI **3.7.0** (as exercised in P3)  
**Status:** human-operated UX runbook  
**Secrets:** never paste panel URL path, passwords, UUIDs, VLESS URIs, or QR payloads into Git / REPORT / chat archives  

---

## 1. How to open the panel

1. Use the operator bookmark or local secret note for the **authenticated HTTPS URL** (`metacode-cloud.com:443` + secret path).  
2. Authenticate with panel credentials from the local secret contour.  
3. Confirm you are on FriendHosting (not EQVPS/VEESP) before editing clients.

Do **not** browse to `:2096` or ask to open `:2096` in UFW.

---

## 2. Where to find clients

1. Open **Inbounds**.  
2. Select inbound remark **`FRIENDHOSTING-DE-RAW-8443`** (VLESS + TLS + RAW/TCP `:8443`).  
3. Open that inbound’s **client list**.

Clients are distinguished by **display email / remark labels**, not by reading UUIDs aloud.

---

## 3. How to distinguish clients

| Safe label | Typical display pattern |
|------------|-------------------------|
| WSP-ONE | `WSP-ONE-FRIENDHOSTING-DE-RAW-8443` |
| MCA-PHONE | `MCA-PHONE-FRIENDHOSTING-DE-RAW-8443` |
| Unit-01 … Unit-03 | `Unit-0N-FRIENDHOSTING-DE-RAW-8443` |
| Unit-MichaelPhone | `Unit-MichaelPhone-FRIENDHOSTING-DE-RAW-8443` |

Canonical model: [../assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-DEVICE-IDENTITY-MODEL-v1.md](../assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-DEVICE-IDENTITY-MODEL-v1.md)

---

## 4. Copy QR / link (preferred UX)

1. Select **exactly one** client.  
2. Use the native **QR** and/or **copy link** control for that client.  
3. Import into the device client (e.g. v2rayN) as a **new** profile.  
4. Activate and smoke-test egress `92.42.99.126`.

**Do not** treat local `clients\` files as the primary way to provision a device. Local files are backup/registry.

---

## 5. Create a new per-device client

1. Confirm charter / need (new physical device).  
2. On inbound `:8443`, **add client** with unique display label following the naming pattern.  
3. Leave transport/TLS/SNI/port unchanged.  
4. Export via native QR/link.  
5. Record status in local registry (SERVER_IDENTITY_READY → DEVICE_TEST_PENDING until physical PASS).  
6. Do **not** share UUIDs into Git.

---

## 6. Disable / revoke one client

1. Identify exact display label.  
2. Optional scoped backup of panel DB if charter requires.  
3. **Disable or delete only that client**.  
4. Confirm `:8443` still healthy and other clients remain.  
5. Update local registry to REVOKED.

Detail: [FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md](FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md)

---

## 7. Rotate one device

1. **Add** replacement client first.  
2. Provision device; PASS smoke/real apps as required.  
3. **Then** disable old client.  
4. Never rotate all devices because one failed.  
5. Never change Reality/WS/gRPC/MTU during a simple identity rotation.

---

## 8. Why local files are not primary UX

P3 established that 3X-UI native share reconstruction matches known-good profiles when panel fields are correct. Operator speed and fewer stale-file mistakes favor panel QR/copy-link. Local artifacts remain for:

- offline recovery;  
- inventory of which labels exist;  
- restore after panel loss.

---

## 9. Do not expose `:2096`

`:2096` may listen process-side but is **UFW DENY** by design (**ACCEPTED HARDENED BOUNDARY**). Convenience is not a reason to publish it. Use nginx `:443` + secret path.

---

## 10. Post-change regression (minimum)

After any client create/disable/rotate:

- SSH `:3333` reachable  
- nginx `:443` TLS OK  
- Xray `:8443` TCP/TLS OK  
- Remaining needed clients still enabled  
- Spot-check WSP-ONE if workstation ops continue  

---

*3X-UI operator runbook v1 · FriendHosting P3 UX · 2026-08-30.*

# REPORT — FriendHosting P3 Per-Device VLESS Identities 01

**Programme:** MARS Server Ops & VPS Forge  
**Wave:** FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01  
**Date (UTC):** 2026-08-30  
**Target:** FRIENDHOSTING-DE / `92.42.99.126` / `metacode-cloud.com` / SSH `:3333`  
**Git:** no commit / no push  

> **Amendment (P3.1, 2026-08-30):** Legacy identity `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` was **RETIRED** (server deleted) under operator charter. Canonical live client count is now **6**. Closeout: [MARS-SERVER-OPS-FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01.md](MARS-SERVER-OPS-FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01.md). Sections below remain the historical P3 creation record (7-client interim state).

**Mutations this wave:** VEESP = 0 · EQVPS = 0 · FriendHosting `:8443` architecture = 0 · FriendHosting legacy identity deletion = 0 · FriendHosting new client additions = **6** · reboot = 0 · firewall = 0 · SSH = 0 · Windows network before operator smoke = 0 · secret disclosure = 0 · Foreign WIP = 0  

---

## 1. Executive verdict

| Gate | Result |
|------|--------|
| **P3 SERVER MODEL** | **PASS** |
| Independent clients created | **6** (+ 1 legacy preserved = **7** total on `:8443`) |
| UUID uniqueness (new + disjoint from legacy) | **PASS** |
| `:8443` architecture unchanged | **PASS** (VLESS + TLS + RAW/TCP; SNI `metacode-cloud.com`; flow empty; sniffing OFF) |
| Legacy fallback preserved / enabled | **YES** |
| Xray / listeners healthy post-change | **PASS** |
| Local profiles structurally valid | **PASS** |
| **P3 CURRENT-WORKSTATION NEW IDENTITY smoke** | **PENDING OPERATOR** |
| Other devices application acceptance | **DEVICE_TEST_PENDING** |
| **P3 3X-UI Operator Client UX** | **PASS** (native QR/copy-link; WSP-ONE export structurally matches known-good MARS profile) |

**FRIENDHOSTING P3 PER-DEVICE IDENTITIES: PARTIAL** — server model + 3X-UI operator UX complete; workstation new-identity smoke blocked on operator import/test **from 3X-UI** (not local files).

---

## 2. Why per-device identities

Shared/general-client UUID prevents safe revoke/rotate for a single lost device and blocks traffic attribution. P3 moves FriendHosting toward **one independent VLESS identity per approved device** on the **already accepted** `:8443` endpoint, without opening reserve `:24443`.

---

## 3. Source device inventory

| Source | Role |
|--------|------|
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\` | **Authoritative current fleet folders** |
| [EQVPS-MICRO-IP-operator-client-runbook-v1.md](../assets/EQVPS-MICRO-IP/EQVPS-MICRO-IP-operator-client-runbook-v1.md) | Approved production device list (six) |
| FriendHosting local `clients\MCA-ONE\` | Existing FH working profile |
| Task charter speculative names (`WSP-PHONE`, `Unit Metallka`) | **Not** provisioned — see §4 |

EQVPS client folders present: `MCA-ONE`, `MCA-PHONE`, `Unit-01`, `Unit-02`, `Unit-03`, `Unit-MichaelPhone`.

---

## 4. Device-name reconciliation

| Physical / role | EQVPS approved name | FriendHosting LEGACY label | FriendHosting P3 NEW label | Notes |
|-----------------|---------------------|----------------------------|----------------------------|-------|
| Primary Windows workstation | MCA-ONE | `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` | `WSP-ONE-FRIENDHOSTING-DE-RAW-8443` | Same machine; **not merged**. NEW uses `WSP-ONE` to avoid colliding with legacy email/remarks. |
| Phone | MCA-PHONE | — | `MCA-PHONE-FRIENDHOSTING-DE-RAW-8443` | EQVPS name retained |
| Unit-01 | Unit-01 | — | `Unit-01-FRIENDHOSTING-DE-RAW-8443` | |
| Unit-02 | Unit-02 | — | `Unit-02-FRIENDHOSTING-DE-RAW-8443` | |
| Unit-03 | Unit-03 | — | `Unit-03-FRIENDHOSTING-DE-RAW-8443` | |
| Unit-MichaelPhone | Unit-MichaelPhone | — | `Unit-MichaelPhone-FRIENDHOSTING-DE-RAW-8443` | |
| WSP-PHONE (charter mention) | maps → MCA-PHONE | — | **not used as display** | Naming generation alias only |
| Unit Metallka (charter mention) | **not in EQVPS approved six** | — | **not created** | Explicitly unprovisioned historically |

**Do not treat MCA-ONE and WSP-ONE as interchangeable labels in tooling:** MCA-ONE = legacy FH profile; WSP-ONE = P3 workstation identity for the same physical operator workstation.

---

## 5. Pre-mutation health

| Check | Result |
|-------|--------|
| SSH `:3333` | PASS |
| nginx `:443` TLS | PASS |
| 3X-UI localhost `:20901` listen + active | PASS (HTTP probe; panel bound localhost) |
| Xray `:8443` TCP + TLS | PASS |
| Legacy client present | PASS (`MCA-ONE-FRIENDHOSTING-DE-RAW-8443`) |
| Inbound before change | 1 inbound · 1 client · network `tcp` · security `tls` · SNI `metacode-cloud.com` · sniffing `enabled=false` · flow empty |

Evidence: `evidence/FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01/A0-pre-health*.json|txt`

---

## 6. P3 backup/restore

| Item | Value |
|------|-------|
| Remote | `/root/mars-backups/friendhosting-p3-pre-device-identities-20260830T105341Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-p3-pre-device-identities-20260830T105341Z.tgz` |
| Size | 80676164 bytes |
| SHA-256 match | **YES** (`dbdc2da0…eaa2`) |
| Contents | `/etc/x-ui`, `x-ui.db`, `/usr/local/x-ui`, xray config snapshot, clients-safe list, nginx/LE/ufw/fail2ban/ssh snapshots |
| Restore strategy | **CONFIRMED** — `B1-RESTORE-STRATEGY.md` (+ local twin `-RESTORE-STRATEGY.md`) |

**BACKUP + RESTORE STRATEGY CONFIRMED** before client additions.

Note: a concurrent second backup attempt (`…105530Z`) was aborted mid-SFTP; incomplete local twin removed. Canonical P3 pre-mutation backup remains `…105341Z`.

---

## 7. Current `:8443` client model (after P3)

| Field | Value |
|-------|-------|
| Inbound remark | `FRIENDHOSTING-DE-RAW-8443` |
| Port | 8443 |
| Protocol | vless |
| Transport | tcp (RAW) |
| TLS | yes |
| SNI | metacode-cloud.com |
| Flow | empty (all clients) |
| Sniffing | OFF |
| Clients | **7** (1 legacy + 6 new) |

---

## 8. Legacy fallback identity

| Item | Value |
|------|-------|
| Display | `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` |
| Status | **LEGACY-FALLBACK / MIGRATION SAFETY NET** |
| Enabled | **YES** |
| Edited UUID | **NO** |
| Deleted in P3 | **NO** |
| Local path | `...\clients\MCA-ONE\` |

---

## 9. New identity model

Pattern: `<DEVICE>-FRIENDHOSTING-DE-RAW-8443` on the **same** inbound.  
No second inbound. No Reality/WS/gRPC/XHTTP. No `:24443`.

---

## 10. New clients created

| # | Display name | Device folder | Status |
|---|--------------|---------------|--------|
| 1 | WSP-ONE-FRIENDHOSTING-DE-RAW-8443 | WSP-ONE | SERVER_CLIENT_CREATED · CURRENT_WORKSTATION_SMOKE_PENDING |
| 2 | MCA-PHONE-FRIENDHOSTING-DE-RAW-8443 | MCA-PHONE | SERVER_CLIENT_CREATED · DEVICE_TEST_PENDING |
| 3 | Unit-01-FRIENDHOSTING-DE-RAW-8443 | Unit-01 | SERVER_CLIENT_CREATED · DEVICE_TEST_PENDING |
| 4 | Unit-02-FRIENDHOSTING-DE-RAW-8443 | Unit-02 | SERVER_CLIENT_CREATED · DEVICE_TEST_PENDING |
| 5 | Unit-03-FRIENDHOSTING-DE-RAW-8443 | Unit-03 | SERVER_CLIENT_CREATED · DEVICE_TEST_PENDING |
| 6 | Unit-MichaelPhone-FRIENDHOSTING-DE-RAW-8443 | Unit-MichaelPhone | SERVER_CLIENT_CREATED · DEVICE_TEST_PENDING |

---

## 11. Local client-artifact structure

Root: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\`

Per device (new):

- `friendhosting-de-raw-8443.json`
- `friendhosting-de-raw-8443.vless.txt`
- `meta.local.json`

Plus: `REGISTRY.local.json` (local-only).

---

## 12. Profile validation

For each new profile (structural):

| Check | Result |
|-------|--------|
| server `metacode-cloud.com` | PASS |
| port 8443 | PASS |
| VLESS + TLS + tcp | PASS |
| SNI `metacode-cloud.com` | PASS |
| flow empty | PASS |
| Reality/WS/gRPC/XHTTP absent | PASS |
| UUID present + unique among new | PASS |
| Disjoint from legacy UUID | PASS |

Evidence: `R2-profile-validation.json`

---

## 13. Current workstation migration

| Item | Value |
|------|-------|
| Mapping | Physical MCA-ONE workstation → NEW display **WSP-ONE-FRIENDHOSTING-DE-RAW-8443** |
| NEW profile path | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\WSP-ONE\friendhosting-de-raw-8443.json` |
| NEW VLESS file | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\WSP-ONE\friendhosting-de-raw-8443.vless.txt` |
| Legacy profile | **not overwritten** |

---

## 14. Operator smoke

**STOP — awaiting operator.**

1. Import **NEW** profile `WSP-ONE-FRIENDHOSTING-DE-RAW-8443` into v2rayN **without deleting** `MCA-ONE-FRIENDHOSTING-DE-RAW-8443`.
2. Activate NEW profile.
3. Run:

```text
curl.exe -x http://127.0.0.1:10808 https://api.ipify.org
```

Expected: `92.42.99.126`

```text
curl.exe -x http://127.0.0.1:10808 -I https://www.google.com
```

4. Real apps: ChatGPT · YouTube playback · Cursor.

Do not continue programme until operator reports NEW identity PASS (or FAIL with evidence).

---

## 15. Other device migration status

All non-workstation new profiles: **PROFILE_READY** + **SERVER_CLIENT_CREATED** + **DEVICE_TEST_PENDING**.  
No APPLICATION PASS claimed.

---

## 16. Revocation model

Documented: [runbooks/FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md](../runbooks/FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md)

Logic: identify exact device client → disable/remove **only that UUID** → validate Xray → confirm peers → update local registry.

---

## 17. Rotation model

Same runbook: add replacement → test → disable old → validate → archive local secrets. No fleet-wide rotate.

---

## 18. Server regression

| Check | Result |
|-------|--------|
| SSH `:3333` | PASS |
| nginx `:443` | PASS |
| Xray `:8443` TCP/TLS | PASS |
| x-ui active | PASS |
| Legacy enabled | YES |
| New clients present/enabled | YES |
| Architecture drift | NONE observed |

---

## 19. Secret boundary

UUIDs/URIs live only under `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\`.  
Git evidence/report contain display names, paths, statuses — **no** UUID/URI/QR/panel passwords/SSH private keys.

---

## 20. Inventory/runbook updates

- [SERVER-INVENTORY-v1.md](../SERVER-INVENTORY-v1.md) — P3 identity model note  
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) — P3 status + next (operator smoke → P4)  
- Revocation/rotation runbook created (above)

---

## 21. Remaining migration work

1. Operator: NEW workstation identity smoke (egress + HTTPS + ChatGPT/YouTube/Cursor).  
2. Per-device tests on MCA-PHONE / Unit-* when available.  
3. Later charter: retire legacy MCA-ONE only after fleet proven.  
4. Do **not** create `:24443` until P4 charter.

---

## 22. Next-wave recommendation

**P4 — FRIENDHOSTING RESERVE RAW/TLS INBOUND `:24443`**  
Same provider/domain/TLS family; VLESS+TLS+RAW; compatible per-device identity model. **Not started in P3.**

---

## 23. Evidence paths

| Path | Role |
|------|------|
| `projects/mars-server-ops/evidence/FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01/` | Git-safe evidence |
| `local/infrastructure/FRIENDHOSTING-GERMANY/p3-per-device-identities-01-20260830T105341Z/` | Local run (backup wave) |
| `local/infrastructure/FRIENDHOSTING-GERMANY/p3-per-device-identities-01-resume-20260830T110451Z/` | Local resume (profiles) |
| `local/infrastructure/FRIENDHOSTING-GERMANY/backups/friendhosting-p3-pre-device-identities-20260830T105341Z.tgz` | Secret-bearing backup twin |
| `tools/friendhosting-p3/p3-per-device-identities-01.py` | Mutation helper |
| `tools/friendhosting-p3/p3-per-device-identities-01-resume.py` | Resume helper |

---

## 24. Mutation/Git closeout

| Item | Value |
|------|-------|
| FriendHosting new clients | +6 |
| FriendHosting architecture | unchanged |
| Legacy deletion | 0 |
| VEESP / EQVPS | 0 |
| commit / push | 0 |
| Foreign WIP | untouched |

---

## 3X-UI Operator Client UX

**Wave addendum:** FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01 · **PASS**

### Preferred operator interface

- **Preferred:** authenticated FriendHosting **3X-UI** (nginx panel path on `:443`) → open VLESS RAW/TLS `:8443` inbound → select named device client → native **QR / copy link** → import into v2rayN / mobile client.
- **Local secret files** under `local/infrastructure/FRIENDHOSTING-GERMANY\clients\` remain **backup / registry / recovery only** — not the preferred day-to-day profile source.
- Public subscription on `:2096` is **not** required and remains **UFW DENY**. Panel process bind: `:20901` = `127.0.0.1`; `:2096` may listen process-wide but stays firewalled.

### Critical 3X-UI 3.7.0 live-client finding (fixed this wave)

Early P3 wrote new identities into inbound `settings` JSON (and partially `client_traffics`) but **did not** register rows in 3.7 tables `clients` + `client_inbounds`. Live Xray therefore still had **only the legacy client** until this UX wave synced all seven identities into the canonical client tables and restarted x-ui/Xray generation.

**After fix:** `clients` = 7 · `client_inbounds` = 7 · inbound settings = 7 · live Xray `:8443` clients = **7**.

### Visible client labels (safe)

| Visible email / name in 3X-UI | Role | Enabled |
|-------------------------------|------|---------|
| `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` | LEGACY / FALLBACK — comment: `LEGACY FALLBACK — DO NOT DELETE YET` | YES |
| `WSP-ONE` | Current workstation NEW identity | YES |
| `MCA-PHONE` | DEVICE_TEST_PENDING | YES |
| `Unit-01` | DEVICE_TEST_PENDING | YES |
| `Unit-02` | DEVICE_TEST_PENDING | YES |
| `Unit-03` | DEVICE_TEST_PENDING | YES |
| `Unit-MichaelPhone` | DEVICE_TEST_PENDING | YES |

Legacy **email not renamed** to `LEGACY-MCA-ONE-FALLBACK` (avoids changing semantics of already-imported working profiles). Fallback purpose is documented via **comment** + this report.

UUID uniqueness across all seven: **PASS**. No UUID rotation this wave.

### Native QR / link availability

3X-UI **3.7.0** supports per-client QR and copy-link from the inbound client list (and/or Clients view bound to the inbound). Share parameters for this inbound are aligned via the `hosts` row:

- address / SNI: `metacode-cloud.com`
- port: `8443`
- security: `tls`
- ALPN: `http/1.1` (stored as JSON array in DB)
- fingerprint (client share): `chrome`
- transport: TCP / header none (inherited from inbound; not Reality)

Server-side `tlsSettings.fingerprint` remains empty (client uTLS fingerprint is share-side only).

### WSP-ONE export vs known-good MARS profile

| Check | Result |
|-------|--------|
| Native 3X-UI-style share reconstruction | **STRUCTURALLY VALID** |
| Comparison vs local known-good `clients\WSP-ONE\friendhosting-de-raw-8443.vless.txt` | **MATCH** (host/port/VLESS/TLS/SNI/ALPN/fp/type/headerType/flow/encryption; UUID equal internally, not printed) |
| Material export mismatch remaining | **NONE** after hosts ALPN JSON + fingerprint alignment |

Transient incident during hosts insert: invalid non-JSON `alpn` string briefly crashed x-ui DB init; corrected to JSON array `["http/1.1"]`; x-ui restored; Xray `:8443` returned to 7 clients. No architecture / firewall / reboot mutation.

### Operator workflow (actual 3.7.0)

1. Open FriendHosting 3X-UI (authenticated panel URL).
2. Open **Inbounds** → inbound **FRIENDHOSTING-DE-RAW-8443** (VLESS + TLS + RAW/TCP `:8443`).
3. In that inbound’s client list, select **`WSP-ONE`**.
4. Use the native **QR** and/or **copy link** control for **that** client only.
5. Import into v2rayN as a **NEW** profile; leave legacy FriendHosting profile intact.
6. Activate `WSP-ONE` and run normal smoke (egress should be `92.42.99.126`).

Other devices: same native export path; status remains **DEVICE_TEST_PENDING** until physical tests.

### Regression (post UX wave)

| Check | Result |
|-------|--------|
| SSH `:3333` | PASS |
| nginx `:443` TLS | PASS |
| 3X-UI / x-ui active | PASS |
| Xray `:8443` TCP/TLS | PASS |
| UFW `:2096` / `:20901` | DENY (unchanged) |
| Legacy preserved | YES |
| Six new clients enabled | YES |
| `:24443` | not created |

### Evidence (this addendum)

`projects/mars-server-ops/evidence/FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01/` (D12 hosts JSON fix · D13 final audit / compare).  
Tools: `tools/friendhosting-p3/p3-3xui-*.py`. Local compare artifacts stay under `local/infrastructure/FRIENDHOSTING-GERMANY\p3-3xui-operator-ux-compare\` (out of Git).

### Mutation zeros (UX wave)

VEESP = 0 · EQVPS = 0 · UUID rotation = 0 · legacy deletion = 0 · `:8443` transport/TLS/SNI/domain unchanged · `:24443` = 0 · firewall mutate = 0 · reboot = 0 · secret disclosure outside 3X-UI/local contour = 0 · commit/push = 0.

---

*End of report · STOP for operator: import **WSP-ONE** from 3X-UI native QR/copy-link (no local file browsing).*

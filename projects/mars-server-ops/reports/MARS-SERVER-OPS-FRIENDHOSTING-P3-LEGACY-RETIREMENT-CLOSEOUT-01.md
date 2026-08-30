# REPORT — FriendHosting P3.1 Legacy Identity Retirement + Migration Closeout 01

**Programme:** MARS Server Ops & VPS Forge  
**Wave:** FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01  
**Date (UTC):** 2026-08-30  
**Target:** FRIENDHOSTING-DE / `92.42.99.126` / `metacode-cloud.com` / SSH `:3333`  
**Stack:** 3X-UI 3.7.0 · Xray 26.7.28 · inbound `FRIENDHOSTING-DE-RAW-8443` (VLESS + TLS + RAW/TCP `:8443`)  
**Git:** no commit / no push  

**Mutations this wave:** VEESP = 0 · EQVPS = 0 · FriendHosting legacy deletion = **1** · remaining client mutation = 0 · `:8443` architecture = 0 · firewall = 0 · SSH = 0 · reboot = 0 · secret disclosure = 0 · Foreign WIP = 0 · commit/push = 0  

---

## 1. Executive verdict

| Gate | Result |
|------|--------|
| **P3 LEGACY RETIREMENT** | **PASS** |
| Legacy server identity removed | **YES** (`MCA-ONE-FRIENDHOSTING-DE-RAW-8443`) |
| Pre-delete → post-delete count | **7 → 6** |
| Six per-device identities survive | **PASS** (all enabled; UUIDs unique; no orphans) |
| Server regression | **PASS** |
| WSP-ONE | **PASS** (server-side active; egress observed `92.42.99.126`) |
| MCA-PHONE | **PASS** (server-side active; prior physical acceptance retained) |
| Unit-01 / 02 / 03 / MichaelPhone | **SERVER_IDENTITY_READY** · **DEVICE_TEST_PENDING** |
| **P3 PER-DEVICE VLESS MIGRATION** | **PASS / CLOSED** |

---

## 2. Operator retirement authorization

Operator charter explicitly lifted the temporary “LEGACY FALLBACK — DO NOT DELETE YET” protection and ordered deletion of **exactly** `MCA-ONE-FRIENDHOSTING-DE-RAW-8443`.

Preferred administration path: **VEESP control VPN**. This workstation egress during the wave was **`92.42.99.126`** (on FriendHosting VPN) — **not** an independent VEESP path. Fact documented; **v2rayN was not auto-switched**.

---

## 3. Pre-delete client state

Live 3X-UI / Xray audit (authority): **7** enabled clients on `:8443`.

Safe labels (exact):

1. `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` (legacy target; present exactly once)  
2. `WSP-ONE`  
3. `MCA-PHONE`  
4. `Unit-01`  
5. `Unit-02`  
6. `Unit-03`  
7. `Unit-MichaelPhone`  

UUID uniqueness verified internally (not printed). Architecture: tcp / tls / SNI `metacode-cloud.com` / remark `FRIENDHOSTING-DE-RAW-8443`.

Evidence: `evidence/FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01/A1-pre-client-audit.*`

Critical health pre-mutation: SSH `:3333`, nginx `:443`, 3X-UI, Xray `:8443`, TLS `:8443`, UFW — **PASS**. Public allow: 80 / 3333 / 443 / 8443. `:2096` denied; `:20901` blocked.

---

## 4. Backup / restore gate

**BACKUP + RESTORE STRATEGY CONFIRMED** before deletion.

| Artifact | Path | Role |
|----------|------|------|
| Remote full | `/root/mars-backups/friendhosting-p3-pre-legacy-retirement-20260830T120733Z.tgz` | Full contour (`/etc/x-ui` + `/usr/local/x-ui`); SHA-256 `4952b6368ad884be1a6737506f7f81c8464aaa28cb2e44807c038049918abac8` |
| Remote essential | `/root/mars-backups/friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz` | x-ui.db + Xray `:8443`-relevant config + safe snaps |
| **Primary local twin** | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz` | Validated twin; size ~296 KB; **7** clients including legacy |
| SHA-256 essential | `647ca4da349e26ce4617ecc9a1cf2cfc1aaf7a5c89a8fd31d9f4d1ad30ff9ddc` | Remote ↔ local **MATCH = YES** |
| Pre-delete DB snap | `/root/mars-backups/x-ui.db.p31-pre-delete-20260830T122423Z` | Immediate pre-delete DB |

**Restore (documented):** restore pre-delete `x-ui.db` (or essential/full archive) → restart/reload `x-ui` only as required → verify **7** clients including legacy → verify `WSP-ONE`. See `B1-RESTORE-STRATEGY.md` and local `*-RESTORE-STRATEGY.md`.

Note: full ~80 MB SFTP twin over hairpin FH VPN was not completed as matched local twin; **full remains remote-authoritative**. Essential twin is the SHA-matched local rollback payload for client-model restore.

---

## 5. Exact retired identity

**Deleted (exact once):** `MCA-ONE-FRIENDHOSTING-DE-RAW-8443`

Not deleted: `WSP-ONE`, `MCA-PHONE`, `Unit-01`, `Unit-02`, `Unit-03`, `Unit-MichaelPhone`.

---

## 6. Deletion method

Canonical application-model path for 3X-UI 3.7 consistency:

- Remove client from inbound `settings` JSON clients array  
- Remove matching rows from `clients`, `client_inbounds`, `client_traffics` (hosts if present)  
- `systemctl restart x-ui`  

Evidence: `C1-delete-legacy.txt` (`DELETE_OK`), `C1-deletion-method.json`.

No positional/index guess; identity matched by exact email/label. No unrelated row surgery.

---

## 7. Post-delete client model

| Check | Result |
|-------|--------|
| Client count | **6** |
| Labels | `WSP-ONE`, `MCA-PHONE`, `Unit-01`, `Unit-02`, `Unit-03`, `Unit-MichaelPhone` |
| All enabled | **YES** |
| UUID uniqueness | **PASS** |
| Legacy absent | **YES** |
| Orphan `client_inbounds` | **0** |
| Architecture | Unchanged (tcp/tls/SNI/remark) |

Evidence: `D1-post-client-audit.*`

---

## 8. 3X-UI / x-ui consistency

Settings emails ≡ `clients` table ≡ live Xray client emails (safe labels). No orphaned legacy mapping detected where inspected. Panel service active after restart.

---

## 9. Server regression

| Check | Result |
|-------|--------|
| 3X-UI | **PASS** |
| Xray | **PASS** |
| `:8443` listening + TLS | **PASS** |
| nginx `:443` | **PASS** |
| SSH `:3333` | **PASS** |
| UFW | **PASS** (allow 80/3333/443/8443; deny boundaries preserved) |
| `:2096` | denied |
| `:20901` | blocked |
| New listener / architecture / firewall / SSH / reboot | **none** |

Evidence: `D2-regression.*`

---

## 10. WSP-ONE acceptance

- Server-side: present, enabled on accepted `:8443` inbound — **PASS**  
- Post-mutation workstation egress observed: **`92.42.99.126`** — supporting evidence of FH path still active  
- Charter prior physical acceptance: **PASS**  
- Operator app re-smoke (ChatGPT / YouTube / Cursor) this session: not newly re-proven in isolation; no contradiction observed  

**WSP-ONE: PASS**

---

## 11. MCA-PHONE acceptance

- Server-side: present, enabled — **PASS**  
- Charter known physical acceptance: **PASS**  
- Live phone re-test this session: **not invented / not re-executed**  

**MCA-PHONE: PASS** (server validity + prior operator acceptance)

---

## 12. Other device status

| Label | Server identity | Physical device test |
|-------|-----------------|----------------------|
| Unit-01 | READY | DEVICE_TEST_PENDING |
| Unit-02 | READY | DEVICE_TEST_PENDING |
| Unit-03 | READY | DEVICE_TEST_PENDING |
| Unit-MichaelPhone | READY | DEVICE_TEST_PENDING |

Physical pending **does not** block identity-model closeout.

---

## 13. Local retired-secret handling

Path: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\MCA-ONE`

Policy applied: **do not blindly delete**. Status **PRESERVED+MARKED**:

- Metadata: **RETIRED — SERVER IDENTITY REMOVED**  
- Not presented as an active profile  

Evidence: `E1-local-legacy.json`

---

## 14. Final P3 identity model

| Item | Value |
|------|--------|
| Canonical client count | **6** |
| Shared inbound | `FRIENDHOSTING-DE-RAW-8443` `:8443` VLESS+TLS+RAW |
| Legacy fallback | **RETIRED** |
| Operator UX | 3X-UI primary (QR / copy-link) |
| Local `clients\` | backup / registry only |
| **P3 migration** | **PASS / CLOSED** |

---

## 15. Inventory / runbook updates

Updated:

- `projects/mars-server-ops/SERVER-INVENTORY-v1.md`  
- `projects/mars-server-ops/OPERATIONAL-INDEX.md`  
- `reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01.md` (P3.1 amendment)  
- `runbooks/FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md` (legacy retired)  

No UUIDs / URIs in Git docs.

---

## 16. Next operational backup

**Do not execute in this wave.**

**NEXT:** FRIENDHOSTING FINAL OPERATIONAL BACKUP 01  

Purpose: capture complete stable state after Plus upgrade, disk expansion, P2 hardening, ACME closure, per-device identity migration, and legacy retirement.

Then: MARS SERVER OPS FRIENDHOSTING DOCUMENTATION + KNOWLEDGE CONSOLIDATION.

**Only after those:** reconsider P4 reserve `:24443`.

---

## 17. Evidence paths

`X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01\`

Key files: `A0-*`, `A1-*`, `B1-*`, `B1b-*`, `B1c-*`, `B2-*`, `C0-*`, `C1-*`, `D1-*`, `D2-*`, `D3-*`, `E1-*`, `Z-summary.json`

Local backups under: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\`

Tools (assistive, not runtime product): `projects/mars-server-ops/tools/friendhosting-p3/p3-legacy-retirement-closeout-01*.py`

---

## 18. Git / mutation closeout

| Claim | Value |
|-------|--------|
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| FriendHosting legacy deletion | **EXACTLY 1** |
| FriendHosting remaining client mutation | **0** |
| FriendHosting `:8443` architecture mutation | **0** |
| FriendHosting firewall mutation | **0** |
| FriendHosting SSH mutation | **0** |
| FriendHosting reboot | **0** |
| Secret disclosure | **0** |
| Foreign WIP mutation | **0** |
| commit / push | **0** |

Foreign WIP remains out of scope. Default MARS closeout: **no commit, no push**.

---

*END REPORT — FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01*

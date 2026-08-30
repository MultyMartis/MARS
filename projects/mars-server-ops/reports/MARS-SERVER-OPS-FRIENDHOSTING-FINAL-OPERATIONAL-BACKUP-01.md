# REPORT — MARS SERVER OPS FRIENDHOSTING FINAL OPERATIONAL BACKUP 01

**Wave:** FRIENDHOSTING FINAL OPERATIONAL BACKUP 01  
**Date (UTC stamp):** `20260830T125003Z`  
**Target:** FRIENDHOSTING-DE / FriendHosting / `92.42.99.126` / `metacode-cloud.com` / SSH `:3333`  
**Verdict:** **PASS**

---

## 1. Executive verdict

FriendHosting accepted post–Plus / post–P2 / post–P3 state was frozen into a verified **final operational backup**.

| Gate | Result |
|------|--------|
| Pre-backup health | **PASS** |
| Remote archive | **PASS** |
| Local twin | **PASS** |
| SHA-256 remote = local | **YES** |
| Archive readability / key sections | **PASS** |
| Restore procedure written | **CONFIRMED** |
| Bare-metal restore exercised | **NO** |
| Post-backup service regression | **PASS** |
| Service architecture mutation | **0** |
| Client mutation | **0** |

```text
BACKUP: PASS
RESTORE STRATEGY: CONFIRMED
RESTORE PROCEDURE CONFIRMED
FULL BARE-METAL RESTORE NOT YET EXERCISED
```

---

## 2. Why final backup was taken

Before documentation/brain consolidation or any reserve-port (`:24443`) work, the programme needed a **restorable operational freeze** of the now-working FriendHosting stack sufficient to recover from configuration loss, accidental mutation, bad hardening, client-model mistakes, nginx/TLS issues, or 3X-UI/Xray corruption.

This wave is **backup-only** (plus documentation of restore steps). It does **not** add features.

---

## 3. Current accepted FriendHosting state

| Field | Value |
|-------|-------|
| Stable ID | FRIENDHOSTING-DE |
| Hostname | imart216311 |
| OS | Ubuntu 24.04.4 LTS (kernel 6.8.0-138-generic at capture) |
| Hardware | **2 vCPU** / **~1.9 GiB RAM** / **20 GiB** disk / root **~19G** ext4 / **2 GiB** swap |
| Domain / IPv4 | metacode-cloud.com → **92.42.99.126** |
| SSH | `:3333` key-only; PasswordAuthentication disabled; marsops sudo |
| VPN | VLESS + TLS + RAW/TCP **`:8443`** |
| Xray | **26.7.28** |
| 3X-UI | **3.7.0** (panel localhost `:20901`; public `:2096` DENY) |
| nginx | `:443` TLS; ACME webroot on `:80` |
| Security | UFW default deny; fail2ban active; journald capped; certbot.timer active |
| Clients | **6** (legacy retired) |
| Lifecycle | CONTROL / OPERATIONAL-CANDIDATE — **not** PRODUCTION_ACCEPTED |
| P2 | **PASS** |
| P3 | **PASS / CLOSED** |

---

## 4. Pre-backup health gate

All critical checks **PASS** before archive creation:

| Check | Result |
|-------|--------|
| SSH `:3333` | PASS |
| nginx `:443` (listen + TLS + HTTP answer) | PASS |
| 3X-UI localhost `:20901` | PASS |
| Xray `:8443` (listen + TLS) | PASS |
| TLS `:443` / `:8443` | PASS |
| DNS A → 92.42.99.126 | PASS |
| UFW intended map | PASS |
| fail2ban active | PASS |
| swap 2 GiB | PASS (SwapTotal 2097148 kB) |
| certbot.timer | PASS |
| ACME webroot signal | PASS |
| client count `:8443` | **6** / legacy absent |

Evidence: `evidence/FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01/A0-pre-gates.json`, `A0-pre-remote.txt`, `A1-safe-baseline.txt`.

Note: panel/root HTTP may return **404**; reachability is accepted on any HTTP status with live listener (aligned with prior P3 health doctrine).

---

## 5. Backup scope

Scoped operational restore archive (not whole-root dump), secret-bearing:

| Area | Included |
|------|----------|
| 3X-UI / x-ui | `/etc/x-ui` (DB + config), `/usr/local/x-ui` application tree |
| Xray | runtime under x-ui `bin/` + inbound/client state in DB |
| nginx | `/etc/nginx` |
| Let's Encrypt / certbot | `/etc/letsencrypt` (+ renewal hooks if present) |
| SSH / sudo | `/etc/ssh`, sudoers (+.d), authorized_keys **fingerprints** in meta |
| UFW | `/etc/ufw` |
| fail2ban | `/etc/fail2ban` |
| System | fstab, swapfile metadata, journald, systemd unit/status snaps, dpkg inventory, listeners, safe `clients-safe.json` (labels only; no UUID values in safe meta) |

Safe metadata also captured under archive `meta/` (hostname, free, df, UFW status, certbot certificate listing, etc.).

---

## 6. Remote archive

| Field | Value |
|-------|-------|
| Path | `/root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz` |
| Companion | `/root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz.sha256` |
| Staging tree | `/root/mars-backups/friendhosting-final-operational-20260830T125003Z/` |
| Size | **80746687** bytes |

---

## 7. Local archive

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-final-operational-20260830T125003Z.tgz` |
| SHA file | `...\friendhosting-final-operational-20260830T125003Z.tgz.sha256` |
| Restore twin doc | `...\friendhosting-final-operational-20260830T125003Z-RESTORE-STRATEGY.md` |
| Size | **80746687** bytes |

**Not in Git** (secret-bearing).

---

## 8. Hash / readability validation

| Check | Result |
|-------|--------|
| Remote exists / non-zero | PASS |
| Local exists / non-zero | PASS |
| SHA-256 remote | `1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2` |
| SHA-256 local | `1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2` |
| Match | **YES** |
| `tar` list readable | PASS |
| Key sections present | etc-ssh, etc-nginx, etc-letsencrypt, etc-ufw, etc-fail2ban, usr-local-x-ui, x-ui-db, fstab, clients-safe.json, journald, sudoers — **all PASS** |
| clients-safe count | **6** (expected labels) |
| Members | 342 |

Evidence: `B1-backup-validation.json`, `B1-backup-remote.txt`, `B1-backup-local-members.txt`.

---

## 9. Restore procedure

Canonical Git-safe runbook (no secrets):

`projects/mars-server-ops/runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md`

Covers: OS/package prerequisites; SSH; UFW; fail2ban; nginx; Let's Encrypt/certbot; 3X-UI DB/config; Xray via x-ui; swap/fstab/journald; daemon-reload; service order; listener/TLS/transport/panel/client validation; real-workload smoke; explicit recovery risks (SSH lockout, stale certs, DB/schema mismatch, UFW ordering, identity loss).

---

## 10. Restore confidence

| Class | Status |
|-------|--------|
| BACKUP | **PASS** |
| RESTORE STRATEGY | **CONFIRMED** |
| Destructive / bare-metal restore test | **NOT YET EXERCISED** |

Do **not** claim full disaster-recovery proof from this wave alone.

---

## 11. Post-backup service regression

After archive create + local download, live checks repeated — **PASS**:

| Surface | Result |
|---------|--------|
| SSH `:3333` | PASS |
| nginx `:443` | PASS |
| 3X-UI | PASS |
| Xray `:8443` | PASS |
| UFW | PASS |
| fail2ban | PASS |
| TLS | PASS |
| VPN architecture | **UNCHANGED** |
| Client count | **6** |

Evidence: `C1-post-gates.json`.

---

## 12. Current identity model

| Label | Status |
|-------|--------|
| WSP-ONE | active identity (prior physical PASS) |
| MCA-PHONE | active identity (prior physical PASS) |
| Unit-01 | SERVER_IDENTITY_READY / DEVICE_TEST_PENDING |
| Unit-02 | SERVER_IDENTITY_READY / DEVICE_TEST_PENDING |
| Unit-03 | SERVER_IDENTITY_READY / DEVICE_TEST_PENDING |
| Unit-MichaelPhone | SERVER_IDENTITY_READY / DEVICE_TEST_PENDING |
| MCA-ONE-FRIENDHOSTING-DE-RAW-8443 | **RETIRED / REMOVED FROM SERVER** |

Preferred day-to-day UX remains **3X-UI native QR/copy-link**. Local client folders = backup/registry only.

---

## 13. Backup limitations

- Not a provider-panel snapshot; not full disk image.
- Does not restore RAM, kernel, or hypervisor disk layout.
- Does not prove bare-metal rebuild without a chartered restore drill.
- Secret-bearing — must stay off Git.
- Later mutations after `20260830T125003Z` are **out of this freeze**.
- Package inventory is a point-in-time `dpkg -l` snap, not a pinned offline mirror.

---

## 14. Inventory update

Updated safe truth in:

- `projects/mars-server-ops/SERVER-INVENTORY-v1.md` — final backup timestamp, remote/local paths, SHA status, restore procedure status, client count 6, Plus baseline, P2 PASS, P3 PASS/CLOSED.
- `projects/mars-server-ops/OPERATIONAL-INDEX.md` — wave PASS; next = documentation consolidation; P4 deferred.

No secrets written to Git docs.

---

## 15. Next documentation / brain wave

**Do not execute in this task.**

**NEXT:** MARS SERVER OPS FRIENDHOSTING DOCUMENTATION + KNOWLEDGE CONSOLIDATION 01

Must reconcile infrastructure truth, architecture, registry, security posture, port map, backup/restore, TLS renewal, per-device identities, 3X-UI operator UX, provider qualification lessons, runbooks, incident/rollback, Server Ops reusable knowledge, maturity update, and broader post-VPN roadmap.

**P4 reserve `:24443` remains DEFERRED** until that consolidation completes.

---

## 16. Evidence paths

| Path | Role |
|------|------|
| `projects/mars-server-ops/evidence/FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01/` | Sanitized gates / validation / summary |
| `projects/mars-server-ops/tools/friendhosting-final-backup/final-operational-backup-01.py` | Assistive backup helper (not a product) |
| `projects/mars-server-ops/runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md` | Restore procedure |
| `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-final-operational-20260830T125003Z.tgz` | Secret-bearing local twin |
| `/root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz` | Secret-bearing remote archive |
| `local/.../final-operational-backup-01-20260830T125003Z/` | Local run mirror of evidence |

---

## 17. Git / mutation closeout

| Control | Count |
|---------|------:|
| VEESP mutation | 0 |
| EQVPS mutation | 0 |
| FriendHosting config mutation | 0 |
| FriendHosting client mutation | 0 |
| FriendHosting firewall mutation | 0 |
| FriendHosting SSH mutation | 0 |
| FriendHosting reboot | 0 |
| Secret disclosure (chat/Git UUIDs/keys) | 0 |
| Foreign WIP mutation | 0 |
| commit / push | 0 |

Foreign WIP elsewhere in the repo was left untouched. No commit/push in this wave.

---

*End of REPORT — FRIENDHOSTING FINAL OPERATIONAL BACKUP 01 · PASS.*

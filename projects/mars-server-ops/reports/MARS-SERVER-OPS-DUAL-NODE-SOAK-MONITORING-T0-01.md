# REPORT — MARS SERVER OPS DUAL-NODE SOAK / LIGHTWEIGHT MONITORING T0 01

**Wave:** FRIENDHOSTING + VEESP SOAK / LIGHTWEIGHT MONITORING 01  
**Date (UTC):** 2026-08-30T18:59:59Z  
**Verdict:** **PASS WITH RESIDUALS** · `SOAK_T0_PASS` · long-term soak **NOT YET PROVEN**

---

## 1. Verdict

Lightweight read-only health layer created and executed once (T0) against both accepted VPN nodes. Combined: **PASS_WITH_RESIDUALS**. No server/VPN/client mutation. No reboot.

---

## 2. FriendHosting T0

| Field | Value |
|-------|-------|
| Verdict | **PASS_WITH_RESIDUALS** |
| Hostname | imart216311 |
| Uptime | ~38441 s (~10.7 h) |
| Load | 0.00 0.00 0.00 |
| Disk root | 40% |
| RAM avail | ~79% |
| Swap used | ~0.02% of 2G |
| SSH `:3333` | PASS |
| VPN `:8443` + TLS | PASS · CN metacode-cloud.com · expires 2026-11-27 (~89d) |
| x-ui / xray / nginx / fail2ban / UFW | active |
| Certbot | present · timer scheduled |
| Backup | `friendhosting-operational-20260830T132309Z.tgz` · **FRESH** · SHA sidecar present |
| Real workload (prior evidence) | ChatGPT / YouTube / Cursor **PASS** |

Hairpin residual: operator-local TCP to `:20901`/`:2096` may show OPEN while on-VPN; remote UFW DENY + VEESP peer probe = **not public**.

---

## 3. VEESP T0 (MCA-VPN-001)

| Field | Value |
|-------|-------|
| Verdict | **PASS_WITH_RESIDUALS** |
| Uptime | ~1169423 s (~13.5 d) |
| Disk root | 45% |
| RAM avail | ~56% |
| Swap used | ~3.3% of 1G |
| SSH `:22` | PASS |
| VPN `:8443` + TLS | PASS · CN wsp-cloud.com · expires 2026-11-11 (~73d) |
| x-ui / xray / fail2ban / UFW | active |
| Backup | `veesp-final-operational-20260830T184024Z.tgz` · **FRESH** · SHA sidecar present |
| Real workload (prior evidence) | ChatGPT / YouTube / Cursor **PASS** (post system hardening) |

---

## 4. Known residuals

| Node | Residual | Class |
|------|----------|-------|
| VEESP | `:5928` PUBLIC TLS-DIRECT | ACCEPTED residual |
| VEESP | `:2096` PUBLIC UNUSED UNPROVEN | Documented residual |
| FriendHosting | Local TCP OPEN on `:2096`/`:20901` while on-VPN | Hairpin artifact — UFW DENY proven externally |

---

## 5. Backup freshness

| Node | Stamp | Age class |
|------|-------|-----------|
| FriendHosting | 20260830T132309Z | **FRESH** (≤7d) |
| VEESP | 20260830T184024Z | **FRESH** (≤7d) |

Policy: FRESH ≤7d · AGING 8–30d · STALE >30d. Event-driven backups preferred (pre/post mutation), not daily full.

---

## 6. Monitoring tool / runbook

| Artifact | Path |
|----------|------|
| Tool dir | `X:\AI MARS\projects\mars-server-ops\tools\vpn-nodes-health\` |
| Python checker | `...\vpn-nodes-lightweight-health-01.py` |
| PowerShell launcher | `...\Invoke-VpnNodesHealth.ps1` |
| Node defs | `...\nodes.json` (no secrets) |
| Runbook | `X:\AI MARS\projects\mars-server-ops\runbooks\VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md` |

---

## 7. Soak schedule

| Checkpoint | Status |
|------------|--------|
| T0 | **DONE** · `SOAK_T0_PASS` |
| T+24h | PENDING (separate run) |
| T+72h | PENDING |
| T+7d | PENDING |

Long-term soak: **NOT YET PROVEN**.

---

## 8. Git reconciliation

See terminal closeout in this wave. Selective staging of `projects/mars-server-ops/` only; foreign WIP untouched; no push; secrets/local infrastructure not staged.

---

## 9. Commit hash / status

Recorded in final terminal report after selective commit wave.

---

## 10. Next step

1. T+24h soak checkpoint (same tool, new evidence folder)  
2. T+72h · T+7d  
3. Begin planning first **non-VPN** Server Ops workload (Docker service deploy / restore lab)  
4. P4 `:24443` remains **DEFERRED**

---

## Safety confirmations

| Item | Count |
|------|-------|
| FriendHosting server mutation | 0 |
| VEESP server mutation | 0 |
| VPN mutation | 0 |
| Client mutation | 0 |
| Reboot | 0 |
| Secret disclosure | 0 |
| Foreign WIP mutation | 0 |

---

*Evidence: `X:\AI MARS\projects\mars-server-ops\evidence\DUAL-NODE-SOAK-MONITORING-T0-01\`*

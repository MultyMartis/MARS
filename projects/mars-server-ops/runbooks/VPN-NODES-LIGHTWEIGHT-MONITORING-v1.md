# VPN Nodes — Lightweight Monitoring Runbook v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **documented + human-invoked helper** — not Prometheus/Grafana, not an agent fleet, not autonomous monitoring  
**Tool:** `X:\AI MARS\projects\mars-server-ops\tools\vpn-nodes-health\`  
**Applies to:** FRIENDHOSTING-DE · MCA-VPN-001 (VEESP)

---

## 1. Purpose

Answer quickly, with evidence:

- Is the VPS / SSH / VPN `:8443` reachable?
- Is TLS healthy / when does it expire?
- Are Xray / 3X-UI / SSH / firewall / fail2ban healthy?
- Disk / RAM / swap state?
- Local operational backup age?
- Known residuals vs regressions?
- Has the node survived over time (soak), not only one session?

**Does not replace** real-workload acceptance (ChatGPT / YouTube / Cursor through the VPN profile).

---

## 2. How to run

From Windows (operator machine with local SSH keys under `X:\AI MARS\local\infrastructure\`):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "X:\AI MARS\projects\mars-server-ops\tools\vpn-nodes-health\Invoke-VpnNodesHealth.ps1" -Checkpoint T0
```

Or Python directly:

```text
python "X:\AI MARS\projects\mars-server-ops\tools\vpn-nodes-health\vpn-nodes-lightweight-health-01.py" --checkpoint T0
```

Optional filters:

```powershell
...\Invoke-VpnNodesHealth.ps1 -Checkpoint "T+24h" -Node FRIENDHOSTING-DE -Node MCA-VPN-001
```

Evidence default (T0 wave):  
`X:\AI MARS\projects\mars-server-ops\evidence\DUAL-NODE-SOAK-MONITORING-T0-01\`

Later checkpoints should use a **new evidence folder** (e.g. `...-T24H-01`) so T0 is not overwritten.

**Safety:** read-only remote probes. No Xray/3X-UI/client/firewall/SSH/TLS/nginx/package/swap/DNS mutation. No reboot.

---

## 3. Verdict meanings

| Verdict | Meaning |
|---------|---------|
| **PASS** | Core reachability + services + expected ports OK; no hard issues; no open known residuals requiring notation |
| **PASS_WITH_RESIDUALS** | Core OK; documented residuals and/or soft warnings present |
| **FAIL** | Hard issue (SSH/VPN/TLS/service/disk fail threshold/unexpected public port) |

Known residuals (VEESP `:5928` PUBLIC TLS-DIRECT; `:2096` PUBLIC UNUSED UNPROVEN) **must not** auto-fail the node when they match documented expectation.

---

## 4. Soak model

| Checkpoint | When | Token if health OK |
|------------|------|--------------------|
| **T0** | First run of this layer | `SOAK_T0_PASS` |
| **T+24h** | Separate execution ~24h later | `SOAK_24H_PASS` |
| **T+72h** | Separate execution ~72h later | `SOAK_72H_PASS` |
| **T+7d** | Separate execution ~7d later | `SOAK_7D_PASS` |

Do **not** wait inside a Cursor session. No sleep loops. No spam probes.

**Long-term soak** remains **NOT YET PROVEN** until later checkpoints are actually run and filed.

T0 alone does **not** promote lifecycle to `PRODUCTION_ACCEPTED`.

---

## 5. Certificate expiry

TLS handshake is checked on `:8443` with the node SNI (domain).

| Class | Rule (default) |
|-------|----------------|
| **PASS** | ≥ 21 days remaining |
| **WARN** | 7–21 days |
| **FAIL** | < 7 days or handshake failure |

Operator action on WARN: schedule renew / verify ACME (FriendHosting certbot webroot) or VEESP `/root/cert` renew path before FAIL.

---

## 6. Disk / RAM / swap thresholds

| Signal | Warn | Fail |
|--------|------|------|
| Root filesystem use % | ≥ 80% | ≥ 90% |
| RAM available % of total | < 10% | — (warn only unless OOM evidence) |
| Swap used % of swap | ≥ 75% | — (warn; investigate leak/pressure) |

Swap **absent** (total 0) is a warning on nodes that were hardened with swap present.

---

## 7. Backup age policy

Local preferred operational backup under `local\infrastructure\...\backups\` (existence + age + SHA sidecar presence). **Does not** recalculate historical SHA on every run.

| Class | Age since backup stamp |
|-------|------------------------|
| **FRESH** | ≤ 7 days |
| **AGING** | 8–30 days |
| **STALE** | > 30 days |

Recommended frequency (doctrine-aligned; not daily full backups):

| Trigger | Expectation |
|---------|-------------|
| **Before mutation** | Pre-change checkpoint (Class G / operational) |
| **After major accepted mutation** | Fresh verified operational backup + local twin |
| **Routine** | Opportunistic / on schedule only when operator charters; prefer event-driven over daily full |

STALE alone → soft warning, not automatic FAIL (unless charter says otherwise).

---

## 8. When operator intervention is required

Intervene if:

- Verdict **FAIL**
- TLS WARN/FAIL and renewal path unclear
- Disk approaching FAIL
- SSH unreachable
- x-ui / xray down
- Unexpected public port appears (not in expected / known residual list)
- Backup STALE **and** a mutation wave is planned

Do **not** treat documented VEESP panel residuals as surprise failures.

---

## 9. Server health vs real-workload acceptance

| Layer | Proves |
|-------|--------|
| This health checker | Host reachability, TLS, services, resources, backup age |
| Real-workload doctrine | Apps through VPN (ChatGPT / YouTube / Cursor, etc.) |

**Hairpin caveat:** while the operator workstation is connected through the same VPN node, local TCP probes to firewalled panel ports (e.g. FriendHosting `:2096` / `:20901`) may show OPEN. Authority for expected-not-public is **remote listen bind + UFW DENY** (and optional peer probe). Do not treat hairpin OPEN as a public exposure FAIL.

Documented workload state (as of latest acceptance evidence):

- FriendHosting: ChatGPT / YouTube / Cursor **PASS**
- VEESP: ChatGPT / YouTube / Cursor **PASS** (after system hardening)

T0 monitoring does **not** re-run those app tests.

---

## 10. Related

- [SERVER-INVENTORY-v1.md](../SERVER-INVENTORY-v1.md)  
- [BACKUP-RESTORE-MODEL-v1.md](../BACKUP-RESTORE-MODEL-v1.md)  
- [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](../REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md)  
- FriendHosting restore: [FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md](FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md)  
- VEESP restore: [VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md)

---

*Lightweight monitoring runbook v1 · 2026-08-31 · human-invoked only.*

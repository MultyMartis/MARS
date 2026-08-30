# MARS Server Ops — Server Inventory v1

**Status:** **schema + asset rows** — MCA-VPN-001 live; AdminVPS Server B deferred (assigned IP REJECTED); EQVPS negative control; FriendHosting **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** (soak **T0 PASS_WITH_RESIDUALS**; long-term soak **NOT YET PROVEN**; **not** PRODUCTION_ACCEPTED; dual local operational backup `20260830T132309Z` VERIFIED)  
**Not:** live asset registry, CMDB export, or automated discovery output

---

## 1. Purpose

Define a **sanitized, Git-safe** inventory schema for VPS and Linux servers under Server Ops stewardship.

Phase 1A created structure only. Phase **1B-0** adds the first **legacy-import** row for MCA-VPN-001. Later rows are added by chartered intake / closeout waves.

---

## 2. Design rules

| Rule | Detail |
|------|--------|
| **No secrets** | Passwords, keys, tokens, UUIDs, client URIs never in inventory rows |
| **No invented facts** | Empty or UNKNOWN until operator-approved intake |
| **IP optional** | Public/private IPs optional; VPN closeout may record IPs already published in REPORT evidence |
| **Local IP store** | If IPs must not live in Git, record `ip_ref` pointing to local-only file |
| **Evidence refs** | Link to REPORT / Storage paths, not raw dumps |
| **SAFE UNKNOWN** | Use explicit UNKNOWN/TBD for unverified fields |

---

## 3. Field definitions

| Field | Required | Description |
|-------|----------|-------------|
| `inventory_ref` | **YES** | Stable programme id — assigned at intake; temporary planning refs allowed |
| `operator_name` | REC | Human owner / primary operator |
| `owner_ref` | OPT | Programme or client ref — **not** ATLAS id unless later bound |
| `provider` | REC | Hosting provider name |
| `server_role` | REC | Primary role + control role if diagnostic |
| `hostname_label` | REC | Sanitized hostname or label |
| `public_domain_refs` | OPT | Domain names (sanitized) |
| `public_ip` | OPT | Optional; omit if local-only policy |
| `private_ip` | OPT | Optional |
| `ip_ref` | OPT | Pointer to local-only IP record |
| `os_family` | REC | e.g. `linux` |
| `os_version` | OPT | Verified OS string |
| `region_datacenter` | OPT | Region or DC label |
| `production_criticality` | REC | `prod` / `staging` / `dev` / `lab` / `UNKNOWN` |
| `lifecycle_state` | REC | `planned` / `active` / `draining` / `retired` / `UNKNOWN` (+ programme notes) |
| `service_list` | OPT | Major services / public ports (no secrets) |
| `access_model_ref` | OPT | Access doc link |
| `passport_ref` | OPT | VPS passport instance |
| `backup_status` | OPT | `documented` / `partial` / `none` / `UNKNOWN` |
| `restore_status` | OPT | `documented` / `partial` / `tested` / `none` / `UNKNOWN` |
| `security_state` | OPT | Sanitized posture |
| `acceptance_state` | OPT | Scoped states from Real-Workload Acceptance Doctrine |
| `monitoring_status` | OPT | `documented` / `partial` / `none` / `UNKNOWN` |
| `known_issues` | OPT | Non-secret |
| `dependencies` | OPT | Domains/services depended on |
| `last_verified` | OPT | ISO date |
| `evidence_refs` | OPT | REPORT or Storage pointers |
| `notes` | OPT | Non-secret |
| `safe_unknown_fields` | OPT | Unverified fields |

---

## 4. Inventory table

| inventory_ref | provider | server_role | hostname_label | public_domain_refs | public_ip | os_version | region_datacenter | production_criticality | lifecycle_state | service_list | backup_status | restore_status | security_state | acceptance_state | monitoring_status | last_verified | evidence_refs |
|---------------|----------|-------------|----------------|-------------------|-----------|------------|-------------------|------------------------|-----------------|--------------|---------------|----------------|----------------|------------------|-------------------|---------------|---------------|
| MCA-VPN-001 | VEESP | dedicated VPN — **positive control** · **STABLE / ACCEPTED CURRENT VPN WORKLOAD** (panel residuals documented) | wsp-cloud | wsp-cloud.com | 178.173.250.69 | Ubuntu 22.04.5 LTS | SAFE UNKNOWN | prod (HIGH) | **active** | 3X-UI **3.7.0** / Xray **26.7.28** / VLESS+TLS+RAW `:8443` (+ Reality `:46489` / Docker MTProto `:8445`; nginx ABSENT; cert `/root/cert`; panel PUBLIC TLS-DIRECT `:5928` ACCEPTED RESIDUAL; `:2096` PUBLIC UNUSED UNPROVEN) | **BACKUP VERIFIED** preferred final `20260830T184024Z` (**81065422** B; SHA match) + historical post-hardening/pre-hardening/post-upgrade/pre-upgrade/operational/pre-cred | restore procedure **CONFIRMED** ([VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md)); bare-metal **NOT EXERCISED** | SSH KEY-ONLY (`marsops`+root recovery); PasswordAuth **disabled**; UFW **active** (22/8443/46489/5928/2096/8445); fail2ban; swap 1G; journald capped; `:5928` ACCEPTED RESIDUAL; `:2096` UNUSED UNPROVEN; reboot-required **YES** (not rebooted) | TRANSPORT **PASS** · REAL_WORKLOAD **PASS** · system security **PASS** · panel exposure **PASS WITH RESIDUALS** · final backup **PASS** · soak **T0 PASS_WITH_RESIDUALS** · long-term soak **NOT YET PROVEN** | lightweight documented ([VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md](runbooks/VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md); T0 evidence) | 2026-08-30 | DUAL-NODE-SOAK-MONITORING-T0-01; FINAL-FULL-OPERATIONAL-BACKUP-01; PANEL-EXPOSURE-HARDENING-01; SYSTEM-SECURITY-HARDENING-01; 3XUI-UPGRADE; 3XUI-ADMIN; DUAL-LOCAL-BACKUP; MCA-VPN-001 assets |
| EQVPS-MICRO-IP | EQVPS (Hetzner AS24940 class) | dedicated VPN — **negative/problematic control** | metacode-cloud | metacode-cloud.com | 95.216.126.173 | Ubuntu 24.04.4 LTS | Helsinki / HEL class | lab / investigation | **active — not production-accepted** | 3X-UI 3.7.0 / Xray 26.7.28 / VLESS+TLS+RAW `:8443` | partial | documented restore runbook exists | KEY-ONLY SSH historical; UFW used | TRANSPORT **PASS** · REAL_WORKLOAD **FAIL** · root cause **UNPROVEN** | none | 2026-08-29 | EQVPS assets; AUDIT 01; EXP-A01; EXP-A01b |
| FRIENDHOSTING-DE | FriendHosting (prefix via AS47447 / 23M GmbH) | dedicated VPN — **independent modern control / OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** | imart216311 | metacode-cloud.com | 92.42.99.126 | Ubuntu 24.04.4 LTS | Germany / FRA-facing signal | lab → scoped ops | **active — OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** (soak T0 PASS_WITH_RESIDUALS; long-term soak NOT YET PROVEN; not PRODUCTION_ACCEPTED) | 3X-UI 3.7.0 / Xray 26.7.28 / VLESS+TLS+RAW `:8443` (**6** per-device clients; legacy retired) / nginx `:443`→panel localhost / SSH `:3333` / ACME `:80` webroot | **BACKUP VERIFIED** `20260830T132309Z` (latest dual-wave twin; **80743234** B; SHA match) + prior final freeze `20260830T125003Z` + archives; bare-metal **NOT YET EXERCISED** | restore procedure **CONFIRMED** ([FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md](runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md)); full DR **NOT TESTED** | SSH KEY-ONLY `:3333`; UFW allow 3333/443/8443/80 deny 20901/2096; fail2ban sshd; swap 2G; `*:2096` UFW DENY ACCEPTED HARDENED BOUNDARY; certbot webroot dry-run PASS | TRANSPORT **PASS** · REAL_WORKLOAD **PASS** · scoped ops acceptance **YES** · soak **T0 PASS_WITH_RESIDUALS** · long-term soak **NOT YET PROVEN** · Plus hardware **PASS** · P2 **PASS** · P3 identity **CLOSED** · dual backup **PASS** | lightweight documented ([VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md](runbooks/VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md); T0 evidence) | 2026-08-30 | DUAL-NODE-SOAK-MONITORING-T0-01; assets/FRIENDHOSTING-DE; DUAL-LOCAL-BACKUP-01; FINAL-OPERATIONAL-BACKUP-01; P3/P2/PLUS reports |
| SERVER-B-PLANNING | AdminVPS | dedicated VPN (secondary; stack ABSENT) | metacode-cloud.com | metacode-cloud.com | *(local/secret_ref)* | Ubuntu 24.04 LTS | Finland / Helsinki (operator) | prod (intended) — **blocked** | **provisioned — FINAL ASSET REGISTRATION PENDING**; assigned IP **REJECTED** for direct entry | SSH key-only; UFW; fail2ban; VPN stack ABSENT | provider weekly copy claimed — SAFE UNKNOWN | SAFE UNKNOWN | KEY-ONLY; UFW/fail2ban ACTIVE | Direct network gate **FAIL** (assigned IP); provider **NOT REJECTED** | partial | 2026-08-26 | SERVER-B-PLANNING assets |

### Row notes — MCA-VPN-001

- Not an ATLAS ID — legacy managed-asset reference.  
- Positive historical/operational control.  
- Proven architecture for acceptance matrix: **VLESS + TLS + RAW/TCP `:8443`** (WS claim superseded — SC-001).  
- Separate from n8n/automation VEESP VPS.  
- Passport: [SERVER-A-CURRENT-PASSPORT-v1.md](assets/MCA-VPN-001/SERVER-A-CURRENT-PASSPORT-v1.md).  
- Security posture: [SECURITY-POSTURE-v1.md](assets/MCA-VPN-001/SECURITY-POSTURE-v1.md).  
- **Preferred final operational backup (`20260830T184024Z`):** `veesp-final-operational-20260830T184024Z.tgz` — remote `/root/mars-backups/`; local twin; size **81065422**; SHA-256 `b15631b7d1519fbd8364b73541fbf6e240f5e1032b0b44ef49fc34725bc80cec`; MATCH. Report: [reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md](reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md).  
- **Historical post–system-security snapshot (`20260830T163612Z`):** size **81048677**; SHA-256 `1857afff8dbc087540b252394438115a9babb1b42c212c03137c4d41e7d920d7`; MATCH — superseded as preferred.  
- **Pre-hardening rollback (`20260830T162532Z`):** size **81015066**; SHA-256 `ec201264ef9ef0062ec19fa67c3c7bb56c6522b803c6ed1842c77e6ef497b7a7`; MATCH.  
- **Post-upgrade x-ui snapshot (`20260830T155842Z`):** size **80876064**; SHA-256 `97ee0394a308f827b9798d748c86f740ec8b2501a0c60712c7927913db5389d0`; MATCH.  
- **Pre-upgrade x-ui snapshot (`20260830T154548Z`):** 3.4.1 + matching DB — size **83815970**; SHA-256 `ae78f5ef548bdbcea0677c259d949698ae66941a5ebe8b95f3b6e9e11b5aac5b`; MATCH. Restoring this stamp returns **old application version** + pre-upgrade DB/schema.  
- **Full operational backup (`20260830T132309Z`):** still valid broader inventory twin (Xray **26.6.22** era) — SHA-256 `d10b67cb1b8a9e0beb4a131a583eee1af56cb153e4513d1e599f6e8bba9112c8`. Restoring it after upgrade **also** reverts panel admin DB to pre-rotation credentials.  
- **Scoped pre-credential snapshot (`20260830T141517Z`):** `/etc/x-ui/` only; SHA-256 `ce6134f4b7eed075571323a2d7cbfede0bc192967b81464929ab11c27463c3b3`.  
- Dual backup report: [reports/MARS-SERVER-OPS-DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01.md](reports/MARS-SERVER-OPS-DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01.md).  
- **3X-UI upgrade + panel exposure wave (2026-08-30):** upgrade **3.4.1 → 3.7.0 PASS**; Xray **26.6.22 → 26.7.28**. Report: [reports/MARS-SERVER-OPS-VEESP-3XUI-UPGRADE-PANEL-EXPOSURE-HARDENING-01.md](reports/MARS-SERVER-OPS-VEESP-3XUI-UPGRADE-PANEL-EXPOSURE-HARDENING-01.md).  
- **System security hardening 01 (2026-08-30):** KEY-ONLY SSH; UFW active; fail2ban; swap 1G; journald cap — **PASS**. Report: [reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md](reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md).  
- **Panel exposure hardening 01 (2026-08-30):** `:5928` ACCEPTED RESIDUAL; `:2096` UNUSED UNPROVEN left open; nginx DEFERRED. Report: [reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md](reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md).  
- **Next:** T+24h / T+72h / T+7d soak checkpoints via [VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md](runbooks/VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md). P4 `:24443` remains DEFERRED.

### Row notes — EQVPS-MICRO-IP

- Temporary inventory_ref aligned to existing asset folder — not ATLAS ID.  
- Negative/problematic control.  
- Exact root cause **UNPROVEN**.  
- Asset locus: [assets/EQVPS-MICRO-IP/](assets/EQVPS-MICRO-IP/).

### Row notes — FRIENDHOSTING-DE

- Temporary inventory_ref — final MCA-style registration requires separate charter.  
- Canonical asset pack: [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md).  
- Lifecycle: **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** (SC-011). Soak **T0 PASS_WITH_RESIDUALS**; long-term soak **NOT YET PROVEN**. Do **not** set `PRODUCTION_ACCEPTED` until fuller soak + DR expectations.  
- Network: `92.42.99.0/24`, AS47447 / 23M GmbH.  
- Commercial tier (operator claim, 2026-08-30): **Plus** — exact panel SKU numbers **not** yet persisted in MARS (`PROVIDER PANEL SPEC = OPERATOR-OBSERVED / EXACT VALUE NOT YET PERSISTED`).  
- Final Plus hardware baseline: **2 vCPU** / **~1.9 GiB RAM** / **20 GiB** disk (~19G root ext4) / **2 GiB swap**.  
- **P2 hardening:** **PASS** — [P2-CLEAN-HARDENING-RECONCILIATION-02](reports/MARS-SERVER-OPS-FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02.md).  
- **P3 identity:** **PASS / CLOSED** — [P3-LEGACY-RETIREMENT-CLOSEOUT-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01.md) (6 clients; legacy retired).  
- **Prior final freeze (`20260830T125003Z`):** SHA-256 `1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2`; size **80746687**; retained as historical freeze.  
- **Latest dual-wave operational backup (`20260830T132309Z`):** remote `/root/mars-backups/friendhosting-operational-20260830T132309Z.tgz`; local `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-operational-20260830T132309Z.tgz`; size **80743234**; SHA-256 `a434c1fdd178c3df133b74b503e8298b150a6640727c15d89aee341b9bf6e617`; remote/local **MATCH**; restore procedure **CONFIRMED**; bare-metal **NOT YET EXERCISED**.  
- **Identity model:** WSP-ONE **PASS**; MCA-PHONE **PASS**; Unit-* **DEVICE_TEST_PENDING**. Preferred UX = 3X-UI native QR/copy-link.  
- **P4 `:24443`:** **DEFERRED**.  
- Next FriendHosting ops: T+24h soak checkpoint ([SERVER-OPS-WIDER-ROADMAP-v1.md](SERVER-OPS-WIDER-ROADMAP-v1.md); [VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md](runbooks/VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md)).  
- Local secrets: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\`.

### Row notes — SERVER-B-PLANNING

- Temporary planning inventory_ref.  
- Looking-glass/preflight ≠ assigned IP suitability.  
- VPN stack not installed while direct path rejected.  
- Access: [SERVER-B-SSH-ACCESS-MODEL-v1.md](assets/SERVER-B-PLANNING/SERVER-B-SSH-ACCESS-MODEL-v1.md).

---

## 5. Intake workflow

1. Operator provides sanitized facts or read-only discovery charter.  
2. Assign `inventory_ref` per naming convention.  
3. Create or link `passport_ref` from [VPS-PASSPORT-v1.md](VPS-PASSPORT-v1.md).  
4. Link `access_model_ref` when available.  
5. Record `acceptance_state` via [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md).  
6. Mark `safe_unknown_fields`.  
7. Record `evidence_refs` — no secrets in Git.

---

## 6. Related documents

- [VPS-PASSPORT-v1.md](VPS-PASSPORT-v1.md)  
- [SERVICE-MAP-v1.md](SERVICE-MAP-v1.md)  
- [ACCESS-MODEL-v1.md](ACCESS-MODEL-v1.md)  
- [STORAGE-MODEL-v1.md](STORAGE-MODEL-v1.md)  
- [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](SUPERSEDED-CONCLUSIONS-REGISTER-v1.md)  
- [SERVER-OPS-AGENT-KNOWLEDGE-v1.md](SERVER-OPS-AGENT-KNOWLEDGE-v1.md)  
- [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md)  
- [reports/MARS-SERVER-OPS-FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01.md](reports/MARS-SERVER-OPS-FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01.md)

---

*Server Inventory v1 · FriendHosting OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD · dual-node soak T0 PASS_WITH_RESIDUALS · 2026-08-30.*

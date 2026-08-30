# Current State Reconciliation v1 — MCA-VPN-001

**Purpose:** Structured comparison of legacy handoff vs live read-only intake  
**Status:** Phase 1B-1 **complete 2026-08-25** — **PASS WITH GAPS**  
**Evidence:** [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md)  
**Not:** authorization to execute commands or mutate production

---

## Usage rules

1. **Live observed value** populated from read-only evidence during chartered intake only.  
2. **Match?** uses: MATCH, CHANGED, PRESENT, ABSENT, SAFE UNKNOWN, NOT CHECKED.  
3. Link **Evidence ref** to Git-safe evidence — never secrets.

---

## Reconciliation matrix

| Field | Legacy handoff value | Legacy confidence | Live observed value | Match? | Action | Evidence ref |
|-------|---------------------|-------------------|---------------------|--------|--------|--------------|
| provider | VEESP | HIGH | NOT CHECKED (provider panel) | NOT CHECKED | Provider panel reconcile | — |
| tariff | SAFE UNKNOWN | — | NOT CHECKED | NOT CHECKED | Provider panel | — |
| datacenter | SAFE UNKNOWN | — | NOT CHECKED | NOT CHECKED | Provider panel + ASN | — |
| OS | Ubuntu 22.04.5 LTS | HIGH | Ubuntu 22.04.5 LTS | **MATCH** | — | [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md) |
| kernel | From inventory script (historical) | MEDIUM | 5.15.0-187-generic | **PRESENT** | — | same |
| hostname | wsp-cloud | HIGH | wsp-cloud | **MATCH** | — | same |
| CPU | ~1 vCPU | HIGH | 1 vCPU Xeon Gold 6248 | **MATCH** | — | same |
| RAM | ~1 GB | HIGH | 1.0 GiB, no swap | **MATCH** | — | same |
| disk | ~20 GB | HIGH | 20G, 42% used | **MATCH** | — | same |
| public IP | Redacted / `<SERVER_IP>` | HIGH (exists) | `<SERVER_IP>` captured | **PRESENT** | Redact in Git | same |
| domains | wsp-cloud.com | HIGH | wsp-cloud.com (cert CN) | **MATCH** | — | same |
| SSH port | 22/TCP (historical) | MEDIUM | 22 | **MATCH** | — | same |
| SSH auth model | SAFE UNKNOWN | — | root + password enabled | **PRESENT** | Hardening review (charter) | same |
| firewall | SAFE UNKNOWN | — | ufw inactive; nft+fail2ban on 22 | **PRESENT** | Document posture | same |
| fail2ban | SAFE UNKNOWN | — | active, enabled | **PRESENT** | — | same |
| Docker | SAFE UNKNOWN on VPN VPS | — | active; MTProto container | **PRESENT** | Confirm MTProto scope | same |
| nginx | Not confirmed in Server A path | HIGH (absence) | not installed | **MATCH** | — | same |
| x-ui version | 3.4.1 (historical) | MEDIUM-HIGH | semver not obtained | **SAFE UNKNOWN** | Version probe charter | same |
| Xray version | 26.6.22 (historical log) | HIGH | 26.6.22 | **MATCH** | — | same |
| x-ui panel protocol | HTTPS | HIGH | HTTPS (cert under /root/cert) | **MATCH** | — | same |
| x-ui panel port | 5928 | HIGH | 5928 | **MATCH** | — | same |
| x-ui panel base path | `<3XUI_PANEL_PATH>` — secret | HIGH | PRESENT in DB (redacted) | **SAFE UNKNOWN** | Compare via local secrets only | same |
| VLESS | Direction confirmed | MEDIUM | 2 inbounds, both vless | **MATCH** | — | same |
| Reality | Direction confirmed | HIGH/MEDIUM | inbound id 3, port 46489 | **MATCH** | — | same |
| TCP | In legacy docs | MEDIUM | implied by listeners | **PRESENT** | — | same |
| Vision | In legacy docs | MEDIUM | not in stream_settings flags | **SAFE UNKNOWN** | Deep config read charter | same |
| WebSocket | Not on Server A (legacy topo) | MEDIUM | inbound id 1 WS flag set | **CHANGED** | Update topology doc | same |
| inbound ports | SAFE UNKNOWN | — | 8443, 46489 | **PRESENT** | — | same |
| outbounds | SAFE UNKNOWN | — | NOT CHECKED | NOT CHECKED | Read-only config charter | — |
| routing | SAFE UNKNOWN | — | NOT CHECKED | NOT CHECKED | Read-only config charter | — |
| DNS | SAFE UNKNOWN | — | NOT CHECKED | NOT CHECKED | Read-only config charter | — |
| certificate issuer | Likely Let's Encrypt | MEDIUM-HIGH | Let's Encrypt (YE2) | **MATCH** | — | same |
| certificate expiry | Dynamic | — | 2026-11-11 | **PRESENT** | Monitor renewal | same |
| renewal | SAFE UNKNOWN | — | no certbot timer seen | **SAFE UNKNOWN** | Identify renewal path | same |
| systemd services | x-ui confirmed | HIGH | x-ui, docker, fail2ban, ssh active | **PRESENT** | — | same |
| `/etc/letsencrypt` | existed (archive scope) | HIGH | **absent** on live FS | **CHANGED** | Confirm cert migration | same |
| backup archives | 3xui_full + mca-gate-full-* | HIGH | both under /root/MCA/backups/ | **MATCH** (paths CHANGED for 3xui) | tar -tf / checksum charter | same |
| backup checksums | NOT PROVEN | — | NOT CHECKED | NOT CHECKED | Operator verify | — |
| local backup copy | Intended — not checksum-proven | MEDIUM | NOT CHECKED | NOT CHECKED | Operator inventory | — |
| restore test | Full DR NOT TESTED | HIGH | NOT TESTED | **MATCH** (still unproven) | DR drill charter | — |
| monitoring | SAFE UNKNOWN | — | fail2ban only identified | **SAFE UNKNOWN** | — | same |
| MTProto artifact | `/root/mtproto_backup.json` existed | HISTORICAL | file present + live container | **PRESENT** | — | same |
| MCA directory state | `/root/MCA/` structure created | HIGH | structure present | **MATCH** | — | same |
| `/root/3xui_full_backup.tar.gz` | existed at root | HIGH | absent (migrated) | **CHANGED** | — | same |
| `/root/xui-repair-backup` | deletion approved | MEDIUM | absent | **ABSENT** | — | same |

---

## Reconciliation outcomes (Phase 1B-1 — 2026-08-25)

| Outcome | Count / note |
|---------|----------------|
| **MATCH** | Core identity, OS sizing, Xray 26.6.22, panel 5928, nginx absence, VLESS/Reality direction |
| **CHANGED** | `/etc/letsencrypt` absent; backup path migration; WebSocket on TLS inbound |
| **PRESENT** | fail2ban, Docker/MTProto, SSH posture, ufw inactive, cert under `/root/cert` |
| **ABSENT** | `/root/xui-repair-backup`, root-level 3xui archive |
| **SAFE UNKNOWN** | 3X-UI semver, webBasePath legacy match, Vision, renewal mechanism |
| **NOT CHECKED** | provider tariff/datacenter, outbounds/routing, backup checksums |

**Verdict:** **PASS WITH GAPS** — live baseline established; operator review before mutation.

---

## Related documents

- [LIVE-INTAKE-CHECKLIST-v1.md](LIVE-INTAKE-CHECKLIST-v1.md)
- [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md)
- [SERVER-A-CURRENT-PASSPORT-v1.md](SERVER-A-CURRENT-PASSPORT-v1.md)
- [SERVER-A-LEGACY-PASSPORT-v1.md](SERVER-A-LEGACY-PASSPORT-v1.md)

---

*Current State Reconciliation v1 · live intake 2026-08-25 · PASS WITH GAPS.*

# Server A Legacy Passport v1 — MCA-VPN-001

**Status:** LEGACY LAST-KNOWN — **LIVE VERIFY REQUIRED**  
**Authority:** Sanitized historical handoff — **not** current live truth  
**Not:** ATLAS entity; not a live CMDB record

---

## 1. Identity

| Field | Legacy last-known value | Tag |
|-------|-------------------------|-----|
| **Asset ref** | `MCA-VPN-001` | LEGACY |
| **Provider** | VEESP | LEGACY LAST-KNOWN |
| **Role** | Dedicated VPN VPS | LEGACY LAST-KNOWN |
| **Historical hostname** | `wsp-cloud` | LEGACY LAST-KNOWN |
| **Public domain** | `wsp-cloud.com` | LEGACY LAST-KNOWN |
| **Public IPv4** | *(omitted — redacted)* | LIVE VERIFY REQUIRED |
| **OS** | Ubuntu 22.04.5 LTS | LEGACY LAST-KNOWN |
| **Virtualization** | KVM | LEGACY LAST-KNOWN |
| **CPU** | ~1 vCPU (Xeon Gold 6248 family per inventory) | LEGACY LAST-KNOWN |
| **RAM** | ~1 GB | LEGACY LAST-KNOWN |
| **Disk** | ~20 GB | LEGACY LAST-KNOWN |
| **Datacenter / region** | SAFE UNKNOWN | LIVE VERIFY REQUIRED |
| **Commercial tariff** | SAFE UNKNOWN | LIVE VERIFY REQUIRED |

**Separation rule:** This VPS is **VPN-only**. A **separate** VEESP VPS hosts n8n/automation workloads. Do **not** merge roles.

---

## 2. Runtime stack

| Component | Legacy last-known | Tag |
|-----------|-------------------|-----|
| **Management** | 3X-UI | LEGACY LAST-KNOWN |
| **Proxy core** | Xray | LEGACY LAST-KNOWN |
| **Persistent DB** | SQLite `/etc/x-ui/x-ui.db` | LEGACY LAST-KNOWN |
| **Protocol direction** | VLESS / Reality | LEGACY LAST-KNOWN |
| **Transport notes** | TCP / Vision mentioned in legacy docs | MEDIUM confidence — **LIVE VERIFY REQUIRED** |
| **WebSocket on Server A** | Not confirmed current | SAFE UNKNOWN |
| **Docker as VPN runtime** | Not confirmed | SAFE UNKNOWN |
| **nginx in traffic path** | **Not confirmed** — future WS/TLS/nginx is separate node plan | NOT CURRENT |

### Version hints (historical)

| Software | Last identified | Tag |
|----------|-----------------|-----|
| 3X-UI | 3.4.1 | LEGACY LAST-KNOWN — LIVE VERIFY REQUIRED |
| Xray | 26.6.22 (from logs) | LEGACY LAST-KNOWN — LIVE VERIFY REQUIRED |

---

## 3. Management access (sanitized)

| Surface | Legacy last-known | Tag |
|---------|-------------------|-----|
| **Panel protocol** | HTTPS | LEGACY LAST-KNOWN |
| **Known-good panel port** | 5928 | LEGACY LAST-KNOWN |
| **Panel base path** | Secret-bearing — `<3XUI_PANEL_PATH>` — **not stored in Git** | LEGACY LAST-KNOWN |
| **Panel URL pattern** | `https://wsp-cloud.com:5928/<3XUI_PANEL_PATH>/` | LEGACY LAST-KNOWN |
| **Panel credentials** | `<3XUI_ADMIN_LOGIN>` / `<3XUI_ADMIN_PASSWORD>` — local only | NOT IN GIT |
| **Root administration** | Historically used | LEGACY LAST-KNOWN |
| **SSH/SFTP** | TCP/22 historically used (WinSCP) | LEGACY LAST-KNOWN |
| **SSH auth policy** | Password and/or key discussed — current policy unknown | LIVE VERIFY REQUIRED |

---

## 4. Certificates

| Item | Legacy last-known | Tag |
|------|-------------------|-----|
| **Let's Encrypt tree** | `/etc/letsencrypt` | LEGACY LAST-KNOWN |
| **Additional cert material** | `/root/cert` | LEGACY LAST-KNOWN |
| **CA** | Likely Let's Encrypt | MEDIUM — LIVE VERIFY REQUIRED |
| **Renewal method** | SAFE UNKNOWN | LIVE VERIFY REQUIRED |
| **Certificate expiry** | Dynamic | LIVE VERIFY REQUIRED |

Private key material is **SECRET-BEARING** — never commit.

---

## 5. Backup posture (summary)

| Statement | Tag |
|-----------|-----|
| Historical `3xui_full_backup.tar.gz` existed | LEGACY LAST-KNOWN |
| Newer VPN/application archive ~`mca-gate-full-2026-06-27-1845.tar.gz` created | LEGACY LAST-KNOWN |
| Archive scope: VPN/app paths only — **NOT full server backup** | CONFIRMED HISTORICAL |
| Full Ubuntu filesystem backup | **NOT PROVEN** |
| Checksum workflow | **NOT PROVEN** |
| Backup encryption | **NOT PROVEN** |
| Off-server copy | Intended/likely — **not checksum-confirmed** | MEDIUM |

See [BACKUP-STATE-v1.md](BACKUP-STATE-v1.md).

---

## 6. Recovery posture (summary)

| Capability | Status |
|------------|--------|
| Targeted 3X-UI panel settings recovery via SQLite | **PROVEN** (historical) |
| Blank VPS → restore → working VPN | **NOT PROVEN** |
| Full disaster recovery drill | **NOT TESTED** |

See [RECOVERY-STATE-v1.md](RECOVERY-STATE-v1.md).

---

## 7. Production criticality

| Field | Value |
|-------|-------|
| **Criticality** | HIGH — production VPN / single legacy active node |
| **Failure domain** | Single-node — operator may depend on this path for connectivity |
| **Change default** | READ-ONLY FIRST; charter + backup before mutation |

---

## 8. Explicit exclusions from this passport

The following are **not** documented here as values:

- Client UUIDs
- Reality private keys / ShortIDs
- Panel secret base path (actual string)
- SSH passwords / private keys
- Raw public IP (programme redaction)
- Subscription tokens / URIs

---

## 9. Related documents

- [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md)
- [legacy/WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md](legacy/WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md)

---

*Server A Legacy Passport v1 · MCA-VPN-001 · import only.*

# VPN Runtime Legacy v1 — MCA-VPN-001

**Status:** LEGACY LAST-KNOWN — **LIVE VERIFY REQUIRED**  
**Scope:** 3X-UI, Xray, protocol direction — sanitized references only

---

## 1. 3X-UI

| Item | Legacy last-known | Tag |
|------|-------------------|-----|
| **Historical version** | 3.4.1 | LEGACY LAST-KNOWN — LIVE VERIFY REQUIRED |
| **Install root** | `/usr/local/x-ui` | LEGACY LAST-KNOWN |
| **Main binary** | `/usr/local/x-ui/x-ui` | LEGACY LAST-KNOWN |
| **Database** | `/etc/x-ui/x-ui.db` (SQLite) | LEGACY LAST-KNOWN |
| **systemd unit** | `x-ui` | LEGACY LAST-KNOWN |
| **Settings command** | `x-ui settings` | historical procedure |
| **Log command** | `x-ui log` | historical procedure |
| **Panel protocol** | HTTPS | LEGACY LAST-KNOWN |
| **Known-good port** | 5928 | LEGACY LAST-KNOWN |
| **Panel base path** | `<3XUI_PANEL_PATH>` — **SECRET — not in Git** | LEGACY LAST-KNOWN |

### Panel credentials (references only)

| Entity | Storage |
|--------|---------|
| Admin login | `<3XUI_ADMIN_LOGIN>` — local/secret store |
| Admin password | `<3XUI_ADMIN_PASSWORD>` — local/secret store |

---

## 2. Xray

| Item | Legacy last-known | Tag |
|------|-------------------|-----|
| **Historical log version** | Xray 26.6.22 started | LEGACY LAST-KNOWN — LIVE VERIFY REQUIRED |
| **Binary/runtime path** | `/usr/local/x-ui/bin/` | LEGACY LAST-KNOWN |
| **Config tree backed up** | `/etc/xray` existed / included in archives | LEGACY LAST-KNOWN |
| **Config authority** | May be 3X-UI-generated vs `/etc/xray` alone | **SAFE UNKNOWN** |
| **Exact inbound config** | Not safely reconstructed in handoff | **SAFE UNKNOWN** |
| **Exact outbound config** | Not retained | **SAFE UNKNOWN** |

---

## 3. Protocols and transports

| Protocol / feature | Legacy evidence | Confidence | Tag |
|-------------------|-------------------|------------|-----|
| **VLESS** | Documented as VPN direction | MEDIUM | LEGACY — VERIFY |
| **Reality** | Worked / central to setup | HIGH/MEDIUM | LEGACY — VERIFY |
| **TCP** | In legacy documentation | MEDIUM | LEGACY — VERIFY |
| **Vision** | In legacy documentation | MEDIUM | LEGACY — VERIFY |
| **WebSocket on Server A** | Not confirmed current | — | SAFE UNKNOWN |
| **VMess** | Not established | — | SAFE UNKNOWN |
| **Trojan** | Not established | — | SAFE UNKNOWN |

---

## 4. Secret entities (names only — never values in Git)

| Entity | Server B rule |
|--------|---------------|
| `<XUI_CLIENT_UUID>` | Generate new for B |
| `<REALITY_PRIVATE_KEY>` | Generate new for B |
| `<REALITY_PUBLIC_KEY>` | Derived from new private key |
| `<REALITY_SHORT_ID>` | Generate new for B |
| `<REALITY_SNI>` | Research/config-specific |
| `<REALITY_TARGET>` | Environment-specific |
| `<SUBSCRIPTION_SECRET>` | New for B if used |
| `<3XUI_PANEL_PATH>` | New for B |
| `<TLS_PRIVATE_KEY>` | Never clone from A |

---

## 5. Docker / MTProto

| Item | Status |
|------|--------|
| Docker as part of VPN runtime | **SAFE UNKNOWN** — `docker_list.txt` artifact alone insufficient |
| MTProto | `/root/mtproto_backup.json` existed — current use **SAFE UNKNOWN** |

---

## 6. Operational warnings (from incidents)

1. **READ-ONLY FIRST** on production single-node VPN.  
2. Do **not** stop/disable `x-ui` during exploratory diagnostics without impact analysis and emergency access.  
3. `systemctl restart x-ui` causes service interruption — use only with recovery path.

---

## Related documents

- [NETWORK-TOPOLOGY-v1.md](NETWORK-TOPOLOGY-v1.md)
- [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md)
- [KNOWN-GOOD-PROCEDURES-v1.md](KNOWN-GOOD-PROCEDURES-v1.md)

---

*VPN Runtime Legacy v1 · no secret values · live verification pending.*

# EQVPS RAW 24443 Port A/B — Provisioning Report (2026-08-29)

Git-safe report. No secrets. Operator daily key source remains 3X-UI panel.

## Verdict

**RAW_24443_AB_READY_FOR_OPERATOR_TEST**

Server-side provisioning and isolated client validation passed. Real Cursor/Firefox application conclusion requires the operator manual A/B after importing `MCA-ONE-RAW-24443-AB` from 3X-UI.

## Preflight

### MARS
- Workspace: `X:\AI MARS` on volume label `AI WS`
- `OPERATIONAL-INDEX.md` consulted before writes
- Evidence root: `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-24443-ab-2026-08-29\`

### Git
- Branch: `mars/canonical-post-recovery`
- **NO COMMIT** (per task charter)
- Foreign WIP preserved; no staging performed

### EQVPS state (pre-wave)
- SSH: `marsops@95.216.126.173` via `marsops_ed25519`
- Hostname: `metacode-cloud`
- `x-ui`: active
- Listeners: 22, 443, 8443, 20901, 2096 (24443 absent pre-wave)

## Existing control — 8443

| Check | Result |
|-------|--------|
| Inbound id | 2 (unchanged) |
| Remark | `EQVPS-TLS-RAW-8443` |
| Client count | 6 (unchanged) |
| Control client | `MCA-ONE-RAW-8443` present |
| Network/security | tcp / tls |
| ALPN | `http/1.1` |
| **8443 unchanged** | **YES** |

Post-wave TLS check on `:8443`: Verify return code **0 (ok)**.

## New A/B inbound

| Field | Value |
|-------|-------|
| Remark | `EQVPS-TLS-RAW-24443-AB` |
| Inbound id | 4 (new) |
| Port | **24443** |
| Protocol | VLESS |
| Transport | RAW/tcp (`network=tcp`) |
| Security | TLS |
| Certificate | Existing Let’s Encrypt `metacode-cloud.com` (reused) |
| SNI | `metacode-cloud.com` |
| ALPN | `http/1.1` (matched 8443) |
| Fingerprint | `chrome` (matched 8443) |
| Flow | empty (matched 8443) |
| Sniffing | cloned from 8443 |
| Client count | **1** |

## Test client

| Field | Value |
|-------|-------|
| Remark/email | `MCA-ONE-RAW-24443-AB` |
| Client id | 22 |
| UUID | **withheld** — retrieve from 3X-UI only |
| Daily key source | **3X-UI panel** (not MARS Git) |

## Backup

| Item | Path |
|------|------|
| Remote archive | `/root/mars-backups/eqvps-pre-raw-24443-ab-20260828T203556Z.tgz` |
| Local copy | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-pre-raw-24443-ab-20260828T203556Z.tgz` |
| SHA-256 | `061BA50B76F8C78790F2F90A1AFB995F53C090662AAACF06B36451EBB6E17975` |
| Archive readability | verified (local hash matches remote) |
| Rollback ready | **YES** |

### Rollback procedure (do not execute unless this wave causes server-side harm)

1. Stop experiment safely: disable/remove inbound `EQVPS-TLS-RAW-24443-AB` (port 24443) and linked test client only.
2. Remove UFW rule `24443/tcp` (comment: `EQVPS RAW 24443 A/B test`).
3. If DB drift occurs, restore `/etc/x-ui/x-ui.db` from backup dir inside the timestamped archive.
4. `systemctl restart x-ui` and verify listeners: 22, 443, **8443**, 20901, 2096; confirm **24443 absent**.
5. Re-verify TLS on 8443 and 443 unchanged.

**Do not** restore over production 8443/443 inbounds unless explicitly chartered.

## Firewall

| Rule | Status |
|------|--------|
| `24443/tcp` ALLOW | added (IPv4 + IPv6) |
| Other UFW rules | **NONE changed** |

Existing rules preserved: 22, 443, 8443, 20901, 2096.

## TLS validation (24443)

| Check | Result |
|-------|--------|
| Listen | `*:24443` present after restart |
| UFW allow | yes |
| Handshake (remote SNI) | OK |
| SNI | `metacode-cloud.com` |
| ALPN | `http/1.1` |
| Certificate CN | `metacode-cloud.com` |
| Issuer | Let’s Encrypt |
| Verify return code | **0 (ok)** |

## Isolated VLESS validation (Windows, no v2rayN DB/TUN changes)

Method: temporary local HTTP proxy `127.0.0.1:18089` via standalone Xray (`C:\Program Files\v2rayN\bin\xray\xray.exe`). Active operator VPN remained **VEESP**.

| Test | Result |
|------|--------|
| Egress IP | **95.216.126.173** |
| YouTube homepage | HTTP **200**, ~873 KB body |
| Cloudflare 1 MB | HTTP **200**, 1,048,576 bytes |
| Cloudflare 10 MB | HTTP **200**, 10,485,760 bytes |
| Local verdict | **RAW_24443_LOCAL_PASS** |

Timing samples (curl write-out):
- YouTube: connect ~0.001s, TLS ~0.279s, TTFB ~0.397s, total ~1.139s
- CF 1 MB: total ~1.134s
- CF 10 MB: total ~4.802s

## TCP A/B (25 attempts each, Windows host via current path)

| Target | Success | Fail | min ms | avg ms | max ms |
|--------|---------|------|--------|--------|--------|
| `metacode-cloud.com:8443` | 25 | 0 | 62 | 65.0 | 100 |
| `metacode-cloud.com:24443` | 25 | 0 | 61 | 63.4 | 68 |
| `178.173.250.69:8443` (VEESP) | 25 | 0 | 88 | 92.2 | 99 |

**Observation:** No TCP connect instability differential between EQVPS 8443 and 24443 in this bounded sample. 24443 slightly lower average latency; both 100% success.

ICMP ping (10 probes, not proof of app health):
- `95.216.126.173`: 10/10, avg ~61 ms
- `178.173.250.69`: 10/10, avg ~93 ms

Raw evidence: `tcp-connect-ab.json`, `ping-eqvps.txt`, `ping-veesp.txt`, `tracert-*.txt` under evidence folder.

## Path comparison

| Target | TCP connect (this session) | Notes |
|--------|---------------------------|-------|
| VEESP `178.173.250.69:8443` | 25/25 OK, ~92 ms avg | Control path baseline |
| EQVPS `95.216.126.173:8443` | 25/25 OK, ~65 ms avg | Same host, production port |
| EQVPS `95.216.126.173:24443` | 25/25 OK, ~63 ms avg | A/B port |

**UNRESOLVED:** Application-layer long-lived session behavior (Cursor Agent, Firefox video) cannot be distinguished from underlying path while operator remains on VEESP TUN during provisioning. Server-side and isolated-client tests do not reproduce the reported hangs.

## Provider/network research (2026-08-29)

| Classification | Fact |
|----------------|------|
| **RECENTLY RESOLVED** | NBG1–FRA backbone maintenance completed **2026-08-28 12:07 UTC** — brief latency risk only |
| **RECENTLY RESOLVED / WATCHING** | FRA–HEL backbone fault started **2026-08-21**; last update **2026-08-23** monitoring — not reoccurred over weekend per Hetzner |
| **UNRELATED** | Object Storage NBG/HEL degradations — not EQVPS compute/VPS path |
| **ACTIVE INCIDENT** | None identified affecting EQVPS VPS TCP ingress on 2026-08-29 |

**Relevance:** Possible background latency/packet-loss history on Helsinki-related backbone, but **no active incident** at provisioning time. Does **not** explain port-specific 8443 vs 24443 difference (none observed in TCP A/B).

## 3X-UI

| Check | Result |
|-------|--------|
| Inbound `EQVPS-TLS-RAW-24443-AB` visible in DB/runtime | **YES** |
| Client `MCA-ONE-RAW-24443-AB` visible | **YES** |
| Linked clients on 24443 | 1 |
| Daily key source | **3X-UI** |

## Mutations

### EQVPS (exact)
- INSERT inbound id **4**: `EQVPS-TLS-RAW-24443-AB` / port **24443** / VLESS+TLS+RAW/tcp (cloned from 8443 stream/sniffing)
- INSERT/UPDATE client id **22**: `MCA-ONE-RAW-24443-AB` with fresh UUID (secret)
- INSERT `client_inbounds` link
- UFW allow **24443/tcp** only
- `systemctl restart x-ui`

### VEESP
- **NONE**

### Windows / v2rayN
- **NONE** to v2rayN profile DB, TUN, routing, DNS, or global settings
- Temporary isolated Xray process only (local evidence)

## Git

**NO COMMIT**

## OPERATOR TEST (after this task — manual)

1. Open 3X-UI panel on EQVPS (existing operator access path).
2. Locate inbound **`EQVPS-TLS-RAW-24443-AB`** (port **24443**).
3. Copy VLESS URI / QR for client **`MCA-ONE-RAW-24443-AB`** from 3X-UI (do not use MARS Git files for daily key).
4. Import into v2rayN as a **separate profile**; do not alter global TUN/routing/DNS settings.
5. Activate **24443** profile; confirm latency indicator.
6. Test Firefox: YouTube homepage, real video playback, ChatGPT.
7. Test Cursor: one simple Agent prompt.
8. Switch back to **`MCA-ONE-RAW-8443`** on port **8443** and repeat steps 5–7 for A/B comparison.

**Note:** Cursor may disconnect when switching VPN — that is expected and does not invalidate server provisioning.

## Interpretation (pre-operator)

| Outcome | Meaning |
|---------|---------|
| If **24443 works** in Firefox/Cursor while **8443 fails** | **PORT/PATH-SPECIFIC BEHAVIOR STRONGLY SUPPORTED** (middlebox or port-targeted interference) |
| If **both fail identically** while server + isolated client pass | **PORT HYPOTHESIS REJECTED**; investigate EQVPS network path / long-lived application connection behavior / client TUN stack |
| Current server-side TCP A/B | **No port-dependent connect anomaly** detected |

## NEXT ACTION

**WAIT FOR OPERATOR A/B RESULT**

---
Evidence bundle: `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-24443-ab-2026-08-29\`

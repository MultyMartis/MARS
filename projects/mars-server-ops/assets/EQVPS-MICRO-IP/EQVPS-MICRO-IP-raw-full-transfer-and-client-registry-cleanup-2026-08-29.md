# EQVPS-MICRO-IP — RAW full-transfer diagnostic + 3X-UI client registry cleanup (2026-08-29)

**Wave:** network diagnostic reset + operator-facing client registry cleanup  
**Host:** `metacode-cloud.com` / `95.216.126.173`  
**Production candidate:** VLESS + TLS + RAW/tcp on TCP/8443  
**Operator working VPN during wave:** VEESP (`wsp-cloud.com:8443`) — **not modified**

This document is **Git-safe**. It contains **no** panel passwords, UUIDs, VLESS URIs, subscription tokens, or private keys.

---

## 1. Strategy reset

### Previously proven incorrectly

- Small **HEAD** / short-response checks (Google/YouTube/ChatGPT HEAD, api.ipify) were treated as sufficient transport proof.
- Those tests did **not** establish sustained full-body HTTPS transfer viability.
- XHTTP / Custom Config troubleshooting paths are **historical/deferred** and were **not** revisited in this wave.

### Tested now

- Isolated local Xray client on `127.0.0.1:18088` (mixed inbound), outbound to EQVPS RAW `:8443` with ALPN `http/1.1`, fingerprint `chrome`, mux disabled.
- **Full-body** downloads with timing/byte metrics.
- HTTP/1.1 vs HTTP/2 differential (where curl supports it).
- Socket observation during large transfer (local + server read-only `ss -ti`).
- MTU/PMTU read-only collection (Windows + EQVPS) and bounded DF ping probes.
- 3X-UI client registry cleanup to make the panel the operator-facing key source.

---

## 2. Full-transfer classification

**Result:** `EQVPS_RAW_FULL_TRANSFER_PASS`

**Implication:** Isolated EQVPS RAW network path can sustain full HTTPS body transfers. Remaining browser hang symptom when using EQVPS through v2rayN is classified as **`V2RAYN_TUN_PATH_SPECIFIC`** pending targeted comparison (not proven as server RAW stall in this wave).

---

## 3. RAW isolated full-transfer summary (127.0.0.1:18088)

| Test | Exit | Bytes | Total time | Notes |
|------|------|-------|------------|-------|
| api.ipify.org | 0 | 15 | ~0.3s | Egress `95.216.126.173` |
| Google HEAD (control) | 0 | small | fast | HTTP 200 |
| YouTube HEAD (control) | 0 | small | fast | HTTP 200 |
| ChatGPT HEAD (control) | 0 | small | fast | HTTP 403 challenge (network reachable) |
| **YouTube full body** | 0 | **760,412** | **~0.91s** | ~833 KB/s |
| **ChatGPT full body** | 0 | **8,463** | **~0.36s** | 403 body = transfer proof |
| **Cloudflare ~1 MB** | 0 | **1,000,000** | **~0.93s** | ~1.05 MB/s |
| **Cloudflare ~10 MB** | 0 | **10,000,000** | **~1.57s** | ~6.2 MB/s |

Raw evidence directory (local-only):

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-full-transfer-diagnostic-raw-2026-08-29\`

---

## 4. HTTP version differential

- Windows `curl.exe` on operator workstation: **`--http2` not supported** → HTTP/2 differential **SKIPPED**.
- HTTP/1.1 full-body tests **completed successfully** for YouTube, Google-sized payloads, and Cloudflare speed endpoints.

---

## 5. TCP / socket evidence (read-only)

During active ~10 MB download through isolated `:18088`:

- Local Xray process showed established connection to `95.216.126.173:8443`.
- VEESP v2rayN process remained active to `178.173.250.69:8443` (operator not switched).
- Server `ss -ti` on `:8443` from operator public IP showed **elevated retransmissions/loss counters on some sockets** (e.g. non-zero `bytes_retrans`, `lost`, `retrans`, `cwnd:1`) **while download still completed at multi-MB/s**.

**Interpretation:** path shows occasional loss/retrans under load, but **did not prevent** isolated full-transfer completion. Not classified as PMTU blackhole.

Evidence files: `local-xray-sockets.txt`, `server-8443-sockets.txt` (local-only diagnostic folder).

---

## 6. MTU / PMTU

### Windows (read-only)

| Interface | MTU |
|-----------|-----|
| Ethernet | 1500 |
| Loopback | default |

TUN adapter present for VEESP session; not used for isolated `:18088` tests.

### EQVPS (read-only)

| Item | Value |
|------|-------|
| Primary interface | `eth0` UP |
| Interface MTU | **1500** |
| Default route | via `95.216.126.161` dev `eth0` |
| `net.ipv4.ip_no_pmtu_disc` | 0 |
| `net.ipv4.tcp_mtu_probing` | 0 |
| `net.ipv4.tcp_base_mss` | 1024 |
| `net.ipv4.tcp_min_snd_mss` | 48 |

### DF probe (Windows → 95.216.126.173)

- Bounded `-f -l` probes: payloads **500–1472** succeeded.
- Largest successful payload in sweep: **1472**
- Approximate path MTU: **1472 + 28 = 1500**

No PMTU blackhole evidence from DF probes.

---

## 7. Root cause status

| Category | Status |
|----------|--------|
| **FACTS** | Isolated EQVPS RAW full-body transfers PASS; api.ipify egress correct; MCA-ONE RAW identity preserved through cleanup; post-cleanup isolated ipify re-check PASS; VEESP remained active operator profile |
| **INFERENCES** | Browser hang on YouTube/ChatGPT when using EQVPS via v2rayN likely involves **v2rayN routing/TUN/DNS/split-tunnel path**, not raw EQVPS transport stall; server socket stats show loss/retrans under load but transfers complete |
| **UNPROVEN** | Exact v2rayN mechanism (TUN vs explicit proxy vs DNS vs routing rules); HTTP/2-specific inner behavior (curl limitation); whether browser hang reproduces on `:10808` full-body curl vs `:18088` |

---

## 8. 3X-UI backup (pre client cleanup)

| Item | Value |
|------|-------|
| Local path | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\post-raw-pre-client-cleanup-2026-08-29\x-ui.db` |
| SHA256 | `0E1B3E0878F18500D741026A9335562F631D027ADDAA956CB7B35CE64E531E7E` |
| Server rollback copy | `/etc/x-ui/x-ui.db.pre-cleanup-2026-08-29` |
| Rollback ready | **YES** |

---

## 9. Client registry cleanup

**Server mutation:** YES — client registry cleanup only. **No transport architecture mutation.**

### Before (summary)

| Client | Inbound | Classification | Action |
|--------|---------|----------------|--------|
| marsops-reality-primary | orphan (no inbound) | HISTORICAL_DELETE | DELETE |
| marsops-fallback-xhttp | RAW 8443 | OBSOLETE_DELETE | DELETE |
| marsops-xhttp-443-primary | XHTTP 443 | TECHNICAL_KEEP | RENAME → MARS-XHTTP-443-TEST |
| MCA-ONE-RAW-8443 | RAW 8443 | PRODUCTION_KEEP | KEEP (UUID preserved) |
| MCA-ONE-FALLBACK-8443 | RAW 8443 | OBSOLETE_DELETE | DELETE |
| MCA-PHONE-FALLBACK-8443 | RAW 8443 | OBSOLETE_DELETE | DELETE |
| Unit-01..03, Unit-MichaelPhone *-FALLBACK-8443 | RAW 8443 | OBSOLETE_DELETE | DELETE |
| MCA-ONE..Unit-MichaelPhone *-PRIMARY-443 | XHTTP 443 | OBSOLETE_DELETE | DELETE |

Full before inventory: `client-registry-cleanup-raw-2026-08-29\inventory-before.txt` (local-only).

### After

**RAW 8443 production (inbound `EQVPS-TLS-RAW-8443`, tcp):**

- MCA-ONE-RAW-8443 (**UUID preserved**)
- MCA-PHONE-RAW-8443 (new identity)
- Unit-01-RAW-8443 (new identity)
- Unit-02-RAW-8443 (new identity)
- Unit-03-RAW-8443 (new identity)
- Unit-MichaelPhone-RAW-8443 (new identity)

**XHTTP 443 (inbound unchanged, experimental/deferred):**

- **MARS-XHTTP-443-TEST** (single technical test client; renamed from prior technical identity)

**Deleted obsolete clients:** 14 identities removed (orphan Reality, fallback XHTTP, six PRIMARY-443 production XHTTP clients, six FALLBACK-8443 stale clients, plus duplicate technical naming cleanup via rename).

New non-MCA-ONE RAW UUID map stored locally only: `client-registry-cleanup-raw-2026-08-29\new-raw-uuids.local.json` (**not for Git**).

Post-cleanup inventory: `client-registry-cleanup-raw-2026-08-29\inventory-after.txt` (local-only).

---

## 10. Panel operator workflow (updated)

**For normal device provisioning, key retrieval, QR, and subscription:**

→ **Use the 3X-UI panel** (`https://metacode-cloud.com:20901/...` — exact path in local `operator-access.local.md`).

**MARS local files** (`clients\`, secrets, backups) remain:

- backup / evidence / disaster recovery / automation support
- **not** the primary human daily key UI

See updated `EQVPS-MICRO-IP-operator-client-runbook-v1.md`.

---

## 11. Server health (post cleanup)

| Check | Status |
|-------|--------|
| x-ui | **active** |
| Xray (standalone unit) | inactive (embedded in x-ui — expected) |
| :22 | listening |
| :443 | listening (XHTTP inbound unchanged) |
| :8443 | listening (RAW/TLS) |
| :20901 | listening (panel) |
| :2096 | listening (subscription) |
| New ports | **none observed** |
| MCA-ONE RAW auth (isolated :18088 post-cleanup) | **PASS** (ipify → 95.216.126.173) |

---

## 12. Mutations summary

| Area | Changed |
|------|---------|
| EQVPS transport architecture | **NO** |
| VEESP | **NO** |
| v2rayN | **NO** |
| 3X-UI client registry | **YES** |
| Git commit | **NO** |

---

## 13. Next action

Because isolated EQVPS RAW **full transfer PASS**:

→ Remaining problem is **v2rayN/TUN-path-specific**.

**Smallest next diagnostic (without switching VEESP TUN):**

Run full-body curl through **v2rayN explicit proxy** `:10808` (same URLs as Phase E: YouTube + ChatGPT + 10 MB Cloudflare) and compare byte/time metrics against isolated `:18088` baseline. If `:10808` stalls while `:18088` passes, the defect is inside v2rayN proxy/routing/DNS handling for EQVPS profile — not EQVPS RAW server transport.

---

## 14. Evidence paths

| Artifact | Path |
|----------|------|
| Network diagnostic raw | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-full-transfer-diagnostic-raw-2026-08-29\` |
| Client cleanup raw | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\client-registry-cleanup-raw-2026-08-29\` |
| Git-safe report (this file) | `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-raw-full-transfer-and-client-registry-cleanup-2026-08-29.md` |

# Client Compatibility v1 — MCA-VPN-001

**Status:** Historical notes + current Windows Clash Verge candidate pointer — **not** a live device inventory  
**Scope:** Documented client behaviour and future dual-profile requirement

---

## 1. CONFIRMED HISTORICAL

### Windows — v2rayN

| Fact | Detail | Confidence |
|------|--------|------------|
| Client used | **v2rayN** on Windows | HIGH |
| Server-side fault | Not proven for TUN/startup issues | — |

**Known client-side issues after Windows reinstall:**

| Symptom | Detail |
|---------|--------|
| Startup/minimize | Application did not restore expected state reliably after reboot |
| TUN elevation | TUN required UAC / elevation |
| First TUN enable | Did not persist — TUN appeared off again after UAC |
| Second TUN enable | Worked |

**Classification:** CONFIRMED HISTORICAL — client-side UX issue; contributed to search for alternatives.

**Current workstation posture (2026-09-11):** v2rayN is **not** the preferred daily driver. See [CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md](../../CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md). Unified Clash profile covers VEESP + FriendHosting via group `MARS-VPN`. Do not run v2rayN TUN and Clash TUN together.

### Windows — Clash Verge (current preferred candidate, 2026-09)

| Fact | Detail | Confidence |
|------|--------|------------|
| Preferred candidate client | **Clash Verge Rev 2.5.2** / **Mihomo v1.19.29** TUN **System** | HIGH (operator A/B + gVisor→System result) |
| Acceptance | **PROVISIONALLY ACCEPTED — SYSTEM STACK** · **FINAL SOAK PENDING** | — |
| Unified profile | `X:\AI MARS\local\infrastructure\CLASH-VERGE-WINDOWS\mars-vpn-windows.yaml` (gitignored) | HIGH |
| Authority | `X:\AI MARS\projects\mars-server-ops\CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md` | — |

**Classification:** CURRENT CANDIDATE BASELINE — not a claim of final soak-proven stability.

---

## 2. MEDIUM confidence

| Platform | Client | Notes |
|----------|--------|-------|
| Android | **v2rayNG** | Appeared in legacy generated documentation — verify current operator preference |

---

## 3. Future requirement (APPROVED / INTENDED)

Client devices must support **independent profiles**:

| Profile | Server |
|---------|--------|
| **Server A profile** | MCA-VPN-001 (existing) |
| **Server B profile** | Future independent VPS |

### Failover model (initial)

| Approach | Status |
|----------|--------|
| **Manual profile switching** | **Acceptable** for initial Server B rollout |
| Automatic failover | **Not designed** in this wave — defer |

### Server B client identity rule

Server B requires **new** credentials and secrets — do **not** clone Server A client URIs, UUIDs, or subscription tokens into Git or shared docs.

---

## 4. Explicit exclusions

Do **not** store in this repository:

- Client secret URIs / subscription links
- QR payload secrets
- Per-client UUID values
- Reality key material

---

## 5. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Exact subscription format/token | SAFE UNKNOWN |
| Number of active clients | SAFE UNKNOWN |
| iOS / macOS / Linux clients in use | SAFE UNKNOWN |

---

## Related documents

- [CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md](../../CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md)
- [SERVER-B-CLONE-BASELINE-v1.md](SERVER-B-CLONE-BASELINE-v1.md)
- [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md) — Incident E (v2rayN)

---

*Client Compatibility v1 · historical + planning · Windows Clash Verge pointer 2026-09-11 · no client secrets.*

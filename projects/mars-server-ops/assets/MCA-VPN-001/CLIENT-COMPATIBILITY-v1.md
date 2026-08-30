# Client Compatibility v1 — MCA-VPN-001

**Status:** Historical client notes — **not** live client inventory  
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
| Current preferred Windows client post-v2rayN issues | SAFE UNKNOWN |

---

## Related documents

- [SERVER-B-CLONE-BASELINE-v1.md](SERVER-B-CLONE-BASELINE-v1.md)
- [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md) — Incident E (v2rayN)

---

*Client Compatibility v1 · historical + planning · no client secrets.*

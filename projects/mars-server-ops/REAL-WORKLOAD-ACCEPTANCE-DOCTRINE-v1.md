# MARS Server Ops — Real-Workload Acceptance Doctrine v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **BASELINE v1** — reusable acceptance vocabulary and evidence hierarchy  
**Origin:** VPN case study (AdminVPS → EQVPS → FriendHosting / VEESP controls), 2026-08  
**Not:** automated test product, monitoring fleet, or claim that any live service is production-accepted

---

## 1. Purpose

Separate **technical reachability** from **operator-usable acceptance**.

Primary lesson from EQVPS:

```text
TRANSPORT PASS ≠ REAL-WORKLOAD ACCEPTANCE PASS
```

A node that passes ping, TLS, HTTPS, and even multi-megabyte body transfer can still **FAIL** Cursor, ChatGPT, YouTube playback, or similar interactive workloads.

---

## 2. Scoped acceptance states

Use these labels explicitly. Do not collapse them into a single “PASS”.

| State | Meaning |
|-------|---------|
| `SERVER_PROCESS_PASS` | Required processes/services are running (e.g. xray, nginx, sshd) |
| `PORT_LISTEN_PASS` | Expected ports listen on expected interfaces |
| `TLS_PASS` | Certificate / handshake / SNI behaviour acceptable for the charter |
| `TRANSPORT_PASS` | Proxy/VPN egress + repeated HTTPS/body transfer pass under controlled client |
| `EGRESS_PASS` | Observed public egress matches expected node IP/path |
| `APPLICATION_PASS` | Named application completes a **functional** task (not mere HTTP fetch) |
| `REAL_WORKLOAD_ACCEPTANCE_PASS` | Required real workloads pass under the intended operator client path |
| `OPERATIONALLY_ACCEPTED_CURRENT_VPN_WORKLOAD` | Node accepted for **current VPN operator workloads** after transport + real-workload + hardening + identity + backup gates — **still not** generic production; soak may remain unproven |
| `PRODUCTION_ACCEPTED` | Operator promotion after **long-term soak** + backup/restore completeness (including DR expectations named by charter) + hardening gates |

**Rules:**

- Each state is **scoped** to a charter, client path, and time window.  
- `APPLICATION_PASS` for one prompt/session is **insufficient** for `REAL_WORKLOAD_ACCEPTANCE_PASS`.  
- `REAL_WORKLOAD_ACCEPTANCE_PASS` is **insufficient** for `OPERATIONALLY_ACCEPTED_CURRENT_VPN_WORKLOAD` without hardening/backup/identity gates named by programme.  
- `OPERATIONALLY_ACCEPTED_CURRENT_VPN_WORKLOAD` is **insufficient** for `PRODUCTION_ACCEPTED` without soak and fuller DR discipline.  
- Do **not** claim generic production suitability for arbitrary apps from a VPN acceptance alone.  
- Missing evidence = **NOT TESTED** / **UNPROVEN** — never silent PASS.

**Acceptance ladder (never collapse):**

```text
PING ≠ TCP ≠ TLS ≠ TRANSPORT ≠ APPLICATION ≠ REAL-WORKLOAD
  ≠ OPERATIONALLY ACCEPTED (scoped) ≠ LONG-TERM STABILITY ≠ PRODUCTION_ACCEPTED
```

---

## 3. Evidence hierarchy (highest → lowest)

When conclusions conflict, prefer higher evidence:

1. **Repeatable real-workload acceptance** (same client path; recovery control where applicable)  
2. **Controlled A/B/A** (endpoint or variable switch with pre/post control)  
3. **Large / full-body transport** (multi-MB HTTPS via intended proxy path)  
4. **Simple HTTP / HTTPS** (HEAD/GET status)  
5. **TLS handshake**  
6. **TCP connect / known-listener gate**  
7. **Ping / ICMP**  
8. **Hypothesis / marketing / looking-glass alone**

```text
repeatable real workload
  >
controlled A/B/A
  >
large/full-body transport
  >
simple HTTP
  >
TLS
  >
TCP
  >
ping
  >
hypothesis
```

---

## 4. VPN workload examples (minimum set when VPN is the mission)

| Workload | Acceptance signal |
|----------|-------------------|
| **Cursor** | Multi-cycle Agent/diagnostic session usable (not one fetch) |
| **ChatGPT** | Operator prompt/response usable |
| **YouTube** | Playback (not thumbnails-only) |
| **Browser interaction** | Representative sites required by charter |
| **Telegram** | Where required by charter |

Record **PASS / FAIL / NOT TESTED** per workload. Non-blocking failures must be labelled as such.

---

## 5. Repetition rule

| Pattern | Interpretation |
|---------|----------------|
| One successful app prompt | **Insufficient** for stable PASS |
| Multi-cycle same session | Minimum for `APPLICATION_PASS` |
| Pre-control → candidate → post-control | Required to claim endpoint-follow failure |
| Hours/days soak without config churn | Required before `PRODUCTION_ACCEPTED` (not required to claim scoped `OPERATIONALLY_ACCEPTED_CURRENT_VPN_WORKLOAD`) |

---

## 6. Reporting discipline

Every acceptance REPORT should state:

- which states were tested;  
- which passed / failed / not tested;  
- client path (TUN / system proxy / mixed port);  
- exact endpoint identity (sanitized);  
- evidence paths;  
- whether exact root cause is **UNPROVEN**.

---

## 7. Related documents

- [CONTROL-EVIDENCE-METHODOLOGY-v1.md](CONTROL-EVIDENCE-METHODOLOGY-v1.md)  
- [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](SUPERSEDED-CONCLUSIONS-REGISTER-v1.md)  
- [VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md)  
- [SERVER-OPS-AGENT-KNOWLEDGE-v1.md](SERVER-OPS-AGENT-KNOWLEDGE-v1.md)  
- [assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-CURRENT-TRUTH-v1.md](assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-CURRENT-TRUTH-v1.md)  
- [reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md](reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md)

---

*Real-Workload Acceptance Doctrine v1 · updated for scoped operational acceptance · documentation only · no runtime claimed.*

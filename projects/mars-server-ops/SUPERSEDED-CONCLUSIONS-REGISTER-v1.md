# MARS Server Ops — Superseded Conclusions Register v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **canonical register** — human-maintained  
**Rule:** Do not preserve an old conclusion merely because it already exists in MARS.  
**Not:** automated truth engine

---

## 1. Purpose

Record important claims that later evidence **contradicted** or **narrowed**, so agents and operators do not revive stale truths from older reports or chat handoffs.

Each entry:

| Field | Content |
|-------|---------|
| `id` | Stable register id |
| `old_claim` | What was previously believed or written |
| `status` | `SUPERSEDED` (required for entries here) |
| `new_evidence` | What overturned it |
| `replacement_truth` | Current standing statement |
| `source_refs` | Reports / assets |

---

## 2. Active superseded entries (VPN case study era)

### SC-001 — VEESP production inbound is WebSocket

| Field | Value |
|-------|-------|
| **old_claim** | VEESP / MCA-VPN-001 primary client path is WS (WebSocket). |
| **status** | **SUPERSEDED** |
| **new_evidence** | EXP-A01 live effective config: VLESS + TLS + RAW/TCP `:8443` (`network: tcp`, header `none`). |
| **replacement_truth** | Current proven VEESP working architecture for control acceptance: **VLESS + TLS + RAW/TCP `:8443`**. Aug 25 “WS” intake language is stale documentation. |
| **source_refs** | `reports/MARS-SERVER-OPS-EXP-A01-LIVE-VEESP-EQVPS-RUNTIME-RECONCILIATION.md` |

### SC-002 — EQVPS `:24443` Cursor stable PASS

| Field | Value |
|-------|-------|
| **old_claim** | EQVPS RAW/TLS `:24443` yielded a stable Cursor PASS usable as acceptance. |
| **status** | **SUPERSEDED** as standing acceptance claim (never established as durable PASS in audit; treat any one-run anecdote as non-canonical). |
| **new_evidence** | EQVPS AUDIT 01 + EXP-A01b: real-app acceptance on EQVPS **FAIL**; `:24443` not proven better than `:8443`. |
| **replacement_truth** | EQVPS real-workload acceptance = **FAIL/unstable**. Port A/B alone does not equal application PASS. |
| **source_refs** | `reports/MARS-SERVER-OPS-EQVPS-AUDIT-01-…`, `reports/MARS-SERVER-OPS-EXP-A01b-…` |

### SC-003 — Transport PASS equals VPN acceptance

| Field | Value |
|-------|-------|
| **old_claim** | Isolated/full-body transport PASS on EQVPS means the VPN path is acceptance-complete. |
| **status** | **SUPERSEDED** |
| **new_evidence** | EXP-A01b A/B/A: EQVPS transport PASS while Cursor/ChatGPT/YouTube FAIL; VEESP recovery restores apps. |
| **replacement_truth** | Use [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md). `TRANSPORT_PASS` ≠ `REAL_WORKLOAD_ACCEPTANCE_PASS`. |
| **source_refs** | EXP-A01b; FriendHosting real-app acceptance report |

### SC-004 — Premature HTTP/2 / early root-cause theories as proven EQVPS cause

| Field | Value |
|-------|-------|
| **old_claim** | Specific early theories (e.g. HTTP/2-only, single knob) treated as proven EQVPS root cause. |
| **status** | **SUPERSEDED** as proven mechanism |
| **new_evidence** | Multi-wave matrix leaves exact mechanism **UNPROVEN**; FriendHosting third control strengthens endpoint/ASN/path/reputation domain without isolating one sub-cause. |
| **replacement_truth** | Strongest diagnosis domain = EQVPS endpoint / Hetzner-HEL path / reputation / app treatment (+ residual config confounds). Exact root cause = **UNPROVEN**. |
| **source_refs** | FriendHosting NETWORK-REALAPP-ACCEPTANCE-01 §21; EXP-A01b |

### SC-005 — Reality failure caused by CRLF alone

| Field | Value |
|-------|-------|
| **old_claim** | CRLF line endings alone caused Reality inbound failure. |
| **status** | **SUPERSEDED / INCOMPLETE** |
| **new_evidence** | Reality FIX-02: CRLF was hygiene only; LF import still produced invalid stored PublicKey. |
| **replacement_truth** | CRLF is a hygiene issue, not the complete Reality failure mechanism. |
| **source_refs** | `reports/MARS-SERVER-OPS-EQVPS-ALT-A-REALITY-VISION-FIX-02.md` |

### SC-006 — Pre-listener FriendHosting `:443` timeouts = network failure

| Field | Value |
|-------|-------|
| **old_claim** | Early FriendHosting `:443` 0/25 timeouts proved path/network failure. |
| **status** | **SUPERSEDED AS PORT-PATH EVIDENCE** |
| **new_evidence** | Intake-01: after known listener, TCP `:443` 25/25 PASS; pre-listener timeouts classified non-diagnostic. |
| **replacement_truth** | Known-listener TCP gates are required before interpreting timeouts as path failure. |
| **source_refs** | `reports/MARS-SERVER-OPS-FRIENDHOSTING-INTAKE-01-DIRECT-443-GATE.md` |

### SC-007 — FriendHosting unproven / not justified as control

| Field | Value |
|-------|-------|
| **old_claim** | FriendHosting control unjustified (EXP-A01 standing gate NO) / node unproven. |
| **status** | **SUPERSEDED** |
| **new_evidence** | EXP-A01b justified independent control; Intake/Build/nginx waves completed; NETWORK-REALAPP-ACCEPTANCE-01: TRANSPORT PASS + REAL-APP PASS. |
| **replacement_truth** | FriendHosting = independent modern control; lifecycle = **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD**; long-term soak **NOT YET PROVEN**; **not** `PRODUCTION_ACCEPTED`. |
| **source_refs** | EXP-A01b; FriendHosting acceptance reports; DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01 |

### SC-008 — CASE A provider/path strengthening NOT established (EXP-A01 standing)

| Field | Value |
|-------|-------|
| **old_claim** | EXP-A01: CASE A not established; FriendHosting gate NO. |
| **status** | **SUPERSEDED** |
| **new_evidence** | EXP-A01b completed same-TUN A/B/A with application-layer differential. |
| **replacement_truth** | Application-layer endpoint differential **established**; exact sub-cause still **UNPROVEN**. |
| **source_refs** | EXP-A01b §22 |

### SC-009 — EQVPS XHTTP dual-path as current production baseline

| Field | Value |
|-------|-------|
| **old_claim** | XHTTP dual path / early “PRODUCTION STABLE” framing as current EQVPS production truth. |
| **status** | **SUPERSEDED as production path** |
| **new_evidence** | RAW `:8443` control deployment + cleanup; audit marks XHTTP retained for testing only. |
| **replacement_truth** | EQVPS production **candidate** class was VLESS+TLS+RAW `:8443`; current operational verdict = transport PASS / real-workload FAIL. |
| **source_refs** | EQVPS AUDIT 01; RAW 8443 control deployment asset |

### SC-010 — UpCloud / FI-HEL1 as active Server B procurement path

| Field | Value |
|-------|-------|
| **old_claim** | UpCloud FI-HEL1 is the active Server B procurement decision. |
| **status** | **SUPERSEDED** |
| **new_evidence** | Eligibility/compliance conflict; AdminVPS path selected. |
| **replacement_truth** | Historical UpCloud decision retained as SUPERSEDED artifact only. |
| **source_refs** | `assets/SERVER-B-PLANNING/PROCUREMENT-DECISION-v1.md` |

### SC-011 — FriendHosting remains only CONTROL / OPERATIONAL-CANDIDATE after final backup

| Field | Value |
|-------|-------|
| **old_claim** | After transport/real-workload/hardening/identity/backup gates, FriendHosting must still be labelled only `CONTROL / OPERATIONAL-CANDIDATE` with no scoped operational acceptance state. |
| **status** | **SUPERSEDED** |
| **new_evidence** | Documentation consolidation 01 reconciles taxonomy: technical build PASS · transport PASS · real-workload PASS · hardening PASS · backup PASS · per-device identity migration PASS. |
| **replacement_truth** | Use `OPERATIONALLY_ACCEPTED_CURRENT_VPN_WORKLOAD` (scoped VPN). Soak remains **NOT YET PROVEN**. Do **not** set `PRODUCTION_ACCEPTED`. Control role (independent modern control) remains true. |
| **source_refs** | `reports/MARS-SERVER-OPS-FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01.md`; Real-Workload Acceptance Doctrine |

### SC-012 — Shared MCA-ONE UUID remains FriendHosting canonical identity

| Field | Value |
|-------|-------|
| **old_claim** | Shared/legacy `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` remains the standing primary identity model. |
| **status** | **SUPERSEDED** |
| **new_evidence** | P3 per-device model + P3.1 legacy retirement: six device identities; legacy deleted from server. |
| **replacement_truth** | Canonical model = one VLESS identity per device; legacy **RETIRED**. |
| **source_refs** | P3-PER-DEVICE; P3-LEGACY-RETIREMENT-CLOSEOUT-01 |

---

## 3. Count

**Active superseded entries in this register:** **12** (SC-001 … SC-012).

Wave-local superseded counts inside older reports remain historical; this register is the **canonical** consolidation point going forward.

---

## 4. How to add entries

1. Prefer updating this register over scattering “SUPERSEDED” only inside one REPORT.  
2. Link the REPORT that established the replacement truth.  
3. Do not delete historical reports — mark them stale via this register.  
4. Never put secrets in register rows.

---

## 5. Related documents

- [CONTROL-EVIDENCE-METHODOLOGY-v1.md](CONTROL-EVIDENCE-METHODOLOGY-v1.md)  
- [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md)  
- [reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md](reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md)

---

*Superseded Conclusions Register v1 · FriendHosting documentation consolidation 01 · 2026-08-30.*

# REPORT — MARS Server Ops VPN Case Study Closeout 01

**Programme:** MARS Server Ops & VPS Forge  
**Wave:** VPN-CASE-STUDY-CLOSEOUT-01  
**Date (local):** 2026-08-30  
**Mode:** DOCUMENTATION / KNOWLEDGE / REGISTRY reconciliation only  
**Git:** no commit / no push  

**Mutations this wave:** Server = 0 · VEESP = 0 · EQVPS = 0 · FriendHosting = 0 · Secret disclosure = 0 · Foreign WIP = 0  

---

## 1. Executive verdict

The AdminVPS → EQVPS → FriendHosting VPN investigation is consolidated into reusable Server Ops knowledge **before** any further FriendHosting production mutation.

| Verdict | Status |
|---------|--------|
| Overall closeout | **PASS** — current truth, doctrines, superseded register, inventory, and roadmap reconciled |
| VEESP | Positive control · VLESS+TLS+RAW `:8443` · real-workload **PASS** |
| EQVPS | Negative/problematic control · transport **PASS** · real-workload **FAIL** · exact root cause **UNPROVEN** |
| FriendHosting | Independent modern control / **OPERATIONAL-CANDIDATE** · transport **PASS** · real-workload **PASS** · soak **NOT YET PROVEN** · **not** `PRODUCTION_ACCEPTED` |
| Strongest EQVPS diagnosis | Endpoint / Hetzner-HEL path / prefix reputation / application treatment (+ residual config confounds) |
| Exact EQVPS root cause proven | **NO** |
| Next FriendHosting wave | **P1 — pre-hardening backup + restore anchor** |
| Server mutations this wave | **0** |

**Primary principle satisfied:** turn the VPN investigation into reusable MARS Server Ops knowledge before mutating the now-working FriendHosting node further.

---

## 2. Source / evidence precedence

Applied priority:

1. Newest reproducible evidence / current live reports  
2. Controlled A/B/A experiments  
3. Current programme documentation  
4. Older reports  
5. Historical handoffs (lessons learned — not immutable spec)

Conflicts → newer reproducible evidence wins. Contradicted older claims → **SUPERSEDED** in [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](../SUPERSEDED-CONCLUSIONS-REGISTER-v1.md).

**Primary current sources:**

- FriendHosting: Intake-01, Control-Node Build PREP, 3X-UI nginx public access, NETWORK-REALAPP-ACCEPTANCE-01  
- Controls: EXP-A01, EXP-A01b  
- History: EQVPS AUDIT 01, WEBGPT-HANDOFF-01, SERVER-B AdminVPS verdicts  
- Programme: OPERATIONAL-INDEX, SERVER-INVENTORY, BACKUP-RESTORE, VPS provider/preflight runbooks  

Root `X:\AI MARS\OPERATIONAL-INDEX.md` was **not present** at wave start — programme index used: `projects/mars-server-ops/OPERATIONAL-INDEX.md`.

---

## 3. Current infrastructure truth

### 3.1 VEESP (MCA-VPN-001)

| Field | Current truth |
|-------|---------------|
| Role | Positive historical/operational control |
| Architecture | **VLESS + TLS + RAW/TCP `:8443`** |
| Real workload | **PASS** (EXP-A01b A/B/A) |
| OS (live EXP-A01) | Ubuntu 22.04.5 LTS |
| Server Xray (EXP-A01) | 26.6.22 |
| Identity | `wsp-cloud.com` / `178.173.250.69` |

### 3.2 EQVPS (EQVPS-MICRO-IP)

| Field | Current truth |
|-------|---------------|
| Role | Negative/problematic control |
| Architecture (candidate) | VLESS + TLS + RAW/TCP `:8443` |
| Basic/transport acceptance | **PASS** |
| Real-workload acceptance | **FAIL / unstable** |
| Exact root cause | **UNPROVEN** |
| OS | Ubuntu 24.04.4 LTS |
| 3X-UI / Xray | 3.7.0 / 26.7.28 |
| Identity | `metacode-cloud.com` / `95.216.126.173` · Hetzner AS24940 class |

### 3.3 FriendHosting (FRIENDHOSTING-DE)

| Field | Current truth |
|-------|---------------|
| Role | Independent modern control / operational-candidate |
| OS | Ubuntu 24.04.4 LTS |
| Panel / core | 3X-UI 3.7.0 · Xray 26.7.28 |
| VPN | VLESS + TLS + RAW/TCP `:8443` · SNI `metacode-cloud.com` |
| Control plane | nginx `:443` → localhost-only 3X-UI |
| SSH | `:3333` |
| Network | `92.42.99.126` · `92.42.99.0/24` · AS47447 / 23M GmbH evidence |
| TRANSPORT | **PASS** |
| REAL-APP | **PASS** (Cursor / ChatGPT / YouTube incl. playback) |
| Long-term soak | **NOT YET PROVEN** |

No secret values recorded in this report.

### 3.4 AdminVPS (SERVER-B-PLANNING)

| Field | Current truth |
|-------|---------------|
| Role | Provider qualification case / assigned-IP rejection evidence |
| Host health | Historically PASS after bootstrap |
| Assigned IP direct entry | **REJECTED** |
| Provider globally rejected | **NO** |
| VPN stack | **ABSENT** |
| Lesson | Looking-glass / pre-purchase PASS ≠ assigned subnet/IP suitability |

---

## 4. VEESP verdict

**PASS as positive control.**

Standing claim that VEESP uses WS as the current proven working architecture is **SUPERSEDED** (SC-001). Live effective inbound for the acceptance matrix is RAW/TCP `:8443`.

---

## 5. EQVPS verdict

**Transport PASS · Real-workload FAIL · Root cause UNPROVEN.**

Useful as a **negative control**, not as an operational VPN for Cursor/ChatGPT/YouTube under the tested Goodline + v2rayN TUN path.

One-run `:24443` Cursor anecdotes are **not** acceptance (SC-002).

---

## 6. FriendHosting verdict

**Technical acceptance PASS · Real-workload acceptance PASS · Soak NOT YET PROVEN · Lifecycle = CONTROL / OPERATIONAL-CANDIDATE.**

Do **not** promote to `PRODUCTION_ACCEPTED` in this wave. Do **not** mutate further until P1 backup/restore completeness is chartered and executed.

---

## 7. Root-cause hypothesis update

Re-evaluated with FriendHosting as third control (from NETWORK-REALAPP-ACCEPTANCE-01, carried forward):

| Hypothesis | Update |
|------------|--------|
| Global Windows failure | **WEAKENED** |
| v2rayN generic issue | **WEAKENED** |
| Wintun/TUN generic issue | **WEAKENED** |
| Client Xray 26.7.28 generic issue | **WEAKENED** |
| Server Xray 26.7.28 generic issue | **WEAKENED** |
| VLESS TLS RAW generic issue | **WEAKENED** |
| Goodline generic incompatibility | **WEAKENED** |
| EQVPS configuration-specific issue | **UNCHANGED** (still possible; sniffing etc. confounds) |
| EQVPS IP/prefix reputation | **STRENGTHENED** |
| EQVPS/Hetzner/HEL path/provider interaction | **STRENGTHENED** |
| MTU | **WEAKENED** as primary explanation |
| DNS | **UNCHANGED** / residual |
| IPv6 | **WEAKENED** as differentiator |
| Application/CDN interaction | **STRENGTHENED** (with reputation/path) |

**Exact EQVPS mechanism:** **UNPROVEN**.

---

## 8. Superseded conclusions

Canonical register: [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](../SUPERSEDED-CONCLUSIONS-REGISTER-v1.md)

**Count this closeout:** **10** active entries (SC-001 … SC-010), including:

- Old VEESP WS characterization  
- EQVPS `:24443` Cursor stable PASS as standing claim  
- Premature HTTP/2 / single-knob root-cause theories as proven  
- Transport PASS interpreted as application PASS  
- Reality CRLF-only conclusion  
- Pre-listener FriendHosting `:443` timeout as network failure  
- FriendHosting unjustified / unproven  
- EXP-A01 “CASE A not established” standing gate  
- XHTTP dual-path as current production baseline  
- UpCloud as active Server B procurement  

---

## 9. Provider qualification lessons

Canonical homes (updated, not duplicated as parallel frameworks):

- [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  
- [VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md)  
- [VPS-PROCUREMENT-GATE-v1.md](../VPS-PROCUREMENT-GATE-v1.md)  

**Before purchase / commitment (direct ISP path):**

- TUN OFF · System Proxy OFF  
- ping · route · known-listener TCP · download  
- ASN/network diversity · country/provider diversity when required  

**Critical lesson:** provider looking-glass performance does **not** guarantee the assigned subnet/IP is suitable (**AdminVPS case**).

---

## 10. Real-workload acceptance doctrine

Canonical path:

`X:\AI MARS\projects\mars-server-ops\REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md`

States: `SERVER_PROCESS_PASS` → … → `TRANSPORT_PASS` → … → `REAL_WORKLOAD_ACCEPTANCE_PASS` → `PRODUCTION_ACCEPTED`.

One successful application prompt is **insufficient** for stable PASS.

---

## 11. Evidence hierarchy

Documented in Real-Workload Acceptance Doctrine and Control & Evidence Methodology:

```text
repeatable real workload > controlled A/B/A > large/full-body transport
> simple HTTP > TLS > TCP > ping > hypothesis
```

---

## 12. Control-node methodology

Canonical path:

`X:\AI MARS\projects\mars-server-ops\CONTROL-EVIDENCE-METHODOLOGY-v1.md`

| Role | Node |
|------|------|
| Positive | VEESP |
| Negative | EQVPS |
| Independent modern | FriendHosting |

Generalized to DB/Docker/staging/provider/service troubleshooting.

---

## 13. Anti-config-churn rule

If transport PASS and real workload FAIL: do **not** auto-churn Reality/XHTTP/WS/gRPC/BBR/sysctl/MTU/DNS/core versions.

Identify failure class → use controls → one variable → evidence → retest.

**No random performance tuning** unless evidence shows a bottleneck.

---

## 14. Backup / restore doctrine

Canonical path (updated completeness gate):

`X:\AI MARS\projects\mars-server-ops\BACKUP-RESTORE-MODEL-v1.md`

Rule: a backup is not operationally complete until a restore strategy exists.

Required properties: exact source · timestamp · location · hash/checksum where practical · readability · restore procedure · rollback boundary · post-restore validation.

---

## 15. Server registry reconciliation

**Canonical registry implementation:** [SERVER-INVENTORY-v1.md](../SERVER-INVENTORY-v1.md) (schema + asset rows — not a CMDB product).

Updated/added rows:

| inventory_ref | Update |
|---------------|--------|
| MCA-VPN-001 | Reconciled as positive control + RAW truth |
| EQVPS-MICRO-IP | **Added** negative control row |
| FRIENDHOSTING-DE | **Added** operational-candidate row |
| SERVER-B-PLANNING | Retained AdminVPS rejection case |

No secret values. Final ATLAS/MCA ID for FriendHosting remains **pending** separate charter.

---

## 16. FriendHosting lifecycle state

| Layer | Classification |
|-------|----------------|
| Technical acceptance | **PASS** |
| Real-workload acceptance | **PASS** |
| Long-term soak | **NOT YET PROVEN** |
| Programme lifecycle | **active — CONTROL / OPERATIONAL-CANDIDATE** |
| Production | **not** `PRODUCTION_ACCEPTED` |

---

## 17. FriendHosting next roadmap (planned — not executed)

| Priority | Wave | Notes |
|----------|------|-------|
| **P1** | Complete pre-hardening backup + restore anchor | Completeness gate before further mutation |
| **P2** | Operational/security hardening | See §17.1 principles |
| **P3** | Per-device VLESS identities / revocation | Local-only secret registry; no UUID/URI in Git |
| **P4** | Reserve VLESS TLS RAW inbound on **`:24443`** | Keep `:8443` intact; do **not** put RAW Xray on `:443` (nginx owns `:443`) |
| **P5** | Backup automation + health monitoring | Documentation/runbooks first |
| **P6** | Multi-day real-workload soak + promotion decision | Only then consider `PRODUCTION_ACCEPTED` |

**Explicit:** NO random performance tuning unless evidence demonstrates a bottleneck.  
**Explicit:** Do not introduce Reality/WS/gRPC solely for “more backups” before same-transport reserve validation.

### 17.1 Future hardening principles (planned, not executed)

- Preserve SSH `:3333` until replacement access proven  
- Verify SSH key-based operator access before password/root restrictions  
- Firewall review · fail2ban/security review  
- Certificate renewal validation · boot/recovery · disk/RAM/swap  
- Logging/rotation · reboot survival · backup/restore validation  
- Do **not** prescribe BBR/sysctl/MTU without evidence  

### 17.2 Client identity roadmap (planned)

Prefer one independent VLESS identity per device/operator endpoint (name · revoke/rotate · local-only secrets). Whether primary+reserve inbounds share device identity or use separate per-inbound identities remains an open taxonomy decision for a later charter (do not decide blindly here).

---

## 18. Server Ops Agent knowledge update

Agents must:

1. Read OPERATIONAL-INDEX + inventory before VPN/provider claims.  
2. Prefer Real-Workload Acceptance Doctrine over “curl PASS = done”.  
3. Consult Superseded Conclusions Register before restating old report claims.  
4. Use Control & Evidence Methodology instead of multi-variable churn.  
5. Keep secrets out of Git per SECRET-HANDLING-MODEL.  
6. Treat historical handoffs as lessons, not immutable specs.

---

## 19. Server Ops maturity / capability implications

| Area | Implication |
|------|-------------|
| Documentation maturity | Raised — doctrines + register now exist |
| Runtime/automation maturity | **Unchanged** — still documentation-first, human-supervised |
| Diagnostic maturity | Raised — three-control pattern proven useful |
| Production VPN maturity | FriendHosting candidate only; soak incomplete |
| Forbidden overclaim | Do not claim Server Ops Agent product, CMDB, or autonomous admin |

---

## 20. Wider post-VPN roadmap

After FriendHosting P-waves stabilize, return Server Ops to reusable lifecycle for:

Linux VPS · Docker apps · PostgreSQL · n8n · reverse proxy · TLS · deployments · backup/restore · migration · monitoring · incident response · storage/capacity · DB/application stacks.

```text
REQUIREMENTS → PREFLIGHT → BACKUP/ROLLBACK → DEPLOY → TECHNICAL VALIDATION
→ REAL-WORKLOAD ACCEPTANCE → DOCUMENTATION → MONITORING → RECOVERY
```

---

## 21. Exact files created / updated

### Created

| Path |
|------|
| `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md` |
| `X:\AI MARS\projects\mars-server-ops\REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md` |
| `X:\AI MARS\projects\mars-server-ops\CONTROL-EVIDENCE-METHODOLOGY-v1.md` |
| `X:\AI MARS\projects\mars-server-ops\SUPERSEDED-CONCLUSIONS-REGISTER-v1.md` |

### Updated

| Path |
|------|
| `X:\AI MARS\projects\mars-server-ops\SERVER-INVENTORY-v1.md` |
| `X:\AI MARS\projects\mars-server-ops\OPERATIONAL-INDEX.md` |
| `X:\AI MARS\projects\mars-server-ops\BACKUP-RESTORE-MODEL-v1.md` |
| `X:\AI MARS\projects\mars-server-ops\VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md` |
| `X:\AI MARS\projects\mars-server-ops\VPS-PROVIDER-SELECTION-RUNBOOK-v1.md` |

---

## 22. Git closeout

| Item | Status |
|------|--------|
| Branch | `mars/canonical-post-recovery` |
| Volume | `X:` / `AI WS` |
| Commit | **0** |
| Push | **0** |
| Broad git add | **0** |
| Foreign WIP | Present elsewhere — **out of scope** · not staged · not mutated |
| HEAD vs origin | Pre-existing divergence noted — **not altered** this wave |
| Server mutations | **0** |

**STOP.** Next action requires a **separate charter** (recommended: FriendHosting **P1** backup + restore anchor).

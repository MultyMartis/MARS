# REPORT — MARS Server Ops Web-GPT Knowledge Handoff 01

**Programme:** MARS Server Ops & VPS Forge  
**Task class:** READ-ONLY / EVIDENCE-FIRST knowledge acquisition  
**Generated:** 2026-08-29  
**Workspace:** `X:\AI MARS` · volume label **AI WS** · branch `mars/canonical-post-recovery`  
**Mutations in this task:** Git = 0 · Server = 0 · VPN = 0 · Config = 0 · Secret disclosure = 0  

**Report path (canonical for this wave):**  
`X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-WEBGPT-HANDOFF-01.md`

**Evidence classes used throughout:** FACT · INFERENCE · HYPOTHESIS · UNPROVEN  

**Precedence used when reconciling conflicts:**  
1) later reproducible operational evidence → 2) later scoped acceptance evidence → 3) direct config/runtime evidence → 4) accepted programme docs → 5) older REPORT conclusions → 6) chat-derived claims without artifacts.

---

## 1. Executive verdict

**MARS Server Ops is a documentation-first, human-supervised external-infrastructure programme — not an autonomous agent, not a VPS control plane, and not a shipped runtime product.**

As of the strongest in-repo + local evidence dated **2026-08-27 … 2026-08-29**:

| Contour | Current canonical reading |
|---------|---------------------------|
| **Programme maturity** | Documented procedures + chartered human-invoked waves; **no** autonomous scheduler/orchestrator |
| **Control VPN node** | **MCA-VPN-001 / VEESP** (`wsp-cloud.com` / `178.173.250.69`) — operator working path; **do not mutate** without separate charter |
| **Second VPN node** | **EQVPS Micro-IP** (`metacode-cloud.com` / `95.216.126.173`) — production **candidate** ingress = **VLESS + TLS + RAW/tcp :8443**; XHTTP :443 **deferred**; Reality **withdrawn** as production |
| **AdminVPS Server B** | Provisioned host health **PASS**; **current assigned IP REJECTED** for direct Goodline entry; app stack **ABSENT**; **superseded as DNS/ingress target** by EQVPS for `metacode-cloud.com` |
| **FriendHosting** | **NOT EVIDENCED** in MARS Git programme tree or `X:\AI MARS STORAGE\mars-server-ops\` (folder absent) — treat external chat numbers as **UNVERIFIED** |
| **EQVPS real-app acceptance via v2rayN TUN** | **NOT PROVEN** as production PASS; isolated Xray full-transfer **PASS**; remaining hang class classified as **v2rayN/TUN-path-specific** (INFERENCE, not root cause) |
| **24443 Cursor PASS** | **NOT recorded** as accepted PASS in MARS evidence; latest Git-safe report = **READY_FOR_OPERATOR_TEST** / wait for operator A/B |
| **OPERATIONAL-INDEX.md** | **STALE** relative to EQVPS waves (still AdminVPS-centric; claims no Phase 4A/3X-UI) |
| **Git tracking** | Entire `projects/mars-server-ops/` appears **untracked** vs HEAD in this session (`git ls-files` empty; `??` status) — programme exists on disk; remote/canonical commit state of this tree is **SAFE UNKNOWN / operator must verify** |

**Bottom line for the new Web-GPT owner:** reconstruct current truth from **EQVPS asset reports (Aug 27–29) + MCA-VPN-001 live passport (Aug 25) + AdminVPS Phase 3E3 closure**, and treat **programme OPERATIONAL-INDEX + SERVER-INVENTORY rows as partially stale**. Do **not** diagnose/fix EQVPS yet. Do **not** purchase/configure FriendHosting from this report alone. Next step is operator-authorized **FULL SERVER OPS / EQVPS AUDIT** after Web-GPT builds its own current-state model.

---

## 2. Scope and method

### In scope
- Reconstruct programme identity, governance, inventory, VEESP/EQVPS/AdminVPS chronology, acceptance matrix, hypotheses, backups, contradictions.
- Inspect local EQVPS contour **metadata only** (directory names, report pointers). No secret values.

### Out of scope / not performed
- EQVPS root-cause fix
- Server / VPN / DNS / firewall mutation
- FriendHosting purchase
- Live SSH “health check” of production (default: repo/local evidence first)
- Git commit/push/stage
- Foreign WIP (large unrelated modified tree under Website Factory / WPilot / iSEO / etc.)

### Method
1. Confirm workspace / volume / branch (preflight).  
2. Read programme entry + foundation docs.  
3. Read all Git-safe EQVPS markdown under `assets/EQVPS-MICRO-IP\` (23 files).  
4. Read MCA-VPN-001 + SERVER-B-PLANNING key artifacts.  
5. List local EQVPS infrastructure contour (names only).  
6. Narrow Storage check for `mars-server-ops` / FriendHosting.  
7. Synthesize with explicit contradiction / stale / superseded / unverified sections.

**LIVE VERIFICATION NOT PERFORMED — REQUIRES SEPARATE OPERATOR-AUTHORIZED AUDIT** for: live VEESP inbound transport class (WS vs RAW), live EQVPS panel state after last wave, FriendHosting Looking Glass, sustained Cursor Agent sessions.

---

## 3. Sources inspected

### Programme entry / foundation (absolute paths)
- `X:\AI MARS\projects\mars-server-ops\OPERATIONAL-INDEX.md`
- `X:\AI MARS\projects\mars-server-ops\SERVER-OPS-CHARTER-v1.md`
- `X:\AI MARS\projects\mars-server-ops\SERVER-INVENTORY-v1.md`
- `X:\AI MARS\projects\mars-server-ops\ACCESS-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\SECRET-HANDLING-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\BACKUP-RESTORE-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\CHANGE-RISK-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\STORAGE-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\SERVICE-MAP-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROVIDER-SELECTION-RUNBOOK-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROCUREMENT-GATE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PASSPORT-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROVIDER-RESEARCH-SCORECARD-v1.md`

### MCA-VPN-001 / VEESP
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\` (passport, live intake, reconciliation, topology, backups, incidents, legacy handoff, etc.)

### AdminVPS / Server B planning
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\` (README, architecture freeze, preflight, 3E final verdict, AdminVPS support case, etc.)

### EQVPS Micro-IP (all 23 Git-safe reports)
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\` — full set dated 2026-08-27 … 2026-08-29 (listed in §29).

### Local EQVPS contour (metadata listing only)
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\` — directories: `backups\`, `ssh\`, `clients\`, multiple `*-raw-YYYY-MM-DD\` evidence bundles; files `secrets.local.md`, `operator-access.local.md` (**secret-bearing — values not read into this report**).

### Storage
- `X:\AI MARS STORAGE\` exists.  
- `X:\AI MARS STORAGE\mars-server-ops\` — **ABSENT**.  
- Narrow scan of `incoming\` / `backups\` / `exports\` / `documentation\` / `ARCHIVE\` for FriendHosting/EQVPS labels: **no FriendHosting evidence recovered** in this task.

### Repo root
- `X:\AI MARS\OPERATIONAL-INDEX.md` — **ABSENT** (programme entry is under `projects\mars-server-ops\`).  
- `X:\AI MARS\AGENTS.md` / `.cursorrules` — authority for X-drive / honesty / git discipline (session context).

### Not used as authority
- External chat handoff numbers (FriendHosting preflight timings, “24443 Cursor PASS then invalidated”) unless independently evidenced in MARS.

---

## 4. Programme architecture

### What MARS Server Ops is (FACT)
Canonical name: **MARS Server Ops & VPS Forge**.  
Working folder: `X:\AI MARS\projects\mars-server-ops\`.  
Lane framing in programme index: **B — External Infrastructure (Human-Supervised)**.

Purpose (documented): human-supervised documentation, schemas, runbooks, and controlled procedures for external server infrastructure (VPS, Linux, VPN/3X-UI/Xray, Docker, n8n host, databases, reverse proxy, backups).

Mandatory formulation from programme index:

```text
Git documents and governs procedure.
External servers execute outside Git.
No live server is owned by the repository.
```

### Exact programme scope (FACT)
**In scope when chartered:** sanitized inventory/passports; VPN docs/runbooks; Docker/host procedures; n8n host-level docs; DB backup/migration docs; reverse proxy/TLS procedures; backup/restore manifests; health check runbooks; implementation charters + REPORT evidence.

**Explicit exclusions:** autonomous orchestrator; SSH automation fleet; VPS hosting product; Kubernetes; secret-manager product; autonomous monitoring; local Windows/Laragon (MLI); EAR as admin automation; default site-specific CMS ops.

### Current entry point (FACT)
Primary: `X:\AI MARS\projects\mars-server-ops\OPERATIONAL-INDEX.md`  
Charter: `...\SERVER-OPS-CHARTER-v1.md`  
**Caution:** that index’s “current active phase” narrative is **STALE** vs EQVPS evidence (§22–23).

### Execution model (FACT)
`Web-GPT → Cursor/Codex → Human approval`  
No standing agent production credentials. Read-only default for external surfaces. Every external mutation needs an exact charter (server, service, change, risk, backup, validation, rollback, named approval).

### Registry / ATLAS (FACT)
Programme states registry row **NONE** / ATLAS binding **NONE** in Phase 0/1A decisions. Asset refs like `MCA-VPN-001` are programme-managed labels, not ATLAS IDs.

---

## 5. Server Ops Agent maturity

| Layer | Status | Evidence |
|-------|--------|----------|
| **Documented architecture** | **EXISTS** | Charter, models, provider selection Stages 0–11, runbooks |
| **Implemented tooling** | **PARTIAL / human-invoked** | PowerShell preflight scripts under SERVER-B-PLANNING; local SSH keys; remote wave scripts referenced in EQVPS raw evidence dirs — **not** a productized agent |
| **Human-invoked operational capability** | **DEMONSTRATED** | Multiple chartered EQVPS and Server B waves with REPORT + backup + rollback text |
| **Experimental capability** | **PRESENT** | EQVPS XHTTP research; RAW 24443 A/B inbound |
| **Planned capability** | **DOCUMENTED / DEFERRED** | Phase 4A+ originally deferred behind AdminVPS direct path; many “future phase” docs listed in index still not created as named artifacts |
| **Autonomous scheduler / orchestrator** | **NOT IMPLEMENTED** | Explicit non-scope in charter/index |
| **Monitoring product** | **NOT IMPLEMENTED** | fail2ban-only style notes; no fleet monitoring |
| **Evidence ingestion automation** | **NOT a product** | Human REPORT files + local raw directories |

**Do not describe Server Ops Agent / VPS Forge as autonomous.** Closest real maturity: **chartered Cursor/Codex execution under operator approval**, with secrets local-only.

---

## 6. Current server inventory

### A. MCA-VPN-001 — VEESP control node (active production VPN)

| Field | Value | Class |
|-------|-------|-------|
| Identifier | `MCA-VPN-001` / Server A | FACT |
| Provider | VEESP (legacy/live label; panel **NOT CHECKED** at intake) | FACT |
| Location | Amsterdam / NL — **chat claim**; Git passport `region` SAFE UNKNOWN; research backlog mentions NL/FI | UNPROVEN for Amsterdam as live DC |
| Public IPv4 | `178.173.250.69` | FACT in later EQVPS comparison docs; Git passport redacts as `<SERVER_IP>` |
| Domain | `wsp-cloud.com` | FACT |
| OS | Ubuntu 22.04.5 LTS | FACT (live 2026-08-25) |
| Role | Production dedicated VPN (HIGH criticality) | FACT |
| Environment | prod / active | FACT |
| Panel | 3X-UI HTTPS `:5928` | FACT |
| Xray | **26.6.22** at 2026-08-25 intake | FACT |
| Inbounds (intake) | `:8443` VLESS+TLS+**WebSocket** (`MCA-Gate-TLS`); `:46489` VLESS+Reality | FACT (2026-08-25) |
| Later client runtime claim | Operator active profile RAW/TLS `:8443` (`MCA-Gate-TLS-MCA-ONE`) | FACT as **client runtime capture** 2026-08-28/29; may conflict with Aug 25 server intake — see §22 |
| nginx | Not installed / not in path | FACT |
| SSH | root+password enabled (security risk) | FACT |
| ufw | inactive | FACT |
| Backup | Application archives present; full DR **NOT TESTED** | FACT |
| Acceptance | Operator treats as working control for ChatGPT/YouTube/Google/TUN (stated in EQVPS RAW control report) | FACT as operator-working-path claim in EQVPS docs; not a fresh acceptance matrix in this handoff |

Sources:  
`...\assets\MCA-VPN-001\SERVER-A-CURRENT-PASSPORT-v1.md`  
`...\assets\MCA-VPN-001\LIVE-INTAKE-EVIDENCE-v1.md`  
`...\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-veesp-style-raw-8443-control-deployment-2026-08-29.md`

### B. EQVPS Micro-IP — second VPN node (production candidate)

| Field | Value | Class |
|-------|-------|-------|
| Identifier | EQVPS-MICRO-IP (final MCA inventory_ref **not** assigned in SERVER-INVENTORY) | FACT |
| Provider | EQVPS Micro-IP | FACT |
| Underlying network | Path/DNS consistent with **Hetzner Helsinki**; ownership **not** claimed as corporate fact | FACT (observed) / UNPROVEN (ownership) |
| ASN | AS24940 — **external claim**; not strongly labeled in EQVPS md corpus searched | UNPROVEN in programme markdown |
| Location | Helsinki | FACT (path/evidence) |
| Public IPv4 | `95.216.126.173` | FACT |
| Domain | `metacode-cloud.com` | FACT |
| OS | Ubuntu 24.04.4 LTS | FACT |
| Stack | 3X-UI **v3.7.0**; Xray **26.7.28** | FACT |
| Role | Secondary VPN / AI-workstation path candidate | FACT |
| Current production candidate transport | VLESS + TLS + **RAW/tcp :8443**; SNI `metacode-cloud.com`; ALPN `http/1.1`; flow empty; mux disabled | FACT (operator runbook 2026-08-29) |
| Deferred | XHTTP :443 (technical client only) | FACT |
| Withdrawn | Reality production ingress | FACT |
| Panel / sub | Public HTTPS `:20901` / `:2096` (paths secret-local) | FACT |
| A/B inbound | RAW/TLS `:24443` provisioned; operator app A/B **pending** in last report | FACT |
| Backup | Multiple dated tarballs + SHA256 in reports; restore runbook exists but partially stale | FACT |
| Real-app acceptance | Isolated full-transfer PASS; v2rayN TUN real-app **not** proven PASS | FACT / UNPROVEN |

### C. AdminVPS Server B (provisioned; direct path rejected; app absent)

| Field | Value | Class |
|-------|-------|-------|
| Identifier | `SERVER-B-PLANNING` (temporary; final ID pending) | FACT |
| Provider | AdminVPS | FACT |
| Location | Finland / Helsinki (preferred FI1) | FACT |
| Hostname intent | historically `metacode-cloud.com` | FACT (planning) — **domain later bound to EQVPS** |
| IP | redacted `<SERVER_B_IP>` in Git | FACT |
| OS | Ubuntu 24.04 LTS | FACT |
| SSH | `marsops` KEY-ONLY :22 | FACT |
| UFW/fail2ban | ACTIVE | FACT |
| Direct TUN-OFF | ping/22/443 **FAILED** | FACT |
| VPN-mediated SSH | WORKS | FACT |
| 3X-UI/Xray | **ABSENT** | FACT |
| Verdict | Current IP **REJECTED** for direct entry; provider **NOT REJECTED** | FACT |
| Status vs EQVPS | **Superseded as active second-node build path** for domain/ingress; host may still exist | INFERENCE from chronology |

### D. FriendHosting (candidate control node)

| Field | Value | Class |
|-------|-------|-------|
| Existence in MARS evidence | **Not found** in programme tree; Storage programme root absent | FACT (absence) |
| Looking Glass `194.5.62.19` / Telehouse Frankfurt preflight numbers | External handoff only | **UNVERIFIED** |
| Purchase / provision state | Unknown | **UNKNOWN** |

---

## 7. VEESP / MCA-VPN-001 canonical state

### Canonical identity (FACT)
- Asset: MCA-VPN-001  
- Domain: `wsp-cloud.com`  
- IP (later docs): `178.173.250.69`  
- OS: Ubuntu 22.04.5 LTS  
- Role: **CONTROL** production VPN — leave untouched unless separate charter  

### Configuration history (synthesized)
1. **Legacy era:** WS + TLS + nginx architecture documented in legacy handoff (`...\legacy\WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md`).  
2. **Live intake 2026-08-25:** nginx **absent**; VLESS TLS+**WebSocket** on `:8443`; Reality on `:46489`; Xray **26.6.22**; panel `:5928`.  
3. **Operator working profile (EQVPS waves 2026-08-28/29):** v2rayN active outbound described as VLESS + TLS + **RAW/tcp** `:8443` to `wsp-cloud.com`, ALPN `http/1.1`, used as control for ChatGPT/YouTube/Google.

### CONTRADICTION (HIGH importance)
Aug 25 **server** intake says **WebSocket** on `:8443`.  
Aug 28–29 **client/control** evidence says **RAW**.  

**Canonical interpretation for handoff:**  
- Treat VEESP as **operator-working control path**.  
- Treat exact current **server-side** transport class as **REQUIRES LIVE READ-ONLY RECONCILE** (not assumed from chat).  
- Do **not** mutate VEESP to “fix” the contradiction without charter.

### Application acceptance (as claimed in EQVPS RAW control report)
Stated working under VEESP TUN: Cursor/ChatGPT/YouTube/browser/normal web — used as **control baseline**, not re-proven in this handoff wave. Classify as **operator-attested working path** pending fresh matrix if audit requires.

### Backup / restore
- Application backups present under server `/root/MCA/backups/...` (paths in BACKUP-STATE / passport).  
- Targeted panel recovery historically proven; **full DR NOT TESTED**.  
- Classification: **BACKUP EXISTS / RESTORE UNVERIFIED** for full-host; partial restore strategy documented historically.

---

## 8. Provider-selection history

### Why a second server was needed (FACT)
Single production VPN failure domain on MCA-VPN-001. Server B planned as **independent** secondary VPN (no shared DB/keys/certs/control plane). Manual client profile switching — not automatic failover. Server A must remain untouched during B construction.

### Goals / constraints (FACT from selection docs)
- AI-workstation path: Cursor / ChatGPT / related providers (time-sensitive).  
- Provider separation / independent path from Server A.  
- Goodline **direct** preflight doctrine (TUN OFF) before trusting an IP for VPN entry.  
- Location research historically included Finland / Netherlands (and others in clone baseline).  
- Netherlands not universally forbidden; Server A historically associated with NL research; Server B preferred **Finland** after UpCloud/AdminVPS path.

### UpCloud (SUPERSEDED)
Technically attractive FI-HEL1 path documented then **SUPERSEDED** due to customer eligibility/compliance conflict — no identity/residency/payment bypass.  
Evidence: `...\SERVER-B-PLANNING\PROCUREMENT-DECISION-v1.md` (historical).

### AdminVPS (provisioned; direct IP rejected)
Selected as replacement; FI1 pre-purchase network **APPROVED**; provisioned; hardened; reboot PASS; **assigned IP direct path FAILED**; support case prepared for operator (agents must not auto-send).

### EQVPS (selected as working second-node build)
After AdminVPS direct-entry rejection, EQVPS Micro-IP became the executed second-node contour with DNS `metacode-cloud.com`, full 3X-UI/Xray stack, and ongoing acceptance work.

### FriendHosting (external candidate)
Intended (per external handoff) as near-equivalent control experiment in Frankfurt/Telehouse. **No MARS artifact found** proving preflight numbers or order state in this investigation.

---

## 9. AdminVPS chronology

| When | Event | Verdict |
|------|-------|---------|
| Pre-purchase | FI1 network tests from operator path | **PASS / APPROVED** |
| Procurement | AdminVPS Finland provisioned | **PROVISIONED** |
| Phase 3B | Read-only provisioning intake | PASS WITH RESIDUALS |
| Phase 3C | Secure SSH bootstrap (`marsops` Ed25519) | PASS WITH RESIDUALS |
| Phase 3D | Base OS security + UFW + fail2ban | PASS WITH RESIDUALS |
| Phase 3E | Controlled reboot | PASS |
| Phase 3E direct gate | TUN-OFF ping/22/443 | **FAILED** |
| Phase 3E2 | Temporary SSH/443 forensic | Deployed then removed |
| Phase 3E3 (2026-08-26) | Final network verdict + support pack | Current IP **REJECTED**; host health **PASS**; provider **NOT REJECTED** |
| Post-EQVPS | Domain `metacode-cloud.com` used by EQVPS | AdminVPS no longer DNS/ingress authority for that domain |

**Lessons (FACT):**  
- Pre-purchase Looking Glass / test IP ≠ post-provision assigned IP path.  
- VPN-on tests can falsely PASS reachability; **TUN-OFF Goodline direct gate is mandatory**.  
- Temporary diagnostic ports must be removed (done in 3E3).  
- Do not install Phase 4A / 3X-UI on AdminVPS until direct path ACCEPTED (programme rule at time of 3E3).  

**Current status:** unresolved routing/IP case with provider; **deferred/superseded as active VPN build** relative to EQVPS work — host may still be alive (LIVE VERIFY if needed).

---

## 10. EQVPS full chronology

Ordered from evidence (do not collapse):

1. **2026-08-27 — Read-only intake** — fresh Ubuntu host; SSH :22 only; no VPN stack; traceroute shows Hetzner HEL path. Verdict `READY_WITH_RESIDUALS`.  
2. **2026-08-27 — SSH bootstrap** — `marsops` key/sudo; harden SSH; `PASS_WITH_RESIDUALS`.  
3. **2026-08-27 — Base OS security** — UFW 22 only; fail2ban; app ports closed.  
4. **2026-08-27 — Controlled reboot + direct port gate** — temporary listeners prove Goodline TUN-OFF TCP 22/443/8443 **PASS**; temps removed.  
5. **2026-08-27 — DNS + architecture** — `metacode-cloud.com` A bound to EQVPS; plan Reality :443 + XHTTP :8443.  
6. **2026-08-27 — Ingress charter** — charter only initially; then executed.  
7. **2026-08-27 — Ingress deployment** — 3X-UI 3.7.0 + Xray 26.7.28; Reality :443 + XHTTP :8443; Reality **server PASS / Goodline FAIL**; XHTTP :8443 usable. `PASS_WITH_RESIDUALS`.  
8. **2026-08-28 — Goodline stabilization** — Reality withdrawn; :443 migrated to XHTTP; dual XHTTP 443+8443. Verdict `XHTTP_443_PRIMARY_PASS`.  
9. **2026-08-28 — Current ingress baseline** — documents “PRODUCTION STABLE” XHTTP dual path (**later superseded**).  
10. **2026-08-28 — Client provisioning** — six devices on XHTTP primary/fallback.  
11. **2026-08-28 — Public panel/subscription** — panel 20901 + sub 2096 public HTTPS; fix localhost subscription emission.  
12. **2026-08-28 — XHTTP client forensics** — padding / import hypotheses; later weakened.  
13. **2026-08-28 — v2rayN runtime JSON diff** — live runtime was **VEESP**, not EQVPS XHTTP.  
14. **2026-08-28 — Custom config / Custom v2 / live truth / v1-v2 root cause / v2.1** — DNS bootstrap deadlock from copying VEESP `wsp-cloud.com` DNS exemption; v2.1 local fix; browser/TUN still UNPROVEN.  
15. **2026-08-29 — VEESP-style RAW :8443** — :8443 XHTTP → RAW/TLS; isolated local PASS; operator acceptance pending.  
16. **2026-08-29 — RAW full-transfer + client cleanup** — full-body YouTube/ChatGPT/CF 1MB/10MB PASS on isolated proxy; fleet cleaned to six RAW clients + one XHTTP test client.  
17. **2026-08-29 — RAW :24443 A/B** — clone inbound; isolated PASS; TCP A/B no connect anomaly; **operator Cursor/Firefox A/B still WAITING** in report.  
18. **Operator runbook updated** — production candidate = RAW :8443; XHTTP deferred; Reality not production.

---

## 11. EQVPS 443 / XHTTP history

| Phase | Architecture | Outcome |
|-------|--------------|---------|
| Initial plan | Reality primary on 443 | Selected |
| Deploy | Reality on 443 | Server OK; Goodline FAIL (`received real certificate`) |
| Stabilization | XHTTP on 443 primary | Goodline XHTTP PASS (at that time) |
| Client acceptance chase | Custom configs / padding / DNS | Multiple hypotheses; not durable production confidence |
| After RAW wave | XHTTP 443 preserved as **experimental/deferred**; production clients removed except technical test | Current |

**Why XHTTP attempted:** Reality unusable on required Goodline path; need TLS-based camouflage/path that worked on :8443 first.  
**TLS termination:** in Xray (LE cert for `metacode-cloud.com`), not nginx.  
**nginx:** not part of EQVPS ingress architecture in these waves.  
**Final classification:** **DEFERRED / NON-PRODUCTION** for fleet. Do not treat Aug 28 “PRODUCTION STABLE XHTTP” docs as current without reading Aug 29 RAW reports.

---

## 12. EQVPS 8443 RAW/TLS history

| Stage | State |
|-------|-------|
| Early | XHTTP fallback on 8443 (PASS for early browsing/egress) |
| 2026-08-29 control wave | Mutated to **RAW/tcp + TLS**; VEESP-style field match (port/ALPN/flow/mux/fingerprint pattern) |
| Validation | Server listeners/TLS OK; isolated Xray `:18088` ipify/Google/YouTube PASS |
| Full-transfer wave | YouTube full body, ChatGPT body, CF 1MB/10MB PASS |
| Operator v2rayN TUN | Remaining hang / real-app issues → classified **V2RAYN_TUN_PATH_SPECIFIC** (INFERENCE) |

**Separate explicitly:**

| Class | Status |
|-------|--------|
| **TRANSPORT HEALTH** (server + isolated Xray) | **PASS** (strong evidence 2026-08-29) |
| **REAL APPLICATION ACCEPTANCE** (v2rayN TUN / Cursor sustained / YouTube playback / ChatGPT prompt) | **NOT PROVEN as PASS** in Git-safe corpus; symptoms reported; next diagnostics proposed |

---

## 13. EQVPS 24443 A/B history

### Why created
Controlled port A/B to test whether application hangs are **port/path-specific** vs common EQVPS/client factors. Cloned RAW/TLS settings from 8443 onto **24443**.

### What MARS evidence shows (FACT)
- Server inbound `EQVPS-TLS-RAW-24443-AB` created; UFW allow added; backup with SHA256.  
- Isolated validation: egress EQVPS IP; YouTube body; CF 1MB/10MB **PASS**.  
- TCP connect A/B 25/25 both ports — **no connect anomaly**.  
- Report verdict: **`RAW_24443_AB_READY_FOR_OPERATOR_TEST`**.  
- Explicit: real Cursor/Firefox conclusion **requires operator manual A/B**.  
- **NEXT ACTION: WAIT FOR OPERATOR A/B RESULT**.

### About “8443 FAIL → 24443 PASS (Cursor)” then “invalidated”
**Not supported as recorded MARS verdicts.**  
- No Git-safe report elevates 24443 to **Cursor PASS**.  
- No later Git-safe report documents invalidation of such a PASS.  
Treat any such narrative as **chat-derived UNVERIFIED** unless operator supplies dated evidence into MARS.

**If** an operator later observed a false PASS, mark that observation as **SUPERSEDED** only when dated evidence exists. As of this handoff: **UNVERIFIED claim**, not a proven superseded verdict.

---

## 14. EQVPS acceptance matrix

Legend: PASS / FAIL / UNSTABLE / NOT TESTED / UNKNOWN  
Sources: primarily 2026-08-29 RAW full-transfer + 24443 + RAW control + operator runbook notes.

| Test | Isolated Xray | v2rayN explicit `:10808` | v2rayN TUN | Notes |
|------|---------------|--------------------------|------------|-------|
| api.ipify → 95.216.126.173 | PASS | NOT TESTED (proposed next) | UNKNOWN / symptom history | Isolated PASS post-cleanup |
| Basic HTTPS (Google) | PASS | NOT TESTED | UNKNOWN | |
| Repeated HTTPS | PARTIAL (transfer series) | NOT TESTED | UNKNOWN | |
| Cloudflare 1 MB | PASS | NOT TESTED | UNKNOWN | |
| Cloudflare 10 MB | PASS | NOT TESTED | UNKNOWN | |
| YouTube HTTP full body | PASS | NOT TESTED | UNKNOWN | |
| YouTube browser homepage | NOT TESTED (isolated curl body only) | UNKNOWN | UNSTABLE/FAIL reports historically | |
| YouTube video playback | NOT TESTED | NOT TESTED | UNKNOWN / hang reports | |
| ChatGPT homepage | PASS body (403 challenge OK as transfer) | NOT TESTED | UNKNOWN / hang reports | |
| ChatGPT login | NOT TESTED | NOT TESTED | UNKNOWN | |
| ChatGPT actual prompt | NOT TESTED | NOT TESTED | UNKNOWN | |
| Facebook control | NOT TESTED | NOT TESTED | NOT TESTED | |
| Cursor basic request | NOT TESTED in provisioning reports | NOT TESTED | UNKNOWN | 24443 report waits for operator |
| Cursor sustained Agent | NOT TESTED | NOT TESTED | UNKNOWN | |
| Telegram | NOT TESTED | NOT TESTED | NOT TESTED | |
| Reality Goodline client | — | — | FAIL (2026-08-27/28) | Withdrawn |
| XHTTP early Goodline browsing | PASS (historical) | — | — | Superseded as production path |

**Rule reinforced in programme evidence:** small HEAD/latency checks are **insufficient**; `.ru` may go **direct** via Goodline and must not prove VPN egress.

---

## 15. Windows / v2rayN client model

### Evidenced elements (FACT)
- Windows operator workstation; v2rayN **7.22.3 x64**  
- Bundled/used Xray **26.7.28** (also earlier probe with 26.5.9 in one forensic)  
- TUN / Wintun present in VEESP sessions  
- Mixed/explicit proxy commonly `127.0.0.1:10808`  
- Isolated probes used alternate local ports (`18088`, `18089`) without mutating v2rayN DB  

### Routing / DNS lessons (FACT)
- Custom v2 copied VEESP routing/DNS shell but left `wsp-cloud.com` DNS exemption → `metacode-cloud.com` DNS via proxy → bootstrap deadlock.  
- `.ru` / geoip:ru / private → direct; UDP/443 block; catch-all → proxy — described as VEESP working shell pattern in differential analysis.  
- **`.ru` direct through Goodline ≠ VPN egress proof.**

### Experiments documented
- System Proxy / TUN / Custom Config / subscription import / HTTP compatibility notes / MTU read-only (Ethernet 1500; DF probes no blackhole) / HTTP2 curl skip (Windows curl lacks `--http2` in that wave).

---

## 16. Hypothesis register

| Hypothesis | Why considered | For | Against | Status |
|------------|----------------|-----|---------|--------|
| Closed/not-listening port | classic | early unknowns | direct port gates PASS | **REJECTED** for 22/443/8443 reachability |
| Invalid TLS cert | classic | — | LE verify return 0; CN match | **REJECTED** for current RAW |
| Wrong SNI | classic | — | SNI matches domain in validated waves | **WEAK / largely REJECTED** for current RAW |
| Wrong ALPN | VEESP match work | — | ALPN http/1.1 matched deliberately | **WEAK** |
| Insufficient bandwidth | hang | — | CF 10MB ~MB/s isolated PASS | **REJECTED** as primary |
| MTU / PMTU blackhole | hang | — | DF probes ~1500; transfers complete | **REJECTED** as blackhole; residual loss counters noted |
| TUN globally broken | client hangs | VEESP TUN works as control | VEESP works | **REJECTED** as global |
| Firefox/Vivaldi-only | browser variance | — | insufficient comparative matrix | **UNPROVEN / WEAK** |
| Browser cache / stale sockets | UX | — | weak evidence | **WEAK** |
| HTTP/2-only Cursor issue | Cursor hangs | — | curl HTTP2 skipped; unproven | **UNPROVEN / WEAK** |
| DNS failure / bootstrap deadlock | Custom v2 fail | strong differential evidence | fixed in v2.1 locally; doesn’t explain all RAW TUN hangs | **STILL PLAUSIBLE** for Custom-shell class; **not sole root** for RAW |
| Xray 26.7.28 regression | version chase | — | isolated 26.7.28 PASS | **WEAK / REJECTED** as sole |
| v2rayN 7.22.3 regression | client | wrong-profile / serialization issues documented | VEESP works on same client | **STILL PLAUSIBLE** for EQVPS profile path |
| RAW/TLS regression | transport | — | isolated RAW PASS | **REJECTED** as server transport stall |
| Provider/ASN/IP issue | EQVPS/Hetzner | path retrans under load; Helsinki path | isolated transfers PASS; no proven block | **STILL PLAUSIBLE** |
| Goodline↔Hetzner path issue | ISP path | Reality MITM-class fail; AdminVPS direct fail history | EQVPS direct TCP PASS | **STILL PLAUSIBLE** for some apps |
| App/CDN-specific behaviour | Cursor/ChatGPT/YT | differential app symptoms | incomplete matrix | **LEADING HYPOTHESIS class (application-path)** — **UNPROVEN root** |
| Hetzner backbone incident causation | Aug 21–28 FRA–HEL notes | chronological overlap | no active incident at 24443 provision; no proven causal chain | **UNPROVEN causation** (incident existence partially FACT from report’s research notes) |
| v2rayN TUN/routing/DNS/split-tunnel specific | after full-transfer PASS | programme inference 2026-08-29 | not mechanistically proven | **LEADING HYPOTHESIS** |

**ROOT CAUSE:** **NOT PROVEN.**

---

## 17. Hetzner incident relevance

From `EQVPS-MICRO-IP-RAW-24443-port-ab-2026-08-29.md` provider research table:

| Item | Classification |
|------|----------------|
| NBG1–FRA maintenance completed 2026-08-28 12:07 UTC | FACT (as recorded research note) |
| FRA–HEL backbone fault started 2026-08-21; last update 2026-08-23; not reoccurred over weekend per Hetzner | FACT (as recorded research note) |
| Active incident affecting EQVPS TCP ingress on 2026-08-29 | None identified |
| Causation of EQVPS app hangs | **UNPROVEN** |
| Explains 8443 vs 24443 difference | **No** (TCP A/B identical success) |

Primary sources for this claim live in that report + its local evidence bundle; original Hetzner status page captures were **not separately inventoried** in Git-safe tree during this handoff.

---

## 18. FriendHosting preflight evidence

**Verdict:** **NOT FOUND IN MARS EVIDENCE BASE (this investigation).**

Checked:
- All `projects\mars-server-ops\` markdown (no FriendHosting / 194.5.62.19 / Telehouse hits of substance).  
- `X:\AI MARS STORAGE\mars-server-ops\` absent.  
- Narrow Storage name scan — no FriendHosting artifacts recovered.

Therefore external numbers (20/20 ping, 0% loss, 82–91 ms, 25/25 TCP/443, 50MB/100MB timings) remain **UNVERIFIED claims** until operator files evidence under Server Ops assets/Storage.

**Current FriendHosting state from MARS:** **UNKNOWN** (not proven planned/ordered/provisioned).

---

## 19. FriendHosting control experiment plan

**Status in MARS:** **NOT DOCUMENTED as an approved charter artifact** found in this pass.

External intended logic (preserve as **experiment logic only**, not predetermined truth):

- Near-equivalent stack: Ubuntu 24.04, 3X-UI 3.7.0, Xray 26.7.28, VLESS+TLS+RAW, ports 8443/24443.  
- Keep Windows client stack constant.  
- Real acceptance: Cursor sustained Agent, YouTube homepage+playback, ChatGPT login+prompt, Facebook control, curl/10MB.  
- **PASS on FriendHosting** → increases confidence in EQVPS/Hetzner/IP/path domain.  
- **Same failure** → weakens provider-specific hypothesis; shift to client/app/common-path factors.

Do **not** execute without operator charter + Goodline TUN-OFF preflight gate + backup/restore plan.

---

## 20. Backup / restore / rollback inventory

### Programme doctrine (FACT)
> A backup is not operationally complete until a restore strategy exists.

Source: `X:\AI MARS\projects\mars-server-ops\BACKUP-RESTORE-MODEL-v1.md`

### EQVPS anchors (safe structural)

| Anchor | Path (local) | Restore strategy | Class |
|--------|--------------|------------------|-------|
| postinstall ingress | `...\EQVPS-MICRO-IP\backups\eqvps-ingress-postinstall-20260827T175740Z.tgz` | restore runbook | BACKUP + RESTORE STRATEGY DOCUMENTED / restore test UNKNOWN |
| goodline pre/post XHTTP443 | `...\backups\eqvps-ingress-goodline-*.tgz` | restore runbook | same |
| client provision pre/post | `...\backups\eqvps-clients-*.tgz` | restore runbook | same |
| public access pre/post | `...\backups\eqvps-public-access-*.tgz` | restore runbook | same |
| pre RAW 8443 | `...\backups\eqvps-pre-raw-8443-20260828T180336Z\` (+ sha256 in report) | yes (rollback to XHTTP 8443) | BACKUP + RESTORE STRATEGY CONFIRMED (text); restore drill UNKNOWN |
| post-raw pre-cleanup DB | `...\backups\post-raw-pre-client-cleanup-2026-08-29\x-ui.db` | yes | BACKUP + RESTORE STRATEGY CONFIRMED (text) |
| pre RAW 24443 | `...\backups\eqvps-pre-raw-24443-ab-20260828T203556Z.tgz` (+ sha256) | yes (remove 24443 / restore DB) | BACKUP + RESTORE STRATEGY CONFIRMED (text) |

Restore runbook:  
`X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`  
**STALE WARNING:** runbook baseline text still oriented to earlier XHTTP dual production — use with Aug 29 RAW reports.

### VEESP / MCA-VPN-001
Application backups present; full DR **NOT TESTED** → **BACKUP EXISTS / RESTORE UNVERIFIED**.

### AdminVPS
Provider weekly copy claimed SAFE UNKNOWN; no VPN app backups (stack absent).

### Secret-bearing
Local backups/clients/ssh/secrets may contain secrets — **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]**.

---

## 21. Constraints and safety boundaries

- X-drive only for MARS writes; canonical roots: `X:\AI MARS`, `X:\AI MARS STORAGE`, `X:\MARS-Localhost`.  
- Secrets: local + Storage only; never Git; never print.  
- External mutation: charter + approval + backup + validation + rollback.  
- VEESP = control — default **no touch**.  
- AdminVPS support tickets: operator-only send.  
- `.ru` direct ≠ VPN proof.  
- curl PASS ≠ application acceptance.  
- Single Cursor reply ≠ sustained Agent PASS.  
- Foreign WIP in repo: **out of scope** (large unrelated modified set present).  
- This handoff performed **no** live SSH verification by default.

---

## 22. CONTRADICTIONS

| # | Older claim (A) | Source (B) | Later conflicting evidence (C) | Source (D) | Canonical interpretation (E) | Confidence (F) |
|---|-----------------|------------|--------------------------------|------------|------------------------------|----------------|
| 1 | Programme waiting AdminVPS route; no Phase 4A/3X-UI | `OPERATIONAL-INDEX.md` | EQVPS has full 3X-UI/Xray + public panel + RAW fleet | EQVPS Aug 27–29 reports | Index **STALE**; EQVPS is active second-node evidence | **HIGH** |
| 2 | Inventory Server B owns `metacode-cloud.com` intent; app absent | `SERVER-INVENTORY-v1.md` | Domain bound to EQVPS ingress | EQVPS DNS/ingress reports | Domain operationally on EQVPS; AdminVPS row outdated for domain/role | **HIGH** |
| 3 | XHTTP dual 443/8443 “PRODUCTION STABLE” | `EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md` | RAW 8443 production candidate; XHTTP deferred | runbook + RAW reports 2026-08-29 | Prefer Aug 29 runbook | **HIGH** |
| 4 | No public panel/subscription | current-ingress-baseline | Public 20901/2096 PASS wave | public-panel report | Public management plane is current | **HIGH** |
| 5 | Reality primary | architecture + charter | Reality withdrawn after Goodline FAIL | goodline stabilization | Reality not production | **HIGH** |
| 6 | VEESP :8443 = WebSocket | MCA passport 2026-08-25 | VEESP control described as RAW in EQVPS waves | RAW control + runtime JSON | **LIVE RECONCILE REQUIRED** | **MEDIUM** |
| 7 | Missing XHTTP padding = root cause | xhttp forensic | wrong active profile; DNS deadlock; later RAW path | runtime-diff; v1-v2; RAW reports | Padding not sole root; multi-hypothesis evolution | **HIGH** |
| 8 | Restore runbook “current production” XHTTP | ingress-restore-runbook | RAW production candidate | Aug 29 reports | Runbook procedure useful; baseline architecture stale | **HIGH** |
| 9 | External: 24443 Cursor PASS | chat | MARS: ready for operator test only | RAW-24443 report | No Cursor PASS recorded | **HIGH** (absence) |

---

## 23. STALE CONCLUSIONS

1. `OPERATIONAL-INDEX.md` “next action = AdminVPS support; no 3X-UI until direct PASS”.  
2. `SERVER-INVENTORY-v1.md` lacking EQVPS row / AdminVPS as primary Server B story.  
3. `EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md` as current architecture.  
4. XHTTP fleet as production device set (cleaned 2026-08-29).  
5. Ingress restore runbook’s implied current dual-XHTTP baseline.  
6. Any doc implying Reality is EQVPS production primary.  
7. Assumption that programme tree is already committed to `origin/mars/canonical-post-recovery` — **disk evidence exists; git tracking empty in this session**.

---

## 24. SUPERSEDED VERDICTS

| Verdict | Superseded by |
|---------|---------------|
| UpCloud procurement decision | AdminVPS decision v2 |
| Reality as EQVPS production primary | Goodline stabilization → XHTTP; later Reality remains withdrawn |
| XHTTP 8443 as production fallback | RAW 8443 control deployment |
| XHTTP as production fleet path | RAW full-transfer + client registry cleanup + operator runbook |
| “Copy VEESP routing shell identically” for EQVPS Custom v2 | v1–v2 differential root-cause (hostname DNS exemption) |
| AdminVPS as active DNS target for `metacode-cloud.com` | EQVPS DNS binding |

---

## 25. UNVERIFIED CLAIMS

1. FriendHosting Looking Glass metrics / purchase recommendation / Telehouse Frankfurt selection — **no MARS file**.  
2. FriendHosting ordered/provisioned.  
3. AS24940 as formal EQVPS ownership claim.  
4. VEESP datacenter = Amsterdam (chat); Git SAFE UNKNOWN.  
5. Full VEESP application acceptance matrix freshly re-run.  
6. Cursor PASS on EQVPS 24443 (and subsequent invalidation).  
7. Sustained Cursor Agent PASS on EQVPS RAW 8443.  
8. ChatGPT prompt PASS / YouTube playback PASS on EQVPS via v2rayN TUN.  
9. Hetzner backbone incident **caused** EQVPS failures.  
10. Exact current VEESP server inbound = RAW (vs Aug 25 WebSocket intake).  
11. Whether AdminVPS VPS still exists/paid.  
12. That `projects/mars-server-ops` is on remote canonical history (local tree currently untracked vs HEAD).

---

## 26. Canonical current facts

1. Server Ops is human-supervised documentation + chartered execution — **not autonomous**.  
2. VEESP/`wsp-cloud.com`/`178.173.250.69` is the operator **control** VPN path — do not mutate casually.  
3. EQVPS/`metacode-cloud.com`/`95.216.126.173` runs Ubuntu 24.04.4 + 3X-UI 3.7.0 + Xray 26.7.28.  
4. EQVPS production **candidate** ingress = VLESS+TLS+RAW :8443.  
5. EQVPS XHTTP :443 = deferred; Reality = not production.  
6. EQVPS RAW isolated full-transfer tests **PASS**.  
7. EQVPS real-app acceptance via v2rayN TUN is **not proven PASS**.  
8. RAW :24443 A/B inbound exists; operator app conclusion pending in last report.  
9. AdminVPS Server B host hardened but direct IP rejected; app stack absent.  
10. Secrets live under `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\` (and MCA-VPN-001 local) — not Git.  
11. Programme OPERATIONAL-INDEX is stale relative to EQVPS.  
12. No FriendHosting evidence located in MARS in this investigation.  
13. Backup doctrine requires restore strategy; several EQVPS tarballs have documented rollback text; full restore drills largely UNKNOWN.  
14. Foreign WIP elsewhere in repo is out of scope and must not be staged.

---

## 27. Open questions

1. Exact live VEESP `:8443` transport (WS vs RAW) — live read-only reconcile.  
2. True EQVPS root cause of app hangs — **unproven**.  
3. Operator results for RAW 8443 and 24443 Cursor/YouTube/ChatGPT A/B — missing or not filed.  
4. Whether `:10808` full-body curl matches isolated `:18088` (proposed next diagnostic).  
5. FriendHosting evidence location / whether experiment should be chartered.  
6. AdminVPS host lifecycle (keep/destroy/support).  
7. Update programme index + inventory to include EQVPS row and retire stale AdminVPS “current” narrative.  
8. Git commit strategy for currently untracked `projects/mars-server-ops/` tree (operator decision).  
9. Restore-test evidence for EQVPS backups.  
10. Whether Storage layout `X:\AI MARS STORAGE\mars-server-ops\` should be created per STORAGE-MODEL.

---

## 28. Recommended next Web-GPT actions

**Do not execute EQVPS “fix” waves from this handoff alone.**

Suggested sequence:

1. **Web-GPT reviews this handoff** end-to-end; mark disagreements explicitly.  
2. **Build Web-GPT’s own canonical current-state model** (short living note), prioritizing Aug 29 EQVPS runbook + RAW reports over OPERATIONAL-INDEX.  
3. **Identify questionable prior reasoning** (padding-as-root; any chat-only 24443 PASS; FriendHosting-as-fact; index-as-current).  
4. **No automatic mutations.**  
5. Operator later explicitly requests: **FULL SERVER OPS / EQVPS AUDIT**.  
6. Audit design targets (examples only):  
   - live read-only VEESP inbound reconcile;  
   - file any missing operator A/B results;  
   - `:10808` vs `:18088` full-transfer compare;  
   - Cursor sustained session protocol;  
   - decide AdminVPS disposition;  
   - if FriendHosting proceeds: charter + TUN-OFF preflight + near-equivalent stack experiment;  
   - refresh OPERATIONAL-INDEX + SERVER-INVENTORY;  
   - decide git commit wave for Server Ops tree.  

---

## 29. Evidence path index

### Programme
- `X:\AI MARS\projects\mars-server-ops\OPERATIONAL-INDEX.md`
- `X:\AI MARS\projects\mars-server-ops\SERVER-OPS-CHARTER-v1.md`
- `X:\AI MARS\projects\mars-server-ops\SERVER-INVENTORY-v1.md`
- `X:\AI MARS\projects\mars-server-ops\ACCESS-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\SECRET-HANDLING-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\BACKUP-RESTORE-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\CHANGE-RISK-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\STORAGE-MODEL-v1.md`
- `X:\AI MARS\projects\mars-server-ops\SERVICE-MAP-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROVIDER-SELECTION-RUNBOOK-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROCUREMENT-GATE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PASSPORT-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\VPS-PROVIDER-RESEARCH-SCORECARD-v1.md`
- `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-WEBGPT-HANDOFF-01.md` *(this file)*

### MCA-VPN-001
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\SERVER-A-CURRENT-PASSPORT-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\LIVE-INTAKE-EVIDENCE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\CURRENT-STATE-RECONCILIATION-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\NETWORK-TOPOLOGY-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\BACKUP-STATE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\RECOVERY-STATE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\INCIDENT-HISTORY-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\CLIENT-COMPATIBILITY-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\MCA-VPN-001\legacy\WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md`

### SERVER-B / AdminVPS
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\README.md`
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\ARCHITECTURE-FREEZE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-DIRECT-NETWORK-GATE-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\PROCUREMENT-DECISION-v1.md` *(superseded)*  
- plus sibling Phase 3B–3E2 docs in same folder

### EQVPS Git-safe reports
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-read-only-intake-2026-08-27.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-controlled-ssh-bootstrap-2026-08-27.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-base-os-security-firewall-2026-08-27.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-controlled-reboot-direct-port-gate-2026-08-27.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-dns-binding-ingress-architecture-2026-08-27.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-deployment-charter-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-deployment-2026-08-27.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-goodline-ingress-stabilization-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-production-client-provisioning-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-public-panel-subscription-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-xhttp-client-handshake-forensic-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-v2rayn-runtime-json-diff-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-v2rayn-custom-config-control-test-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-v2rayn-routing-template-custom-v2-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-v2rayn-custom-v2-live-runtime-truth-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-v2rayn-v1-v2-differential-root-cause-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-custom-v2-1-endpoint-bootstrap-fix-2026-08-28.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-veesp-style-raw-8443-control-deployment-2026-08-29.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-raw-full-transfer-and-client-registry-cleanup-2026-08-29.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-RAW-24443-port-ab-2026-08-29.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-operator-client-runbook-v1.md`
- `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`

### Local EQVPS contour (non-secret structure)
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\`
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\`
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-24443-ab-2026-08-29\`
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-8443-control-raw-2026-08-29\`
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-full-transfer-diagnostic-raw-2026-08-29\`
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\secrets.local.md` — **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]**
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\operator-access.local.md` — **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]**
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh\` — **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]**

### Storage
- `X:\AI MARS STORAGE\` (exists; programme subroot `mars-server-ops` **absent** at time of handoff)

---

## 30. Git / mutation closeout

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` on `X:` |
| Branch | `mars/canonical-post-recovery` |
| This report created | YES — untracked until operator commits |
| `projects/mars-server-ops` vs HEAD | Appears **fully untracked** in this session |
| Foreign WIP | Present extensively outside Server Ops — **untouched** |
| Staged changes by this task | **NONE** |
| Commit | **NOT DONE** (not requested) |
| Push | **NOT DONE** |
| Server mutation | **0** |
| VPN / config mutation | **0** |
| Secret disclosure | **0** |
| Live remote verification | **NOT PERFORMED** (default) |

**Git mutation = 0 · Server mutation = 0 · Secret disclosure = 0**

---

*End of REPORT — MARS Server Ops Web-GPT Knowledge Handoff 01 · CURRENT TRUTH OVER HISTORICAL CONVENIENCE.*

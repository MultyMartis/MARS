# REPORT — MARS Server Ops EXP-A01b — Offline EQVPS Acceptance Capture

**Programme:** MARS Server Ops & VPS Forge  
**Experiment:** EXP-A01b (operator-guided offline A/B/A acceptance)  
**Analysis date (local):** 2026-08-29  
**Evidence session:** `X:\AI MARS\projects\mars-server-ops\evidence\EXP-A01b\2026-08-29_173912_live`  
**Mode:** POST-RUN ANALYSIS ONLY — no re-run, no server/client mutation, no FriendHosting provision, no Git commit/push  
**Evidence classes:** FACT · INFERENCE · HYPOTHESIS · UNPROVEN  

**Mutations in this analysis task:** Git = 0 · VEESP = 0 · EQVPS = 0 · Client config = 0 · Secret disclosure = 0  

---

## 1. Executive verdict

**EXP-A01b successfully reproduced the target differential:**

```text
VEESP PASS
  →
EQVPS TRANSPORT PASS / REAL APPLICATION FAIL
  →
VEESP PASS AGAIN
```

under a controlled Windows/v2rayN/TUN client environment where the **primary changed variable was the selected VPN endpoint/profile** (VEESP RAW `:8443` → EQVPS RAW `:8443` → VEESP RAW `:8443`).

| Layer | Result |
|-------|--------|
| VEESP baseline transport + Cursor/ChatGPT/YouTube | **PASS** |
| EQVPS transport (egress / HTTPS / repeat / ~10 MB) | **PASS** (pre- and post-app) |
| EQVPS Cursor / ChatGPT / YouTube / Facebook | **FAIL** |
| VEESP recovery transport + Cursor/ChatGPT/YouTube | **PASS** |
| A/B/A differential | **REPRODUCED** |
| Exact root cause | **UNPROVEN** |
| Experiment quality | **STRONG** |

**Primary principle (quantified, not overclaimed):** real-application failure **followed the EQVPS endpoint** and **disappeared when the VEESP control endpoint was restored**, while EQVPS basic transport remained healthy. This **STRONGLY WEAKENS** global Windows / v2rayN / Wintun / browser / Cursor / Goodline-outage theories, and **materially strengthens** the EQVPS endpoint / provider / path / application-interaction domain — **without proving** which sub-hypothesis inside that domain is causal.

---

## 2. Experiment validity

**Overall experimental-quality verdict: STRONG**

| Validity criterion | Assessment |
|--------------------|------------|
| Endpoint/profile as primary changed variable | **Met** (operator UI switch; harness `vpn_auto_switch=false`, `v2rayn_config_writes=0`) |
| Pre-control (VEESP baseline) | **Met** — transport + three real apps |
| Post-control (VEESP recovery) | **Met** — transport + three real apps + final internet OK |
| Transport measured independently of apps | **Met** — curl via `:10808` before apps; post-app transport recheck still PASS on EQVPS |
| Applications tested separately | **Met** — Cursor, ChatGPT, YouTube, Facebook as distinct operator records |
| Recovery reproduced | **Met** — egress returned to `178.173.250.69`; apps PASS again |
| Automated evidence + operator observations | **Met** — JSON/CSV/txt suite + `manual-acceptance.csv` |
| `COMPLETED.marker` | **Present** |
| Remaining uncontrolled variables | Present but **bounded** (see §5) — do not invalidate A/B/A |

**Limitations (do not downgrade below STRONG, but constrain causal claims):**

1. Real-app rows are **operator-attested**, not instrumented browser/Cursor telemetry.  
2. Facebook **not** tested on VEESP baseline/recovery.  
3. Live server differences remain (sniffing on/off; Xray 26.6.22 vs 26.7.28) — held constant during A01b, not equalized.  
4. Single time window (~11 minutes UTC).  
5. Client Xray access log extract = **NOT AVAILABLE**; v2rayN log extract = **PARTIAL / stale dated files**.  
6. Profile-specific client settings (DNS exemption hostname, SNI/host identity) necessarily change with endpoint — **expected** for this A/B, but not zero confounding.

**Not INVALID:** completion marker, egress IP transitions, transport suites, and recovery all cohere.

---

## 3. Session metadata

| Field | Value |
|-------|-------|
| Harness | EXP-A01b-1.0.0 |
| DryValidate | `false` |
| Session dir | `...\evidence\EXP-A01b\2026-08-29_173912_live` |
| SESSION_START (UTC) | 2026-08-29T10:39:12Z |
| SESSION_COMPLETED (UTC) | 2026-08-29T10:50:42Z |
| Completed local | 2026-08-29T17:50:42+07:00 |
| Status | `COMPLETED` |
| Admin required / used | `false` / `false` |
| VPN auto-switch | `false` |
| v2rayN config writes | `0` |
| Server mutations | `0` |
| Secret disclosure | `0` |
| Windows | 10.0.19045 (Pro caption in precheck) |
| Mixed proxy | `127.0.0.1:10808` listening, owned by `xray` |
| Port `:18088` | **not listening** (expected; no isolated probe) |
| TUN adapter | `xray_tun` Up, NlMtu **1500** |
| Default route preference | `xray_tun` present alongside Ethernet |

**Phase timestamps (UTC, from `session-events.csv`):**

| Event | UTC |
|-------|-----|
| VEESP baseline transport done | 10:39:42 |
| VEESP baseline apps recorded | 10:41:09 |
| EQVPS switch confirmed | 10:41:50 |
| EQVPS transport done | 10:41:56 |
| EQVPS apps (phase4) done | 10:47:01 |
| EQVPS post-app transport done | 10:47:05 |
| VEESP recovery switch confirmed | 10:47:44 |
| VEESP recovery transport done | 10:47:51 |
| VEESP recovery apps + final OK | 10:50:30–10:50:42 |

---

## 4. Evidence inspected

| Artifact | Role |
|----------|------|
| `COMPLETED.marker` | Full-completion gate (`COMPLETED`) |
| `session-summary.json` | Phase rollup + embedded A/B/A matrix |
| `session-events.csv` | Timestamped event log |
| `manual-acceptance.csv` | Operator Y/N answers + Cursor stop note |
| `precheck.json` | Client/OS/TUN/proxy precheck |
| `baseline-veesp.json` + `transport-veesp.txt` | VEESP transport suite |
| `eqvps.json` + `transport-eqvps.txt` | EQVPS transport suite |
| `eqvps-post-app.json` + `transport-eqvps-post-app.txt` | EQVPS transport after app FAILs |
| `recovery-veesp.json` + `transport-recovery.txt` | VEESP recovery transport |
| `process-snapshot.txt` | v2rayN/xray process IDs across phases |
| `v2rayn-log-extract.txt` | Bounded / **PARTIAL** (old guiLogs) |
| `xray-client-log-extract.txt` | **NOT AVAILABLE** |
| `README.md` | Harness purpose / secrets policy |

**Prior reports (context, not re-executed):**

- `...\reports\MARS-SERVER-OPS-WEBGPT-HANDOFF-01.md`  
- `...\reports\MARS-SERVER-OPS-EQVPS-AUDIT-01-EVIDENCE-ARCHITECTURE-RECONCILIATION.md`  
- `...\reports\MARS-SERVER-OPS-EXP-A01-LIVE-VEESP-EQVPS-RUNTIME-RECONCILIATION.md`  

**Secrets:** UUIDs / URIs / passwords / panel paths **not** reproduced in this report. Egress IPs and public hostnames retained as experimental identifiers.

---

## 5. Controlled-variable verification

Intended A/B/A switch (operator):

```text
VEESP RAW :8443  →  EQVPS RAW :8443  →  VEESP RAW :8443
```

**Egress IP evidence (FACT):**

| Phase | `api.ipify.org` body | Interpretation |
|-------|----------------------|----------------|
| VEESP baseline | `178.173.250.69` | VEESP |
| EQVPS | `95.216.126.173` | EQVPS |
| EQVPS post-app | `95.216.126.173` | Still EQVPS |
| VEESP recovery | `178.173.250.69` | VEESP restored |

| Variable | Classification | Notes |
|----------|----------------|-------|
| Selected VPN endpoint/profile | **CHANGED** | Primary experimental variable |
| Windows machine | **HELD CONSTANT** | Same precheck host |
| v2rayN version | **HELD CONSTANT** | 7.22.3 (EXP-A01 + log extract startup lines) |
| Client Xray version | **HELD CONSTANT** | 26.7.28 path under Program Files (EXP-A01) |
| TUN enabled / Wintun path | **HELD CONSTANT** | `xray_tun` Up throughout precheck; harness forbids TUN toggle |
| TUN MTU | **HELD CONSTANT** | 1500 |
| Routing mode (intended) | **HELD CONSTANT** | Operator instruction: do not change routing |
| DNS mode (global) | **HELD CONSTANT** | Ethernet DNS `192.168.0.1` at precheck; no harness DNS edit |
| UDP/443 block | **HELD CONSTANT** | No evidence of change in session |
| System Proxy | **HELD CONSTANT** | EXP-A01: ProxyEnable=0; harness forbids change; tests used `:10808` |
| Browser setup | **HELD CONSTANT** (assumed) | No evidence of browser reconfiguration mid-session |
| Physical Goodline link | **HELD CONSTANT** | Same Ethernet path; recovery PASS argues against outage |
| Server sniffing (VEESP off / EQVPS on) | **HELD CONSTANT** *within each endpoint* | **DIFFERENT across endpoints** (prior live recon) |
| Server Xray version | **HELD CONSTANT** *within each endpoint* | VEESP 26.6.22 / EQVPS 26.7.28 (prior live recon) |
| Profile-bound identity (SNI/host/UUID/DNS exemption target) | **CHANGED** (necessary) | Follows endpoint; not a structural client-stack change |
| xray process PID | **CHANGED** on switch | Expected core restart; `process-snapshot.txt` shows new xray PID near recovery |

**Remaining uncontrolled variable that most weakens causal precision (not the A/B/A existence claim):**  
endpoint-bound client profile identity + unresolved server sniffing/version deltas. These keep **root cause UNPROVEN** while still allowing **endpoint-following failure** as FACT.

---

## 6. VEESP baseline

**Transport (automated, via `http://127.0.0.1:10808`) — PASS**

| Test | Result | Detail |
|------|--------|--------|
| Egress | PASS | `178.173.250.69`, HTTP 200 |
| Ordinary HTTPS | PASS | Cloudflare trace 200 |
| Repeated HTTPS ×5 | PASS | 5/5 |
| ~10 MB body | PASS | 10_000_000 bytes in ~2.53 s |

**Manual real apps — PASS** (`manual-acceptance.csv` @ 10:41:09Z)

| App | Question | Answer |
|-----|----------|--------|
| Cursor | works | **Y** |
| ChatGPT | prompt_works | **Y** |
| YouTube | playback_works | **Y** |

Matches operator observation. Facebook **NOT TESTED** at baseline.

---

## 7. EQVPS transport

**PASS** — both immediately after switch and after application FAIL phase.

| Suite | Egress IP | HTTPS | Repeat | ~10 MB |
|-------|-----------|-------|--------|--------|
| EQVPS (10:41:51Z) | `95.216.126.173` | PASS | 5/5 | PASS (~1.60 s) |
| EQVPS post-app (10:47:01Z) | `95.216.126.173` | PASS | PASS (1× recheck) | PASS (~2.01 s) |

**FACT:** EQVPS basic transport health remained intact **while** real apps failed. Transport PASS **must not** be read as application-path PASS.

---

## 8. EQVPS Cursor acceptance

| Question | Evidence answer |
|----------|-----------------|
| complete usable response | **N** |
| Reconnecting | **Y** |
| stuck Thinking | **Y** |
| Taking longer than expected | **Y** |
| Agent stopped retrying | **N** |
| Operator note | «Я сам остановил курсор» (operator manually stopped Cursor) |

**Classification: FAIL** (not UNSTABLE)

**Justification:** usable complete response = **NO**, with the known failure symptom cluster (Reconnecting + Thinking + Taking longer) reproduced. Manual stop after evident failure does **not** downgrade to UNSTABLE. Do **not** claim the Agent independently exhausted retries — `agent_stopped_retry=N`.

Timestamp: 2026-08-29T10:43:44Z (≈2 minutes after EQVPS transport PASS).

---

## 9. EQVPS ChatGPT acceptance

| Question | Answer |
|----------|--------|
| Homepage/UI usable | **N** |
| Prompt submitted | **N** |
| Complete response | **N** |

**Classification: APPLICATION/UI ACCEPTANCE FAIL BEFORE PROMPT EXECUTION**

Do **not** phrase as “prompt failed.” Evidence shows failure **before** submission.

Timestamp: 2026-08-29T10:45:37Z.

---

## 10. EQVPS YouTube acceptance

| Question | Answer |
|----------|--------|
| Homepage | **N** |
| Video page | **N** |
| Playback starts | **N** |
| Playback usable | **N** |

**Classification: REAL APPLICATION FAIL**

Do **not** substitute prior curl / full-body / IWR YouTube HTTP tests for this browser acceptance row.

Timestamp: 2026-08-29T10:46:45Z.

---

## 11. Facebook control

| Phase | Result |
|-------|--------|
| VEESP baseline | **NOT TESTED** |
| EQVPS (this session, operator usable) | **FAIL** (`usable=N` @ 10:47:01Z) |
| VEESP recovery | **NOT TESTED** |

### Reconciliation with earlier path asymmetry

| Source | Claim / result | Strength |
|--------|----------------|----------|
| EXP-A01 live recon | VEESP TUN **IWR** Facebook FAIL; EQVPS isolated `:18088` **IWR** PASS | Different method (IWR), different path type |
| AUDIT 01 matrix | Facebook EQVPS TUN / browser = **NOT TESTED** / UNKNOWN | No MARS-filed browser PASS |
| Operator/task memory of historical explicit-proxy “Facebook opened” | **Not located** as a Git-safe filed PASS under `assets/EQVPS-MICRO-IP` | Treat as **UNVERIFIED / weak historical** |
| EXP-A01b | EQVPS TUN-path browser usable = **FAIL** | Strongest current filed browser row |

**Possible explanations (non-exclusive, none proven):** TUN vs explicit/isolated proxy; different session/time; different browser state; intermittent/path behaviour; weak old evidence.

→ Filed under **CONTRADICTIONS / UNRESOLVED DIFFERENCES** (§20). **No invented root cause.**

---

## 12. VEESP recovery

**Transport — PASS** (egress `178.173.250.69`, HTTPS, 5/5 repeat, 10 MB ~2.50 s) starting 10:47:44Z.

**Manual apps — PASS** @ 10:50:30Z:

| App | Answer |
|-----|--------|
| Cursor works again | **Y** |
| ChatGPT prompt works | **Y** |
| YouTube playback works | **Y** |

**Final:** `veesp_restored_internet_ok=Y` @ 10:50:42Z.

Matches operator observation that VEESP restore restored usable Internet/apps.

---

## 13. Canonical A/B/A matrix

| Test | VEESP BASELINE | EQVPS | VEESP RECOVERY |
|------|----------------|-------|----------------|
| Transport egress | **PASS** | **PASS** | **PASS** |
| Ordinary HTTPS | **PASS** | **PASS** | **PASS** |
| Repeated HTTPS | **PASS** | **PASS** | **PASS** |
| ~10 MB | **PASS** | **PASS** | **PASS** |
| Cursor | **PASS** | **FAIL** | **PASS** |
| ChatGPT | **PASS** | **FAIL** | **PASS** |
| YouTube | **PASS** | **FAIL** | **PASS** |
| Facebook | **NOT TESTED** | **FAIL** | **NOT TESTED** |

EQVPS post-app transport recheck: **PASS** (supports transport≠application separation).

---

## 14. Transport vs application finding

**Prominent finding (FACT):**

| EQVPS layer | Verdict |
|-------------|---------|
| TRANSPORT HEALTH | **PASS** |
| REAL APPLICATION ACCEPTANCE | **FAIL** (Cursor, ChatGPT, YouTube, Facebook) |

Same mixed-proxy path (`:10808`) that carried PASS transport measurements coexisted with FAIL real apps. Therefore:

- Transport PASS ≠ application path PASS.  
- Failure class is **application / long-lived / interactive / CDN-facing path behaviour under EQVPS egress**, not “EQVPS cannot egress HTTPS” or “EQVPS cannot transfer ~10 MB.”

---

## 15. Client/global-failure hypotheses weakened

Because VEESP PASS → EQVPS app FAIL → VEESP PASS again **without structural client changes**:

| Hypothesis | Effect of EXP-A01b |
|------------|--------------------|
| Global v2rayN failure | **STRONGLY WEAKENED** |
| Global Wintun / TUN failure | **STRONGLY WEAKENED** |
| Global Windows networking failure | **STRONGLY WEAKENED** |
| Global browser failure | **STRONGLY WEAKENED** |
| Global Cursor failure | **STRONGLY WEAKENED** |
| Global Goodline outage | **STRONGLY WEAKENED** |
| Simple persistent client misconfiguration (affecting all profiles equally) | **STRONGLY WEAKENED** |

**Not mathematically excluded:** profile-specific client settings, residual DNS/split rules for `metacode-cloud.com`, intermittent path state, app/CDN policies tied to EQVPS IP, sniffing/version interaction.

---

## 16. Remaining server/configuration differences

From EXP-A01 live recon (unchanged by A01b; A01b did not mutate servers):

| Difference | VEESP | EQVPS | Status after A01b |
|------------|-------|-------|-------------------|
| Sniffing on `:8443` | off | on | Still **POSSIBLY MATERIAL**; untested by A01b |
| Server Xray version | 26.6.22 | 26.7.28 | Still **POSSIBLY MATERIAL**; untested by A01b |
| OS/kernel | 22.04 / 5.15 | 24.04 / 6.8 | Unchanged; transport healthy both sides |
| UFW | inactive | active (8443 allowed) | Unchanged; transport PASS |

**Sequencing judgment vs FriendHosting:**  
Equalizing sniffing or Xray version **on EQVPS** would isolate one config knob with **less geographic confounding**, but would **not** discriminate provider/ASN/path from shared Goodline↔Hetzner / IP-reputation / CDN interaction. After a clean A/B/A application differential, an **independent near-equivalent provider control** has **higher discriminatory value** for the now-leading domain. Prefer FriendHosting (with sniffing/version intentionally matched in the charter) **before** EQVPS mutation experiments. Run sniffing/version A/B on EQVPS **after FriendHosting**, or **only if FriendHosting also FAILs**.

---

## 17. Updated hypothesis register

| ID | Hypothesis | Confidence after A01b | Supporting | Contrary / limiting | Still unproven |
|----|------------|----------------------|------------|---------------------|----------------|
| **A** | EQVPS server configuration error | **MEDIUM** | Apps fail only on EQVPS; sniffing/version deltas exist | Transport PASS; no smoking-gun field proven causal | That a specific config bit causes app FAIL |
| **B** | Xray 26.7.28 server-version interaction | **LOW–MEDIUM** | Version differs from working VEESP | Client also 26.7.28; EQVPS transport PASS | Version as cause |
| **C** | Sniffing difference | **MEDIUM** | On vs off across endpoints | Untested directly in A01b | Sniffing as cause |
| **D** | EQVPS provider/network behaviour | **MEDIUM–HIGH** | Failure follows EQVPS endpoint | Transport PASS; other sub-hyps open | Provider as sole cause |
| **E** | Hetzner endpoint/network behaviour | **MEDIUM** | EQVPS on Hetzner HEL path (colo HEL in CF traces) | No ASN forensics this wave | Hetzner-specific causation |
| **F** | EQVPS public IP reputation / IP-specific behaviour | **MEDIUM** | Broad app FAIL under same IP that PASSes curl | No reputation/API evidence filed here | IP reputation as cause |
| **G** | Goodline ↔ EQVPS/Hetzner path issue | **MEDIUM–HIGH** | Client constant; only endpoint/path changes | Single window; no traceroute/pcap | Path as sole cause |
| **H** | Application/CDN/backend interaction with that path/IP | **MEDIUM–HIGH** | Transport PASS + multi-app FAIL pattern | Mechanism unknown | Exact CDN/policy mechanism |
| **I** | Windows/v2rayN global client problem | **LOW** | — | VEESP baseline+recovery PASS | — |
| **J** | Wintun/TUN global problem | **LOW** | — | Same TUN stack PASSes on VEESP | — |
| **K** | MTU / simple PMTU issue | **LOW** | — | 10 MB PASS both endpoints | Subtle PMTU for some apps only |
| **L** | DNS issue | **LOW–MEDIUM** | Could explain early ChatGPT/YouTube UI FAIL | Ordinary HTTPS PASS via same proxy; VEESP recovery PASS | Residual split-DNS under EQVPS profile |
| **M** | Intermittent / time-dependent network issue | **LOW–MEDIUM** | Always possible in one window | Immediate recovery PASS; coherent A/B/A | Longer multi-day replication |

**No ROOT CAUSE row.** Closest framing: **endpoint-following application-path defect domain** (INFERENCE), spanning D/E/F/G/H plus residual A/C.

---

## 18. Provider/path hypothesis assessment

| Question | Answer |
|----------|--------|
| Does A01b strengthen EQVPS endpoint/provider/path/app-interaction domain? | **YES** (materially) |
| Is provider/path **proven** root cause? | **NO / UNPROVEN** |
| Does transport equivalence falsify provider issues? | **NO** — apps can fail with healthy basic transport |
| CASE A (provider/path strengthened by VEESP PASS / EQVPS FAIL under controlled client)? | **YES — now established at application layer** (EXP-A01’s “NOT established” is **superseded** for this question) |

Confidence language: **MEDIUM–HIGH** for “defect domain includes EQVPS endpoint/path/IP/app interaction”; **not HIGH** for any single named provider fault.

---

## 19. FriendHosting decision gate

**Gate: YES**

**Is an independent provider / network control node now justified?** **YES.**

**Why now (after A01b, not after A01 alone):**  
Same-client TUN A/B/A is **complete**. Failure **follows EQVPS** and clears on VEESP. Remaining uncertainty is inside endpoint/provider/path/app-interaction vs residual EQVPS-local config (sniffing/version). A third near-equivalent node discriminates those families.

**Planned candidate (operator-external knowledge; not MARS-persisted preflight metrics):**  
FriendHosting · Germany · Frankfurt · Telehouse — treat Looking Glass numbers as **UNVERIFIED** until separately filed.

**What FriendHosting discriminates:**

```text
Same Windows / v2rayN / TUN / client environment
+ near-equivalent VLESS/TLS/RAW server stack
+ different provider
+ different network/ASN
+ different location
```

| Outcome | Interpretation |
|---------|----------------|
| FriendHosting **PASS** while EQVPS still **FAIL** | **Strongly increases** endpoint/provider/path/IP-domain confidence for EQVPS |
| FriendHosting also **FAIL** | EQVPS-provider-specific hypothesis **weakens substantially**; shared client/ISP/application-path factors need deeper investigation (plus revisit sniffing/version) |

**Charter hygiene:** match sniffing and Xray version deliberately in the FriendHosting build notes to reduce confound; do not treat unpublished operator metrics as evidence until copied into MARS Storage/evidence.

---

## 20. CONTRADICTIONS

1. **Facebook:** historical / chat “opened on explicit proxy” vs EXP-A01b EQVPS browser **FAIL**; also EXP-A01 isolated IWR **PASS** vs TUN/browser **FAIL** — methods and paths differ → **UNRESOLVED DIFFERENCE**.  
2. **EXP-A01 executive H (FriendHosting = NO)** vs **post-A01b gate = YES** — not a factual conflict; **decision supersession** after new evidence.  
3. Prior narrative risk: “EQVPS transport healthy ⇒ ready for production apps” vs A01b app FAIL — any such implication is **contradicted** and must not be reused.

**Contradictions / unresolved differences count: 3**

---

## 21. STALE CONCLUSIONS

| Prior conclusion | Status |
|------------------|--------|
| EQVPS real-app TUN acceptance = not proven / pending | **STALE** — now **proven FAIL** for Cursor/ChatGPT/YouTube/Facebook in filed session |
| Need EXP-A01b before provider-path strengthening | **STALE as open action** — A01b **done** |
| FriendHosting not yet justified (EXP-A01) | **STALE as standing gate** — superseded to **YES** |
| VEESP `:8443` may still be WebSocket (older docs) | Remains **STALE** per EXP-A01 (live RAW) — unchanged |

---

## 22. SUPERSEDED VERDICTS

1. EXP-A01: “CASE A / provider-path strengthening **NOT established**” → **SUPERSEDED**: application-layer A/B/A **established**.  
2. EXP-A01: FriendHosting gate **NO** → **SUPERSEDED**: gate **YES**.  
3. EXP-A01 recommended next = EXP-A01b → **SUPERSEDED**: A01b complete; next = FriendHosting control (see §26).  
4. Any standing claim that EQVPS RAW `:8443` is “acceptance-complete” because isolated/full-transfer/curl PASS → **SUPERSEDED** by real-app FAIL.

**Superseded verdicts count: 4**

---

## 23. UNVERIFIED CLAIMS

1. FriendHosting Looking Glass / Telehouse preflight timings (not MARS-persisted).  
2. Historical explicit-proxy “Facebook opened” anecdote (not found as filed PASS).  
3. Chat-era “24443 Cursor PASS” (AUDIT: UNVERIFIED; not re-tested here).  
4. Exact ASN ownership / IP reputation score for `95.216.126.173`.  
5. That sniffing-on or Xray 26.7.28 is the causal mechanism.  
6. That Agent would have stopped retrying without operator intervention.

**Unverified claims count: 6**

---

## 24. Canonical facts after EXP-A01b

1. EXP-A01b session `2026-08-29_173912_live` **COMPLETED** with VEESP restored.  
2. VEESP baseline: transport **PASS**; Cursor/ChatGPT/YouTube **PASS**.  
3. EQVPS: egress **`95.216.126.173`**; transport suite **PASS** (including post-app).  
4. EQVPS Cursor **FAIL** (complete=N; reconnecting/thinking/longer=Y; agent_stopped_retry=N; operator stopped).  
5. EQVPS ChatGPT **FAIL before prompt** (homepage/UI=N).  
6. EQVPS YouTube **REAL APPLICATION FAIL** (all four browser layers N).  
7. EQVPS Facebook usable **FAIL**.  
8. VEESP recovery: transport **PASS**; Cursor/ChatGPT/YouTube **PASS**; internet OK **Y**.  
9. A/B/A differential **reproduced**.  
10. Harness did not auto-switch VPN or write v2rayN config; server mutations **0**.  
11. Exact root cause **UNPROVEN**.  
12. FriendHosting independent control is **justified**.

---

## 25. Remaining open questions

1. Will a near-equivalent FriendHosting Frankfurt node PASS the same real-app matrix on this client?  
2. Does disabling sniffing on EQVPS `:8443` change app acceptance?  
3. Does aligning EQVPS server Xray to 26.6.22 (or VEESP to 26.7.28) change app acceptance?  
4. Does EQVPS FAIL reproduce on **explicit System Proxy / `:10808`-only browser** without TUN (RAW-era falsification still thin)?  
5. Is Facebook FAIL browser-specific vs IWR asymmetry?  
6. What packet/CDN behaviour differs for interactive apps vs Cloudflare speed/trace under EQVPS IP?  
7. Multi-day / multi-hour stability of the differential?

---

## 26. Recommended next experiment

**Single best next experiment: FriendHosting independent provider/path control (EXP-FH01 / charter name TBD).**

**Procedure sketch (do not execute in this task):**

1. Provision FriendHosting DE/FRA/Telehouse per operator procurement gates.  
2. Build near-equivalent VLESS+TLS+RAW `:8443` stack; **deliberately record** sniffing + Xray version (prefer match to VEESP sniffing-off **or** document matched-to-EQVPS — pick one in charter).  
3. Same Windows client; change **only** selected profile/endpoint.  
4. Repeat A01b matrix: transport + Cursor + ChatGPT + YouTube (+ Facebook).  
5. Restore VEESP; confirm recovery.

**Then:**

- If FH **PASS** / EQVPS **FAIL** → deepen EQVPS IP/provider/path/CDN investigation; sniffing/version become secondary.  
- If FH **FAIL** → prioritize EQVPS sniffing-off A/B and shared-path forensics **before** blaming EQVPS provider alone.

**Sniffing / Xray-version equivalence:** test **after FriendHosting**, or **only if FriendHosting reproduces the problem**.

---

## 27. Evidence path index

```text
X:\AI MARS\projects\mars-server-ops\evidence\EXP-A01b\2026-08-29_173912_live\
  COMPLETED.marker
  README.md
  session-summary.json
  session-events.csv
  manual-acceptance.csv
  precheck.json
  baseline-veesp.json
  transport-veesp.txt
  eqvps.json
  transport-eqvps.txt
  eqvps-post-app.json
  transport-eqvps-post-app.txt
  recovery-veesp.json
  transport-recovery.txt
  process-snapshot.txt
  v2rayn-log-extract.txt
  xray-client-log-extract.txt

X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-EXP-A01b-OFFLINE-EQVPS-ACCEPTANCE-CAPTURE.md
```

---

## 28. Git/server/client mutation closeout

| Boundary | Status |
|----------|--------|
| Analysis workspace | `X:\AI MARS` · volume **AI WS** · branch `mars/canonical-post-recovery` |
| Report created | This file only (documentation) |
| Git commit | **Not performed** |
| Git push | **Not performed** |
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| Client configuration mutation | **0** |
| FriendHosting provision | **Not performed** |
| Secret disclosure | **0** |
| Foreign WIP | Present elsewhere in tree — **out of scope**; not staged |

### Executive questions (A–K)

| Q | Answer |
|---|--------|
| **A.** Did VEESP pass before EQVPS? | **YES** |
| **B.** Did EQVPS basic transport pass? | **YES** |
| **C.** Did EQVPS real applications pass? | **NO** |
| **D.** Did VEESP recover after leaving EQVPS? | **YES** |
| **E.** Was the A/B/A differential reproduced? | **YES** |
| **F.** Does A01b materially weaken global Windows/v2rayN/TUN failure theory? | **YES** |
| **G.** Does A01b materially strengthen EQVPS endpoint/provider/path/application-interaction domain? | **YES** |
| **H.** Is the exact root cause proven? | **UNPROVEN** |
| **I.** Is FriendHosting now justified? | **YES** |
| **J.** Sniffing/Xray-version vs FriendHosting sequencing? | **After FriendHosting** (or **only if FriendHosting reproduces FAIL**) |
| **K.** Single best next experiment? | **FriendHosting independent control** (near-equivalent stack, same client, full app matrix) |

---

**End of report.**

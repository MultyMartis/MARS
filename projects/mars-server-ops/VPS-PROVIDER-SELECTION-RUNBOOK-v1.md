# VPS Provider Selection Runbook v1

**Programme:** MARS Server Ops & VPS Forge  
**Capability:** VPS PROVIDER SELECTION INTELLIGENCE  
**Status:** **BASELINE v1** — reusable decision procedure  
**Not:** purchase automation, provider API product, or standing recommendation engine

---

## 1. Purpose

Provide a **canonical, reusable** workflow for choosing VPS / cloud providers, geographic locations, datacenters, tariffs, and network paths for future MARS infrastructure tasks.

**Mandatory first stage:** OPERATOR REQUIREMENT INTAKE.  
Do **not** begin by assuming country, company, plan, or architecture.

---

## 2. Agent behaviour (mandatory)

Future Server Ops agents **must not** open with:

```text
Which VPS provider do you want?
```

when the operator expects a recommendation.

Instead:

1. Understand workload  
2. Understand operator / client network geography (sanitized)  
3. Understand required external services  
4. Understand payment / compliance constraints  
5. Normalize requirements  
6. Research current market (when chartered)  
7. Create ranked candidates  
8. Explain exclusions  
9. Deep-review top candidates  
10. Re-rank  
11. Give operator decision gate  
12. Perform real network tests (where applicable)  
13. Recommend procurement  

At hard blockers: ask the operator.  
Do not make the operator manually repeat facts already safely available in current MARS context.

**Never suggest falsifying** country, address, residency, company identity, or payment origin.

---

## 3. Canonical workflow (Stages 0–11)

| Stage | Name | Gate |
|-------|------|------|
| **0** | Operator requirement intake | Requirements captured |
| **1** | Requirements normalization | MUST / SHOULD / NICE / EXCLUSION table |
| **2** | Country / region screening | Candidate regions (not yet providers) |
| **3** | Provider long-list | Broad candidate set |
| **4** | Hard exclusion screen | Survivors only; exclusions recorded |
| **5** | Weighted shortlist / ranking | Scorecard applied |
| **6** | Deep provider site review | Primary-source review of top candidates |
| **7** | Final candidate re-approval | APPROVED FOR NETWORK TEST / HOLD / REJECTED |
| **8** | Pre-purchase network testing | Evidence from actual operator network |
| **9** | Procurement decision | [VPS-PROCUREMENT-GATE-v1.md](VPS-PROCUREMENT-GATE-v1.md) PASS |
| **10** | Post-provision network validation | Assigned IP tested |
| **11** | Controlled build | Separate implementation charter |

**Do not skip** from provider discovery to purchase.

### Case evidence (do not treat as standing provider ban list)

| Case | Lesson |
|------|--------|
| **AdminVPS / Server B** | **looking-glass PASS ≠ assigned IP/subnet PASS**. Preflight can PASS; assigned IP later REJECTED for direct ISP entry — retest **assigned** IP before heavy build. Canonical lesson for provider qualification. |
| **EQVPS / Hetzner HEL** | Transport PASS ≠ real-workload PASS; endpoint/ASN/path remain primary suspect domain (**UNPROVEN** exact mechanism). FriendHosting third control further weakens generic client/stack theories. |
| **FriendHosting / AS47447** | Value of **independent provider + different ASN/network + assigned-IP validation + known-listener TCP gate + real-workload acceptance**. Now **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** (soak unproven). |
| **VEESP** | Positive historical control — VLESS+TLS+RAW `:8443` real-workload PASS |

Canonical method docs: [VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md), [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md), [CONTROL-EVIDENCE-METHODOLOGY-v1.md](CONTROL-EVIDENCE-METHODOLOGY-v1.md).

---

## 4. Stage summaries

### Stage 0 — Operator requirement intake

Use [VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md](VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md).

Establish what the server is **for** before searching providers: workload, client location (sanitized), service compatibility, performance, resilience, access/recovery, payment/compliance.

Sensitive personal location details must **not** be needlessly committed to Git — use sanitized operational facts only.

### Stage 1 — Requirements normalization

Produce a requirement table. Classify every item: **MUST HAVE**, **SHOULD HAVE**, **NICE TO HAVE**, **EXCLUSION**.

A **HARD EXCLUSION** overrides a high marketing score.

### Stage 2 — Country / region screening

Screen countries/regions **before** detailed provider ranking where useful.

Evaluate: approximate geography; expected latency; required AI/service country support; legal/provider restrictions; likely route diversity; relationship to existing infrastructure; jurisdiction / failure-domain independence.

- Never rank a country on physical distance alone.  
- Never treat provider marketing latency as operator truth.

### Stage 3 — Provider long-list

Create a broad candidate set. For each provider identify: company; country; datacenter; virtualization; network/ASN; plans; traffic; IPv4/IPv6; backup; snapshots; console; rescue; firewall; IP replacement; support; VPN/proxy policy; payment; jurisdiction acceptance.

Prefer **primary sources**.

### Stage 4 — Hard exclusion screen

Eliminate providers that fail mandatory requirements **before** detailed scoring.

Record every exclusion:

| PROVIDER | FAILED REQUIREMENT | EVIDENCE | EXCLUSION VERDICT |

Never silently drop a provider.

Learned patterns (examples, not permanent rules):

- Technically excellent provider unsuitable because it does not accept customers in the operator jurisdiction.  
- Provider accepts customer but prohibits VPN/proxy in a specific location.  
- Desired location shares an undesirable failure domain with an existing node.

### Stage 5 — Weighted shortlist / ranking

Use [VPS-PROVIDER-RESEARCH-SCORECARD-v1.md](VPS-PROVIDER-RESEARCH-SCORECARD-v1.md).

Weights **must** be adapted to the task. Price is **not** dominant by default. Score never overrides a HARD EXCLUSION.

### Stage 6 — Deep provider site review

For top candidates, review actual current sites and documentation in depth: tariffs; datacenters; AUP/terms; prohibited services; payment; refund; traffic; network restrictions; blocked ports; VPN docs; support; backup/snapshot/recovery; IP replacement; KVM details; test hosts; looking-glass / iperf endpoints.

- Primary provider documentation preferred.  
- Secondary/community evidence must be **labelled**.  
- Do not convert marketing claims into verified facts.  
- Identify contradictions inside provider documentation.  
- Time-sensitive facts: mark **REVERIFY AT NEXT PROCUREMENT**.

### Stage 7 — Final candidate re-approval

Re-score after deep review. Verdicts:

| Verdict | Meaning |
|---------|---------|
| **APPROVED FOR NETWORK TEST** | Proceed to Stage 8 |
| **APPROVED WITH RESIDUALS** | Proceed with explicit residuals listed |
| **HOLD** | Insufficient evidence or operator decision pending |
| **REJECTED** | Do not proceed |

Do **not** purchase yet.

### Stage 8 — Pre-purchase network testing

Use [VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md).

Test from the **actual** operator workstation/network. If VPN/TUN would distort results, temporarily test using direct ISP routing. Do not require Cursor/AI tools during measurement.

### Stage 9 — Procurement decision

Pass [VPS-PROCUREMENT-GATE-v1.md](VPS-PROCUREMENT-GATE-v1.md). Only then: **PROCUREMENT ALLOWED**.

### Stage 10 — Post-provision network validation

Pre-purchase endpoints prove **provider/location** suitability only. They do **not** prove the assigned VPS/IP path.

Before full production build verify: IP reachability; SSH; latency; loss; throughput; IP reputation where relevant; required AI/services; provider console; backup state.

If assigned IP has poor reachability: investigate **IP replacement** before heavy configuration.

### Stage 11 — Controlled build

Separate explicit implementation charter. Server Ops documentation does not authorize uncontrolled install.

---

## 5. External service compatibility (time-sensitive)

For AI-workstation VPN tasks, check **current** support/availability for required services such as:

- OpenAI / ChatGPT  
- Cursor and model providers used through Cursor  
- Anthropic when relevant  
- Google services when relevant  
- GitHub, Telegram, required APIs, target websites  

These are **TIME-SENSITIVE**. Do **not** hard-code country availability permanently into MARS. Re-check authoritative current sources at each procurement wave. Mark stale claims **REVERIFY AT NEXT PROCUREMENT**.

---

## 6. Related documents

| Document | Role |
|----------|------|
| [VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md](VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md) | Stage 0 intake categories |
| [VPS-PROVIDER-RESEARCH-SCORECARD-v1.md](VPS-PROVIDER-RESEARCH-SCORECARD-v1.md) | Stages 4–5 / 7 scoring |
| [VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md) | Stages 8 / 10 network tests |
| [VPS-PROCUREMENT-GATE-v1.md](VPS-PROCUREMENT-GATE-v1.md) | Stage 9 gate |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Programme navigation |
| Case study (Server B) | [assets/SERVER-B-PLANNING/SERVER-B-PROVIDER-SELECTION-CASE-v1.md](assets/SERVER-B-PLANNING/SERVER-B-PROVIDER-SELECTION-CASE-v1.md) |

---

## 7. Explicit non-claims

This runbook does **not**:

- authorize purchase, DNS mutation, SSH, or provider login;  
- claim any provider is permanently preferred;  
- replace Survivability destructive / risk authorities;  
- invent disk sizes, prices, or IP addresses.

---

*VPS Provider Selection Runbook v1 · documentation baseline · no runtime claimed.*

# Server B Provider Selection Case v1

**Planning locus:** `SERVER-B-PLANNING`  
**Status:** **CASE STUDY DOCUMENTED** — records completed operator/Web-GPT selection process  
**Not:** new market research; not proof Server B is provisioned  
**Generic capability:** [../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)

---

## 1. Purpose of this case

Turn the operator’s completed real-world Server B provider-selection process into a **reusable evidence case** under Server Ops.

This document **records** process and findings already established. It does **not** perform new provider research. Future cases must re-run Stages 0–11; do not treat AdminVPS as a permanent default.

---

## 2. Stage 0 — Requirement intake (sanitized summary)

| Category | Sanitized fact |
|----------|----------------|
| **Workload** | Independent secondary **production VPN** node; operator working VPN route; Xray / 3X-UI intended (native MARS install later — **no** marketplace preinstall) |
| **Role vs Server A** | Secondary node; Server A (MCA-VPN-001 / VEESP Amsterdam) remains untouched |
| **Client / operator network** | Operator jurisdiction requiring legitimate local payment path; home Ethernet + possible TUN for normal use — preflight measured on path appropriate to tests |
| **Service compatibility** | AI-workstation VPN path — OpenAI / ChatGPT, Cursor and related model providers, other APIs as needed — **TIME-SENSITIVE**; reverify at next procurement |
| **Performance** | Latency-sensitive interactive use; throughput important; IPv4 required |
| **Resilience** | Different failure domain from Server A (not Amsterdam / not same VEESP NL footprint); independent identity/domain |
| **Access / recovery** | Console / recovery path desired; IP replacement capability desirable |
| **Payment / compliance** | Provider must accept customer from operator’s actual jurisdiction; **no** falsification of residency/identity |

Sensitive personal details: **not** recorded in Git.

---

## 3. Stage 1 — Normalization (high level)

| Class | Examples for this case |
|-------|------------------------|
| **MUST HAVE** | Eligible customer jurisdiction; VPN/3X-UI use permitted for chosen location; workable payment; Finland (or equivalent screened region) path quality; independent from Server A NL failure domain; public IPv4; Ubuntu 24.04 LTS clean install |
| **SHOULD HAVE** | Official network test endpoints; emergency console; IP replacement; short initial billing term |
| **NICE TO HAVE** | Snapshots / provider backup options |
| **EXCLUSION** | Provider refuses operator jurisdiction; VPN forbidden at target DC; shared undesirable failure domain with Server A; payment path impossible |

---

## 4. Stage 2 — Country / region screening (summary)

| Region | Role in this case | Notes |
|--------|-------------------|-------|
| **Finland** | Preferred / tested | Strong pre-purchase network results for operator path |
| **Germany** | Compared | Materially worse observed HTTP/RTT in test window |
| **Netherlands** | Control / undesired for Server B geography | Server A already VEESP Amsterdam — failure-domain conflict for secondary node; NL AdminVPS endpoints also failed ICMP/HTTP in observed window (do **not** claim entire NL unavailable) |

Never ranked on distance alone. Marketing latency not treated as truth.

---

## 5. Stages 3–4 — Long-list and hard exclusions (recorded)

### UpCloud (historical candidate)

| Field | Value |
|-------|-------|
| Technical attractiveness | High (plan/location fit for FI-HEL1) |
| Deeper registration review | Customer-eligibility / compliance conflict for operator’s actual situation |
| Verdict | **REJECTED FOR THIS OPERATOR / CURRENT PROCUREMENT CASE** |
| Decision doc status | [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) marked **SUPERSEDED** |

**No attempt to bypass provider eligibility restrictions is acceptable.**

### Other exclusion patterns learned

| Pattern | Lesson |
|---------|--------|
| Excellent tech, wrong eligibility | Hard exclusion |
| Accepts customer but forbids VPN at location | Hard exclusion |
| Desired country but shares failure domain with existing node | Hard exclusion / strong demotion |

Full silent drops: **forbidden** — exclusions must be written.

---

## 6. Stages 5–7 — Ranking and deep review (AdminVPS)

| Finding (operator/Web-GPT established) | Classification |
|----------------------------------------|----------------|
| Serves Russian customers | PRIMARY review claim — **REVERIFY AT NEXT PROCUREMENT** |
| Finland VPS available (Helsinki / FI1 tested) | PRIMARY + OPERATOR-OBSERVED |
| VPN / 3X-UI use supported for relevant location based on reviewed provider material | PRIMARY review — **REVERIFY AT NEXT PROCUREMENT** |
| Normal Russian payment path usable | OPERATOR context — **REVERIFY AT NEXT PROCUREMENT** |
| Network test facilities available | OPERATOR-OBSERVED |
| Real pre-purchase tests completed | See [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md) |

**Stage 7 verdict for AdminVPS Finland:** **APPROVED FOR NETWORK TEST** → network PASS → procurement candidate.

Do **not** generalize as permanent recommendation.

---

## 7. Stages 8–9 — Network + procurement

| Item | Result |
|------|--------|
| Network preflight | **PASS** — [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md) |
| Procurement gate | **APPROVED FOR PROCUREMENT** — [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) |
| Provisioned? | **NO** — NOT YET PROVISIONED |

---

## 8. Stages 10–11 — Not started

| Stage | Status |
|-------|--------|
| 10 Post-provision validation | **NOT STARTED** — no assigned IP yet |
| 11 Controlled build | **NOT STARTED** — requires separate charter after intake |

---

## 9. Related documents

- [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md)  
- [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md)  
- [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) (SUPERSEDED UpCloud)  
- [../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  

---

*Server B Provider Selection Case v1 · historical process record · Server B not provisioned.*

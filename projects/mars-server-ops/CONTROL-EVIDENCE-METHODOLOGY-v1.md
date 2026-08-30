# MARS Server Ops — Control & Evidence Methodology v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **BASELINE v1** — reusable diagnostic method  
**Origin:** VPN investigation (VEESP / EQVPS / FriendHosting), 2026-08  
**Not:** orchestration product, auto-A/B engine, or proof of any live root cause

---

## 1. Purpose

Prefer **independent controls** and **one-variable changes** over multi-knob config churn when a service is technically reachable but operationally broken.

---

## 2. Control-node roles (VPN case — generalized)

| Role | VPN example | Purpose |
|------|-------------|---------|
| **Positive / known-good control** | VEESP (`MCA-VPN-001`) | Proves the operator client stack and path can succeed |
| **Negative / problematic control** | EQVPS | Reproduces transport PASS + real-workload FAIL |
| **Independent modern control** | FriendHosting Germany (`FRIENDHOSTING-DE`) | Same architecture class on different provider/ASN/path; now **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** (soak still unproven) |

**Why three controls beat endless config edits:**

- Holds the Windows/v2rayN/TUN/client-core stack constant while changing endpoint.  
- Distinguishes **global client failure** from **endpoint/provider/path failure**.  
- Prevents premature Reality/WS/gRPC/BBR/MTU experiments when acceptance already fails at application layer.

**EQVPS diagnostic stance after FriendHosting final acceptance (documentation):**

| Exact root cause | **UNPROVEN** |
| Strongly weakened | generic Windows / v2rayN / TUN / Xray 26.7.28 / VLESS+TLS+RAW / generic Goodline inability |
| Strengthened domain | EQVPS endpoint / IP / prefix / Hetzner-HEL / path / application interaction |
| Do not overclaim | Exact mechanism remains unknown |

Negative case = EQVPS. Independent positive case = FriendHosting. Positive control = VEESP.

---

## 3. Generalization beyond VPN

Use the same pattern for:

| Domain | Positive control | Negative / candidate | Independent control |
|--------|------------------|----------------------|---------------------|
| DB migration | Known-good source | Failing target | Third environment with same schema class |
| Docker host migration | Working host | Broken host | Clean third host |
| Staging vs production | Staging PASS baseline | Production anomaly | Isolated reproduce node |
| Provider migration | Old provider PASS | New provider FAIL | Alternate provider same stack |
| Service troubleshooting | Last known-good revision | Current failing revision | Minimal reproduce instance |

**Method:** change **one primary variable** (endpoint, host, image tag, provider IP), keep client/operator path constant, capture evidence, restore control.

---

## 4. Anti-config-churn rule

**If** basic transport / process health is **PASS** and real workload is **FAIL**:

Do **not** automatically change:

- Reality / XHTTP / WS / gRPC / HTTPUpgrade  
- BBR / sysctl / MTU / DNS stack “because maybe”  
- Core version churn without A/B charter  
- Multi-variable panel rebuilds  

**Instead:**

1. Classify the failure (`TRANSPORT` vs `APPLICATION` vs `PATH` vs `CONFIG` vs `UNKNOWN`).  
2. Establish or reuse controls.  
3. Change **one** variable.  
4. Capture evidence.  
5. Retest real workloads.  
6. Record WEAKENED / UNCHANGED / STRENGTHENED / UNPROVEN for each hypothesis.

No random performance tuning unless evidence shows a bottleneck.

**Reusable slogan for Server Ops agents:**

```text
Healthy transport + failing apps  ⇒  classify + controls + single-variable A/B
                                 ≠  transport-mode roulette
```

---

## 5. Evidence precedence

1. Newest reproducible evidence / current live reports  
2. Controlled A/B/A experiments  
3. Current programme documentation  
4. Older reports  
5. Historical handoffs  

Conflicts → newer reproducible evidence wins. Older contradicted conclusions → **SUPERSEDED** in [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](SUPERSEDED-CONCLUSIONS-REGISTER-v1.md).

Evidence classes: **FACT** · **INFERENCE** · **HYPOTHESIS** · **UNPROVEN** · **OPERATOR-PROVIDED**.

---

## 6. Hypothesis status vocabulary

| Status | Meaning |
|--------|---------|
| **WEAKENED** | New evidence reduces likelihood |
| **UNCHANGED** | Still possible; not newly informed |
| **STRENGTHENED** | New evidence increases likelihood |
| **UNPROVEN** | Not established as causal mechanism |

Exact mechanism remains **UNPROVEN** until evidence truly isolates it.

---

## 7. Related documents

- [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md)  
- [CHANGE-RISK-MODEL-v1.md](CHANGE-RISK-MODEL-v1.md)  
- [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  
- [SERVER-OPS-AGENT-KNOWLEDGE-v1.md](SERVER-OPS-AGENT-KNOWLEDGE-v1.md)  
- [reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md](reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md)

---

*Control & Evidence Methodology v1 · FriendHosting third-control update · documentation only.*

# VPS Provider Research Scorecard v1

**Programme:** MARS Server Ops & VPS Forge  
**Stages:** 4 (hard exclusion), 5 (weighted ranking), 7 (re-approval)  
**Status:** **BASELINE v1** — reusable scoring model  
**Not:** automated scorer, marketing comparator, or permanent provider ranking

---

## 1. Absolute rule

```text
HARD EXCLUSION overrides any high score.
Score never authorizes purchase alone.
```

---

## 2. Hard exclusion log (Stage 4)

Before scoring, eliminate mandatory failures. **Never silently drop** a provider.

| PROVIDER | FAILED REQUIREMENT | EVIDENCE | EXCLUSION VERDICT | DATE |
|----------|--------------------|----------|-------------------|------|
| | | | | |

### Example hard exclusions

| Exclusion | Typical evidence |
|-----------|------------------|
| Provider refuses customer jurisdiction | Registration / KYC / ToS / support statement |
| VPN explicitly forbidden for chosen location | AUP / offer terms for that DC |
| Required payment impossible | Payment docs |
| Required service country unsupported | Current authoritative service docs (time-sensitive) |
| No required virtualization | Product page |
| No IPv4 when IPv4 required | Plan page |
| No emergency recovery path | Support / rescue docs |
| Unacceptable traffic / AUP policy | Terms |
| Undesirable shared failure domain with existing node | Inventory + ASN/region analysis |

---

## 3. Suggested scoring dimensions (Stage 5)

Weights **MUST** be adapted to the task. Do **not** make price dominant by default.

For latency-sensitive AI/VPN workstation use: network quality and service compatibility may outrank price.

| Dimension | Suggested weight band | Task notes |
|-----------|----------------------|------------|
| Compliance / eligibility | High when jurisdiction constrained | |
| Network geography | High for latency / failure-domain tasks | |
| Expected latency | High for interactive / AI VPN | Pre-purchase test later |
| Expected throughput | Medium–High | Pre-purchase test later |
| VPN / use-case permission | High for VPN nodes | Location-specific |
| Service compatibility | High for AI workstation | Time-sensitive |
| Failure-domain independence | High for secondary nodes | |
| Provider / network reputation | Medium | Label secondary evidence |
| Traffic allowance | Medium | |
| CPU / RAM value | Medium | |
| Backup / snapshot | Medium–High for prod | |
| Emergency console | Medium–High for prod | |
| IP replacement capability | Medium–High for VPN | |
| IPv4 / IPv6 | As required | |
| Support | Medium | |
| Payment compatibility | High when constrained | |
| Price | Low–Medium default | Never sole driver |
| Operational simplicity | Medium | |

---

## 4. Scoring template

Use a consistent scale (example: **0–5**, or **N/A** if not applicable).

| Provider | DC / location | Dim scores… | Weighted total | Residuals | Stage 5 rank |
|----------|---------------|-------------|----------------|-----------|--------------|
| | | | | | |

After Stage 6 deep review, **re-score** (Stage 7):

| Provider | Previous total | Post-review total | Stage 7 verdict | Residuals |
|----------|----------------|-------------------|-----------------|-----------|
| | | | APPROVED FOR NETWORK TEST / APPROVED WITH RESIDUALS / HOLD / REJECTED | |

---

## 5. Evidence labelling

| Label | Meaning |
|-------|---------|
| **PRIMARY** | Provider official site / docs / panel |
| **SECONDARY** | Community, blogs, third-party tests |
| **OPERATOR-OBSERVED** | Measured from operator network |
| **SAFE UNKNOWN** | Not verified |
| **REVERIFY AT NEXT PROCUREMENT** | Time-sensitive; must not be treated as permanent |

Do not convert marketing claims into verified facts.

---

## 6. Related documents

- [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  
- [VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md](VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md)  
- [VPS-PROCUREMENT-GATE-v1.md](VPS-PROCUREMENT-GATE-v1.md)  
- Server B case: [assets/SERVER-B-PLANNING/SERVER-B-PROVIDER-SELECTION-CASE-v1.md](assets/SERVER-B-PLANNING/SERVER-B-PROVIDER-SELECTION-CASE-v1.md)  

---

*Research Scorecard v1 · model only · no standing provider preference.*

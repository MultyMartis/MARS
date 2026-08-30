# Server B Provider Decision v2

**Status:** **APPROVED FOR PROCUREMENT — NOT YET PROVISIONED**  
**Wave:** MARS Server Ops — VPS Provider Selection Intelligence baseline  
**Authority:** Operator-approved procurement-test candidate after eligibility conflict on prior UpCloud path  
**Supersedes:** [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) (UpCloud) — historical record retained

---

## 1. Current approved procurement candidate

| Field | Approved value |
|-------|----------------|
| **Provider** | **AdminVPS** |
| **Location** | Finland / Helsinki |
| **Preferred tested network** | **FI1** |
| **Purpose** | Independent secondary production VPN node and operator working VPN route |
| **Plan (intended)** | **Micro** |
| **vCPU** | 2 |
| **RAM** | 4 GB |
| **Disk / storage** | **CONFIRM AT CHECKOUT** — do **not** invent |
| **Operating system** | Ubuntu 24.04 LTS — clean installation |
| **Initial purchase term** | **1 month** |
| **Marketplace preinstalled 3X-UI** | **NO** — native controlled MARS installation later |
| **Domain (registered)** | `metacode-cloud.com` |
| **DNS mutation in this wave** | **NONE** |

---

## 2. Procurement state

```text
APPROVED FOR PROCUREMENT — NOT YET PROVISIONED
```

| State | Meaning |
|-------|---------|
| **Approved for procurement** | Operator may purchase AdminVPS Finland VPS per this decision after checkout confirmation |
| **Not yet provisioned** | No AdminVPS VPS has been attested to MARS under this decision |

Do **not** mark Server B as provisioned.

---

## 3. Why AdminVPS replaced UpCloud

| Topic | Record |
|-------|--------|
| UpCloud technical fit | Technically attractive (FI-HEL1 / Starter profile) |
| Blocking issue | Deeper account-registration review established a **customer-eligibility / compliance conflict** for the operator’s actual situation |
| Bypass | **Not acceptable** — no falsification of country/residency/identity/payment origin |
| UpCloud verdict | **REJECTED FOR THIS OPERATOR / CURRENT PROCUREMENT CASE** |
| Historical doc | [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) → **SUPERSEDED** |

AdminVPS was then researched in depth (operator/Web-GPT). Current findings (case-specific — **REVERIFY AT NEXT PROCUREMENT**):

- Serves Russian customers  
- Finland VPS available  
- VPN / 3X-UI use supported for the relevant location based on reviewed provider material  
- Operator can use normal Russian payment path  
- Network test facilities available  
- Real pre-purchase tests completed — [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md)  

Do **not** generalize this as a permanent recommendation.

---

## 4. Failure-domain rule (unchanged)

```text
Server B must not depend on Server A.
Server A remains untouched during Server B construction.
```

Server A: MCA-VPN-001 — VEESP / Amsterdam region footprint.  
Server B: AdminVPS / Finland — geographic separation intentional.

Independent identity/secrets: [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md).

---

## 5. Network preflight

| Item | Status |
|------|--------|
| Pre-purchase FI1 | **PASS / APPROVED** |
| Post-provision assigned IP | **NOT YET APPLICABLE** |

Evidence: [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md).

---

## 6. Explicitly not recorded (SAFE UNKNOWN / deferred)

| Field | Status |
|-------|--------|
| AdminVPS server identifier | **NOT YET ASSIGNED** |
| Public IPv4 | **NOT YET ASSIGNED** |
| Public IPv6 | **NOT YET ASSIGNED** |
| Hostname | **NOT YET ASSIGNED** |
| Exact disk size | **CONFIRM AT CHECKOUT** |
| Price paid / billing identifiers | **NOT RECORDED** |
| Exact deployment timestamp | **NOT YET OCCURRED** |
| Final MCA asset ID | **NOT ASSIGNED** — locus remains `SERVER-B-PLANNING` |

Populate after operator provisioning using [PROVISIONING-INTAKE-CHECKLIST-v1.md](PROVISIONING-INTAKE-CHECKLIST-v1.md).

---

## 7. Procurement gate checklist (this case)

| Gate | Result |
|------|--------|
| Requirements complete | **PASS** (case documented) |
| Compliance pass | **PASS** for AdminVPS (UpCloud excluded) |
| Use-case policy pass | **PASS** based on reviewed provider material — **REVERIFY AT NEXT PROCUREMENT** |
| Payment pass | **PASS** for operator path — **REVERIFY AT NEXT PROCUREMENT** |
| Failure-domain pass | **PASS** (FI vs Server A NL) |
| Deep site review complete | **PASS** (operator/Web-GPT) — **REVERIFY AT NEXT PROCUREMENT** |
| Network preflight pass | **PASS** |
| Operator approval | **APPROVED FOR PROCUREMENT** |

Generic gate: [../../VPS-PROCUREMENT-GATE-v1.md](../../VPS-PROCUREMENT-GATE-v1.md).

---

## 8. Next operator action

1. Purchase **AdminVPS Finland** VPS for **one month** using the approved configuration after confirming **actual checkout** (plan Micro, 2 vCPU, 4 GB RAM, Ubuntu 24.04 LTS clean, disk as shown at checkout).  
2. Prefer tested network **FI1** / Helsinki path where checkout allows.  
3. **Stop** before manual application installation (no marketplace 3X-UI; no uncontrolled build).  
4. Return sanitized provisioning facts via [PROVISIONING-INTAKE-CHECKLIST-v1.md](PROVISIONING-INTAKE-CHECKLIST-v1.md).  
5. Then run **post-provision** network validation against the **assigned IP**.

---

## 9. Related documents

- [SERVER-B-PROVIDER-SELECTION-CASE-v1.md](SERVER-B-PROVIDER-SELECTION-CASE-v1.md)  
- [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md)  
- [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) — SUPERSEDED  
- [ARCHITECTURE-FREEZE-v1.md](ARCHITECTURE-FREEZE-v1.md)  
- [../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  

---

*Provider Decision v2 · AdminVPS Finland · APPROVED FOR PROCUREMENT · NOT YET PROVISIONED.*

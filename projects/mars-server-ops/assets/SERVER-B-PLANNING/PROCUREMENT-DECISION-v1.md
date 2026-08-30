# Server B Procurement Decision v1

**Status:** **SUPERSEDED**  
**Superseded by:** [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) (AdminVPS / Finland / Helsinki)  
**Wave:** MARS Server Ops Phase 3A (historical)  
**Authority:** Historical operator-approved planning freeze — **not** current procurement authority

---

## Supersession notice

```text
SUPERSEDED
Reason: provider customer-eligibility/compliance conflict discovered during deeper registration review.
```

| Topic | Record |
|-------|--------|
| Historical candidate | UpCloud / FI-HEL1 |
| Technical attractiveness | High |
| Blocking issue | Customer-eligibility / compliance conflict for the operator’s actual situation |
| Verdict for this operator / current case | **REJECTED FOR THIS OPERATOR / CURRENT PROCUREMENT CASE** |
| Bypass of eligibility restrictions | **Not acceptable** |
| Current approved candidate | **AdminVPS** Finland / Helsinki — see v2 |

This document is retained as **historical decision evidence**. Do not use it to authorize purchase.

---

## 1. Procurement summary (historical — frozen snapshot)

| Field | Approved value (at time of v1) |
|-------|--------------------------------|
| **Provider** | UpCloud |
| **Location** | FI-HEL1 — Helsinki, Finland |
| **Plan** | Starter |
| **vCPU** | 2 |
| **RAM** | 4 GB |
| **Storage** | 30 GB |
| **Public IPv4** | Included (provider plan) |
| **Operating system** | Ubuntu 24.04 LTS |
| **Server purpose** | Independent secondary production VPN node |

---

## 2. Historical procurement state (at time of v1)

```text
APPROVED BY OPERATOR — NOT YET PROVISIONED
```

At supersession time, Server B remained **not provisioned** under UpCloud. No UpCloud VPS creation is authorized by this superseded record.

---

## 3. Failure-domain rule (still valid conceptually)

```text
Server B must not depend on Server A.
Server A remains untouched during Server B construction.
```

Independent identity requirements remain in [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md). Current provider binding: [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md).

---

## 4. Explicitly not recorded (SAFE UNKNOWN / deferred)

The following were **not invented** in v1 and remain unassigned under the superseded UpCloud path:

| Field | Status |
|-------|--------|
| UpCloud server UUID | **NOT ASSIGNED** (path abandoned) |
| Public IPv4 address | **NOT ASSIGNED** |
| Public IPv6 address | **NOT ASSIGNED** |
| Hostname | **NOT ASSIGNED** |
| Independent domain | Later: `metacode-cloud.com` recorded under v2 — DNS not mutated in planning waves |
| UpCloud account identifiers | **NOT IN GIT** |
| Price paid / billing identifiers | **NOT RECORDED** |
| Exact deployment timestamp | **DID NOT OCCUR** under this decision |
| Final MCA asset ID | **NOT ASSIGNED** — locus remains `SERVER-B-PLANNING` |

---

## 5. Phase context (historical)

| Phase | Status at v1 |
|-------|--------------|
| Phase 1B-1 | **COMPLETE** — Server A live read-only intake |
| Phase 2A | **COMPLETE** — UpCloud / FI-HEL1 provider decision approved by operator |
| Phase 2B | **ARCHITECTURE DECISION APPROVED** |
| Phase 3A | **ACTIVE** — procurement + identity prep |

**Later reconciliation:** Phase 2A UpCloud approval superseded for eligibility/compliance; see Provider Selection Intelligence case and Decision v2.

---

## 6. Next operator action

**Do not** create UpCloud Server B under this document.

Follow [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) — AdminVPS Finland procurement.

---

## 7. Related documents

- [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) — **current**
- [SERVER-B-PROVIDER-SELECTION-CASE-v1.md](SERVER-B-PROVIDER-SELECTION-CASE-v1.md)
- [ARCHITECTURE-FREEZE-v1.md](ARCHITECTURE-FREEZE-v1.md)
- [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md)
- [PROVISIONING-INTAKE-CHECKLIST-v1.md](PROVISIONING-INTAKE-CHECKLIST-v1.md)
- [../MCA-VPN-001/SERVER-B-CLONE-BASELINE-v1.md](../MCA-VPN-001/SERVER-B-CLONE-BASELINE-v1.md)

---

*Procurement Decision v1 · SUPERSEDED · retained as historical evidence · Server B not provisioned.*

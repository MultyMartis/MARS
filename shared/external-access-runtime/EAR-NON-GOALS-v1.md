# EAR Non-Goals v1

Explicit exclusions. If a capability is not listed in [EAR-SCOPE-v1.md](EAR-SCOPE-v1.md) and appears here, it is **out of scope** for EAR v1 foundation and default charters.

---

## Analysis and decision-making

| Non-goal | Rationale |
|----------|-----------|
| Site audit logic | Belongs to OCPilot / WPilot / other consumers |
| Risk scoring or remediation plans | Consumer or human operator |
| Automated “fix” suggestions from live site | Violates separation; invites write pressure |
| SEO / catalog / theme **interpretation** | Consumer domain |

---

## Autonomy and automation claims

| Non-goal | Rationale |
|----------|-----------|
| Autonomous 24/7 crawlers | No HITL; boundary violation |
| Hidden background sync | Stealth automation forbidden by MARS discipline |
| Credential vault in git | Security model forbids |
| “Runtime exists” without source proof | Status honesty (AGENTS.md) |

---

## Write and destructive operations (v1)

| Non-goal | Rationale |
|----------|-----------|
| **Mode 3 — Connected Read Write** | **NOT ALLOWED IN V1** |
| File upload to production/test | Deferred to Phase 5 evaluation |
| Database INSERT/UPDATE/DELETE | Deferred |
| Admin actions that change state | Deferred |
| Mass delete or overwrite | Always forbidden without separate charter |

---

## Pilot and governance ownership

| Non-goal | Rationale |
|----------|-----------|
| Replacing OCPilot baselines or comparison methodology | Consumer responsibility |
| Modifying WPilot, ORCA, Website Factory repos in EAR foundation | Task charter isolation |
| Governance expansion or new policy engine | Not EAR’s role |
| MARS orchestration / multi-agent runtime | No runtime claimed |

---

## Implementation artifacts (v1 foundation task)

| Non-goal | Rationale |
|----------|-----------|
| Working code, scripts, connectors | Architecture-only deliverable |
| n8n / CI jobs / scheduled jobs | No fake automation |
| Docker services for EAR | **SAFE UNKNOWN** future; not v1 |
| npm/pip packages published as “EAR SDK” | Not v1 |

---

## Data handling extremes

| Non-goal | Rationale |
|----------|-----------|
| Full production DB dumps in git | Forbidden; external bulk only with charter |
| PII harvesting beyond audit need | Minimize; operator charter |
| Malware scanning as EAR core | Separate security charter if needed |

---

## Marketing / status anti-patterns

Do **not** claim:

- “EAR is deployed”
- “Sites are connected”
- “Snapshots are automatic”
- “MARS can access your hosting”

Until human-reviewed implementation evidence exists in-repo under explicit charter.

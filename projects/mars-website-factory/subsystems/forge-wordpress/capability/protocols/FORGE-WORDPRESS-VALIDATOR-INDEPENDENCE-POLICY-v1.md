# Forge WordPress Validator Independence Policy v1

**Document type:** Validation independence and escalation policy  
**Version:** v1  
**Stage:** FW-04

---

## Principles

Validators are **reusable independent review profiles** — not autonomous agent processes. Independence is achieved through role separation and separate Cursor passes when required.

---

## Independence rules

| Rule | Requirement |
|------|-------------|
| **WV6 visual parity** | Implementer **must not** approve own WV6 pass |
| **Security pass** | Implementer **must not** approve own security validation |
| **Visual parity authority** | **Operator** approves visual parity (WV6) |
| **Handoff acceptance** | **WPilot reviewer** (or operator acting as handoff reviewer) approves handoff acceptance |
| **Independent pass** | Validation may run as **separate Cursor Agent pass** with validator profile loaded |
| **No rewrite on validate** | Validator reads diff and artifacts; does **not** rewrite implementation unless assigned separate fix task |

---

## Role matrix

| Role | May implement | May self-validate structural | May approve WV6 | May approve security | May approve handoff |
|------|---------------|------------------------------|-----------------|----------------------|---------------------|
| Implementer (specialist) | Yes | Partial (non-blocking checks) | **No** | **No** | **No** |
| Independent validator pass | No | Yes | No (recommends) | Yes (recommends) | No (recommends) |
| Operator | No | Yes | **Yes** | Yes (escalation) | Yes (pre-handoff) |
| WPilot reviewer | No | No | No | No | **Yes** (operational acceptance) |

---

## Separate Cursor pass pattern

When independence is required:

1. **Pass A — Implement:** Load specialist + FW-SK-10; produce implementation; self-validate non-blocking items.
2. **Pass B — Validate:** Load validator profile(s) FW-V-01–07; read artifacts and diff only; produce validator report.
3. **Pass C — Operator gate:** Operator reviews WV6 evidence and accepts or rejects.

Same agent session **may** run Pass B if operator explicitly assigns validator role and implementer work is complete — but implementer **must not** mark WV6 or security as PASS without Pass B or operator review.

---

## Escalation

| Finding type | Escalate to |
|--------------|-------------|
| Blocking architecture | Operator + WAD revision |
| Blocking security | Operator; no release until resolved |
| Visual parity failure | Operator visual review |
| Handoff contract gap | Operator + WPilot boundary check |
| Scope violation | STOP — operator |

---

## Related

- [../validators/](../validators/)
- [FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md](FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md)
- [../../standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](../../standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md)
- [../../FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](../../FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md)

---

*Validator independence policy v1.*

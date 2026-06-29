# MARS — System Maturity Map (X-Drive Pack 2026-06)

**SoT:** [governance/current-operational-state-v1.md](../../governance/current-operational-state-v1.md)

**Filesystem migration means:** `PHYSICAL PATH RECONCILED` — **not** `RUNTIME IMPLEMENTED`, `PRODUCTION VALIDATED`, or `AUTOMATED`.

---

## Maturity classes (honest)

| Class | Meaning |
|-------|---------|
| **operational** | Used today in human-supervised workflows |
| **experimental** | Bounded in-tree probes; REPORT + lane isolation |
| **conceptual** | Contracts and vocabulary — no shipped product |
| **planned** | May exist later — not commitment language |
| **external** | Outside MARS core (n8n, live hosts) |
| **historical** | Legacy import — three-way split required |
| **excluded** | Do not treat as canonical MARS core |
| **SAFE UNKNOWN** | Missing evidence — state verification step |

---

## Area matrix

| Area | Maturity | Notes |
|------|----------|-------|
| Governance docs | operational (maintenance) | Frozen baseline post–Cycle 8 |
| Execution loop | operational | Web-GPT → Cursor → Human |
| Website Factory | operational (methodology) | **Not** runtime engine |
| mars-runtime | experimental / conceptual | R1 boundary only |
| tools/ | operational (manual) | Helpers — not enforcers |
| Survivability | operational | Human-invoked validator |
| WPilot | operational (reference) | RC5 proven on DEV — external execution |
| OCPilot | operational | External hosting/FTP |
| ORCA | operational | PPC toolkit — runtime **excluded** |
| MIG | operational | R1 narrow spine |
| Search PPC Production | operational (lifecycle) | Cross-system lifecycle gate — **NOT** autonomous engine |
| ATLAS / OPS | planned (foundation) | Docs only — not CRM/ERP |
| NOVA | planned | Methodology — not started |
| MetaBOT | operational (docs) | **External n8n** execution |
| HomeGateway | planned | Docs + prototype |
| GitGuard | operational (advisory) | Cross-cutting Survivability |
| X-drive paths | operational | X0–X9 complete — migration **CLOSED** (path reconciliation ≠ runtime) |

---

## Anti-mythology routers

| If chat claims… | Respond… |
|-----------------|----------|
| Registry row = deployed system | **EXCLUDED** — human-maintained intent |
| Path migration = new runtime | **EXCLUDED** — physical reconciliation only |
| Validator configured = auto-enforced | **EXCLUDED** — human-operated check only |
| Factory pack = running factory | **EXCLUDED** — methodology |

---

*End of 08_SYSTEM_MATURITY_MAP — X-Drive Pack 2026-06.*

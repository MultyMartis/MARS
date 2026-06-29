# MARS — Programme Registry Summary (X-Drive Pack 2026-06)

**SoT:** [registry/project-registry.md](../../registry/project-registry.md) — this file is a chat distillate; re-verify rows on conflict.

**Cross-cutting (not project_id rows):** GitGuard (Survivability), IdeaBox (`continuity/`), X-drive migration (infrastructure wave, not a project_id).

---

## Registered programmes

| project_id | Status | Maturity (honest) | Canonical entry | External boundary |
|------------|--------|-------------------|-----------------|-------------------|
| `mars-website-factory` | planned | Strategic methodology — **not** runtime factory | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Delivery via workspaces; no auto-deploy |
| `triumph-manipulator-landing` | planned | Website Factory production pack | `projects/triumph-manipulator-landing/README.md` | Workspace delivery, not deployed site |
| `orca` | active | Operational PPC toolkit — **EXCLUDED** runtime | `projects/orca/OPERATIONAL-INDEX.md` | Human-supervised review framework |
| `mig` | active | R1 groundtruth — narrow v0.1 spine | `projects/mig/OPERATIONAL-INDEX.md` | Acquires reality; ORCA interprets — human handoff only |
| `ocpilot` | active | OpenCart/ocStore ops pack | `projects/ocpilot/OPERATIONAL-INDEX.md` | **Sibling** to WPilot; live hosting external |
| `wpilot` | active | Reference CMS pilot — RC5 proven on DEV | `projects/wpilot/OPERATIONAL-INDEX.md` | Live WordPress on Beget DEV external |
| `ear-runtime` | active | R1 skeleton + config loader only | `projects/ear-runtime/OPERATIONAL-INDEX.md` | Architecture in `shared/external-access-runtime/` |
| `mars-survivability` | active | Contracts, protocols, human-invoked tools | `projects/mars-survivability/OPERATIONAL-INDEX.md` | **Not** automated enforcement |
| `nova` | planned | Mobile Factory methodology (RBM v1) | `projects/nova/README.md` | Implementation not started |
| `atlas` | planned | Foundation + population docs | `projects/atlas/OPERATIONAL-INDEX.md` | **Not** CRM/ERP; separate registries |
| `ops` | planned | Business ops domain foundation | `projects/ops/OPERATIONAL-INDEX.md` | **Not** CRM/ERP; ATLAS-consuming |
| `homegateway-v4-ai` | planned | Personal cockpit docs + UI prototype | `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md` | **Not** control plane |
| `metabot-seo-content-agent` | active | Canonical MetaBOT docs | `projects/metabot-seo-content-agent/README.md` | **External n8n** runtime |
| `seo-content-agent` | planned | **Legacy** — do not extend | `projects/seo-content-agent/` | Superseded by metabot pack |

---

## Infrastructure programmes (not all in registry rows)

| System | Entry | Role |
|--------|-------|------|
| MARS Localhost Infrastructure | `projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md` | `X:\MARS-Localhost\` governance |
| Forge WordPress / AG-WP-001 | `projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md` | Factory subsystem — **not** WPilot ownership |
| EAR Architecture | `shared/external-access-runtime/OPERATIONAL-INDEX.md` | Normative design — runtime in `ear-runtime` |
| Search PPC Production | `projects/mars-search-ppc-production/README.md` | Operational PPC production lane |

---

## Critical distinctions (preserve)

| Topic | Truth |
|-------|-------|
| Website Factory | Methodology + contracts — **≠** runtime factory engine |
| ATLAS / OPS | Documentation-layer registries — **≠** deployed CRM/ERP |
| MetaBOT | Execution is **external n8n** — in-repo docs only |
| WPilot / OCPilot | **Siblings** — separate CMS lanes |
| Forge WordPress / AG-WP-001 | Factory subsystem — **not** owned by WPilot |
| GitGuard | Cross-cutting Survivability layer — human-invoked/advisory |
| X-drive migration | Infrastructure wave X0–X9 — **not** a `project_id` |

---

## Storage / Localhost dependencies (verified current)

| Programme | Dependency |
|-----------|------------|
| OCPilot | Bulk under `X:\AI MARS STORAGE\ocpilot\` per external-storage-registry |
| WPilot | Local token path `X:\AI MARS\local\tokens\` (local-only) |
| MIG | Session exports may reference Storage incoming paths |
| MLI / Forge | Local Laragon at `X:\MARS-Localhost\` |

**SAFE UNKNOWN:** On-disk folder existence under Storage — verify in session.

---

*End of 03_PROGRAM_REGISTRY_SUMMARY — X-Drive Pack 2026-06.*

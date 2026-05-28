# Triumph — rules deprecation index (V6 rollout)

**Purpose:** Route agents to **one** active rule set without deleting historical docs.

**Canonical (active):** [`TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](TRIUMPH-V6-CURRENT-FRONTEND-RULES.md)

---

## Active

| Document | Use when |
|----------|----------|
| [`TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](TRIUMPH-V6-CURRENT-FRONTEND-RULES.md) | Any V6 workspace production task |
| [`V6-PAGE-ROLLOUT-PLAN.md`](V6-PAGE-ROLLOUT-PLAN.md) | Multi-page sequencing |
| `workspaces/triumph-manipulator-landing-v6/README.md` | Workspace identity + build |
| [`projects/mars-website-factory/russian-no-word-splitting-typography-v1.md`](../mars-website-factory/russian-no-word-splitting-typography-v1.md) | Generic RU typography (Triumph-specific overrides in V6 rules §E) |

---

## Deprecated for new work (reference / history only)

| Document | Was for | Conflict / note |
|----------|---------|-----------------|
| [`docs/TRIUMPH-FORGE-V2-FRONTEND-PRODUCTION-RULES.md`](docs/TRIUMPH-FORGE-V2-FRONTEND-PRODUCTION-RULES.md) | V2 workspace + old section order | Wrong workspace (`v2/`), wrong DOM markers |
| [`V2-CANONICAL-STATE.md`](V2-CANONICAL-STATE.md) | V2 paths | Points to `triumph-manipulator-landing-v2/` |
| [`V2-FRONTEND-SOURCE-OF-TRUTH.md`](V2-FRONTEND-SOURCE-OF-TRUTH.md) | V2 SoT | Superseded by V6 workspace |
| [`V2-FREEZE-STATE.md`](V2-FREEZE-STATE.md) | V2 freeze | Historical |
| [`V3-*`](.) (SOURCE-AUTHORITY, EXECUTION-BOUNDARIES, etc.) | V3 battle-test era | V4/V5/V6 stack not aligned |
| [`frontend-workspace.md`](frontend-workspace.md) | V1 path `workspaces/triumph-manipulator-landing/` | **Stale path** — see V6 README |
| [`frontend-agent-brief.md`](frontend-agent-brief.md) | Session brief | Update pointer to V6 rules before sessions |
| V5 reports under `workspaces/triumph-manipulator-landing-v5/reports/` | Hardening / mailer history | Some mention `backend/api/forms/send.php` — **obsolete**; V6 uses `send-lead.php` |

---

## Do not delete

Historical files stay in-repo for audit and ORCA lineage. Mark tasks with **active doc = TRIUMPH-V6-CURRENT-FRONTEND-RULES.md** in REPORT headers.

---

## Workspace map

| Version | Path | Status |
|---------|------|--------|
| V1 | `workspaces/triumph-manipulator-landing/` | Legacy |
| V2–V4 | `workspaces/triumph-manipulator-landing-v{2,3,4}/` | Historical |
| V5 | `workspaces/triumph-manipulator-landing-v5/` | Frozen mailer MVP source |
| **V6** | `workspaces/triumph-manipulator-landing-v6/` | **Active rollout** |

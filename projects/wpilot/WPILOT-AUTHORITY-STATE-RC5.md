# WPilot Authority State — RC5

**Classification:** Authority registration — canonical CMS Pilot runtime reference state.  
**Authority State:** `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19`  
**Date:** 2026-06-19  
**Scope:** Documentation only. No code, runtime, deploy, or Sprint 3 changes.

---

## Authority summary

| Field | Value |
|-------|-------|
| **Authority State** | `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19` |
| **Status** | **ACTIVE** — first proven CMS Pilot runtime reference implementation in MARS |
| **Commit** | `648632acbdd42703427fd76a0cb1fd8d88641dcc` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Release candidate** | `v0.3.0-RC5` |
| **Plugin version** | `0.3.0` (schema `0.2.0`) |
| **Registry `project_id`** | `wpilot` — [registry/project-registry.md](../../registry/project-registry.md) |

---

## Runtime maturity

| Maturity label | Meaning | RC5 status |
|----------------|---------|------------|
| `proven_content_writes` | Plugin REST write path with backup, validate, rollback on DEV | **PROVEN** |
| `proven_connection_runtime` | Authenticated REST bridge with connection tracking and operator visibility | **PROVEN** |

**Environment:** DEV only — `https://dev.gktriumph.ru`  
**Supervision model:** Human-supervised (HITL). Not autonomous. Not production.

**Canonical evidence:** [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md)  
**Release specification:** [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md)

---

## Proven surface

### Plugin REST runtime (formal)

| Surface | Endpoint family | Scope |
|---------|-----------------|-------|
| Inspect (read) | `GET /wp-json/wpilot/v1/*` read routes | Site info, pages, plugins, environment |
| Backup | `POST /wp-json/wpilot/v1/pages/{id}/backups` | `page.post_content` only |
| Apply | `POST /wp-json/wpilot/v1/pages/{id}/scoped-replace` | Exact-once replace on `page.post_content` |
| Validate | Checksum + post-write validation in apply/rollback responses | Per operation |
| Rollback | `POST /wp-json/wpilot/v1/pages/{id}/rollback` | Restore from plugin backup row |

**Proven targets (evidence v1):** page, shortcode, footer, css_fragment, environment, site — see Proven Capabilities register.

**Write primitive limit:** scoped exact-once replace on `page.post_content` only. Not menu, widget, CSS, footer endpoint, regex, or mass replace via plugin REST.

### Operator admin surface

| Surface | Purpose |
|---------|---------|
| MetaCODE WPilot admin dashboard | Runtime maturity, connection status, endpoint inventory, safety panels |
| Connection tab | Last Successful Connection, Last Endpoint, status labels |
| Russian localization | `ru_RU` PO/MO compiled |

### MARS connection surface

| Surface | Purpose |
|---------|---------|
| Local token file | `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` |
| Auth header | `X-WPilot-Token` |
| Connection tracker options | `last_authorized_connection_at`, `last_authorized_endpoint`, success/failure metadata |

**Never persisted in tracker:** token, headers, payloads, request bodies.

---

## Proven workflow

### Canonical safety loop (plugin REST)

```
inspect → backup → apply → validate → rollback
```

**Evidence:** Runtime Proof Sprint (backup + rollback 3/3 PASS); Runtime Prototype Sprint 2 (scoped-replace 3/3 PASS + rollback re-validation).

### Helper-based DEV workflows (pre-sprint / parallel path)

Human-supervised tasks on DEV also proved: inspect → backup → apply → validate; apply → validate → cleanup. These used temporary PHP helpers — distinct from formal plugin REST write API proof.

### Audit and checksum pipeline

- `wpilot_audit_log` lifecycle events per `operation_id`
- `sha256:` checksum on inspect, backup, apply, rollback
- WPBakery-safe full `post_content` recovery proven on pages 38, 69, 954

---

## Proven connection model

```
local token file
  → authenticated REST (X-WPilot-Token)
    → connection tracking (success/failure metadata)
      → operator visibility (admin Connection tab)
```

| Step | RC5 status | Evidence |
|------|------------|----------|
| MARS local token reaches bridge | **PROVEN** | RC3/RC4/RC5 connection reports; RC5 freeze |
| Authenticated REST accepted | **PROVEN** | Live DEV verification |
| Connection metadata persists | **PROVEN** | BUGFIX-01 + BUGFIX-02; RC5 operator-confirmed |
| Admin displays Last Successful Connection / Last Endpoint | **PROVEN** | RC5 operator-confirmed |

**Token policy:** [local-storage-policy.md](local-storage-policy.md)

---

## Known limits

| Limit | Meaning |
|-------|---------|
| **DEV only** | All proven apply/inspect/connection runs on `dev.gktriumph.ru` — not production evidence |
| **Single site** | One WordPress instance — no multisite proof |
| **Human-supervised** | Operator-initiated — not autonomous runtime |
| **Narrow write primitive** | Plugin REST write proven for `page.post_content` scoped-replace only |
| **Helper vs plugin REST** | Pre-sprint DEV tasks used temporary helpers; do not conflate with plugin REST proof |
| **Local STORAGE evidence** | Backup/validation bundles outside git by policy |
| **TEST-01 partial** | Clean ZIP install on disposable WordPress — **PARTIAL**; RC5 live on DEV is separate evidence |
| **Sprint 3 HOLD** | No new endpoints, no expansion without explicit HITL charter |
| **OCPilot parity** | WordPress evidence does not transfer to OpenCart |

**Not yet proven (selected):** production execution, autonomous execution, plugin REST writes for menu/widget/CSS/footer, clean ZIP install, multisite, `restore_backup` as distinct operation.

Full register: [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md) § Not Yet Proven.

---

## Freeze status

| Layer | Status |
|-------|--------|
| **RC5 authority freeze** | **ACTIVE** — 2026-06-19 |
| **Core Model v1** | **Stable** — no new architecture passes without explicit charter |
| **Plugin / runtime code** | **FROZEN** — no changes in RC5 authority pass |
| **Sprint 3** | **HOLD** |
| **New REST endpoints** | **EXCLUDED** |
| **Production deploy** | **EXCLUDED** |

**Freeze documents:**

- [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md)
- [reports/wpilot-state-freeze-2026-06-19.md](reports/wpilot-state-freeze-2026-06-19.md)

---

## Why RC5 matters

WPilot RC5 is the **first CMS Pilot runtime in MARS** with proven end-to-end operational discipline:

| Capability | RC5 meaning |
|------------|-------------|
| **inspect** | Read-only REST inspection of site state before any mutation |
| **backup** | Pre-apply backup with checksum before write |
| **apply** | Controlled scoped write with validation |
| **validate** | Post-write checksum and integrity checks |
| **rollback** | Proven restore from backup with re-validation |
| **connection tracking** | MARS local token → authenticated REST → persisted metadata → operator admin visibility |

Before RC5, WPilot existed as documentation, policy stack, and partial plugin source. RC5 establishes a **reference implementation** for the CMS Pilot family safety loop — not as “plugin MVP” marketing, but as **evidence-backed runtime maturity** on DEV.

**Family pattern (conceptual):** [projects/shared/runtime-patterns/CMS-PILOT-RUNTIME-PATTERN-v1.md](../shared/runtime-patterns/CMS-PILOT-RUNTIME-PATTERN-v1.md)  
**Sibling context:** [projects/ocpilot/cms-ecommerce-pilots-family.md](../ocpilot/cms-ecommerce-pilots-family.md)

---

## Explicit exclusions (normative)

| Excluded | Reason |
|----------|--------|
| MARS orchestration runtime | WPilot is External Systems lane — not MARS core runtime |
| Autonomous CMS administration | Human-supervised only |
| Production deployment | DEV scope until separately chartered |
| Sprint 3 | HOLD until explicit HITL charter |
| Token values in repo | Security baseline |

---

## Related authority documents

| Document | Role |
|----------|------|
| [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) | RC5 final state — Reference Implementation |
| [WPILOT-LIFECYCLE-STATE.md](WPILOT-LIFECYCLE-STATE.md) | Lifecycle state definitions |
| [WPILOT-MAINTENANCE-POLICY-v1.md](WPILOT-MAINTENANCE-POLICY-v1.md) | Post-RC5 maintenance policy |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | WPilot navigation index |
| [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md) | Evidence register |
| [ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-RC5-2026-06-19.md](ecosystem-sync/WPILOT-ECOSYSTEM-SYNC-RC5-2026-06-19.md) | Ecosystem sync note |
| [milestones/WPILOT-MILESTONE-001-FIRST-PROVEN-WRITE-PATH.md](milestones/WPILOT-MILESTONE-001-FIRST-PROVEN-WRITE-PATH.md) | First proven write milestone |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| RC5 clean ZIP install on disposable WordPress | **UNKNOWN** — TEST-01 PARTIAL |
| Exact RC5 proof timestamps in dedicated connection report | **UNKNOWN** — operator-confirmed; BUGFIX-02 report exists |
| Whether HEAD equals `648632ac…` at read time | Verify with `git rev-parse HEAD` when needed |
| Sprint 3 scope or charter | **Not claimed** — HOLD |

---

*WPilot Authority State RC5 · documentation authority registration · 2026-06-19.*

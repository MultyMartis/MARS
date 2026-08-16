# FP-0002 — Agent / System Responsibility Map v1

**Wave:** PROD-P02  
**Date:** 2026-08-13  
**Rule:** Ownership from current MARS topology — not analogy. No secret values.

---

## 1. FP-0002 / Site Ops contour

**Locus:** `X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\`

Owns:

- project-specific production operational state;
- production passport;
- access matrix;
- protected zones;
- change reports;
- source/runtime reconciliation;
- deployment scopes (exact-file allowlists);
- local credential **path** references (not values);
- DNS cutover status documentation.

Does **not** own: WPilot plugin source, Forge methodology product, generic remote connector runtime.

---

## 2. WPilot

**Locus:** `projects/wpilot/`  
**On this site:** migrated plugin `metacode-wpilot` (version unverified).

Owns:

- supported WordPress REST inspection and bounded entity operations;
- authentication / read / write gates (`bridge_enabled`, `write_enabled`, `dev_confirmed`);
- operation backups for supported mutations (Layer C), when a write gate exists.

Does **not** own:

- generic filesystem transport;
- all WordPress configuration;
- hosting;
- DNS;
- unrestricted DB operations;
- theme/plugin exact-file deploys.

---

## 3. Forge WordPress / AG-WP-001

**Locus:** `projects/mars-website-factory/subsystems/forge-wordpress/`  
**Agent:** AG-WP-001 — REGISTERED draft; **NOT RUNTIME-ACTIVE**; **NOT PRODUCTION READY**.

Role: methodology / engineering knowledge provider for WordPress factory work.

Does **not** become production owner of Shpigovsky Beget.

---

## 4. MARS Remote Operations / access layer

| Component | Evidence | Role for FP-0002 |
|-----------|----------|------------------|
| ROL `projects/remote-operations-layer/` | `MINIMAL_CHARTER` / L2 structured contract; **not implemented runtime** | Charter/checklist language only. **Not** used as SFTP/DB connector |
| EAR `projects/ear-runtime/` | Connector **SKELETON ONLY**; listing/manifest **MOCK ONLY**; **not live connector** | **Not** assigned as production filesystem/DB owner |
| Shared EAR architecture | Frozen architecture docs | Reference only |

**Conclusion:** filesystem and DB access for Shpigovsky are **operator / Cursor tool-mediated site operations**, not fictional autonomous MARS infrastructure.

---

## 5. Runtime checkout

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\runtime-checkouts\fp-0002-shpigovsky-production\repo` |
| Status | **DEFERRED** (no scheduled runtime yet) |
| Future use | Scheduled/read monitoring from **clean** checkout of `origin/mars/canonical-post-recovery` |
| Forbidden | Running such jobs from dirty `X:\AI MARS`; placing secrets inside the checkout |

---

## 6. Operator

Owns:

- entering credentials into local-only files;
- Beget panel HITL;
- confirming Layer A backups;
- DNS cutover when chartered;
- never pasting secrets into chat;
- rotation of passwords/tokens.

Does **not** transfer production mutation rights merely by filling files.

---

## 7. Responsibility matrix

| Concern | Owner | Support | Explicit non-owner |
|---------|-------|---------|--------------------|
| Production operational state / passport / matrix | FP-0002 Site Ops | Operator | WPilot, Forge, EAR |
| Protected zones / change model / backup model | FP-0002 Site Ops | Operator | — |
| Source (`WORDPRESS/`) vs live runtime reconciliation | FP-0002 Site Ops | Operator | WPilot (not a deploy tool) |
| Exact-file filesystem deploy | FP-0002 Site Ops + operator/Cursor tools | — | EAR, ROL, WPilot |
| WP Admin content/settings | Operator + chartered Site Ops | WPilot only for proven entity ops | Forge AG-WP-001 |
| WPilot REST read/write gates | WPilot programme + Site Ops charters | Operator | Forge, EAR |
| Hosting panel / backups create | Operator | Site Ops docs | Agents by default |
| DNS | Operator | Site Ops status docs | Everyone else |
| DB unrestricted / schema | Operator + explicit charter | — | WPilot, Forge |
| Runtime scheduled jobs | Future clean checkout | Site Ops | Dirty main worktree |
| Methodology / WP engineering patterns | Forge WordPress / AG-WP-001 | — | Production runtime |

---

*Responsibility Map v1 · PROD-P02 · topology from repo evidence.*

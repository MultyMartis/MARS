# Forge WordPress — Local Environment Decision v1

**Document type:** Environment decision record  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**Honesty:** Design decision only — **not** proof that any stack is installed on operator machines.

---

## 1. Purpose

Select canonical local WordPress development profiles for human-supervised Forge WordPress implementation, with **Windows compatibility** as a hard constraint (R-DEV-01).

---

## 2. Candidate comparison

| Criterion | Native Windows (Laragon / XAMPP) | Local (Flywheel) | DDEV | Docker Compose | wp-env | WP Playground | Playground CLI | Remote DEV | Staging-first |
|-----------|----------------------------------|------------------|------|----------------|--------|---------------|----------------|------------|---------------|
| **Windows compatibility** | **High** | **High** | Medium (WSL2/Docker) | Medium | Low (Docker) | **High** | **High** | **High** | **High** |
| **Setup cost** | Low–medium | Low | Medium–high | High | Medium | **Very low** | Low | Low (if exists) | Medium |
| **Reproducibility** | Medium | Medium | **High** | **High** | High | Medium | Medium | Low | Medium |
| **Agent compatibility** | **High** | **High** | Medium | Medium | Medium | **High** (sandbox) | **High** | Low (EAR) | Low |
| **Gulp compatibility** | **High** | **High** | **High** | **High** | **High** | Medium | Medium | **High** | **High** |
| **WP-CLI support** | **Full** | **Full** | **Full** | **Full** | **Full** | Limited | Limited | Host-dependent | Host-dependent |
| **Database support** | **Real MySQL/MariaDB** | **Real** | **Real** | **Real** | **Real** | In-memory / export | In-memory | **Real** | **Real** |
| **Shared hosting parity** | **High** (Beget-class) | **High** | Medium | Medium | Medium | Low | Low | **High** | **High** |
| **Isolation** | Medium | **High** | **High** | **High** | **High** | **High** | **High** | N/A | N/A |
| **Reset / rollback** | Medium | **High** | **High** | **High** | **High** | **High** | **High** | Low | Medium |
| **Team portability** | Medium | **High** | **High** | Medium | Medium | Medium | Medium | Low | Medium |

---

## 3. Rejected as mandatory default

| Candidate | Decision | Rationale |
|-----------|----------|-----------|
| **WordPress Playground (sole env)** | **REJECT** as default | No full theme/plugin lifecycle, limited WP-CLI, ACF sync, and shared-hosting parity |
| **Docker / DDEV (mandatory)** | **REJECT** as default | Not proven on current operator machine; disproportionate for studio static→theme projects |
| **wp-env** | **DEFER** | Docker dependency conflicts with Windows-first, low-friction baseline |
| **Staging-first only** | **REJECT** as Forge default | Pollutes shared DEV; violates local-first implementation discipline |

---

## 4. Adopted profiles

### 4.1 Default profile — **Local by Flywheel** (primary)

| Attribute | Value |
|-----------|-------|
| **Stack** | Local WP — isolated sites, nginx/Apache, MySQL, PHP |
| **Use** | Full Factory-native WordPress implementation (theme, ACF, custom plugin, WV2–WV9) |
| **Windows** | **Supported natively** |
| **WP-CLI** | Via Local shell or bundled terminal |
| **Gulp** | Frontend build runs **outside** Local; assets copied/synced into theme `assets/` |
| **Shared hosting parity** | PHP + MySQL + `.htaccess` patterns align with Beget-class hosts |
| **Install scope** | Per-operator machine; **not** in Git |
| **Evidence** | FW-01 ADOPT; operator-familiar per Research Base v1 |

**Fallback within default class:** **Laragon** portable if Local unavailable — same profile rules.

### 4.2 Lightweight profile — **WordPress Playground + static reference**

| Attribute | Value |
|-----------|-------|
| **Stack** | Playground (browser) or `@wp-playground/cli` |
| **Use** | Quick HTML smoke, agent sandbox, WV0 manifest checks, read-only structure preview |
| **Not for** | Full pilot implementation, ACF JSON workflow, PHPUnit, production packaging |
| **Gulp** | Compare `dist/` static output without full WP stack |

### 4.3 Legacy profile — **Remote DEV via WPilot boundary**

| Attribute | Value |
|-----------|-------|
| **Stack** | Existing Beget DEV (e.g. `dev.gktriumph.ru`) |
| **Use** | Legacy sites, post-handoff validation (FW-06), WPilot ChangeSet testing |
| **Not for** | Primary Forge implementation surface — EAR + production mutation risk |
| **Operator** | WPilot operations manifest; Forge produces package first |

### 4.4 Specialized profile — **Docker / DDEV**

| Attribute | Value |
|-----------|-------|
| **Trigger** | Explicit charter: multisite, complex service mesh, team CI mirror |
| **Approval** | Operator + Forge Architect |
| **Default** | **No** — opt-in only |

---

## 5. PHP version matrix (baseline)

| Context | PHP | Notes |
|---------|-----|-------|
| Local default | **8.1+** | Align with intake contract; 8.2 preferred for new pilots |
| Shared hosting target | **8.1** minimum | Beget-class; confirm per project passport |
| WordPress core | **6.4+** | LTS track; pin in project manifest |

MySQL/MariaDB: **10.4+** local; match host where known.

---

## 6. Multi-project isolation

| Rule | Definition |
|------|------------|
| **LOC-ZONE** | One Local site per Forge project slug |
| **Path** | `C:\Users\<user>\Local Sites\<project-slug>\` (Local default) — **not** in MARS Git |
| **MARS link** | Project passport references local URL + path in `local/` secrets (gitignored) |

---

## 7. DEV/staging sync boundary

| Action | Owner |
|--------|-------|
| Local implementation | Forge WordPress operator |
| DEV deploy / scoped replace | **WPilot** + operator |
| Production | **Forbidden** for Forge |

---

## 8. Current machine evidence

See [reports/FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md](reports/FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md) — **Local not detected** on audit host; default profile is **documented choice**, not installed state.

---

## Related

- [FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md)
- [FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md](FORGE-WORDPRESS-PILOT-TOOLING-PROFILE-v1.md)
- [reports/FORGE-WORDPRESS-FW-03-TOOLING-DECISION-RECORD-v1.md](reports/FORGE-WORDPRESS-FW-03-TOOLING-DECISION-RECORD-v1.md)

---

*Local environment decision v1 — profiles only; install is FW-04/FW-05 operator action.*

---

## Superseded note (2026-06-22 — MLI-01)

**Shared localhost policy** supersedes §4.1 **Local by Flywheel as primary shared runtime** for MARS studio operations:

| Topic | New policy |
|-------|------------|
| **Shared runtime provider** | MARS Localhost Infrastructure |
| **Shared runtime root** | `X:\MARS-Localhost` — [MLI OPERATIONAL-INDEX](../../../mars-localhost-infrastructure/OPERATIONAL-INDEX.md) |
| **Laragon root** | `X:\MARS-Localhost\laragon` |
| **WordPress site root** | `X:\MARS-Localhost\sites\wordpress\...` |
| **Primary local stack** | **Laragon** via MLI — **ENABLED** (MLI-01) |
| **Forge relationship** | **Consumer** — does **not** own infrastructure |
| **FW-05 historical** | Profile B (Playground) proof remains valid |
| **FW-05R** | **HOLD** until MLI-03 WordPress runtime profile + PHP/WP-CLI/PHPCS availability |

Local by Flywheel remains an **optional alternative** per-operator if chartered.

**Forge WordPress does not own `X:\MARS-Localhost`. It consumes the WordPress runtime profile provided by MARS Localhost Infrastructure.**

See: [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](../../../mars-localhost-infrastructure/MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md)

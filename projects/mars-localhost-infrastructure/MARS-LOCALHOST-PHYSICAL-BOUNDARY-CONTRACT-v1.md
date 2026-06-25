# MARS Localhost — Physical Boundary Contract v1

**Document type:** Physical boundary contract  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00
**Post-cutover note (2026-06-25):** Active brain root `C:\MARS Phenix\AI MARS`; active runtime root `E:\MARS-Localhost`. MLI-00 audit table below preserves historical `D:\` observations.

---

## Scope

This contract defines **what may live where** between the MARS brain zone (`C:\MARS Phenix\AI MARS`) and the shared local runtime zone (`E:\MARS-Localhost`). It is operator-authoritative for localhost infrastructure and complements [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md).

---

## Brain zone — `C:\MARS Phenix\AI MARS`

### Allowed (permanent)

| Category | Examples |
|----------|----------|
| Source documents | Identity, standards, policies, roadmaps |
| Architecture | MLI contracts, consumer model, Laragon decision |
| Project orchestration | Runtime manifest **pointers**, enablement inputs |
| Git | Repository source of truth |
| Capability packs | Forge WordPress, OCPilot methodology (docs) |
| Manifests | `projects/mars-localhost-infrastructure/manifests/*.json` or `*.md` |
| Pointers | Paths, URLs, database IDs — **not** secrets |
| Lightweight validation reports | Summaries, smoke results, audit reports |

### Forbidden as permanent runtime

| Category | Correct location |
|----------|------------------|
| WordPress core | `E:\MARS-Localhost\sites\wordpress\` |
| OpenCart / ocStore core | `E:\MARS-Localhost\sites\opencart\` |
| Live databases / MySQL data files | `E:\MARS-Localhost\databases\` |
| Uploads / media runtime | `E:\MARS-Localhost\storage\uploads\` or site `wp-content/uploads` |
| Caches (runtime) | `E:\MARS-Localhost\` site or `temp\` |
| Apache / Nginx binaries and live config | `E:\MARS-Localhost\runtime\laragon\` |
| MySQL/MariaDB data directory | `E:\MARS-Localhost\runtime\laragon\` (post MLI-01) |
| Large runtime logs | `E:\MARS-Localhost\logs\` |
| Generated local backups (primary) | `E:\MARS-Localhost\backups\` |

### Brain may reference runtime

Manifests, passports, and reports in `C:\MARS Phenix\AI MARS` **must** record canonical pointers to `E:\MARS-Localhost` paths without copying runtime artefacts into Git.

---

## Runtime zone — `E:\MARS-Localhost`

### Allowed

| Category | Examples |
|----------|----------|
| Local servers | Laragon stack (post MLI-01) |
| CMS runtime | WordPress, OpenCart/ocStore, generic PHP sites |
| Databases | Active DBs, dumps workspace, baselines, temp import |
| Uploads | Site media, import staging |
| Caches | Opcode, object cache files, compiled assets |
| Generated assets | Built theme assets synced for local preview |
| Temporary packages | Import ZIPs, scratch extracts in `temp\` |
| Runtime backups | Site + DB snapshots before major changes |
| Synthetic sites | Validation cases without client data |
| Tooling install roots | Composer, WP-CLI, PHPCS, Playwright (under `tools\`) |
| Certificates | Local TLS material |
| Logs | Apache, Nginx, PHP, MySQL, application logs |

### Forbidden as canonical authority

| Category | Correct location |
|----------|------------------|
| Governance | `C:\MARS Phenix\AI MARS\governance\` |
| Agent definitions | `C:\MARS Phenix\AI MARS\agents\` |
| Standards (SoT) | Consumer packs under `C:\MARS Phenix\AI MARS\projects\` |
| Roadmaps (SoT) | Program roadmaps in brain |
| Registries (SoT) | `C:\MARS Phenix\AI MARS\registry\`, project registries |
| Project truth / passports (SoT) | `C:\MARS Phenix\AI MARS\projects\`, `workspaces\` |
| Git history | `C:\MARS Phenix\AI MARS` only |

Runtime zone files are **execution artefacts**. Authoritative project truth remains in the brain unless explicitly chartered otherwise (e.g. OCPilot bulk under MARS STORAGE).

---

## Cross-zone rules

| ID | Rule |
|----|------|
| **PB-01** | Every registered local runtime has a manifest pointer in `C:\MARS Phenix\AI MARS` |
| **PB-02** | Secrets never committed to Git; live credentials live outside docs |
| **PB-03** | `E:\MARS-Localhost` is **never** a git repository for MARS |
| **PB-04** | MARS brain is **never** relocated to E: for governance or Git |
| **PB-05** | Bulk archives may mirror to `C:\MARS Phenix\AI MARS STORAGE` but live runtime stays on E: |
| **PB-06** | Historical reports preserve point-in-time paths; supersede via addendum, not silent rewrite |

---

## Pre-existing runtime paths (MLI-00 audit — historical)

| Observation | Classification |
|-------------|----------------|
| `D:\MARS-Localhost\` root exists (operator-created) | **Confirmed** (MLI-00; pre Windows reinstall) |
| `D:\MARS-Localhost\laragon\` at root (pre-standard) | **Pre-existing** — canonical target is `runtime\laragon\`; reconcile during **MLI-01**, do not delete in MLI-00 |
| Contents of pre-existing `laragon\` | **SAFE UNKNOWN** — empty or placeholder at audit time |

---

## Post-cutover runtime confirmation (2026-06-25)

| Observation | Classification |
|-------------|----------------|
| `E:\MARS-Localhost\` root exists | **Confirmed** — active operator runtime after drive-letter reconciliation |
| Historical `D:\MARS-Localhost` in MLI-03R.* reports | **Preserved** — incident evidence; no global rewrite |

---

## Related

- [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md)
- [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)
- [MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md](MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md)
- [governance/mars-phoenix-recovery-cutover-receipt-v1.md](../../governance/mars-phoenix-recovery-cutover-receipt-v1.md)

---

*Physical boundary contract v1 — MLI-00; Phoenix path reconciliation 2026-06-25.*

# OCPilot Baselines



**Purpose:** versioned **reference** OpenCart / ocStore installs for comparison with project sites.



## Versioned baselines (preferred)



| Path | Platform / version |

|------|-------------------|

| [opencart-230/](opencart-230/) | OpenCart 2.3.0 |

| [opencart-3037/](opencart-3037/) | OpenCart 3.0.3.7 |

| [opencart-4x/](opencart-4x/) | OpenCart 4.x |

| [ocstore-230/](ocstore-230/) | ocStore 2.3.0 |

| [ocstore-3037/](ocstore-3037/) | ocStore 3.0.3.7 |

| [ocstore-3038-rs2/](ocstore-3038-rs2/) | ocStore 3.0.3.8 (rs.2) — **priority** |

| [ocstore-3039-rs1/](ocstore-3039-rs1/) | ocStore 3.0.3.9 (rs.1) — **priority** |



## Priority first baselines (operator real targets)

1. **ocstore-3038-rs2** — ocStore 3.0.3.8 (rs.2)
2. **ocstore-3039-rs1** — ocStore 3.0.3.9 (rs.1)

Existing **ocstore-3037** remains useful as older reference, but is **not** first priority for new OCPilot work.

Each version folder uses the subfolder contract below. Empty folders are **valid** at this stage — operator uploads baseline in **Run 3 — First Baseline Acquisition**.



## Subfolder contract (every versioned baseline)



| Folder | Purpose |

|--------|---------|

| `files/` | Sanitized vendor file tree (OpenCart or ocStore core files) |

| `database/` | Schema metadata, table descriptions, prefix notes — not live dumps |

| `notes/` | Version notes, source, exclusions, operator commentary |

| `manifest/` | File manifests, directory maps, checksum labels |

| `passports/` | Completed [versioned-baseline-passport-template.md](../templates/versioned-baseline-passport-template.md) per baseline revision |

| `comparison-notes/` | Known differences vs upstream OpenCart or between ocStore builds |



Before comparison use → [baseline-readiness-checklist.md](../baseline-readiness-checklist.md).



## Legacy placeholder



| Path | Role |

|------|------|

| [clean-opencart/](clean-opencart/) | **Legacy / generic placeholder** from Phase 0 — not the preferred target. Use versioned folders above for new work. |



## Rules



- No secrets, no live `config.php`, no customer data dumps in git.

- If required readiness checks fail, OCPilot must ask the operator to provide baseline materials — **do not silently continue**.

- Full raw DB dumps should not be committed unless explicitly approved and sanitized.

- Forbidden: `config.php`, `admin/config.php`, storage configs, credentials, tokens.

- Do not overwrite an old baseline without noting supersession in `notes/` and a new passport in `passports/`.



## Documentation (Run 2)



| Doc | Role |

|-----|------|

| [baseline-storage-model.md](../baseline-storage-model.md) | What belongs in a baseline |

| [templates/versioned-baseline-passport-template.md](../templates/versioned-baseline-passport-template.md) | Standard passport |

| [baseline-comparison-methodology.md](../baseline-comparison-methodology.md) | Layered comparison model |

| [baseline-readiness-checklist.md](../baseline-readiness-checklist.md) | Can this baseline be used? |

| [clean-opencart-baseline.md](../clean-opencart-baseline.md) | Why baseline exists (Run 1.5) |



## Status



- **Run 1.5:** versioned folder structure in place.

- **Run 2:** ingestion model, passport template, comparison methodology, readiness checklist, extended subfolders — **DONE**.

- **Run 2.6:** priority target version baseline folders (`ocstore-3038-rs2`, `ocstore-3039-rs1`) — **DONE**.

- **Run 3:** first operator upload of actual baseline files for priority targets — **planned**.



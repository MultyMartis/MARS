# MARS Localhost — Directory Standard v1

**Document type:** Directory layout standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00  
**Runtime root:** `D:\MARS-Localhost`

---

## Purpose

Define a **universal** localhost directory layout supporting WordPress, OpenCart/ocStore, generic PHP, synthetic validation, and future runtime consumers — without WordPress-centric coupling.

---

## Canonical structure

```text
D:\MARS-Localhost\
├── README.md
├── runtime\
│   └── laragon\                 # Laragon install root (MLI-01)
├── sites\
│   ├── wordpress\
│   │   ├── synthetic\           # e.g. fws-0001
│   │   ├── projects\            # e.g. shpigovsky
│   │   └── sandboxes\
│   ├── opencart\
│   │   ├── synthetic\           # e.g. ocs-0001
│   │   ├── projects\            # e.g. bzpm, sibcar
│   │   └── sandboxes\
│   ├── php\
│   │   ├── synthetic\           # e.g. web-sim-0001
│   │   ├── projects\
│   │   └── sandboxes\
│   └── other\
│       ├── synthetic\
│       ├── projects\
│       └── sandboxes\
├── databases\
│   ├── active\                  # metadata / connection notes only if needed
│   ├── dumps\
│   ├── baselines\
│   └── temp\
├── storage\
│   ├── uploads\
│   ├── imports\
│   ├── exports\
│   ├── packages\
│   └── fixtures\
├── backups\
│   ├── wordpress\
│   ├── opencart\
│   ├── databases\
│   └── runtime\
├── logs\
│   ├── apache\
│   ├── nginx\
│   ├── php\
│   ├── mysql\
│   └── applications\
├── tools\
│   ├── composer\
│   ├── wp-cli\
│   ├── phpcs\
│   ├── playwright\
│   └── utilities\
├── certificates\
├── temp\
└── archive\
```

---

## Design rationale

| Concern | How this layout addresses it |
|---------|-------------------------------|
| **Laragon compatibility** | `runtime\laragon\` isolates stack; document root points to `sites\` (see Laragon decision) |
| **Backup simplicity** | `backups\` + `databases\dumps\` + per-site folders are predictable |
| **Cursor clarity** | Platform → class → slug path is stable across consumers |
| **WordPress** | `sites\wordpress\{class}\{slug}\` with optional `public\` or docroot per Laragon vhost |
| **OpenCart** | `sites\opencart\{class}\{slug}\` mirrors WordPress pattern |
| **Generic PHP** | `sites\php\` avoids CMS-specific assumptions |
| **Future consumers** | `sites\other\` or new platform sibling under `sites\` |

---

## Path conventions

| Element | Rule |
|---------|------|
| **Slugs** | lowercase, latin, kebab-case or compact id (`fws-0001`, `shpigovsky`) |
| **Site root** | `D:\MARS-Localhost\sites\{platform}\{class}\{slug}\` |
| **No spaces** | In paths and folder names |
| **Manifest link** | Brain manifest records full local path + URL |

---

## Laragon document root

**Preferred:** `D:\MARS-Localhost\sites` as Laragon document root (virtual hosts map to subpaths). See [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md).

---

## MLI-00 deviation note

Operator pre-created `D:\MARS-Localhost\laragon\` at **root** before this standard. Canonical target is `runtime\laragon\`. **Do not delete** root `laragon\` in MLI-00; reconcile during MLI-01 enablement.

---

## Not in this tree

| Item | Location |
|------|----------|
| Governance docs | `C:\AI MARS\projects\mars-localhost-infrastructure\` |
| Runtime manifests (SoT) | `C:\AI MARS\projects\mars-localhost-infrastructure\manifests\` |
| Large archived ZIPs (optional) | `C:\AI MARS STORAGE\{consumer}\` |
| MARS Git | `C:\AI MARS` only |

---

## Related

- [MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md](MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md)
- [MARS-LOCALHOST-DOMAIN-STANDARD-v1.md](MARS-LOCALHOST-DOMAIN-STANDARD-v1.md)
- [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md)

---

*Directory standard v1 — MLI-00.*

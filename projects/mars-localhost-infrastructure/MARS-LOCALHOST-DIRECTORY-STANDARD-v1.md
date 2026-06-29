# MARS Localhost — Directory Standard v1

**Document type:** Directory layout standard  
**Version:** v1.1  
**Date:** 2026-06-22  
**Stage:** MLI-01 (updated from MLI-00)  
**Runtime root:** `X:\MARS-Localhost`

---

## Purpose

Define a **universal** localhost directory layout supporting WordPress, OpenCart/ocStore, generic PHP, synthetic validation, and future runtime consumers — without WordPress-centric coupling.

---

## Canonical structure

```text
X:\MARS-Localhost\
├── README.md
├── laragon\                     # Laragon install root (canonical — MLI-01)
├── runtime\
│   └── laragon\                 # DEPRECATED EMPTY PLACEHOLDER (do not use)
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
| **Laragon compatibility** | `laragon\` at D: root; `www\` = junction/vhost registry; physical sites in `sites\` |
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
| **Site root** | `X:\MARS-Localhost\sites\{platform}\{class}\{slug}\` |
| **No spaces** | In paths and folder names |
| **Manifest link** | Brain manifest records full local path + URL |

---

## Laragon document root

**Model:** Physical sites in `X:\MARS-Localhost\sites`; Laragon `www\` holds slug junctions; explicit vhosts in registry. See [MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md](MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md).

---

## MLI-00 → MLI-01 path note

MLI-00 proposed `runtime\laragon\`. Operator installed at `X:\MARS-Localhost\laragon\` before enablement. **Canonical path reconciled in MLI-01** — see [MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md](MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md). `runtime\laragon\` is an empty deprecated placeholder.

---

## Not in this tree

| Item | Location |
|------|----------|
| Governance docs | `X:\AI MARS\projects\mars-localhost-infrastructure\` |
| Runtime manifests (SoT) | `X:\AI MARS\projects\mars-localhost-infrastructure\manifests\` |
| Large archived ZIPs (optional) | `X:\AI MARS STORAGE\{consumer}\` |
| MARS Git | `X:\AI MARS` only |

---

## Related

- [MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md](MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md)
- [MARS-LOCALHOST-DOMAIN-STANDARD-v1.md](MARS-LOCALHOST-DOMAIN-STANDARD-v1.md)
- [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md)

---

*Directory standard v1 — MLI-00.*

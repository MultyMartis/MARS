# Forge WordPress — Repository and Filesystem Model v1

**Document type:** Storage and repository architecture  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

---

## 1. Purpose

Define where Forge WordPress source, assets, validation evidence, and runtime boundaries live across MARS workspace, bulk storage, client workspaces, local WordPress, and external hosting.

---

## 2. Model comparison

| Model | Pros | Cons | Decision |
|-------|------|------|----------|
| **Mono-repo (MARS + WP core)** | Single clone | Core/vendor bloat; violates hosting reality | **REJECT** |
| **Frontend repo + WP repo** | Clean separation | Handoff drift; two remotes | **ADOPT** (logical split, linked by manifest) |
| **Static package → WP repo** | Clear Factory boundary | Extra sync step | **ADOPT** (handoff artifact) |
| **Theme-only repo** | Simple deploy | Misses plugin/ACF | **Partial** — theme subfolder of WP project |
| **Full WP project repo** | Complete picture | Core/uploads noise | **ADOPT** as implementation workspace |

**Baseline:** **Factory frontend workspace** + **WordPress implementation workspace** (theme + functionality plugin + ACF JSON), linked by handoff manifest — **not** a single monorepo with WordPress core.

---

## 3. Canonical layout (Factory-native project)

```text
C:\AI MARS\
  workspaces\website-factory-operations\{FP-ID}\
    INCOMING\                    # design, branding (existing)
    FRONTEND\                    # Gulp client copy — src/, dist/, package.json
    WORDPRESS\                   # Forge implementation workspace (FW-05+)
      theme\{slug}\              # PHP templates, inc/, acf-json symlink target
      plugin\{slug}-functionality\
      docs\                      # WAD, maps, validation reports
      tooling\                   # phpcs.xml, playwright config (future)
      .env.example               # no secrets
    REPORTS\                     # cross-cutting QA

C:\AI MARS STORAGE\
  forge-wordpress\{FP-ID}\
    visual-baselines\            # reference + diff PNGs (bulk)
    db-dumps\                    # local export snapshots (optional)
    release-packages\            # ZIP artifacts + checksums

C:\Users\<user>\Local Sites\{project-slug}\   # Local WP runtime — NOT in Git
  app\public\wp-content\
    themes\{slug}\
    plugins\{slug}-functionality\
```

---

## 4. Artifact placement rules

| Artifact | Git in MARS | STORAGE | Local WP | Notes |
|----------|-------------|---------|----------|-------|
| Approved static frontend `src/` | **Yes** (`FRONTEND/`) | — | — | Source of truth |
| `dist/` build output | **Yes** (committed or CI artifact) | Optional mirror | Synced copy in theme | **Not** source of truth |
| Theme PHP source | **Yes** (`WORDPRESS/theme/`) | — | Symlink or deploy copy | |
| Compiled theme assets | **Yes** (from Gulp) | — | `theme/assets/` | Built, not hand-edited |
| Custom plugins | **Yes** | — | `plugins/` | |
| ACF JSON | **Yes** (`acf-json/` in theme or plugin) | — | Synced | Version-controlled |
| Project documentation | **Yes** | — | — | Linked to MARS governance |
| Environment config | `.env.example` only | — | `local/` gitignored | Secrets **never** in Git |
| Validation artifacts | Summary in `REPORTS/` | Full diffs/screenshots | — | |
| Screenshots / visual diffs | Thumbnails optional | **Primary** bulk path | — | |
| Release packages | Manifest + checksum in Git | ZIP binaries | — | |
| Database dumps | **No** default | **Yes** if retained | Ephemeral | |
| Local secrets / tokens | **No** | **No** | `C:\AI MARS\local\` | WPilot policy |
| Temporary files | **No** | Optional scratch | OS temp | |
| WordPress core | **No** | **No** | Local install | |
| `vendor/` (Composer) | Lock yes; vendor optional | — | `composer install` | |
| `uploads/` | **No** | Media export if needed | Local only | |

---

## 5. Hard rules

| ID | Rule |
|----|------|
| **R-FS-01** | `dist` is **never** source of truth — `src` + build command is |
| **R-FS-02** | Compiled assets live in theme `assets/` (or agreed path); separated from PHP source tree |
| **R-FS-03** | WordPress core, uploads, DB dumps **not** committed without explicit charter |
| **R-FS-04** | Secrets outside Git — `C:\AI MARS\local\` or operator secret store |
| **R-FS-05** | Core **not** duplicated per project repo |
| **R-FS-06** | MARS docs govern methodology; production delivery locus may be host panel (WPilot) |

---

## 6. Boundary map

```text
C:\AI MARS              → methodology, source, manifests, reports (Git)
C:\AI MARS STORAGE      → bulk baselines, packages, dumps (out-of-git)
client workspace        → workspaces/website-factory-operations/{FP-ID}/
local WordPress runtime → Local Sites / Laragon (operator machine)
external hosting        → Beget DEV/staging/prod (WPilot operations)
```

---

## 7. Git strategy

| Repo object | Strategy |
|-------------|----------|
| Factory frontend | Existing client Gulp copy under `FRONTEND/` |
| WordPress implementation | Subtree under same FP folder or separate remote **TBD per pilot** |
| Handoff linkage | `FRONTEND-HANDOFF` manifest: SHA, build command, asset map |
| WPilot handoff | Release package + manifest — not live site Git |

---

## Related

- [governance/mars-infrastructure-reality-v1.md](../../../../governance/mars-infrastructure-reality-v1.md)
- [FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md](FORGE-WORDPRESS-GULP-INTEGRATION-MODEL-v1.md)
- [contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md)

---

*Repository model v1 — design only.*

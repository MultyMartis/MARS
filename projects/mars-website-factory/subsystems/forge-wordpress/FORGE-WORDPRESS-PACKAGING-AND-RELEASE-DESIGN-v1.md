# Forge WordPress — Packaging and Release Design v1

**Document type:** Release artifact specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**Release Candidate ≠ deployment.**

---

## 1. Package types

| Package | Contents | Consumer |
|---------|----------|----------|
| **Theme source** | PHP, `template-parts/`, `acf-json/`, unminified assets optional | Git / review |
| **Theme deploy artifact** | ZIP: PHP + built `assets/` — no `node_modules`, `.scss` sources optional per manifest | WPilot / host |
| **Plugin source** | Custom functionality plugin tree | Git |
| **Plugin artifact** | ZIP excluding dev files | WPilot |
| **ACF JSON** | In theme or plugin path | Sync on deploy |
| **WPilot handoff bundle** | ZIPs + manifests + WV reports | WPilot operator |

---

## 2. RELEASE-MANIFEST fields

Per [templates/FORGE-WORDPRESS-RELEASE-MANIFEST-TEMPLATE-v1.md](templates/FORGE-WORDPRESS-RELEASE-MANIFEST-TEMPLATE-v1.md):

- `project_id` / FP reference
- `version` (semver)
- `git_revision` (SHA)
- `build_timestamp`
- `theme_version` / `plugin_version`
- `checksums` (SHA-256 per ZIP)
- `dependency_manifest` (npm, composer, WP plugins)
- `environment_requirements` (PHP, WP, MySQL)
- `validation_reports` (WV0–WV9 index)
- `screenshots` (reference paths)
- `known_limitations`
- `production_mode`
- `wp_debug_expected: false`

---

## 3. Naming and versioning

| Artifact | Pattern |
|----------|---------|
| Theme ZIP | `{slug}-theme-{version}.zip` |
| Plugin ZIP | `{slug}-functionality-{version}.zip` |
| Handoff bundle | `{fp-id}-forge-wp-handoff-{version}.zip` |
| Version | Semver — bump on release candidate |

---

## 4. Build flow

```text
build_frontend_assets
  → package_theme
  → package_functionality_plugin (if any)
  → build_release_manifest
  → wv9-package-lint
  → prepare_wpilot_handoff
```

**Stop point:** Forge WordPress Release Candidate delivered to operator — **WPilot applies** to DEV/staging.

---

## 5. Explicit exclusions

- Production deploy pipeline
- FTP/autonomous upload
- Live search-replace

---

## Related

- [contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md)
- [FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md)

---

*Packaging design v1 — stops before deploy.*

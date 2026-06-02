# Site Template (`_template-site`)

Copy this folder to `sites/<site-slug>/` when onboarding a project site (Run 3).

## Folder map

| Subfolder | Use |
|-----------|-----|
| `materials/` | Source materials from operator (sanitized briefs, path lists, screenshots without secrets) |
| `audits/` | General audit outputs |
| `opencart-analysis/` | OpenCart version, core structure, theme layout findings |
| `catalog-analysis/` | Categories, products, attributes, filters, options |
| `extension-analysis/` | Modules, extensions, ocMod, vQmod if present |
| `theme-analysis/` | Templates, layouts, theme overrides |
| `controller-analysis/` | Controllers, models, language files touched by project logic |
| `seo-url-analysis/` | SEO URLs, redirects, aliases, route mapping |
| `database-analysis/` | Schema observations, table map, safe metadata only |
| `import-planning/` | Future catalog import plans — no uncontrolled import files in repo |
| `backups/` | Backup references or sanitized backup metadata (`files/`, `database/`) |
| `snapshots/` | Sanitized file/database snapshots or manifests (`files/`, `database/`) |
| `tasks/` | Scoped task files |
| `reports/` | `# REPORT — …` outputs |
| `safe-unknown/` | Unresolved findings and questions |
| `qa/` | QA checklists and results |

## Rules

- No secrets. No live credentials.
- No raw production dumps unless explicitly approved and sanitized.
- Do not rename `_template-site` in place for a real client — always copy.

## Baseline compare

During audit, compare site evidence to the matching versioned baseline under [baselines/](../../baselines/README.md). Document delta in `opencart-analysis/` and audit reports.

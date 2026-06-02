# OCPilot — Project Sites Workflow

**Scope:** куда класть материалы по каждому OpenCart dealership / project site.

## Layout

```
projects/ocpilot/sites/
  README.md
  <site-slug>/          # copy from _template-site/
    materials/
    audits/
    opencart-analysis/
    catalog-analysis/
    extension-analysis/
    theme-analysis/
    controller-analysis/
    seo-url-analysis/
    database-analysis/
    import-planning/
    backups/files|database/
    snapshots/files|database/
    tasks/
    reports/
    safe-unknown/
    qa/
```

## Intake (Run 3)

1. Operator chooses **site-slug** (lowercase, hyphenated; no secrets in name).
2. Copy `_template-site/` → `sites/<site-slug>/`.
3. Fill [templates/project-site-passport-template.md](templates/project-site-passport-template.md) → store in `materials/` or `reports/`.
4. Never commit credentials into any subfolder.

## Folder semantics

| Folder | Contents |
|--------|----------|
| `materials/` | Source materials from operator — sanitized briefs, path lists, screenshots **without** secrets |
| `audits/` | General audit outputs, checklists |
| `opencart-analysis/` | OpenCart version, core structure, theme layout findings |
| `catalog-analysis/` | Categories, products, attributes, filters, options |
| `extension-analysis/` | Modules, extensions, ocMod, vQmod if present |
| `theme-analysis/` | Templates, layouts, theme overrides |
| `controller-analysis/` | Controllers, models, language files touched by project logic |
| `seo-url-analysis/` | SEO URLs, redirects, aliases, route mapping |
| `database-analysis/` | Schema observations, table map, safe metadata only |
| `import-planning/` | Future catalog import plans — **no** uncontrolled import files in repo |
| `backups/` | **Metadata only** in repo — real backups live external/local operator storage |
| `snapshots/` | Sanitized file/database snapshots or manifests; binary snapshots external |
| `tasks/` | Scoped task cards, change requests (links to templates) |
| `reports/` | `# REPORT — …` artifacts per run |
| `safe-unknown/` | Unresolved findings and questions blocking progress |
| `qa/` | QA checklists and results |

## Secrets policy

- **No** passwords, tokens, `config.php`, SQL dumps in repo.
- Credentials **outside** repo; passport records access *class* only.
- No raw production dumps unless explicitly approved and sanitized.

## Baseline Selection

Before read-only audit (Run 5), select and verify the matching versioned baseline.

**Workflow:**

1. **Identify platform** — OpenCart or ocStore (admin footer, operator brief, version file).
2. **Identify version** — exact release line (e.g. 3.0.3.7, 2.3.0, 4.x minor pin).
3. **Select matching baseline** — map to folder under [baselines/](baselines/README.md):

   | Project site | Baseline folder |
   |--------------|-----------------|
   | OpenCart 2.3.x | `baselines/opencart-230/` |
   | OpenCart 3.0.3.7 | `baselines/opencart-3037/` |
   | OpenCart 4.x | `baselines/opencart-4x/` |
   | ocStore 2.3.x | `baselines/ocstore-230/` |
   | ocStore 3.0.3.7 | `baselines/ocstore-3037/` |

4. **Verify baseline readiness** — run [baseline-readiness-checklist.md](baseline-readiness-checklist.md). Required: passport, files, manifest. Optional: DB metadata, comparison notes.
5. **Start audit** — compare per [baseline-comparison-methodology.md](baseline-comparison-methodology.md); record deltas in site analysis folders and audit report.

**If baseline unavailable** (wrong version, empty folder, readiness fail):

- Record **SAFE UNKNOWN** in `sites/<slug>/safe-unknown/`.
- Request baseline creation or upload — **Run 3 — First Baseline Acquisition**.
- **Do not silently continue** with comparison claims.

## Relation to baseline

During audit, compare site evidence to the **matching versioned** baseline selected above. Document delta in `opencart-analysis/`, relevant analysis folders, and audit report.

## External access

Human-supervised access patterns: [shared/external-access-patterns/](../../shared/external-access-patterns/README.md).

## Forbidden

- Using `sites/` as production deploy target.
- Storing payment card or customer PII exports.

## Template site

`_template-site/` is not a live site — structure reference only. Do not run operations against `_template-site` as if it were production.

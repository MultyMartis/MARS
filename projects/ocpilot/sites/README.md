# OCPilot Project Sites

Per-site workspaces for OpenCart dealership / client projects.

## Create a site

1. Copy `_template-site/` → `<site-slug>/`.
2. Register in [project-site-registry.md](../project-site-registry.md).
3. Create external bulk root: `C:\AI MARS STORAGE\ocpilot\project-sites\<site-slug>\`.
4. Follow [project-sites-workflow.md](../project-sites-workflow.md).
5. Fill [site-passport.md](site-001/site-passport.md) per [site-passport-standard.md](../site-passport-standard.md).

**First site (Run 4):** [site-001/](site-001/) — SITE-001.

**Second site (Run 4.113):** [site-002/](site-002/) — SITE-002 (ЗПМ), **AWAITING INTAKE**.

## Analysis zones (OpenCart-specific)

Each site folder includes dedicated analysis areas beyond general `materials/` and `audits/`:

| Folder | Purpose |
|--------|---------|
| `opencart-analysis/` | Version, core, theme structure |
| `catalog-analysis/` | Categories, products, attributes, filters |
| `extension-analysis/` | Modules, ocMod, vQmod |
| `theme-analysis/` | Templates, layouts, overrides |
| `controller-analysis/` | Controllers, models, language deltas |
| `seo-url-analysis/` | SEO URLs, redirects, aliases |
| `database-analysis/` | Schema map, safe metadata |
| `import-planning/` | Catalog import plans (no uncontrolled import files) |
| `qa/` | QA checklists and results |

See `_template-site/README.md` for full folder map.

## Rules

- One folder per site under `sites/`.
- No credentials or DB dumps in repo.
- Real backups and snapshots live **outside** git; repo holds metadata only.

## Template

`_template-site/` — structural reference, not a production target.

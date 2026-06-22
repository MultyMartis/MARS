# FW-SK-10 — WordPress Code Implementation v1

**Skill ID:** FW-SK-10  
**Stage:** FW-04 capability

## Purpose
Implement approved WordPress theme and functionality plugin locally per specification.

## When to use
- After approved implementation spec (FW-SK-09)
- Local environment available (FW-05+)

## Prerequisites
- Approved implementation spec
- Approved WAD, content model, maps
- Filesystem scope declared
- Safe command policy loaded

## Inputs
- Implementation spec
- Read-only approved frontend source
- ACF schema, CPT map, theme architecture

## Outputs
- Theme files (complete)
- Functionality plugin files (complete)
- ACF Local JSON
- CPT/taxonomy registration
- Enqueued assets integrated

---

## Allowed implementation

| Category | Allowed |
|----------|---------|
| Custom theme files | Yes |
| Template parts | Yes |
| Asset integration | Yes |
| Theme bootstrap | Yes — thin `functions.php` |
| Project functionality plugin | Yes |
| ACF Local JSON | Yes |
| CPT/taxonomy registration | Yes — in plugin per WAD |
| Admin UX configuration | Yes — per approved map |
| Local forms/integrations | Yes — local only |
| Local build scripts | Yes — if in spec |
| Validation configuration | Yes — project-local |

---

## Required discipline

- **Full files, not fragments** — deliver complete file contents per edit
- **No silent rewrites** — document structural changes
- **No frontend visual invention** — match approved HTML/CSS classes
- **Preserve approved classes** unless documented deviation
- **`functions.php` remains bootstrap** — load `inc/` modules
- **Modular code** — one concern per file where practical
- **Escaping** — `esc_html`, `esc_attr`, `esc_url` as appropriate
- **Sanitization** — on all saved input
- **Nonces** — on forms and AJAX
- **Capabilities** — check before privileged actions
- **WPCS** — WordPress Coding Standards alignment
- **Comments** — only where non-obvious
- **No secrets** in code or config committed
- **No production URLs** hardcoded
- **No direct DB edits** — use WordPress APIs

---

## Required implementation order

```text
1. theme foundation (style.css, functions.php bootstrap, inc/ loader)
2. assets (enqueue, copied/built CSS/JS/fonts)
3. global templates (header, footer)
4. page templates (front-page, page, archive, single)
5. reusable components (template-parts)
6. content bindings (ACF getters in templates)
7. ACF/CPT (JSON sync, registration in plugin)
8. admin UX (options pages, labels via JSON)
9. interactions (minimal JS — match frontend)
10. validation (self-check PHPCS, template smoke)
```

Do not skip order without operator-approved spec amendment.

---

## Standards used
- FW-S-03, FW-S-04, FW-S-07
- FW-S-02 ACF, FW-S-01 CPT
- Safe command policy

## Allowed tools
- Write within scope
- `phpcs` (read), local `wp` CLI if approved and local only
- npm/gulp for asset build if in spec

## Forbidden actions
- Production deploy commands
- `wp plugin install` without approval
- Database SQL direct
- Editing WordPress core
- Editing approved frontend source
- Installing unlisted plugins

## Validation
- Self-run PHPCS on changed PHP files
- Template hierarchy loads without fatal errors (when env available)
- FW-V-02, FW-V-03 recommended before claiming complete

## Human gate
Code review before validation pass — operator or separate pass.

## Stop conditions
- Spec not approved
- Scope violation
- Missing local environment when code requires runtime test
- PHPCS blocking errors unresolved

## Report format
```text
# REPORT — Forge WordPress Theme Implementation
## Files created/updated
## Implementation order completed
## Security checks
## Deviations from frontend
## Self-validation (PHPCS)
```

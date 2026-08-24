# REPORT — FP-0002 SPECIALISTS HUB LAYOUT POLISH 01

**Date (UTC):** 2026-08-24  
**Production:** https://shpigovsky.ru/  
**Page:** #1030 `/specyalisty/` (Specialists Hub)  
**Core version:** unchanged `0.3.27-specialists-hub-admin-ux` (theme-only wave; no core bump)  
**Theme CSS/templates:** updated in place under `shpigovsky`

## Verdict

**PASS** — Three operator-approved layout cleanups live on Specialists Hub only; home / other surfaces keep `internal-page-nav` and rehab inner `.container`; indexing remains OPEN; Olya/Admin editorial meta on #1030 preserved.

## 1. Current-origin preflight

- Workspace `X:\AI MARS`, volume `X:` / `AI WS`
- Fresh worktree: `X:\AI MARS\worktrees\fp0002-specialists-hub-layout-polish-01`
- Branch: `wave/fp0002-specialists-hub-layout-polish-01`
- Base: `origin/mars/canonical-post-recovery` @ `99bd5bd8066341c2896f8e423efd215efa177057`
- Shared dirty main foreign WIP **not** used

## 2. Fresh production intake

Evidence: `REPORTS/evidence/prod-maint-specialists-hub-layout-polish-01/01-intake.json`

| Item | Value |
|------|--------|
| Template | `page-templates/specialists-hub.php` |
| Core | `0.3.27-specialists-hub-admin-ux` |
| Theme | `0.3.0-d7a-shell` |
| `blog_public` | `1` |
| Reusable enabled | `1` |
| Selection | `rehab_requirements`, `about_home` |
| Lead/body | present (Olya editorial; preserved) |
| Hub HTML | had `internal-page-nav`; rehab had nested inner `.container` |
| `/specialisty/` | HTTP 404 (untouched) |

## 3. `internal-page-nav`

**Previous owner on Hub:** `shpigovsky_render_breadcrumbs()` default wrap=`auto` → `internal` via `shpigovsky_breadcrumbs_should_use_internal_wrap()` (emits `.internal-page-nav > .container` around breadcrumbs).

**Change:** page-local only in `page-templates/specialists-hub.php`:

`shpigovsky_render_breadcrumbs( array( 'wrap' => 'none' ) );`

Component `template-parts/components/internal-page-nav.php` **not** deleted. Other callers unchanged. Live: Hub has breadcrumbs, **no** `internal-page-nav`; `/o-centre/` and `/uslugi/` still have `internal-page-nav`.

## 4. `.plain-page-content__body`

**Owner:** `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css`

**Before:**

```css
.plain-page-content__body {
  max-width: 820px;
  font-size: 18px;
  line-height: 24px;
  color: var(--color-text-secondary, #475371);
}
```

**After:**

```css
.plain-page-content__body {
  color: var(--color-text-secondary, #475371);
  margin-bottom: var(--pad-gap);
}
```

No replacement typography/width styles added. Child rules under `.plain-page-content__body` untouched.

## 5. Rehabilitation requirements container

**Canonical partial:** `template-parts/home/rehabilitation-requirements.php` (component-owned `.container` by default).

**Usages:** front page; generic content reusable; Specialists Hub reusable; (class reuse elsewhere is separate templates).

**Implementation:** optional arg `omit_inner_container`. Specialists Hub `hub-content.php` passes `omit_inner_container => true` because Hub already wraps in `.container.plain-page-content__container`. Home and other callers unchanged — keep inner `.container`.

Live: Hub rehab section opens without nested inner `.container`; home rehab still has `<div class="container">` immediately inside the section.

## 6. Files changed (runtime)

1. `WORDPRESS/theme/shpigovsky/page-templates/specialists-hub.php`
2. `WORDPRESS/theme/shpigovsky/template-parts/specialist/hub-content.php`
3. `WORDPRESS/theme/shpigovsky/template-parts/home/rehabilitation-requirements.php`
4. `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css`

Docs/evidence: this report + `REPORTS/evidence/prod-maint-specialists-hub-layout-polish-01/` + `PROJECT-STATUS.md`.

## 7. Deployment

Exact-file SFTP deploy (4 files). Layer-B pre copies under evidence `layer-b-pre/`. Manifest: `03-deploy-manifest.json`. Remote `php -l` PASS for all PHP. Editorial meta on #1030 unchanged after deploy.

## 8. Live QA

| Check | Result |
|-------|--------|
| `/specyalisty/` HTTP 200 | PASS |
| `internal-page-nav` absent | PASS |
| Breadcrumbs / H1 / header / footer | PASS |
| Specialist listing | PASS |
| Rehab block present, no inner `.container` | PASS |
| Editorial lead/body preserved | PASS |
| PHP fatals | none |
| CSS rule | PASS |

Note: `is-revealed` is JS reveal-class added at runtime; initial HTML has `data-reveal class="home-rehabilitation-requirements"` (same as pre-wave). Not a regression.

## 9. Regression QA

| Surface | Result |
|---------|--------|
| Home rehab keeps inner `.container` | PASS |
| `/o-centre/` `internal-page-nav` | PASS |
| `/uslugi/` `internal-page-nav` | PASS |

## 10. SEO / indexing / robots

- `blog_public=1` OPEN
- `/specyalisty/` 200 canonical unchanged
- `/specialisty/` still 404, no redirect added
- `robots.txt` still HTTP 200 (physical file; not rewritten this wave)

## 11. Production ↔ source parity

All 4 deployed files: exact SHA match (`05-parity.json`).

## 12. Backup / rollback

Operator full Beget backup acknowledged for this maintenance period. Wave Layer-B: evidence `layer-b-pre/` exact pre-deploy bytes for the 4 touched remote paths. Restore those paths from Layer-B to roll back.

## 13. Harvest

**NO NEW HARVEST REQUIRED.**

## 14. Mutation statement

Theme template/CSS layout cleanup only. No CPT, no Page #1030 content/meta writes, no reusable selection changes, no redirects, no robots, no indexing switch, no forms/SMTP/privacy/Metrika, no core version bump.

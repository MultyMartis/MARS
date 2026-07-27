# REPORT — I-SEO REPORT HUB REPORT STYLING / CLIENT TEMPLATE CHARTER 01

## 1. Execution Verification

- repo root: `X:\AI MARS`
- drive: `X:`
- volume label: `AI WS`
- branch: `mars/canonical-post-recovery`
- HEAD before: `4e1798bcfc540ae0422d13853bc380e89f92bc81`
- staged/index state (main): foreign-only staged WIP present under `projects/client-ops-reporting-bridge/` (and related); **no** `projects/iseo-report-hub/` staged
- clean temporary worktree used: **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-styling-template-charter-01\repo`
- i-SEO WIP clean before: **yes**
- foreign WIP preserved: **yes** (main index untouched)
- write scope: allowlisted Active Brain docs only under `projects/iseo-report-hub/product/`, `projects/iseo-report-hub/reports/`, `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

## 2. Baseline Reviewed

- PDF Hardening primary: `d8a1b9e10ad62773aebe9347593c6a87aded2259`; hash-record `01127fb5a0a673eda547fa49b8620713f493308a`; tip clarify `4e1798bcfc540ae0422d13853bc380e89f92bc81`; smoke 67/67 PASS
- PDF Browser primary: `ddea70ba803cb196444377d43d9673633bbde7b5`; final tip `b24f6beb7488c15f393540900e3d94e1ad8733ee`; PDF export id **2** key `snapshot-1-pdf-v1`
- HTML Export primary: `25cf8d4229c1e31bf1159ed2976bb320340bb336`; hash-record `ce1c095a7d67192e59b764d7b9ea64229e1c48ae`; HTML export id **1** key `snapshot-1-html-v1`
- Artifact baseline (read-only FS): HTML size **5360** checksum `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4`; PDF size **133005** checksum `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320`; both outside public/Git
- Snapshot baseline (from prior docs): id **1** `monthly-1-v1` active checksum `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38`
- DB baseline: expected migrations **7**; tables **15**; `report_exports` **2** (docs/prior hardening attestation; optional live DB query not required for docs-only charter)
- Current limitation: no formal styling/template/branding policy; minimal embedded CSS only; no template id/version; no HTML/PDF visual design system

## 3. Charter Output

Created:

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-styling-client-template-charter-01.md`

Updated:

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md` — active stage; styling charter section; canonical docs 195–199; next stages; boundaries

## 4. Template Model Decision

- code-first default template: **yes**
- template id: `iseo_default_v1`
- template version: `1`
- why no DB-backed registry yet: MVP needs visual/parity proof without migration/admin UI; HTML comments/meta can carry ids first
- why no client branding DB yet: no public/client portal; LOCAL_FIXTURE_ONLY; logo/rights/path not confirmed; avoid schema creep

Model options recorded: A code-only (MVP), B Git config later, C DB registry later, D client assignment later.

## 5. Styling / Branding Policy

- professional i-SEO internal/client report; clean printable; light theme; no SaaS-card overdesign; radius 0 default
- readable Cyrillic via local/system font stacks; no CDN fonts
- HTML/PDF parity via single embedded CSS + `@media print` / `@page` A4
- no external assets; no JS in export artifact
- client branding MVP: i-SEO text brand + snapshot client/project/site names only; logo upload / color picker deferred
- A4 printable margins; Edge-safe CSS; page-break best-effort

## 6. Immutability / Export Versioning

- snapshot payload remains immutable content input
- template is render policy (deterministic by id/version)
- existing HTML id **1** / PDF id **2** must not be silently overwritten when styling lands
- restyle requires new export version or explicit repair/regeneration charter
- future metadata: `template_id`, `template_version`, `render_engine`, `render_options`, source checksums, `source_html_export_id` for PDF
- optional DB-09 later for durable columns / `report_templates` registry — not this wave

## 7. Validation Plan

Future Default Template Implementation must validate:

- baseline exports unchanged by default
- new HTML carries template id/version
- no external assets/JS
- Cyrillic readable; A4/print sane
- PDF from styled HTML works with hardening/idempotency intact
- no public route regression

This charter wave: docs-only; no styling smoke execution beyond read-only artifact checksum confirm.

## 8. Restrictions Confirmed

- no app-source edits: **yes**
- no runtime edits: **yes**
- no DB mutation: **yes**
- no SQL/migration creation/edit: **yes**
- no report_exports / report_snapshots / report_blocks / monthly_report_contents / weekly_checkpoint / reporting_period row changes: **yes**
- no artifact regeneration: **yes**
- no new export rows: **yes**
- no package install/download: **yes**
- no push/fetch/pull/reset/clean/stash: **yes** (commit docs only; push no)

## 9. Commit

- exact-path git add: allowlisted docs only (in clean worktree)
- commit message: `docs(iseo-report-hub): add report styling template charter`
- commit hash: `f7d21ac7a1fe75699074a9829c41483419bd8433`
- hash-record follow-up (report only): `PENDING_HASH_RECORD`
- push: **no**

## 10. SAFE UNKNOWN

- Live MySQL row counts were not re-queried in this docs-only wave; expected counts taken from PDF Hardening attestation and read-only artifact FS check. Re-verify DB in Implementation 01 preflight.
- Exact Edge print margin/footer chrome behavior after new CSS is unknown until Implementation 01 PDF spot-check.
- Whether Implementation 01 will need a temporary non-registered HTML file vs an explicit new export version is deferred to that charter’s operator choice.

## 11. Recommended Next Action

I-SEO Report Hub — Report Styling Default Template Implementation 01

## 12. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-styling-client-template-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

## 13. Git Actions

- exact-path git add: **yes** (allowlisted docs only)
- commit: **yes** (primary + hash-record)
- push: **no**
- fetch: **no**
- pull: **no**
- checkout/update-ref: worktree detached at HEAD; post-commit `git update-ref refs/heads/mars/canonical-post-recovery <new-tip>` from clean worktree if safe
- reset: **no**
- restore: scoped restore on main for changed i-SEO docs only if needed to align working tree to HEAD
- clean: **no**
- stash: **no**
- broad git add: **no**
- clean temporary worktree: `X:\AI MARS STORAGE\git-sync-iseo-report-styling-template-charter-01\repo` used for commit

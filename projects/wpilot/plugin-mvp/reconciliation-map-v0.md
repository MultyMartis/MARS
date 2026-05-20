# WPilot Plugin MVP Reconciliation Map v0

**Status:** CORE reconciliation document.
**Scope:** `projects/wpilot/**` documentation only.
**Lane:** B.
**Chat type:** Plugin Engineering.

This map records what already exists for MetaCODE WPilot Plugin planning before any MVP evolution. It is a consolidation aid, not proof of plugin implementation, runtime integration, autonomous operation, production readiness, or deployed code.

## Existing WPilot Files Found

| File | Status | Existing coverage |
|---|---|---|
| `README.md` | CORE | WPilot definition, Phase 1 document map, security baseline, SAFE UNKNOWN. |
| `phase-1-mvp.md` | CORE | Human-supervised Beget test-site MVP workflow, read-only inspection, backup, rollback, WPBakery/The7 inspection, QA, exclusions. |
| `boundaries.md` | CORE | Entity classification, external systems, ownership rules, forbidden claims, forbidden paths/materials, production rule. |
| `access-safety.md` | CORE | Secret handling, access classes, least-access principle, materials not allowed in repo, revocation check. |
| `backup-rollback-rules.md` | CORE | Backup confirmation, rollback plan requirements, safe rollback targets, disallowed rollback dependencies, stop/escalate rules. |
| `qa-checklist.md` | OPERATIONAL | Phase 1 QA gates for scope, access, backup, rollback, read-only inspection, safe tests, closeout. |
| `beget-test-plan.md` | OPERATIONAL | Beget test sequence, stop conditions, evidence to record. |
| `milestones.md` | PARTIALLY OPERATIONAL | Confirmed DEV/testing history: FTP operation, rollback, DEV indexing isolation, WPBakery structure inspection, scoped DB-assisted edit. |
| `metacode-wpilot-plugin-concept.md` | PLANNED | Planned plugin concept, strategic target hierarchy, Mode A Factory-native / Mode B legacy compatibility split, non-goals, goals, security principles, candidate REST endpoints, operational boundaries, SAFE UNKNOWN. |
| `metacode-wpilot-plugin-mvp-roadmap.md` | PLANNED | Phased plugin roadmap from skeleton to read-only bridge, scoped writes, Factory-native structured draft pipeline direction, DEV isolation helper, production safety, future browser/admin layer, future Blog/Page integration. |
| `templates/site-passport-template.md` | OPERATIONAL | Sanitized site facts, WordPress signals, access classes, backup facts, approved targets. |
| `templates/change-request-template.md` | OPERATIONAL | Human-approved scoped change request with forbidden-action check. |
| `templates/rollback-plan-template.md` | OPERATIONAL | Exact rollback planning template with backup confirmation, steps, verification, escalation. |
| `reports/test-report-template.md` | OPERATIONAL | Sanitized run report template with access, backup, rollback, inspection, actions, QA, risks. |

## Existing Concept Inventory

### Plugin Concepts

Canonical source: `metacode-wpilot-plugin-concept.md`.

Already covered:

- Narrow WordPress bridge plugin concept.
- Human-supervised AI-assisted WordPress administration.
- Controlled authenticated logged operations.
- Read structure, pages/posts, WPBakery content.
- Backups, scoped edits, rollback, operation logs.
- Explicit non-goals: autonomous admin, backdoor, unrestricted DB shell, public SaaS plugin, production runtime, credential storage.

### Roadmap And MVP Scope

Canonical sources:

- `metacode-wpilot-plugin-mvp-roadmap.md` for plugin phases.
- `phase-1-mvp.md` for existing WPilot human-operated DEV/testing baseline.

Already covered:

- Plugin skeleton, read-only bridge, safe scoped writes, DEV isolation helper, production-safety hardening, optional future browser/admin layer.
- Existing WPilot Phase 1 sequence: read-only inspection, access safety, backup, rollback, safe file-level test, test page copy/create, WPBakery/The7 inspection, child-theme CSS patch, database read-only awareness, QA/report.

### Strategic Modes

Canonical sources:

- `metacode-wpilot-plugin-concept.md` for the strategic target hierarchy and mode definitions.
- `metacode-wpilot-plugin-mvp-roadmap.md` for sequencing implications.
- `../README.md` for the short operator-facing summary.

Current reconciliation:

- **Mode A - Factory-native controlled sites** is the primary long-term strategy: Website Factory-created WordPress with known stack, approved plugins/themes, approved templates, structured content payloads, known mutation zones, and human-approved publishing gates.
- **Mode B - legacy/external compatibility** is the secondary strategy: WPBakery, The7, Elementor, unknown plugins/themes, legacy HTML/content shape, refusal-first inspection, dry-run-heavy validation, conservative mutation policy.
- WPBakery handling belongs to Mode B compatibility. It remains useful for current DEV evidence and external site support, but it is not the ideal long-term WPilot target.
- No document should recast WPilot as a universal autonomous WordPress AI runtime.

### Rollback Concepts

Canonical sources:

- `backup-rollback-rules.md` for current WPilot operational rollback discipline.
- `metacode-wpilot-plugin-mvp-roadmap.md` for future plugin-created page backups and rollback endpoints.
- `templates/rollback-plan-template.md` for run-level rollback planning.

Already covered:

- Backup before write-like action.
- External backup facts only, no archives or dumps in repo.
- Exact target, before state, rollback action, verification, stop conditions, human owner.
- Plugin roadmap requires page backup before scoped writes and rollback to plugin-created backup.

### Audit And Logging Concepts

Canonical source: `metacode-wpilot-plugin-concept.md`, with roadmap support in `metacode-wpilot-plugin-mvp-roadmap.md`.

Already covered:

- Audit log for every request.
- Logging plan before operational endpoints.
- Logs should include who/what/when/target/outcome without storing secrets.

Needs stabilization:

- Storage choice remains SAFE UNKNOWN: custom table, WordPress option, or export format.
- Minimal log schema needs to be stated as MVP planning guidance.

### REST/API Ideas

Canonical source: `metacode-wpilot-plugin-concept.md`.

Already covered candidate endpoints:

- `GET /site-info`
- `GET /plugins`
- `GET /themes`
- `GET /pages`
- `GET /page/{id}`
- `GET /page/{id}/wpbakery-map`
- `POST /page/{id}/backup`
- `POST /page/{id}/replace-text`
- `POST /page/{id}/rollback`
- `GET /seo/indexing-state`
- `POST /seo/dev-isolation`
- `GET /logs`

Needs stabilization:

- MVP route prefix and exact WordPress REST registration remain SAFE UNKNOWN.
- Endpoint status labels should separate CORE read-only endpoints, DEV-ONLY helper endpoints, and EXCLUDED operations.

### WPBakery Parsing Notes

Canonical sources:

- `milestones.md` for confirmed DEV/testing observations.
- `metacode-wpilot-plugin-concept.md` for planned structural map endpoint.
- `metacode-wpilot-plugin-mvp-roadmap.md` for scoped write strategy.

Already covered:

- DEV milestone detected `vc_row`, `vc_column`, `vc_raw_html`, and `vc_column_text`.
- Full shortcode replacement produced `0 rows affected`; anchor-based replacement worked in one confirmed DEV case.
- Plugin concept proposes `GET /page/{id}/wpbakery-map`.
- Roadmap says WPBakery content should be handled as structured content where possible, not blind global string mutation.

Needs stabilization:

- MVP should define the parser as a conservative shortcode-aware map, not a complete WPBakery renderer.
- Unknown shortcode variants, theme wrappers, encoded content, and nested/raw HTML behavior remain SAFE UNKNOWN.

### Security Boundaries

Canonical sources:

- `access-safety.md`
- `boundaries.md`
- `metacode-wpilot-plugin-concept.md`
- `metacode-wpilot-plugin-mvp-roadmap.md`

Already covered:

- No secrets in repo.
- No credential storage.
- Disabled/restricted plugin start.
- Token-based authentication and per-site secret.
- Operation allowlist.
- No arbitrary SQL.
- No file manager.
- No plugin/theme/core updates.
- No autonomous operation.
- Human approval for risky writes.

Needs stabilization:

- Explicit MVP language should say no unrestricted filesystem access and no code execution.
- Token model should be clearly per-site, revocable, and never logged in plaintext.
- DEV-only installation scope should be explicit for the MVP planning pack.

## Duplicates And Overlaps

| Area | Overlap | Resolution |
|---|---|---|
| WPilot scope vs plugin scope | `phase-1-mvp.md` describes current human-operated WPilot Phase 1; plugin docs describe future bridge plugin. | Keep both. Treat `phase-1-mvp.md` as operational baseline and plugin docs as PLANNED extension. |
| Strategic modes | README, concept, roadmap, and Website Factory pointers mention Factory-native vs legacy compatibility. | Keep `metacode-wpilot-plugin-concept.md` canonical for definitions; roadmap owns sequencing; README/Website Factory docs should only summarize and link. |
| Rollback | `backup-rollback-rules.md`, roadmap Phase 2, rollback template all discuss rollback. | Keep `backup-rollback-rules.md` as canonical operational discipline; plugin docs should reference rollback-first writes and plugin-created page backups. |
| Security baseline | `README.md`, `access-safety.md`, `boundaries.md`, plugin concept, roadmap. | Keep `access-safety.md` and `boundaries.md` canonical for WPilot-wide security; plugin docs carry plugin-specific enforcement. |
| WPBakery notes | `milestones.md` records confirmed DEV evidence; plugin docs plan parser/replacement. | Keep `milestones.md` as evidence log; plugin docs must not overclaim parser completeness. |
| DEV isolation | `milestones.md` records confirmed DEV isolation workflow; roadmap plans helper endpoint. | Keep helper as DEV-ONLY and explicitly not production SEO automation. |
| API surface | `metacode-wpilot-plugin-concept.md` lists candidate endpoints; roadmap phases group capabilities. | Keep concept as canonical endpoint inventory; roadmap as sequencing. |

## Conflicts And Terminology Drift

| Issue | Current state | Reconciliation |
|---|---|---|
| `disabled by default or restricted to administrator users` | The phrase permits two interpretations. | MVP should require disabled by default, then explicit enablement and administrator capability checks. |
| Database writes | `phase-1-mvp.md` says DB read-only in MVP; `milestones.md` records operator-assisted DB write; plugin roadmap says no arbitrary SQL but scoped writes. | Distinguish existing human-operated DEV exception from planned plugin MVP. Plugin MVP excludes arbitrary SQL and direct SQL endpoints; scoped page writes use WordPress APIs after rollback-first checks. |
| Production safety | Roadmap includes Phase 4 production-safety hardening. | MVP remains DEV-ONLY. Production hardening is PLANNED, not permission for production use. |
| Browser/admin layer | Roadmap Phase 5 mentions optional future layer. | Keep EXPERIMENTAL and outside MVP. Plugin core remains narrow REST bridge. |
| Audit storage | Roadmap allows table or option storage; concept lists logs. | Leave storage as SAFE UNKNOWN, but define minimum event fields in concept/roadmap. |

## Abandoned Or Outdated Ideas

No clearly abandoned WPilot plugin files were found under `projects/wpilot/**`.

Superseded-by-context candidates:

- Direct DB-assisted content replacement from `milestones.md` is historical DEV evidence, not a recommended plugin implementation path.
- WPBakery/The7 compatibility as a primary strategic target is superseded by the Factory-native controlled-site strategy; keep it as legacy/external compatibility mode.
- Browser/admin integration in roadmap Phase 5 is future EXPERIMENTAL, not part of MVP.
- Any production use implied by later hardening phases is superseded by DEV-ONLY MVP scope until separate evidence and approval exist.

## Recommended Canonical MVP Docs

Use this compact pack:

1. `metacode-wpilot-plugin-concept.md` — CORE/PLANNED canonical plugin architecture, security boundary, REST surface, auth, rollback, audit, scoped replacement, WPBakery strategy.
2. `metacode-wpilot-plugin-mvp-roadmap.md` — CORE/PLANNED implementation sequencing and MVP/non-goal labels.
3. `backup-rollback-rules.md` — CORE operational rollback discipline inherited by plugin MVP.
4. `access-safety.md` — CORE access and secret handling rules inherited by plugin MVP.
5. `boundaries.md` — CORE entity, ownership, external-system, and forbidden-claim rules.
6. `milestones.md` — PARTIALLY OPERATIONAL evidence log, not architecture.
7. `plugin-mvp/reconciliation-map-v0.md` — CORE reconciliation index for avoiding duplicate architecture.

Do not create another broad architecture document unless implementation work begins and a missing detail cannot be placed in the existing concept or roadmap.

## Missing Compact Updates Needed

The existing docs are sufficient as the MVP planning pack after targeted edits to:

- Add explicit DEV-ONLY MVP installation scope to the plugin concept.
- Add compact filesystem structure guidance to the plugin concept.
- Normalize authentication as disabled-by-default, explicit enablement, per-site token, administrator capability checks, token rotation/revocation, and no plaintext token logging.
- Stabilize minimal audit log fields.
- Label REST endpoints by CORE, DEV-ONLY, PLANNED, and EXCLUDED.
- State rollback-first writes and WordPress-API-based scoped replacement.
- Clarify WPBakery parsing as shortcode-aware structural mapping, not a full renderer.
- Add explicit exclusions: no unrestricted filesystem access, no code execution, no arbitrary SQL, no autonomous behavior.
- Preserve the Mode A / Mode B strategic split and avoid duplicate architecture docs.
- Keep Factory-native structured content, Blog Agent handoff, approved template pipeline, and human-approved publishing as future integration directions until contracts exist.

## SAFE UNKNOWN

- No plugin source code was found under `projects/wpilot/**`.
- Exact WordPress REST route prefix and implementation classes are unknown.
- Exact auth design details, token hashing/storage, nonce use, and capability mapping are unknown.
- Audit log storage choice is unknown.
- WPBakery parser reliability across real pages, themes, raw HTML blocks, nested shortcodes, and encoded content is unknown.
- Compatibility with target WordPress/PHP versions, security plugins, cache plugins, SEO plugins, The7 variants, and hosting restrictions is unknown.
- Production readiness remains unknown and cannot be claimed.
- Factory-native WordPress template-slot schema, structured content payload format, Blog Agent contract, and human-approved publishing pipeline remain undefined.


# MetaCODE WPilot Plugin MVP Roadmap

**Classification:** Planned WordPress bridge plugin roadmap.
**Chat type:** External Systems.
**Active lane:** B.
**Status:** PLANNED roadmap only; no plugin implementation in this repository.

## Goal

Define a conservative MVP path for a future MetaCODE WPilot Plugin that can act as a controlled bridge between WPilot and managed WordPress sites.

The roadmap preserves the WPilot boundary: human-supervised operation, no stored credentials, no autonomous website control, no arbitrary SQL, and no production-runtime claim.

Strategic direction: WPilot should prioritize **Factory-native WordPress sites created through MARS Website Factory** as the long-term controlled target, while keeping legacy/external WordPress support as a conservative compatibility bridge.

## Canonical MVP Pack

This roadmap should be read with:

- `plugin-mvp/reconciliation-map-v0.md` - CORE reconciliation map and canonical source selection.
- `metacode-wpilot-plugin-concept.md` - PLANNED plugin architecture, REST surface, auth, audit, rollback, scoped replacement, WPBakery strategy.
- `access-safety.md` - CORE secret and access handling.
- `backup-rollback-rules.md` - CORE rollback discipline.
- `local-storage-policy.md` - CORE local-only operator storage policy for ignored `D:\AI MARS\local\` and `D:\AI MARS\backups\` folders.
- `boundaries.md` - CORE ownership and forbidden-claim boundaries.
- `milestones.md` - PARTIALLY OPERATIONAL DEV/testing evidence, not plugin implementation proof.

## MVP Boundary

The plugin MVP is **DEV-ONLY** until a separate production-readiness task proves otherwise.

MVP requirements:

- Disabled by default.
- Explicit WordPress-admin enablement.
- Per-site token.
- Administrator capability checks.
- Operation logging.
- Rollback-first writes.
- Scoped-only replacement.
- WPBakery-aware structural mapping.
- Human-supervised operation.

MVP exclusions:

- No arbitrary SQL.
- No unrestricted filesystem access.
- No code execution.
- No mass replacement.
- No plugin, theme, or WordPress core updates.
- No credential storage.
- No autonomous behavior.
- No public SaaS/plugin-marketplace release claim.

## Strategic Operating Modes

The roadmap separates two operating modes:

| Mode | Roadmap role | Scope posture |
|---|---|---|
| **Mode A - Factory-native controlled sites** | Primary long-term strategy. | Known stack, approved plugins/themes, approved templates, structured block/content schemas, predictable layouts, Website Factory contracts, known mutation zones, human-approved publishing pipeline. |
| **Mode B - legacy/external sites** | Secondary compatibility strategy. | WPBakery, The7, Elementor, unknown plugins/themes, legacy HTML/content chaos, refusal-first inspection, dry-run-heavy validation, conservative mutation policy. |

Phase 0-3 work may still validate Mode B because the current DEV evidence is WPBakery/The7-shaped. That does not make WPBakery the preferred long-term target. WPBakery handling remains a compatibility layer for legacy/external sites.

## Phase 0 - Plugin Skeleton

**Status:** CORE / PLANNED / DEV-ONLY.

Purpose: establish a minimal WordPress plugin shell and operator-facing controls before exposing site operations.

Expected scope:

- Admin page.
- Status screen.
- Token generation.
- Token rotation and revocation.
- Enabled/disabled switch.
- Audit log table or option storage.
- Clear warning that the plugin is a controlled bridge, not an autonomous admin.

Exit criteria:

- Plugin can be installed by a human administrator.
- Plugin defaults to disabled.
- Operator can generate, rotate, and revoke the per-site token.
- Every request path has a logging plan before operational endpoints are added.
- No operational endpoint is exposed without explicit enablement and authentication.

## Phase 1 - Read-Only Bridge

**Status:** CORE / PLANNED / DEV-ONLY.

Purpose: allow authenticated inspection without content mutation.

Expected scope:

- Site info.
- Active theme and child theme.
- Plugin list.
- Pages list.
- Page content read.
- WPBakery shortcode detection.
- Structural map output.
- Indexing state read.
- Operation logs.

Exit criteria:

- WPilot can inspect WordPress structure through controlled read-only endpoints.
- The plugin exposes enough page and WPBakery structure to plan a scoped edit.
- No endpoint mutates content, files, settings, plugins, themes, or database schema.
- Logs record read operations without storing secrets or plaintext tokens.

## Phase 2 - Safe Scoped Writes

**Status:** CORE / PLANNED / DEV-ONLY.

Purpose: introduce narrowly bounded content changes with backup and rollback support.

Expected scope:

- Page backup.
- Single occurrence text replacement.
- WPBakery-aware scoped replacement.
- Rollback to backup.
- Dry-run or diff preview before mutation.
- No arbitrary SQL.
- No unrestricted filesystem access.
- No code execution.
- No mass replace.

Exit criteria:

- A page backup is required before a write.
- Replacement is limited to one approved target and one approved occurrence unless a human explicitly approves a different scoped operation.
- WPBakery content is handled as structured content where possible, not blind global string mutation.
- Rollback can restore the specific plugin-created backup for the target page.
- Ambiguous matches are rejected by default.
- Writes use WordPress APIs rather than arbitrary SQL endpoints.

## Phase 2F - Factory-Native Structured Draft Pipeline

**Status:** PLANNED; outside current MVP unless a separate Factory integration task is opened.

Purpose: define how Website Factory-approved artifacts could become WordPress drafts or updates through WPilot without claiming autonomous CMS control.

Expected scope:

- Approved page template identifiers.
- Approved content payloads mapped to known section/block slots.
- SEO/content fields derived from approved Website Factory artifacts.
- Known mutation zones declared by the implementation/handoff pack.
- Dry-run diff between approved Factory payload and WordPress draft/current page.
- Human-approved publish/update decision before any live change.

Exit criteria:

- A Factory-native content operation can be described without raw global string replacement.
- The operation references approved blueprint/template/content artifacts.
- WPilot refuses payloads that do not match the approved template/content contract.
- Publishing remains blocked until human approval and rollback evidence exist.

Non-goals:

- No autonomous blog or page publishing.
- No direct generation-to-live WordPress mutation.
- No claim that Website Factory currently exports WordPress-ready payloads.
- No replacement of Website Factory's blueprint, design, frontend, QA, or approval stages.

## Phase 3 - DEV Isolation Helper

**Status:** DEV-ONLY / PLANNED.

Purpose: help operators prevent development or test sites from being indexed accidentally.

Expected scope:

- `robots.txt` status.
- WordPress noindex state.
- Frontend meta robots check.
- Optional controlled toggle.

Exit criteria:

- The plugin can report indexing exposure signals.
- Any toggle is disabled unless explicitly enabled and approved.
- The helper is documented as a development/test safety tool, not a production SEO automation system.

## Phase 4 - Production Safety

**Status:** PLANNED; outside MVP.

Purpose: harden the bridge before any production use is considered.

Expected scope:

- Approval tokens.
- Dry-run mode.
- Diff preview.
- Rollback requirement.
- Operation logs.
- Strict permissions.

Exit criteria:

- Risky writes require explicit approval evidence.
- Operator can preview the exact proposed change before execution.
- Logs include who/what/when/target/outcome metadata without storing secrets.
- Permission checks prevent non-administrative or unintended access.
- Production use remains unavailable unless the operator approves a separate production-specific run with backup and rollback evidence.

## Phase 5 - Future Browser/Admin Layer Integration

**Status:** EXPERIMENTAL; outside MVP.

Purpose: explore optional integration with browser/admin workflows after the plugin core is stable.

Expected scope:

- Optional, not required for MVP.
- Separate from plugin core.
- Used only where WordPress APIs are insufficient or human-admin review remains necessary.

Exit criteria:

- Browser/admin integration is not required for read-only or scoped-write MVP behavior.
- Any future browser/admin layer has its own permissions, logging, and approval model.
- The plugin core remains a narrow authenticated API bridge.

## Phase 6 - Future Blog/Page Agent Integration

**Status:** EXPERIMENTAL / PLANNED; outside MVP.

Purpose: align future Blog Agent or page-generation work with Website Factory contracts and WPilot safety boundaries.

Expected direction:

- Blog/page ideas become approved content artifacts before WordPress handoff.
- Approved templates define allowed sections, fields, CTA slots, SEO fields, and internal-link rules.
- WPilot consumes only a bounded draft/update request, not an open-ended "write this site" instruction.
- Controlled SEO/content workflows provide metadata, schema candidates, and internal linking notes for review.
- Human approval is required before publish, schedule, or live update.

Exit criteria:

- A content artifact contract exists and is linked from the roadmap.
- A publishing approval artifact exists and names target site, page/post, operation, rollback plan, and approver.
- WPilot can refuse incomplete, unapproved, or contract-mismatched content.

Until those contracts exist, Blog Agent integration is **SAFE UNKNOWN**.

## Estimated Effort

- Read-only MVP: 1-2 days.
- Scoped write MVP: 3-7 days.
- Safer production-ready bridge: 2-4 weeks.

These estimates assume an experienced WordPress/PHP developer, limited endpoint scope, and a test site with admin access. They do not include public-plugin hardening, marketplace release, broad compatibility testing, penetration testing, or enterprise compliance work.

## Risks

- Security exposure if authentication, token handling, permission checks, or logging are weak.
- Accidental broad edits if replacement scope is too loose.
- WPBakery shortcode corruption if content is modified without structural awareness.
- Strategic drift if legacy builder compatibility is mistaken for the primary WPilot product target.
- Operator overtrust if Factory-native structure is treated as permission for autonomous publishing.
- Plugin conflict with security, cache, SEO, builder, or theme-specific behavior.
- Cache/SEO plugin interference that makes indexing state or frontend verification misleading.
- Operator overtrust if the bridge is mistaken for autonomous control or a production runtime.

## MVP Non-Goals

- No arbitrary SQL.
- No file manager.
- No plugin updates.
- No theme updates.
- No WordPress core updates.
- No hidden deploy bot behavior.
- No credential storage.
- No autonomous website administration.
- No public SaaS plugin behavior.

## Open Questions

- Should audit logs be stored in a custom table, WordPress options, or an external operator-export format?
- What token rotation and revocation UX is sufficient for Phase 0?
- How should approval tokens be generated, expired, and tied to a specific proposed write?
- What minimum WPBakery map format is useful without overfitting to one theme or page style?
- Which SEO plugins should be read in Phase 1, if any, beyond WordPress core visibility and frontend metadata?
- What cache purge behavior, if any, belongs in MVP without becoming a broad site-control surface?
- Which WordPress/PHP versions are the minimum supported DEV-only implementation targets?
- What Website Factory artifact should be canonical for WordPress template/content payloads?
- What minimum template-slot schema is needed before Factory-native structured operations are safer than exact text replacement?
- Where should publish approval be recorded for human-approved WordPress draft, update, or publish actions?

## SAFE UNKNOWN

- The exact implementation strategy is unknown until a separate plugin-development task is opened.
- The target WordPress versions, PHP versions, security plugins, cache plugins, SEO plugins, and WPBakery variants are unknown until inspected on a real site.
- Production readiness cannot be claimed until implementation, security review, rollback verification, and operator approval evidence exist.
- Factory-native WordPress template contracts, structured content payload format, Blog Agent handoff, and human-approved publishing pipeline remain undefined.

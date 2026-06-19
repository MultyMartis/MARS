# WPilot Proven Capabilities v1

**Classification:** Evidence layer — documented proof of executed capabilities only.  
**Status:** v1 evidence register — updated 2026-06-19 (Runtime Proof + Prototype Sprints 1–2).  
**Site scope:** `https://dev.gktriumph.ru` (DEV/test only, human-supervised).  
**Related:** [WPILOT-MISSION-v1.md](WPILOT-MISSION-v1.md), [WPILOT-OPERATIONS-MANIFEST-v1.md](WPILOT-OPERATIONS-MANIFEST-v1.md), [WPILOT-OPERATION-BINDINGS-v1.md](WPILOT-OPERATION-BINDINGS-v1.md), [local-storage-policy.md](local-storage-policy.md), [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md)

---

## Purpose

Документ фиксирует **только реально подтверждённые** возможности WPilot — то, что было выполнено на DEV-сайте и подкреплено evidence.

**Источники proof в v1:**

| Source type | Examples |
|-------------|----------|
| Completed DEV work | Footer, contacts, cargo-scroll tasks on `dev.gktriumph.ru` |
| In-repo reports | [wpilot-v0.1-dev-operational-release.md](reports/wpilot-v0.1-dev-operational-release.md), [wpilot-operational-milestone-v0.1.md](reports/wpilot-operational-milestone-v0.1.md), [page-read-debug-analysis-v0.md](reports/page-read-debug-analysis-v0.md), [wpilot-runtime-proof-sprint-report.md](reports/wpilot-runtime-proof-sprint-report.md), [wpilot-runtime-prototype-sprint-1-report.md](reports/wpilot-runtime-prototype-sprint-1-report.md), [wpilot-runtime-prototype-sprint-2-report.md](reports/wpilot-runtime-prototype-sprint-2-report.md) |
| Cross-project lesson | [css-multicol-masonry-browser-compatibility-lesson-v1.md](../mars-website-factory/css-multicol-masonry-browser-compatibility-lesson-v1.md) |
| Operator evidence (local-only) | `C:\AI MARS STORAGE\wpilot\backups\dev.gktriumph.ru\` — apply/backup/validation JSON, HTML snapshots (not in git; see [local-storage-policy.md](local-storage-policy.md)) |

Документ **не описывает** roadmap.  
Документ **не описывает** planned features.  
Наличие операции в [Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md) **не делает** её proven без evidence ниже.

---

## Evidence Standard

Capability считается **proven** только если одновременно:

1. **Операция реально выполнена** на `dev.gktriumph.ru` (или зафиксирована live validation в официальном WPilot report).
2. **Есть evidence** — report, JSON result, backup artifact, HTML snapshot или validation output.
3. **Есть validation** — post-apply или post-inspection check с явным результатом.
4. **Есть rollback source или equivalent recovery evidence** — pre-apply backup path, local backup bundle, или documented restore fragment **для apply-операций**.

Без доказательства capability **не считается** proven и попадает в [Not Yet Proven](#not-yet-proven).

**Evidence gap rule:** policy examples в ChangeSet/Rollback (иллюстративные поля без привязки к artifact) **не** считаются proof.

---

## Proven Inspection Capabilities

Подтверждено evidence на DEV и/или в WPilot v0.1 live-test reports:

| Capability | Evidence |
|------------|----------|
| ✓ `inspect_site` — REST read: site info, active theme, active plugins | [wpilot-v0.1-dev-operational-release.md](reports/wpilot-v0.1-dev-operational-release.md) §2 |
| ✓ `inspect_page` — REST page detail + metadata | v0.1 reports; [page-read-debug-analysis-v0.md](reports/page-read-debug-analysis-v0.md); `page-38.pre.json`, `contacts-page69.pre.json` in `C:\AI MARS STORAGE\wpilot\backups\` |
| ✓ `inspect_page` structure / WPBakery signals — `pages/{id}/structure` | v0.1 reports §2, §4 |
| ✓ `inspect_environment` — bridge ping, DEV flags, indexing hints | `wpilot-ping.json` (recovery artifact); v0.1 ping probe |
| ✓ `inspect_footer` — read footer zone markup and layout markers | Footer menu remap validation (`20260617-171904/validation-result.json`); rendered HTML audits |
| ✓ `inspect_shortcode` — read shortcoder / footer fragment content | `footer_contacts.shortcoder.bak.html` backups; `wpilot-backup-result.json` (`post_id` 131) |
| ✓ `inspect_css` — read child-theme CSS affecting footer | `audit-footer-result.json` (matched rules for `.wsp_footer_menu__grid` in `dt-the7-child/style.css`) |
| ✓ `inspect_rendered_html` — browser computed-style / layout audit | `audit-footer-result.json` (Chrome + Firefox); `wpilot-footer-masonry-validate.json` |
| ✓ `inspect_page_storage` — export `post_content` / page storage snapshot | Pre-apply backups: `page-69-*.post_content.txt`, `page-38-*.post_content.txt` in server backup paths and local STORAGE mirrors |
| ✓ `inspect_plugin` — active plugin list (read-only) | v0.1 reports §2 |
| ✓ Phase 2A dry-run / pre-apply text analysis (`draft_shortcode_change` semantics) | v0.1 reports §5; `cargo-scroll-*/dry-run-result.json` in STORAGE |

**Not promoted to proven from inspection list alone (no sufficient isolated evidence):** `inspect_post`, `inspect_widget`, `inspect_menu`, `inspect_header`, `inspect_theme_option`, `inspect_media`.

---

## Proven Plugin REST Runtime Capabilities (Sprint 1–2)

Подтверждено **formal plugin REST** на DEV (`metacode-wpilot` v0.2.0 → v0.3.0), не через temporary PHP helpers:

| Capability | Endpoint / mechanism | Evidence |
|------------|---------------------|----------|
| ✓ Plugin REST backup (`page.post_content`) | `POST /wp-json/wpilot/v1/pages/{id}/backups` | [wpilot-runtime-proof-sprint-report.md](reports/wpilot-runtime-proof-sprint-report.md) — 3/3 PASS |
| ✓ Plugin REST rollback (`page.post_content`) | `POST /wp-json/wpilot/v1/pages/{id}/rollback` | Runtime Proof Sprint — checksum restore on pages 954, 38, 69; WPBakery shortcode counts unchanged on page 38 |
| ✓ Plugin REST scoped replace execute | `POST /wp-json/wpilot/v1/pages/{id}/scoped-replace` | [wpilot-runtime-prototype-sprint-2-report.md](reports/wpilot-runtime-prototype-sprint-2-report.md) — 3/3 PASS |
| ✓ `apply_content_change` via plugin | `scoped-replace` — exact once, `post_content` only | Sprint 2 runs on pages 954, 69, 38 |
| ✓ Post-write validation (plugin) | `validation_result: passed`; checksum before ≠ after | Sprint 2 §5 |
| ✓ Post-rollback validation (plugin) | `restored_checksum == backup checksum == baseline` | Runtime Proof Sprint + Sprint 2 §6 |
| ✓ Audit trail (plugin DB) | `wpilot_audit_log` lifecycle per `operation_id` | `backup_requested` → `backup_created`; `scoped_replace_requested` → `backup_created` → `scoped_replace_verified`; `rollback_requested` → `rollback_verified` |
| ✓ Checksum pipeline (plugin) | `sha256:` on inspect, backup, apply, rollback | Shared `WPilot_Checksum`; verified in all sprint runs |
| ✓ WPBakery-safe plugin recovery | Full `post_content` restore; shortcode integrity | Runtime Proof Sprint page 38; Sprint 2 pages 38, 954 |

**Scope limit (not overstated):** proven write primitive is **scoped exact-once replace on `page.post_content` only**. Not menu, widget, CSS, footer endpoint, or regex/mass replace.

---

## Proven Content Modification Capabilities

Подтверждено **human-supervised DEV apply** (в т.ч. через временные WPilot PHP helpers на DEV; не через formal plugin write API v0.1):

| Capability | Target / site evidence |
|------------|------------------------|
| ✓ Modify shortcode content | `footer_contacts` — `wpilot-apply-result.json`, `20260617-171904/apply-result.json` (`post_id` 131) |
| ✓ Modify footer content (zone-level) | Footer menu groups remap — `validation-result.json` (`groups_match: true`) |
| ✓ Modify WPBakery content (`vc_raw_html`, `vc_row` blocks) | Page 38 cargo-scroll blocks — `cargo-scroll-truck-sync-*/apply-result.json`, `validation-final.json` |
| ✓ Insert content block | Contacts requisites block on page 69 — `contacts-requisites-*/apply-result.json` (`rows_affected: 1`) |
| ✓ Replace content block | Footer menu structure replacement — apply results with `new_length` / fragment swap |
| ✓ Update page content (`post_content`) | Page 69 requisites; page 38 cargo scroll — apply JSON + pre/post HTML in STORAGE backups |

---

## Proven Style Modification Capabilities

| Capability | Evidence |
|------------|----------|
| ✓ Patch child theme CSS (`css_fragment`) | `.wsp_footer_menu__grid` / `.wsp_footer_menu__group` in `dt-the7-child/style.css` — [css-multicol-masonry-browser-compatibility-lesson-v1.md](../mars-website-factory/css-multicol-masonry-browser-compatibility-lesson-v1.md); `audit-footer-result.json` |
| ✓ Footer layout corrections | Footer layout apply — `wpilot-layout-apply-result.json`; menu remap validation |
| ✓ Responsive layout adjustments (scoped footer CSS) | CSS checks in `wpilot-footer-masonry-validate.json` (`column_count_4`, `tablet_column_2`, `mobile_column_1` flags recorded) |
| ✓ Browser compatibility fixes (Chrome/Firefox multicol) | Documented lesson from DEV incident; dual-browser audit in `audit-footer-result.json` |
| ✓ Scoped visual changes without site-wide theme rewrite | Cargo scroll truck sync — `validation-final.json` (`header_intact`, `footer_intact`, `cta_intact`, `all_ok: true`) |

---

## Proven Change Management Capabilities

| Capability | Evidence |
|------------|----------|
| ✓ Create backup before apply | `wpilot-backup-result.json`; `contacts-requisites-*/backup-result.json`; `cargo-scroll-*/backup-result.json` |
| ✓ Create rollback source (pre-apply backup path) | Server paths under `wp-content/uploads/wsp/wpilot-backups/` referenced in apply JSON; local mirrors in `C:\AI MARS STORAGE\wpilot\backups\dev.gktriumph.ru\` |
| ✓ Validate after apply | `contacts-requisites-*/validation.json` (`all_ok: true`); `cargo-scroll-*/validation-final.json`; footer `validation-result.json` |
| ✓ Preserve recovery artifacts | Local STORAGE backup bundles per task timestamp |
| ✓ Maintain change evidence trail | Paired pre/post HTML, apply/backup/validation JSON per run |

**Rollback execution note:** **Plugin REST `rollback_change`** proven on DEV (Runtime Proof Sprint v0.2.0 + Sprint 2 re-validation). Helper-based and hosting-level restore remain separate evidence paths. **`restore_backup`** as distinct operation_id — not separately proven.

---

## Proven Security & Safety Capabilities

| Capability | Evidence |
|------------|----------|
| ✓ DEV-only execution | All cited runs target `dev.gktriumph.ru`; cargo-scroll operator reports state production untouched |
| ✓ Temporary helper cleanup after task | `wpilot-cleanup-result.json`, `wpilot-layout-cleanup-result.json`; `cleanup-result.json` in STORAGE runs; helper URLs → 404 post-cleanup |
| ✓ Secret / helper exposure cleanup | Recovery pass moved secret-bearing helpers from `.recovery-temp` to `C:\AI MARS STORAGE\wpilot\secure-recovery\` (operator report) |
| ✓ `robots.txt` verification | `validation-result.json` (`robots_txt_ok: true`); `wpilot-footer-masonry-validate.json` |
| ✓ `noindex` meta verification | `wpilot-footer-masonry-validate.json` (`meta_robots` noindex/nofollow on DEV) |
| ✓ Scoped modification discipline | Post-apply checks: `phone_unchanged`, `gruzotaxi_section_intact`, `form_intact`, `header_intact`, `footer_intact` |
| ✓ Production environment untouched | Explicit scope in DEV task reports; no production URL evidence in apply artifacts |

---

## Proven Workflow Capabilities

| Workflow | Evidence |
|----------|----------|
| ✓ inspect → backup → apply → validate | Footer menu remap (`20260617-171904/`); contacts requisites (`contacts-requisites-20260617-194945/`); cargo scroll runs |
| ✓ apply → validate → cleanup | `validation-final.json` + `cleanup-result.json` (`helper_removed: true`) in cargo-scroll STORAGE bundles |
| ✓ backup → modify with rollback source prepared | Every cited apply JSON includes `backup_file` path to pre-apply snapshot |
| ✓ inspect → backup → apply → validate → rollback (plugin REST) | Sprint 2 — full lifecycle on pages 954, 69, 38 via `scoped-replace` + rollback endpoints |

---

## Proven Targets

Только targets с реальным evidence на DEV:

| `target_id` | Example `target_id` / entity | Evidence |
|-------------|------------------------------|----------|
| **page** | page 69 (contacts), page 38 (cargo taxi) | apply/backup JSON, HTML snapshots |
| **shortcode** | `footer_contacts` (`post_id` 131) | backup/apply JSON, `.shortcoder.bak.html` |
| **footer** | site footer zone (menu + contacts) | validation-result.json, footer HTML audits |
| **css_fragment** | `dt-the7-child` footer menu CSS | css lesson, audit-footer-result.json |
| **environment** | `dev.gktriumph.ru` DEV bridge | wpilot-ping.json, v0.1 live probes |
| **site** | Triumph DEV WordPress instance | inspect_site / multi-page DEV work corpus |

**Count:** 6 proven targets.

Targets from [Target Registry](WPILOT-TARGET-REGISTRY-v1.md) **without** sufficient apply/inspect evidence in v1: `post`, `widget`, `menu`, `header`, `theme_option`, `media`, `plugin`.

---

## Not Yet Proven

Следующие возможности **не доказаны** evidence v1 (не «невозможны» — **not yet proven**):

| Area | Items |
|------|-------|
| **Targets** | `plugin` (write), `theme_option` (write), `menu` (direct menu API write), `widget`, `header`, `media`, `post` as isolated target |
| **Operations** | `restore_backup` as distinct operation; `apply_shortcode_change` / `apply_footer_change` / `apply_css_change` via **plugin REST**; regex or mass replace; menu/widget/CSS plugin writes |
| **Environments** | production execution; multisite |
| **Execution model** | autonomous execution without human supervision |
| **Configuration** | plugin configuration management; taxonomy management; user management; comment management |
| **Draft layer** | formal `draft_*` ChangeSet lifecycle as automated product (dry-run proven; full draft workflow engine — not) |
| **OCPilot parity** | OpenCart / OCPilot operations (WordPress evidence ≠ OCPilot evidence) |

---

## Known Limits Of Evidence

| Limit | Meaning |
|-------|---------|
| **DEV evidence ≠ production evidence** | All proven apply/inspect runs are on `dev.gktriumph.ru` only. |
| **Single-site evidence ≠ multi-site evidence** | One WordPress instance; no network/multisite proof. |
| **Human-supervised evidence ≠ autonomous evidence** | Operator-initiated tasks, temporary helpers, FTP/deploy scripts — not autonomous runtime. |
| **WordPress evidence ≠ OCPilot evidence** | WPilot proof does not transfer to OpenCart storefront ops. |
| **Helper-based writes ≠ plugin REST write API** | Pre-sprint DEV tasks used temporary helpers; **plugin REST write** proven only for `scoped-replace` on `page.post_content` (v0.3.0, Sprint 2). |
| **Local STORAGE ≠ git evidence** | Backup/validation bundles live outside repo by policy; paths cited, contents not committed. |
| **Policy examples ≠ proof** | Illustrative ChangeSet/Rollback examples in policy docs require separate artifacts to become proven. |

---

## Relationship To Mission

[Mission Charter](WPILOT-MISSION-v1.md) определяет **назначение** WPilot (Personal WordPress Operations Platform, human-supervised, backup-first).

**Proven Capabilities** фиксирует, **что из этого назначения уже доказано практикой** на DEV — не aspirational scope.

---

## Relationship To Operations

[Operations Manifest](WPILOT-OPERATIONS-MANIFEST-v1.md) описывает **разрешённые** типизированные операции (`operation_id`).

**Proven Capabilities** фиксирует **подмножество**, которое реально выполнялось с evidence. Manifest ⊃ Proven; Proven ⊄ Manifest automatic.

---

## Relationship To Roadmap

Документ **не является** roadmap.

Отсутствие capability здесь **не означает** отсутствие в будущем.  
[metacode-wpilot-plugin-mvp-roadmap.md](metacode-wpilot-plugin-mvp-roadmap.md) остаётся **planned** — не пересматривается этим файлом.

---

## Statistics (v1)

| Metric | Count |
|--------|------:|
| **Proven inspection capabilities** | 11 |
| **Proven plugin REST runtime capabilities** | 9 |
| **Proven content modification capabilities** | 6 |
| **Proven style modification capabilities** | 5 |
| **Proven change management capabilities** | 5 |
| **Proven security & safety capabilities** | 7 |
| **Proven workflow capabilities** | 4 |
| **Total proven capabilities** | **47** |
| **Proven targets** | **6** |
| **Not yet proven (listed areas / items)** | **17** |

---

## Notes

WPilot Proven Capabilities v1 — **evidence layer**.

- **Не** policy layer (см. Mission, Manifest, Bindings).
- **Не** runtime layer.
- **Не** marketing document.
- **Не** capability forecast.

Обновление register: только после нового completed DEV work + evidence + validation + recovery artifact — отдельным revision pass.

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Implements runtime | No |
| Replaces Operations Manifest | No |
| Replaces Roadmap | No |
| Canonical evidence register | Yes |

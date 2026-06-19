# WPilot Runtime Contracts v1

**Classification:** Runtime bridge layer — Core Model v1 → plugin implementation.  
**Status:** Documented v1 (2026-06-19).  
**Scope:** Documentation only. Does not implement code, create Core Layers, or amend Mission Charter.  
**Inputs:** WPILOT-*-v1.md Core stack, [plugin-mvp/](../plugin-mvp/) v0 contracts, in-repo plugin source v0.1, [WPILOT-PROVEN-CAPABILITIES-v1.md](../WPILOT-PROVEN-CAPABILITIES-v1.md).

**Relationship to other doc sets:**

| Doc set | Role |
|---------|------|
| **Core Model v1** (`WPILOT-*-v1.md`) | Policy: *what* is allowed and *how runs are described* |
| **Runtime Contracts v1** (this document) | Bridge: *where* things live, *what* plugin/MARS each owns, MVP execution shape |
| **plugin-mvp v0** | Implementation contracts: exact REST JSON, DB columns, refusal codes |
| **Plugin source** (`plugin/metacode-wpilot/`) | Partial proof: read-only + dry-run only (v0.1) |

---

## Executive Summary

Runtime Contracts v1 переводит завершённый Core Model v1 в реалистичную архитектуру будущего плагина `metacode-wpilot` без создания новых Core Layers.

**Ключевой принцип:** WordPress state живёт в WordPress; execution shadow и audit — в плагине; policy, ChangeSet, evidence и operator workflow — в MARS/Cursor; ни один слой не дублирует authority другого.

**MVP execution unit в плагине:** не полный ChangeSet engine, а **narrow operation run** (`operation_id` + `target` + checksums + `backup_id` + audit), привязанный к ChangeSet через `approval_ref` / `changeset_id` в MARS.

**Verdict:** Core Model и plugin-mvp v0 **согласуемы** с оговорками (см. Conflicts). Следующий этап — **Runtime Prototype** (см. §10), не ещё один architecture pass.

---

## 1. Runtime Boundary

### 1.1 Boundary matrix

| Concern | WPilot Plugin (`metacode-wpilot`) | WordPress (host) | MARS (`C:\AI MARS`) | Cursor workflow |
|---------|-----------------------------------|------------------|---------------------|-----------------|
| **Authority over content** | Scoped write via WP APIs only (planned) | **Source of truth** for pages, posts, options, themes, plugins | None — orchestration/docs only | Human-supervised operator |
| **Auth** | Token hash, bridge flags, DEV confirmation | WP users, capabilities, native REST auth | Plaintext token handoff in `local/tokens/` (operator machine) | Operator holds token; never in git |
| **Inspection reads** | REST `wpilot/v1` read endpoints | `wpdb`, theme/plugin APIs, rendered output | Evidence interpretation, reports | Agent calls REST / reviews output |
| **ChangeSet record** | Execution shadow only (`operation_id`, status, checksums, `backup_id`) | — | **Canonical** `changeset_id`, policy fields, approval, description, evidence paths | Authoring, approval gates |
| **Site Snapshot (logical)** | REST response → transient/generated snapshot | Live state | **Canonical** structured bundles, `snapshot_id` convention, local JSON/HTML | Capture, compare, archive |
| **Diff (logical)** | Dry-run match analysis (subset) | — | **Canonical** diff bundles, operator compare | Build diff, validate |
| **Backup (MVP)** | `wpilot_backups` — `post_content` only (planned) | DB tables, uploads, theme files | Operator mirrors: `backups/wpilot/`, `AI MARS STORAGE/wpilot/` | Trigger backup, store evidence |
| **Rollback** | Restore from plugin backup row (planned) | Hosting/DB restore (external) | Rollback plans, evidence, validation JSON | Execute via REST or escalate |
| **Audit** | `wpilot_audit_log` — sanitized events | WP debug logs (not WPilot-owned) | Run reports, QA checklists | Review trail |
| **Policy** | Hard guards (refusal codes) | — | Mission, Manifest, Bindings, Risk Classes | Must not override policy |
| **Proven capabilities** | — | — | **Canonical** evidence register | Update after DEV proof |

### 1.2 Source of truth

| Entity | Canonical source of truth | Notes |
|--------|---------------------------|-------|
| Live WordPress content | **WordPress DB + filesystem** | Plugin reads/writes through WP APIs only |
| `operation_id` / bindings / risk | **Core Model docs** | Plugin enforces subset via refusal, not full matrix |
| `changeset_id` + approval context | **MARS operator workflow** | Plugin accepts `approval_ref`; does not own approval engine |
| Plugin-created backup content | **`{prefix}wpilot_backups`** | Rollback source for plugin writes only |
| Operator/hosting backups | **External storage** (local STORAGE, hosting panel) | Cited in ChangeSet `backup_path`; not in plugin DB |
| Structured site state (Snapshot Model) | **MARS** (logical bundles) | Plugin provides raw reads; MARS structures |
| Token (plaintext) | **Operator local storage** | Plugin stores hash only |
| Audit trail (full run) | **Split:** plugin DB events + MARS reports | Neither alone is complete for human audit |

### 1.3 Never stored inside the plugin

**EXCLUDED from plugin storage (hard rule):**

- Plaintext WPilot tokens, WP passwords, FTP/DB/hosting credentials
- `wp-config.php`, cookies, session data, auth headers
- Full database dumps, full-site backups, hosting panel exports
- Complete ChangeSet policy records (risk narrative, multi-step approval chains)
- MARS governance documents, Cursor prompts, agent instructions
- Canonical Snapshot/Diff bundles (plugin may emit inputs; MARS owns interpretation)
- Secrets from `.recovery-temp` or operator STORAGE paths

### 1.4 Boundary diagram

```
┌─────────────────────────────────────────────────────────────────┐
│ MARS / Cursor (human-supervised)                                │
│  ChangeSet · Approval · Snapshot bundles · Diff · Evidence      │
│  Proven Capabilities · Site passport · local/tokens · reports   │
└────────────────────────────┬────────────────────────────────────┘
                             │ REST + approval_ref
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ metacode-wpilot plugin                                          │
│  Auth · Guards · Read · Dry-run · Backup row · Audit · Write*   │
│  *write = planned MVP scoped-replace path                       │
└────────────────────────────┬────────────────────────────────────┘
                             │ WordPress APIs only
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ WordPress (Beget host) — live source of truth                   │
│  posts · pages · options · themes · plugins · uploads           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. ChangeSet Runtime Contract

### 2.1 Logical model (unchanged)

Canonical schema remains [WPILOT-CHANGESET-v1.md](../WPILOT-CHANGESET-v1.md). Runtime Contracts **do not** extend Core fields.

### 2.2 Runtime split: plugin vs MARS

| ChangeSet concern | MARS (canonical) | Plugin DB (execution shadow) |
|-------------------|------------------|-------------------------------|
| `changeset_id` | ✓ operator-assigned | ✓ optional `changeset_ref` in audit metadata |
| `created_at`, `description` | ✓ | — |
| `operation_id`, `target_type`, `target_id` | ✓ planning | ✓ per run row in audit; backup links target |
| `risk_class`, policy flags | ✓ | ✓ enforced via guards, not stored as full policy |
| `status` (lifecycle) | ✓ operator workflow | ✓ mapped execution status (see §2.3) |
| `approved_at`, `approved_by` | ✓ | `approval_ref` string only |
| `backup_path` (external) | ✓ | — |
| `backup_id` (plugin) | ✓ cited in evidence | ✓ FK in audit + backups table |
| `validation_result` | ✓ reports/JSON | ✓ checksum + `outcome` in audit |
| `rollback_source` | ✓ | `backup_id` when source = plugin |
| `failure_reason` | ✓ | `reason_code` in audit |

**MARS-only (never plugin tables in MVP):**

- Draft-stage ChangeSets without execute intent
- Parent/child ChangeSet chains (`parent_changeset_id`)
- Full evidence file paths and HTML archives
- Risk class narrative and operator notes
- Cross-site ChangeSet index

### 2.3 Plugin execution status mapping

Plugin does **not** implement full ChangeSet lifecycle. It implements **operation run states**:

| Plugin run state | Maps to ChangeSet status | Trigger |
|------------------|---------------------------|---------|
| `requested` | `approved` or `backup_completed` | REST call received |
| `rejected` | `failed` | Refusal before mutation |
| `backup_created` | `backup_completed` | Backup row inserted |
| `applied` | `applied` | Successful scoped write |
| `validated` | `validated` | Post-write checksum OK |
| `rolled_back` | `rolled_back` | Rollback endpoint success |
| `closed` | `closed` | Operator closes in MARS |

Operator advances ChangeSet `draft` → `approved` **in MARS** before plugin execute. Plugin never creates ChangeSet at `draft`.

### 2.4 MVP persistence model

**Plugin (minimal):**

```
wpilot_backups     — pre-write content snapshot
wpilot_audit_log   — lifecycle events per operation_id
wp_options         — bridge state, token hash
```

**MARS (minimal):**

- JSON/markdown run record per ChangeSet under `C:\AI MARS\local\runtime\` or `C:\AI MARS STORAGE\wpilot\`
- Template: [change-request-template.md](../templates/change-request-template.md) → formalized ChangeSet fields

### 2.5 REST exposure

| Capability | MVP |
|------------|-----|
| Create/read/update ChangeSet | **No** — MARS-only |
| Pass `approval_ref` on write | **Yes** |
| Pass `changeset_id` as optional metadata | **Yes** (audit only) |
| Query run history | **Yes** — `GET /audit` or audit fields in write response (subset) |
| Enforce Bindings matrix | **Partial** — hardcoded allowed ops per endpoint |

---

## 3. Snapshot Runtime Contract

### 3.1 Four snapshot forms

| Form | Definition | Owner | MVP |
|------|------------|-------|-----|
| **Logical snapshot** | Site Snapshot Model v1 object graph (`object_type`, relationships, evidence refs) | MARS | Canonical structure for planning/validation |
| **Stored snapshot** | Persisted JSON/HTML bundle with `snapshot_id` | MARS local/STORAGE | Operator saves REST+HTML captures; **not** plugin table |
| **Generated snapshot** | Structured output from inspection REST (`pages/{id}`, `structure`, `site-info`) | Plugin generates raw; MARS interprets | **Primary MVP path** |
| **Transient snapshot** | In-memory content + checksum during dry-run/validate | Plugin | Exists only for request lifecycle |

### 3.2 MVP snapshot scope

**In scope (L0 + L2 partial + L3 signals):**

| Scope | Source endpoint | `object_type` |
|-------|-----------------|---------------|
| Site identity | `GET /site-info`, `GET /ping` | `site`, `environment` |
| Page content | `GET /pages/{id}` | `page` |
| Builder structure | `GET /pages/{id}/structure` | `shortcode` (nodes) |
| Plugins/themes | `GET /plugins`, `GET /themes` | `active_plugins`, `active_theme` |
| Indexing signals | `GET /indexing-state` | `environment` |

**Out of MVP plugin snapshot store:**

- Footer/header zone models as first-class stored objects (derive from page/structure in MARS)
- `css_fragment` file reads (no REST in v0.1; FTP/manual in MARS)
- Full L1 menu graph
- Persisted `snapshot_id` in plugin DB

### 3.3 Snapshot vs backup (runtime reminder)

| | Snapshot | Plugin backup row |
|---|----------|-------------------|
| Purpose | Describe state | Enable restore |
| Plugin table | No | `wpilot_backups` |
| Content | Interpreted multi-object | `content_before` single field |

---

## 4. Diff Runtime Contract

### 4.1 Where diff is computed

| Diff type | Computed in | MVP |
|-----------|-------------|-----|
| Content checksum delta | **Plugin** | ✓ `before_checksum` / `after_checksum` |
| Exact text match preview | **Plugin** (dry-run) | ✓ `match_count`, zone classification |
| Snapshot → Snapshot (structured) | **MARS/Cursor** | Manual or scripted compare of saved JSON |
| Snapshot → Live | **MARS/Cursor** | Re-fetch REST vs stored snapshot |
| Backup → Live | **MARS/Cursor** | Compare `content_before` export vs live read |
| Structure diff (WPBakery tree) | **MARS/Cursor** | Compare `structure` endpoint outputs |
| CSS diff | **MARS/Cursor** | File diff outside plugin |
| Full-site diff | — | **Excluded** MVP |

### 4.2 Diff objects in MVP

| Diff need | MVP approach | Deferred |
|-----------|--------------|----------|
| Pre-apply expected change | Dry-run `match_count: 1` | Full Diff Model bundle |
| Post-apply validation | Checksum match + operator HTML check | Automated snapshot→live diff engine |
| Drift before execute | `expected_checksum` mismatch refusal | Scheduled drift detection |
| Rollback verification | `restored_checksum` vs backup | Post-rollback snapshot diff |
| Severity classification | Operator in MARS | Auto severity in plugin |

### 4.3 Alignment with Diff Model v1

Plugin dry-run ≡ **Content-level**, `change_type: modified`, single `target_type: page`, scoped fragment — not a general diff engine. Canonical diff bundles remain MARS responsibility.

---

## 5. Operation Execution Contract

### 5.1 Contract template

Each operation defines: **input**, **output**, **errors**, **mandatory checks**, **compute location**.

### 5.2 Inspection operations (R0)

#### `inspect_page`

| Aspect | Contract |
|--------|----------|
| **Input** | `target_id` (page ID or resolved slug→ID in MARS); token |
| **Output** | `id`, `post_type`, `status`, `title`, `content`, `content_checksum` |
| **Errors** | `AUTH_*`, `TARGET_NOT_FOUND`, `POST_TYPE_NOT_ALLOWED`, `READ_NOT_ALLOWED` |
| **Checks** | Token valid; bridge enabled; post type in allowlist |
| **Location** | **Plugin** `GET /pages/{id}` |
| **MVP** | ✓ Implemented (v0.1) |

#### `inspect_shortcode`

| Aspect | Contract |
|--------|----------|
| **Input** | `target_id` (shortcode name/zone); parent `page` ID; token |
| **Output** | Structure nodes from `/structure` + content excerpt; or MARS-extracted fragment from `content` |
| **Errors** | `STRUCTURE_PARSE_FAILED`, `STRUCTURE_SAFE_UNKNOWN`, `TARGET_NOT_FOUND` |
| **Checks** | Page readable; parser safe zone classification |
| **Location** | **Plugin** structure endpoint + **MARS** fragment extraction |
| **MVP** | ✓ Partial — structure map proven; named shortcode object requires MARS interpretation |

#### `inspect_footer`

| Aspect | Contract |
|--------|----------|
| **Input** | `target_id` (`footer:main` or zone key); optional `page_id` anchor |
| **Output** | Footer zone HTML/structure markers (MARS from rendered HTML + page content) |
| **Errors** | Same as page/structure reads |
| **Checks** | DEV scope; no mutation |
| **Location** | **MARS** (rendered HTML audit) + **Plugin** page/structure reads |
| **MVP** | ✓ Proven via combined path; no dedicated `/footer` endpoint |

#### `inspect_css`

| Aspect | Contract |
|--------|----------|
| **Input** | `target_id` (`css_fragment` key, e.g. child-theme path) |
| **Output** | CSS text or matched rules (from file read) |
| **Errors** | File not found, path outside allowed theme dir |
| **Checks** | Read-only; path allowlist |
| **Location** | **MARS** (FTP/file access) — **not** plugin MVP |
| **MVP** | ✓ Proven operationally; **no** plugin endpoint |

### 5.3 Apply operations (R2)

#### `apply_shortcode_change` / `apply_content_change` (MVP collapse)

Runtime MVP implements **one write primitive**: scoped exact replace on `page.post_content`.

| Aspect | Contract |
|--------|----------|
| **Input** | `page_id`, `before_text`, `after_text`, `match_mode: exact_once`, `mode: dry_run\|execute`, `approval_ref`, `expected_checksum` (execute) |
| **Output** | `match_count`, `allowed_zone`, `backup_id`, checksums, `mutation_performed` |
| **Errors** | `MATCH_ZERO`, `MATCH_MULTIPLE`, `FORBIDDEN_EDIT_ZONE`, `CHECKSUM_MISMATCH`, `BACKUP_FAILED`, `WRITE_FAILED`, `APPROVAL_REQUIRED` |
| **Checks** | Auth; bridge+DEV+write_enabled; dry-run before execute; backup before mutation; WPBakery zone safe |
| **Location** | **Plugin** `POST /pages/{id}/scoped-replace` |
| **MVP** | Dry-run ✓; execute **planned** |

**Note:** `apply_shortcode_change` and `apply_footer_change` on DEV were proven via **helpers**, not this endpoint. Runtime maps them to same primitive when target resolves to `post_content` on a known page.

#### `apply_footer_change`

| Aspect | Contract |
|--------|----------|
| **Input** | `target_type: footer`, zone scope; resolves to underlying `page`/`shortcode` content mutation |
| **Output** | Same as scoped-replace + validation flags |
| **Errors** | Zone resolution failure → refuse |
| **Checks** | Primary binding target = `footer`; mechanism may be `shortcode` — document in ChangeSet `description` |
| **Location** | **Plugin** (content field) + **MARS** (zone resolution) |
| **MVP** | Collapsed to page content replace when resolvable |

#### `apply_css_change`

| Aspect | Contract |
|--------|----------|
| **Input** | `target_id` (theme CSS path), patch content |
| **Output** | File checksum before/after |
| **Errors** | Path forbidden, write disabled |
| **Checks** | R2/R3 escalation by blast radius |
| **Location** | **MARS** (FTP) — **outside** plugin MVP |
| **MVP** | **Deferred** from plugin; operational path only |

### 5.4 Recovery operations

#### `validate_change`

| Aspect | Contract |
|--------|----------|
| **Input** | Parent ChangeSet context; `target_id`; expected checksum or validation checklist |
| **Output** | `validation_result` object; pass/fail per check |
| **Errors** | Checksum mismatch, render regression |
| **Checks** | R0 read-only; no mutation |
| **Location** | **Plugin** checksum compare + **MARS** HTML/render checks |
| **MVP** | Partial — plugin checksum; full checklist in MARS |

#### `rollback_change`

| Aspect | Contract |
|--------|----------|
| **Input** | `page_id`, `backup_id`, `approval_ref`, `expected_current_checksum` |
| **Output** | `restored_checksum`, `mutation_performed` |
| **Errors** | `BACKUP_NOT_FOUND`, `CHECKSUM_MISMATCH`, `ROLLBACK_WRITE_FAILED` |
| **Checks** | Plugin backup only; target match; single-use policy optional |
| **Location** | **Plugin** `POST /pages/{id}/rollback` |
| **MVP** | **Planned** — not proven end-to-end |

---

## 6. Backup Runtime Contract

### 6.1 Backup types

| Type | Scope | Store | MVP need |
|------|-------|-------|----------|
| **Plugin content backup** | `post_content` one page/post | `{prefix}wpilot_backups` | **Required** for plugin writes |
| **Operator JSON backup** | Page content, shortcode exports | `C:\AI MARS STORAGE\wpilot\` | **Required** (proven) — parallel trail |
| **HTML/render snapshot** | Rendered page | MARS STORAGE | **Recommended** for validation |
| **Theme CSS backup** | File fragment | MARS/FTP copy | Proven; not plugin |
| **Hosting/DB backup** | Full or partial DB | Beget panel | External; operator responsibility |
| **Full-site backup** | Files + DB | Hosting | **Excluded** plugin MVP |

### 6.2 MVP rules

1. Plugin **must** create backup row before any mutation.
2. Plugin backup **≠** site backup; rollback **only** restores that row's `content_before`.
3. Operator **should** maintain parallel STORAGE backup for audit (proven workflow).
4. ChangeSet `backup_path` may point to STORAGE; plugin uses `backup_id`.
5. CSS/file backups remain MARS-operated until dedicated plugin contract exists.

### 6.3 Not needed in MVP

- Plugin-stored theme file backups
- Media/attachment backups
- Menu/widget option backups
- Automated hosting backup trigger
- Backup deduplication across sites

---

## 7. Plugin Database Model (MVP)

Minimal schema — aligns with [database-contract-v0.md](../plugin-mvp/database-contract-v0.md). **No enterprise extensions.**

### 7.1 Tables

#### `{prefix}wpilot_backups`

| Column | Purpose |
|--------|---------|
| `id` | PK; exposed as `backup_id` |
| `operation_id` | Links to audit/run |
| `changeset_ref` | Optional VARCHAR(64) — MARS `changeset_id` |
| `target_type` | MVP: `page` (extend to `post` when enabled) |
| `target_id` | WP post ID |
| `post_type`, `post_status` | Restore metadata |
| `content_before` | LONGTEXT snapshot |
| `content_checksum` | `sha256:` prefix |
| `created_by_user_id`, `created_at` | Audit |
| `source` | Always `plugin` |
| `rollback_used_at` | Nullable |

#### `{prefix}wpilot_audit_log`

| Column | Purpose |
|--------|---------|
| `id` | PK |
| `operation_id` | Groups lifecycle |
| `event_type` | `request`, `backup_created`, `write_succeeded`, `rolled_back`, … |
| `route` | REST path |
| `actor_type` | `token`, `wp_user`, `system` |
| `target_type`, `target_id` | Nullable |
| `outcome` | `accepted`, `rejected`, `succeeded`, `failed`, `rolled_back` |
| `reason_code` | Refusal code |
| `backup_id` | FK optional |
| `before_checksum`, `after_checksum` | Integrity |
| `metadata_json` | Small JSON: `approval_ref`, `changeset_ref`, `match_count` |
| `created_at` | UTC |

### 7.2 Options (no new tables)

`wpilot_enabled`, `wpilot_dev_confirmed`, `wpilot_write_enabled`, `wpilot_emergency_disabled`, `wpilot_token_hash`, `wpilot_schema_version`, retention hints — per v0 contract.

### 7.3 Relationships

```
wpilot_audit_log.backup_id → wpilot_backups.id
wpilot_backups.target_id   → wp_posts.ID (logical, not FK)
```

### 7.4 Explicitly no tables for

- ChangeSets (full)
- Snapshots
- Diff bundles
- Approval records
- Credentials

---

## 8. REST Contract Surface (MVP minimum)

Namespace: `wpilot/v1`. Envelope per [rest-api-contracts-v0.md](../plugin-mvp/rest-api-contracts-v0.md).

| # | Endpoint | Method | Core `operation_id` | Purpose |
|---|----------|--------|---------------------|---------|
| 1 | `/ping` | GET | — | Liveness; no auth |
| 2 | `/site-info` | GET | `inspect_site`, `inspect_environment` | Site + env signals |
| 3 | `/themes` | GET | `inspect_site` (theme facet) | Active theme |
| 4 | `/plugins` | GET | `inspect_plugin`* | Active plugins list |
| 5 | `/pages` | GET | `inspect_page` | Page index |
| 6 | `/pages/{id}` | GET | `inspect_page` | Page content + checksum |
| 7 | `/pages/{id}/structure` | GET | `inspect_shortcode` (partial) | Builder structure map |
| 8 | `/indexing-state` | GET | `inspect_environment` | DEV isolation signals |
| 9 | `/pages/{id}/replace-text/dry-run` | POST | `draft_*` semantics | Dry-run preview |
| 10 | `/pages/{id}/backups` | POST | (precursor to apply) | Create content backup |
| 11 | `/pages/{id}/scoped-replace` | POST | `apply_content_change`**, `apply_shortcode_change`** | Execute scoped replace |
| 12 | `/pages/{id}/rollback` | POST | `rollback_change` | Restore plugin backup |

\* `inspect_plugin` target gap — endpoint returns plugin list; `target_type: plugin` remains unresolved in Core.  
\** Subtype resolved in MARS ChangeSet before call.

**Deferred beyond MVP minimum:** `/logs`, `/footer`, `/css`, menu/widget endpoints, ChangeSet CRUD, batch ops.

### 8.1 Write request shape (execute)

```json
{
  "mode": "execute",
  "before_text": "...",
  "after_text": "...",
  "match_mode": "exact_once",
  "approval_ref": "cs-2026-06-19-footer-menu-001",
  "changeset_ref": "cs-2026-06-19-footer-menu-001",
  "expected_checksum": "sha256:..."
}
```

### 8.2 Write response shape (success)

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "mutation_performed": true,
    "backup_id": 1,
    "before_checksum": "sha256:...",
    "after_checksum": "sha256:...",
    "target_id": 69
  }
}
```

---

## 9. Proven Capabilities Mapping

| Capability area | DEV proven | Plugin v0.1 now | Runtime Contracts MVP |
|-----------------|------------|-----------------|----------------------|
| `inspect_site` / environment | ✓ REST | ✓ | Map to endpoints 2, 8 |
| `inspect_page` + structure | ✓ | ✓ | Endpoints 5–7 |
| `inspect_footer` / shortcode | ✓ (combined) | Partial | MARS interprets 6–7 |
| `inspect_css` | ✓ FTP | — | MARS-only |
| `inspect_plugin` | ✓ list | ✓ `/plugins` | Target gap persists |
| Dry-run / draft semantics | ✓ | ✓ endpoint 9 | Aligned |
| `apply_*` content/footer/shortcode | ✓ helpers | — | Endpoints 10–11 planned |
| `apply_css_change` | ✓ FTP | — | MARS-only |
| Backup before apply | ✓ | — | Endpoint 10 planned |
| `validate_change` | ✓ JSON checks | Partial checksum | MARS checklist + plugin |
| `rollback_change` | **Not proven** | — | Endpoint 12 planned |
| `restore_backup` | **Not proven** | — | Deferred |
| Full ChangeSet product | — | — | MARS workflow |
| Snapshot/Diff persistence | — | — | MARS local |

**Implement immediately (high confidence):** endpoints 1–9 — already implemented or proven.  
**Next prototype target:** 10 → 11 → 12 chain on `dev.gktriumph.ru`.  
**Remain future:** CSS endpoint, menu API, Factory Mode A structured payloads, EAR consumer integration.

---

## 9A. Runtime Surface Proven By Evidence

**Classification:** Evidence overlay on §8 REST surface — 2026-06-19 freeze.  
**Source reports:** [wpilot-runtime-proof-sprint-report.md](../reports/wpilot-runtime-proof-sprint-report.md), [wpilot-runtime-prototype-sprint-1-report.md](../reports/wpilot-runtime-prototype-sprint-1-report.md), [wpilot-runtime-prototype-sprint-2-report.md](../reports/wpilot-runtime-prototype-sprint-2-report.md).

**Environment:** DEV only — `https://dev.gktriumph.ru`. **Plugin:** v0.3.0 / schema 0.2.0.

### Proven endpoint surface

| # | Endpoint | Method | Proven | Sprint evidence |
|---|----------|--------|--------|-----------------|
| 1 | `/ping` | GET | ✓ | v0.1 operational release |
| 2 | `/site-info` | GET | ✓ | v0.1 + proof sprint baseline |
| 3 | `/themes` | GET | ✓ | v0.1 |
| 4 | `/plugins` | GET | ✓ | v0.1 |
| 5 | `/pages` | GET | ✓ | v0.1 |
| 6 | `/pages/{id}` | GET | ✓ | All sprints — checksum baseline |
| 7 | `/pages/{id}/structure` | GET | ✓ | v0.1; WPBakery validation in proof sprint |
| 8 | `/indexing-state` | GET | ✓ | v0.1 |
| 9 | `/pages/{id}/replace-text/dry-run` | POST | ✓ | v0.1; zone rules refined Sprint 2 |
| 10 | `/pages/{id}/backups` | POST | ✓ | Runtime Proof Sprint — 3/3 PASS |
| 11 | `/pages/{id}/scoped-replace` | POST | ✓ | Sprint 2 — 3/3 PASS (apply + rollback each) |
| 12 | `/pages/{id}/rollback` | POST | ✓ | Runtime Proof Sprint — 3/3 PASS; re-used Sprint 2 |

### Proven operation bindings (execute path)

| `operation_id` | REST route | Proven scope | Not proven beyond |
|----------------|------------|--------------|-------------------|
| `inspect_page` | `GET /pages/{id}` | Read + checksum | — |
| `inspect_site` / `inspect_environment` | `GET /site-info`, `/ping`, `/indexing-state` | Read | — |
| `apply_content_change` | `POST /pages/{id}/scoped-replace` | `page.post_content`, exact once | shortcode/footer/css subtypes as separate endpoints |
| `rollback_change` | `POST /pages/{id}/rollback` | Restore plugin backup row | hosting/DB restore |
| `validate_change` | Checksum in apply/inspect responses | Plugin checksum compare | Full MARS HTML checklist automation |
| (backup precursor) | `POST /pages/{id}/backups` | Pre-write snapshot | Non-page targets |

### Proven cross-cutting runtime behaviours

| Behaviour | Evidence |
|-----------|----------|
| `operation_id` (`op_<uuid>`) per run | All write/recovery REST responses |
| `wpilot_audit_log` lifecycle | backup, scoped_replace, rollback events |
| `sha256:` checksum integrity | inspect → backup → apply → rollback chain |
| WPBakery `post_content` safety | Proof sprint page 38; Sprint 2 pages 38, 954 |
| Refusal on failed post-write validation | Sprint 2 Run #2 first attempt — `POST_WRITE_VALIDATION_FAILED` |
| No auto-rollback on failed apply | Sprint 2 policy — `rollback_available: true` when backup exists |

### Not proven (runtime surface)

| Item | Status |
|------|--------|
| `/footer`, `/css`, menu/widget endpoints | Not implemented |
| Production host | Not proven |
| Batch/mass scoped-replace | Not proven |
| `apply_css_change` via plugin | MARS/FTP only |
| ChangeSet REST CRUD | MARS-only by design |

**Deploy note:** Proven deploy path = **FTP upload of plugin source files**. No in-repo or STORAGE ZIP deploy package for v0.3.0 at freeze time.

---

## 10. Conflicts, Gaps, Risks, Recommendation

### 10.1 Core ↔ Runtime conflicts

| ID | Conflict | Severity | Resolution |
|----|----------|----------|------------|
| C1 | ChangeSet example uses `apply_footer_change` + `target_type: shortcode`; Bindings primary = `footer` | Medium | MARS resolves zone→content; plugin mutates `post_content`; document both in `description` |
| C2 | Two backup roots: `C:\AI MARS\backups\` vs `C:\AI MARS STORAGE\wpilot\` | Medium | Runtime: plugin `backup_id` canonical for rollback; STORAGE path = operator evidence mirror; reconcile in operator runbook |
| C3 | `inspect_rendered_html`, `inspect_page_storage` proven but not in Manifest | Medium | Map to `inspect_page` + MARS evidence export; Manifest amendment optional, not blocking prototype |
| C4 | plugin-mvp `target_type` backup enum `post\|page` vs Registry full enum | Low | Plugin stores WP post types; Registry `target_type` in audit metadata |
| C5 | v0.1 plugin has `write_enabled`; v0 contracts use `wpilot_enabled` + DEV only | Low | Align option names in prototype pass |
| C6 | `inspect_plugin` target gap vs `/plugins` endpoint | Low | Endpoint serves list; ChangeSet `target_type` uses `site` or omits until Registry update |

### 10.2 Runtime Gaps

| Gap | Impact | Owner |
|-----|--------|-------|
| No plugin write/rollback endpoints shipped | Blocks formal proof of apply/recovery via bridge | Plugin prototype |
| No ChangeSet↔REST formal schema in Core | Operator convention only | Acceptable for MVP |
| No plugin CSS/footer/menu endpoints | Ops stay split MARS/plugin | Documented |
| Rollback not proven | Recovery story incomplete | Prototype priority |
| No automated Bindings enforcement | Manual operator discipline | Expected human-supervised |
| EAR ↔ WPilot harmonization | SAFE UNKNOWN | Future |

### 10.3 Architecture Risks

| Risk | Mitigation |
|------|------------|
| Treating plugin backup as site backup | Labels, refusal scope, operator training |
| ChangeSet in plugin DB (overengineering) | Shadow fields only; no full lifecycle engine |
| WPBakery string replace breaks structure | Zone classifier + dry-run + exact_once refusal |
| Dual write paths (helper + REST) on DEV | Retire helpers after REST proof; single path |
| Token in repo leak | local-storage-policy; hash-only in WP |

### 10.4 Overengineering Risks

| Temptation | Avoid |
|------------|-------|
| ChangeSet REST CRUD service | MARS files + templates |
| Snapshot/Diff tables in plugin | MARS local JSON |
| Full Bindings engine | Endpoint allowlist |
| Generic apply framework | One scoped-replace primitive |
| Approval Layer document | `approval_ref` string + MARS gate |

### 10.5 Simplification Opportunities

1. **Collapse apply subtypes** to one `scoped-replace` primitive for MVP; differentiate in MARS ChangeSet `operation_id`.
2. **Reuse dry-run endpoint** as draft operation — no separate draft engine.
3. **Single page post type** in write MVP (`wpilot_allowed_post_types: ["page"]`).
4. **Checksum-only validate** in plugin; rich validation stays MARS JSON checklists (proven pattern).
5. **Audit log as run history** — no separate `/logs` endpoint initially.

### 10.6 Final recommendation: next stage

| Option | Description |
|--------|-------------|
| **A. Plugin MVP v2 Architecture** | Another documentation pass before code |
| **B. Runtime Prototype** | Implement backup → scoped-replace → rollback on DEV |

**Selected: B — Runtime Prototype**

**Why:**

1. Runtime Contracts v1 completes the documentation bridge Core → plugin-mvp (this pass).
2. Plugin v0.1 already installs with read + dry-run — **narrowest gap is write path**, not architecture.
3. Proven Capabilities shows apply/backup/validate work on DEV via helpers — **risk is plugin formalization**, not feasibility.
4. `rollback_change` explicitly **not proven** — only a prototype can close this.
5. Further architecture (v2) without execute proof risks **documentation drift** (Core Architecture Review warning).

**Prototype scope (bounded):**

1. Implement `POST /pages/{id}/backups` + `scoped-replace` execute + `rollback` per v0 contracts.
2. Live DEV proof on one page (e.g. page 69 pattern).
3. Update Proven Capabilities register.
4. Retire temporary PHP helpers for that operation class.

**Do not start:** Approval Layer, Validation Layer, Evidence Layer, Runtime Layer as Core docs; multisite; production; CSS write endpoint; Factory Mode A pipeline.

---

## Appendix A — Document map

| Document | Status after Runtime Contracts v1 |
|----------|-----------------------------------|
| Core Model `WPILOT-*-v1.md` | Unchanged canonical policy |
| `plugin-mvp/*-v0.md` | Implementation detail; subordinate to this bridge |
| `runtime-contracts/WPILOT-RUNTIME-CONTRACTS-v1.md` | **Canonical runtime bridge** |
| `plugin/metacode-wpilot/` | Implementation evidence |
| Phase 1 ops docs | Operational companions; Rollback v1 / local-storage-policy cited |

## Appendix B — Metadata

| Field | Value |
|-------|-------|
| Version | v1 |
| Date | 2026-06-19 |
| Core layers created | 0 |
| Mission/Charter changed | No |
| Code changed | No |
| Implements runtime | No — contracts only |

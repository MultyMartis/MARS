# ISEO-SU WPILOT SOURCE AND ROUTE AUDIT v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 4B  
**Date:** 2026-07-24  
**Source:** `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` (unchanged this task)  
**Mode:** Static source inspection only

---

## 1. Source Status

| Field | Value |
|-------|-------|
| **Plugin name** | MetaCODE WPilot |
| **Header Version** | `0.3.0` |
| **Constants VERSION** | `0.3.0` |
| **SCHEMA_VERSION** | `0.2.0` |
| **REST namespace** | `wpilot/v1` |
| **RUNTIME_MATURITY** | `proven_content_writes` |
| **ENVIRONMENT constant** | `DEV` (label; not a host autodetection gate) |
| **Requires PHP / Tested up to** | **Absent from plugin header** — contract incomplete |
| **uninstall.php** | **Absent** |
| **Multisite-specific code** | Not implemented beyond `is_multisite()` reporting in site-info |

---

## 2. Plugin Lifecycle Hooks

| Hook | Behavior |
|------|----------|
| `register_activation_hook` → `WPilot_Settings::activate` | Force `bridge_enabled=false`, `write_enabled=false`, `emergency_disabled=false`, `dev_confirmed=false`; refresh version fields; `WPilot_Schema::install_or_upgrade()` creates/upgrades tables |
| `register_deactivation_hook` → `WPilot_Settings::deactivate` | Disables bridge + write; preserves token hash and other options |
| Uninstall | **No uninstall hook/file** — options/tables retention on delete is **SAFE UNKNOWN / likely retained** |
| `plugins_loaded` | Boots singleton; loads textdomain; registers admin menu + REST |
| Cron / scheduled events | **None found** |
| Frontend hooks | **None found** (admin + REST only) |
| External HTTP (`wp_remote_*`) | **None found** |

Activation **does** create DB tables (`{prefix}wpilot_backups`, `{prefix}wpilot_audit_log`) and options. Activation alone should **not** mutate frontend content; bridge remains off.

---

## 3. Options and Defaults

**Option name:** `wpilot_options`  
**Schema flag option:** `wpilot_schema_valid`

| Key | Default after `defaults()` / activation posture |
|-----|--------------------------------------------------|
| `bridge_enabled` | `false` |
| `write_enabled` | `false` |
| `emergency_disabled` | `false` |
| `token_hash` | `''` (no token) |
| `dev_confirmed` | `false` |
| `allowed_post_types` | hardcoded sanitize → `array( 'page' )` only |
| Connection metadata fields | `last_connection_status=never`, empty timestamps |
| Retention | `retention_days=30`, `backup_retention_max=10` |

**Public REST after activation:** only `GET /wpilot/v1/ping` (`permission_callback` `__return_true`). Ping exposes non-secret status flags (`bridge_enabled`, `write_enabled`, state label) — **no token**.

Admin capability: `manage_options`. Admin nonces: `wpilot_admin_action` / `wpilot_nonce`.

---

## 4. Authentication

| Topic | Source behavior |
|-------|-----------------|
| Header | `X-WPilot-Token` with fallback header name `x_wpilot_token` |
| Storage | Password hash via `wp_hash_password` / `wp_check_password` — **not plaintext** in DB |
| Comparison | `wp_check_password` (not weak `==`) |
| Generation | Prefix `wpilot_` + 48-char password; plaintext returned once to admin UI |
| Bridge gate | Required for authenticated routes via `WPilot_Environment::operational_readiness` |
| DEV confirm | `dev_confirmed` required for operational readiness |
| Emergency | `emergency_disabled` blocks operational routes |
| Write gate | `write_enabled` required for dry-run, rollback, scoped-replace (backup create does **not** require write_enabled) |
| Route `permission_callback` | `read_permission_callback` returns **`true`** for all registered routes except ping uses `__return_true` — **real auth is inside handlers** |

---

## 5. REST Route Inventory

Namespace base: `/wp-json/wpilot/v1`

| Route | Method | Auth | Bridge | write_enabled | Params | Target | Mutation | Backup | Rollback relation | Proven (DEV) | i-seo.su note |
|-------|--------|------|--------|---------------|--------|--------|----------|--------|-------------------|--------------|---------------|
| `/ping` | GET | No | No | No | — | plugin status | No | — | — | PROVEN DEV | Safe public presence check; do not treat as auth |
| `/site-info` | GET | Token | Yes | No | — | site meta | No | — | — | PROVEN DEV | Will reveal PHP/WP versions when authorized |
| `/themes` | GET | Token | Yes | No | — | active theme | No | — | — | PROVEN DEV | Expect `iseoblog` |
| `/plugins` | GET | Token | Yes | No | — | active plugins | No | — | — | PROVEN DEV | Useful to close active-plugin UNKNOWN |
| `/pages` | GET | Token | Yes | No | — | pages ≤50 | No | — | — | PROVEN DEV | WP pages only |
| `/pages/{id}` | GET | Token | Yes | No | `id` | page `post_content` | No | — | — | PROVEN DEV | Raw content disclosure — charter needed |
| `/pages/{id}/structure` | GET | Token | Yes | No | `id` | WPBakery signals | No | — | — | PROVEN DEV | No WPBakery expected on i-seo.su |
| `/indexing-state` | GET | Token | Yes | No | — | blog_public signals | No | — | — | PROVEN DEV | Read-only |
| `/pages/{id}/replace-text/dry-run` | POST | Token | Yes | **Yes** | JSON find/replace/scope… | page content analysis | No | — | pre-write | PROVEN DEV | GATE 6E+ only |
| `/pages/{id}/backups` | POST | Token | Yes | No | JSON approval/changeset/reason | page backup row | DB insert | Creates plugin backup | Enables rollback | PROVEN DEV | Still a DB write; needs charter |
| `/pages/{id}/rollback` | POST | Token | Yes | **Yes** | `backup_id`, `approval_ref`, checksum | page content | **Yes** | Uses backup | Restores content | PROVEN DEV | Production write — later gate |
| `/pages/{id}/scoped-replace` | POST | Token | Yes | **Yes** | `search`, `replace`, `approval_ref`… | page content | **Yes** | Auto pre-backup | Rollback via backup_id | PROVEN DEV | Production write — later gate |

Exact count: **8 read-oriented registrations** (ping + 7 authenticated reads including dry-run as POST analysis) + **3 mutating write/recovery POSTs** (backups/rollback/scoped-replace) — matches constants READ=8 / WRITE=4 when dry-run counted in write-endpoint family per `WRITE_ENDPOINT_COUNT=4` (dry-run + backups + rollback + scoped-replace).

---

## 6. Read Capabilities

Implemented for `post_type=page` only: list, single (includes `content_raw` + checksum), structure/WPBakery signals, themes, plugins, site-info, indexing-state, public ping.

**Not implemented:** CPT inventory/write, ACF field API, menus, widgets, media library, theme file edits, static HTML, filesystem, cache purge, DB admin.

---

## 7. Dry-run Capabilities

`WPilot_Dry_Run`: exact-match analysis; size limits; UTF-8 checks; refuses introducing shortcode-like `[]` or `<script>/<style>` in replace; WPBakery zone checks; requires `write_enabled` even though no content mutation.

---

## 8. Backup Capabilities

Plugin-owned table `{prefix}wpilot_backups` stores `post_content` before-state + checksum. Requires bridge + token + valid schema. Does **not** replace Beget full backup. Retention knobs exist in options.

---

## 9. Write Capabilities

Only scoped exact-once replace on **page** `post_content` via `scoped-replace`, gated by write readiness + `approval_ref`. No theme/plugin/file/static mutation APIs.

---

## 10. Rollback Capabilities

`POST .../rollback` restores from plugin backup with optional checksum guard and required `approval_ref`. Requires `write_enabled`.

---

## 11. Audit and Connection Tracking

| Feature | Implementation |
|---------|----------------|
| Audit log | `{prefix}wpilot_audit_log` via `WPilot_Audit_Service` |
| Connection tracker | Options fields for success/failure/endpoint; no token/payload storage |
| Logging | Bounded `error_log` only when `WP_DEBUG` |

---

## 12. Unsupported Surfaces (for i-seo.su)

Must remain out of WPilot mutation scope unless separately proven and chartered:

- static HTML / shared `css/` `js/`
- calculator / tariff PHP handlers / `/tariff-calc`
- theme templates (`page-home.php`, etc.)
- ACF options / field groups
- CPT `offer` (candidate) and unresolved web-KP files
- menus/widgets/media/cache purge
- Jetpack / WP-Optimize configuration

---

## 13. Security Review

**Bounded static review — not a full professional security audit.**

| Finding | Severity | Notes |
|---------|----------|-------|
| Token hashed at rest; `wp_check_password` | Positive | |
| Bridge/write off by default on activate | Positive | |
| Only `/ping` intentionally public | Positive | |
| `permission_callback` always true | Medium process risk | Auth must remain in every handler; currently present |
| Raw `content_raw` on page read | Medium disclosure | Charter + least-privilege target pages |
| Activation creates tables | Low/expected | Needs Beget backup first |
| No uninstall cleanup | Low | Orphan tables/options possible |
| Incomplete Requires/Tested headers | Medium contract gap | Conditionally accepted |
| No unserialize/eval/arbitrary FS APIs found | Positive (bounded grep) | |
| `$wpdb` uses prepare/insert/update patterns | Acceptable for plugin tables | |
| Admin uses capability + nonce pattern | Positive (source present) | |

---

## 14. Compatibility Notes

See `ISEO-SU-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md`. Key: WP 7.0.2 uses standard APIs observed; PHP runtime UNKNOWN; hybrid site means WPilot covers only WP-owned page content.

---

## 15. SAFE UNKNOWN

| Item | Why |
|------|-----|
| Exact PHP syntax pass (`php -l`) | PHP binary unavailable on agent host |
| Uninstall residual behavior | No uninstall.php |
| Whether host strips `X-WPilot-Token` | Needs GATE 6D |
| Whether Admin JS challenge affects REST clients | Needs GATE 6D |
| Production write safety | Explicitly out of Phase 4B GO scope |

---

*Source and route audit v1 · 2026-07-24 · static only.*

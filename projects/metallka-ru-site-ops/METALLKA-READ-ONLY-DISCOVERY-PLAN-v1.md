# METALLKA — Read-Only Discovery Plan v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** ACCEPTED (Phase 2A — preparation)  
**Date:** 2026-07-25  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Site:** `https://metallka.ru/`  

**Purpose:** Staged future inspection plan for Gate A / Phase 2B.

```text
THIS PLAN DOES NOT AUTHORIZE ACCESS.
Phase 2B must not start automatically.
```

Governing charter: [METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md](METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md)  
STOP rules: [METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md](METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md)  
Evidence: [METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md](METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md)

---

## Global rules for all stages

| Rule | Requirement |
|------|-------------|
| Approval | Gate A approval string required before authenticated / intrusive stages |
| Mutation | **None** |
| Fix-while-discovering | **Forbidden** |
| Analogy fill | **Forbidden** |
| Secrets in REPORT | **Forbidden** |
| Vulnerability probing | **Forbidden** |
| Login guessing / enumeration abuse | **Forbidden** |
| WPilot install / token / bridge / REST | **Forbidden** under this plan |

Stages may be skipped or deferred if a STOP condition fires or access class is unavailable. Record gaps as SAFE UNKNOWN.

---

## STAGE R0 — PUBLIC SURFACE

**When:** Only after Gate A if public inspection is included in the approved scope (or separately if operator authorizes public-only subset).

Read-only public browser / HTTP inspection. Capture:

- Canonical domain  
- HTTPS  
- Redirect behavior  
- Public routes (bounded, non-abusive)  
- Visible WordPress fingerprints **only if reliable**  
- Headers  
- `robots.txt`  
- Sitemap presence  
- Representative pages  
- Page structure  
- Frontend assets  
- Obvious cache / CDN hints  

**Forbidden:** vulnerability probing · enumeration abuse · login guessing.

---

## STAGE R1 — HOSTING / RUNTIME METADATA

**When:** After explicit access approval covering hosting metadata and/or filesystem read.

Capture (no writes):

- Hosting provider  
- PHP version  
- Webserver  
- Docroot  
- Filesystem layout  
- Backup mechanism  
- Logs availability  
- Staging  
- Cron management  

---

## STAGE R2 — WORDPRESS CORE

Read only:

- WordPress version  
- Site URL / Home URL  
- Multisite  
- Permalink model  
- Language  
- Timezone  
- Debug / log status  
- Admin roles relevant to ops  
- DB prefix only if safely visible and operationally needed  

**Do not** export users or sensitive personal data.

---

## STAGE R3 — THEMES

Map:

- Active parent theme  
- Active child theme  
- Exact versions  
- Update state  
- Child overrides  
- Custom theme files  
- Parent modifications if detectable  
- The7 status / version  

**Do not** update anything.

---

## STAGE R4 — PLUGINS

Inventory:

- Active  
- Inactive materially relevant  
- MU plugins  
- Drop-ins  
- Versions  
- Custom plugins  
- WPBakery  
- ACF  
- Forms  
- SEO  
- Cache  
- Security  
- Code Snippets  
- WPilot presence  

**No** activation / deactivation.

---

## STAGE R5 — PAGE / WPBAKERY MAP

Select representative pages. For each:

- ID · URL · type · status · parent · template · builder  
- Raw `post_content` classification  
- `vc_row` · `vc_column` · `vc_column_text` · `vc_raw_html`  
- Custom shortcodes  
- The7 elements  
- Global / shared block references  
- Page-specific CSS / meta  

**Do not** change page content.

---

## STAGE R6 — THE7 OWNERSHIP

Map (read only):

- Theme Options  
- Page meta  
- Global templates  
- Header · footer · sidebar  
- Custom CSS  
- Typography / layout ownership  
- The7-specific builder / templates  
- Theme-owned global elements  

---

## STAGE R7 — NAVIGATION / FORMS

**Menus:** IDs / names · locations · mobile variation · header relation.

**Forms:** plugin · form IDs · page usage · recipient metadata **without** exposing sensitive credentials · SMTP owner · webhook / CRM existence · spam protection.

**Do not** send test forms yet.

---

## STAGE R8 — ACF / CUSTOM DATA

If ACF exists, determine schema ownership:

- DB · PHP · `acf-json` · options pages  

Map only material field groups / content ownership.

**Do not** assume ACF is source of truth.

---

## STAGE R9 — CUSTOM CODE

Inspect read-only:

- Child `functions.php`  
- Custom plugins · MU plugins · Code Snippets  
- Custom JS / CSS  
- `add_shortcode` registrations  
- `wp_head` / `wp_footer` injection  
- Analytics / pixels · integrations · redirects  
- `.htaccess` rules  
- `wp-config` custom blocks  

Sensitive values must be **redacted**.

---

## STAGE R10 — CACHE / INFRASTRUCTURE

Map:

- Page cache · object cache  
- `advanced-cache.php` · `object-cache.php`  
- Optimization / minification  
- The7 generated cache / assets  
- Hosting cache · CDN  
- WAF / ModSecurity hints  
- PHP OPcache where visible  

**No purge.**

---

## STAGE R11 — BACKUP / RESTORE

Establish actual restore model:

- Hosting-native backup  
- DB restore · file restore · plugin rollback  
- Emergency disable method  
- Responsible operator · restore scope  

**Do not** trigger backup creation in Phase R discovery unless separately approved.

---

## STAGE R12 — WPILOT COMPATIBILITY

**Inspect only.** Check:

- WPilot already present?  
- Duplicate / ghost directories?  
- Existing `wpilot_options`?  
- Existing WPilot tables?  
- REST namespace collision?  
- Security plugin / header restrictions  
- Custom REST blocking  
- Whether `X-WPilot-Token` is likely forwardable  
- WordPress / PHP compatibility against current RC6 source  
- The7 / WPBakery risks  

**Do not** install WPilot · create token · enable bridge.

---

## Future output artefacts (populate after discovery — not now)

| Stage cluster | Primary artefacts |
|---------------|-------------------|
| R0–R2 | SITE-PASSPORT · ACCESS-MODEL · WP-ENTITY-MAP |
| R3–R5 | THE7-WPBAKERY-MAP · PAGE-INVENTORY · PLUGIN-INVENTORY |
| R7 | FORM-MAP |
| R9 | CUSTOM-CODE-MAP |
| R10 | CACHE-MAP |
| R11 | BACKUP-ROLLBACK-MODEL |
| R12 | WPILOT-COMPATIBILITY-ASSESSMENT |
| Cross-cutting | LOCAL-MIRROR-DECISION |

Full names listed in the discovery charter §7.

---

## Stage order recommendation

Preferred sequence: **R0 → R1 → R2 → R3 → R4 → R5 → R6 → R7 → R8 → R9 → R10 → R11 → R12**.

R11 may be partially filled from operator intake before filesystem work. R12 depends on R1–R4 evidence. Stop and escalate on any STOP condition rather than reordering into mutation.

---

*Read-Only Discovery Plan v1 · Phase 2A preparation · access NOT AUTHORIZED.*

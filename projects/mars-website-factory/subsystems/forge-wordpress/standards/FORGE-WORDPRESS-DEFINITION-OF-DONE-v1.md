# Forge WordPress — Definition of Done v1

**ID:** FW-S-19  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** C  

A WP Forge site is **not done** because the frontend “looks ready”.

---

## Checklist

| Domain | Done means |
|--------|------------|
| Admin UX | Localized, curated fields, Site Settings SoT, no global debug notices, Dashboard widget; **feature discoverable in normal Admin IA** |
| **CMS / editor workflows** | P1b maps exist; [EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md) PASS (change phone globally, add entity, hide section, internal CTA) |
| Frontend | Templates match approved design; empty Admin data does not show demo leftovers |
| Responsive | Desktop/tablet/mobile per design breakpoints |
| Real devices | Physical QA for device-specific features ([FW-S-17](FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md)) |
| Accessibility basics | One H1; keyboard nav; focus; form labels; `prefers-reduced-motion` |
| SEO | Title/description owner; canonical; no duplicate SEO plugins |
| Sitemap | Native sitemap on **final** host after cutover |
| Forms | Handler + nonce + anti-spam |
| SMTP | Proven delivery on final domain |
| Redirects | Manifest PASS; no loops; query preserved |
| Users | No leftover bootstrap/`@localhost` admins; roles correct |
| System status | Dashboard current; WPilot write state known; **no stale cutover/host steps** |
| Source/prod parity | Exact-file hashes MATCH for product code |
| Source/prod parity | Exact-file hashes MATCH for product code |
| Backup | Named full backup at last freeze/cutover |
| Git | Canonical checkpoint; secrets absent |
| Environment | `WP_ENVIRONMENT_TYPE` correct; debug off in prod |
| Webroot hygiene | [FW-S-20](FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md) PASS |
| DNS | Intended A/NS; **mail zone intact** |
| SSL | Valid on canonical host |
| Indexing | Open only after indexing gate |
| Final crawl | 2xx/redirects as designed; no `.test`/`localhost` in HTML |

Use [QA matrix](../templates/FORGE-WORDPRESS-QA-MATRIX-v1.md) to evidence the rows.

---

## Operational status panel (MEDIUM / HIGH / CUTOVER)

An operator status panel is **part of production state**, not decorative Admin UI.

For waves that change operator-visible runtime state (domain, DNS, SSL, SMTP, indexing, environment, source/runtime parity, backup baseline, module lifecycle, migration, cutover):

| Check | Done means |
|-------|------------|
| Dashboard / status panel updated in the **same wave** | PASS |
| Stale steps removed (no “future host”, no “NS switch pending” after cutover) | PASS |
| Actual host / environment shown | PASS |
| Current open tails shown | PASS |
| Last verification updated from a real check | PASS |

```text
MAJOR PRODUCTION WAVE IS NOT DONE WHILE OPERATOR STATUS UI IS STALE
```

Prefer runtime reads (WordPress/PHP versions, `home`/`siteurl`, indexing, debug, WPilot, mail suppression, core version). Use stored metadata only for wave label, backup acknowledgement, human approval, and facts that cannot be derived in-process.

---

## Admin feature discoverability (MEDIUM / HIGH)

An Admin feature is **not done** because its page, callback, or backend exists.

It is done only when the intended editor can **discover, open, use, save, and revisit** it through the normal Admin information architecture (left menu / declared Site Settings parent). Hidden URLs, source-code knowledge, and report-only paths do not count.

Acceptance sequence:

```text
REGISTERED → VISIBLE → ACCESSIBLE → EDITABLE → SAVE/RELOAD → OPERATOR DISCOVERABLE
```

Do not accept a wave that only proves `render_page()` / a direct `admin.php?page=` callback. Inspect the **visible** `$submenu` of the editor-facing parent (ACF `redirect => true` may rewrite the WP parent slug).

```text
AN ADMIN FEATURE IS NOT DONE BECAUSE ITS PAGE OR BACKEND EXISTS
```

---

*FW-S-19 v1.2 — P18B operational status panel; P18C-FU01 Admin discoverability.*

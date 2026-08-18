# Forge WordPress Plugin Governance Standard v1

**Document type:** Governance standard  
**Version:** v1  
**Date:** 2026-06-22 (v1.1 production addendum 2026-08-18)  
**Stage:** FW-02 + FP-0002 production lessons  
**Validation:** WV4

**Artifact:** [FORGE-WORDPRESS-PLUGIN-REGISTER-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-PLUGIN-REGISTER-TEMPLATE-v1.md)

---

## 1. Purpose

Mandatory plugin register per project. Prevents "install because faster" without risk and duplication assessment.

---

## 2. Register fields (per plugin)

| Field | Description |
|-------|-------------|
| **Plugin** | Name + slug |
| **Purpose** | Why it exists on this project |
| **Category** | See §3 |
| **Required / optional** | `required` \| `optional` \| `dev-only` |
| **Owner** | Who approves keeping it |
| **License** | GPL, commercial, etc. |
| **Data ownership** | What data it stores |
| **Configuration owner** | Who configures |
| **Update owner** | Who applies updates |
| **Security status** | `approved` \| `conditional` \| `legacy` \| `prohibited` \| `unknown` |
| **Replacement** | Alternative if removed |
| **Removal impact** | What breaks |
| **Compatibility** | WP/PHP version notes |
| **WPilot responsibility** | Ops touch this plugin? `yes` \| `no` \| `limited` |

---

## 3. Categories

| Category | Examples |
|----------|----------|
| **architecture-critical** | ACF Pro, custom functionality plugin |
| **content/editor** | Classic Editor disable, block plugins |
| **SEO** | Yoast, Rank Math |
| **forms** | Contact Form 7, Fluent Forms |
| **SMTP** | WP Mail SMTP |
| **performance** | Caching, image optimization |
| **security** | Wordfence, limit login |
| **backup** | UpdraftPlus |
| **migration** | Duplicator (dev only) |
| **operational** | metacode-wpilot |
| **development-only** | Query Monitor — not production |
| **required-infrastructure** | ACF Pro, SMTP (one), host-required |
| **project-functional** | `{project}-functionality` |
| **editor-tool** | Classic Editor — only if Mode requires |
| **temporary-migration** | Duplicator, search-replace CLI wrappers — **REMOVE BEFORE PRODUCTION** |
| **avoid** | second SEO, second cache, page builder as primary (Mode A) |

---

## 4. Status definitions

| Status | Meaning |
|--------|---------|
| **approved** | In register; version pinned; WV4 pass |
| **conditional** | Allowed with documented constraints |
| **legacy** | Pre-existing; Mode C; sunset plan |
| **prohibited** | Must not install — e.g. duplicate SEO plugins |
| **unknown** | Not assessed — **blocks release** |

---

## 5. Installation policy

| Rule | Detail |
|------|--------|
| No install without register entry | Human approval |
| No duplicate capability | One SEO, one SMTP, one cache — justify duplicates |
| No nulled/pirated plugins | **BLOCKER** |
| Dev-only plugins not on production | Enforced in RELEASE-MANIFEST |
| Page builders as primary | **prohibited** Mode A — legacy Mode C only |

---

## 5.1 Before installing a plugin (required questions)

1. Can WordPress **core** already do it (menus, sitemap, privacy, application passwords)?  
2. Does an existing **WP Forge module** already own it?  
3. Will it **duplicate** SEO / cache / forms / sitemap / schema / analytics injection / image optimization?  
4. Maintenance quality (updates, WP/PHP compatibility, abandoned)?  
5. Security / update footprint?  
6. Client editor impact (new menus, upsell nags, capability leaks)?

If two answers are “yes, someone else owns this,” **do not install**.

---

## 5.2 One-owner collision table

Silent duplicate output is a **BLOCKER**.

| Concern | One owner | If Yoast / Rank Math / other exists |
|---------|-----------|-------------------------------------|
| SEO titles/descriptions | WP Forge SEO module **or** SEO plugin — not both writing `<title>` | WAD: plugin owns output; Forge fields disabled **or** opposite |
| XML sitemap | native `wp_sitemaps_*` **or** SEO plugin sitemap — not both public | Disable one; 301 the other if needed |
| Forms | Forge handler **or** CF7/Fluent — not two AJAX owners on one form | |
| Redirects | one redirect plugin **or** server/Forge manifest | |
| Cache / minify | [PERFORMANCE-BASELINE](FORGE-WORDPRESS-PERFORMANCE-BASELINE-v1.md) | |
| Schema | one JSON-LD owner | |
| Analytics injection | Site Settings empty-safe **or** GTM plugin — not both | |
| Image optimization | one | |

---

## 6. WPilot plugin separation

| Plugin | Classification |
|--------|----------------|
| `{project}-functionality` | architecture-critical — project code |
| `metacode-wpilot` | operational — WPilot ops only |
| Third-party | Per category above |

WPilot plugin is **not** a substitute for project functionality plugin.

---

## 7. WV4 blocking

| Condition | Severity |
|-----------|----------|
| Unknown plugin on production manifest | **BLOCKER** |
| Known vulnerable version | **BLOCKER** |
| Prohibited plugin installed | **BLOCKER** |
| Duplicate SEO plugins | **BLOCKER** |
| Dev-only plugin in production register | **MAJOR** |

---

## Related documents

- [FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md)
- [FORGE-WORDPRESS-CODE-OWNERSHIP-BOUNDARIES-STANDARD-v1.md](FORGE-WORDPRESS-CODE-OWNERSHIP-BOUNDARIES-STANDARD-v1.md)
- [FORGE-WORDPRESS-PRODUCTION-UPDATE-SOP-v1.md](../runbooks/FORGE-WORDPRESS-PRODUCTION-UPDATE-SOP-v1.md)
- [FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md](FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md)

---

*Plugin governance standard v1.1 — register mandatory; one-owner collisions explicit.*

# Forge WordPress Plugin Governance Standard v1

**Document type:** Governance standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
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
- [standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md](FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md)

---

*Plugin governance standard v1 — register mandatory.*

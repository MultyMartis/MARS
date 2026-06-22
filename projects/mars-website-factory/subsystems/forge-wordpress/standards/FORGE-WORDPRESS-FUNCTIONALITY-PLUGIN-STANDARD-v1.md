# Forge WordPress Functionality Plugin Standard v1

**Document type:** Architecture standard (L5/L6)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Rules source:** R-TF-01–03; [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md)

---

## 1. Purpose

Separate **presentation** (theme) from **persistent functionality** (plugin). Define proportionality — no boilerplate plugin for trivial sites.

---

## 2. Theme owns

| Domain | Examples |
|--------|----------|
| Presentation | Templates, template parts |
| Visual components | Section markup, CSS/JS enqueue for layout |
| Theme-specific assets | Compiled Factory assets |
| Visual layout behavior | Menus display, template routing |

---

## 3. Plugin or MU-plugin may own

| Domain | Examples |
|--------|----------|
| Persistent CPT | `register_post_type` |
| Persistent taxonomies | `register_taxonomy` |
| Business logic | Custom queries, shortcodes with data |
| Integrations | CRM hooks, webhooks |
| Reusable functionality | Shared across theme changes |
| REST operations | Custom endpoints with permission callbacks |
| Data migrations | Versioned upgrade routines |
| ACF registrations | Local JSON load path, options pages |
| Theme-survival logic | Must survive theme switch |

**MU-plugin:** Use when site policy requires always-on (rare) — document in WAD.

---

## 4. Proportionality rule

| Scenario | Plugin required? |
|----------|------------------|
| Single-page brochure, no CPT, no globals | **Optional** — may use minimal theme-only with WAD note |
| Site options (phone, social) | **Recommended** — options page in plugin |
| News CPT + categories | **Required** |
| ACF field groups | **Required** in plugin (default) |
| Complex integrations | **Required** |

**Do not** create empty "functionality plugin" scaffold without portable logic — document trivial case in FUNCTIONALITY-BOUNDARY artifact.

---

## 5. Minimum plugin structure

```text
{project-slug}-functionality/
├── {project-slug}-functionality.php   # Plugin header + bootstrap
├── includes/
│   ├── post-types.php
│   ├── taxonomies.php
│   ├── acf.php
│   ├── options.php
│   └── integrations.php
├── acf-json/                          # If ACF
├── migrations/
└── languages/
```

One project functionality plugin default — split only with WAD justification.

---

## 6. Separation matrix

| Code type | Theme | Project plugin | MU-plugin | Third-party | WPilot plugin |
|-----------|-------|----------------|-----------|-------------|---------------|
| `page-about.php` | ● | | | | |
| `register_post_type('news')` | | ● | | | |
| ACF JSON | | ● | | | |
| Contact Form 7 | | | | ● | |
| SMTP plugin | | | | ● | |
| Scoped content replace REST | | | | | ● |
| Backup service hook | | | | | ● |

---

## 7. WPilot boundary (explicit)

| Product | Role |
|---------|------|
| **Forge functionality plugin** | Site business model — ships with project |
| **metacode-wpilot** | Operations runtime — **never** mixed into project plugin |

**Forbidden:**

- Implementing WPilot operations inside project functionality plugin
- Bundling metacode-wpilot in RELEASE-MANIFEST as project code
- Using WPilot plugin for CPT/ACF registration

---

## 8. Third-party plugins

Governed by [FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md](FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md) — not duplicated here.

---

## 9. Violations

| Violation | Severity |
|-----------|----------|
| CPT in theme | **BLOCKER** WV1 |
| Business REST in theme | **BLOCKER** |
| Project plugin contains presentation templates | **MAJOR** |
| Empty plugin with no portable logic (undocumented) | **MAJOR** |
| WPilot ops code in project plugin | **BLOCKER** |

---

## Related documents

- [FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md)
- [contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](../contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md)

---

*Functionality plugin standard v1 — R-TF proportionality.*

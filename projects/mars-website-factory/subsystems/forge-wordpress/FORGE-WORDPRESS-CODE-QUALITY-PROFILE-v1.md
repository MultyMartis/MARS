# Forge WordPress — Code Quality Profile v1

**Document type:** Quality baseline profile  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

---

## 1. Profiles

### Required for every project

| Check | Tool | WV | Blocking |
|-------|------|-----|----------|
| PHP syntax | `php -l` | WV2 | Yes |
| WPCS (project ruleset) | PHPCS | WV2 | Critical sniffs |
| Escaping at output | PHPCS + review | WV2/WV4 | Yes |
| No secrets in Git | secret scan | WV4 | Yes |
| JS: no console errors on smoke | Playwright | WV5 | Critical paths |
| Built assets from Gulp | manifest | WV0 | Yes |

### Required for custom functionality

| Check | Tool | WV | Blocking |
|-------|------|-----|----------|
| Nonces / capabilities | PHPCS + review | WV4 | Yes |
| REST `permission_callback` | Review | WV4 | Yes |
| `$wpdb->prepare()` | PHPCS + review | WV4 | Yes |
| Plugin register complete | Checklist | WV4 | Yes |
| PHPUnit (critical logic) | PHPUnit | WV3 | If tests exist |

### Specialized profile

| Trigger | Additional checks |
|---------|-------------------|
| WooCommerce | WC templates, cart/checkout smoke |
| REST API custom | Route tests, auth matrix |
| Migrations | Dry-run, rollback script |
| Third-party integrations | Credential isolation review |

**PHPStan:** Optional — level 5–6 when custom plugin logic is non-trivial. **Not** mandatory for static theme-only Mode A.

---

## 2. PHPCS ruleset (baseline)

| Ruleset | Scope |
|---------|-------|
| `WordPress-Core` | All PHP |
| `WordPress-Docs` | Recommended |
| `WordPress-Extra` | Theme + plugin |
| `WordPress.Security` | **Blocking** subset |
| Project `phpcs.xml.dist` | Excludes `vendor/`, `node_modules/` |

---

## 3. JavaScript / SCSS

| Layer | Strategy |
|-------|----------|
| **JS** | ESLint if modules; else Playwright smoke |
| **SCSS** | Gulp build must pass; Stylelint optional |
| **CSS** | No hand-edit of compiled theme CSS |

---

## 4. Dependency checks

| Type | Action |
|------|--------|
| npm | `npm audit` — review HIGH+ |
| Composer | `composer audit` if used |
| WordPress plugins | Plugin register + WPScan candidate |

---

## Related

- [standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md](standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md)
- [FORGE-WORDPRESS-SECURITY-VALIDATION-DESIGN-v1.md](FORGE-WORDPRESS-SECURITY-VALIDATION-DESIGN-v1.md)

---

*Code quality profile v1.*

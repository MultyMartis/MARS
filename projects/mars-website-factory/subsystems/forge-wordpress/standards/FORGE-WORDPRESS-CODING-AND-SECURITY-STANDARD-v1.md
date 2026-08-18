# Forge WordPress Coding and Security Standard v1

**Document type:** Quality and security standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Validation:** WV2, WV4

**Scope:** Proportional web-studio standard — **not** enterprise compliance framework.

---

## 1. Baseline

| Standard | Application |
|----------|-------------|
| [WordPress Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/) | Theme + custom plugin PHP |
| PHPCS + WPCS | Project ruleset — runner FW-03 |
| WordPress Security Handbook | Escaping, sanitization, capabilities |

---

## 2. Output escaping (required)

| Context | Function |
|---------|----------|
| HTML content | `esc_html()`, `wp_kses_post()` |
| Attributes | `esc_attr()` |
| URLs | `esc_url()` |
| JavaScript | `wp_json_encode()` |
| Textarea | `esc_textarea()` |

**BLOCKER:** unescaped `$_GET`/`$_POST`/DB output in templates.

---

## 3. Input handling

| Layer | Requirement |
|-------|-------------|
| **Sanitization** | `sanitize_text_field`, `absint`, etc. on input |
| **Validation** | Business rules before save |
| **Nonces** | All admin forms and AJAX mutations |
| **Capabilities** | `current_user_can()` before privileged actions |
| **REST** | `permission_callback` on every route |
| **SQL** | `$wpdb->prepare()` — no interpolated SQL |
| **File uploads** | MIME check; restricted types; no executable upload |
| **AJAX** | Nonce + capability; no anonymous destructive AJAX |

---

## 4. Security classes

| Threat | Mitigation |
|--------|------------|
| **XSS** | Escape output; `wp_kses` for rich text |
| **CSRF** | Nonces |
| **SQLi** | Prepared statements |
| **SSRF** | No user-controlled remote fetch without allowlist |
| **Secrets** | Not in repo; env or local tokens |
| **Debug** | `WP_DEBUG` off on production; no `var_dump` in release |
| **Dependencies** | Composer lock; known CVE check WV4 |

---

## 5. Generated code review

AI- or scaffold-generated PHP requires **human review** before merge:

- Capability checks present
- No hardcoded credentials
- No direct `$_REQUEST` in SQL
- Escaping at output boundaries

---

## 6. Violation classification

| Class | Definition | Example |
|-------|------------|---------|
| **BLOCKER** | Must fix before release | Missing nonce; SQL injection vector; known CVE plugin |
| **MAJOR** | Fix or documented waiver | WPCS security sniff fail; missing `esc_url` |
| **WARNING** | Fix when practical | Naming sniff; minor formatting |

---

## 7. Minimum blocking set (release)

| # | Check | Layer |
|---|-------|-------|
| 1 | PHPCS security sniffs pass (or waived MAJOR only) | WV2 |
| 2 | No unescaped output in theme templates | WV4 |
| 3 | REST/AJAX permission callbacks | WV4 |
| 4 | No secrets in Git | WV4 |
| 4a | SMTP mailbox password: Admin write-only; never HTML/log/REST | WV4 |
| 5 | Plugin register security status complete | WV4 |
| 6 | `WP_DEBUG` false in production manifest | WV4 |

---

## 8. Explicitly out of scope (FW-02)

- SOC2 / ISO compliance mapping
- Penetration test mandate
- Mandatory SAST beyond PHPCS
- Container security scanning

Deferred tooling: FW-03.

---

## Related documents

- [FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md)
- [FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md](FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md)

---

*Coding and security standard v1 — proportional studio baseline.*

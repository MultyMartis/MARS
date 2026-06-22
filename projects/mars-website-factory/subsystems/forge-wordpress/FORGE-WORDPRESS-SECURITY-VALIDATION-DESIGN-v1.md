# Forge WordPress — Security Validation Design v1

**Document type:** WV4 security validation specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

Links to **FW-S-07** [FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md](standards/FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md).

**No offensive security tooling.**

---

## 1. Check matrix

| Area | Automatic candidate | Static | Validator review | Human security | Blocker |
|------|---------------------|--------|------------------|----------------|---------|
| Escaping | PHPCS | Templates | Yes | AI code review | Unescaped output |
| Sanitization | PHPCS | Input handlers | Yes | — | Raw superglobal in SQL |
| Validation | — | Business rules | Yes | — | Missing validation on mutations |
| Nonces | PHPCS sniffs | Forms/AJAX | Yes | — | Missing on admin mutations |
| Capabilities | PHPCS + grep | Privileged actions | Yes | — | Missing `current_user_can` |
| REST permissions | — | Route registration | Yes | — | Missing callback |
| AJAX | PHPCS | Handlers | Yes | — | Anonymous destructive |
| SQL preparation | PHPCS | `$wpdb` usage | Yes | — | Interpolated SQL |
| Uploads | — | MIME handlers | Yes | — | Executable upload |
| File operations | — | `include` paths | Yes | — | User-controlled paths |
| Secrets | secret scan | Repo | Yes | — | Credential in Git |
| Debug config | manifest lint | `wp-config` sample | Yes | — | `WP_DEBUG` true in release |
| Dependency CVE | composer/npm audit | Lock files | Yes | Plugin register | Known critical CVE |
| Plugin provenance | — | Plugin register | Yes | Operator | Unapproved plugin |
| Dangerous functions | PHPCS | `eval`, `exec` | Yes | — | Use in production code |
| Production URLs in source | grep/scan | Theme/plugin | Yes | — | Hardcoded prod credentials |

---

## 2. Runner: `wv4-security-scan`

| Input | Output |
|-------|--------|
| Theme + plugin paths | `WV4-SECURITY-REPORT` |
| Plugin register | Compliance table |
| RELEASE-MANIFEST | Debug/secret flags |

---

## 3. Blocker conditions (release)

Minimum blocking set from FW-S-07 §7 — all must pass or documented waiver (MAJOR only).

---

## 4. Explicit exclusions

- Penetration testing mandate
- Offensive scanners against production
- Automated exploit tooling

---

## Related

- [FORGE-WORDPRESS-CODE-QUALITY-PROFILE-v1.md](FORGE-WORDPRESS-CODE-QUALITY-PROFILE-v1.md)
- [standards/FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md](standards/FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md)

---

*Security validation design v1.*

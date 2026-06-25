# MARS Localhost — WP-CLI Standard v1

**Document type:** WP-CLI usage standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Canonical installation

| Item | Path |
|------|------|
| WP-CLI phar | `E:\MARS-Localhost\tools\wp-cli\wp-cli.phar` |
| Wrapper | `E:\MARS-Localhost\tools\wp-cli\wp.cmd` |
| Version (MLI-02) | 2.12.0 |

---

## Verification commands

```bat
E:\MARS-Localhost\tools\activate-mli.cmd
wp --info
wp cli version
```

---

## Policy

| Rule | Value |
|------|-------|
| PHP binding | Laragon PHP 8.3.30 only via activation |
| Packages | No global packages in MLI-02; project-local when WordPress exists |
| Aliases | **Prohibited** pointing at production |
| Production access | **Prohibited** |
| Target URLs | Local `.test` domains only after MLI-03 |
| Cache | User profile cache path — outside Git |
| Update | Operator approval; verify `wp cli version` after update |

---

## MLI-02 boundary

No WordPress runtime exists. **Do not** run site management commands until MLI-03.

---

## Related

- [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md)

---

*WP-CLI standard v1 — MLI-02.*

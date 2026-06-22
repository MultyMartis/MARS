# MARS Localhost — PHPCS / WPCS / PHPCompatibility Standard v1

**Document type:** PHPCS toolchain standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Stack (MLI-02 verified)

| Component | Version | Path |
|-----------|---------|------|
| PHPCS | 3.13.5 | `tools\phpcs\wpcs\vendor\bin\phpcs` (canonical) |
| WPCS | bundled in wpcs vendor | `tools\phpcs\wpcs\` |
| PHPCompatibility | 9.3.5 | `tools\phpcs\phpcompat\vendor\phpcompatibility\php-compatibility` |

Wrapper: `D:\MARS-Localhost\tools\phpcs\phpcs.cmd`

---

## Installed standards (`phpcs -i`)

MySource, PEAR, PSR1, PSR2, PSR12, Squiz, Zend, WordPress, WordPress-Core, WordPress-Docs, WordPress-Extra, **PHPCompatibility**

---

## Shared ruleset

```text
D:\MARS-Localhost\tools\phpcs\rulesets\mars-wordpress.xml
```

- WPCS baseline with moderate exclusions for first profile
- PHPCompatibility `testVersion` 8.3-
- Excludes vendor, node_modules, dist, build, uploads, cache

---

## Smoke fixture only

```text
D:\MARS-Localhost\tools\phpcs\fixtures\mli-smoke-sample.php
```

**Do not** scan client projects from MLI shared tooling.

---

## Activation

```bat
D:\MARS-Localhost\tools\activate-mli.cmd
phpcs --version
phpcs -i
phpcs --standard=D:\MARS-Localhost\tools\phpcs\rulesets\mars-wordpress.xml D:\MARS-Localhost\tools\phpcs\fixtures\mli-smoke-sample.php
```

---

## Related

- [MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md](MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md)

---

*PHPCS/WPCS standard v1 — MLI-02.*

# MARS Localhost — Composer Standard v1

**Document type:** Composer usage standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Canonical installation

| Item | Path |
|------|------|
| Composer phar | `E:\MARS-Localhost\tools\composer\composer.phar` |
| Wrapper | `E:\MARS-Localhost\tools\composer\composer.cmd` |
| PHP binding | Laragon PHP 8.3.30 via `activate-mli.cmd` |

---

## Public key verification

- Run `composer diagnose` after session activation.
- Keys live in Composer home (`%APPDATA%\Composer\` by default): `keys.dev.pub`, `keys.tags.pub`.
- Official update path: `composer self-update --update-keys` (**interactive**).
- MLI-02 verified fingerprints via `composer diagnose` (pubkeys OK).

---

## Policy

| Rule | Value |
|------|-------|
| Global project pollution | **Avoid** — prefer project-local `composer.json` under site or tool fixture |
| `check-platform-reqs` | **NOT APPLICABLE** without a project `composer.json` at cwd |
| Self-update major | **No automatic major** — operator approval per upgrade policy |
| Laragon bundled Composer | Present but **not canonical** — use MLI `tools\composer\` |

---

## Cache and config paths

Resolved at runtime by `composer diagnose` (home, cache, data-dir). Not published in brain docs.

---

## Related

- [MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md](MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md)
- [MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md](MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md)

---

*Composer standard v1 — MLI-02.*

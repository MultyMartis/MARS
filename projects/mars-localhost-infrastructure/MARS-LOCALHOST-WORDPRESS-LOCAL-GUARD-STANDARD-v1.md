# MARS Localhost — WordPress Local Guard Standard v1

**Document type:** WordPress local-only guard standard  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03

---

## Purpose

Enforce **local-only** boundaries for WordPress runtimes on MLI: prevent accidental production database connections, credential leakage, remote WP-CLI targets, and cross-environment URL confusion.

Guards complement [MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md](MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md) and apply to all classes (`synthetic`, `projects`, `sandboxes`).

---

## Guard principles

| ID | Principle |
|----|-----------|
| **WP-G-01** | Local runtime talks to **local** MySQL on `127.0.0.1` / `localhost` only |
| **WP-G-02** | Canonical site URL uses `.test` (or manifest-declared local TLD) — never production domain |
| **WP-G-03** | Secrets live outside Git in `C:\AI MARS\local\mli\{slug}\` |
| **WP-G-04** | WP-CLI must not define production `@alias` targets |
| **WP-G-05** | Production target in manifest is `NONE` unless explicit read-only mirror charter |
| **WP-G-06** | MySQL server binds to loopback for MLI WordPress profile |

---

## Database guards

### wp-config.php

| Check | Required value |
|-------|----------------|
| `DB_HOST` | `127.0.0.1` or `localhost` |
| `DB_NAME` | `mars_wp_*` per naming standard |
| `DB_USER` | Per-runtime `mli_*_app` user |

**Forbidden `DB_HOST` patterns (non-exhaustive):**

- Public hostnames (`*.ru`, `*.com`, managed cloud DB endpoints)
- LAN IPs other than loopback unless manifest charters VPN tunnel
- Production replica hosts

### MySQL server

| Setting | MLI-03 requirement |
|---------|-------------------|
| `bind-address` | **`127.0.0.1`** |
| Application user grants | `mli_*_app@localhost` / `@127.0.0.1` only |
| Remote `%` grants for app users | **Prohibited** |

Verified MLI-03: bind-address hardened from Laragon default `*` exposure.

### Pre-flight grep (operator / automation)

Before import or sync operations:

```bat
findstr /i /s "DB_HOST" E:\MARS-Localhost\sites\wordpress\*\*\wp-config.php
```

Reject any non-loopback host unless manifest exception documented.

---

## URL and domain guards

| Check | Policy |
|-------|--------|
| `siteurl` / `home` options | Must match manifest `local_url` |
| `WP_HOME` / `WP_SITEURL` | Local `.test` only |
| Production domain in options | **Forbidden** |
| Redirect plugins to production | **Forbidden** without charter |

**Reference:** MLI-WP-SYN-001 → `http://fws-0001.test` — not a client production hostname.

---

## WP-CLI guards

| Rule | Policy |
|------|--------|
| `@production` / remote aliases | **Prohibited** in `wp-cli.yml` and global config |
| `wp search-replace` across unknown dumps | Require manifest review first |
| `--url` flag | Local `.test` domain only |
| Remote plugin/theme install from private prod registries | **Forbidden** |

Activation path:

```bat
E:\MARS-Localhost\tools\activate-mli.cmd
```

See [MARS-LOCALHOST-WPCLI-STANDARD-v1.md](MARS-LOCALHOST-WPCLI-STANDARD-v1.md).

---

## Secrets guards

| Item | Allowed location | Forbidden |
|------|------------------|-----------|
| DB password | `runtime.env` | Git, markdown, manifest body |
| WordPress auth keys | `runtime.env` | Committed wp-config templates |
| Production API keys | — | Any local config unless sandbox charter |
| TLS private keys | `E:\MARS-Localhost\laragon\etc\ssl\` | Git |

**Reference secrets path (values not documented):**

```text
C:\AI MARS\local\mli\fws-0001\runtime.env
```

---

## Network and HTTPS guards

| Topic | Policy |
|-------|--------|
| Outbound WordPress updates | Allowed to wordpress.org (operator network) |
| Production site sync plugins | **Not installed** in MLI-03 baseline |
| HTTPS local cert | Self-signed / untrusted CA — acceptable for smoke |
| Production TLS material copy | **Forbidden** |
| Playwright HTTPS smoke | `ignoreHTTPSErrors: true` — local only |

HTTPS validation result for MLI-03: **PASS WITH UNTRUSTED LOCAL CA** when hosts entry present (MLI-02 Playwright pattern).

---

## Data import guards

| Data type | Requirement |
|-----------|-------------|
| Production DB dump | Operator approval + sanitization review |
| Client PII | `projects\` class + passport charter only |
| Production uploads archive | Sanitize; scan for embedded credentials |
| Synthetic fixtures | Preferred default |

**Never** import production credentials into `runtime.env`.

---

## Plugin and theme guards

| Check | MLI-03 |
|-------|--------|
| Forge theme/plugin | **Not installed** — reduces prod coupling |
| Migration plugins (e.g. push-to-live) | **Prohibited** in synthetic proof |
| Backup plugins pointing remote | Audit before enable |

---

## hosts file guards

Hosts entries managed only inside MLI block:

```text
# BEGIN MARS LOCALHOST MANAGED
127.0.0.1 mli-smoke-001.test
127.0.0.1 fws-0001.test
# END MARS LOCALHOST MANAGED
```

| Domain | MLI-03 status |
|--------|---------------|
| `mli-smoke-001.test` | **PASS** |
| `fws-0001.test` | **PENDING ELEVATION** — script supports multi-domain; operator must run elevated add |

Scripts: `E:\MARS-Localhost\tools\hosts\add-mli-host.ps1`

---

## Production target guard

Every WordPress manifest must declare:

```text
production_target: NONE
```

Unless an explicit read-only mirror charter exists (not applicable to MLI-WP-SYN-001).

---

## Validation checklist

Run before marking runtime `active`:

- [ ] `DB_HOST` is loopback
- [ ] MySQL `bind-address` is `127.0.0.1`
- [ ] App DB user restricted to localhost
- [ ] `siteurl` / `home` match manifest
- [ ] No production hostname in wp-config or options
- [ ] `runtime.env` exists; not in Git
- [ ] WP-CLI has no remote aliases
- [ ] Manifest `production_target: NONE`
- [ ] Hosts entry verified or documented as pending elevation
- [ ] HTTPS smoke uses untrusted-CA pattern only — not production cert

---

## Violation response

| Severity | Action |
|----------|--------|
| Production DB host detected | **STOP** — set manifest `hold`; fix config before continue |
| Secrets in Git | Rotate credentials; purge from history per operator policy |
| Production URL in options | `wp search-replace` to local URL; document in report |
| Unexpected remote plugin | Deactivate; remove if not chartered |

---

## Related

- [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md)
- [MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md)
- [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md)
- [MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md](MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md)

---

*WordPress local guard standard v1 — MLI-03.*

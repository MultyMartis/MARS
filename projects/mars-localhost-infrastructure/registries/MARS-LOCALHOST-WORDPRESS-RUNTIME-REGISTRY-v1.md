# MARS Localhost — WordPress Runtime Registry v1

**Document type:** WordPress runtime registry (human-maintained)  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Authority:** Brain (`X:\AI MARS`) — not D: alone

---

## Registry rules

1. One row per sustained WordPress runtime (`synthetic`, `projects`, `sandboxes`).
2. **Runtime ID** follows pattern `MLI-WP-{CLASS}-{nnn}` (class code: SYN, PRJ, SBX).
3. Physical path must be under `X:\MARS-Localhost\sites\wordpress\`.
4. Each row links to a brain runtime manifest — manifest is SoT for detailed fields.
5. Database name and user recorded; **no passwords**.
6. `production_target` must be `NONE` unless explicit mirror charter.

---

## Registered WordPress runtimes

| Runtime ID | Synthetic / Project ID | Class | Slug | Domain | Physical root | Database | DB user | Table prefix | WP version | Locale | Manifest | Secrets path | Production | Status | Last verified |
|------------|------------------------|-------|------|--------|---------------|----------|---------|--------------|------------|--------|----------|--------------|------------|--------|---------------|
| MLI-WP-SYN-001 | FWS-0001 | synthetic | fws-0001 | fws-0001.test | `X:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` | `mars_wp_fws0001` | `mli_fws0001_app` | `mli_` | 7.0 | ru_RU | [MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](../manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) | `X:\AI MARS\local\mli\fws-0001\runtime.env` | **NONE** | active — post-reboot validated | 2026-06-24 (MLI-03R.1) |
| MLI-WP-FP0002-LOCAL | FP-0002 | projects | shpigovsky | shpigovsky.test | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` | `mars_wp_fp0002` | `mli_shpigovsky_app` | `fp02_` | 7.0 | ru_RU | [MLI-WP-FP0002-LOCAL-RUNTIME-MANIFEST-v1.md](../manifests/MLI-WP-FP0002-LOCAL-RUNTIME-MANIFEST-v1.md) | `X:\AI MARS\local\mli\fp-0002\runtime.env` | **NONE** | active / foundation ready — post-reboot validated | 2026-06-24 (MLI-03R.1) |

---

## Stack reference (shared MLI profile)

Applies to all rows unless manifest overrides:

| Component | Version |
|-----------|---------|
| PHP | 8.3.30 |
| MySQL | 8.4.3 |
| Apache | 2.4.66 |
| WP-CLI | 2.12.0 |
| mod_rewrite | enabled |
| MySQL bind-address | 127.0.0.1 |

---

## Hosts and HTTPS summary (MLI-WP-SYN-001)

| Check | Result |
|-------|--------|
| Hosts `mli-smoke-001.test` | **PASS** |
| Hosts `fws-0001.test` | **PENDING ELEVATION** — HTTP 200 via Host header (FW-05R) |
| HTTPS cert | Generated |
| HTTPS smoke | **PASS WITH UNTRUSTED LOCAL CA** (when hosts present) |
| Forge theme/plugin | **INSTALLED** — fws-synthetic + fws-synthetic-core (FW-05R) |
| ACF Free | **ACTIVE** — 6.8.4 |
| MySQL X Protocol 33060 | **DISABLED** — `mysqlx=0` |

---

## Add entry checklist

- [ ] Class and slug chosen per [site classification standard](../MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md)
- [ ] Physical path created under `sites\wordpress\{class}\{slug}\`
- [ ] Registry row added (this document)
- [ ] Runtime manifest created in `manifests/`
- [ ] Vhost row added to [vhost registry](MARS-LOCALHOST-VHOST-REGISTRY-v1.md)
- [ ] Database created per [database naming standard](../MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md)
- [ ] Per-runtime DB user (`mli_{slug}_app`) — localhost only
- [ ] `runtime.env` created outside Git
- [ ] WordPress core installed via WP-CLI
- [ ] Local guards verified per [local guard standard](../MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md)
- [ ] HTTP smoke 200 confirmed
- [ ] HTTPS smoke per certificate standard (optional)

---

## Related

- [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](../MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md)
- [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](../MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)
- [MARS-LOCALHOST-VHOST-REGISTRY-v1.md](MARS-LOCALHOST-VHOST-REGISTRY-v1.md)

---

*WordPress runtime registry v1 — MLI-03.*

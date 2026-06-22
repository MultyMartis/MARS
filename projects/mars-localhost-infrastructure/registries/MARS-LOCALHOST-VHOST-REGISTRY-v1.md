# MARS Localhost — Vhost Registry v1

**Document type:** Local vhost registry (human-maintained)  
**Version:** v1.2  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Authority:** Brain (`C:\AI MARS`) — not Laragon auto-discovery alone

---

## Registry rules

1. One row per sustained or synthetic local site.
2. **Canonical domain** = `{slug}.test` only.
3. Physical path must be under `D:\MARS-Localhost\sites\`.
4. Link each entry to a runtime manifest when site is sustained.
5. Laragon `www\{slug}` junction or explicit vhost must match this registry.

---

## Registered vhosts

| Runtime ID | Slug | Domain | Platform | Class | Physical root | Junction path | Apache vhost path | HTTPS | Hosts status | Manifest | State | Last verified |
|------------|------|--------|----------|-------|---------------|---------------|-------------------|-------|--------------|----------|-------|---------------|
| MLI-SMOKE-001 | mli-smoke-001 | mli-smoke-001.test | php | synthetic | `D:\MARS-Localhost\sites\php\synthetic\mli-smoke-001` | `laragon\www\mli-smoke-001` (optional) | `etc\apache2\sites-enabled\mli-smoke-001.test.conf` | **YES** — `mli-smoke-001.test-ssl.conf` | **PASS** — managed block | [MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md](../manifests/MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md) | active | 2026-06-23 |
| MLI-WP-SYN-001 | fws-0001 | fws-0001.test | wordpress | synthetic | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` | `laragon\www\fws-0001` | `etc\apache2\sites-enabled\fws-0001.test.conf` | **YES** — `fws-0001.test-ssl.conf` | **PENDING ELEVATION** — run `tools\hosts\add-mli-host` (multi-domain) | [MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](../manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) | active / validated | 2026-06-23 |

---

## Add entry checklist

- [ ] Physical path created under `sites\{platform}\{class}\{slug}\`
- [ ] Registry row added
- [ ] Junction or vhost configured
- [ ] `hosts` entry verified (`127.0.0.1 {slug}.test`)
- [ ] Runtime manifest created in brain
- [ ] Smoke HTTP 200 confirmed
- [ ] HTTPS tested per certificate standard (optional)

---

## Related

- [MARS-LOCALHOST-VHOST-PROVISIONING-STANDARD-v1.md](../MARS-LOCALHOST-VHOST-PROVISIONING-STANDARD-v1.md)

---

*Vhost registry v1.2 — MLI-03.*

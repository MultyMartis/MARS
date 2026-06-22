# MARS Localhost — Vhost Registry v1

**Document type:** Local vhost registry (human-maintained)  
**Version:** v1.1  
**Date:** 2026-06-22  
**Stage:** MLI-02  
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
| MLI-SMOKE-001 | mli-smoke-001 | mli-smoke-001.test | php | synthetic | `D:\MARS-Localhost\sites\php\synthetic\mli-smoke-001` | `laragon\www\mli-smoke-001` (optional) | `etc\apache2\sites-enabled\mli-smoke-001.test.conf` | **YES** — `mli-smoke-001.test-ssl.conf` | **PENDING ELEVATION** — use `tools\hosts\add-mli-host` | [MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md](../manifests/MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md) | active | 2026-06-22 |

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

*Vhost registry v1.1 — MLI-02.*

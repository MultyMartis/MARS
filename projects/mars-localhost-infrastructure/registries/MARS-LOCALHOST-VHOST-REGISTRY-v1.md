# MARS Localhost — Vhost Registry v1

**Document type:** Local vhost registry (human-maintained)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01  
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

| Slug | Domain | Platform | Class | Physical path | Web server | HTTPS | Junction | Vhost conf | Manifest |
|------|--------|----------|-------|---------------|------------|-------|----------|------------|----------|
| mli-smoke-001 | mli-smoke-001.test | php | synthetic | `D:\MARS-Localhost\sites\php\synthetic\mli-smoke-001` | Apache | HTTP baseline | `laragon\www\mli-smoke-001` | `etc\apache2\sites-enabled\mli-smoke-001.test.conf` | [MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md](../manifests/MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md) |

---

## Add entry checklist

- [ ] Physical path created under `sites\{platform}\{class}\{slug}\`
- [ ] Registry row added
- [ ] Junction or vhost configured
- [ ] `hosts` entry verified (`127.0.0.1 {slug}.test`)
- [ ] Runtime manifest created in brain
- [ ] Smoke HTTP 200 confirmed

---

*Vhost registry v1 — MLI-01.*

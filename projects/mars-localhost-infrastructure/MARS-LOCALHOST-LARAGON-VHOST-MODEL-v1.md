# MARS Localhost — Laragon Vhost Model v1

**Document type:** Domain and vhost model  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01

---

## Canonical domain rule

```text
Local domain:  {slug}.test
Physical path: E:\MARS-Localhost\sites\{platform}\{class}\{slug}\
```

**Forbidden default:** `wordpress.synthetic.fws-0001.test` (nested category in hostname)

---

## Resolution stack

| Layer | Mechanism |
|-------|-----------|
| **DNS / hosts** | Laragon Auto Virtual Hosts updates Windows `hosts` (requires elevation) OR manual operator entry |
| **Apache vhost** | Auto-generated from `www\{slug}` folder name + explicit `sites-enabled\*.conf` |
| **HTTPS** | Laragon SSL tooling — **deferred baseline** (see MLI-01 HTTPS section) |
| **Registry SoT** | [registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md](registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md) |
| **Runtime manifest** | `manifests\{RUNTIME-ID}-RUNTIME-MANIFEST-v1.md` in brain |

---

## Nested path mapping

Example:

```text
Physical: sites\wordpress\synthetic\fws-0001\
Domain:   fws-0001.test
```

**Implementation:**

1. Create physical directory under `sites\`.
2. Register in vhost registry (slug, platform, class, paths).
3. Create junction `laragon\www\fws-0001` → physical path **OR** explicit vhost file.
4. Restart Apache / Laragon reload.
5. Confirm `hosts` contains `127.0.0.1 fws-0001.test`.

---

## Web server

| Profile | Server |
|---------|--------|
| **Default (MLI)** | Apache httpd 2.4.66 |
| **Alternate** | Nginx 1.28.2 — not default |

---

## HTTPS status (MLI-01)

| Item | Status |
|------|--------|
| Laragon auto-SSL | Available in Laragon UI — **not verified end-to-end in MLI-01** |
| MLI baseline | **HTTP** for smoke |
| Certificate storage (target) | `E:\MARS-Localhost\certificates\` |
| Follow-up | **MLI-02** certificate hardening |

---

## Certificate location (when enabled)

```text
E:\MARS-Localhost\certificates\   # MLI target store
Laragon-managed certs              # under Laragon SSL tooling (operator UI)
```

**No production certificates.**

---

## Runtime manifest pointer

Each registered site must link to a brain manifest:

`C:\AI MARS\projects\mars-localhost-infrastructure\manifests\`

---

*Laragon vhost model v1 — MLI-01.*

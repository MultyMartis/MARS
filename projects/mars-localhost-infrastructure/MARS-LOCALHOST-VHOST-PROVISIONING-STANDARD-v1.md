# MARS Localhost — Vhost Provisioning Standard v1

**Document type:** Vhost provisioning procedure  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Procedure chain

```text
site directory
  → junction (optional Laragon www layer)
  → Apache vhost
  → hosts entry
  → optional local certificate
  → smoke check
  → runtime manifest (brain)
  → vhost registry (brain)
```

---

## Steps

### 1. Site directory

Create under:

```text
X:\MARS-Localhost\sites\{platform}\{class}\{slug}\
```

### 2. Junction (when using Laragon www layer)

```text
X:\MARS-Localhost\laragon\www\{slug}  →  physical site root
```

### 3. Apache vhost

Add to:

```text
X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\{slug}.test.conf
```

HTTP baseline required; HTTPS optional per [MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md](MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md).

### 4. Hosts entry

Run [hosts management](MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md) or extend managed block policy for additional slugs.

### 5. Optional certificate

Generate local dev cert on D: only; never commit private keys.

### 6. Smoke check

Minimum: HTTP 200, expected heading, registry row updated.

### 7. Manifest + registry

- Manifest in `projects/mars-localhost-infrastructure/manifests/`
- Row in [registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md](registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md)

---

## MLI-02 scope boundary

This standard is **documented** in MLI-02. WordPress and OpenCart vhosts are **MLI-03 / MLI-04** only.

---

## Related

- [MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md](MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md)
- [MARS-LOCALHOST-SMOKE-SUITE-v1.md](MARS-LOCALHOST-SMOKE-SUITE-v1.md)

---

*Vhost provisioning standard v1 — MLI-02.*

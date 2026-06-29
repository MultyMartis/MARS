# MARS Localhost — Domain Standard v1

**Document type:** Local domain naming standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00

---

## Purpose

Assign **one canonical local URL** per runtime site with no production collision risk.

---

## Preferred TLD

```text
.test
```

RFC 2606-style local use; not issued for public DNS in normal operations.

**Alternatives (operator-only):** `.local`, `.localhost` — must be documented in manifest if used; `.test` remains default for new sites.

---

## Naming model

```text
{slug}.test
```

| Component | Rule |
|-----------|------|
| **slug** | Matches site folder slug under `sites\{platform}\{class}\` |
| **case** | lowercase only |
| **charset** | latin letters, digits, hyphen |
| **length** | short; prefer ≤ 32 characters |
| **uniqueness** | one canonical URL per runtime manifest |

### Examples

| Site | Canonical URL |
|------|---------------|
| FWS-0001 synthetic WordPress | `fws-0001.test` |
| Shpigovsky project | `shpigovsky.test` |
| BZPM OpenCart project | `bzpm.test` |
| Sibcar OpenCart project | `sibcar.test` |
| OCPilot test | `ocpilot-test.test` |

---

## Requirements

| ID | Requirement |
|----|-------------|
| **DM-01** | lowercase hostnames only |
| **DM-02** | latin charset only |
| **DM-03** | short, memorable slugs |
| **DM-04** | **no** reuse of client production domains (e.g. `example.ru`) |
| **DM-05** | **no** reuse of registered DEV/production hosts as local canonical URL |
| **DM-06** | **no** ambiguous aliases — pick one canonical URL per manifest |
| **DM-07** | Laragon / hosts file entries must match manifest exactly |
| **DM-08** | Avoid cookie domain overlap with production TLDs |

---

## HTTPS policy

| Topic | Policy |
|-------|--------|
| **Local TLS** | Optional but recommended for parity testing |
| **Certificates** | Stored under `X:\MARS-Localhost\certificates\` |
| **Trusted local CA** | Use if operator supports (e.g. mkcert) — document in MLI-01 |
| **Production certs** | **Prohibited** — never copy production TLS material |
| **Default MLI-00** | HTTP acceptable for foundation; HTTPS enablement in MLI-01+ |

---

## Subdomains

Allowed when manifest documents them:

```text
admin.bzpm.test
api.web-sim-0001.test
```

Prefer flat `{slug}.test` unless consumer requires subdomain isolation.

---

## Related

- [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)
- [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md)

---

*Domain standard v1 — MLI-00.*

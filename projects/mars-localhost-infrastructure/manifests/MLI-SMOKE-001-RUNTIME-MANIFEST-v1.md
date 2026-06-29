# MLI-SMOKE-001 — Runtime Manifest v1

**Document type:** Runtime manifest (brain SoT)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01

---

## Identity

| Field | Value |
|-------|-------|
| **Runtime ID** | MLI-SMOKE-001 |
| **Synthetic ID** | mli-smoke-001 |
| **Class** | synthetic |
| **Platform** | php |
| **Status** | `VALIDATED_SMOKE` |

---

## Paths and URLs

| Field | Value |
|-------|-------|
| **MARS authority path** | `X:\AI MARS\projects\mars-localhost-infrastructure\manifests\MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md` |
| **Runtime path** | `X:\MARS-Localhost\sites\php\synthetic\mli-smoke-001` |
| **Local URL (HTTP)** | `http://mli-smoke-001.test/` |
| **Junction** | `X:\MARS-Localhost\laragon\www\mli-smoke-001` |
| **Vhost registry** | [MARS-LOCALHOST-VHOST-REGISTRY-v1.md](../registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md) |

---

## Runtime stack

| Field | Value |
|-------|-------|
| **PHP version** | 8.3.30 |
| **DB ID** | NONE |
| **DB version** | N/A |
| **Web server** | Apache 2.4.66 |

---

## Ownership

| Field | Value |
|-------|-------|
| **Runtime owner** | MARS Localhost Infrastructure (operator) |
| **Implementation owner** | MLI program |
| **Operations owner** | Operator |
| **Production target** | NONE |

---

## State

| Field | Value |
|-------|-------|
| **Backup state** | none |
| **Rollback state** | delete junction + site folder |
| **Secrets location** | N/A |
| **Last validation** | 2026-06-22 — MLI-01 HTTP smoke (Host header) |

---

*Runtime manifest v1 — MLI-SMOKE-001.*

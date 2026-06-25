# MARS Localhost — Document Root Decision v1

**Document type:** Architecture decision record  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01  
**Status:** **DECIDED**

---

## Target

**Physical site storage (canonical):** `E:\MARS-Localhost\sites`

**Laragon must not become the long-term store of client/CMS source trees.**

---

## Options evaluated

| Option | Description | Verdict |
|--------|-------------|---------|
| **A — Direct document root** | Set Laragon `DocumentRoot` = `E:\MARS-Localhost\sites` | **REJECTED** — Auto Virtual Hosts would expose category folders (`wordpress.test`, `php.test`) |
| **B — Full junction www → sites** | `laragon\www` → `sites` | **REJECTED** — same nested-domain problem as A |
| **C — Slug junction registry + explicit vhosts** | Physical paths under `sites\`; `www\{slug}` junctions OR explicit Apache vhost per registry entry | **ADOPTED** |

---

## Adopted model (Option C)

```text
Physical storage:
  E:\MARS-Localhost\sites\{platform}\{class}\{slug}\

Laragon www (registry layer):
  E:\MARS-Localhost\laragon\www\{slug}  → junction to physical path

Explicit vhosts (when junction insufficient):
  E:\MARS-Localhost\laragon\etc\apache2\sites-enabled\{slug}.test.conf
```

| Requirement | How met |
|-------------|---------|
| Sites live in `sites\` | **YES** — physical path only |
| Laragon not CMS storage | **YES** — `www\` holds junctions / Laragon default page only |
| `.test` domains | `{slug}.test` via Auto Virtual Hosts + registry vhosts |
| Category paths preserved | `sites\wordpress\synthetic\fws-0001` etc. |
| No duplicate source trees | Junction points to single physical tree |
| Cursor absolute paths | Documented in vhost registry + runtime manifest |

---

## Laragon `DocumentRoot`

**Remains:** `E:\MARS-Localhost\laragon\www`

**Rationale:** Compatible with Laragon Auto Virtual Hosts and minimal change to operator install. Physical content stays in `sites\`.

---

## MLI-01 smoke implementation

| Item | Value |
|------|-------|
| Physical path | `E:\MARS-Localhost\sites\php\synthetic\mli-smoke-001` |
| Junction | `laragon\www\mli-smoke-001` → physical path |
| Vhost | `etc\apache2\sites-enabled\mli-smoke-001.test.conf` |
| Domain | `mli-smoke-001.test` |

---

## Related

- [MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md](MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md)
- [registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md](registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md)

---

*Document root decision v1 — MLI-01.*

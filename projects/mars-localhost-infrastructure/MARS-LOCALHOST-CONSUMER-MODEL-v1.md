# MARS Localhost — Consumer Model v1

**Document type:** Consumer relationship model  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01

---

## Principle

MARS Localhost Infrastructure is **shared**. Consumers **use** runtime profiles; they **do not own** `D:\MARS-Localhost`.

---

## Forge WordPress

| Aspect | Detail |
|--------|--------|
| **Uses** | WordPress local runtime; PHP; MariaDB/MySQL; WP-CLI; PHPCS; Playwright; local screenshots; `sites/wordpress/synthetic` and `projects` |
| **Owns** | Implementation methodology, theme/plugin source in `C:\AI MARS\workspaces\` |
| **Does not own** | Shared localhost root, Laragon install, global toolchain layout |
| **Statement** | Forge WordPress does **not** own `D:\MARS-Localhost`. It consumes the WordPress runtime profile provided by MARS Localhost Infrastructure. |
| **FW-05R** | Full local WordPress re-validation on Profile A — **HOLD** until MLI-03 WordPress runtime profile |

**Pointer:** [projects/mars-website-factory/subsystems/forge-wordpress/](../mars-website-factory/subsystems/forge-wordpress/)

---

## OCPilot

| Aspect | Detail |
|--------|--------|
| **Uses** | OpenCart/ocStore runtime; PHP; DB; local site copies; import simulations; module/theme tests |
| **Future OpenCart root** | `D:\MARS-Localhost\sites\opencart\...` |
| **Owns** | OpenCart operational pack, baselines, site passports in brain |
| **Does not own** | MLI root or Laragon |
| **Statement** | OCPilot may consume the OpenCart runtime profile of MARS Localhost Infrastructure. **No** OCPilot implementation or runtime migration in MLI-01. |
| **MLI-04** | OpenCart runtime profile validation — **PLANNED** |

**Pointer:** [projects/ocpilot/](../ocpilot/)

---

## Website Factory

| Aspect | Detail |
|--------|--------|
| **Uses** | May provide approved frontend Gulp packages to consumers |
| **Does not own** | PHP runtime, databases, or localhost stack |
| **Relationship** | Upstream of Forge WordPress handoff |

---

## WPilot

| Aspect | Detail |
|--------|--------|
| **Uses** | May accept verified WordPress package; may work with registered DEV (`dev.gktriumph.ru`) |
| **Does not own** | Localhost infrastructure |
| **Boundary** | WPilot operates remote DEV/production; MLI is local-only |

---

## Future consumers

| Examples | Profile |
|----------|---------|
| Generic PHP agents | `sites/php/` |
| Migration simulators | `sites/php/synthetic/` or `sites/other/` |
| API/webhook tests | `sites/php/sandboxes/` |

New consumers require operator acknowledgment and manifest discipline; no automatic registry entry.

---

## Consumer onboarding checklist

1. Identify platform profile (`wordpress`, `opencart`, `php`)
2. Create site class folder + slug on D:
3. Register manifest in brain
4. Assign local domain + database name
5. Document consumer-specific validation requirements in consumer pack
6. Do **not** fork MLI directory standard per consumer

---

## Related

- [MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md](MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md)
- [MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md](MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md)

---

*Consumer model v1 — MLI-00.*

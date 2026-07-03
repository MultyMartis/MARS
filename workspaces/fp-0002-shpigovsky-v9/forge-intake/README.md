# FP-0002 V9 Forge WordPress Intake Pack

**Phase:** V9-05B  
**Date:** 2026-07-02  
**Stable baseline:** `fp-0002-v9-operator-approved-static-frontend-stable-01` @ `a51376872fbfefb7d5f68a58b440c726d6cf3de3`  
**Intake gate:** V9-05A **APPROVED** — foundation **ADOPTED**  
**Runtime checkpoint:** V9-05B **COMPLETE** — `foundation-002-v9-pre-implementation`
**Latest WordPress runtime gate:** V9-06D.1 rerun **PASS** — runtime delivery complete; object skeleton not started

## Entry documents

- [FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md](./FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md) — V9-04 contract pack
- [FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md](./validation/FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md) — V9-05A gate (APPROVED)
- [FP-0002-V9-05B-PRE-IMPLEMENTATION-RUNTIME-CHECKPOINT-GATE-v1.md](./validation/FP-0002-V9-05B-PRE-IMPLEMENTATION-RUNTIME-CHECKPOINT-GATE-v1.md) — **V9-05B checkpoint (COMPLETE)**
- [FP-0002-V9-06C1-SOURCE-ACTIVATION-GATE-RESOLUTION-GATE-v1.md](./validation/FP-0002-V9-06C1-SOURCE-ACTIVATION-GATE-RESOLUTION-GATE-v1.md) — **V9-06C.1 source gate (PASS)**
- [FP-0002-V9-06D1-RERUN-RUNTIME-DELIVERY-GATE-v1.md](./validation/FP-0002-V9-06D1-RERUN-RUNTIME-DELIVERY-GATE-v1.md) — **V9-06D.1 rerun runtime delivery gate (PASS)**

## Structure

| Folder | Contents |
|--------|----------|
| `authority/` | Authority hierarchy |
| `routes/` | Route inventory, object model, permalinks |
| `templates/` | Page-to-template map, theme target map |
| `components/` | Component-to-template-part map |
| `content/` | Content ownership, migration manifest |
| `fields/` | Native fields, ACF, repeaters, global options |
| `blog/` | Blog architecture |
| `reviews/` | Reviews architecture |
| `menus/` | Menus and breadcrumbs |
| `forms/` | Modal, Scroll-to-Top, forms |
| `assets/` | Asset and media migration |
| `legal/` | Legal pages, placeholder policy |
| `seo/` | SEO and metadata boundary |
| `implementation/` | Forge sequence, runtime contract, dependencies |
| `validation/` | Audits, review gate, immutability |
| `registers/` | Blockers, risks, open decisions |
| `manifests/` | Machine-readable JSON companions |

## Validation

```bash
npm run validate:forge-intake
```

**V9-06D.1 rerun runtime delivery is COMPLETE.** V9-06D.2 object skeleton requires separate operator authorization.

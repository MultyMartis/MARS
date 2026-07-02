# FP-0002 V9 Forge WordPress Intake Pack

**Phase:** V9-04  
**Date:** 2026-07-02  
**Stable baseline:** `fp-0002-v9-operator-approved-static-frontend-stable-01` @ `a51376872fbfefb7d5f68a58b440c726d6cf3de3`

## Entry document

[FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md](./FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md)

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

**WordPress implementation is NOT authorized by this pack alone** — requires FW-06B operator charter and environment gate (V9-05).

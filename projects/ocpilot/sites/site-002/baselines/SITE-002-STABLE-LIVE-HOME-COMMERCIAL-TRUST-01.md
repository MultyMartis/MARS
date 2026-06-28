# SITE-002 — STABLE LIVE — Home Commercial Trust 01

**Status:** **ACTIVE** on TEST — Home CTA band uses `zpm-commercial-trust` (replaces legacy `zpm-dealers` dealers block)  
**URL:** https://zpm.new-site.space/  
**Date:** 2026-06-29  
**Report:** [SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md](../reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md)

## Scope

| Surface | Change |
|---------|--------|
| **Home** | Legacy `zpm-dealers` block → `zpm-commercial-trust` (home-adapted copy, cert podium, form card) |
| **Catalog / katalog / corp / PDP** | **Unchanged** — `blockdealersform.twig` restored for `/katalog` |

## Live artifact hashes (post-deploy)

| Artifact | SHA256 | Bytes |
|----------|--------|-------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust_home.twig` | `69b4daad5621dbe0fe7140159466e4c70a56f226f0faa0f14b83fb5b23f06386` | 9160 |
| `catalog/controller/common/home.php` | `8e68ab0866f7822c6530b37dd0c4544c22b86b4895f32035def7fe338e098fb9` | 3852 |
| `catalog/view/theme/default/template/sections/blockdealersform.twig` | `5abad9f2d27e3f575f6d79b4d50bd877c0fb6844645aff6af4f2f8b2bb9bbe99` | 4375 *(restored legacy — katalog)* |

Manifest: [fix-manifest-20260628-193747.json](../reports/home-commercial-trust-work/fix-manifest-20260628-193747.json)

## Authority chain

- Visual/CSS: `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` + `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`
- Markup source: catalog `zpm-commercial-trust` (`blockcommercialtrust.twig` first section — no PLP FAQ grid on Home)
- JS: existing dealer form handler — `.zpm-dealers[data-dealers] .zpm-form` (dual class hook on Home block)

## Backups

Suffix `.pre-home-commercial-trust-01.bak` in `backups/` — see deployment report.

## Rollback

```bash
python projects/ocpilot/sites/site-002/reports/home-commercial-trust-work/site-002-home-commercial-trust-rollback.py
```

## Supersedes (Home CTA only)

- Legacy Home `zpm-dealers` + bare `zpm-form` layout — **historical** on Home only

## Preserved baselines

- `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`
- `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`
- `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` (CSS authority)

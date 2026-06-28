# SITE-002 — STABLE LIVE — Operator Manual Polish 01

**Status:** **ACTIVE** on TEST — **sole visual/behavioural authority** for SITE-002  
**URL:** https://zpm.new-site.space/  
**Date:** 2026-06-29  
**Report:** [SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md](../reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md)

## Authority policy

| Rule | Value |
|------|--------|
| **Operator manual CSS** | **CANONICAL** |
| **Operator manual HTML/Twig** | **CANONICAL** |
| **Operator manual JS** | **CANONICAL** |
| **Do NOT use as reference** | Pass 1.2 CSS/HTML/JS work copies, Pass 1.1 deploy snapshots, pre-checkpoint backups except for rollback |

## Live artifact hashes (post-capture)

| Artifact | SHA256 | Bytes |
|----------|--------|-------|
| `assets/css/style.css` | `1d190d97953cfaab17bb1f9948e0eecafb777710d7c1ba613a35181b28e88a86` | 379934 |
| `assets/js/main.js` | `17cb1fffe8831d4ac633d5bd41e047c31b4fd478a0e1cfa67c8667c42ab539e8` | 204187 |
| `catalog/view/theme/default/template/information/dealers.twig` | `ecc6dc8b06faa8f9691edb02b6c10cee6eec22982d7d34275e163c3cd7370b5c` | 45886 |

Full capture manifest: [capture-manifest.json](../reports/site-002-operator-manual-polish-01-work/capture-manifest.json)

## Operator manual delta vs Pass 1.2

| File | vs Pass 1.2 |
|------|-------------|
| `assets/css/style.css` | **CHANGED** — Pass 1.2 post SHA256 was `243d6d5e2a1ad00c06c450f4b90dc72adb1671b64a681f266675abdbd9330252` |
| `catalog/view/theme/default/template/information/dealers.twig` | **CHANGED** vs Pass 1.1 deploy snapshot — operator manual edit on TEST |
| All other captured corp/catalog files | **Same** as prior deploy snapshots at capture time |

Pass 1.2 did **not** deploy Twig/JS — those files are registered as live authority from FTP capture.

## Scope

Full TEST storefront authority after operator manual polish following Visual Polish Pass 1.2:

- Home · About · Delivery · Payment · Warranty · Dealers · Custom Manufacturing · Catalog · PDP support files

## Backups

Checkpoint backups in `backups/` with suffix `.pre-site-002-operator-manual-polish-01.bak` — see capture manifest.

## Rollback

1. Beget full backup (operator)  
2. Restore files from `backups/*.pre-site-002-operator-manual-polish-01.bak` via FTP  
3. Clear Twig cache `system/storage/cache/template/`

## Supersedes

- `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` — **historical**; do **not** use Pass 1.2 CSS/HTML/JS as reference  
- Pass 1.1 · Pass 1 (rejected) — historical only

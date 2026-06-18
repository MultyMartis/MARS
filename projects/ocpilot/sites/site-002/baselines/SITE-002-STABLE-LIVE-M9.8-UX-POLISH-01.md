# SITE-002 — Stable Live M9.8 UX Polish Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-19 (operator-requested stable checkpoint after M9.8 deploy passes and manual PLP polish)  
**Mode:** Metadata-only registration — **no FTP**, **no deploy**, **no file capture**

---

## 1. Authority state

`SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`

---

## 2. Current source of truth

| Priority | Source | Notes |
|----------|--------|-------|
| **1** | **Live TEST** — https://zpm.new-site.space/ | Authoritative storefront state |
| **2** | **Full Beget backup** | Operator attestation — new full backup completed |
| **3** | **Manual UI refinements** | **CANONICAL** |
| **4** | **Manual CSS refinements** | **CANONICAL** |
| **5** | **Manual Twig refinements** | **CANONICAL** |

Prior repo baselines, work copies (`*-work/`), `backups/stable-*` folders, and pre-pass `.bak` files are **historical** and must **not** be treated as current live state without a fresh live capture.

**Do not** use old work copies as baseline for the next task.

---

## 3. Registration context

This checkpoint supersedes `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` for **current live truth** and records the post-pass live state after M9.8 deploy passes and operator manual PLP polish.

---

## 4. Completed work (registered)

### M9.8 deploy passes

| Pass | Status on live |
|------|----------------|
| **M9.8.1 — PDP Gallery Compact** | **active** |
| **M9.8.2 — PDP Lightbox Constraints** | **active** |
| **M9.8.5 — Products Per Page Selector** | **active** |

### Operator manual refinements (CANONICAL)

| Pass | Status on live |
|------|----------------|
| **PLP Grid Density Pass** | **active** |
| **PLP Compact Pass** | **active** |
| **Filter Compact Pass** | **active** |
| **Breakpoint Polish Pass** | **active** |
| **Manual CSS Refinement Pass** | **active** |
| **Manual Twig Refinement Pass** | **active** |

---

## 5. Active stable state summary

| Item | Value |
|------|--------|
| Authority | **`SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`** |
| M9.8.1 PDP Gallery Compact | **active** — side-rail thumbs layout + responsive reinit |
| M9.8.2 PDP Lightbox Constraints | **active** — constrained Fancybox viewport (desktop 80vw/80vh; mobile 95vw/90vh) |
| M9.8.5 Products Per Page Selector | **active** — limit selector 10 / 20 / 50 / 100 on PLP |
| Manual PLP / filter / breakpoint polish | **active** — operator CSS/Twig edits supersede prior captures |
| Live truth | **hosting state on `zpm.new-site.space`** |
| Beget backup | Operator attests **full global backup exists** (new backup after manual polish) |

---

## 6. Pass evidence (repo references — not live verification)

| Pass | Evidence |
|------|----------|
| M9.8.1 PDP Gallery Compact | `m9.8.1-pdp-gallery-compact-work/` · [m9.8.1-pdp-gallery-compact-qa-result.json](../qa/m9.8.1-pdp-gallery-compact/m9.8.1-pdp-gallery-compact-qa-result.json) |
| M9.8.2 PDP Lightbox Constraints | `m9.8.2-pdp-lightbox-constraints-work/` · [m9.8.2-pdp-lightbox-constraints-qa-result.json](../qa/m9.8.2-pdp-lightbox-constraints/m9.8.2-pdp-lightbox-constraints-qa-result.json) |
| M9.8.5 Products Per Page Selector | `m9.8.5-products-per-page-work/` · [m9.8.5-products-per-page-qa-result.json](../qa/m9.8.5-products-per-page/m9.8.5-products-per-page-qa-result.json) |
| Manual PLP / filter / breakpoint / CSS / Twig passes | Operator attestation only — no separate repo deploy pack |

This checkpoint does **not** re-verify live files — operator attestation + pass QA artifacts only.

---

## 7. Beget global backup

The operator attests a **new Beget full global backup** exists on hosting after manual PLP polish. This external backup is part of the recovery chain alongside live operator state.

**This checkpoint does not contain or verify Beget backup artifacts** — operator attestation only.

---

## 8. This checkpoint does NOT contain site files

This registration is a **metadata-only checkpoint**:

| Included | Not included |
|----------|--------------|
| Baseline name and registration timestamp | FTP download of `public_html` |
| Active pass inventory and recovery strategy | `config.php` |
| OCPilot state / passport updates | Database dumps |
| Operator attestation of live state | SHA256 manifests of current live files |
| Supersedes prior live checkpoints for live truth | Vendor trees, full screenshot archives |

**No site files were downloaded for this checkpoint.**

---

## 9. Rollback source

Rollback / restore options, in order of scope:

1. **Beget full backup** — full hosting restore (operator-controlled; external to repo)
2. **Current live TEST state** — operator live state on https://zpm.new-site.space/
3. **File-level backups from completed passes** — `backups/*.pre-*`, pass deploy manifests in `backups/` — **specific file rollback only**
4. **Prior repo STABLE folders** — historical; **not** guaranteed to match post-M9.8 live state

**Rollback source for this checkpoint:** **Beget full backup + current live TEST state + file-level pass backups**.

---

## 10. Rule before next tasks

Before any next SITE-002 change:

1. Identify the **specific live files** that will be touched (Twig, CSS, JS, PHP).
2. Perform **live-capture of only those files** (FTP read + SHA256) immediately before agent edits.
3. Do **not** rely on old work copies (`*-work/`, prior `stable-*` folders, `.pre-*.bak` from earlier passes) as current truth.

See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md).

---

## Status

| Field | Value |
|-------|--------|
| Checkpoint type | **STABLE LIVE CHECKPOINT** (metadata-only) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Prior authority (file baseline) | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` — historical for file rollback only |
| Rollback source | **Beget full backup + current live TEST + file-level pass backups** |
| Deploy | **NO** |
| FTP changes | **NO** |

---

*Documentation only — no runtime claimed.*

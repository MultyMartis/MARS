# SITE-002 — Stable Live PDP V5.1 Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-14 21:00:00 (local operator time)  
**Mode:** Metadata-only registration — **no FTP**, **no deploy**, **no file capture**

---

## 1. Baseline name

`SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14`

---

## 2. Registration date and time

**2026-06-14 21:00:00** — operator-requested stable checkpoint after PDP V5.1 scroll offset polish pass and all prior live passes on 2026-06-14.

---

## 3. Live site is source-of-truth

The **current live TEST storefront** on hosting is the authoritative source-of-truth for SITE-002.

This checkpoint supersedes `SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14` for **current live truth** and records the post-pass live state after:

| Pass | Status on live |
|------|----------------|
| **PDP V5.1 — Specifications Collapse** | **active** |
| **PDP V5.1 — Scroll UX Fix** | **active** |
| **PDP V5.1 — Scroll Offset Polish** | **active** (QA pass) |
| **Category V2.3.1 — Subcategory Polish** | **active** |
| **Operator manual visual polish** | **active** |

Prior repo baselines, work copies (`*-work/`), and `backups/stable-*` folders are **historical** and must **not** be treated as current live state without a fresh live capture.

**Do not** use old work copies as baseline for the next task.

---

## 4. Active stable state summary

| Item | Value |
|------|--------|
| PDP generation | **V5.1** |
| Specs collapse | **active** — `data-product-specs-toggle` in `producttabs.twig` + scoped CSS/JS |
| Scroll UX | **active** — tab/content scroll behavior in `main.js` |
| Scroll offset | **active** — `scrollToProductContentMain` with desktop 140px / mobile 100px offset (QA pass) |
| Category | **V2.3.1** subcategory polish **active** |
| Manual operator edits | **active** — live CSS/Twig polish supersede prior captures |
| Live truth | **hosting state on `zpm.new-site.space`** |
| Beget backup | Operator attests **full global backup exists** |

---

## 5. Pass evidence (repo references — not live verification)

| Pass | Evidence |
|------|----------|
| PDP V5.1 Specs Collapse | [SITE-002-PDP-V5.1-SPECIFICATIONS-COLLAPSE-PASS.md](../reports/SITE-002-PDP-V5.1-SPECIFICATIONS-COLLAPSE-PASS.md) |
| PDP V5.1 Scroll UX Fix | `backups/pdp-v5.1-scroll-ux-fix-deploy-manifest-20260614-132010.json` · `qa/pdp-v5.1-scroll-ux-fix/` |
| PDP V5.1 Scroll Offset Polish | `backups/pdp-v5.1-scroll-offset-polish-deploy-manifest-20260614-135747.json` · [pdp-v5.1-scroll-offset-polish-qa-result.json](../qa/pdp-v5.1-scroll-offset-polish/pdp-v5.1-scroll-offset-polish-qa-result.json) |
| Category V2.3.1 Subcategory Polish | [SITE-002-CATEGORY-V2.3.1-SUBCATEGORY-POLISH-PASS.md](../reports/SITE-002-CATEGORY-V2.3.1-SUBCATEGORY-POLISH-PASS.md) |

This checkpoint does **not** re-verify live files — operator attestation + pass reports only.

---

## 6. Beget global backup

The operator attests a **Beget full global backup** exists on hosting. This external backup is part of the recovery chain alongside live operator state.

**This checkpoint does not contain or verify Beget backup artifacts** — operator attestation only.

---

## 7. This checkpoint does NOT contain site files

This registration is a **metadata-only checkpoint**:

| Included | Not included |
|----------|--------------|
| Baseline name and registration timestamp | FTP download of `public_html` |
| Active pass inventory and recovery strategy | `config.php` |
| OCPilot state / passport updates | Database dumps |
| Operator attestation of live state | SHA256 manifests of current live files |
| Supersedes prior compact checkpoint for live truth | Vendor trees, full screenshot archives |

**No site files were downloaded for this checkpoint.**

---

## 8. Recovery strategy

Rollback / restore options, in order of scope:

1. **Beget global backup** — full hosting restore (operator-controlled; external to repo)
2. **Operator live state** — manual rollback on FTP using operator's knowledge of current live files
3. **Pass-level repo backups** — `backups/*.pre-pdp-v5.1-*`, `backups/*.pre-pdp-specs-collapse-pass.bak`, etc. — **specific file rollback only**
4. **Prior repo STABLE folders** — historical; **not** guaranteed to match post-PDP-V5.1 live state

**Rollback source for this checkpoint:** **Beget global backup + operator live state**.

---

## 9. Rule before next tasks

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
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14` |
| Rollback source | **Beget global backup + operator live state** |
| Deploy | **NO** |
| FTP changes | **NO** |

---

*Documentation only — no runtime claimed.*

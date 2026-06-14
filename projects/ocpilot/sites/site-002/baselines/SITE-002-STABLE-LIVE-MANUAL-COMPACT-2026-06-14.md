# SITE-002 — Stable Live Manual Compact Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-14 17:45:27 (local operator time)  
**Mode:** Metadata-only registration — **no FTP**, **no deploy**, **no file capture**

---

## 1. Baseline name

`SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14`

---

## 2. Registration date and time

**2026-06-14 17:45:27** — operator-requested stable checkpoint registration in OCPilot/MARS.

---

## 3. Live site is source-of-truth

The **current live TEST storefront** on hosting is the authoritative source-of-truth for SITE-002 after operator manual edits:

- **PDP** — manually refined by operator
- **Category** — manually refined by operator
- **CSS / Twig** — operator live edits supersede prior local work copies and agent captures

Prior repo baselines (`SITE-002-STABLE-PDP-V4-2026-06-10`, `SITE-002-STABLE-CATEGORY-V2.2-2026-06-10`, and related folders) are **historical** and must **not** be treated as current live state after operator manual passes.

---

## 4. Beget global backup

The operator has performed a **Beget global backup** on hosting. This external backup is part of the recovery chain alongside live operator state.

**This checkpoint does not contain or verify Beget backup artifacts** — operator attestation only.

---

## 5. This checkpoint does NOT contain site files

This registration is a **compact metadata checkpoint**:

| Included | Not included |
|----------|--------------|
| Baseline name and registration timestamp | FTP download of `public_html` |
| Recovery strategy documentation | `config.php` |
| OCPilot state / passport updates | Database dumps |
| Working rules update | SHA256 manifests of current live files |
| Operator attestation of live state | Vendor trees, screenshots, deploy scripts |

**No site files were downloaded for this checkpoint.**

---

## 6. Recovery strategy

Rollback / restore options, in order of scope:

1. **Beget global backup** — full hosting restore (operator-controlled; external to repo)
2. **Operator live state** — manual rollback on FTP using operator's knowledge of current live files
3. **Prior repo STABLE folders** — point rollback for **specific historical passes only**; **not** guaranteed to match post-manual-edit live state

**Do not** assume repo `backups/stable-*` folders reflect live after operator manual edits without a fresh live capture.

---

## 7. Rule before next tasks

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
| Rollback source | **Beget global backup + operator live state** |
| Supersedes (for live truth) | All prior repo file captures where operator manual edits occurred after capture |
| Related report | [SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md](../reports/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md) |

---

*Documentation only — no runtime claimed.*

# REPORT — SITE-002 Production FTP Path Reconciliation

**Site ID:** SITE-002  
**Project:** ЗПМ / BZPM  
**OCPilot run:** 4.172  
**Date:** 2026-07-03  
**Mode:** read-only FTP verification · documentation reconciliation · local tool fixes  
**Production URL:** https://bzpm.ru/

---

## 1. Scope

Eliminate documentary ambiguity between:

- FTP login root
- Application root
- Public document root
- OpenCart storage root

No remote file mutations. No secrets changes. Baseline `SITE-002-STABLE-PROD-INITIAL-01` retained — path interpretation only.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS\` |
| Volume | `X:` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `65c7f029dfb7b5fb0c0f8e9e341dfde5b8d60e3d` |
| Secrets edited | **NO** |
| Foreign WIP touched | **NO** |

---

## 3. FTP login namespace

| Field | Value |
|-------|--------|
| FTP host | `assum.beget.tech` (from secrets — not logged) |
| Login `PWD` | `/` |
| First-level directories | `public_html/`, `storage/` |
| Virtual `/bzpm.ru/` path | listable but **empty** (no OpenCart markers) |
| Chroot interpretation | FTP account chrooted to hosting application root `/bzpm.ru/`; login `/` ≡ hosting `/bzpm.ru/` |

Evidence: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\verification\SITE-002-FTP-PATH-RECONCILIATION-01.json`

---

## 4. Application root

| Path concept | Hosting / application path | FTP-visible path | Status | Evidence |
|--------------|---------------------------|------------------|--------|----------|
| Application root | `/bzpm.ru/` | `/` (chrooted login) | **CONFIRMED** | Secrets `Remote root`; FTP login shows `public_html/` + `storage/` siblings |

---

## 5. Public document root

| Path concept | Hosting / application path | FTP-visible path | Status | Evidence |
|--------------|---------------------------|------------------|--------|----------|
| Public document root | `/bzpm.ru/public_html/` | `/public_html/` | **CONFIRMED** | OpenCart markers present |

**Markers inside `/public_html/` (existence only — not downloaded):**

| Marker | Present |
|--------|---------|
| `index.php` | yes |
| `config.php` | yes |
| `admin/` | yes |
| `catalog/` | yes |
| `system/` | yes |
| `image/` | yes |

`/bzpm.ru/public_html/` on FTP: listable but **empty** — not the live document root inside this chroot.

---

## 6. OpenCart storage root

| Path concept | Hosting / application path | FTP-visible path | Status | Evidence |
|--------------|---------------------------|------------------|--------|----------|
| OpenCart storage root | `/bzpm.ru/storage/` | `/storage/` | **CONFIRMED** | `cache/`, `download/`, `logs/`, `modification/`, `session/`, `upload/`, `vendor/` |

No recursive inventory of logs, sessions, cache, or upload data performed.

---

## 7. guarantee.twig verification

| Field | Value |
|-------|--------|
| Hosting path | `/bzpm.ru/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| FTP-visible path | `/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| Status | **CONFIRMED** |
| Size (FTP `SIZE`) | 46856 bytes |
| `/bzpm.ru/public_html/...` variant | **NOT FOUND** (550 on SIZE) |

Operator-confirmed Production file path reconciled with FTP chroot semantics.

---

## 8. Chroot / path interpretation

**Rule:** hosting path and FTP-visible path may differ because of chroot. This does **not** mean application root equals `/public_html/`.

| Term | Correct meaning for SITE-002 Production |
|------|----------------------------------------|
| Secrets `Remote root` | Application root `/bzpm.ru/` |
| Public deploy root | `public_html/` inside application root |
| FTP login `/` | Chrooted view of `/bzpm.ru/` |
| FTP deploy path for theme files | `/public_html/<relative-opencart-path>` |

**Incorrect (fixed in docs):** describing `/public_html/` as the root of the entire OpenCart installation.

---

## 9. Documentation updates

| File | Change |
|------|--------|
| `production-profile.md` | Added path model table; clarified secrets semantics |
| `site-passport.md` | Production connection note; parity status |
| `project-access-brief.md` | Path model section; FTP access summary |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | Production path model block |
| `baselines/SITE-002-STABLE-PROD-INITIAL-01.md` | Application / public / storage roots; guarantee paths |
| `reports/SITE-002-FIRST-PRODUCTION-CAPTURE.md` | Run 4.172 reconciliation note; operator note corrected |
| `OCPILOT-STATE.md` | Evidence cutoff; FTP path model |
| `OPERATIONAL-INDEX.md` | Run 4.172 entry |

`secrets.md`: **not modified** — `Remote root: /bzpm.ru/` retained as application root.

---

## 10. Tool updates

| File | Change |
|------|--------|
| `site-002-prod-readonly-capture.py` | Added `resolve_production_paths()`; inventory/downloads use `ftp_visible_public_root` |
| `site-002-prod-ftp-retry.py` | Uses shared path resolver; connection artefacts carry full path model |
| `site-002-prod-ftp-path-verify.py` | **NEW** — read-only path verification helper (Run 4.172) |
| `tools/README.md` | Registered new verify script |

Tools remain read-only by default; no hardcoded credentials; no `C:` historical paths.

---

## 11. Baseline impact

| Item | Status |
|------|--------|
| Checkpoint `SITE-002-STABLE-PROD-INITIAL-01` | **RETAINED** |
| HTTP capture | not re-run |
| Screenshots | not re-run |
| Admin capture | not re-run |
| FTP inventory / downloads | not re-run |
| Checksums | unchanged |
| Baseline revoked | **NO** |

Only root-path **interpretation** in documentation was corrected.

---

## 12. Remote mutation confirmation

```text
Remote uploads: 0
Remote edits: 0
Remote deletes: 0
Remote renames: 0
Database operations: 0
```

---

## 13. Git status

Selective commit scoped to repository documentation + tools. Storage verification JSON and secrets excluded from Git.

---

## 14. Final verdict

```text
SITE-002 PRODUCTION PATH MODEL CONFIRMED — READY FOR FIRST CONTROLLED PRODUCTION CHANGE
```

Application root `/bzpm.ru/`, public document root `/bzpm.ru/public_html/`, and OpenCart storage root `/bzpm.ru/storage/` are confirmed. FTP-visible equivalents are `/`, `/public_html/`, and `/storage/` respectively under chroot.

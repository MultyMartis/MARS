# MARS Localhost MLI-02 — Cleanup Decisions v1

**Document type:** Cleanup decisions report  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## `D:\MARS-Localhost\runtime\laragon`

| Check | Finding |
|-------|---------|
| Exists | **Yes** |
| Contents | **Empty** (placeholder from MLI-00) |
| In use | **No** — canonical Laragon at `D:\MARS-Localhost\laragon` |
| Action | **Recommendation only** — operator may delete after explicit approval |
| Auto-delete | **NOT PERFORMED** |

---

## `laragon.cmd` stale paths

| Path | Issue |
|------|-------|
| `laragon\bin\laragon\laragon.cmd` | References `D:\Projects\Laragon-installer\6.0-W64\` |

| Decision |
|----------|
| **DEPRECATED** for MLI workflows |
| **NOT auto-patched** — risk of breaking Laragon UI assumptions |
| **Canonical CLI** remains `D:\MARS-Localhost\tools\activate-mli.cmd` |

---

## Related

- [MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md](../MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md)

---

*Cleanup decisions v1 — MLI-02.*

# RUN-5 — First Findings (Repository Evidence Only)

**Site:** SITE-001 — Автосалон СИБКАР  
**Run:** 5 — initialization  
**Evidence cutoff:** 2026-06-01  
**Rule:** No live site assumptions. No invented technical findings.

---

## Known facts (provable from repository or non-secret external layout)

### Site identity and charter

| Fact | Source |
|------|--------|
| Site ID **SITE-001**, name **Автосалон СИБКАР** | [site-passport.md](../site-passport.md), [project-access-brief.md](../project-access-brief.md) |
| Environment **TEST** | Passport, access brief, [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) |
| Claimed platform **ocStore**, version **3.0.3.8 (rs.2)** | Passport, access brief — **operator-recorded, not file-verified on live site** |
| Approved baseline **`ocstore-3038-rs2`** | [INTAKE-COMPLETE.md](../materials/INTAKE-COMPLETE.md), charter, [project-site-registry.md](../../../project-site-registry.md) |
| Read-only audit **authorized** | [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) — status READY FOR RUN 5 |
| Registry status **READY FOR AUDIT** | [project-site-registry.md](../../../project-site-registry.md) |
| Intake closed **2026-06-01** (Run 4.99) | [intake-readiness-review.md](../../../intake-readiness-review.md) |

### URLs and access (non-secret)

| Fact | Source |
|------|--------|
| Test URL documented: `https://sibcar.new-site.space/` | [project-access-brief.md](../project-access-brief.md), passport |
| Public URL | **SAFE UNKNOWN** (access brief) |
| Admin URL | **SAFE UNKNOWN** |
| Access types marked available (hosting, FTP, SSH, PMA, admin, DB) | Access brief — **channels not confirmed for Run 5 execution** |
| Credentials | External only — **not inspected** (`secrets/` exists on disk; contents not read into this report) |

### Backup (operator-recorded)

| Fact | Source |
|------|--------|
| File + DB backup claimed **YES** | Access brief (updated block) |
| Backup date **31.05.2026**, location **Beget backup system** | Access brief |
| Independent verification | **Not performed** in this run |

### Business context (operator checklist, not technical proof)

Access brief lists planned work items as checked: rebranding, vehicle catalog import, SEO, Yandex Direct, design/theme changes, technical audit, etc. These describe **project intent**, not verified implementation state.

### Baseline readiness (comparison reference)

| Fact | Source |
|------|--------|
| Baseline folder **READY** | [baselines/ocstore-3038-rs2/README.md](../../../baselines/ocstore-3038-rs2/README.md) |
| Promoted vendor tree **~4055 files** under `files/` | [ocstore-3038-rs2-passport-v1.md](../../../baselines/ocstore-3038-rs2/passports/ocstore-3038-rs2-passport-v1.md) |
| Canonical ZIP SHA256 documented | [baseline-manifest-v1.md](../../../baselines/ocstore-3038-rs2/manifest/baseline-manifest-v1.md) |
| Baseline `index.php` defines **VERSION `3.0.3.8`** | Baseline manifest (selective extract note) |
| ocStore signals in baseline: `ru-ru/`, `tweak.ocmod.xml`, `tweak-54fz.ocmod.xml` | Baseline manifest |
| Install SQL **136** tables, default prefix **`oc_`** | [database-metadata-v1.md](../../../baselines/ocstore-3038-rs2/database/database-metadata-v1.md) |
| `comparison-notes/` | **Empty** (placeholder only) |

### External storage (layout only — no site snapshot content reviewed)

| Fact | Source |
|------|--------|
| Path exists: `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\` | Passport, [external-storage-registry.md](../../../external-storage-registry.md) |
| Subfolders present: `audits/`, `backups/`, `materials/`, `reports/`, `snapshots/`, `temp/`, `secrets/` | Filesystem listing (2026-06-01) |
| Bulk content | **Not present** — subfolders contain `.gitkeep` or README only; **no file manifest or site ZIP** in external storage at initialization |

### Repository site workspace

| Fact | Source |
|------|--------|
| Repo metadata files present | `site-passport.md`, `AUDIT-CHARTER.md`, `project-access-brief.md`, `materials/INTAKE-COMPLETE.md`, `README.md` |
| Analysis subfolders (`opencart-analysis/`, `theme-analysis/`, etc.) | **Not created** in repo — [README.md](../README.md) describes template map only |
| Run 5 deliverables (this run) | `tasks/RUN-5-DATA-REQUEST.md`, `reports/RUN-5-*.md` |

---

## Known unknowns (SAFE UNKNOWN)

| Topic | Why unknown | What would verify |
|-------|-------------|-------------------|
| Live site is ocStore **3.0.3.8 (rs.2)** | Only operator brief + intake marker; no site `index.php` in repo/external bulk | P1-A version excerpts |
| **rs.2** build identity on live site | rs suffix not verified from live tree | Package folder signals, OCMOD set vs baseline |
| File diff vs baseline | No site file manifest | P1-C manifest or P2-C snapshot |
| Active theme | Passport lists as pending | P2-A |
| Installed extensions / ocMod | No inventory | P2-B |
| SEO URL mode and aliases | No storefront/DB evidence | P3-A |
| DB table set beyond core 136 | No `SHOW TABLES` | P3-B |
| Hosting provider | Passport / brief | Operator note or hosting panel metadata (non-secret) |
| Admin URL | Brief | P3-C |
| Catalog scale (products, categories) | Not in repo | Admin read-only or DB counts (chartered later) |
| Custom modules / dealership logic | Not in repo | File diff + extension inventory |
| Whether prior rebranding/import/SEO work left technical traces | Business checklist ≠ audit proof | Phases 3–7 |
| Backup restorability | Claim only | Operator restore drill (out of scope Run 5 init) |
| Malware / compromised core | No scan chartered | Separate security charter |
| Quarantine intake report artifact | Passport notes gap | Operator material if exists |

---

## Documentation inconsistencies (not site findings)

| Item | Observation |
|------|-------------|
| [project-access-brief.md](../project-access-brief.md) header | **INTAKE IN PROGRESS**; **Run 5 allowed: NO** |
| [site-passport.md](../site-passport.md), charter, intake review | **READY FOR RUN 5** / Run 5 **YES** |
| [sites/site-001/README.md](../README.md) | Still **AWAITING INTAKE** / Run 5 gate **NO** — stale template text |
| **Resolution** | Operator may align brief/README; Run 5 initialization follows **AUDIT-CHARTER** + intake review **YES** |

---

## Expected audit targets (after evidence intake)

These are **targets for Phases 2–8**, not current findings:

| Target | Audit question |
|--------|----------------|
| Version gate | Confirm `3.0.3.8` + ocStore markers match baseline |
| File delta | Added/removed/modified paths vs `baselines/ocstore-3038-rs2/files/` |
| ocMod / extensions | Inventory and classify third-party vs project |
| Theme | Active theme vs baseline `default` |
| SEO | `seo_url` configuration and TEST storefront routes |
| Schema | Extra tables vs 136 baseline tables |
| Core edits | Modified files in `system/`, `catalog/controller` not explained by ocMod |
| Risks | Version skew, 3039 mismatch, dense ocMod on core, missing backups evidence, TEST vs prod drift |

---

## Risks visible from metadata only (not live site)

| Risk | Severity | Basis |
|------|----------|--------|
| **Comparison blocked** until P1 evidence | High | No site manifest or snapshot in repo/external bulk |
| **Version unverified on live system** | High | Baseline match assumed from intake, not file proof |
| **Stale access brief gate** | Medium | Operator confusion on Run 5 permission |
| **Empty `comparison-notes/`** | Medium | ocStore-specific subtraction incomplete in methodology |
| **Business goals marked done** | Medium | May imply prior core/theme edits — increases diff surface; unverified |
| **Secrets folder on operator machine** | Low (process) | Correct external placement; agent must not copy to git |
| **TEST URL only** | Low | Prod drift unknown if prod exists later |

---

## What OCPilot should inspect next (ordered)

1. **Operator:** Deliver Priority 1 in [RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md).  
2. **Phase 2:** Version verification report in `opencart-analysis/`.  
3. **Phase 3:** File manifest diff vs `ocstore-3038-rs2/files/`.  
4. **Phase 4–5:** Theme + extension/ocMod inventories.  
5. **Phase 6–7:** SEO + DB schema metadata.  
6. **Phase 8:** Consolidated `RUN-5-AUDIT-REPORT.md` + risk/next-run list.  
7. **Optional human:** Refresh [project-access-brief.md](../project-access-brief.md) Run 5 gate and [README.md](../README.md) status.

---

## Related documents

- [RUN-5-AUDIT-PLAN.md](RUN-5-AUDIT-PLAN.md)  
- [RUN-5-SCOPE.md](RUN-5-SCOPE.md)  
- [RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md)

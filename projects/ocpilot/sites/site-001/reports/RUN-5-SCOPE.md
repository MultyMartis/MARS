# RUN-5 — Scope Definition (SITE-001)

**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST  
**Run:** 5 — First Read-Only Site Audit  
**Charter:** [AUDIT-CHARTER.md](../AUDIT-CHARTER.md)  
**Date:** 2026-06-01 (initialization)

---

## IN SCOPE

### Authorization and identity

- Read-only audit per [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) and [intake-readiness-review.md](../../../intake-readiness-review.md)
- Site identity, environment, and claimed version from passport and access brief
- Baseline comparison against `baselines/ocstore-3038-rs2/` per approved match

### Technical inspection (read-only, evidence-based)

| Area | Scope |
|------|--------|
| **Platform / version** | Verify ocStore 3.0.3.8 (rs.2) from file/admin evidence |
| **File structure** | Path inventory and diff vs baseline vendor tree |
| **Core / ocStore deltas** | Classify per [baseline-comparison-methodology.md](../../../baseline-comparison-methodology.md) |
| **Extensions** | Installed modules, payment/shipping/feed paths, ocMod XML inventory |
| **Theme** | Active theme name, `catalog/view/theme/` architecture |
| **SEO** | SEO URL mode, alias structure, sample public routes (TEST) |
| **Database metadata** | Table list, prefix, extra tables vs baseline schema metadata — **no row dumps** |
| **Risks** | Visible structural risks (version mismatch, orphan mods, core edits, stale backups) |
| **Documentation** | Reports and analysis folders under `projects/ocpilot/sites/site-001/` |

### Evidence sources allowed

- Repository metadata and baseline files
- Operator-supplied sanitized artifacts per [RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md)
- External bulk at `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\` (metadata references in repo only)
- Supervised read-only: SFTP listing, SSH read, hosting file manager view, admin read-only navigation, phpMyAdmin structure queries — **only after operator confirms channel (P3-C)**

### Business context (documentation only)

- Stated goals: rebranding, catalog, SEO, Yandex Direct prep ([project-access-brief.md](../project-access-brief.md))
- Findings framed as audit facts, not marketing claims

---

## OUT OF SCOPE

### Changes and operations

| Excluded | Notes |
|----------|--------|
| File modifications on live site | Any write to TEST or other env |
| Database modifications | INSERT/UPDATE/DELETE, migrations, imports |
| Admin configuration changes | Settings, modules install/uninstall, user edits |
| Cache reset / modification refresh | Alters runtime state |
| Theme / controller / model edits | Including hotfixes |
| OCMOD install, edit, rebuild | Write operation |
| Product/catalog import | Business execution — future chartered run |
| Production environment | Unless separately chartered; current env **TEST** only |

### Security and compliance depth

- Credential collection or storage in git
- Penetration testing, malware scanning (not chartered; baseline passport notes no scan performed on vendor ZIP either)
- GDPR/legal review of privacy policies
- Performance/load testing

### Assumptions and automation

- Claiming audit results without operator evidence for live site state
- Automated diff platform (not implemented in OCPilot — human-operated comparison)
- Full binary compare of `image/catalog/` media
- Customer/order/PII data analysis

### Repository areas outside SITE-001 lane

- Modifying governance under `governance/` (unless separately chartered)
- Changing baseline vendor tree without baseline promotion workflow
- Other project sites (SITE-002+)

---

## READ ONLY GUARANTEES

### OCPilot / agent commitments (Run 5)

| Guarantee | Detail |
|-----------|--------|
| **No live writes** | No FTP upload, no file save on host, no git commit of site code |
| **No DB writes** | No data change via PMA or CLI |
| **No admin writes** | No install/uninstall, no setting save, no modification refresh |
| **Repo writes limited** | Documentation and analysis markdown under `projects/ocpilot/sites/site-001/` only |
| **No secrets in repo** | Credentials stay in external `secrets/` — not read into git-tracked files |
| **SAFE UNKNOWN** | Used when live site state cannot be proven |
| **Stop on charter conflict** | If evidence requires write to proceed, halt and request human charter |

### Operator commitments (expected)

- Supply sanitized evidence per data request
- Use TEST environment for storefront sampling unless redirected
- Confirm backup exists before any **future** write run (backup claimed 31.05.2026 Beget — not independently verified in this run)
- Supervise any admin/PMA session

### Evidence handling

| Allowed | Forbidden |
|---------|-----------|
| Path lists, sizes, hashes | Full `config.php` with secrets |
| VERSION constants | API keys, SMTP passwords |
| Table names, counts | Full mysqldump with rows |
| Redacted screenshots | Session cookies in repo |

---

## Environment boundary

| Field | Value |
|-------|-------|
| **Target environment** | TEST |
| **Test URL (documented)** | `https://sibcar.new-site.space/` |
| **Production** | OUT OF SCOPE unless new charter |
| **Write on TEST** | OUT OF SCOPE for Run 5 |

---

## Phase boundary (this run vs follow-on)

| Run 5 initialization (complete) | Run 5 execution (follow-on) |
|--------------------------------|-----------------------------|
| Scope, plan, data request, repo-only findings | Phases 1–8 per [RUN-5-AUDIT-PLAN.md](RUN-5-AUDIT-PLAN.md) |
| No live inspection | Requires P1 evidence + operator supervision |

---

## Related documents

- [AUDIT-CHARTER.md](../AUDIT-CHARTER.md)  
- [RUN-5-AUDIT-PLAN.md](RUN-5-AUDIT-PLAN.md)  
- [RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md)  
- [project-access-brief.md](../project-access-brief.md)

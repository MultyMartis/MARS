# RUN-5 — Audit Plan (SITE-001)

**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST  
**Platform (claimed):** ocStore 3.0.3.8 (rs.2)  
**Baseline:** `projects/ocpilot/baselines/ocstore-3038-rs2/`  
**Charter:** [AUDIT-CHARTER.md](../AUDIT-CHARTER.md)  
**Methodology:** [baseline-comparison-methodology.md](../../../baseline-comparison-methodology.md)

---

## Run 5 objective summary

| # | Audit question | Primary phase |
|---|----------------|---------------|
| 1 | Is the site really ocStore 3.0.3.8 rs.2? | Phase 2 |
| 2 | What differs from baseline? | Phase 3–7 |
| 3 | What customizations exist? | Phase 7 |
| 4 | What extensions/modifications exist? | Phase 5 |
| 5 | What theme architecture exists? | Phase 4 |
| 6 | What SEO structure exists? | Phase 6 |
| 7 | What risks are visible? | Phase 8 |
| 8 | What should OCPilot inspect next? | Phase 8 output |

---

## Audit phases

### Phase 0 — Initialization (this run)

| Item | Detail |
|------|--------|
| **Status** | **COMPLETE** (repository documentation only) |
| **Activities** | Charter review; baseline readiness confirm; data request; scope; first findings from repo evidence |
| **Outputs** | `tasks/RUN-5-DATA-REQUEST.md`, `reports/RUN-5-*.md` |
| **No live site access** | By design |

### Phase 1 — Evidence intake (operator)

| Item | Detail |
|------|--------|
| **Blocked by** | Priority 1 items in [RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md) |
| **Activities** | Receive manifests, version excerpts, layout confirmation; store bulk externally |
| **Outputs** | External paths logged in repo `materials/` index note (paths only); update `safe-unknown/` |
| **Gate** | P1 complete before any comparison claims |

### Phase 2 — Platform and version verification

| Item | Detail |
|------|--------|
| **Activities** | Cross-check `VERSION` in site `index.php` / `admin/index.php` vs baseline (`3.0.3.8`); detect ocStore signals (`ru-ru/`, `tweak.ocmod.xml`, `tweak-54fz.ocmod.xml` per baseline manifest) |
| **Outputs** | `opencart-analysis/version-verification-v1.md` |
| **Comparison** | Site signals vs [baseline-manifest-v1.md](../../../baselines/ocstore-3038-rs2/manifest/baseline-manifest-v1.md) |
| **SAFE UNKNOWN** | rs.2 build if folder naming / OCMOD set does not confirm rs.2 vs generic 3.0.3.8 |

### Phase 3 — File tree vs baseline (Layer 1–2)

| Item | Detail |
|------|--------|
| **Activities** | Path presence diff: added / missing / modified files under `admin/`, `catalog/`, `system/`; subtract known ocStore baseline paths |
| **Outputs** | `opencart-analysis/file-diff-summary-v1.md`; optional manifest in external storage |
| **Strategy** | Top-down: counts by subtree → high-risk paths (`system/engine`, `system/library`, modified core controllers) → full diff only where justified |
| **Baseline tree** | `baselines/ocstore-3038-rs2/files/` (~4055 files) |
| **Exclusions** | Cache, sessions, logs, bulk `image/catalog/` |

### Phase 4 — Theme architecture (Layer 3)

| Item | Detail |
|------|--------|
| **Blocked by** | P2-A active theme name |
| **Activities** | Map `catalog/view/theme/<active>/`; compare structure to baseline `default` theme; note overrides vs third-party theme package |
| **Outputs** | `theme-analysis/active-theme-inventory-v1.md` |

### Phase 5 — Extensions and ocMod (Layer 4)

| Item | Detail |
|------|--------|
| **Blocked by** | P2-B inventory |
| **Activities** | Inventory `extension/*` paths; list `system/*.ocmod.xml`; map modification cache footprint; classify per methodology |
| **Outputs** | `extension-analysis/extension-inventory-v1.md`, `extension-analysis/ocmod-inventory-v1.md` |

### Phase 6 — SEO structure

| Item | Detail |
|------|--------|
| **Blocked by** | P3-A |
| **Activities** | Document SEO URL mode, rewrite rules evidence (`.htaccess` pattern names only if sanitized), sample routes, `oc_seo_url` counts |
| **Outputs** | `seo-url-analysis/seo-structure-v1.md` |

### Phase 7 — Database schema metadata (cross-cutting)

| Item | Detail |
|------|--------|
| **Blocked by** | P3-B |
| **Activities** | Compare table list to baseline 136 core tables; list extra tables; confirm prefix |
| **Outputs** | `database-analysis/schema-delta-v1.md` |
| **No row data** | Schema names only |

### Phase 8 — Customizations, risks, next run

| Item | Detail |
|------|--------|
| **Activities** | Layer 5 project custom signals; risk register; prioritized next inspection targets |
| **Outputs** | `reports/RUN-5-AUDIT-REPORT.md` (final, after phases 2–7); `safe-unknown/open-items-v1.md` |
| **Template** | [inspection-report-template.md](../../../templates/inspection-report-template.md) |

---

## Comparison strategy

### Order (mandatory)

```
Evidence intake → Version confirm → File tree diff → ocStore layer subtract → Theme → Extensions/ocMod → SEO → DB metadata → Custom/Risks
```

### Classification (per methodology)

| Class | Recording folder |
|-------|------------------|
| OpenCart core | `opencart-analysis/` |
| ocStore modification | `opencart-analysis/` (tagged) |
| Third-party extension | `extension-analysis/` |
| Theme modification | `theme-analysis/` |
| Project customization | `controller-analysis/`, `database-analysis/` |
| SAFE UNKNOWN | `safe-unknown/` |

### Diff mechanics (human-operated)

| Approach | When |
|----------|------|
| Manifest compare (path + size) | First pass — Phase 3 |
| Selective content/hash compare | Modified paths flagged in manifest diff |
| Admin/screenshot inventory | Extensions when file tree ambiguous |
| Baseline reference | Always `ocstore-3038-rs2`; **do not** substitute `ocstore-3039-rs1` without version proof |

### Baseline readiness (precondition)

| Check | Status (repo evidence) |
|-------|------------------------|
| `files/` promoted | **YES** — Run 3.5 |
| Manifest present | **YES** — `baseline-manifest-v1.md` |
| Database metadata | **YES** — `database-metadata-v1.md` |
| `comparison-notes/` populated | **NO** — placeholder only; ocStore-vs-core deltas may be **SAFE UNKNOWN** until notes added |

---

## SAFE UNKNOWN handling

| Situation | Action |
|-----------|--------|
| Missing P1 evidence | **Stop** comparison; record in `safe-unknown/`; do not infer site file state |
| Version signals conflict | No baseline match claim; request re-verification |
| File differs, cause unclear | Label **SAFE UNKNOWN**; do not auto-tag as «custom» |
| rs.2 not provable | Report as 3.0.3.8 with rs build **SAFE UNKNOWN** |
| Empty `comparison-notes/` | Layer 2 ocStore subtraction incomplete — flag in report |
| External storage empty | Cannot verify operator materials; rely on new P1–P3 deliveries |

---

## Stop conditions

| Condition | Response |
|-----------|----------|
| Baseline fails [baseline-readiness-checklist.md](../../../baseline-readiness-checklist.md) | Halt; operator action (not current — baseline READY) |
| Platform/version **SAFE UNKNOWN** after Phase 2 | No layer 3+ claims beyond evidence |
| Wrong baseline version detected | Stop; re-run [baseline-match-workflow.md](../../../baseline-match-workflow.md) |
| Operator revokes read-only charter | Halt all inspection |
| Evidence contains secrets in repo path | Quarantine; do not commit; request redacted resubmit |
| Write operation requested mid-audit | Refuse; refer to charter |

---

## Expected final outputs (after Phases 1–8)

| Artifact | Location |
|----------|----------|
| Version verification | `opencart-analysis/version-verification-v1.md` |
| File diff summary | `opencart-analysis/file-diff-summary-v1.md` |
| Theme inventory | `theme-analysis/active-theme-inventory-v1.md` |
| Extension inventory | `extension-analysis/extension-inventory-v1.md` |
| SEO structure | `seo-url-analysis/seo-structure-v1.md` |
| Schema delta | `database-analysis/schema-delta-v1.md` |
| Consolidated audit report | `reports/RUN-5-AUDIT-REPORT.md` |
| Open unknowns | `safe-unknown/open-items-v1.md` |

---

## Registry status (planned)

| Transition | When |
|------------|------|
| READY FOR AUDIT → AUDIT IN PROGRESS | Operator confirms P1 delivery and supervised Phase 2 start |
| AUDIT IN PROGRESS → (unchanged) | Until final report accepted |

Update [project-site-registry.md](../../../project-site-registry.md) only when human operator approves status change.

---

## Related documents

- [RUN-5-SCOPE.md](RUN-5-SCOPE.md)  
- [RUN-5-FIRST-FINDINGS.md](RUN-5-FIRST-FINDINGS.md)  
- [RUN-5-DATA-REQUEST.md](../tasks/RUN-5-DATA-REQUEST.md)  
- [project-access-brief.md](../project-access-brief.md)

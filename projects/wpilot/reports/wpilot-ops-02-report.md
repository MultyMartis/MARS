# REPORT — WPilot OPS-02

**Task:** Release Candidate Preparation (`v0.3.0-RC1`)  
**Date:** 2026-06-19  
**Scope:** Documentation and audit only — no deploy, no ZIP build, no commit, no Sprint 3  
**Prior pass:** [wpilot-ops-01-report.md](wpilot-ops-01-report.md)  
**Checkpoint:** `8c67478` (`feat(wpilot): freeze v0.3.0 proven runtime`)

---

## 1. Release Baseline Decision

**Question:** What is release v0.3.0 — Variant A (checkpoint only) or Variant B (checkpoint + UX-01)?

### Recommendation: **Variant B**

| Variant | Files | Verdict |
|---------|-------|---------|
| A — `8c67478` only | 22 | Historical checkpoint artifact; valid for runtime reproduction, **not** RC1 baseline |
| **B — `8c67478` + UX-01** | **25** | **Official RC1 baseline** |

**Rationale:**

1. Runtime execution maturity (`proven_content_writes`) is proven at checkpoint `8c67478`.
2. UX-01 aligns operator admin surface with that maturity — without it, admin UI contradicts proven capabilities (read-only bridge drift).
3. Current `metacode-wpilot.php` **requires** `admin/class-wpilot-admin-ui-model.php` — deploying UX-01 bootstrap with old 22-file ZIP causes fatal error.
4. UX-01 adds `RUNTIME_MATURITY`, endpoint inventory panels, and i18n foundation — no REST/schema/auth changes.
5. Task context: UX-01 completed; ZIP stale vs working tree.

**Decision record:** [wpilot-ops-02-baseline-decision.md](wpilot-ops-02-baseline-decision.md)

---

## 2. Plugin Inventory

**Target:** `projects/wpilot/plugin/metacode-wpilot/`

**File count:** **25** — confirmed via glob scan (OPS-02).  
**Extraneous files:** **None** (no debug, secrets, evidence, `.bak`, `.tmp`).

### Canonical inventory by category

| Category | Count | Files |
|----------|-------|-------|
| **Core Runtime** | 9 | `metacode-wpilot.php`, `class-wpilot-plugin.php`, `class-wpilot-constants.php`, `class-wpilot-settings.php`, `class-wpilot-environment.php`, `class-wpilot-errors.php`, `class-wpilot-response.php`, `class-wpilot-request-context.php`, `class-wpilot-operation-id.php` |
| **Admin UI** | 2 | `admin/class-wpilot-admin-page.php`, `admin/class-wpilot-admin-ui-model.php` |
| **Localization** | 2 | `languages/metacode-wpilot.pot`, `languages/metacode-wpilot-ru_RU.po` |
| **Runtime Services** | 9 | `class-wpilot-audit-service.php`, `class-wpilot-auth.php`, `class-wpilot-backup-service.php`, `class-wpilot-checksum.php`, `class-wpilot-dry-run.php`, `class-wpilot-rollback-service.php`, `class-wpilot-scoped-replace-service.php`, `class-wpilot-site-reader.php`, `class-wpilot-wpbakery-detector.php` |
| **REST** | 1 | `class-wpilot-rest-controller.php` |
| **Schema** | 1 | `class-wpilot-schema.php` |
| **Operator doc** | 1 | `README.md` |

**Checkpoint delta:** +3 files vs `8c67478` (ui-model, `.pot`, `.po`); +4 modified files (bootstrap, admin-page, constants, plugin).

**Missing from tree:** `languages/metacode-wpilot-ru_RU.mo`

---

## 3. Localization Decision

### Files present

| File | Status |
|------|--------|
| `languages/metacode-wpilot.pot` | ✓ |
| `languages/metacode-wpilot-ru_RU.po` | ✓ (78 msgids) |
| `languages/metacode-wpilot-ru_RU.mo` | ✗ Absent |

### Textdomain alignment

| Source | Value | Match |
|--------|-------|-------|
| Plugin header `Text Domain` | `metacode-wpilot` | ✓ |
| `WPilot_Constants::TEXT_DOMAIN` | `metacode-wpilot` | ✓ |
| `Domain Path` | `/languages` | ✓ |
| `load_plugin_textdomain()` | Present (UX-01) | ✓ |

### How to obtain `.mo` (do not hand-author; do not use online converters)

**Option A — GNU gettext `msgfmt` (local toolchain):**

```bash
msgfmt -o languages/metacode-wpilot-ru_RU.mo languages/metacode-wpilot-ru_RU.po
```

Requires gettext tools installed on operator machine (`msgfmt` in PATH).

**Option B — WP-CLI (WordPress standard):**

```bash
wp i18n make-mo languages/
```

Requires WP-CLI installed; run from plugin directory or with `--path` to WordPress root.

**Option C — Poedit (desktop):** open `.po`, export/save `.mo` locally — not a third-party web service.

**Not acceptable per task:** manual binary editing, online PO→MO converter websites.

### Verdict: **Non-blocking Gap** (for RC Ready)

| Scope | Classification |
|-------|----------------|
| RC1 package readiness (`B — RC Ready`) | **Non-blocking** — English UI works; `.po` foundation complete |
| Full ru_RU localization proof | **Blocked** until `.mo` compiled and deployed |
| Clean install step 7 (ru_RU) | Cannot pass Russian runtime check without `.mo` |
| Plugin activation / REST / writes | **Not blocked** |

---

## 4. RC Document

**Created:** [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md](../WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md)

Captures: version, schema, checkpoint, Variant B baseline, categorized file inventory (25 files), runtime inventory, 12 endpoints, known limitations, not-yet-proven surface, ZIP rebuild specification.

---

## 5. ZIP Rebuild Impact

**Not built in OPS-02.** Specification only.

### Existing package

| Field | Value |
|-------|-------|
| Path | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0.zip` |
| Size | 36,556 bytes |
| Files | **22** (Variant A — checkpoint only) |
| Date | 2026-06-19 |

### Future RC1 ZIP vs existing ZIP

| Item | Old ZIP (22) | RC1 ZIP (25+) |
|------|--------------|---------------|
| `admin/class-wpilot-admin-ui-model.php` | ✗ | **✓ required** |
| `languages/metacode-wpilot.pot` | ✗ | **✓** |
| `languages/metacode-wpilot-ru_RU.po` | ✗ | **✓** |
| `languages/metacode-wpilot-ru_RU.mo` | ✗ | Optional until ru_RU proof |
| `metacode-wpilot.php` | Pre-UX-01 | UX-01 (requires ui-model) |
| `admin/class-wpilot-admin-page.php` | Pre-UX-01 | UX-01 panels |
| `includes/class-wpilot-constants.php` | No maturity constants | `RUNTIME_MATURITY`, counts |
| `includes/class-wpilot-plugin.php` | No textdomain | `load_plugin_textdomain()` |
| Runtime services / REST / schema | ✓ same | ✓ unchanged |

**Impact summary:** Future ZIP is **not interchangeable** with current ZIP. Mixing UX-01 bootstrap with old ZIP = **fatal**. Full rebuild required for any ZIP-based deploy of RC1.

---

## 6. Clean Install Plan

**Created:** [WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md](../WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md)

Procedure (not executed):

1. Disposable WordPress  
2. ZIP Install (RC1 package)  
3. Activate  
4. Verify Tables  
5. Verify REST  
6. Verify Dashboard (UX-01 panels)  
7. Verify Localization  
8. Verify Backup  
9. Verify Rollback  

Each step includes expected results and fail criteria.

**Complements:** [WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md](../WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md) (OPS-01 checklist form).

---

## 7. Release Status

### **B — RC Ready**

| Level | Assessment |
|-------|------------|
| A — Stay Internal | Superseded — RC specification now exists |
| **B — RC Ready** | **Selected** — baseline decided (Variant B); inventory verified; RC doc + clean install plan prepared; no new critical blockers |
| C — Clean Install Proven | Not met — test not executed |

**Rationale:**

- Runtime proven on DEV (FTP) — unchanged from OPS-01.
- RC1 specification complete with Variant B baseline.
- Plugin tree clean (25 files, no extras).
- Localization `.mo` = non-blocking gap for RC, documented with compile instructions.
- ZIP rebuild specified but not executed.
- Clean install test plan ready, not run.

**Before C:** build RC1 ZIP, optionally compile `.mo`, execute clean install test plan, commit UX-01.

---

## 8. Git Status

```
 M projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-page.php
 M projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-constants.php
 M projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-plugin.php
 M projects/wpilot/plugin/metacode-wpilot/metacode-wpilot.php
?? projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-ui-model.php
?? projects/wpilot/plugin/metacode-wpilot/languages/
?? projects/wpilot/reports/wpilot-ux-01-report.md
?? projects/wpilot/WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md
?? projects/wpilot/WPILOT-RELEASE-INVENTORY-v0.3.0.md
?? projects/wpilot/reports/wpilot-ops-01-report.md
?? projects/wpilot/reports/wpilot-ops-02-baseline-decision.md    (this OPS-02 pass)
?? projects/wpilot/WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md        (this OPS-02 pass)
?? projects/wpilot/WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md        (this OPS-02 pass)
?? projects/wpilot/reports/wpilot-ops-02-report.md             (this OPS-02 pass)
```

**HEAD:** `8c67478` — UX-01 plugin changes and all OPS-01/OPS-02 docs uncommitted.

**No commit performed.**

---

## 9. SAFE UNKNOWN

| Item | Detail |
|------|--------|
| **ZIP clean install** | RC1 ZIP not built; test plan not executed |
| **UX-01 commit hash** | Baseline references working tree; no tagged RC1 commit yet |
| **`msgfmt` / WP-CLI on operator machine** | Availability not verified in this pass |
| **Hosting constraints** | Beget upload limits, PHP version on hypothetical clean WP — not audited |
| **Plugin README step 5** | Still says "read-only bridge" — copy lag |
| **RC1 ZIP filename** | Operator to name final artifact (e.g. `metacode-wpilot-v0.3.0-RC1.zip`) |

---

## 10. SECURITY RISK

| Risk | Level | Notes |
|------|-------|-------|
| Secrets in plugin tree | **Low** | Scan clean — 25 files, no tokens/credentials |
| Secrets in existing deploy ZIP | **Low** | 22-file checkpoint ZIP — no secrets detected (OPS-01) |
| Token in git | **Low** | Hash-in-DB design only |
| ZIP stale vs UX-01 bootstrap | **Medium (operational)** | Fatal `require` if mixed deploy |
| Information disclosure (admin UI) | **Low** | REST route inventory intentional |
| Production misuse | **Medium (policy)** | DEV-only guards; clean install not proven |
| `.mo` compile supply chain | **Low** | Use local `msgfmt` or WP-CLI only |

No **SECURITY RISK** stop condition for internal RC preparation. Operational caution: **never deploy UX-01 bootstrap with 22-file ZIP**.

---

## Deliverables Summary

| Deliverable | Path | Status |
|-------------|------|--------|
| Baseline decision | `projects/wpilot/reports/wpilot-ops-02-baseline-decision.md` | Created |
| RC specification | `projects/wpilot/WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md` | Created |
| Clean install test plan | `projects/wpilot/WPILOT-CLEAN-INSTALL-TEST-PLAN-v1.md` | Created |
| OPS-02 report | `projects/wpilot/reports/wpilot-ops-02-report.md` | Created |

**Not performed:** deploy, ZIP build, `.mo` generation, clean install execution, commit, Sprint 3, new endpoints.

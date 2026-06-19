# WPilot OPS-02 — Release Baseline Decision

**Task:** OPS-02 Part 1 — Define Release Baseline  
**Date:** 2026-06-19  
**Decision status:** Recommended — pending operator commit/tag  
**No commit performed in this pass.**

---

## Question

What constitutes release **v0.3.0** for Release Candidate `v0.3.0-RC1`?

| Variant | Definition |
|---------|------------|
| **A** | Git checkpoint `8c67478` only — 22 plugin files |
| **B** | Checkpoint `8c67478` **+ UX-01** — 25 plugin files (working tree atop checkpoint) |

---

## Repository Evidence (2026-06-19)

| Signal | Variant A (`8c67478`) | Variant B (+ UX-01) |
|--------|----------------------|---------------------|
| Plugin file count | 22 | 25 |
| Runtime REST / schema / auth | Proven on DEV | Unchanged — admin/i18n only |
| `metacode-wpilot.php` requires `class-wpilot-admin-ui-model.php` | No | **Yes** — fatal if missing |
| `load_plugin_textdomain()` | Absent | Present |
| `WPilot_Constants::RUNTIME_MATURITY` | Absent | `proven_content_writes` |
| Admin UI reflects v0.3.0 proven runtime | **No** — read-only / dry-run drift | **Yes** |
| `languages/` | Absent | `.pot` + `ru_RU.po` |
| Existing deploy ZIP | Matches (22 files) | **Stale** — missing 3 UX-01 files |
| Git HEAD | `8c67478` | Working tree uncommitted atop `8c67478` |
| UX-01 report | N/A | [wpilot-ux-01-report.md](wpilot-ux-01-report.md) — completed |

---

## Runtime Maturity Alignment

**Runtime maturity level:** `proven_content_writes`

| Layer | Checkpoint `8c67478` | UX-01 |
|-------|---------------------|-------|
| Plugin REST write path | Proven | Not modified |
| DB schema `0.2.0` | Proven | Not modified |
| Operator admin surface | Misaligned copy (read-only bridge claims) | Aligned with proven capabilities register |
| Declared maturity in admin UI | Not surfaced | Surfaced via `RUNTIME_MATURITY` constant |
| i18n foundation | None | Textdomain bootstrap + `.pot` / `.po` |

**Conclusion:** Runtime **execution** maturity is established at checkpoint `8c67478`. **Operator-facing maturity representation** (admin dashboard, endpoint inventory, safety panels, localized strings) requires UX-01. Without UX-01, an operator installing v0.3.0 sees UI copy that contradicts documented proven runtime.

UX-01 is therefore **mandatory for Runtime Maturity compliance** at the **release/operator surface** — not because it changes REST behavior, but because it is the only in-tree artifact that correctly declares and displays `proven_content_writes` for v0.3.0.

---

## Decision

### **Recommend Variant B**

**Official release baseline for `v0.3.0-RC1`:**

```
8c67478 (feat(wpilot): freeze v0.3.0 proven runtime)
  + UX-01 working-tree changes (uncommitted at OPS-02 time)
```

**Canonical plugin tree:** `projects/wpilot/plugin/metacode-wpilot/` — **25 files**

### Rationale

1. UX-01 is completed and scoped to admin/i18n — no Sprint 3, no new endpoints.
2. Current bootstrap **cannot activate** without `admin/class-wpilot-admin-ui-model.php`.
3. RC document must describe operator surface consistent with [WPILOT-STATE-FREEZE-2026-06-19-v1.md](../WPILOT-STATE-FREEZE-2026-06-19-v1.md) and [WPILOT-PROVEN-CAPABILITIES-v1.md](../WPILOT-PROVEN-CAPABILITIES-v1.md).
4. Existing ZIP (`metacode-wpilot-v0.3.0.zip`) represents Variant A only — must be rebuilt for RC1.
5. Variant A remains valid as a **historical checkpoint artifact** but is **not** the recommended RC baseline.

### Variant A — when acceptable

Variant A is acceptable only for:

- Reproducing exact checkpoint `8c67478` behavior on DEV via FTP (legacy admin copy).
- Diffing runtime-only changes without UX-01 scope.

It is **not** acceptable as the RC1 package baseline.

---

## Required Follow-up (operator, not automated)

| Action | Owner |
|--------|-------|
| Commit UX-01 plugin changes atop `8c67478` | Operator |
| Tag or annotate `v0.3.0-RC1` baseline commit | Operator |
| Rebuild deploy ZIP from Variant B tree (+ `.mo` when ready) | Operator |
| Execute clean install test plan | Operator |

---

## Related Documents

| Document | Role |
|----------|------|
| [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md](../WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md) | RC specification (uses Variant B) |
| [wpilot-ops-02-report.md](wpilot-ops-02-report.md) | Full OPS-02 report |
| [wpilot-ux-01-report.md](wpilot-ux-01-report.md) | UX-01 change record |

---

## Document Status

| Field | Value |
|-------|-------|
| Implements runtime | No — decision record only |
| Committed to git | No — OPS-02 deliverable |

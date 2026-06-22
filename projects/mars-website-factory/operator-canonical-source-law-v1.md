# Website Factory Operator-Canonical Source Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**  
**Not:** runtime enforcement, git hook, or automated overwrite protection.

**Authority:** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) · [frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md)

---

## 1. Core law

```text
Manual operator changes inside the active src tree become canonical immediately.

Generated specifications, previous screenshots, measurements, token maps,
reports and earlier commits must not overwrite current operator-authored source.
```

**CURRENT SRC IS CANONICAL.** Operator manual changes override previous specifications, measurements, reviews, generated implementations, and checkpoints.

---

## 2. Required preflight (every frontend task)

Before any frontend edit:

1. Inspect `git status`.
2. Inspect current `src` files (read actual content — do not assume from specs).
3. Detect operator uncommitted or manual changes.
4. Mark them as **protected**.
5. Build on top of current `src`.
6. Never regenerate a block from an older specification without explicit operator approval.

**Fail state:** `OPERATOR SOURCE AUTHORITY GATE — FAIL` · `IMPLEMENTATION DENIED`

---

## 3. Prohibited actions (without explicit operator approval)

- wholesale file replacement;
- regeneration from spec;
- restoration from previous commit (`git reset`, `git restore .`, `git checkout -- .`, `git clean`, `git revert` on protected `src`);
- automatic formatting that changes design values;
- removal of manual classes because they are absent from old docs;
- replacement of direct values with old tokens;
- reintroduction of deleted tokens or old SCSS partial architecture;
- technical governance markers in production DOM (`data-safe-unknown`, etc.).

---

## 4. Report requirements (mandatory fields)

Every frontend report must include:

```text
Operator changes detected:
Operator changes protected:
Operator-authored files modified by agent:
Operator-authored design values changed:
Previous artefacts overridden by current src:
Canonical source status:
```

**Expected:** `Operator-authored design values changed: 0` unless operator-approved exception.

---

## 5. Pilot binding

**FP-0002 V6:** `active_src_authority: OPERATOR_CANONICAL` · `design_value_freeze: ACTIVE` (see [no-new-design-values-after-operator-calibration-law-v1.md](no-new-design-values-after-operator-calibration-law-v1.md)).

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — Operator-Canonical Source Law; FP-0002 V6 pilot authority |

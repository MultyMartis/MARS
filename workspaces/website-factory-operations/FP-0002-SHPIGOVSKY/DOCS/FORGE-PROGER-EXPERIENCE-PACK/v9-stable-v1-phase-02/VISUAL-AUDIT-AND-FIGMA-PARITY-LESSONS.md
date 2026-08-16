# Visual Audit and Figma Parity Lessons (Phase 02)

**Primary evidence:** E58 freeze + audit + FU01 decision pack; E60-FIX01; E62A/E62D 404 metrics; E63 viewport pack

---

## 1. E58 visual audit — what it was

E58 did **not** mean “make WordPress pixel-match Figma everywhere.”

Sequence:

1. Freeze current accepted baseline (backup + marker + Git persistence).
2. Run Figma/static vs runtime layout audit (**findings only**).
3. Produce operator decision pack (E58-FU01).
4. Implement **only** operator-confirmed items (E58-VA-001 → E59).

Excluded from forced correction at audit time: lifebuoy, heroes, main header, floating header, footer (operator-owned / in-motion surfaces).

Findings severity at audit: 0 CRITICAL / 1 HIGH / 4 MEDIUM / 3 LOW — then FU01 reclassified several MEDIUM/LOW as false positives.

---

## 2. Figma authority vs operator-accepted runtime

Figma is authoritative for:

- untouched / new surfaces without operator CSS canon;
- geometry metrics when operator requests Figma correction (404 PNG metrics).

Operator-accepted runtime is authoritative for:

- surfaces the operator has manually tuned;
- intentional deviations after visual review;
- post-freeze CSS edits until next promote.

**Conflict rule:** current explicit operator decision wins; then current accepted runtime; then approved Figma for new/untouched areas.

---

## 3. Hierarchy of visual authorities

| Priority | Authority | Use when |
|----------|-----------|----------|
| 1 | **Current explicit operator decision** | Spoken/written accept, reject, or named fix |
| 2 | **Current accepted runtime** | Live site after promote; hashes match what operator sees |
| 3 | **Approved Figma for untouched/new areas** | New page/component without operator CSS history |
| 4 | **Stable freeze** | Named rollback / style extraction (E58 for E60-FIX01 crumbs) |
| 5 | **Older static implementation** | Historical V9 static reference |
| 6 | **Inferred design rules** | Weakest — label SAFE UNKNOWN |

### Exceptions / conflict resolution

- If operator names a freeze as style authority for a selector family → that freeze outranks newer mistaken agent CSS for those selectors (E60-FIX01).
- If automated audit conflicts with class-matched remeasure → prefer remeasure + operator board (FU01 false positives).
- If Figma and accepted runtime differ on an excluded surface → **do not “fix”** without new charter.
- If only inferred tokens disagree → report SAFE UNKNOWN; do not mass-normalize H2 sizes (VA-004 lesson).

---

## 4. Exact geometry vs content-driven variation

| Exact geometry OK | Content-driven variation expected |
|-------------------|-----------------------------------|
| Button size, title font metrics on 404 | Card heights with different copy lengths |
| Breadcrumb font-size/line-height tokens | Blog card text wrapping |
| Decor asset pixel dimensions | Review teaser length before clamp |

Do not fail audits solely because content length differs from Figma lorem.

---

## 5. Why “matches stable backup” can still be visually wrong

- Backup may already contain an **unwanted** state if taken after the regression.
- Hash match on whole `v9-style.css` does not prove a **selector** is correct.
- Agent may restore E58 **typography** while leaving a bad **hover** rule — or claim typography restore when only hover mattered (E60 narrative trap).
- Operator may have accepted runtime **after** the backup timestamp.

Always extract the **specific selectors** under dispute and compare computed styles at target viewports.

---

## 6. Concrete FP-0002 examples

### Breadcrumbs (E60 → E60-FIX01)

- E60 applied `accent-hover` to crumb links under a global hover classification.
- Typography already matched E58 (14/18; blog ≤1024 8/12).
- FIX01 restored hover to E58 `var(--color-accent)` using E58 freeze `operator-edits/v9-style.css`.

### Reviews typography (E60-FIX01)

- Name used `<h2 class="review-archive-card__name">` → wrong cascade.
- Corrected to `<div class="review-archive-card__name">` with computed **18px / 24px**.

### 404 Figma measurement (E62A/E62D)

- Measure from operator design PNG pair; apply typography color/size and button geometry in `fp02-404.css`.
- PNG decor owns cutout radius; CSS should not fight the asset.

### Viewport evidence

- Prefer multi-viewport packs (1440/1024/480/370) for Stable claims (E62C/E63).
- Incomplete screenshot packs ⇒ PARTIAL, not silent PASS (E61 gap).

---

## 7. When not to “fix” operator CSS

- File hash shows RUNTIME_AHEAD and edits are outside wave scope.
- Surface listed as audit exclusion.
- Change would require global token normalize with high blast radius (global H2).
- Only evidence is brittle DOM-index pairing (FU01 false positives).

---

## 8. How to report SAFE UNKNOWN

Use when:

- markup skeleton differs but computed visual is unclear without operator eyes;
- metric delta exists but pairing is unreliable;
- authority conflict unresolved.

Template:

```text
SAFE UNKNOWN — <surface/selector>
Evidence: <paths>
Competing authorities: <list>
Blocked action: <what was not changed>
Operator question: <one concrete question>
```

---

## 9. Traceability

| Item | Path |
|------|------|
| Freeze marker | `REPORTS/FREEZE-FP-0002-V9-06E58-CURRENT-BASELINE-BEFORE-VISUAL-AUDIT-ACCEPTED.md` |
| Audit report | `REPORTS/REPORT-FP-0002-V9-06E58-figma-visual-layout-audit.md` |
| Decision pack | `REPORTS/REPORT-FP-0002-V9-06E58-FU01-visual-audit-operator-decision-pack.md` |
| Breadcrumb restore | `REPORTS/REPORT-FP-0002-V9-06E60-FIX01-breadcrumb-subnav-reviews.md` |

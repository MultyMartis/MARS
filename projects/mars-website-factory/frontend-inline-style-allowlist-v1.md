# MARS Website Factory — Frontend Inline Style Allowlist v1

**Status:** **documented** — human-operated allowlist for **Inline Style Compliance Audit** (Enforcement Pack EG-03).  
**Not:** automated HTML linter or CI enforcement.

**Purpose:** Define which inline `style=""` attributes are **ALLOWED**, which are **FORBIDDEN**, and when **WAIVED** applies.

**Authority:** [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) §3.3 · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.1.

**Default rule:** Inline styles are **FORBIDDEN** in Factory Gulp production paths unless listed below or **WAIVED** with Exception Registry record.

---

## 1. Disposition vocabulary

| Disposition | Meaning |
|-------------|---------|
| **ALLOWED** | Matches an allowlist entry — does not block gate |
| **FORBIDDEN** | Not allowlisted; no waiver — blocks **INLINE STYLE COMPLIANCE** |
| **WAIVED** | Not allowlisted; Lead exception with decision id + justification + authority citation |

---

## 2. Factory-wide ALLOWED entries

| ID | Pattern / context | Allowed properties | Notes |
|----|-------------------|-------------------|-------|
| **IS-01** | Third-party embed sandbox (explicit HITL) | Vendor-required only | Must cite vendor doc in REPORT; project Lead ack |
| **IS-02** | Email / CMS export snapshot (non-production path) | — | **N/A** for production PASS scope |
| **IS-03** | `display:none` on `<noscript>` fallback | `display` | Rare; document in REPORT if used |
| **IS-04** | Print-only hooks (`@media print` alternative unavailable) | Print-specific | Prefer SCSS print partial — inline is last resort |

**Not allowlisted by default:** `margin`, `padding`, `gap`, `width`, `height`, `color`, `font-size`, `line-height`, `grid-template-*`, flex sizing — use SCSS partials.

---

## 3. FORBIDDEN (always unless WAIVED)

| Class | Examples | Authority |
|-------|----------|-----------|
| Layout spacing | `style="margin:…"`, `style="padding:…"`, `style="gap:…"` | OL-01 · [frontend-production-rules-v0.md](frontend-production-rules-v0.md) §4 |
| Typography | `style="font-size:…"`, `style="line-height:…"` | OL-05 |
| Color / surface | `style="background:…"`, `style="color:…"` | Project SSOT tokens in SCSS |
| Grid/flex overrides | `style="grid-template-columns:…"` | OL-03 · OL-04 |
| Word-break hacks | `style="word-break:…"` | OL-06 |

---

## 4. Project extensions

Projects may append rows to a **project allowlist appendix** linked from Production Standards — each row requires:

- **decision id**
- **owner**
- **justification**
- **authority citation** (rank 1 SSOT clause)

Incomplete project rows → treat as **FORBIDDEN**.

---

## 5. Audit method

1. Build succeeds → inspect **`dist/**/*.html`**.
2. Grep / manual review: `style="` and `style='`.
3. For each hit: classify **ALLOWED** · **FORBIDDEN** · **WAIVED**.
4. Emit REPORT line: `INLINE STYLE COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN`.

---

## 6. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — Inline Style Allowlist for Enforcement Pack v1. |

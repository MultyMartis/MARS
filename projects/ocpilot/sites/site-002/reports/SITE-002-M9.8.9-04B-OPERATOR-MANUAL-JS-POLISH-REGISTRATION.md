# REPORT — M9.8.9-04B OPERATOR MANUAL JS POLISH REGISTRATION

**Project:** SITE-002 (ЗПМ / BZPM)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Environment:** TEST — https://zpm.new-site.space/  
**Date:** 2026-06-19  
**Mode:** Documentation-only knowledge registration — **no FTP, no deploy, no site changes**

---

## 1. Purpose

Register operator manual JavaScript refinements on live TEST that occurred **after** M9.8.9-04A (`FILTER SCROLL OFFSET TUNING`). Update Technical Knowledge Map and project index docs so agents and operators treat live manual JS as canonical.

---

## 2. Operator changes registered

### 2.1 Filter scroll offset

| Item | M9.8.9-04A (deploy pass) | Live canonical (operator manual) |
|------|--------------------------|----------------------------------|
| Function | `scrollToCategorySection()` | same |
| File | `assets/js/main.js` | same |
| Offset | `var offset = 15` | **`var offset = 0`** (or equivalent zero offset) |

**Canonical value:** **0** — filter/AJAX scroll lands with no extra top gap above `section.category`.

**Historical evidence:** [SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md](SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md)

### 2.2 Sticky header trigger

| Item | Value |
|------|-------|
| File | `assets/js/main.js` |
| Change | Operator manually adjusted sticky header show/hide threshold |
| Exact threshold | **SAFE UNKNOWN** — not captured in repo at registration time |
| Canonical | Live TEST sticky header behaviour on catalog/PLP |

---

## 3. Policy registered

| Rule | Detail |
|------|--------|
| **Manual JS refinements are canonical** | Operator edits on live TEST override M9.8.9-04A deploy snapshot and work copies |
| **Pre-task verification** | Before header/filter JS work: verify live `main.js`; do not trust pass reports alone |
| **Conflict resolution** | Live TEST wins over documentation and prior pass SHA |

---

## 4. Knowledge map update

**Section added:** **§10 Operator Manual JS Refinements** in [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)

Contents:

- Filter scroll offset = **0** (canonical)
- Sticky header trigger manually adjusted (**SAFE UNKNOWN** exact value)
- Manual JS refinements are canonical
- Pre-task rule for header/filter JS tasks

**§1 Authority Rules** updated to include JS in manual refinement policy.

**Renumbered:** former §10 Operational Rules → **§11**.

---

## 5. Updated files

| File | Change |
|------|--------|
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | **§10 Operator Manual JS Refinements**; §1 JS in canonical policy; §11 Operational Rules |
| `site-passport.md` | Link to §10 + 04B registration report |
| `README.md` | Link to operator manual JS refinements entry |
| `reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md` | **created** — this report |

---

## 6. SAFE UNKNOWN

| Item | What would verify |
|------|-------------------|
| Exact sticky header trigger threshold | Live FTP capture of `assets/js/main.js` + diff vs 04A post-deploy hash |
| Whether offset is literal `0` or `getPageScrollOffset()` restored | Live `main.js` line in `scrollToCategorySection()` |
| SHA-256 of live `main.js` after operator edits | FTP download + hash at next forensic pass |

---

## 7. Git

| Action | Value |
|--------|-------|
| Commit | **YES** — `site-002: register operator manual js refinements` |
| Push | **YES** |

---

**No site modifications. No FTP. No deploy.**

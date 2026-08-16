# Known Non-Blocking State — Sales Manager v2 Stable Baseline 2026-08-17

**STATUS:** PRODUCTION STABLE  
**Canonical baseline:** [PRODUCTION-STABLE-BASELINE-2026-08-17.md](PRODUCTION-STABLE-BASELINE-2026-08-17.md)

Record only real remaining items. Do not invent technical debt.

---

## 1. First natural Monday reminder observation

**Expected:** Enabled Mon–Fri 10:00 Europe/Moscow; weekday gate proven; reminder regression passing.

**At freeze time:** First natural Monday reminder after the weekday-gate change still required operator observation after natural **2026-08-17 10:00 Europe/Moscow** execution (MSK was still Sunday evening at freeze capture).

**Classification:** Expected pending observation — **not** a production defect and **not** a reason to mark the contour unstable.

**Label:** `STABLE_BASELINE_WITH_PENDING_NATURAL_REMINDER_OBSERVATION`

**Forbidden during freeze:** Manual reminder trigger.

---

## 2. Acceptance-only TMP callback filling (historical spam card)

During a previous acceptance test, re-delivery of an **already-spam** historical lead card required TMP callback filling because the production formatter appropriately omitted some state-changing callbacks for an already-spam entity.

**Classification:** Acceptance-only tooling behavior — **not** a production defect unless live normal production behavior for pending/real cards is broken (it is not, at freeze).

TMP/local acceptance tooling may remain under `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\` for forensics; it is **not** authoritative production runtime.

---

## 3. Explicit non-issues

- No invented technical debt backlog.
- No classification of pending natural Monday observation as instability.
- No requirement to keep experimental reconstruction (`RS_LABEL_DEFS`) paths — removed from production raw UX.

Gate: `SM_STABLE_KNOWN_STATE_DOCUMENTED`

# MARS Website Factory — Validation waiver semantics v0

**Status:** **documentation only** — **governed risk acceptance** for validation findings. **Not** policy engine enforcement.

**Version:** v0.

**Related:** [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [validation-escalation-model-v0.md](validation-escalation-model-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

---

## 1. Waiver authority

- Only **named roles** with explicit governance (per project / reference matrix) may authorize waivers.
- **Validator** documentation role **does not** silently waive HITL-class findings unless product policy explicitly delegates (default: **does not**).

---

## 2. Waiver types

| Type | Meaning |
|------|---------|
| **conditional waiver** | Unblock **only** if named conditions are met (deadline, follow-up validation, client sign-off). |
| **temporary waiver** | Time-bounded; must expire or renew; downstream stages must show **expired** handling. |
| **scoped waiver** | Applies to named artifact, page, finding ID, or severity band — not blanket “project waived.” |
| **expired waiver** | No longer authoritative; revalidation or new waiver required. |
| **revoked waiver** | Explicitly withdrawn — dependent outcomes return to **failed** / **blocked** unless fixed. |

---

## 3. Required waiver metadata (conceptual)

- **approver** identity (human)
- **scope** (what is waived)
- **reason** (business/legal/technical)
- **timestamp**
- **expiry** (if any)
- **paired findings** (which validation results are covered)

**SAFE UNKNOWN:** exact storage / ticketing fields.

---

## 4. Explicit prohibitions

| Forbidden | Consequence if claimed |
|-----------|------------------------|
| **Silent waiver** | Breaks audit trail — **disallowed** |
| **Automatic waiver** | No “bot waived” without human record — **disallowed** |
| **Implicit waiver inheritance** | Child artifact does **not** inherit parent waiver unless explicitly scoped and recorded — **disallowed** |

**SAFE UNKNOWN** must **never** be documented as equivalent to a waiver (per system signals dictionary).

---

*Last updated: 2026-05-12.*

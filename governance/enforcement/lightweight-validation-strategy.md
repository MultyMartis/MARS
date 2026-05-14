# Lightweight validation strategy (future-facing, human-primary)

**Status:** **documented** — **strategy only**. **No** scripts shipped by this document. **No** promise of tooling.

---

## Explicit non-goals

- **This is NOT autonomous governance** — humans remain accountable for merges and claims.
- **This is NOT a policy engine** — no repo-wide automated allow/deny of contributions.
- **This is NOT runtime enforcement** — nothing here executes inside MARS processes or intercepts tasks.

---

## What MAY later be semi-validated (optional, local)

If the team adds **opt-in** dev scripts or editor checks, candidates include:

| Signal | Example approach | Caveat |
|--------|------------------|--------|
| Broken **internal** markdown links | Link checker scoped to `governance/`, `interfaces/`, `README.md` | False positives on intentional anchors; external URLs flaky. |
| **Forbidden phrases** | Grep against a **small** list derived from [forbidden-runtime-claims.md](forbidden-runtime-claims.md) | Context-blind; **human** interprets. |
| Missing **Status:** line | Heuristic on new files under selected dirs | Does not judge correctness of status text. |
| **Stage mismatch** | Diff headline vs [../master-build-map.md](../master-build-map.md) table row for same stage | Tables are authoritative; script is advisory. |
| Missing **SAFE UNKNOWN** section | Detect absence of heading where template requires it | Cannot judge semantic completeness. |
| **Registry reference mismatch** | Compare cited `tool_id` / agent id to `agents/registry.md` / `tools/registry.md` | Does not know **external**-only tools unless labeled. |

All of the above, if ever built, should be **non-blocking** or **pre-push opt-in** unless the team explicitly decides otherwise.

---

## What should remain human-reviewed

- Whether prose **accurately** reflects evidence (three-way split).
- Security and **integration** risk wording.
- **Architecture** decisions and scope of **pilots**.
- **Lane** boundaries (production vs MARS core).
- **Lifecycle** and **audit** narrative coherence across multiple files.

---

## What must never be auto-assumed

- That **stated stage** implies **implemented** system.
- That **registry rows** imply **live permissions** or **runtime** support.
- That **contracts** imply **tests** or **deployment**.
- That absence of a keyword means the doc is **safe** (silence ≠ proof).

---

## Lightweight future checks (process)

- Pre-release **manual** pass using [governance-checks.md](governance-checks.md) IDs.
- New **high-risk** phrases added to [forbidden-runtime-claims.md](forbidden-runtime-claims.md) when drift patterns appear.

---

*Phase S1 — complements [README.md](README.md) enforcement folder purpose.*

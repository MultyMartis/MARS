# MARS — Reality audit framework

**Status:** **documented** — governance-only, **human-operated** review semantics. **Not** runtime code, **not** orchestration, **not** telemetry, **not** automated certification.

**Purpose:** Define what a **Reality Audit** is in MARS so future reviews stay anchored to **operational truth**, **usefulness**, and **human experience**—not to narrative drift or abstraction prestige.

---

## 1. What a Reality Audit is

A Reality Audit is a **deliberate**, **human-led** assessment pass that asks whether MARS documentation, helpers, and working habits still **match how work is actually done** and **still earn their maintenance cost**.

It evaluates:

- **Operational reality** — what people do, skip, work around, or overload on.
- **Usefulness** — what reduces ambiguity, risk, or rework vs what only decorates the repo.
- **Friction** — where semantics, volume, or ceremony slow safe execution (see [operational-friction-semantics.md](operational-friction-semantics.md)).
- **Drift** — where labels, maps, and stories diverge from evidence and lanes (aligns with S2 registry honesty, S3 survivability, S6/S7 operationalization posture).

---

## 2. What a Reality Audit is not

- **Not governance certification** — passing an audit does not “bless” the system; failing assumptions are acceptable outputs.
- **Not runtime validation** — absence of failing CI or absence of crashes does **not** imply operational maturity.
- **Not productization of review** — no dashboard, scoreboard, or automated audit engine is implied by this framework.
- **Not telemetry-driven** — evidence is **operational** (artifacts, commits, REPORTs, human testimony), not metrics pipelines.

---

## 3. Core vocabulary (audit lens)

| Term | Meaning |
|------|---------|
| **Operational evidence** | Observable traces humans can inspect without claiming instrumentation: completed REPORTs, migration packages, registry edits, lesson logs, reproduced workflows, explicit “we stopped using X” notes. **SAFE UNKNOWN** when evidence is missing. |
| **Human feedback** | Qualitative operator input: confusion, fatigue, workarounds, onboarding time, “we never open that file.” |
| **Helper usefulness** | Whether a script, checklist, formatter, or local validator **reduces** error or load vs adding noise (S5/S6 boundaries apply). |
| **Governance friction** | Cost imposed by docs/rules: duplication, unclear SoT, prestige language, ceremony without payoff (see [operational-friction-semantics.md](operational-friction-semantics.md)). |
| **Semantic breakdown** | Terms or diagrams that **no longer bind behavior**—people act one way while documents claim another. |
| **Stabilization signals** | Repeatable practice, clear ownership, reduced exception rate **as judged by humans**, willingness to index/narrow rather than expand. |
| **Deprecation signals** | Persistent non-use, harmful ambiguity, duplicate SoT, failed experiments that should not masquerade as patterns (see [deprecation-and-pruning-semantics.md](deprecation-and-pruning-semantics.md)). |

---

## 4. Relationships in the S0–S7 stack

- **S1 enforcement docs** — cue forbidden claims; audits ask whether those cues are **used** or ignored.
- **S2 registry / identity** — audits test whether registry presence is mistaken for runtime truth.
- **S3 survivability / entropy / onboarding** — audits prioritize overload and continuity honesty.
- **S4 execution contracts / validation chain** — audits ask whether REPORT and validation **language** matches actual gates.
- **S5 tooling boundaries** — audits judge helper value vs creep toward pseudo-platforms.
- **S6 operationalization** — audits check maturity labels vs evidence; interoperability claims vs exports.
- **S7 experiments** — audits separate **useful probes** from **historical noise** and mythology (see [reality-vs-mythology-warnings.md](reality-vs-mythology-warnings.md)).

---

## 5. Starting artifacts

- Question catalog: [reality-audit-questions.md](reality-audit-questions.md)
- Governance usefulness dimensions: [governance-usefulness-review.md](governance-usefulness-review.md)

---

## 6. SAFE UNKNOWN

Whether your team will schedule audits on a calendar cadence, tie them to releases, or run them ad hoc—**not** specified here. Whether quantitative rubrics will ever be adopted—**SAFE UNKNOWN**; this framework stays **qualitative and human-reviewed**.

# Reporting — Gulp Frontend Agent

Every material frontend prompt run ends with a **REPORT** whose title and sections satisfy this pack **and** align to [`../../projects/mars-website-factory/reporting-standard-v0.md`](../../projects/mars-website-factory/reporting-standard-v0.md) — especially **§4.2 Frontend implementation REPORT** (mandatory/forbidden there applies).

## Canonical header

```text
# REPORT — <task>
```

---

## Required sections (this pack)

| Section | Content |
|---------|---------|
| **Changed files** | Repo-relative paths modified (maps to factory **Updated files**). |
| **Created files** | New files under `src/…` or docs, with paths. |
| **Deleted files** | Any paths removed (or state *none*). |
| **Build result** | Command run + outcome, or **not run** with reason (**SAFE UNKNOWN** if scripts unverified). |
| **QA result** | Summary against [`qa-checklist.md`](qa-checklist.md); pass / fail / partial with evidence. |
| **Risks** | Open issues, HITL triggers, performance or a11y concerns. |
| **SAFE UNKNOWN** | Bounded unknowns per [`safe-unknown-prompt-rules-v0.md`](../../projects/mars-website-factory/safe-unknown-prompt-rules-v0.md). |
| **Git status** | Output of `git status --short` after the session’s edits. |
| **Next step** | What the operator or downstream role should do (e.g. QA lane, HITL, another section). |

---

## Factory alignment (also include when applicable)

Per **reporting-standard v0 §3**, add as applicable:

- **Artifact changes** — e.g. `frontend_handoff_id` anchor, blueprint/design ids touched conceptually.
- **QA changes** — QA artifacts produced/amended.
- **Runtime exclusions** — e.g. `mars-runtime/*`, paths intentionally not opened.
- **Push status** — `not requested` / `pushed to <remote>/<branch>` / `failed: <reason>`.
- **Verification results** — lint/build/viewport checks **actually performed**.

## Forbidden in REPORT

- Claiming **CI green** or **deploy** without evidence.
- Claiming **dist** was fixed by hand.
- **Fake QA pass** or **fake build success**.

---

*Documentation only — not an automated log format.*

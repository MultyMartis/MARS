# MARS Website Factory - Terminal Survivability Governance

**Status:** **documented** - Website Factory terminal survivability governance and human-supervised execution-environment methodology only.  
**Not:** runtime terminal framework, terminal automation engine, shell abstraction runtime, CLI orchestration platform, automatic encoding repair, universal shell compatibility layer, or guaranteed terminal integrity.

**Core principle:** frontend execution must preserve **terminal readability, console integrity, UTF-8 continuity, validation-command survivability, and execution-environment awareness** so that operators can trust what happened without pretending terminal output is an automated source of truth.

**Companion documents:** [shell-compatibility-model.md](shell-compatibility-model.md), [encoding-drift-taxonomy.md](encoding-drift-taxonomy.md).  
**Related layers:** [operational-workflow-governance.md](operational-workflow-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [failure-recovery-governance.md](failure-recovery-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [cognitive-load-governance.md](cognitive-load-governance.md).  
**Forge integration:** consolidated through [`../../agents/mars-forge/qa-checklist.md`](../../agents/mars-forge/qa-checklist.md), not a separate checklist file.

---

## 1. Positioning

Terminal Survivability Governance formalizes lessons from Triumph V3 / Forge execution where command syntax, shell environment, and live terminal encoding affected operational readability.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Human-supervised terminal readability, output readability, console integrity, shell-safe validation commands, and terminal readability continuity | Terminal runtime frameworks, shell abstraction engines, CLI orchestration, automatic terminal repair, or universal terminal behavior |
| Documentation-first handling of broken Unicode rendering, parser errors, command-portability limits, and display-level corruption | Claims that files were repaired, corrupted, or validated without file evidence |
| Forge reporting discipline for `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, and `ENCODING READABILITY FINDINGS` | Autonomous shell adaptation, automatic encoding detection, or guaranteed live-output fidelity |

The governance question is not "did the command eventually run?"  
The governance question is: **can the operator read, trust, and reconstruct terminal evidence without confusing display corruption, parser failure, and file corruption?**

---

## 2. Canonical Definition

**Terminal survivability** is the ability of a human-supervised execution session to preserve readable, reconstructable terminal evidence across shell syntax differences, live-output noise, encoding issues, and validation-command failures.

It protects:

- **Output readability** - terminal output remains legible enough to support validation and reporting.
- **UTF-8 continuity** - Unicode-heavy project docs and reports remain readable in terminal output where operationally relevant.
- **Console integrity** - terminal display, parser behavior, and command result are not conflated with file content.
- **Shell-safe execution** - commands are written for the active shell, especially PowerShell on Windows.
- **Command portability** - portability is explicit and checked, not assumed from bash habits.
- **Validation-command survivability** - validation commands should fail clearly, readably, and with actionable evidence.
- **Execution-environment awareness** - shell type, OS, encoding, path rules, and command separators are considered before command execution.
- **Agent terminal hygiene** - agents avoid noisy, ambiguous, shell-blind terminal use that erodes review confidence.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Terminal survivability** | Terminal evidence remains readable and reconstructable enough for human-supervised validation. |
| **Terminal readability continuity** | Terminal output preserves readability across command execution, live updates, errors, and reporting. |
| **Output readability** | Console output is legible, bounded, and useful for validation rather than noisy or corrupt. |
| **UTF-8 continuity** | Unicode text remains readable in terminal output, or display-level corruption is explicitly disclosed. |
| **Console integrity** | Operators distinguish terminal display state from actual file content and validation evidence. |
| **Shell-safe execution** | Commands use syntax, separators, quoting, and environment assumptions valid for the active shell. |
| **PowerShell compatibility** | Windows PowerShell command syntax and separators are used when the active shell is PowerShell. |
| **Command portability** | Commands identify portability limits instead of assuming bash, PowerShell, cmd, or POSIX equivalence. |
| **Validation-command survivability** | Validation commands remain readable and actionable even when they fail. |
| **Execution-environment awareness** | Shell type, OS, encoding, path format, and command semantics are considered before execution. |
| **Operational shell discipline** | Terminal commands are planned, scoped, readable, and shell-compatible enough to support governance evidence. |

---

## 4. Core Rules

- **PowerShell commands must use PowerShell-safe separators.** Do not assume `&&` works in a Windows PowerShell shell.
- **Avoid bash-only syntax in Windows shell.** Bash idioms require an actual bash environment or an explicit portability note.
- **Shell type must be considered before validation commands.** Validation evidence is weaker when the command cannot parse in the active shell.
- **UTF-8 readability matters operationally.** Broken live output can hide errors, warnings, or evidence boundaries.
- **Broken terminal output must not be ignored blindly.** Treat unreadable output as a terminal survivability finding or SAFE UNKNOWN until clarified.
- **Display corruption is not guaranteed file corruption.** Confirm file content separately before claiming docs/files were damaged.
- **Validation commands should prioritize survivability and readability.** Prefer commands that fail clearly and produce bounded, readable evidence.
- **Command portability should be explicit, not assumed.** State whether a command is PowerShell-specific, bash-specific, or intentionally portable.
- **Parser errors are validation failures.** A parser error means the command did not validate the intended thing.
- **Terminal hygiene is part of QA confidence.** Noisy, unreadable, shell-blind terminal behavior reduces confidence even if files remain intact.

---

## 5. Triumph V3 / Forge Lessons Captured

Triumph V3 / Forge execution exposed reusable Website Factory lessons:

- A command written with bash-style operators can fail under PowerShell with `ParserError` / `InvalidEndOfLine`.
- Parser failure is an execution-environment issue, not proof that project files were damaged.
- Live terminal output can show broken Unicode rendering while actual Markdown files remain intact.
- Display-level corruption and file-level corruption must be separated in reports.
- Shell compatibility is a **SAFE UNKNOWN** area unless the active shell, command syntax, and output readability are verified.
- Validation commands should be chosen for readability and shell compatibility, not only convenience.
- Terminal output that cannot be read cleanly should be treated as reduced evidence, not ignored.

These are Website Factory governance lessons, not Triumph-specific runtime behavior and not evidence of an automated shell layer.

---

## 6. Terminal Review Questions

Before treating terminal output as validation evidence, ask:

- What shell is active: PowerShell, bash, cmd, or another environment?
- Does the command use shell-specific separators, quoting, environment variables, globbing, or redirection?
- Did the command parse and run, or did it fail before the intended validation?
- Is the output readable enough to support the claim?
- Are Unicode characters rendered correctly where readability matters?
- Is any broken output display-level only, or is there file-content evidence of corruption?
- Would a future operator understand the command, result, and limitation?
- Should the result be reported as PASS, PARTIAL, FAIL, or SAFE UNKNOWN?

---

## 7. Anti-Patterns

Forbidden drift vocabulary:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Bash-on-PowerShell drift** | Bash separators or syntax are used in PowerShell, producing parser errors or misleading validation failure. |
| **Shell-assumption drift** | The operator assumes a shell model without checking the active execution environment. |
| **Shell-blind execution** | Commands are run without considering shell syntax, path format, quoting, or separator rules. |
| **Encoding corruption drift** | Broken live output is normalized until readability and evidence boundaries are lost. |
| **Unreadable terminal output** | Console output cannot support validation because characters, errors, or evidence are not legible. |
| **Parser-error survivability failure** | Parser errors are ignored or treated as if validation ran successfully. |
| **Terminal-noise collapse** | Excessive or corrupt output buries the signal needed for review. |
| **Console readability erosion** | Gradual output unreadability weakens confidence, handoff, and QA traceability. |
| **Environment-assumption drift** | OS, shell, encoding, and command behavior are treated as universal. |
| **Invisible execution failure** | A command fails in a way that is easy to miss because output is noisy, truncated, or unreadable. |
| **Validation-command incompatibility** | The validation command itself is incompatible with the active environment. |
| **Operational shell fragility** | Execution depends on fragile terminal assumptions rather than explicit shell discipline. |

Use [encoding-drift-taxonomy.md](encoding-drift-taxonomy.md) for encoding-specific drift classification.

---

## 8. Forge Integration

When Forge is selected, terminal survivability is a validation and report-confidence concern:

- Use [`qa-checklist.md`](../../agents/mars-forge/qa-checklist.md) to record consolidated `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, and `ENCODING READABILITY FINDINGS`.
- Keep terminal survivability findings separate from source fidelity, implementation reliability, QA confidence, workflow discipline, and failure recovery findings.
- Record shell type, command form, parser/readability outcome, and whether file-content verification was needed.
- Treat parser errors, unreadable output, and shell-incompatible validation commands as PARTIAL/FAIL evidence until rerun with shell-safe syntax.
- Escalate SAFE UNKNOWN when terminal output cannot prove whether validation actually ran or whether corruption is display-only.

This is human-supervised methodology. It does not create autonomous shell adaptation, automatic encoding repair, universal shell compatibility, or guaranteed terminal integrity.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Active shell is unclear | Cannot know which syntax and separators are valid. |
| Command used bash syntax in PowerShell | Cannot treat parser failure as validation evidence. |
| Terminal output is unreadable | Cannot safely interpret warnings, errors, or result boundaries. |
| Unicode rendering is broken | Cannot infer whether file content is corrupt without separate file inspection. |
| Validation command is shell-incompatible | Cannot claim the intended validation ran. |
| Live-output evidence is noisy or truncated | Cannot reconstruct the result reliably. |
| Command portability was assumed | Cannot know whether results transfer across Windows, PowerShell, bash, or CI contexts. |

**Action:** state the unknown, identify the needed rerun or file verification, and classify the command result as safe with disclosure, rerun required, HITL required, blocked, or monitored risk.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Terminal Survivability Governance layer - shell-safe execution, terminal readability, UTF-8 continuity, console integrity, validation-command survivability, PowerShell compatibility lessons, and Forge consolidated findings; documentation only. |

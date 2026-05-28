# MARS Website Factory - Shell Compatibility Model

**Status:** **documented** - shell compatibility model for human-supervised Website Factory validation and terminal execution only.  
**Not:** shell abstraction runtime, cross-shell execution engine, CLI orchestration layer, automatic command translator, or guarantee of universal shell compatibility.

**Parent governance:** [terminal-survivability-governance.md](terminal-survivability-governance.md).  
**Companion taxonomy:** [encoding-drift-taxonomy.md](encoding-drift-taxonomy.md).  
**Forge integration:** consolidated through [`../../agents/mars-forge/qa-checklist.md`](../../agents/mars-forge/qa-checklist.md).

---

## 1. Purpose

This model names the shell compatibility factors that must be considered before using terminal commands as validation evidence in Website Factory and Forge execution.

Shell compatibility matters because a command can be technically reasonable in one shell and fail before validation in another. In Windows execution contexts, PowerShell syntax must be treated as first-class rather than assuming bash semantics.

---

## 2. Compatibility Layers

| Layer | Review question |
|-------|-----------------|
| **Shell identity** | Is the active shell PowerShell, bash, cmd, or another environment? |
| **Separator semantics** | Are command separators valid for the active shell? |
| **Quoting and paths** | Are spaces, backslashes, quotes, and environment variables shell-safe? |
| **Encoding behavior** | Does the shell render UTF-8 output readably enough for the task? |
| **Validation semantics** | Did the command actually validate the intended thing, or only fail to parse? |
| **Portability declaration** | Is the command shell-specific or intentionally portable? |
| **Evidence readability** | Can a future operator reconstruct the result from terminal output? |

---

## 3. PowerShell Compatibility Rules

PowerShell-compatible execution should follow these rules when the active shell is PowerShell:

- Use PowerShell-safe sequencing instead of assuming bash `&&`.
- Prefer separate commands or PowerShell control flow when command success must gate the next command.
- Quote paths containing spaces, especially workspace paths such as `C:\AI MARS`.
- Treat parser errors such as `ParserError` / `InvalidEndOfLine` as command compatibility failures.
- Do not report validation PASS when the validation command failed before execution.
- Keep output bounded and readable enough to preserve terminal readability continuity.
- When using commands that are common across shells, still consider path, quoting, and encoding differences.

---

## 4. Shell-Safe Command Patterns

| Intent | Shell-safe governance guidance |
|--------|--------------------------------|
| Run one validation command | Prefer a single command whose output can be read clearly. |
| Run dependent validation commands | Use active-shell control flow or run commands separately with explicit result interpretation. |
| Check repository state | Use commands that do not require bash-only chaining in PowerShell. |
| Search references | Prefer tool-based search or shell-compatible search commands with clear quoting. |
| Inspect Markdown readability | Use file reads or shell-safe commands that preserve UTF-8 readability. |
| Report failures | Distinguish parser failure, command failure, validation failure, and unreadable output. |

This model does not prescribe a universal command library. It asks operators to make shell assumptions visible before relying on command output.

---

## 5. Command Portability

**Command portability** is explicit, not assumed.

| Portability state | Meaning |
|-------------------|---------|
| **PowerShell-specific** | Command is intended for PowerShell semantics and may not run in bash/cmd. |
| **Bash-specific** | Command uses POSIX/bash syntax and requires a bash environment. |
| **Likely portable** | Command appears common but still needs shell/path/encoding awareness. |
| **Unknown portability** | Shell behavior has not been verified; report as SAFE UNKNOWN if validation depends on it. |

Portable-looking commands can still fail because of separators, quoting, globbing, path spaces, encoding, or tool availability.

---

## 6. Validation-Command Survivability

A validation command is survivable when:

- it is valid in the active shell;
- it produces bounded, readable output;
- it distinguishes parser failure from validation failure;
- it leaves enough evidence for report reconstruction;
- it does not hide errors behind noisy or corrupt live output;
- it does not require undocumented shell assumptions.

A validation command is not survivable when it fails to parse, renders unreadably, depends on the wrong shell, or cannot be reconstructed by another operator.

---

## 7. Anti-Patterns

| Anti-pattern | Risk |
|--------------|------|
| **Bash-on-PowerShell drift** | Bash syntax such as `&&` is used where PowerShell cannot parse it. |
| **Shell-assumption drift** | Active shell is ignored because the command "usually works." |
| **Environment-assumption drift** | Windows, PowerShell, path spaces, and encoding are treated as incidental. |
| **Validation-command incompatibility** | The command fails before it can validate the intended target. |
| **Invisible execution failure** | Parser or command failure is buried in noisy output and later reported as validation. |
| **Operational shell fragility** | Execution quality depends on fragile shell habits rather than explicit command discipline. |

---

## 8. Reporting Guidance

When shell compatibility affects validation, report:

- active shell, if known;
- command or command class used;
- whether the command parsed and ran;
- whether output was readable;
- whether the validation claim is PASS, PARTIAL, FAIL, or SAFE UNKNOWN;
- whether a shell-safe rerun was required;
- whether file content was separately verified when terminal rendering was suspect.

Use `SHELL COMPATIBILITY FINDINGS` for shell syntax, separator, quoting, path, command portability, and parser-error issues.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Shell identity is not confirmed | Cannot know whether syntax is valid. |
| Command portability is untested | Cannot assume the same command works across environments. |
| Parser error occurred | Intended validation did not run. |
| Output readability is insufficient | Cannot reconstruct the result confidently. |
| Encoding state is unclear | Cannot distinguish display corruption from file corruption. |
| Tool availability differs by environment | Cannot assume validation can be repeated elsewhere. |

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Shell Compatibility Model - PowerShell compatibility, shell-safe execution, command portability, validation-command survivability, and reporting guidance; documentation only. |

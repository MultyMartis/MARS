# MARS Website Factory - Encoding Drift Taxonomy

**Status:** **documented** - taxonomy for human-supervised terminal encoding and readability drift classification.  
**Not:** automatic encoding detector, terminal repair engine, Unicode validator, runtime logging platform, or guarantee of UTF-8 rendering integrity.

**Parent governance:** [terminal-survivability-governance.md](terminal-survivability-governance.md).  
**Compatibility model:** [shell-compatibility-model.md](shell-compatibility-model.md).  
**Forge integration:** consolidated through [`../../agents/mars-forge/qa-checklist.md`](../../agents/mars-forge/qa-checklist.md).

---

## 1. Purpose

This taxonomy names encoding and terminal readability drift patterns that can appear during Website Factory / Forge execution.

Encoding drift is dangerous because unreadable terminal output can hide parser errors, validation failures, warnings, file-path issues, or evidence boundaries. It can also tempt operators to confuse display-level corruption with file-level corruption.

---

## 2. Taxonomy Summary

| Drift pattern | Primary risk |
|---------------|--------------|
| **Encoding corruption drift** | Broken Unicode rendering erodes evidence readability. |
| **Unreadable terminal output** | Output cannot support validation or handoff claims. |
| **Terminal-noise collapse** | Noise, corrupt characters, or excessive output bury the actionable signal. |
| **Console readability erosion** | Terminal output gradually becomes less useful for review. |
| **Display-file conflation** | Display corruption is mistaken for file corruption or file integrity. |
| **UTF-8 continuity loss** | Unicode-heavy documentation or reports stop rendering readably in terminal context. |
| **Invisible execution failure** | Parser/command failures are missed because output is unreadable or noisy. |
| **Validation evidence opacity** | The terminal output cannot prove what validation ran or failed. |

---

## 3. Encoding Corruption Drift

**Definition:** Terminal output renders text as broken characters, mojibake, or unreadable glyphs while the actual file state remains unverified.

Signals:

- Cyrillic, symbols, or Markdown punctuation render as corrupted characters;
- error output is partially unreadable;
- report content displayed in the terminal cannot be trusted as-is;
- operators infer file corruption from terminal display alone.

Impact:

- weakens evidence readability;
- hides warnings and errors;
- can create false file-corruption claims.

Mitigation:

- verify file content with direct file reads when needed;
- report display-level corruption separately from file content;
- rerun essential validation with readable output if possible.

---

## 4. Unreadable Terminal Output

**Definition:** Output is too corrupt, dense, truncated, or noisy to support the validation claim.

Signals:

- PASS/FAIL evidence cannot be located;
- warnings/errors are visually buried;
- output has mixed encodings or broken lines;
- a future operator could not reconstruct the result.

Impact:

- reduces QA confidence;
- damages handoff and report integrity;
- increases risk of invisible execution failure.

Mitigation:

- reduce command output scope;
- prefer bounded validation commands;
- classify the result as PARTIAL or SAFE UNKNOWN until readable evidence exists.

---

## 5. Terminal-Noise Collapse

**Definition:** Terminal output contains enough unrelated noise, repeated errors, corrupt rendering, or excessive live logs that the useful signal collapses.

Signals:

- the validation result is surrounded by unrelated logs;
- parser errors scroll past without clear handling;
- long command output is used where a focused check would work;
- operators stop reading terminal output carefully.

Impact:

- hides failures;
- weakens report evidence;
- raises cognitive load and review fatigue.

Mitigation:

- run focused commands;
- summarize only verified outcomes;
- link terminal-noise risk to cognitive-load and QA-confidence findings when material.

---

## 6. Display-File Conflation

**Definition:** Operators treat display corruption as proof of file corruption, or treat readable display as proof that file content is intact.

Signals:

- "terminal showed mojibake" becomes "docs are corrupted" without file inspection;
- readable output is treated as full file validation;
- file-content verification is skipped after display issues.

Impact:

- creates false recovery work;
- can hide actual corruption or falsely claim damage;
- weakens operational honesty.

Mitigation:

- separate terminal rendering evidence from file content evidence;
- inspect actual files before claiming corruption or integrity;
- record `ENCODING READABILITY FINDINGS` when display/file distinction matters.

---

## 7. UTF-8 Continuity Loss

**Definition:** UTF-8 readability does not survive terminal display, especially for multilingual docs, symbols, or report text.

Signals:

- Cyrillic and special symbols render incorrectly;
- Markdown headings or bullets become difficult to read;
- live terminal output cannot preserve report readability.

Impact:

- reduces operator confidence;
- creates documentation review friction;
- may hide command results inside broken text.

Mitigation:

- avoid relying solely on live terminal display for multilingual file integrity;
- use direct file reads for document verification;
- keep terminal output concise and readable.

---

## 8. Invisible Execution Failure

**Definition:** The command failed or did not validate the intended target, but output readability problems make that failure easy to miss.

Signals:

- parser errors appear before intended command output;
- command separators are incompatible with the active shell;
- output corruption obscures error text;
- report claims validation without confirming the command ran.

Impact:

- creates false PASS or false confidence;
- weakens validation-command survivability;
- can propagate shell-assumption drift.

Mitigation:

- confirm command parsed and ran;
- rerun with shell-safe syntax;
- classify parser or readability failure as `SHELL COMPATIBILITY FINDINGS` or `ENCODING READABILITY FINDINGS`.

---

## 9. Reporting Use

When encoding drift appears, record:

- drift pattern name;
- affected command or output class;
- whether the issue is display-level, file-level, or SAFE UNKNOWN;
- validation impact: PASS, PARTIAL, FAIL, SAFE UNKNOWN;
- rerun or file verification needed;
- relationship to shell compatibility, QA confidence, workflow discipline, or failure recovery.

Use `ENCODING READABILITY FINDINGS` for UTF-8 continuity, unreadable terminal output, console readability erosion, terminal-noise collapse, and display/file conflation.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Terminal rendering is corrupt | Cannot infer file content from display alone. |
| Output is unreadable | Cannot prove command outcome reliably. |
| Parser errors are obscured | Cannot know whether validation ran. |
| Unicode output is required for review | Cannot confirm readability continuity without a readable view. |
| File content was not inspected | Cannot claim display corruption did or did not affect files. |
| Live output was truncated or noisy | Cannot reconstruct evidence boundaries. |

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial Encoding Drift Taxonomy - encoding corruption drift, unreadable terminal output, terminal-noise collapse, console readability erosion, display-file conflation, UTF-8 continuity loss, and invisible execution failure; documentation only. |

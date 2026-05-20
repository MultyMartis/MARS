# Cleanup Abort Conditions v1

## Status

Abort conditions for future cleanup only. No cleanup was executed.

## Abort Cleanup If

### Hidden Dependencies Found

Stop if:

- any non-consolidation ORCA doc directly references a target template or checklist;
- any workflow, README, or operator entrypoint points to a specific old template;
- human operator usage depends on the original filenames.

### Operator Confusion Risk Increases

Stop if:

- the consolidated template does not clearly replace the old files;
- operators cannot identify the right template;
- redirect or archive policy is unclear;
- old and new templates compete.

### Escalation Logic Degrades

Stop if:

- escalation triggers become less visible;
- recommended human owner field is removed;
- high-impact incomplete evidence no longer escalates;
- operator authority limits disappear.

### SAFE UNKNOWN Degrades

Stop if:

- SAFE UNKNOWN is removed as a required field;
- uncertainty is reframed as failure;
- missing evidence is hidden to make the review look complete;
- weak evidence can appear stronger after merge.

### Merged Template Complexity Increases

Stop if:

- the merged template is longer than practical use requires;
- optional tradeoff fields dominate the core review;
- low-risk reviews require too many fields;
- the template becomes another methodology layer.

### Readability Decreases

Stop if:

- the operator cannot complete the template quickly;
- section names become abstract;
- repeated boundary text overwhelms the review fields;
- the structure hides action, defer, stop, or escalate.

## Reversibility Requirements

Before execution:

- keep originals untouched;
- use archive-only before deletion;
- document source-to-target mapping;
- preserve direct links if redirect READMEs are used;
- run `git status --short -uall` before and after cleanup;
- do not continue if rollback path is unclear.

## Safety Priority

Cleanup safety matters more than cleanup speed. Preserving operator usability matters most. Low-evidence and escalation logic are safety-critical.

## Boundary

These abort conditions block cleanup. They do not authorize cleanup.

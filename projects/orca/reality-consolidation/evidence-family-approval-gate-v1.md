# Evidence Family Approval Gate v1

## Status

Human approval gate for future cleanup. Planning only.

## Required Approval Questions

### Target Structure

- Is `projects/orca/evidence-core/` approved as the future consolidated target folder?
- Should the target folder name be `evidence-core/`, `evidence-and-reality/`, or something else?
- Is the proposed six-file target set approved?
- Should `operator-decision-rules-v1.md` remain inside evidence core, or stay in a separate operator-facing folder?

### Old Folder Policy

- Should old folders remain with redirect READMEs?
- Should `projects/orca/evidence/` remain as the canonical source instead of creating `evidence-core/`?
- Should `projects/orca/confidence/`, `projects/orca/contradictions/`, and `projects/orca/operator-decisions/` remain visible for backward navigation?
- Should redirects be short and practical, or include migration notes?

### Preservation Policy

- Should any original docs be preserved unchanged?
- Are any source files actively referenced by other ORCA docs or operator habits?
- Should `contradiction-tracking-model-v1.md` remain standalone because it is safety-critical?
- Should `operator-decisions/escalation-rules-v1.md` remain standalone because it is operator-critical?
- Should `confidence/pattern-reliability-scoring-v1.md` be preserved despite false-precision risk?

### Archive Versus Delete

- Should cleanup be archive-only instead of delete?
- If archive-only, where should archived docs live?
- Should archive files keep original paths, or move under a future archive folder?
- Should archived docs receive a header explaining replacement files?
- Should anything be deleted at all in the first cleanup pass?

### Commit And Review Safety

- Should this be committed before cleanup?
- Should cleanup be split into separate commits by phase?
- Should the first execution pass touch only templates/checklists?
- Should a diff review be required after each cleanup phase?
- Should `git status --short -uall` be required before and after each phase?

### Operator Usability

- Who is the intended operator-facing entrypoint after cleanup?
- What is the shortest path for a PPC operator to record evidence and make a decision?
- What fields are mandatory in the future evidence review template?
- What fields are optional appendix detail?
- What would make the consolidated structure too theoretical?

### Safety Rules

- Which evidence fields must never be removed?
- Which contradiction states must survive?
- Should evidence strength and confidence become one practical scale?
- What is the approved SAFE UNKNOWN definition?
- What escalation rules must remain visible?

## Approval Needed Before Any Execution

Cleanup must not start until the operator answers:

1. Is the target folder approved?
2. Is archive-only required?
3. Which original files must remain unchanged?
4. Which files are allowed to become redirect READMEs?
5. Is a commit required before cleanup?

## Default Safe Position

If any answer is unknown:

- do not delete;
- do not archive;
- do not move;
- do not rewrite source docs;
- preserve all original files;
- create only planning documents.

## Boundary

This approval gate does not perform cleanup. It blocks cleanup until explicit human decisions are recorded.

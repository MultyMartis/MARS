# Execution Guard Checklist v1

**Status:** `MINIMAL_V1`
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

Use before and during scoped MARS agent tasks.

Automatic interception is not implemented.

Validator is human-invoked unless proven otherwise.

## Path Preflight

- [ ] Full target path is resolved.
- [ ] Target path is inside approved scope.
- [ ] No `..` escape is present.
- [ ] No UNC path is used unless explicitly authorized.
- [ ] No symlink, junction, or reparse escape is followed.
- [ ] Deprecated roots are not used as operational targets.

## Volume Identity

- [ ] `Get-Location` returns `X:\AI MARS` for repo tasks.
- [ ] `Get-Volume -DriveLetter X` returns label `AI WS`.
- [ ] Mismatch causes `STOP — X VOLUME IDENTITY OR WORKSPACE MISMATCH`.

## Scope Lock

- [ ] Task id is present.
- [ ] Approved write paths are explicit.
- [ ] Out-of-scope paths are explicit.
- [ ] Protected zones are listed.
- [ ] Empty scope lock is treated as invalid.

## Protected Zones

- [ ] `governance/` not edited unless explicitly scoped.
- [ ] `registry/` not edited unless explicitly scoped.
- [ ] `AGENTS.md` and `.cursorrules` not edited unless explicitly scoped.
- [ ] `web-gpt-sources/` not edited unless explicitly scoped.
- [ ] `projects/mars-survivability/`, `projects/mars-website-factory/`, and `projects/mars-search-ppc-production/` not edited unless explicitly scoped.
- [ ] `workspaces/` not edited unless one exact workspace is scoped.

## Git Safety

- [ ] `git status --short` read before mutation.
- [ ] Foreign WIP identified and preserved.
- [ ] No `git add .`.
- [ ] No `git add -A`.
- [ ] No `git commit -a`.
- [ ] No `git stash`.
- [ ] No `git reset`.
- [ ] No `git restore`.
- [ ] No `git clean`.
- [ ] No staging, commit, or push unless explicitly requested.

## Filesystem Safety

- [ ] Writes only inside approved `X:\` root.
- [ ] No root-level operation on `X:\`.
- [ ] No delete/replace/cleanup of `X:\AI MARS\`, `X:\AI MARS STORAGE\`, or `X:\MARS-Localhost\`.
- [ ] No manual edit of generated/build output unless task explicitly authorizes source/regen path.
- [ ] No unrelated file edits.

## Destructive Operation Boundary

Destructive operations require separate charter.

Before any destructive operation, require:

- [ ] exact path list;
- [ ] dry-run or preview;
- [ ] checkpoint / backup;
- [ ] explicit operator approval;
- [ ] rollback method;
- [ ] audit evidence.

If any item is missing, stop with `NEED HUMAN APPROVAL` or `SECURITY RISK`.

## External System Boundary

- [ ] External systems are named.
- [ ] External mutation is authorized or explicitly out of scope.
- [ ] Credentials boundary is defined if relevant.
- [ ] Remote operations require separate ROL charter.
- [ ] No remote operation is inferred from local documentation.

## Checkpoint / Rollback

- [ ] Checkpoint requirement matches risk class.
- [ ] Cache is not treated as checkpoint.
- [ ] REPORT is not treated as persistence.
- [ ] Rollback path is documented for medium/high risk work.

## Approval

- [ ] Operator approval required status is explicit.
- [ ] Approval is exact, scoped, and dated when needed.
- [ ] Visual/product approval is not inferred from build or technical PASS.

## Evidence

- [ ] File paths listed.
- [ ] Commands listed.
- [ ] Validation output or receipt recorded.
- [ ] Screenshots/checksums included when task requires them.
- [ ] SAFE_UNKNOWN entries are bounded and resolvable.

## Halt Conditions

Stop when:

- workspace or volume identity fails;
- scope is ambiguous;
- protected-zone mutation is requested without charter;
- destructive operation lacks required boundary;
- remote operation lacks separate ROL charter;
- validation evidence is missing for a PASS claim;
- foreign WIP would be touched;
- implementation/runtime claim is not supported by source evidence.

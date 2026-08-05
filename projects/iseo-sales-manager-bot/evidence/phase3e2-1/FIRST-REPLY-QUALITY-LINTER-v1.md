# FIRST REPLY QUALITY LINTER v1 (evidence)

Deterministic checks before marking draft ready:

- forbidden system phrases absent
- known website / contacts not re-requested
- explicitly absent site not requested
- customer name safely used / fallback
- no unsupported promise
- ≤3 question groups
- length limit
- no duplicated sentence / warning
- concrete comment acknowledged when theme supported
- generic template not used for recognized meaningful theme
- HTML escaped
- no internal marker in customer draft
- closing present

On failure: `first_reply_ready=false` or safe fallback; do not publish broken copy block.

Architecture: [../../architecture/FIRST-REPLY-QUALITY-LINTER-v1.md](../../architecture/FIRST-REPLY-QUALITY-LINTER-v1.md)  
Harness H40 PASS.

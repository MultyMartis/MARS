# Remote Preflight Checklist v1

**Status:** `MINIMAL_CHARTER`
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

Use before any remote-facing task. Automatic interception is not implemented. Validator is human-invoked.

## Preflight Checks

- [ ] Target identity known (system name, platform, URL/host label without secrets)
- [ ] Environment known (`prod` / `dev` / `stage`; not `unknown` if mutation is requested)
- [ ] Scope exact (allowed paths/objects listed; no unbounded scope)
- [ ] Credentials not pasted into chat (operator-managed only; ROL is not a credential vault)
- [ ] Backup / rollback exists (required for any write or destructive class)
- [ ] Production status known (live production vs non-production is explicit)
- [ ] Action class known (not `UNKNOWN` if mutation is requested)
- [ ] Operator approval present (for any remote mutation)
- [ ] Remote mutation allowed (all charter conditions satisfied)
- [ ] Stop conditions checked

## Blocking Outcomes

Stop and do **not** mutate when any of the following is true:

- target identity incomplete;
- environment is `unknown` and mutation is requested;
- action class is `UNKNOWN` and mutation is requested;
- credentials are requested into chat or agent context;
- backup/rollback is missing for write/destructive classes;
- production status is unknown for a live surface;
- operator approval is missing for mutation;
- remote mutation is not allowed by charter;
- stop conditions are unmet.

Stop outputs: `SAFE UNKNOWN`, `NEED HUMAN APPROVAL`, or `SECURITY RISK`.

## Read-Only Note

`READ_ONLY` still requires:

- target identity known;
- credentials not pasted into chat;
- operator approval when the programme or task requires it;
- stop conditions checked.

`READ_ONLY` must not silently escalate into writes.

## After Preflight

If all mutation-relevant checks pass:

1. Use `templates/remote-task-starter-v1.md`.
2. Follow `contracts/remote-operations-charter-v1.md`.
3. Close with `gates/remote-report-gate-v1.md`.

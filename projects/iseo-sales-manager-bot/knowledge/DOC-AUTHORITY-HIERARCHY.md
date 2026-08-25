# Documentation Authority Hierarchy

Use this hierarchy when documents conflict.

## 1. README / Project Entry

The project README or top-level index orients readers. It is not allowed to override the stable baseline when older wording conflicts.

## 2. FINAL-HANDOFF

[FINAL-HANDOFF.md](../FINAL-HANDOFF.md) is the fast recovery index for a lost chat/context. It points to authority; it does not replace authority.

## 3. Canonical Stable Docs

Highest project truth for current production:

- [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)
- [PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md](../baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md)
- [PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md](../baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md)
- [CURRENT-PRODUCTION-ARCHITECTURE.md](../architecture/CURRENT-PRODUCTION-ARCHITECTURE.md)

## 4. Current Contracts

Current architecture contracts explain the baseline in operational detail:

- data/state;
- lifecycle;
- Gmail intake;
- Telegram;
- reminders;
- Admin;
- Sheets dependencies.

## 5. Runbooks And Recovery

Runbooks and recovery docs guide operators. If a runbook conflicts with a stable baseline, follow the baseline and update the runbook.

## 6. Checklists

Checklists are execution aids. They are not proof by themselves. A checked item needs corresponding evidence.

## 7. Reports And Evidence

Reports and evidence support decisions. Later reports do not automatically supersede stable docs unless they explicitly declare a new accepted baseline or operator-approved phase.

## 8. Historical Phase Docs

Phase 2/early Phase 3 architecture documents are historical where conflicting. Files with production supersession banners should be read as design context only.

## Conflict Rule

When in doubt, use this order:

```text
stable baseline -> current architecture contracts -> runbooks/recovery -> reports/evidence -> historical design docs
```

If no repository evidence proves a runtime fact, write SAFE UNKNOWN.


# Generated artifact MANUAL_STABLE policy v1

**Locus:** Search PPC shared documentation  
**Implementation:** `tools/commander-transport/src/manual-stable-guard.mjs`

## States

| State | Meaning | Generator behavior |
|-------|---------|-------------------|
| `GENERATED` | Fresh generator output | May overwrite with same version policy |
| `MANUALLY_EDITED` | Operator changed content | Warn; hash compare before overwrite |
| `MANUAL_STABLE` | Operator-declared stable | **Refuse overwrite** |
| `SUPERSEDED` | Replaced by newer version | Read-only archive |
| `ARCHIVED` | Historical evidence | Read-only |

## MANUAL_STABLE rules

1. Generator must not overwrite the file.
2. Generator must compare current hash with recorded hash.
3. Generator must stop if overwrite would occur.
4. New version requires **new filename** (e.g. `-v2`) or explicit operator authorization.
5. Status must appear in project artifact index.
6. Manual edits must not be silently normalized away.

## Corvonero registration

See `pilots/corvonero/CORVONERO-MANUAL-STABLE-ARTIFACTS-v1.json`:

- `02-CORVONERO-CAMPAIGN-STRATEGY-AND-RESEARCH-v1.html` — MANUAL_STABLE

## API

```javascript
import { checkManualStableOverwrite, ARTIFACT_EDIT_STATES } from './manual-stable-guard.mjs';

const result = checkManualStableOverwrite(entry, { intent: 'overwrite' });
if (!result.allowed) { /* stop generation */ }
```

## Cross-references

- `SEARCH-PPC-CLIENT-APPROVAL-WORKFLOW-v1.md`
- `SEARCH-PPC-PROJECT-CLOSURE-CHECKLIST-v1.md`
- Artifact locator contract (`artifact-locator.mjs`)

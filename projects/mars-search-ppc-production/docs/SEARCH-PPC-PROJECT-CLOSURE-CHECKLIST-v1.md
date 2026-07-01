# Search PPC project closure checklist v1

Reusable checklist for pilot post-project closure (human-operated).

## 1. Preflight

- [ ] Confirm X: / AI WS / canonical branch / HEAD
- [ ] Inventory Corvonero vs unrelated WIP
- [ ] No destructive git/filesystem ops

## 2. Verified backup

- [ ] Timestamped immutable backup under `AI MARS STORAGE/backups/search-ppc/`
- [ ] Repository + Storage archives
- [ ] Git evidence + manifest + SHA256
- [ ] `BACKUP_VERIFIED: true`

## 3. Project freeze

- [ ] Current artifact index (JSON + MD)
- [ ] Client feedback state
- [ ] Manual-stable registry
- [ ] Historical packages marked DO NOT IMPORT

## 4. Knowledge capture

- [ ] Problem register (35+ incidents)
- [ ] Lessons learned (grounded in evidence)
- [ ] Cleanup candidate inventory (plan only)

## 5. Shared hardening

- [ ] Regression tests for confirmed failure modes
- [ ] Documentation cross-linked to release gate

## 6. Explicit exclusions

- [ ] No import / launch / authority regen / client file rewrite
- [ ] No cleanup execution without operator approval
- [ ] No git commit unless separately chartered

## Reference implementation

Corvonero: `pilots/corvonero/CORVONERO-POST-PROJECT-CLOSURE-CHECKLIST-v1.md`

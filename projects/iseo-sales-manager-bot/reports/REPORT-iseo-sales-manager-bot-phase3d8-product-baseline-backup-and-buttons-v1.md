# REPORT — ISEO SALES MANAGER BOT PHASE 3D.8 PRODUCT BASELINE, RECOVERY BACKUP, AND ACTION-BUTTON RESTORATION

## 1. Verdict

**COMPLETE — BASELINE AND BACKUP READY; LIVE BUTTON CONFIRMATION PENDING**

Product baseline documented, recovery backup verified on Storage, button defect repaired and API-proven on two recipients. Operator visual confirmation on both Telegram clients remains recommended (harness multi-copy edit saw 1 copy).

## 2. Operator-approved scope

Phase 3D.8 product baseline + recovery backup + action-button restoration. No parser redesign, no AI ON, no Sales-Manager-v2 activation, no new workflows, no restore of revoked moderators, no automatic client messages.

## 3. Environment

- Repo root: `X:\AI MARS` (volume `AI WS`)
- Clean worktree: `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3d8-20260805-032341\repo`
- n8n host: `n8n.ai-metacode.com`
- Backup root: `X:\AI MARS STORAGE\backups\iseo-sales-manager-bot\2026-08-05-phase3d8-baseline\`

## 4. Git preflight

- Main workspace branch `mars/canonical-post-recovery` but **diverged** from origin with foreign WIP + staged client-ops files
- Origin tip at start: `6351ce6c`
- Ancestry OK for `6351ce6c`, `ce06f240`, `e78303e2` on origin
- Commits performed only via clean worktree

## 5. Git tails

Historical iseo-sm worktrees/branches retained (not deleted). `phase3d71` already at canonical `6351ce6c`. Dirty main untouched. Details: `evidence/phase3d8/GIT-TAIL-CLOSEOUT-v1.md`.

## 6. Canonical baseline

Integration base: `origin/mars/canonical-post-recovery` @ `6351ce6c` (+ this phase commit after push).

## 7. Current access state

Observed from Admin executions (no raw IDs):

| Role | Status | Count |
|------|--------|------:|
| admin | active | 1 |
| moderator | active | 1 |
| moderator | revoked | 2 |

Matches operator intent. Olya/Nikita not restored.

## 8. Workflow baseline

| Workflow | ID | Active | Nodes |
|----------|----|--------|------:|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 |
| Admin.dev | wLrLp4WQHm1VJmxz | true | 57 |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | 19 |

CONFIG: production, AI OFF, parser `sm-parser-v3.2`, message `sm-msg-v2.2`.

## 9. Product documentation

Created `product/` layer: overview, current baseline, architecture, reusable deployment model, versioning/rollout, roadmap, known limitations, glossary, reminder draft. Linked from README / OPERATIONAL-INDEX.

## 10. Reusable deployment model

Documented target: shared core + per-client bot/secrets/sources/storage/staff + staged rollout/rollback/fleet visibility. Explicitly marked current vs target vs not-yet-implemented.

## 11. Versioning and rollout

Documented product/workflow/parser/message/storage/deployment versions and channels: development → harness → reference i-SEO → acceptance → pilots → wider → health → stop/rollback.

## 12. Recovery backup

Storage package created with private + sanitized contours, manifests, sheet tab structure, forensic, git baseline notes, RECOVERY-README, SHA256SUMS. Not committed to Git.

## 13. Backup verification

Checksum file generated; sanitized snapshots derived from post-repair raw exports; private raw retained only under Storage backup.

## 14. Button defect

Original live cards missing action buttons; archive `/leads` excluded.

## 15. Button payload forensic

Trace through Format → Expand → Claim → Restore → IF → Send. See `REPLY-MARKUP-PAYLOAD-TRACE-v1.md`.

## 16. Root cause

1. Missing `telegram_has_buttons` / callback fields in Format (IF routed to plain send).  
2. Send keyboard nested under `additionalFields` (n8n ignored; API had no `reply_markup`).  
3. Admin sha256 token ≠ Format FNV token (callbacks unauthorized until sync).

## 17. Repair

Format bridge fields; Send top-level keyboard params; Admin FNV lead-token sync. Same workflow IDs. Node counts unchanged (45/57).

## 18. Callback authorization

ACCESS_CONTROL still gates clicks. After token sync: authorized admin transition `pending→processed` observed. Revoked/public remain denied by existing contract.

## 19. Multi-copy synchronization

Edit Lead Card succeeded for one known copy in harness (buttons removed). Expand Card Sync returned 1 copy — operator should confirm second client UI.

## 20. Archive boundary

`/leads` archive cards remain non-actionable by design.

## 21. Harness

Local button harness: **30/30 PASS**.

## 22. Live acceptance

Synthetic two-recipient delivery with API-proven inline buttons; no duplicate sends in poll window; processed transition after token sync. Visual dual-client confirmation PENDING.

## 23. Parser 3.3 backlog

Requirements package under `research/parser-3.3/` (observations, site-state model, comment boundaries, intent, first-reply rules, fixtures, semantic model draft). **No runtime parser changes.**

## 24. Reminder draft

`product/PENDING-LEAD-REMINDER-SPEC-v1-DRAFT.md` — DRAFT / NOT IMPLEMENTED.

## 25. Final access state

Unchanged intentional roster: 1 active admin, 1 active moderator, 2 revoked moderators.

## 26. Final workflow state

Ops active 45; Admin active 57; v2 inactive; OpenRouter disabled. See `FINAL-WORKFLOW-STATE-v1.md`.

## 27. Safety counters

- AI provider calls = 0  
- Automatic client messages = 0  
- Workflows created = 0  
- Destructive Git operations = 0  
- Parser runtime changes = 0  
- Semantic-classification runtime changes = 0  

## 28. Files created

`product/**`, `research/parser-3.3/**`, `evidence/phase3d8/**`, this report; Storage backup package (outside git).

## 29. Files changed

README, OPERATIONAL-INDEX, and architecture/implementation/guides touch-ups where linked/notes required.

## 30. Security validation

No secrets, Telegram/chat IDs, workbook IDs, phones, raw emails, screenshots, or unsanitized workflow JSON staged for Git. Private backups remain under Storage only.

## 31. Commit

- `67e2fea6` — `fix(iseo-sales-manager-bot): restore lead action buttons and document product baseline`
- `7407a0cb` — `docs(iseo-sales-manager-bot): tighten phase 3d8 baseline limitation notes`

Clean worktree allowlist: `projects/iseo-sales-manager-bot/**` only.

## 32. Push

Pushed without force to `origin/mars/canonical-post-recovery`  
Canonical tip: `7407a0cb`.

## 33. Risks

- Multi-copy sync may leave a second card with buttons until operator confirms/clicks.  
- Synthetic Gmail finalize errors are expected and must not be confused with production Gmail path.  
- Main workspace remains dirty — future agents must keep using clean worktrees.

## 34. SAFE UNKNOWN

- Exact Sheets row counts / formula bodies not fully exported (structure inferred from workflows).  
- Moderator UI visual state after processed transition not operator-attested in this session.

## 35. Remaining operator actions

1. Visually confirm both Telegram accounts.  
2. Optional real button press.  
3. Confirm second copy updates.  
4. Keep Olya/Nikita revoked unless re-enrollment is intentional.

## 36. Stop condition

Phase 3D.8 documentation + backup + button repair complete for commit/push. Do not begin Parser 3.3 implementation. Do not implement reminders. Do not enable AI.

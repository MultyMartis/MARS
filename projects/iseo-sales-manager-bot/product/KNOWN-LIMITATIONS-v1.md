# KNOWN LIMITATIONS v1

- Original lead action buttons: **repaired in Phase 3D.8** (Format bridge + Send keyboard nesting + Admin FNV token sync); Telegram API returned both buttons on both synthetic recipient sends. **ATTENTION:** operator visual dual-client confirmation is still recommended because harness multi-copy edit observed 1 copy.
- Parser remains `sm-parser-v3.2`; Parser 3.3 / Lead Semantic Model **not implemented** (backlog under `research/parser-3.3/`).
- Explicit no-site state not modeled; Telegram links can be mistaken for websites; source-page/comment boundary issues remain.
- Intent may default incorrectly to Audit; first reply may repeat already-known questions.
- Pending-lead reminders **not implemented** (draft only).
- Reusable multi-client deployment / automatic client rollout **not implemented**.
- AI ON **not approved**.
- Archive `/leads` cards remain intentionally buttonless.
- Main `X:\AI MARS` workspace is dirty with foreign WIP — commits must use clean worktrees.
- Full Sheets PII cell dumps are not part of the Phase 3D.8 backup package (structure only).

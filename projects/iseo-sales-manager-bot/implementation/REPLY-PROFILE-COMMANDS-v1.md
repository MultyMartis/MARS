# REPLY PROFILE COMMANDS v1

> **SUPERSEDED for addressing syntax by Phase 3G.2:** use **[REPLY-PROFILE-ADMIN-COMMANDS-v2.md](REPLY-PROFILE-ADMIN-COMMANDS-v2.md)** (number-based `<N>`).  
> This v1 page is retained for **historical honesty** (3G.1 username/token addressing). Treat username-token forms as **obsolete**.

**Lib:** `implementation/runtime-libs/reply-profile-commands-v1.mjs` (runtime now implements v2 number API)

## Commands (historical v1 — obsolete addressing)

| Command | Role | Effect | Classification |
|---------|------|--------|----------------|
| `/reply_profiles` | Admin | list profiles | **current** (list still exists) |
| `/reply_profile <user>` | Admin | show one by username/display token | **obsolete** → `/reply_profile <N>` |
| `/reply_name_set <user> <name>` | Admin | set name | **obsolete** → `/reply_name_set <N> <name>` |
| `/reply_name_enable <user>` | Admin | enable | **obsolete** → `/reply_name_enable <N>` |
| `/reply_name_disable <user>` | Admin | disable | **obsolete** → `/reply_name_disable <N>` |
| `/my_reply_profile` | Admin + Moderator | self view | **current** |

Moderator mutations → deny text: изменение имени доступно только администратору. (3G.2 wording: `Эта команда доступна только администратору.`)

## Help lines

Admin help includes reply-profile command block; moderator help includes only `/my_reply_profile`.  
**3G.2:** rebuild via [ROLE-AWARE-HELP-BUILDER-v2.md](ROLE-AWARE-HELP-BUILDER-v2.md) — no substring patch; placeholders use `<номер>`.

## Live Admin wiring

Command routes in Admin.dev: **live**. Number contract: [REPLY-PROFILE-NUMBERING-v1.md](../architecture/REPLY-PROFILE-NUMBERING-v1.md).  
Phase 3G.1.1 readback: `evidence/phase3g1-1/LIVE-PROFILE-READBACK-v1.md`.  
Phase 3G.2 stubs: `evidence/phase3g2/REPLY-PROFILE-COMMANDS-v1.md`.

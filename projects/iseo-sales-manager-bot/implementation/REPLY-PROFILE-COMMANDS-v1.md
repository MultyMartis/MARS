# REPLY PROFILE COMMANDS v1

**Lib:** `implementation/runtime-libs/reply-profile-commands-v1.mjs`

## Commands

| Command | Role | Effect |
|---------|------|--------|
| `/reply_profiles` | Admin | list profiles |
| `/reply_profile <user>` | Admin | show one |
| `/reply_name_set <user> <name>` | Admin | set + enable if valid |
| `/reply_name_enable <user>` | Admin | enable (requires valid name) |
| `/reply_name_disable <user>` | Admin | disable |
| `/my_reply_profile` | Admin + Moderator | self view |

Moderator mutations → deny text: изменение имени доступно только администратору.

## Help lines

Admin help includes reply-profile command block; moderator help includes only `/my_reply_profile`.

## Live Admin wiring

Command routes in Admin.dev: live patch / operator visual acceptance pending or in progress.

# ADMIN HELP BUILDER v1

**Status:** live on Admin.dev Help node (Phase 3F.2.2); **extended by Phase 3G.2** — see **[ROLE-AWARE-HELP-BUILDER-v2.md](ROLE-AWARE-HELP-BUILDER-v2.md)** for current Admin/moderator templates including reply-profile section  
**Parse mode:** HTML (`cmdHtml` wraps commands in `<code>`; placeholders use `&lt;…&gt;` outside code tags)

## Rules

1. Rebuild templates explicitly — never substring-patch existing help lines.
2. `cmdHtml('/command')` wraps **only** the slash command token.
3. Admin and moderator use separate `helpReply(role)` branches.
4. Moderator help must not advertise config, AI toggles, moderator-management, or reminder configuration commands.
5. Staff lead commands listed for both Admin and active moderator: `/leads`, `/lead_history`, `/pending_count`, `/pending_leads`, `/reminder_status`.
6. Admin-only reminder configuration (`/reminder_on|off|time|timezone|min`) under heading **Только для администратора**.
7. **Phase 3G.2:** Admin help must include reply-profile block (number placeholders); moderator help among profile cmds: only `/my_reply_profile`.

## Defect class prevented

Unsafe insert of `/lead_history` into `/ai_on` string (Phase 3F.2.1 partial help edit) — see `evidence/phase3f2-2/HELP-BUILDER-ROOT-CAUSE-v1.md`.

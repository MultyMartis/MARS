# HELP BUILDER ROOT CAUSE v1

## Summary

Admin `/help` showed a corrupted AI/history block because `/lead_history` was inserted **inside** the string argument of `cmdHtml('/ai_on')` via unsafe substring editing.

## Exact live fragment (pre-repair)

```js
cmdHtml('/ai_o\n/lead_history &lt;номер&gt; — история лидаn') + ' — включить ИИ',
```

## Mechanisms observed

| Symptom | Mechanism |
|---|---|
| `/ai_on` → `/ai_o` | Trailing `n` of `/ai_on` consumed by a bad replace/insert |
| Visible `&lt;номер&gt;` | Pre-escaped HTML entities placed inside `cmdHtml()` → `escHtml` double-escaped `&` to `&amp;lt;` **or** entities shown raw when parse/escaping mismatched; corrupted fragment also broke `<code>` boundaries |
| Literal `n` (`лидаn`) | Intended `\n` separator degraded to character `n` during string surgery |
| Merged lines | Newline embedded **inside** the `cmdHtml(...)` argument instead of a new array element |
| Missing pending / reminder_status | Outdated Admin help template never rebuilt after Phase 3F.1 commands shipped |

## Not the cause

- Telegram message truncation (length was fine)
- Separate duplicate Help constants fighting at runtime (single Help node)
- Moderator branch (Admin role path was the corrupted one)

## Fix principle

Do **not** patch the damaged substring again. Rebuild `helpReply(role)` as explicit Admin and moderator templates with `cmdHtml('/command')` only wrapping the command token; placeholders like `<номер>` stay outside as HTML entities `&lt;номер&gt;` when `parse_mode=HTML`.

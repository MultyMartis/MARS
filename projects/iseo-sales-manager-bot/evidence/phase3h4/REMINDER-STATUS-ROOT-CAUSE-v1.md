# REMINDER STATUS ROOT CAUSE v1

## Verdict

Admin `/reminder_status` long-form reply builder contained **invalid JavaScript** due to a literal backslash-n sequence (`,\n`) between array elements inside the `statusText` assembly — not a valid JS newline inside a string or template.

## Mechanism

- Source: Reminder Commands Code node, Admin long-form branch
- Parser error: **SyntaxError** at parse/eval time
- Effect: entire command handler aborts; operator sees **silence** (no Capture fallback reached for this failure mode pre-patch)

## Non-causes (ruled out)

- Telegram webhook miss — trigger received command
- Authorization deny — admin auth passed
- Sheets read failure — failure precedes Sheets-dependent assembly on this path
- Moderator short-form — separate branch; syntactically fine

## Repair class

String/join fix: use valid JS array `.join('\n')` or template literal newlines; eliminate literal `,\n` token between elements.

## Regression guard

Offline harness: Reminder Commands extracted body validated via `node --check`; `brokenLiteral=false` post-repair.

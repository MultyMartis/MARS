# TEXT FALLBACK PARSER v1 — Phase 3E.1

**Harness:** H02 (multiline text), H03 (one-line / collapsed)

## Behavior

When HTML is absent or empty:

1. Prefer `request_text` / plain text body.
2. Same label regexes as HTML path after plain normalization.
3. Collapsed single-line forms (labels separated by spaces) must still isolate comment and exclude «Отправлено со страницы».

## Acceptance

- Name + site state recovered without HTML.
- One-line fixture preserves comment content and strips page footer bleed.

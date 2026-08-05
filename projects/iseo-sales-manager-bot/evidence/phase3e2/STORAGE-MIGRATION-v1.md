# STORAGE-MIGRATION-v1 — First Reply v2 (additive)

**Mode:** append-only / compatibility  
**Historical bulk regeneration:** **0** (forbidden)

## Preserve

All Parser 3.3 / prior reply columns including `first_reply_text`, `first_reply_source`, `reply_template_version`.

## Additive fields (new leads)

- `first_reply_version`
- `first_reply_mode`
- `first_reply_subject`
- `first_reply_questions`
- `first_reply_reason_codes`
- `first_reply_omitted_reason`
- `first_reply_ready`
- `first_reply_warnings`

Where sheet width is constrained, semantic snapshot may continue via existing `quality_comment` carrier (`first_reply_version=…`) until headers are appended under operator-approved Sheets edit.

## Compatibility

- Old rows: render stored legacy `first_reply_text`; do not fabricate v2 fields
- `/leads` archive: use stored draft; no per-request regeneration
- Backup headers/schema before any live header append

## Backup

Pre-patch Ops/Admin structural JSON stored under local `phase3e2-local/backups/` (private; not committed).

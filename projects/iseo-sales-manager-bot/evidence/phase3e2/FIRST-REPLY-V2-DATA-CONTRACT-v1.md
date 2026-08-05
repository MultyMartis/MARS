# FIRST-REPLY-V2-DATA-CONTRACT-v1

**Version:** `sm-reply-v2.0`  
**Phase:** 3E.2

## Required output fields

| Field | Type | Notes |
|-------|------|-------|
| first_reply_version | string | `sm-reply-v2.0` |
| first_reply_mode | string | normal / test_suppressed / contact_suppressed |
| first_reply_subject | string | short topic |
| first_reply_text | string | draft body |
| first_reply_questions | string/list | asked groups |
| first_reply_reason_codes | string/list | suppressed codes |
| first_reply_omitted_reason | string | omission reason |
| first_reply_ready | boolean | sendable draft ready |
| first_reply_warnings | string/list | non-fatal warnings |

## Compatibility fields retained

- `first_reply_source` (`template` / `test_omitted` / `none`)
- `reply_template_version`

## Forbidden in draft text

parser confidence, probable-test reasons, source markers, internal service codes, workflow state, lead ID, employee names, hashes.

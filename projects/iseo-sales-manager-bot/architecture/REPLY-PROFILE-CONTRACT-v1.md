# REPLY PROFILE CONTRACT v1

**Phase:** 3G.1  
**Version:** `iseo-recipient-name-v1.0`  
**Storage:** additive fields on `ACCESS_CONTROL` rows

## Fields

| Field | Type | Notes |
|-------|------|-------|
| `reply_sender_name` | string | approved client-facing first name |
| `reply_sender_enabled` | bool | personalization on/off |
| `reply_company_name` | string | default `INTLSEO` |
| `reply_profile_version` | string | contract version stamp |
| `reply_profile_updated_at` | string | ISO timestamp |
| `reply_profile_updated_by` | string | admin actor label |

## Validation (fail-closed name)

- Length 2–32
- Letters (Latin/Cyrillic); optional hyphen/apostrophe; no multi-token full names (no auto-shorten surname)
- Reject: empty, `@`, URLs, phones/digits, emoji, role labels, company tokens

## Resolution states

| State | Meaning |
|-------|---------|
| `ready` | valid name + enabled |
| `blocked_sender_disabled` | valid name but disabled |
| `blocked_missing_sender_name` | missing/invalid name |

## Commands (Admin mutations only)

- `/reply_profiles`, `/reply_profile`, `/reply_name_set`, `/reply_name_enable`, `/reply_name_disable`
- Moderator: `/my_reply_profile` (view only)

## Related

- Runtime: `implementation/runtime-libs/reply-profile-lib.mjs`
- Commands: `implementation/runtime-libs/reply-profile-commands-v1.mjs`

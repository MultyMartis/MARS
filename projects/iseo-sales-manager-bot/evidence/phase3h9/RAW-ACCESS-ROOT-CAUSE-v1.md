# RAW ACCESS ROOT CAUSE v1

**Class:** registry/credential failure **mislabeled** as insufficient permissions.

Not:

- authorized user rejected by a correct access checker while ACCESS was healthy
- raw payload missing
- lead_id mismatch as the deny path (Handle never ran)
- per-card ownership
- archive vs current card

Yes:

- Google Sheets OAuth `invalid_grant` on ACCESS_CONTROL + CONFIG
- Check User Authorization correctly set `registry_unavailable`
- Answer Callback Deny ignored deny_reason and always answered with a permission string

Staff model was not ambiguous. ADMIN_A remained the same Telegram user on both cases.

# ACF Source-of-Truth Guidelines — from FP-0002

**Status:** experience documentation only

---

## Rules of thumb

1. **ACF is normal source** for admin-managed pages once parity is declared.
2. **Hardcoded template demo is emergency only** — not the silent default when fields are empty.
3. **Seed current visible content** before cutting over SoT — preserve what the operator already accepted on FE.
4. **Preserve operator data** — never blank accepted ACF to “clean up” without charter + backup.
5. **Clearing optional fields should hide** the block/section (empty-safe), not resurrect demo strings.
6. **Use repeaters for repeated text blocks** — nature paragraphs, stages, FAQ rows, etc.
7. **Media fields should reference Media Library attachments** — not theme-only paths for editor-replaceable images (theme fallbacks allowed as emergency).
8. **Page-specific content** — no wrong copy-paste between services/sections (especially brand/medical copy).
9. **Before/after exports required** for seed/mutation tasks — JSON/CSV/postmeta dumps under validation folders or backups.
10. **Document the field model** in `DOCS/*-ADMIN-PARITY-MODEL-v1.md` before/while implementing.

---

## Cutover recipe

```text
inventory FE blocks
→ design ACF group in FE order
→ seed from visible content
→ switch FE reads to ACF
→ empty-optional → hide
→ quarantine demo inject to emergency helpers
→ operator review
→ freeze
```

---

## Anti-goals

- Seeding one page’s alcohol/special copy into siblings.
- Claiming SoT while fallbacks still fire on empty common fields.
- Mixing unrelated legacy ACF groups without hiding them by role.

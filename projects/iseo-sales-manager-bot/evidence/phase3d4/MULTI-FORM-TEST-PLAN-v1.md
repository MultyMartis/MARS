# MULTI FORM TEST PLAN v1

**Phase:** 3D.4  
**Policy:** **one form per iteration** — no parallel form changes

---

## 1. Registry source

Form definitions: `knowledge/WEBSITE-FORM-FORMATS-v1.md`

Each form record specifies: page slug, field labels, expected service, parser notes, synthetic fixture id.

---

## 2. Iteration gate (mandatory)

For each new website form:

| Step | Owner | Action |
|------|-------|--------|
| 1 | Operator | Add/update registry record (no real client samples) |
| 2 | Dev | Extend parser fixture(s) for that form only |
| 3 | Dev | Run local harness (F-AF + supplied-form) |
| 4 | Operator | Submit **one** synthetic or chartered clean test email |
| 5 | Operator | Verify single Telegram card semantics |
| 6 | Olya | Optional UX review on that form only |
| 7 | Docs | Evidence note + report section before next form |

**Stop** after one form passes — do not batch SEO + audit + callback in one patch wave.

---

## 3. Form queue (planned)

| Priority | Form slug | Registry status | Phase 3D.4 |
|----------|-----------|-----------------|------------|
| 1 | `free-audit` | **defined** | **accepted** (supplied fixture) |
| 2 | `seo` | placeholder | not opened |
| 3 | `direct` | placeholder | not opened |
| 4 | `site-build` | placeholder | not opened |
| 5 | `callback` | placeholder | not opened |
| 6 | `calculator` | placeholder | not opened |

---

## 4. Per-iteration test checklist

- [ ] Registry record complete (labels + page slug + service default)
- [ ] Parser fixture added (synthetic body only)
- [ ] Local harness PASS for that fixture
- [ ] `parser_version` unchanged mid-iteration unless parser patch is the iteration scope
- [ ] One live or chartered test email processed
- [ ] Card: contact/site/source_page correct
- [ ] `/stats` excludes synthetic rows
- [ ] No second form patched in same n8n deploy

---

## 5. Rollback per form

If a form iteration fails live:

1. Revert parser change for **that form's rules only** if isolated.
2. Do not revert Olya enrollment or unrelated forms.
3. Capture `/last_error` + fixture id in evidence.
4. Re-run harness before redeploy.

---

## 6. Out of scope

- Bulk import of historical form variants.
- Multi-language forms (unless separately chartered).
- AI ON per-form tuning.

---

*Related: knowledge/WEBSITE-FORM-FORMATS-v1.md · SUPPLIED-FORM-END-TO-END-v1.md · guides/OPERATOR-RUNBOOK-v1.md.*

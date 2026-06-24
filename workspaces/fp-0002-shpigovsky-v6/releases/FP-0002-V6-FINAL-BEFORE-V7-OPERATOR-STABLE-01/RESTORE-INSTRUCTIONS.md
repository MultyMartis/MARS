# FP-0002 V6 Restore Instructions

**Release:** `FP-0002-V6-FINAL-BEFORE-V7-OPERATOR-STABLE-01`

## Prerequisites

1. Node.js and npm available on PATH.
2. MARS shared Font Awesome source present at:
   `workspaces/shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`
   (relative from workspace: `../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`)
3. Do **not** use `git reset`, `git restore .`, `git checkout -- .`, `git clean`, or `git revert` on operator-canonical source.

## Restore from external ZIP

1. Create a clean directory outside active V6/V7 workspaces.
2. Extract `FP-0002-V6-FINAL-BEFORE-V7-OPERATOR-STABLE-01-SOURCE.zip`.
3. Verify file checksums against `CHECKSUMS-SHA256.txt`.
4. Place workspace under `workspaces/fp-0002-shpigovsky-v6/` **or** keep isolated for test restore.
5. From workspace root:

```bash
npm ci
npm run build
```

## Expected build outputs

- `dist/index.html`
- `dist/uslugi.html`
- `dist/assets/vendor/swiper/swiper-bundle.min.js`
- `dist/assets/vendor/fancybox/fancybox.umd.js`
- `dist/assets/fonts/inter/*.woff2`
- `src/partials/components/modal-consultation.html` (source include)

## Verification checklist

- [ ] `npm ci` completes without errors
- [ ] `npm run build` completes without errors
- [ ] Home and Services dist pages exist
- [ ] Active includes resolve (no gulp-file-include errors)
- [ ] Local Inter fonts copied to dist
- [ ] Swiper and Fancybox vendor assets present
- [ ] Modal partial exists in source tree

## Authority rule

Restored source is operator-canonical. Do not normalize or “fix” manual operator values when restoring.

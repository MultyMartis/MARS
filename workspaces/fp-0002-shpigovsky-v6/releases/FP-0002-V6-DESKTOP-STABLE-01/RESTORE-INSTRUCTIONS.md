# FP-0002 V6 DESKTOP STABLE 01 — Restore Instructions

**Release ID:** `FP-0002-V6-DESKTOP-STABLE-01`  
**Archive:** `FP-0002-V6-DESKTOP-STABLE-01-SOURCE.zip`  
**Canonical source authority:** operator-canonical `src/` only — **not** `dist/`

---

## 1. Requirements

| Item | Value |
|------|-------|
| Node.js | v24.13.1 (validated at freeze) |
| npm | 11.8.0 (validated at freeze) |
| OS | Windows / cross-platform Node supported |
| Working folder | Any empty directory; example `C:\restore\fp-0002-v6-desktop-stable-01\` |

No secrets or credentials are required for local restore.

---

## 2. Unpack archive

1. Obtain `FP-0002-V6-DESKTOP-STABLE-01-SOURCE.zip` from MARS Storage (see release manifest).
2. Extract to a clean directory. Root folder inside archive: `FP-0002-V6-DESKTOP-STABLE-01/`.
3. Verify `CHECKSUMS-SHA256.txt` against extracted files (see §8).

---

## 3. Install dependencies

```powershell
cd FP-0002-V6-DESKTOP-STABLE-01
npm ci
```

Use `npm ci` (not `npm install`) to match frozen `package-lock.json`.

**Font Awesome build dependency:** Gulp copies Font Awesome Pro from `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` at the MARS repository root (two levels above workspace). Archive includes generated bridge file `src/scss/vendors/fa-all.css`; full rebuild outside the repo requires equivalent shared vendor access.

---

## 4. Build

```powershell
npm run build
```

Expected: Gulp completes without errors; `dist/index.html` and `dist/assets/` are generated.

---

## 5. Dev watcher (optional)

```powershell
npm run watch
```

Or `npm run watch:dev` if live reload is needed. Do not replace `src/` with `dist/` output.

---

## 6. Local Inter fonts

After build, confirm:

- `dist/assets/fonts/inter/inter-300.woff2`
- `dist/assets/fonts/inter/inter-400.woff2`
- `dist/assets/fonts/inter/inter-500.woff2`
- Latin subset WOFF2 files present
- `src/fonts/inter/INTER-FONT-PROVENANCE.md` documents local delivery

---

## 7. No Google Fonts

In restored `src/pages/index.html` and compiled CSS:

- No `<link>` to `fonts.googleapis.com` or `fonts.gstatic.com`
- No runtime `@import` to Google Fonts in active page CSS
- Provenance doc may reference historical Google URL for equivalence only

---

## 8. Expected output

| Artifact | Path |
|----------|------|
| HTML | `dist/index.html` |
| CSS | `dist/assets/css/style.css` |
| JS | `dist/assets/js/main.js` |
| Inter WOFF2 | `dist/assets/fonts/inter/*.woff2` |
| Images | `dist/assets/img/**` |
| FA webfonts | `dist/assets/webfonts/**` (generated from shared vendor bridge) |

---

## 9. Git baseline by tag

From MARS repository root:

```powershell
git fetch origin tag fp-0002-v6-desktop-stable-01
git checkout fp-0002-v6-desktop-stable-01
```

Workspace path: `workspaces/fp-0002-shpigovsky-v6/`.

---

## 10. Do not substitute `dist` for `src`

- `dist/` is **generated output** — rebuild from `src/` after any restore.
- Do not copy `dist/` back into `src/` or treat build output as canonical source.
- Design values are frozen in `src/scss/style.scss` and HTML partials.

---

## Verification checklist

- [ ] Archive checksum matches manifest
- [ ] File checksums match `CHECKSUMS-SHA256.txt`
- [ ] `npm ci` succeeds
- [ ] `npm run build` succeeds
- [ ] No Google Fonts network dependency in active page
- [ ] No `data-safe-unknown` in active `src/` HTML
- [ ] Desktop Header / Hero / Footer render from local build

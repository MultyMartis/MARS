# FP-0002 V6 HOME SECTION 01 OPERATOR STABLE 01 — Restore Instructions

**Release ID:** `FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01`  
**Archive:** `FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01-SOURCE.zip`  
**Canonical source authority:** operator-canonical `src/` only — **not** `dist/`

---

## 1. Requirements

| Item | Value |
|------|-------|
| Node.js | v24.13.1 (validated at freeze) |
| npm | 11.8.0 (validated at freeze) |
| OS | Windows / cross-platform Node supported |
| Working folder | Any empty directory |

No secrets or credentials are required for local restore.

---

## 2. Unpack archive

1. Obtain `FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01-SOURCE.zip` from MARS Storage (see release manifest).
2. Extract to a clean directory. Root folder inside archive: `FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01/`.
3. Verify `CHECKSUMS-SHA256.txt` against extracted files (see §8).

---

## 3. Install dependencies

```powershell
cd FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01
npm ci
```

**Font Awesome build dependency:** Gulp copies Font Awesome Pro from `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` at the MARS repository root.

---

## 4. Build

```powershell
npm run build
```

---

## 5. Local Inter fonts

After build, confirm WOFF2 files under `dist/assets/fonts/inter/`.

---

## 6. No Google Fonts

No `fonts.googleapis.com` or `fonts.gstatic.com` in restored active page.

---

## 7. Expected output

| Artifact | Path |
|----------|------|
| HTML | `dist/index.html` |
| CSS | `dist/assets/css/style.css` |
| JS | `dist/assets/js/main.js` |

---

## 8. Git baseline by tag

```powershell
git fetch origin tag fp-0002-v6-section-01-operator-stable-01
git checkout fp-0002-v6-section-01-operator-stable-01
```

Workspace path: `workspaces/fp-0002-shpigovsky-v6/`.

---

## 9. Section 01 freeze verification

After build, confirm:

- Section 01 partial: `home-recovery-intro.html` present in dist
- Section 02 **absent**
- `data-safe-unknown` = 0 in active HTML
- Project-owned SCSS files = 1 (`src/scss/style.scss`)
- Responsive shell (Header, Hero, Footer, off-canvas) renders without regression

---

## 10. Do not substitute `dist` for `src`

`dist/` is generated output — rebuild from `src/` after any restore.

---

## Verification checklist

- [ ] Archive checksum matches manifest
- [ ] File checksums match `CHECKSUMS-SHA256.txt`
- [ ] `npm ci` succeeds
- [ ] `npm run build` succeeds
- [ ] Section 01 present; Section 02 absent
- [ ] No Google Fonts in active page
- [ ] Local Inter present

# FP-0002 V6 RESPONSIVE SHELL STABLE 01

**Release identity:** `FP-0002-V6-RESPONSIVE-SHELL-STABLE-01`  
**Milestone:** FP-0002 RESPONSIVE SHELL STABLE BASELINE  
**Recorded:** 2026-06-23  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`

---

## Release identity

| Field | Value |
|-------|-------|
| Release ID | `FP-0002-V6-RESPONSIVE-SHELL-STABLE-01` |
| Git tag | `fp-0002-v6-responsive-shell-stable-01` |
| Prior checkpoint | `fp-0002-v6-desktop-stable-01` (`759637ac69a6f71f3f0c68181a978b5db0aa8d3d`) |
| Branch | `mars/post-cycle8-live-tests` |

---

## Operator approval

| Item | Status |
|------|--------|
| Desktop Header | **APPROVED** |
| Mobile Header | **APPROVED AS CURRENT BASELINE** |
| Desktop Hero | **APPROVED** |
| Off-canvas left-side menu | **APPROVED AS CURRENT BASELINE** |
| Desktop Footer | **APPROVED** |
| Mobile Footer | **APPROVED AS CURRENT BASELINE** |
| Local Inter | **APPROVED** |
| Visible FOUT | **RESOLVED** |
| Operator-canonical src | **ACTIVE** |
| Main content | **NOT STARTED** |

---

## Stable scope

Frozen responsive shell only:

- Header (desktop + mobile bar)
- Hero (desktop)
- Off-canvas menu (left-side opening)
- Footer (desktop + mobile responsive rules)
- Local Inter WOFF2 delivery
- Universal `.btn` system
- Single `src/scss/style.scss`
- Empty `main` placeholder

**Not in scope:** main content sections between Hero and Footer.

---

## Canonical source authority

```text
Current files under src/ are operator-canonical.
This release records and backs up that authority.
No automated task may overwrite current src without explicit operator instruction.
```

---

## Git branch

`mars/post-cycle8-live-tests`

---

## Git commit

Release commit message: `chore(fp-0002): freeze responsive shell stable baseline`

Resolve hash: `git rev-parse fp-0002-v6-responsive-shell-stable-01`

---

## Git tag

| Field | Value |
|-------|-------|
| Name | `fp-0002-v6-responsive-shell-stable-01` |
| Type | Annotated |
| Message | FP-0002 V6 responsive shell stable baseline: desktop/mobile Header, left off-canvas, Hero, desktop/mobile Footer and local Inter. |

---

## Backup archive path

| Location | Path |
|----------|------|
| MARS Storage (primary) | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-RESPONSIVE-SHELL-STABLE-01-SOURCE.zip` |
| Archive sidecar | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-RESPONSIVE-SHELL-STABLE-01-SOURCE.sha256` |

ZIP is **not** committed to Git (external storage policy).

---

## Backup archive checksum

```
SHA-256: 44f1a9d0e347e54d888a5026f3251b9ba7c341380c7bfc2f6f5bc8d5be062c0f
Size: 4060068 bytes
Entries: 36
Source files checksummed: 27
```

Manifest SHA-256: compute at commit time from this file path in repo.

---

## Source inventory

| Category | Count |
|----------|------:|
| Canonical `src/` files | 22 |
| Asset files (svg/png/woff2 in src) | 11 |
| Local Inter WOFF2 | 6 |
| Off-canvas JS module | 1 (`src/js/main.js`) |

See [CHECKSUMS-SHA256.txt](./CHECKSUMS-SHA256.txt) for per-file SHA-256.

**Operator changes since desktop stable:** mobile header actions wrapper, messenger icons in mobile bar, off-canvas left panel geometry, mobile footer responsive rules — included in baseline; not reverted.

---

## Design-system state

| Law / contract | Status |
|----------------|--------|
| Universal Style Scale (`--pad-*`) | ACTIVE |
| `--radius-main` / `--radius-full` only | ACTIVE |
| `--button-letter-spacing` | PROHIBITED |
| Universal `.btn` system | ACTIVE |
| Single base `.container` | ACTIVE |
| `--container-hero` exception | APPROVED |
| One project SCSS file | ACTIVE |
| Operator-canonical source law | ACTIVE |
| Design value freeze | **ACTIVE** |

---

## Font delivery

| Field | Value |
|-------|-------|
| Delivery | LOCAL_WOFF2 |
| Google Fonts runtime dependency | REMOVED |
| `font-display` | block |
| Critical preload | ACTIVE |
| Provenance | `src/fonts/inter/INTER-FONT-PROVENANCE.md` |

---

## Header status

**Desktop — APPROVED** — operator-canonical; frozen.  
**Mobile — APPROVED AS CURRENT BASELINE** — logo, primary phone, messenger icons, menu trigger; frozen.

---

## Hero status

**APPROVED** — desktop operator-canonical; frozen.

---

## Off-canvas status

**APPROVED AS CURRENT BASELINE** — opens from left (`translateX(-100%)` → `0`); closes via button, overlay, Escape; scroll lock; focus return; both phones, navigation, CTA in panel.

---

## Footer status

**Desktop — APPROVED** — operator-canonical; frozen.  
**Mobile — APPROVED AS CURRENT BASELINE** — responsive rules active; frozen.

---

## Main content status

**NOT STARTED**

---

## JavaScript status

Off-canvas mobile menu in `src/js/main.js` — `data-offcanvas*` hooks only; no CSS class behavior hooks.

---

## Build command

```powershell
cd workspaces/fp-0002-shpigovsky-v6
npm ci
npm run build
```

---

## Build result

**PASS** — validated at freeze.

**Archive verification:** PASS  
**Checksum verification:** PASS  
**Restore test:** PASS — archive extracted to `workspaces/fp-0002-shpigovsky-v6-responsive-shell-restore-test/`, `npm ci`, `npm run build` succeeded; local fonts present; no Google Fonts in dist HTML; off-canvas JS present.

**Build dependency:** Font Awesome Pro bridge reads `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` at repo root (not inside ZIP).

---

## Restore procedure

See [RESTORE-INSTRUCTIONS.md](./RESTORE-INSTRUCTIONS.md).

---

## Frozen invariants

```text
Current src is operator-canonical.
One project SCSS file: src/scss/style.scss.
No SCSS partials.
Shared --pad-* scale.
--radius-main and --radius-full only.
--button-letter-spacing prohibited.
Universal .btn system.
Single base .container.
--container-hero approved exception.
Local Inter WOFF2.
No Google Fonts runtime in active page.
No data-safe-unknown in active HTML.
Semantic-case HTML.
JS hooks through data-*.
Responsive shell design values frozen.
Off-canvas opens from left.
```

---

## Authorized next phase

```text
AUTHORIZED NEXT PHASE:
Main content — home Section 01 only (desktop), after operator gate
```

Section 02+ and full mobile main content remain **NOT STARTED**.

---

## Known limitations

- Main content sections not implemented.
- Mobile main content sections not implemented (shell only).
- Font Awesome build requires MARS shared vendor tree at repo root.
- `dist/` is generated only — not canonical source.

---

## Unrelated WIP excluded

Not part of this release: OCPilot, ORCA, MIG/search-ppc, Forge WordPress, localhost infrastructure, BZPM, `.recovery-temp/`, other workspaces, unrelated reports.

---

## Related artefacts

| Artefact | Path |
|----------|------|
| File checksums | [CHECKSUMS-SHA256.txt](./CHECKSUMS-SHA256.txt) |
| Restore instructions | [RESTORE-INSTRUCTIONS.md](./RESTORE-INSTRUCTIONS.md) |
| Release screenshots | [../../reviews/releases/visual/](../../reviews/releases/visual/) |
| Off-canvas matrix | [../../reviews/responsive/FP-0002-V6-OFFCANVAS-FUNCTIONAL-MATRIX.json](../../reviews/responsive/FP-0002-V6-OFFCANVAS-FUNCTIONAL-MATRIX.json) |
| Operational status | [../../foundation/FP-0002-V6-OPERATIONAL-STATUS.md](../../foundation/FP-0002-V6-OPERATIONAL-STATUS.md) |

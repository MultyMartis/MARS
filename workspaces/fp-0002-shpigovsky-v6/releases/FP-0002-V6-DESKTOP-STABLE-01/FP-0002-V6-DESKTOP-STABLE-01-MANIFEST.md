# FP-0002 V6 DESKTOP STABLE 01

**Release identity:** `FP-0002-V6-DESKTOP-STABLE-01`  
**Milestone:** FP-0002 FIRST STABLE DESKTOP BASELINE  
**Recorded:** 2026-06-23  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`

---

## Release identity

| Field | Value |
|-------|-------|
| Release ID | `FP-0002-V6-DESKTOP-STABLE-01` |
| Git tag | `fp-0002-v6-desktop-stable-01` |
| Prior checkpoint | `24e55bb1d459870e1adbd73f37dde6d0c23e6734` |
| Branch | `mars/post-cycle8-live-tests` |

---

## Operator approval

Operator visually confirmed desktop baseline (2026-06-23):

| Item | Status |
|------|--------|
| Operator confirmed local font result | **APPROVED** |
| Visible FOUT | **NOT OBSERVED / RESOLVED** |
| Desktop Header | **APPROVED** |
| Desktop Hero | **APPROVED** |
| Desktop Footer | **APPROVED** |
| Operator-canonical src | **APPROVED** |
| Current desktop geometry | **STABLE** |

---

## Stable scope

Frozen desktop shell only:

- Header (desktop)
- Hero (desktop)
- Footer (desktop)
- Local Inter WOFF2 delivery
- Universal `.btn` system
- Single `src/scss/style.scss`
- Empty `main` placeholder

**Not in scope:** mobile Header, off-canvas menu, mobile Footer, main content sections.

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

Release commit message: `chore(fp-0002): freeze desktop stable baseline`

Resolve hash: `git rev-parse fp-0002-v6-desktop-stable-01`

---

## Git tag

| Field | Value |
|-------|-------|
| Name | `fp-0002-v6-desktop-stable-01` |
| Type | Annotated |
| Message | FP-0002 V6 desktop stable baseline: approved Header, Hero, Footer and local Inter delivery. |

---

## Backup archive path

| Location | Path |
|----------|------|
| MARS Storage (primary) | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-DESKTOP-STABLE-01-SOURCE.zip` |
| Archive sidecar | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-DESKTOP-STABLE-01-SOURCE.sha256` |

ZIP is **not** committed to Git (external storage policy).

---

## Backup archive checksum

```
SHA-256: d1cbc9d385bd33ec6b358f8e7ffc39948875aec62383c3485fa0d38c3a0e3438
Size: 4056213 bytes
```

---

## Source inventory

| Category | Count |
|----------|------:|
| Canonical `src/` files | 22 |
| Asset files (svg/png/woff2 in src) | 11 |
| Local Inter WOFF2 | 6 |

See [CHECKSUMS-SHA256.txt](./CHECKSUMS-SHA256.txt) for per-file SHA-256.

**Operator change vs `24e55bb1`:** `src/scss/style.scss` — post-checkpoint operator calibration (`.btn` vertical alignment; footer background removal). Included in baseline; not reverted.

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

**APPROVED** — desktop operator-canonical; frozen.

---

## Hero status

**APPROVED** — desktop operator-canonical; frozen.

---

## Footer status

**APPROVED** — desktop operator-canonical; frozen.

---

## Main content status

**NOT STARTED**

---

## Responsive status

Desktop baseline frozen. Mobile/responsive **NOT STARTED**.

---

## JavaScript status

Zero skeleton (`src/js/main.js` stub). No mobile/off-canvas JS.

---

## Build command

```powershell
cd workspaces/fp-0002-shpigovsky-v6
npm ci
npm run build
```

---

## Build result

**PASS** — validated at freeze (Node v24.13.1, npm 11.8.0).

**Restore test:** PASS — archive extracted to `workspaces/fp-0002-shpigovsky-v6-restore-test/`, `npm ci`, `npm run build` succeeded.

**Build dependency:** Font Awesome Pro bridge reads `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` at repo root (not inside ZIP). Restore outside MARS repo requires equivalent shared path or pre-built `src/scss/vendors/fa-all.css`.

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
Desktop design values frozen.
```

---

## Authorized next phase

```text
AUTHORIZED NEXT PHASE:
Mobile Header
Off-canvas Mobile Menu
Mobile Footer
```

Main content remains **NOT STARTED**. Mobile work must branch from this tag; must not alter frozen desktop values without explicit unfreeze.

---

## Known limitations

- Main content sections not implemented.
- No responsive/mobile layout.
- Font Awesome build requires MARS shared vendor tree at repo root.
- `dist/` is generated only — not canonical source.
- Foundation JSON under `foundation/` may contain stale Google Fonts references; **src/** is authority.

---

## Unrelated WIP excluded

Not part of this release: OCPilot, ORCA, MIG/search-ppc, Forge WordPress, localhost infrastructure, BZPM, `.recovery-temp/`, other workspaces, unrelated reports, restore-test workspace folder.

---

## Related artefacts

| Artefact | Path |
|----------|------|
| File checksums | [CHECKSUMS-SHA256.txt](./CHECKSUMS-SHA256.txt) |
| Restore instructions | [RESTORE-INSTRUCTIONS.md](./RESTORE-INSTRUCTIONS.md) |
| Release screenshot | [FP-0002-V6-DESKTOP-STABLE-01-FULL.png](./FP-0002-V6-DESKTOP-STABLE-01-FULL.png) |
| Operational status | [../../foundation/FP-0002-V6-OPERATIONAL-STATUS.md](../../foundation/FP-0002-V6-OPERATIONAL-STATUS.md) |

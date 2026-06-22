# FP-0002 V6 HOME SECTION 01 OPERATOR STABLE 01

**Release identity:** `FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01`  
**Milestone:** FP-0002 HOME SECTION 01 OPERATOR POLISH FREEZE  
**Recorded:** 2026-06-23  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`

---

## Release identity

| Field | Value |
|-------|-------|
| Release ID | `FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01` |
| Git tag | `fp-0002-v6-section-01-operator-stable-01` |
| Prior checkpoint | `69fe35b7066d1724edb256509631b05bfc56c621` |
| Prior shell release | `fp-0002-v6-responsive-shell-stable-01` |
| Branch | `mars/post-cycle8-live-tests` |

---

## Operator approval

| Item | Status |
|------|--------|
| Responsive shell | **FROZEN** |
| Hero | **FROZEN** |
| Section 01 | **OPERATOR POLISHED / APPROVED / FROZEN** |
| Footer | **FROZEN** |
| Local Inter | **APPROVED** |
| Visible FOUT | **RESOLVED** |
| Operator-canonical src | **ACTIVE** |
| Section 02 | **NOT STARTED** |
| Section 03 | **NOT STARTED** |

---

## Stable scope

Frozen baseline includes:

- Responsive shell (Header desktop/mobile, off-canvas, Footer desktop/mobile)
- Hero (desktop)
- Section 01 operator-polished (`home-recovery-intro.html`)
- Local Inter WOFF2 delivery
- Universal `.btn` system
- Single `src/scss/style.scss`
- Current style foundation tokens

**Not in scope:** Section 02+, Section 03+, main content beyond Section 01.

---

## Canonical source authority

```text
Current src — OPERATOR CANONICAL
Previous generated implementations (including commit 69fe35b agent delivery) are historical evidence only.
Operator manual polish after 69fe35b is the active design authority for Section 01.
```

---

## Operator changes since `69fe35b`

| File | Operator change | Preserve |
|------|-----------------|----------|
| `src/partials/sections/home-recovery-intro.html` | Decor image HTML commented out; wrapper `--wrapper` layout; 6-card grid (3×2); icon/title inline structure; `fa-check` icons | YES |
| `src/scss/style.scss` | H1–H3 token scale adjusted; `main > section` vertical padding; Section 01 flex/grid/card restyle; card border primary color; transparent card bg; card gap 20px; benefits dot 8px | YES |
| `src/pages/index.html` | Unchanged vs 69fe35b | YES |
| `src/js/main.js` | Unchanged vs 69fe35b | YES |

---

## Git commit

Release commit message: `chore(fp-0002): freeze operator-polished section 01`

Resolve hash: `git rev-parse fp-0002-v6-section-01-operator-stable-01`

---

## Git tag

| Field | Value |
|-------|-------|
| Name | `fp-0002-v6-section-01-operator-stable-01` |
| Type | Annotated |
| Message | FP-0002 V6 stable baseline with operator-polished Section 01, responsive shell, Hero, Footer and local Inter. |

---

## Backup archive path

| Location | Path |
|----------|------|
| MARS Storage (primary) | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01-SOURCE.zip` |
| Archive sidecar | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-HOME-SECTION-01-OPERATOR-STABLE-01-SOURCE.sha256` |

---

## Restore procedure

See [RESTORE-INSTRUCTIONS.md](./RESTORE-INSTRUCTIONS.md).

---

## Frozen invariants

```text
Section 01 HTML/SCSS operator values frozen.
Responsive shell frozen.
One project SCSS file: src/scss/style.scss.
Local Inter WOFF2.
No Google Fonts runtime in active page.
No data-safe-unknown in active HTML.
Section 02 absent from index.html at this release.
```

---

## Authorized next phase

```text
AUTHORIZED NEXT PHASE:
Home Section 02 only (desktop), after audit gate PASS
```

---

## Related artefacts

| Artefact | Path |
|----------|------|
| File checksums | [CHECKSUMS-SHA256.txt](./CHECKSUMS-SHA256.txt) |
| Restore instructions | [RESTORE-INSTRUCTIONS.md](./RESTORE-INSTRUCTIONS.md) |
| Operational status | [../../foundation/FP-0002-V6-OPERATIONAL-STATUS.md](../../foundation/FP-0002-V6-OPERATIONAL-STATUS.md) |

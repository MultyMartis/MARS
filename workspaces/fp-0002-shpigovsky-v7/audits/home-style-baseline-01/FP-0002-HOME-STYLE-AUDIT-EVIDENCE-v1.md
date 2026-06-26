# FP-0002 — Home Style Audit Evidence v1

**Audit ID:** `home-style-baseline-01`  
**Date:** 2026-06-26

---

## 1. Authority preflight evidence

| Check | Result | Evidence |
|-------|--------|----------|
| Repository | `C:\MARS Phenix\AI MARS` | `git rev-parse --show-toplevel` |
| Branch | `mars/canonical-post-recovery` | `git branch --show-current` |
| HEAD | `f5a9ecd74921f3677e4b7b817be0fe75172b27dc` | `git rev-parse HEAD` |
| Tag | `fp-0002-v7-home-operator-stable-before-style-audit-01` → **same commit** | `git rev-list -n 1 <tag>` |
| Remote | Tracking `origin/mars/canonical-post-recovery`, no ahead/behind shown | `git status -sb` |
| Stable ZIP | Present | `C:\MARS Phenix\AI MARS STORAGE\...\FP-0002-V7-HOME-OPERATOR-STABLE-BEFORE-STYLE-AUDIT-01-SOURCE.zip` |
| ZIP SHA-256 | `61A7AC49E4A55EEDFF5389B91F91C3467D0134D1482E5F1FEDB598E3B0E6506B` | `Get-FileHash` |
| `node_modules` | Present | `Test-Path` → True |
| `dist/index.html` | Present | `Test-Path` → True |

**Authority verdict:** PASS — branch, HEAD, tag, and ZIP align.

**Source cleanliness:** FAIL for strict “clean tree” — two unstaged WIP lines in FP-0002 source (typo + founder photo radius). Audit authority = **committed** `f5a9ecd7`, not working tree.

---

## 2. Source inventory paths verified

| Path | Status @ f5a9ecd7 |
|------|-------------------|
| `src/pages/index.html` | 19 main sections + hero in intro |
| `src/pages/uslugi.html` | 5 home partials reused |
| `src/partials/layout/*` | head, header, footer |
| `src/partials/sections/*` | 20 section partials + hero-inner |
| `src/scss/style.scss` | ~4052 lines monolith |
| `src/js/main.js` | 1228 lines |
| `src/img/**` | content, hero, branding, social |
| `src/svg/**` | external-link, founder-quote-mark |
| `src/video/**` | not present as top-level dir in inventory (videos under img/content) |

---

## 3. Build and render evidence

| Action | Result |
|--------|--------|
| `npm run build` | **FAILED** — `EBUSY: resource busy or locked, rmdir dist` |
| Active dist server | `http-server` on port **4174** serving `dist/` (terminal pid 3068) |
| dist correspondence to f5a9ecd7 | **Not re-verified by rebuild** — existing dist assumed from prior operator build; WIP in working tree not in dist if server started from earlier build |

**Screenshots:** Not captured — CSS/source analysis sufficient for baseline audit; viewport checks deferred to Services planning pass when dist can be rebuilt without lock.

**Render inspection method:** Source + compiled CSS rules + existing dist availability + prior review docs under `reviews/package-001/`.

---

## 4. Design materials evidence

| Asset | Status |
|-------|--------|
| `Spig_v1.2.fig` | Present (untracked in git status) — active design authority per foundation docs |
| `26.06.2026/Услуги общая - Десктоп.png` | Present (~9.2 MB) |
| `26.06.2026/Услуги общая - Мобильная.png` | Present (~5.1 MB) |
| `Шпиговский.fig` | Not used per task boundary |

---

## 5. Working-tree drift (documented, not fixed)

```diff
home-recovery-intro.html: «ШШпиговский» → «Шпиговский» (typo fix WIP)
style.scss: founder variant-b photo border-radius 0 → var(--radius-main) (WIP)
```

Classification: WIP outside audit commit scope; operator should commit or discard separately.

---

## 6. Supporting internal docs referenced

- `reviews/package-001/spacing-cleanup/FP-0002-V7-BASE-VERTICAL-RHYTHM-AUTHORITY.md`
- `foundation/FP-0002-V7-OPERATIONAL-STATUS.md`
- `PROJECT-STATUS.md` (services reuse notes)

---

## 7. Screenshot directory

`evidence/screenshots/` — created empty; no files added (build lock prevented fresh capture run).

---

*End of audit evidence v1.*

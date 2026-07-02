# FP-0002 V9 — ZPM Preloader Authority Map v1

**Phase:** V9-03A  
**Status:** Authority selected for adaptation (not copied verbatim)

## Search inventory

| Path | Classification | Notes |
|------|----------------|-------|
| `projects/ocpilot/sites/site-002/reports/site-002-operator-manual-polish-01-work/live-capture/assets__js__main.js` | **CURRENT_ZPM_AUTHORITY** | Complete preloader IIFE: storage gate, fake progress, `window.load`, BFCache `pageshow`, min show time |
| `projects/ocpilot/sites/site-002/reports/site-002-operator-manual-polish-01-work/live-capture/assets__css__style.css` | **CURRENT_ZPM_AUTHORITY** | `.zpm-preloader` SCSS/CSS block, `html.is-preloader-active`, reduced-motion |
| `projects/ocpilot/sites/site-002/qa/m9.13-about-redesign-v2-desktop.html` | **APPROVED_EXAMPLE** | Inline head script + markup anatomy |
| `projects/ocpilot/sites/site-002/reports/*-work/style.css` | **HISTORICAL** | Iteration copies of same block |
| `workspaces/fp-0002-shpigovsky-v9` (pre V9-03A) | **UNSUITABLE** | No preloader present |

## Selected authority

**Primary:** `site-002-operator-manual-polish-01-work/live-capture` (JS + CSS paired capture)

## Reusable pattern

1. Early `<head>` inline script adds `is-preloader-active` when storage gate allows.
2. Fixed full-viewport overlay with progress line (fake progress until `load`).
3. `html.is-preloader-active` controls visibility + `overflow: hidden`.
4. Minimum visible duration before fade-out.
5. `pageshow` with `persisted` → immediate hide (BFCache).
6. `prefers-reduced-motion` shortens/removes transitions.

## ZPM branding not copied

- Class prefix `zpm-preloader` → `site-preloader`
- Percent text (`0%`) removed for calmer FP-0002 UX
- ZPM color tokens → FP-0002 `--color-page-background`, `--color-accent`
- Logo: FP-0002 `assets/img/branding/logo.svg`

## FP-0002 adaptations

| ZPM | FP-0002 V9-03A |
|-----|----------------|
| `localStorage` daily key `zpmPreloaderShownDate` | `sessionStorage` key `fp0002_preloader_session` (once per session) |
| `MIN_SHOW_MS` 500 | 300 ms |
| No hard fail-safe in captured snippet | 3000 ms fail-safe timeout |
| Percent + line | Logo + line only |
| `zpm-preloader` markup | `site-preloader` partial |

## Risks

- Static MPA: full page reload shows preloader once per session only (by design).
- `sessionStorage` denial handled: preloader may show each navigation; site remains usable.

## Rejected alternatives

- Inventing preloader without ZPM reference — rejected per phase charter.
- Daily `localStorage` repeat policy — rejected; operator preferred restrained session repeat.

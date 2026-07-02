# FP-0002 V9 — Forge Readiness Notes v1

**Status:** `FP0002_V9_OPERATOR_APPROVED_STATIC_FRONTEND_STABLE_BASELINE_COMPLETE`  
**Phase:** V9-03 stable baseline checkpoint complete — ready for V9-04 Forge Intake Pack

## Motion contracts (V9-03F — Forge must preserve)

### Preloader
- **None.** Forge must **not** recreate preloader, sessionStorage loading gate, or global page-load fade.
- Page renders immediately on load.

### Buttons
- Hover: **color/border/box-shadow only** — no transform lift
- Duration: `var(--motion-base)` (~0.3s)

### Modal
- **Runtime authority:** operator-approved **Triumph Manipulator** modal lifecycle (overflow lock + open/close cleanup), adapted for FP-0002 scroll container — **not** V9-03D/V9-03E shell-fixed runtimes.
- Overlay: semitransparent `rgba(17, 24, 39, 0.56)`; fixed viewport; fade ~0.3s (**Shpigovsky visual design unchanged**)
- Close lifecycle: `data-modal-state="closing"` → animate → `[hidden]`
- **Scroll lock (V9-03F):** `html/body.is-modal-scroll-locked` with `height:auto` during lock + saved `bodyScrollLockY` restore on unlock — **no** `pageShellEl.style.position=fixed`, **no** global `body { position: fixed }`
- **Focus:** `preventScroll` on modal field + trigger restore
- **DOM:** modal **outside** `.site-page-shell` via `global-consultation-modal.html`
- WordPress dynamic templates must preserve one global modal and this behavior contract
- Forge must **not** copy Triumph visual design/branding
- Acceptance test: **no visible background movement** on open/close (operator visual review)

### Gallery (Fancybox 5)
- Unchanged from V9-03B

### Section reveal
- `[data-reveal]` scroll animation remains

### Scroll-to-top (V9-03G)
- **One global shared component** emitted once per page via footer include
- Fixed bottom-right; visible when `scrollY > 500`; hidden at `scrollY <= 500`
- Click: smooth scroll to top; reduced-motion → immediate scroll
- z-index **900** — below modal (1200) and offcanvas (1000)
- **No interaction** with modal scroll lock or body classes
- WordPress integration must preserve **one global instance**; verify admin-bar offset later if needed
- No preloader

## O-Centre infrastructure narrative (V9-03C)

- Groups **G0–G5** are current authority on `/o-centre/`
- **G6 mobile-close block intentionally removed** — Forge must not recreate `data-inf-group="g6"` or mobile-only infrastructure-19/20 stack

See also `FP-0002-V9-MOTION-SYSTEM-v1.md` and `FP-0002-V9-PRELOADER-BEHAVIOR-v1.md` (03B supersedes preloader background/reveal details).

## Source authority

- **Frontend source:** `workspaces/fp-0002-shpigovsky-v9/src/`
- **Visual/runtime reference:** `workspaces/fp-0002-shpigovsky-v9/dist/`
- **Route authority:** `tools/v9-route-manifest.json` (version 9.02)

## Route inventory (31 published)

All manifest routes emitted. No genotyping. No new V9-02 placeholder routes.

## Internal links (V9-02)

- All meaningful client-facing navigation resolves to manifest routes or allowlisted social `#`
- Blog fixture article: `/blog/nazvanie-stati/`
- Reviews archive: `/otzyvy/` (no detail pages)
- Service/O-Centre links reconciled

## Legal page family

| Route | Status | Forge mapping |
|-------|--------|---------------|
| `/privacy-policy/` | LEGAL_DEMO_DOCUMENT | WordPress Page / legal template |
| `/user-agreement/` | LEGAL_DEMO_DOCUMENT | WordPress Page / legal template |
| `/consent-personal-data/` | LEGAL_DEMO_DOCUMENT | WordPress Page + form consent link |
| `/cookie-files-policy/` | LEGAL_DEMO_DOCUMENT | WordPress Page |

- Content is **provisional** — `[ДЕМО: ...]` tokens must be replaced before production
- Legal body should remain editor-manageable
- Form consent links must preserve routes: `/privacy-policy/`, `/consent-personal-data/`
- Cookie policy exists; **cookie consent banner not implemented** — separate Forge phase

## Template interpretation

| V9 status | Forge meaning |
|-----------|---------------|
| `APPROVED_FULL` | Preserve as approved templates/content |
| `PLACEHOLDER` | Ordinary template instance — content pending |
| `LEGAL_DEMO_DOCUMENT` | Full legal copy with DEMO tokens — replace before publish |

## Unpublished

- `/uslugi/genotipirovanie/` — **must not enter Forge intake**

## Social href="#" allowlist

Telegram, WhatsApp, Max, YouTube — operator supplies URLs in Forge.

## Forms

`FORM_MODE=STATIC_DEMO_NO_BACKEND` — replace with WordPress/backend in Forge phase.

## Rejected baseline

Do **not** use Phase 07C-B Storage static package as Forge input.

## Stable checkpoint (V9-03)

- Static frontend stable checkpoint **complete**
- Input baseline tag: `fp-0002-v9-operator-approved-static-frontend-stable-01`
- Forge must use V9 `src/` as implementation source; V9 `dist/` as rendered visual authority
- G6 must not be recreated; genotyping route remains excluded
- Legal DEMO tokens remain production blockers
- **Forge Intake Pack not yet created** — next phase V9-04

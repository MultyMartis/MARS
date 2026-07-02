# REPORT — FP-0002 V9 Phase 03G Scroll-to-Top

**Verdict:** PASS (pending operator visual review)  
**Phase:** V9-03G  
**Branch:** `mars/canonical-post-recovery`  
**HEAD:** `5e7c86db73398df6a01074a60af3afa796de41b3`  
**V9 status:** `FP0002_V9_03G_SCROLL_TO_TOP_COMPLETE_PENDING_OPERATOR_VISUAL_REVIEW`  
**Operator review:** Narrow scroll-to-top visual + modal regression — **pending**  
**Git checkpoint:** None (no stage / commit / tag / push)

## Preflight

| Check | Result |
|-------|--------|
| Drive `X:` | OK |
| Volume `AI WS` | OK |
| Repository `X:\AI MARS` | OK |
| V9 workspace | OK |
| V8 protection | Not modified |
| Triumph authority | Not modified |
| V9-03F modal present | OK |
| Preloader | Absent |
| G6 | Absent |

## Approved backup (before edits)

| Field | Value |
|-------|-------|
| Evidence | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03g-scroll-to-top\` |
| ZIP | `…\snapshot-approved-v9-03f-before-scroll-to-top\FP-0002-V9-03F-OPERATOR-APPROVED-PRE-SCROLL-TO-TOP.zip` |
| SHA-256 | `6E5092D2FCCA79ADA16B78BB14934A5E03432EEE21CD43937FEDD515E887D106` |
| Size | 484,766,736 bytes / 1938 files |
| Completed before source edits | **Yes** |

## Scroll-to-top architecture

| Item | Value |
|------|-------|
| Partial | `src/partials/components/scroll-to-top.html` |
| Include | `footer.html` (after `.site-page-shell` close) |
| Instances per route | **1** (31/31) |
| JS | append-only `initScrollToTop` in `src/js/main.js` |
| Threshold | 500px |
| Click | smooth scroll top; reduced-motion → instant |
| z-index | 900 |
| Desktop offset | 15px bottom-right + safe-area |
| Mobile offset | 10px bottom-right + safe-area |
| Icon | inline SVG |
| Accessible name | `Прокрутить страницу наверх` |

## Build

| Item | Value |
|------|-------|
| Command | `npm run build` |
| Result | **Succeeded** |
| Routes | 31 |
| CSS SHA-256 | `F89FCB86A678C5FB4D4A94DB2E423095A23564B6C3BE19D7E39CF5AF0D30ABDE` |
| JS SHA-256 | `19518C4BF86FBDA4FD5128D67EF00CBF7A2BDC6000A571B65D75BFA6AF27DB8A` |

## Validation

- Automated: **PASS** (`npm run validate`, port 8797)
- HTTP 31/31 routes: **200**
- Modal hash unchanged
- Preloader: absent
- G6: absent

## Preview

**http://127.0.0.1:8797/**

## Protected

- V9-03F modal runtime unchanged
- No preloader restoration
- No route/content changes
- No git checkpoint
- Storage evidence not committed

# iOS Lifebuoy — ownership map + root-cause analysis (PROD-P12)

## Chain (production, post-intake)

| Layer | Owner |
|-------|-------|
| DOM | `template-parts/layout/body-start.php` — `.fp02-lifebuoy-parallax` + mover + img |
| CSS layer | `assets/css/fp02-lifebuoy-parallax.css` |
| JS motion | `assets/js/fp02-lifebuoy-parallax.js` |
| Enqueue | `inc/assets.php` |
| Operator CSS | `v9-style.css` — **0** lifebuoy selectors (verified) |

## P08 attempt (historical)

P08 changed CSS-variable-only transform → dual-write CSS vars + **direct `img.style.transform`**.  
Claimed WebKit-safe. Real iPhone still reported static by Olya → treat as **not proven on device**.

## Root-cause analysis (bounded evidence)

Strongest multi-factor cause (not “Safari issue” alone):

1. **`contain: layout paint size` on `position: fixed` root**  
   Creates a size-contained fixed compositing context. iOS Safari historically fails to visually update descendant transforms inside such layers while scroll progresses — layer paints once and appears static.

2. **Transform applied on `<img>` inside that contained fixed root**  
   Image replaced-element + contain/paint interaction increases compositor freeze risk vs transforming a plain block wrapper.

3. **Mixed `%` + `vh` units inside the animated `translate3d(...)` string**  
   iOS dynamic viewport / scrollable chrome can leave `%`/`vh` transform matrices visually stale during momentum scrolling even when JS updates the string.

4. **Scroll source** relied primarily on `window.scrollY` without documentElement fallback / touchmove keep-alive (secondary risk on iOS momentum).

5. **Operator CSS did not override lifebuoy** (eliminated as primary cause after intake).

IOS LIFEBUOY ROOT-CAUSE ANALYSIS COMPLETE

## P12 fix — single transform ownership

- Markup: add `.fp02-lifebuoy-parallax__mover` wrapper (`data-fp02-lifebuoy-mover`).
- **JS is the sole animated transform owner** on the mover (`translate3d(px, px, 0) scale() rotate()`).
- CSS: soften contain to `contain: paint`; image `transform: none`; mover holds initial pose until first JS paint only.
- Scroll: `scrollY` / `pageYOffset` / `documentElement.scrollTop` fallbacks + passive `touchmove` → rAF.
- Reduced motion: freeze progress `t=0.28` preserved.

LIFEBUOY TRANSFORM OWNERSHIP = SINGLE AND PROVEN (code-level)  
WEBKIT/IOS-SAFE LIFEBUOY SCROLL ANIMATION IMPLEMENTED (static/WebKit-safe design)  
PHYSICAL IPHONE QA = OPERATOR/OLYA PENDING

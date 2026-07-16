# Preload / enqueue decision — V9-06E56-FU02

- Theme `inc/assets.php` does **not** preload Inter (or any) local fonts.
- Fonts load exclusively via CSS `@font-face` inside `v9-style.css`.
- Decision: **NO preload** for Libertinus Serif Regular.
- Rationale: match existing architecture; avoid inventing a new preload path; title font still loads via CSS with `font-display: swap`.
- `assets.php` left unchanged (source/runtime hash unchanged).

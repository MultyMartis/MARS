# E58-VA-001 — notes

## Recommendation
RECOMMEND CONFIRM — HIGH confidence

## Cause
V9 Home passes utility classes into partials:
- why-us: 
o-top-padding--30
- staff-photo / feature-grid: 
o-top-padding no-top-padding--30
- clinic-landscape: 
o-top-padding

WP partials still contain literal @@class from static include syntax and ront-page.php does not pass $args classes. CSS utilities exist in 9-style.css (lines ~357–363) but are never applied.

## Not operator CSS intentional
Protected operator CSS hash unchanged; this is a template port gap, not an accepted visual tweak.

## Smallest correction (DO NOT IMPLEMENT)
1. Replace @@class in Home partials with PHP class merge.
2. Pass the same V9 class strings from ront-page.php.
No new spacing tokens required.

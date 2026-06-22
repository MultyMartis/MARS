# Forge WordPress FW-05 — Lessons Learned v1

**Date:** 2026-06-22

---

## What worked

- Selective FW-04 git checkpoint isolated capability pack cleanly
- Gulp synthetic frontend built and validated without PHP stack
- Skill-driven architecture artifact chain before implementation
- Theme/plugin split with shared CSS/JS from dist
- Playwright reference captures at 1440/1024/390
- Independent validator reports with honest NOT EXECUTED markers
- Release RC1 packaging via project-local Node scripts

## What did not work fully

- Profile A (Local/Laragon) not available — full WP runtime proof deferred
- WordPress Playground CLI version opaque; automated mount/population not completed in FW-05
- PHPCS/php -l blocked without host PHP
- WP-rendered visual parity not captured

## Skills — gaps

- FW-SK-11 should explicitly branch validation when host PHP absent
- FW-SK-12 should document reference-only path when WP URL unavailable

## Validators — useful findings

- FW-V-02 caught need to mark PHPCS honestly
- FW-V-05 prevented false pixel parity claim
- FW-V-07 confirmed release manifest completeness

## Context load

- Full skill pack readable but heavy; context loading tiers worked when preflight declared scope

## Unsafe commands avoided

- No system-wide PHP/Docker/Local install
- No production or client site access

## Missing tools

- PHP, Composer, WP-CLI, PHPCS, Local, Docker, ACF Pro

## Standards / templates to refine before client pilot

- ACF Pro vs Free deviation template in implementation spec
- Playground vs Local profile selection checklist in FW-05 input
- Visual capture script output path validation

## Pre–client pilot requirements

1. Operator installs Profile A (Local or Laragon)
2. PHP + PHPCS project-local in workspace
3. ACF Pro license for options workflow if required
4. Operator WV6 sign-off on real WP render

---

*Lessons learned v1 — FW-05.*

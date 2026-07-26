# METALLKA — Local Mirror Decision v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26

---

## Decision

# DEFER

---

## Reasons (technical)

1. Operator confirmed staging/dev **not required** for current site-ops model.  
2. Architecture is a **standard single WordPress root** (not hybrid static+WP like some precedents).  
3. Docroot, theme/plugin inventory, and WPBakery ownership are now mapped enough for **bounded admin/file tasks** without a mirror.  
4. No production `.git` / build pipeline requiring local compile parity.  
5. Mirror would mainly help destructive experimentation — not justified while first tasks stay low-risk text edits.

Revisit only if future work needs bulk theme forks, risky plugin upgrades, or repeated destructive testing.

---

*Local Mirror Decision v1 · DEFER.*

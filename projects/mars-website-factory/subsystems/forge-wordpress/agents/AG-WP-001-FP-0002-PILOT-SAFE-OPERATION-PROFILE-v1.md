# AG-WP-001 — FP-0002 Pilot-Safe Operation Profile v1

**Document type:** Pilot-safe operation profile (preparatory)  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

**Current pilot state:** **LOCKED** — no approval tokens before FW-06B and pilot charter.

---

## Pre-authorized R0 candidate set (after unlock)

`wp.inspect.runtime` · `wp.inspect.frontend_handoff` · `wp.inspect.theme` · `wp.inspect.functionality_plugin` · `wp.inspect.plugin_state` · `wp.inspect.routes` · `wp.inspect.assets` · `wp.validate.php_syntax` · `wp.validate.core_checksums` · `wp.validate.database` · `wp.validate.routes`

---

## Review-required R1 (after unlock)

`wp.plan.implementation` · `wp.plan.theme_architecture` · `wp.plan.functionality_architecture` · `wp.plan.content_model` · `wp.plan.plugin_decisions` · `wp.plan.validation` · `wp.plan.rollback`

---

## Explicit-approval R2/R3 (after unlock — not auto-authorized)

`wp.scaffold.theme` · `wp.scaffold.functionality_plugin` · `wp.scaffold.tests` · `wp.change.apply_approved_source` · `wp.checkpoint.create` · local plugin activation · local option mutation · content-model application

---

## Blockers (unchanged)

```text
FP-0002 pilot: BLOCKED
FW-06B: WAITING
AG-WP-001 runtime: NOT ACTIVE
Production authority: NONE
```

---

*Pilot-safe profile v1 — preparatory only.*

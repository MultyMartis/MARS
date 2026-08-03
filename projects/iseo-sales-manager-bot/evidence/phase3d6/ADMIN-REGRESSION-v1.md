# ADMIN REGRESSION v1

Phase 3D.6 changed Admin.dev from 51 to **54** nodes without creating workflows. Existing Admin command surface remains registry-authorized; `/help` now advertises `/my_status` for public, moderator and Admin paths with HTML `<code>` formatting.

Regression acceptance:

- Harness **29/29 PASS**.
- `ai_enabled=false`; Operational has OpenRouter AI disabled and zero provider calls in harness.
- Operational.dev remains active with 36 nodes and sole Gmail intake.
- Sales-Manager-v2 remains inactive.
- Client auto-messages: 0; workflows created: 0.

No runtime implementation is claimed inside MARS; this document records external n8n evidence.

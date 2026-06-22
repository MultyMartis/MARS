# FWS-0001 — WordPress Architecture Decision v1

**Mode:** A — Custom theme + functionality plugin  
**Page builder:** None  
**ACF:** Free + Settings API fallback (ACF Pro not available)

## Rationale

Synthetic service site with CPT archive/single, curated fields, and static frontend parity. No flexible content builder. Taxonomy not required — service list is flat CPT.

## Boundaries

- Theme: presentation + template hierarchy
- Plugin: CPT `service`, meta registration, ACF fallback helpers
- No WPilot overlap

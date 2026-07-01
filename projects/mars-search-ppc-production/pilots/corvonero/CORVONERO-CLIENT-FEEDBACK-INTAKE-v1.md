# Corvonero client feedback intake v1

Reusable template for recording client feedback while project state is **CLIENT_FEEDBACK_PENDING**.

## Usage

1. Client sends corrections on ads, strategy HTML, landing copy, or commercial claims.
2. Operator creates one intake record per discrete change request in `CORVONERO-CLIENT-FEEDBACK-INTAKE-v1.json`.
3. Classify each item using the change classes below.
4. Mark downstream impacts before accepting any change that touches authority or deployable packages.

## Change classes

| Class | Typical impact |
|-------|----------------|
| `SPELLING_ONLY` | No authority/regeneration |
| `COPY_CHANGE` | May affect ads/landing only |
| `COMMERCIAL_CLAIM_CHANGE` | Requires client reconfirmation |
| `SERVICE_SCOPE_CHANGE` | Semantic + architecture review |
| `GEO_CHANGE` | Routing + negatives + ads |
| `LANDING_URL_CHANGE` | Ads + landing briefs |
| `GROUP_STRUCTURE_CHANGE` | Authority + Commander package |
| `KEYWORD_CHANGE` | Authority + Commander package |
| `UNKNOWN_REVIEW` | Operator triage required |

## Required fields

See `CORVONERO-CLIENT-FEEDBACK-INTAKE-v1.json` → `field_definitions`.

## Protected artifacts

Do not apply feedback by regenerating:

- `02-CORVONERO-CAMPAIGN-STRATEGY-AND-RESEARCH-v1.html` (MANUAL_STABLE)
- Client-sent XLSX/DOCX without explicit new version

## Current state

- **Entries:** 0 (awaiting client)
- **JSON:** `CORVONERO-CLIENT-FEEDBACK-INTAKE-v1.json`

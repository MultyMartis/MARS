# SAFE UNKNOWN Rules v1 — DOCX Pilot

## Definition

**SAFE UNKNOWN** marks content that is intentionally **not verified** at export time. The exporter must **preserve** and **highlight** these items — never invent replacements.

## Mandatory behaviors

| Rule | Implementation |
|------|----------------|
| Collect per-section UNKNOWN | Parser reads `### SAFE UNKNOWN` and inline `SAFE UNKNOWN` markers |
| Dedicated export section | `render-safe-unknown.js` — warning shading |
| Canonical fallbacks | Live URL, NAP, form endpoint, hourly rate if absent in pack |
| No auto-resolve | Exporter does not substitute production values |
| Factory handoff | UNKNOWN list repeated for implementer visibility |

## Canonical UNKNOWN categories (pilot)

1. **Live URLs** — canonical route not QA'd on production
2. **Final NAP** — phone/hours/address pending operator sign-off
3. **Form endpoint** — `action` URL unknown
4. **Exact pricing** — hourly RUB rate not approved for publication
5. **Review integrations** — widget URLs pending
6. **B2B tax/docs** — VAT wording pending confirmation

## Visual treatment

- Amber warning block (`#FFF3CD`)
- Numbered list in dedicated section
- Section-level UNKNOWN repeated under each section when present

## Operator responsibility

Only a **human operator** may clear an UNKNOWN by updating the source content pack and re-exporting. DOCX export does not clear gates or UNKNOWN state.

## Boundary

These rules are **documentation + render discipline** — not a validation engine. For pack validation, use project-specific QA outside this pilot.

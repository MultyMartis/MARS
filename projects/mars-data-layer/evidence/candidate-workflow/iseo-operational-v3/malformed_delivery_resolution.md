# Malformed delivery residual — resolution

## Finding (shadow import)

- One residual: `delivery_lead_card_malformed`
- Sheet row context: LEAD_DELIVERIES row historically polluted
- Content characteristic: HTTP webhook header dump written into delivery payload/text fields (not a valid lead card)

## Classification

**`LEGACY INVALID ROW`**

Not:

- `IMPORTER MAPPING DEFECT` (importer correctly preserved invalid historical cell content)
- `VALID PRODUCTION CASE NOT YET MODELED` (not a legitimate business delivery)

## Disposition

- Exclude permanently from v3 runtime correctness claims
- Do not treat as schema blocker for candidate acceptance
- Do not rewrite shadow historical row meaning in this wave
- Cutover prep may quarantine/exclude this delivery_id from projection/metrics

## Impact on v3 candidate

None on critical path. v3 writes structured JSON payloads via `enqueue_delivery` / commit function.

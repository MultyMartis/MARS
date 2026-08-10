# CANONICAL LEAD CARD RENDERER — v1

## Phase 3H.7.3.1 (2026-08-10)
- Verdict baseline: acceptance-card canonicalization + authoritative instance v1.1
- Root cause: callback status sync used reduced `buildFinalCard`; fixed to full canonical body
- Contract: `iseo-authoritative-card-instance-v1.1`
- Soak: new final 48h restarted (does not reuse 3H.7.3 T+0); Phase 3I.1 blocked; AI OFF
- Evidence: `evidence/phase3h731/`

Contract id: `iseo-canonical-lead-card-renderer-v1`

## Purpose

One human-facing Telegram lead-card renderer for:

- normal production intake;
- operator-resurfaced existing leads.

## Inputs

- authoritative lead object (LEADS / lead_clean fields);
- `manager_status` (`pending` | `processed` | `spam`);
- recipient profile (ACCESS_CONTROL reply sender fields);
- delivery context;
- optional internal `delivery_reason` (e.g. `operator_resurface`).

## Outputs

- production card text (`sm-msg-v2.4` via `formatLeadCard`);
- keyboard (pending Processed/Spam, or terminal Reopen);
- approved first-response draft + per-recipient personalization;
- manager guidance when applicable.

## Hard rules

1. Internal `delivery_reason` must not alter human-facing structure.
2. Never render `#ERROR!` / `#N/A` / `#VALUE!` / `#REF!` as contact.
3. Never render internal aliases (`REAL_REOPEN_*`) or `operator resurface` labels.
4. Prefer phone/email/messenger over derived `primary_contact`.
5. Module path: `implementation/runtime-libs/canonical-lead-card-renderer-v1.mjs`.

## Related

- `architecture/LEAD-CARD-INSTANCE-REGISTRY-v1.md`
- `architecture/TELEGRAM-UX-CONTRACT-v1.md`
- `architecture/MANAGER-CARD-v2.4-CONTRACT-v1.md`


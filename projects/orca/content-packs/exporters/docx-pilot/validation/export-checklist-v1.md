# Export Checklist v1 — DOCX Pilot

Operator completes after each human-triggered export.

## File integrity

- [ ] DOCX opens in Microsoft Word without repair dialog
- [ ] File size > 10 KB (non-empty document)
- [ ] Output path matches runbook: `output/triumph-manipulyator-5-tonn-pack-v1.docx`

## Structure

- [ ] Cover page present with project_id and route_id
- [ ] `export_version` and `generated_at` populated
- [ ] PPC continuity section present
- [ ] SEO continuity section present
- [ ] Sections **01 HERO** through **10 FINAL CTA** all present
- [ ] SAFE UNKNOWN dedicated section visible (warning styling)
- [ ] Factory implementation notes section present
- [ ] Approval section at end with three primary gates

## Semantic fidelity

- [ ] Hero H1: «Манипулятор 5 тонн в Краснодаре»
- [ ] Spec table values: 5 т / 3 т / 14 м / 6.2×2.2 / 2 часа
- [ ] Denied tasks include legkovye/evacuation filter
- [ ] No invented hourly rate in pricing section
- [ ] semantic lock visible on cover and per-section

## SAFE UNKNOWN

- [ ] Hourly rate marked unknown in pricing context
- [ ] Form endpoint unknown noted
- [ ] NAP/hours verification called out
- [ ] UNKNOWN not silently removed or replaced with guesses

## Approvals

- [ ] `approved_for_factory` matches pack snapshot
- [ ] `approved_for_ads` shows NOT approved (pilot pack default)
- [ ] `approved_for_launch` shows NOT approved
- [ ] Sign-off blank present; export did not auto-approve

## Encoding & claims

- [ ] Russian text readable — no mojibake (кракозябры)
- [ ] No fake review quotes, fleet size, or statistics added by exporter
- [ ] Phone `tel:+79004658331` preserved where in source

## Sign-off

| Role | Name | Date |
|------|------|------|
| Export operator | | |
| Factory reviewer | | |

**Fail-closed:** if any critical item fails, do not hand to Factory until pack MD fixed and re-exported.

# Operator Review Flow v0

## Purpose

Human review gates for landing content packs before export and Factory handoff.

## Review types

| Type | When | Outcome |
|------|------|---------|
| **Structural review** | Pack `draft` | Section order 01–10 complete |
| **Semantic review** | Pre-`approved` | Locks, denied tasks, PPC continuity |
| **Export review** | Pre-DOCX client send | DOCX matches pack; metadata correct |
| **Factory QA** | Post-build | HTML vs pack — MODE 1 continuity |
| **Ads readiness** | Pre-launch | `approved_for_ads` |

## Structural checklist

- [ ] All required sections present or omission documented
- [ ] `pack_id`, `route_slug`, `canonical_url` consistent
- [ ] `ppc_continuity` matches campaign instance
- [ ] `seo_continuity` H1 aligns with hero
- [ ] Each section has `section_purpose` + `ppc_continuity`

## Semantic checklist

- [ ] No fleet / autopark language (if single-machine page)
- [ ] Capability numbers consistent across sections
- [ ] Denied tasks align with FAQ
- [ ] No invented prices, stats, review quotes
- [ ] CTA hierarchy documented
- [ ] SAFE UNKNOWN list complete

## Continuity checklist (PPC)

- [ ] H1 ↔ ad headline 1
- [ ] Hero bullets ↔ ad description / callouts
- [ ] Price intent closed without fake tariff
- [ ] Messenger order documented (if applicable)

## Sign-off table

| Transition | Operator | Date | Notes file |
|------------|----------|------|------------|
| draft → reviewed | | | |
| reviewed → approved | | | |
| approved → factory-ready | | | `approved_for_factory` |
| export client DOCX | | | `approved_for_client_export` |
| ads ready | | | `approved_for_ads` |
| launch | | | `approved_for_launch` |

## AI assistance rules

- AI may **propose** edits in `draft` only
- AI **must not** set gates or `artifact_state`
- AI **must not** remove SAFE UNKNOWN without evidence path

## On failure

| Finding | Action |
|---------|--------|
| Lock breach in Factory HTML | Halt; file incident note; reconcile pack |
| Missing evidence | Mark SAFE UNKNOWN; block `approved_for_launch` |
| Drift vs Commander group | Fix pack or campaign instance — human decision |

## Boundary

Review flow documentation only.

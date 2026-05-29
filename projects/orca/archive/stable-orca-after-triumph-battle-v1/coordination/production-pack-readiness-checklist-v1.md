# Production Pack Readiness Checklist v1

**Use:** immediately before `approved_for_factory` and handoff issuance  
**Actor:** human operator (ORCA author signs; no auto-pass)  
**Pair with:** [factory-handoff-minimum-contract-v1.md](factory-handoff-minimum-contract-v1.md)

Mark **PASS** / **FAIL** / **N/A** / **WAIVED (operator initial + date)**.

---

## 1. Identity and routing

| # | Check | PASS criteria |
|---|-------|---------------|
| 1.1 | `route_id` matches `landing-route-registry.json` | Exact ID |
| 1.2 | `canonical_url` / slug correct | Matches registry `.html` paths (e.g. `/fbs-zhbi.html`) |
| 1.3 | `group_id` + campaign ref documented | Instance JSON cited |
| 1.4 | Blueprint path pinned | Not folder-only `landing-pages/` |
| 1.5 | V6 `factory_hints` partial paths | Under `triumph-manipulator-landing-v6` |

---

## 2. Route alignment

| # | Check | PASS criteria |
|---|-------|---------------|
| 2.1 | `page_intent` matches blueprint PAGE PURPOSE | No merged intents |
| 2.2 | Positioning locks table complete | No fleet / fake price |
| 2.3 | Differentiation vs zakaz documented | For non-master routes |
| 2.4 | Denied tasks present | Route-specific |
| 2.5 | Negative space (anti-junk) explicit | Evacuation, oversize, etc. |

---

## 3. H1 alignment

| # | Check | PASS criteria |
|---|-------|---------------|
| 3.1 | H1 matches `primary_ad_variant` | Table in `ppc/ad-alignment.md` |
| 3.2 | Multi-ad strategy resolved or WAIVED | No open D2-class gap |
| 3.3 | Title / meta description aligned | No contradictory intent |
| 3.4 | Case / typography notes for Factory | `&nbsp;` locks if needed |

---

## 4. CTA alignment

| # | Check | PASS criteria |
|---|-------|---------------|
| 4.1 | `cta_priority` set (form vs call) | Matches PPC instance |
| 4.2 | Primary label locked 🔒 | Exact RU string |
| 4.3 | `cta_surface_priority[]` documented | Hero, FAQ, modal |
| 4.4 | `data-form-id` naming convention noted | Per V6 rules |
| 4.5 | ≤2 primary red CTAs in hero viewport | Per density doc |

---

## 5. FAQ integrity

| # | Check | PASS criteria |
|---|-------|---------------|
| 5.1 | FAQ count matches blueprint minimum | No empty FAQ |
| 5.2 | Answers do not invent pricing | По задаче framing |
| 5.3 | No contradiction with denied tasks | Cross-read |
| 5.4 | Objection handling for route intent | Use-case / B2B / geo specific |

---

## 6. Proof integrity

| # | Check | PASS criteria |
|---|-------|---------------|
| 6.1 | `trust_mode` + `proof_mode` set | |
| 6.2 | No invented review counts / stars | Evidence or operational wording |
| 6.3 | Review sources named if claimed | Yandex / Avito etc. |
| 6.4 | Hero proof strip items evidenced | No fleet metrics |
| 6.5 | `drift_acceptance.destructive` empty or waived | Operator sign-off |

---

## 7. Trust integrity

| # | Check | PASS criteria |
|---|-------|---------------|
| 7.1 | Trust section copy locked | `content/trust.md` |
| 7.2 | B2B block only when relevant | yurlic / master — not noise on narrow use-case |
| 7.3 | Legal entity references accurate | **UNKNOWN** marked if not verified |
| 7.4 | No aggregator positioning | Practical operator framing |

---

## 8. Density safe

| # | Check | PASS criteria |
|---|-------|---------------|
| 8.1 | `visual_density` tier assigned | |
| 8.2 | `cargo_cards_max` enforced in hero draft | |
| 8.3 | Hero message budget counted | Within [semantic-density-control-v1.md](semantic-density-control-v1.md) |
| 8.4 | `hero_layout_mode` specified | Typically `grid_form_aside` |
| 8.5 | No v4 destructive patterns in draft | Rate block, fleet features |

---

## 9. Mobile critical

| # | Check | PASS criteria |
|---|-------|---------------|
| 9.1 | `mobile_critical[]` populated | From mobile-criticality rules |
| 9.2 | Known risks documented | Form below fold, call-first, etc. |
| 9.3 | Factory QA device checklist attached or scheduled | Not «UNKNOWN» silently |
| 9.4 | Cargo mobile cap noted if different from desktop | |

---

## 10. No fake claims

| # | Check | PASS criteria |
|---|-------|---------------|
| 10.1 | `SAFE-UNKNOWN.md` complete | No silent invention |
| 10.2 | Tonnage / reach numbers match machine lock | 5/3/14 or route exception |
| 10.3 | Geography claims bounded | Krasnodar / kray — not Russia-wide |
| 10.4 | Speed / guarantee claims evidenced or absent | |
| 10.5 | `claims_forbidden[]` in semantic lock | |

---

## 11. No semantic conflicts

| # | Check | PASS criteria |
|---|-------|---------------|
| 11.1 | PPC continuity table filled | |
| 11.2 | Specs ↔ hero ↔ tasks aligned | |
| 11.3 | Pricing ↔ FAQ aligned | |
| 11.4 | Visual semantics ↔ content slots aligned | |
| 11.5 | `semantic_lock: active` preconditions met | See pack `factory/semantic-lock.md` |
| 11.6 | `approved_for_factory` ready to set | Human only |

---

## 12. Handoff readiness

| # | Check | PASS criteria |
|---|-------|---------------|
| 12.1 | Minimum contract fields prepared | [factory-handoff-minimum-contract-v1.md](factory-handoff-minimum-contract-v1.md) |
| 12.2 | `content_mode: MODE_1` | |
| 12.3 | Pack version + date | |
| 12.4 | Matrix row updated | [remaining-routes-status-matrix-v1.md](remaining-routes-status-matrix-v1.md) |

---

## Verdict

| Result | Action |
|--------|--------|
| **READY** | Set `approved_for_factory: true` → issue handoff → Factory pilot |
| **NOT READY** | Fix FAIL items; bump pack version |
| **READY WITH WAIVERS** | Document each waiver in `APPROVALS.md` — not for destructive drift |

---

## Related

- [orca-factory-coordination-protocol-v1.md](orca-factory-coordination-protocol-v1.md)
- [semantic-pack-generation-system-v1.md](semantic-pack-generation-system-v1.md)

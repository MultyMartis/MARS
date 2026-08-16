# Forge Proger Capability Backlog — After FP-0002

**Status:** backlog only — not scheduled implementation  
**Source:** Phase 1 + Phase 2 experience (especially E54–E63)

Automation levels: `manual` | `assisted` | `semi-auto` (always human-gated for product accept).

---

## High priority

| Capability | Problem solved | FP-0002 evidence | Inputs → outputs | Automation | Human supervision | Priority |
|------------|----------------|------------------|------------------|------------|-------------------|----------|
| Runtime/operator canon detector | Missed RUNTIME_AHEAD overwrites | E56–E63 hash promotes | paths → drift report + promote plan | assisted | classify legitimacy | **H** |
| Exact source/runtime promotion tool | Manual copy errors | E63 3-file promote | file list → hashed promote receipt | semi-auto | approve list | **H** |
| Git exact-allowlist release tool | Dirty monorepo commit risk | E63 798-path allowlist | path roots → allowlist + exclude WIP | assisted | review allowlist | **H** |
| Pre-release tail ledger generator | Silent open tails | E61→E63 | reports/status → ledger MD | assisted | dispositions | **H** |
| Nested-section detector | Invalid CTA nesting | E61/E62C | route HTML → violations | assisted | fix decision | **H** |
| Stable repeater UID utility | Index anchors break | E62B→E62C | repeater rows → UID ensure | semi-auto | confirm model | **H** |
| Backup retention classifier | Disk / wrong deletes | 15GB backup root | backup dirs → class+action | assisted | approve deletes | **H** |

## Medium priority

| Capability | Problem solved | Evidence | Inputs → outputs | Automation | Human | Priority |
|------------|----------------|----------|------------------|------------|-------|----------|
| ACF ownership mapper | Page vs block confusion | E61–E62D | groups+partials → matrix | assisted | design ownership | M |
| Admin field-group auditor | Legacy groups visible | E62C hide | CPT/role → visibility report | assisted | hide vs delete | M |
| Reusable-block ownership validator | Duplicate Blog fields | E61 | FE strings → owner map | assisted | simplify admin | M |
| Duplicate-ID scanner | Anchor/DOM bugs | E63 dup-ID 0 check | routes → ID collisions | semi-auto | fix | M |
| Responsive screenshot/evidence runner | Incomplete packs | E61 gap; E62C/E63 packs | routes+viewports → PNG set | semi-auto | visual accept | M |
| Figma/reference comparison workflow | False-positive audits | E58 FU01 | frames+screens → decision board | assisted | confirm/reject | M |
| WordPress search baseline generator | Ad-hoc search UX | E62E/FIX01 | theme hooks → baseline checklist | assisted | trigger placement | M |
| Safe cleanup planner | Destructive mistakes | this Phase 2 | inventory → staged plan | assisted | charter | M |
| Pagination canonical validator | SEO pagination drift | E62B | archive URLs → canonical checks | assisted | approve | M |

## Deferred / later

| Capability | Problem solved | Evidence | Notes | Priority |
|------------|----------------|----------|-------|----------|
| Production launch assistant | SMTP/indexing/URL replace | Deferred work list | After first real production | D |
| Advanced search relevance tooling | Custom-field search | E62E deferred | Not needed for Stable | D |

---

## Guidance

- Do **not** implement these into Forge Proger brains from this doc alone.
- Prefer thin assisted tools with receipts over autonomous “fixers.”
- Every capability that mutates product requires MARS preflight + backup gate.

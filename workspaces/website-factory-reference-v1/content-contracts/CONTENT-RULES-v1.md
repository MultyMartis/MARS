# Website Factory — Content Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** architecture gates for Content Layer — **documentation only**  
**Связь:** [CONTENT-SYSTEM-v1.md](CONTENT-SYSTEM-v1.md)

**Не является:** automated linter, CMS validation plugin, copy style guide.

---

## Severity legend

| Level | Meaning |
|-------|---------|
| **CRITICAL** | Halt — no content binding / fill until resolved |
| **ERROR** | Must fix before production content gate |
| **WARNING** | Document operator exception |

---

## Rules

### Chain and taxonomy

| ID | Rule | Severity |
|----|------|----------|
| CT-R01 | **Content follows Blueprint** — signals and block stacks must align with active Blueprint IA and exclusions | CRITICAL |
| CT-R02 | **Content follows Page Architecture** — only allowed `page_type` for `site_type_code` | CRITICAL |
| CT-R03 | **Content follows Block Registry** — only 29 v1 `block_id`; signals bind to existing blocks | CRITICAL |
| CT-R04 | **Content cannot violate Validation** — do not bind content to FAIL/CRITICAL page-block validation | CRITICAL |
| CT-R05 | **No new taxonomy in Content workstream** — no new `site_type_code`, `page_type`, `block_id`, or `signal_id` | CRITICAL |

### Upstream layers

| ID | Rule | Severity |
|----|------|----------|
| CT-R06 | **Content follows SEO intent** — page-level signals must not contradict PAGE-SEO-CONTRACT and search intent mix | ERROR |
| CT-R07 | **Content follows Design contract** — required signals must be expressible within selected `VF_*` pattern role | ERROR |
| CT-R08 | **Design subordinate to forbidden blocks** — no signals that imply FORBIDDEN blocks on page | CRITICAL |

### Legal and entity

| ID | Rule | Severity |
|----|------|----------|
| CT-R09 | **LEGAL_PAGE follows Legal Pack** — only `legal_disclosure` + `entity_identity`; marketing signals forbidden | CRITICAL |
| CT-R10 | **Forms require Consent Rule** — `consent` signal mandatory on LEAD_FORM / CHECKOUT instances | CRITICAL |
| CT-R11 | **NAP follows Legal Entity Card** — `contact`, `location`, `entity_identity` must match discovery output | ERROR |
| CT-R12 | **LEGAL_LINKS in production** — footer/legal link signals reference frozen Legal Pack documents | ERROR |

### Truth and evidence

| ID | Rule | Severity |
|----|------|----------|
| CT-R13 | **No unsupported claims** — proof, `certificate`, `guarantee`, `experience` require evidence_rule satisfaction | CRITICAL |
| CT-R14 | **No invented facts** — statistics, awards, client names, regulatory status | CRITICAL |
| CT-R15 | **No fake reviews** — `review` signal requires UGC_AUTHENTIC; curated quotes use TESTIMONIALS with HITL | CRITICAL |
| CT-R16 | **No fake statistics** — metrics in `proof` must be SOURCE_DOCUMENTED | CRITICAL |
| CT-R17 | **No placeholder leakage** — template tokens, lorem, `TBD`, `[COMPANY]` in production-bound slots | ERROR |
| CT-R18 | **Urgency requires source** — `urgency` only with SOURCE_DOCUMENTED deadline/stock rule | ERROR |

### Conversion discipline

| ID | Rule | Severity |
|----|------|----------|
| CT-R19 | **One primary conversion per page** — align with BLOCK-CONVERSION-ROLES; HITL on conflict | ERROR |
| CT-R20 | **Commerce path matches site type** — CATALOG: no `payment`; ECOMMERCE: no RFQ-only PDP without charter | CRITICAL |
| CT-R21 | **Price signal matches model** — RFQ stance vs listed `price` documented per Blueprint | ERROR |

### Scope boundaries

| ID | Rule | Severity |
|----|------|----------|
| CT-R22 | **No copywriting in Content Layer v1** — contracts define signals only | CRITICAL |
| CT-R23 | **No SEO text creation** — meta/keywords out of scope | CRITICAL |
| CT-R24 | **No prompts or generation** — defer to Generation Contracts (not queued) | CRITICAL |
| CT-R25 | **No runtime** — Content Layer is documentation; no content engine claimed | CRITICAL |

---

## Pre-flight checklist (human-operated)

1. Confirm foundation + Legal Pack gates.
2. Run Page Block Validation (manual) — not FAIL/CRITICAL.
3. Resolve `site_type_code`, Blueprint, `page_type`, block stack.
4. Apply SITE-TYPE-CONTENT-MAPPING profile.
5. Apply PAGE-CONTENT-CONTRACTS profile.
6. For each REQUIRED `block_id` — apply BLOCK-CONTENT-CONTRACTS.
7. Cross-check Design `VF_*` selection.
8. Cross-check SEO page role.
9. Document HITL evidence for proof/trust/commerce signals.
10. **Stop** if generation/copy requested — register in CONTENT-GAPS-v1.

---

## SAFE UNKNOWN

- Automated enforcement of CT-R* — **FUTURE**
- Locale-specific evidence rules — **FUTURE**

---

*Content Rules version: v1.*

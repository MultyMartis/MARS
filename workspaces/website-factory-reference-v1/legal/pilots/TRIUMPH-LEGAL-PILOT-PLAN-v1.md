# Triumph Manipulator — Legal Pack Pilot Plan v1

**Версия:** v1  
**Статус:** preparation only — **NO page generation in this document**  
**Site type:** `LANDING` (PPC landing program)  
**Legal architecture:** [LEGAL-PACK-ARCHITECTURE-v1.md](../LEGAL-PACK-ARCHITECTURE-v1.md)  
**Generation contract:** [LEGAL-GENERATION-CONTRACT-v1.md](../LEGAL-GENERATION-CONTRACT-v1.md)

---

## Pilot goal

First **production validation** of Website Factory Core Legal Pack (L1–L4) on a real client project — Triumph Manipulator — using canonical templates with full placeholder replacement, Footer Rule, and Consent Rule compliance.

**Success =** legal pages deployable to production with LEGAL-GENERATION-CONTRACT Phase 3 **PASS**.

---

## Scope

| In scope | Out of scope |
|----------|--------------|
| Core Legal Pack L1–L4 | Extension Packs (ECOMMERCE, SAAS, MARKETPLACE) |
| Variable substitution | Legal text rewrite / paraphrasing |
| URL + footer + consent validation | Non-legal page content changes |
| Production readiness checklist | Mobile App Factory |

---

## Target workspace (candidate)

| Field | Value |
|-------|-------|
| **Primary candidate** | `workspaces/triumph-manipulator-landing-v6/` |
| **Site type** | `LANDING` |
| **Operator confirmation** | **REQUIRED** — v5 vs v6 vs other deploy target |

**Pre-pilot audit findings (v6):**

- Consent Rule HTML on forms — **already canonical** ✓
- Footer legal block — **partial drift**: link `/cookies/` + text «Cookie файлы» vs required `/cookie-files-policy/` + «Политика Cookie-файлов»
- Requisites in footer (ИНН, ОГРН) — present; not in Core template body

---

## Required inputs (operator / client)

Operator must provide **Legal Input Sheet** before generation:

| Variable | Required | Triumph source (to confirm) |
|----------|:--------:|----------------------------|
| `{{company_name}}` | ✓ | e.g. ООО «…» / ТК «Триумф» — **operator confirm legal entity name** |
| `{{domain}}` | ✓ | Production domain — e.g. `manipulator-triumph.ru` or deploy domain |
| `{{email}}` | ✓ | e.g. `info@manipulator-triumph.ru` — **confirm** |
| `{{privacy_policy_url}}` | ✓ | `https://{{domain}}/privacy-policy/` |
| `{{consent_personal_data_url}}` | ✓ | `https://{{domain}}/consent-personal-data/` |
| `{{phone}}` | Optional | `+7 (918) 991-29-91` — if added to pages |
| `{{address}}` | Optional | Краснодар — if added to pages |
| `{{inn}}` | Optional | `5009114932` (visible in v6 footer) |
| `{{ogrn}}` | Optional | `1185027010321` (visible in v6 footer) |

**Historical reference (removed from templates):** `gruzotaxi-triumph.ru`, `info@gktriumph.ru` — **must not** appear in output.

---

## Required variables (production minimum)

Per [LEGAL-GENERATION-CONTRACT-v1.md](../LEGAL-GENERATION-CONTRACT-v1.md):

**FAIL if unresolved at production:**

- `{{company_name}}`
- `{{domain}}`
- `{{email}}`
- `{{phone}}` — if inserted anywhere in legal pages
- `{{address}}` — if inserted
- `{{inn}}` — if inserted
- `{{ogrn}}` — if inserted
- `{{privacy_policy_url}}`
- `{{consent_personal_data_url}}`

---

## Expected outputs (when pilot executes)

| Output | Path (conventional) | Source template |
|--------|---------------------|-----------------|
| Privacy Policy page | `/privacy-policy/` | `privacy-policy-template.md` |
| Consent page | `/consent-personal-data/` | `consent-personal-data-template.md` |
| User Agreement page | `/user-agreement/` | `user-agreement-template.md` |
| Cookie Policy page | `/cookie-files-policy/` | `cookie-files-policy-template.md` |
| Footer legal links | All landing footers | LEGAL-IMPLEMENTATION-RULES §3 |
| Form consent markup | All lead forms | LEGAL-IMPLEMENTATION-RULES §4 |

**Format:** HTML pages in project `src/pages/` (or project convention) — **exact structure TBD at execution**.

---

## Validation checklist (pre-production)

### A. Placeholder scan — **FAIL on any match**

- [ ] No `{{company_name}}`
- [ ] No `{{domain}}`
- [ ] No `{{email}}`
- [ ] No `{{phone}}`
- [ ] No `{{address}}`
- [ ] No `{{inn}}`
- [ ] No `{{ogrn}}`
- [ ] No other `{{...}}`

### B. URL canon

- [ ] `/privacy-policy/` live
- [ ] `/consent-personal-data/` live
- [ ] `/user-agreement/` live
- [ ] `/cookie-files-policy/` live
- [ ] No legacy `/cookies/` in production footer

### C. H1 = footer text

- [ ] Политика конфиденциальности
- [ ] Согласие на обработку персональных данных
- [ ] Пользовательское соглашение
- [ ] Политика Cookie-файлов

### D. Consent Rule (all forms)

- [ ] Exact canonical HTML — no paraphrasing
- [ ] Links: `/consent-personal-data/`, `/privacy-policy/`
- [ ] `&nbsp;` preserved in production markup

### E. Cross-links inside legal pages

- [ ] L1 → L2, L4
- [ ] L2 → L1
- [ ] L4 → L1, L2

### F. Client data leak scan

- [ ] No `gruzotaxi`, `gktriumph`, wrong-domain emails
- [ ] No other client placeholders

---

## Acceptance criteria

| # | Criterion | Required |
|---|-----------|:--------:|
| 1 | All 4 legal pages generated from canonical templates | ✓ |
| 2 | LEGAL-GENERATION-CONTRACT Phase 3 PASS | ✓ |
| 3 | Footer Rule — 4 links, correct text and URLs on all production footers | ✓ |
| 4 | Consent Rule — exact text on every ПДn form | ✓ |
| 5 | Site type LANDING mapping satisfied — [SITE-TYPE-LEGAL-MAPPING-v2.md](../SITE-TYPE-LEGAL-MAPPING-v2.md) | ✓ |
| 6 | Operator sign-off on legal entity name and domain | ✓ |
| 7 | No Extension Pack documents required (LANDING) | ✓ |

**Pilot complete** when criteria 1–7 met and production deploy authorized by operator.

---

## Execution phases (future — not now)

| Phase | Action | Owner |
|-------|--------|-------|
| **0** | Operator confirms target workspace + Legal Input Sheet | Human |
| **1** | Generate 4 pages from templates + substitution | Human / agent (charter) |
| **2** | Fix footer `/cookies/` → `/cookie-files-policy/` + link text | Human / agent |
| **3** | Run validation checklist A–F | Human |
| **4** | Operator production sign-off | Human |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Wrong legal entity name | Operator confirms `{{company_name}}` against registration docs |
| Domain mismatch (staging vs prod) | Separate variable sets per environment; prod gate on prod domain |
| L4 tone mismatch for landing | Accepted for pilot; note in [LEGAL-TEMPLATE-REVIEW-v1.md](../LEGAL-TEMPLATE-REVIEW-v1.md) |
| v6 multi-footer variants (PPC pages) | Scan **all** footer partials, not only main landing |

---

## SAFE UNKNOWN

- Which Triumph workspace version is production deploy target — **operator confirm**.
- Whether legal pages need PHP wrapper / static HTML only — **project convention UNKNOWN**.
- Licensed legal review for Triumph — **not scheduled** in pilot plan.

---

*Pilot plan version: v1. Location: `workspaces/website-factory-reference-v1/legal/pilots/`.*

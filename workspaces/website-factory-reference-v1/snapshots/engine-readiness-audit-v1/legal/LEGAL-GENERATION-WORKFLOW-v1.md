# Website Factory — Legal Generation Workflow v1

**Версия:** v1  
**Область:** human-operated production workflow для Core Legal Pack L1–L4  
**Статус:** documentation only — **не** orchestration engine, **не** CI pipeline

**Связанные документы:**

| Документ | Роль в workflow |
|----------|-----------------|
| [LEGAL-INPUT-SHEET-v1.md](LEGAL-INPUT-SHEET-v1.md) | Input contract schema |
| [LEGAL-INPUT-SHEET-TEMPLATE-v1.md](LEGAL-INPUT-SHEET-TEMPLATE-v1.md) | Fillable template |
| [LEGAL-INPUT-INSTRUCTIONS-v1.md](LEGAL-INPUT-INSTRUCTIONS-v1.md) | Operator guide |
| [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) | Production gate |
| [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md) | Footer, Consent, H1 |
| [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md) | Variable names |
| [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | Site type codes |
| [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md) | Requirements matrix |
| [LEGAL-ENTITY-WORKFLOW-v1.md](../legal-entity/LEGAL-ENTITY-WORKFLOW-v1.md) | Discovery → card (upstream) |
| [LEGAL-ENTITY-CARD-v1.md](../legal-entity/LEGAL-ENTITY-CARD-v1.md) | Entity data before Input Sheet |

**Out of scope:** Mobile App Factory (FUTURE separate factory), Extension Pack auto-generation (FUTURE).

---

## Workflow Overview

```text
0. Legal Entity Discovery → Legal Entity Card (READY)
        ↓
1. Select Site Type
        ↓
2. Create Legal Input Sheet (from card)
        ↓
3. Validate Input Sheet
        ↓
4. Generate Legal Pages
        ↓
5. Validate Placeholders
        ↓
6. Validate Footer Links
        ↓
7. Validate Consent Links
        ↓
8. Production Sign-Off
```

---

## Step 0 — Legal Entity Discovery (upstream)

| Action | Owner | Output |
|--------|-------|--------|
| Prepare `project-input/legal-entity/` | Human | Source documents (P1) |
| Extract → Legal Entity Card | Human / agent | Draft card |
| Validate + resolve conflicts | Human | Card READY or CONFLICT |
| Operator verify card | Human | `operator_verified = true` |

**Gate:** `company_name` and `legal_name` **must not** be UNKNOWN on verified card.  
**Reference:** [LEGAL-ENTITY-WORKFLOW-v1.md](../legal-entity/LEGAL-ENTITY-WORKFLOW-v1.md) Steps 1–5.

**Fail:** skip to Input Sheet from footer only (Triumph-class drift).

---

## Step 1 — Select Site Type

| Action | Owner | Output |
|--------|-------|--------|
| Определить `site_type_code` из approved 8 | Human | Selected site type |
| Проверить applicable legal requirements | Human | Mapping row from SITE-TYPE-LEGAL-MAPPING-v2 |

**Gate:** site type **must** exist in [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md).  
**Fail:** unknown or custom site type without human charter.

---

## Step 2 — Create Legal Input Sheet

| Action | Owner | Output |
|--------|-------|--------|
| Confirm Legal Entity Card READY | Human | Verified card |
| Copy LEGAL-INPUT-SHEET-TEMPLATE-v1 | Human | Project-specific Input Sheet |
| Copy identity + entity fields **from card only** | Human | No parallel discovery |
| Fill domain, address_status, cookie inventory, meta | Human / client data | Completed draft |
| Record `card_id` in notes | Human | Traceability |

**Reference:** [LEGAL-INPUT-INSTRUCTIONS-v1.md](LEGAL-INPUT-INSTRUCTIONS-v1.md)

---

## Step 3 — Validate Input Sheet

| Action | Owner | Pass criteria |
|--------|-------|---------------|
| Schema validation per LEGAL-INPUT-SHEET-v1 | Human | All Required fields filled or documented UNKNOWN |
| Site type ↔ mapping check | Human | L1–L4 requirements understood |
| Operator sign-off | Human | Name, date, authorization = yes |
| Block if UNKNOWN on generation-critical fields | Human | `company_name`, `domain`, `email` must not be UNKNOWN |

**Gate:** **STOP** if sign-off missing or critical fields UNKNOWN.

---

## Step 4 — Generate Legal Pages

| Action | Owner | Output |
|--------|-------|--------|
| Copy canonical templates L1–L4 | Human / charter agent | Draft pages in project |
| Substitute variables from signed Input Sheet only | Human / charter agent | Rendered content |
| Create routes: `/privacy-policy/`, `/consent-personal-data/`, `/user-agreement/`, `/cookie-files-policy/` | Human / charter agent | Project pages |

**Rules:**

- Source templates: `privacy-policy-template.md`, `consent-personal-data-template.md`, `user-agreement-template.md`, `cookie-files-policy-template.md`
- **Forbidden:** AI paraphrasing, alternative consent text, alternative URLs
- Variables: [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md) only

---

## Step 5 — Validate Placeholders

| Action | Owner | Pass criteria |
|--------|-------|---------------|
| Scan production output for forbidden placeholders | Human | Zero `{{company_name}}`, `{{domain}}`, `{{email}}`, `{{phone}}`, `{{address}}`, `{{inn}}`, `{{ogrn}}` |
| Scan for any remaining `{{...}}` | Human | Zero unresolved |
| H1 canonical check | Human | Four pages match LEGAL-IMPLEMENTATION-RULES §5 |
| Client data leak scan | Human | No wrong-domain / legacy client strings |

**Reference scan (example):**

```powershell
Select-String -Path ".\src\pages\legal\*" -Pattern '\{\{(company_name|domain|email|phone|address|inn|ogrn)\}\}'
Select-String -Path ".\src\pages\legal\*" -Pattern '\{\{[^}]+\}\}'
```

**Gate:** any match = **Production Release FAIL**.

---

## Step 6 — Validate Footer Links

| Action | Owner | Pass criteria |
|--------|-------|---------------|
| Scan **all** footer partials (including PPC variants) | Human | Four links present |
| URL check | Human | Exact paths per Footer Rule §3 |
| Text check | Human | Link text = H1 of target page |

| Required text | Required URL |
|---------------|--------------|
| Политика конфиденциальности | `/privacy-policy/` |
| Согласие на обработку персональных данных | `/consent-personal-data/` |
| Пользовательское соглашение | `/user-agreement/` |
| Политика Cookie-файлов | `/cookie-files-policy/` |

**Gate:** drift (e.g. `/cookies/`, «Cookie файлы») = **FAIL**.

---

## Step 7 — Validate Consent Links

| Action | Owner | Pass criteria |
|--------|-------|---------------|
| Scan all forms collecting PD | Human | Consent Rule HTML exact match |
| Link targets | Human | `/consent-personal-data/`, `/privacy-policy/` |
| Markup | Human | `&nbsp;` preserved per canon |

**Canonical text:** [LEGAL-IMPLEMENTATION-RULES.md §4](LEGAL-IMPLEMENTATION-RULES.md) — единственный источник формулировки.

**Gate:** any paraphrasing or wrong URL = **FAIL**.

---

## Step 8 — Production Sign-Off

| Action | Owner | Output |
|--------|-------|--------|
| Consolidate Steps 5–7 results | Human | PASS / FAIL report |
| Record Input Sheet ID in release log | Human | Audit trail |
| Authorize or block deploy | Human (operator) | Production decision |

| Result | Action |
|--------|--------|
| **PASS** | All checks green → production deploy allowed |
| **FAIL** | Block release → fix → re-run Steps 4–7 as needed |

---

## Workflow Constraints (Validation)

| Constraint | Status |
|------------|--------|
| Only 8 approved site types | Enforced at Step 1 |
| Only Core L1–L4 document types | Enforced at Step 4 |
| No new factories | Website Factory only; Mobile App Factory = FUTURE |
| No automated orchestration | Human-operated steps throughout |

---

## SAFE UNKNOWN

- Workflow automation / CLI tool — **not implemented** v1.
- Integration with mars-survivability validators — **documentation reference only**.
- Extension Pack generation steps — **FUTURE** addendum when templates exist.

---

*Workflow version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*

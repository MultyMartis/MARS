# Website Factory — Legal Entity Workflow v1

**Версия:** v1  
**Область:** human-operated workflow — **documentation only**  
**Не является:** orchestration engine, CI pipeline, OCR product

---

## Workflow Overview

```text
0. Project charter + workspace exist
        ↓
1. Prepare project-input/legal-entity/
        ↓
2. Discovery (priority rules P1–P6)
        ↓
3. Extraction → draft LEGAL-ENTITY-CARD-v1
        ↓
4. Validation (format + conflicts)
        ↓
5. Operator verify card (operator_verified = true)
        ↓
6. Populate Legal Input Sheet FROM card
        ↓
7. Legal Input Sheet sign-off
        ↓
8. Legal Generation (L1–L4) — existing workflow
```

**Связь с Legal Generation:** шаги 6–8 — [LEGAL-GENERATION-WORKFLOW-v1.md](../legal/LEGAL-GENERATION-WORKFLOW-v1.md).

---

## Step 0 — Project charter

| Action | Owner | Output |
|--------|-------|--------|
| Подтвердить client workspace path | Human | `workspace_path` |
| Подтвердить site type (approved 8) | Human | Site type for later Input Sheet |
| **Не** начинать legal generation без card path | Human | Charter note |

---

## Step 1 — Prepare input folder

| Action | Owner | Output |
|--------|-------|--------|
| Создать `project-input/legal-entity/` | Human | Empty or populated folder |
| Разместить PDF/DOCX/EGRUL/bank/scan sources | Human / client | Source files |
| Именовать файлы описательно | Human | Audit-friendly names |

**Reference:** [LEGAL-ENTITY-INPUT-STANDARD-v1.md](LEGAL-ENTITY-INPUT-STANDARD-v1.md)

---

## Step 2 — Discovery

| Action | Owner | Output |
|--------|-------|--------|
| Сканировать P1 `project-input/legal-entity/` | Human / agent | Primary source list |
| При отсутствии P1 — эскалация: запросить документы у клиента | Human | Ticket / notes |
| Только при отсутствии P1–P2: читать P3 project docs | Human / agent | Secondary signals |
| P4 footer / P5 content — **signals only**, не auto-fill card | Human / agent | Candidate values + low confidence |
| P6 — operator confirmation для production-critical fields | Human | Verified values |

**Rules:** [LEGAL-ENTITY-DISCOVERY-RULES-v1.md](LEGAL-ENTITY-DISCOVERY-RULES-v1.md)

---

## Step 3 — Extraction

| Action | Owner | Output |
|--------|-------|--------|
| Copy LEGAL-ENTITY-CARD-TEMPLATE-v1 | Human / agent | Project card file |
| Extract per [LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md](LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md) | Human / agent | Draft card |
| Заполнить `source_document`, `source_priority`, `confidence_level` per field | Human / agent | Traceable card |
| **Не** писать в templates/footer/input sheet | — | Invariant |

**Output artifact:** `LEGAL-ENTITY-CARD` (Markdown) в project workspace, напр.:

```text
workspaces/<client>/legal/<project>-LEGAL-ENTITY-CARD-v1.md
```

или

```text
workspaces/<client>/project-input/legal-entity/<project>-card-v1.md
```

**Per charter** — путь фиксируется один раз на проект.

---

## Step 4 — Validation

| Action | Owner | Output |
|--------|-------|--------|
| Format checks (INN, OGRN, KPP, BIK) | Human / agent | Pass / Fail |
| Conflict detection across sources | Human / agent | Conflict report if needed |
| Set `card_status` | Human / agent | `DRAFT` \| `CONFLICT` \| `NOT_READY` |

**Reference:** [LEGAL-ENTITY-VALIDATION-RULES-v1.md](LEGAL-ENTITY-VALIDATION-RULES-v1.md)

**Gate:** конфликты по `company_name`, `legal_name`, `inn`, `ogrn` без resolution → **STOP**.

---

## Step 5 — Operator verify card

| Action | Owner | Output |
|--------|-------|--------|
| HITL review всех production-critical fields | Human | Verified values |
| Set `operator_verified = true` | Human | Card ready for Input Sheet |
| Set `card_status = READY` | Human | Unblock step 6 |

**Critical fields (must be verified):** `company_name`, `legal_name`, `entity_type`, `inn` (if applicable), `ogrn` (if applicable).

---

## Step 6 — Legal Input Sheet from card

| Action | Owner | Output |
|--------|-------|--------|
| Copy LEGAL-INPUT-SHEET-TEMPLATE-v1 | Human | Draft Input Sheet |
| Copy identity + entity fields **from card only** | Human | No parallel discovery |
| Add `domain`, derived URLs, site_type, footer/consent confirmations | Human | Complete Input Sheet |
| Reference `card_id` in Input Sheet `notes` | Human | Traceability |

**Gate:** Input Sheet **must not** invent `company_name` / `legal_name` not present on verified card.

---

## Step 7–8 — Existing legal workflow

Продолжить [LEGAL-GENERATION-WORKFLOW-v1.md](../legal/LEGAL-GENERATION-WORKFLOW-v1.md) с Step 3 (Validate Input Sheet) onward.

---

## Roles

| Role | Responsibility |
|------|----------------|
| Operator | P1 documents, P6 verify, sign-off card + Input Sheet |
| Agent (Cursor) | Extraction assist, conflict report draft — **no** unsupervised production values |
| Client | Supply `project-input/legal-entity/` sources |

---

## SAFE UNKNOWN

- SLA/timing per step — **not scheduled**.
- Automated card validator script — **not implemented** v1.

---

*Workflow version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal-entity/`.*

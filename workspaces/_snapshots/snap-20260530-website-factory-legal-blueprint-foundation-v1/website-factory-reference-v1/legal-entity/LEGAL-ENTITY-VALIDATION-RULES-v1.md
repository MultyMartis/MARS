# Website Factory — Legal Entity Validation Rules v1

**Версия:** v1  
**Статус:** validation semantics — **documentation only**  
**Не является:** automated validator, CI gate (FUTURE)

---

## Назначение

Правила проверки Legal Entity Card **до** передачи данных в Legal Input Sheet и legal generation.

**Workflow step:** [LEGAL-ENTITY-WORKFLOW-v1.md](LEGAL-ENTITY-WORKFLOW-v1.md) Step 4.

---

## Validation phases

| Phase | Scope |
|-------|-------|
| **V1 — Format** | Синтаксис ИНН, ОГРН, КПП, БИК, счетов |
| **V2 — Completeness** | Required fields for entity_type |
| **V3 — Priority integrity** | No illegal downgrade overwrite |
| **V4 — Conflicts** | Cross-source disagreement |
| **V5 — Operator gate** | `operator_verified` before Input Sheet |

---

## V1 — Format rules (RU)

### INN (`inn`)

| `entity_type` | Length | Digits only | Checksum |
|---------------|--------|-------------|----------|
| `LEGAL_ENTITY` | 10 | Required | Recommended human verify; auto checksum **FUTURE** |
| `INDIVIDUAL_ENTREPRENEUR` | 12 | Required | Recommended human verify |
| `SELF_EMPLOYED` | 12 | Required | Same as ИП pattern |
| `UNKNOWN` | — | Fail if inn present without type resolution |

**Fail examples:** `500911493` (9 digits for UL), `abc5009114932`, empty when entity requires inn.

### OGRN / OGRNIP (`ogrn`)

| `entity_type` | Length | Notes |
|---------------|--------|-------|
| `LEGAL_ENTITY` | 13 | Label in docs may be ОГРН |
| `INDIVIDUAL_ENTREPRENEUR` | 15 | ОГРНИП stored in `ogrn` field per card schema |

**Fail:** wrong length, non-numeric.

### KPP (`kpp`)

| Rule | Value |
|------|-------|
| Applicable | `LEGAL_ENTITY` only |
| Length | 9 digits |
| Optional | May be empty for ИП |

### BIK (`bik`)

| Rule | Value |
|------|-------|
| Length | 9 digits |
| Optional block | Banking block optional for L1–L4 |

### Bank accounts

| Field | Typical length | Rule |
|-------|----------------|------|
| `checking_account` | 20 digits | Numeric |
| `correspondent_account` | 20 digits | Numeric |

**Fail:** obvious truncation, letters in account number.

### Email / phone

| Field | Rule |
|-------|------|
| `email` | Contains `@`, no spaces; production domain alignment **checked at Input Sheet** |
| `phone` | Non-empty recommended; format **per operator** (RU +7) |

---

## V2 — Completeness

| `entity_type` | Required before READY |
|---------------|----------------------|
| `LEGAL_ENTITY` | `company_name`, `legal_name`, `inn`, `ogrn`, `operator_verified` |
| `INDIVIDUAL_ENTREPRENEUR` | `company_name`, `legal_name`, `inn`, `ogrn` (ОГРНИП), `operator_verified` |
| `SELF_EMPLOYED` | Charter-specific; minimum `company_name`, `legal_name`, `operator_verified` |
| Any with UNKNOWN identity | `card_status = NOT_READY` |

---

## V3 — Priority integrity

| Check | Pass | Fail |
|-------|------|------|
| Field from P1 not overwritten by P4/P5 in card without note | ✓ | Silent overwrite |
| `source_priority` present for each non-empty field | ✓ | Missing metadata |
| P6 contradicts P1 without conflict resolution | — | **STOP** + conflict report |

---

## V4 — Conflicts

### Когда создавать conflict report

Любое расхождение **production-critical** полей между источниками разного приоритета или равного приоритета:

- `company_name`
- `legal_name`
- `inn`
- `ogrn`
- `kpp`
- `address`

### Conflict report (minimal template)

Создать файл, напр. `legal/<project>-LEGAL-ENTITY-CONFLICT-v1.md`:

```markdown
# Legal Entity Conflict Report v1

**card_id:** ...
**date:** YYYY-MM-DD

| field | value_a | source_a | priority_a | value_b | source_b | priority_b | resolution |
|-------|---------|----------|------------|---------|----------|------------|------------|
| company_name | ООО «ТРИУМФ» | egrul.pdf | P1 | Триумф | footer | P4 | PENDING |

**Resolution status:** PENDING | RESOLVED
**Operator decision:** (required before READY)
```

### Поведение при конфликте

| Rule | Action |
|------|--------|
| Never guess | Не выбирать «более короткое» имя |
| Never auto-merge | Не объединять partial strings |
| Preserve both values | В conflict report |
| Card field | Hold **higher priority** only in card body; lower in report |
| Unresolved | `card_status = CONFLICT` — **STOP** Input Sheet |

---

## V5 — Operator gate

| Check | Pass | Fail |
|-------|------|------|
| `operator_verified = true` | ✓ | Missing |
| Sign-off block in card template completed | ✓ | Empty |
| `company_name` + `legal_name` confirmed | ✓ | UNKNOWN or draft-only |

---

## Mapping to Legal Input Sheet validation

После card READY → Input Sheet validation per [LEGAL-INPUT-SHEET-v1.md](../legal/LEGAL-INPUT-SHEET-v1.md):

- Input Sheet values **must match** card for identity/entity fields.
- Mismatch Input Sheet vs card → **FAIL** (drift).

---

## SAFE UNKNOWN

- Automated INN checksum script in repo — **not implemented** v1.
- International VAT/tax IDs — **not covered**.

---

*Validation version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal-entity/`.*

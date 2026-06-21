# REPORT — КОРВО НЕРО — ATLAS REGISTRATION

**Report type:** Lane B — ATLAS registry population pass record (**relationship correction applied** 2026-06-21)  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Intake slug:** `corvonero`  
**Workspace:** `workspaces/corvonero-yandex-direct/`  
**Canonical report path:** `projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md`

**Is not:** MIG Research Request, ORCA strategy, Website Factory production, commit, push.

---

## 0. Relationship correction summary *(2026-06-21)*

| Issue | Resolution |
|-------|------------|
| REL-CORV-WB-02 **OWNS** contradicted WEB-CORV-01 owner **SAFE UNKNOWN** | **Variant B** — edge **deprecated**; no **OPERATES** substitute; contextual note only |
| REL-CORV-DM-01 **SECONDARY_DOMAIN** mislabeled apex/subdomain | **Superseded** → REL-CORV-DM-02 **POINTS_TO** |
| Attestation | AT-CORV-REL-02 correction act |

**Final active relationships:** REL-0042, REL-CORV-PJ-01, REL-CORV-WB-01, REL-CORV-DM-02 — **no** active Org → Website edge.

---

## 1. Preflight

| Check | Result |
|-------|--------|
| `git status --short` | **Many unrelated WIP changes** — Corvonero ATLAS files are **new untracked** only in this pass |
| `git branch --show-current` | `mars/post-cycle8-live-tests` |
| `git rev-parse --short HEAD` | `1d17429` *(post-correction preflight)* |
| ATLAS OPERATIONAL-INDEX read | **Done** |
| Population registers / schema reviewed | **Done** — ORG, PRJ, WEB, DOM, REL families per [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) |
| ID assignment rules verified | **Done** — sequential slots after ORG-0008, PRJ-0012, REL-0041; slug IDs WEB-CORV-01, DOM-CORV-01 per tranche pattern |
| Foreign WIP modified | **No** — only new ATLAS population artifacts |

---

## 2. Existing Entity Search

| Search term | Register hit | Verdict |
|-------------|--------------|---------|
| `Корво Неро` | **None** | Absent |
| `Corvo Nero` / `corvonero` | **None** in population registers | Absent |
| `ИП Никифоров Роман Вадимович` | **None** | Absent |
| INN `540200831636` | **None** | Absent |
| OGRNIP `324547600100482` | **None** | Absent |
| `corvonero.ru` | **None** | Absent |
| `lk.corvonero.ru` | **None** | Absent |

**Conclusion:** All candidate entities **absent** — population authorized.

**Existing references used (not created):** ORG-0003 i-SEO (vendor); PER-0001 Русецкий Андрей *(reference only — edge not minted)*.

---

## 3. IDs Assigned

| Class | ID | Basis |
|-------|-----|-------|
| Organization | **ORG-0009** | Next after ORG-0008 |
| Legal Entity | **LE-0006** | Next after LE-0005 *(Makita LE-0006 candidate never minted)* |
| Project | **PRJ-0013** | Next after PRJ-0012 |
| Website | **WEB-CORV-01** | Corvonero tranche slug namespace |
| Domain | **DOM-CORV-01** | Corvonero tranche slug namespace |
| Commercial REL | **REL-0042** | Next after REL-0041 |
| Project REL | **REL-CORV-PJ-01** | Tranche slug namespace |
| Website REL | **REL-CORV-WB-01**, **REL-CORV-WB-02** | Tranche slug namespace |
| Domain REL | **REL-CORV-DM-01** *(replaced)*, **REL-CORV-DM-02** | Tranche slug namespace |

---

## 4. Entities Registered

### 4.1 Organization — ORG-0009

| Field | Value |
|-------|-------|
| Canonical name | Центр автоматизации «Корво Неро» |
| Classification | i-SEO client |
| Legal entity | LE-0006 ИП Никифоров Роман Вадимович |
| INN / OGRNIP | 540200831636 / 324547600100482 |
| Registration date | 2024-06-14 |
| Base region | Новосибирск |
| Evidence tier | **E0** |
| Lifecycle | **active** |

### 4.2 Legal Entity — LE-0006

| Field | Value |
|-------|-------|
| Legal form | ИП |
| Completeness | **partial** — E0 operator intake; no CC; no E2 extract |
| Lifecycle | **active** |

### 4.3 Project — PRJ-0013

| Field | Value |
|-------|-------|
| Name | Корво Неро — Яндекс Директ и посадочные страницы |
| Commissioning org | ORG-0009 |
| Lifecycle | **active** |

### 4.4 Website — WEB-CORV-01

| Field | Value |
|-------|-------|
| Host | lk.corvonero.ru |
| URL | `http://lk.corvonero.ru/` |
| Platform | Tilda |
| Owner | **SAFE UNKNOWN** |
| Lifecycle | **active** |

### 4.5 Domain — DOM-CORV-01

| Field | Value |
|-------|-------|
| Hostname | corvonero.ru |
| Class | apex |
| Owner / registrar | **SAFE UNKNOWN** |
| Lifecycle | **active** |

---

## 5. Relationships Registered

### 5.1 Active relationships *(post-correction)*

| ID | Subject | Type | Object | Semantics |
|----|---------|------|--------|-----------|
| **REL-0042** | ORG-0009 Корво Неро | **CLIENT_OF** | ORG-0003 i-SEO | i-SEO client |
| **REL-CORV-PJ-01** | PRJ-0013 | **COMMISSIONED_BY** | ORG-0009 | Project belongs to org |
| **REL-CORV-WB-01** | WEB-CORV-01 | **BELONGS_TO** | PRJ-0013 | Site under Direct project |
| **REL-CORV-DM-02** | DOM-CORV-01 | **POINTS_TO** | WEB-CORV-01 | Apex zone `corvonero.ru` hosts subdomain site `lk.corvonero.ru` — structural pointer only |

### 5.2 Withdrawn / superseded relationships

| ID | Subject | Type | Object | Lifecycle | Reason |
|----|---------|------|--------|-----------|--------|
| **REL-CORV-WB-02** | ORG-0009 | **OWNS** | WEB-CORV-01 | **deprecated** | **Too strong** — site/Tilda owner **SAFE UNKNOWN**; OWNS asserts org-level property without evidence |
| **REL-CORV-DM-01** | DOM-CORV-01 | **SECONDARY_DOMAIN** | WEB-CORV-01 | **replaced** → REL-CORV-DM-02 | Apex is **not** alias hostname for subdomain site |

### 5.3 Org ↔ Website contextual note

WEB-CORV-01 используется как сайт Центра автоматизации «Корво Неро»; юридическое и техническое владение **SAFE UNKNOWN**. Structural path without ownership edge: WEB-CORV-01 ──BELONGS_TO──► PRJ-0013 ──COMMISSIONED_BY──► ORG-0009.

### 5.4 Domain ↔ Website final semantics

`corvonero.ru` (DOM-CORV-01, **apex**) ──**POINTS_TO**──► WEB-CORV-01 (`lk.corvonero.ru`, site hostname). Direction **Domain → Website** per [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7. **Not** SECONDARY_DOMAIN (apex is not alias of subdomain). Domain owner / registrant **SAFE UNKNOWN**.

---

## 6. Unsupported or Deferred Relationships

| Requested semantics | Handling | Reason |
|---------------------|----------|--------|
| WEB **REPRESENTS** ORG | **Contextual note only** — REL-CORV-WB-02 **OWNS** **deprecated** | No **REPRESENTS** type; **OWNS** too strong when owner SAFE UNKNOWN; **OPERATES** not substituted |
| WEB **PART_OF** DOM | **Mapped** → DOM **POINTS_TO** WEB (REL-CORV-DM-02) | Prior **SECONDARY_DOMAIN** incorrect — apex not alias; **POINTS_TO** is §7 fallback |
| ORG-0009 → ORG-0001 | **Rejected** | Operator restriction |
| Андрей **EXECUTES_PPC_FOR** PRJ | **Deferred — documentation note** | Type not in v1 taxonomy; PER-0001 referenced only |
| ORG → DOM **OWNS** | **Deferred** | Domain owner SAFE UNKNOWN |
| Person ↔ Project PPC edge | **Deferred** | Schema / attestation gate |
| Agreement / CRM / finance edges | **Excluded** | ATLAS boundary |

---

## 7. Files Changed

### 7.1 Initial registration *(2026-06-21)*

| # | Path | Action |
|---|------|--------|
| 1 | `projects/atlas/population/ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md` | **Created** |
| 2 | `projects/atlas/population/ATLAS-CORVONERO-ORGANIZATION-ATTESTATION-v1.md` | **Created** |
| 3 | `projects/atlas/population/ATLAS-CORVONERO-PROJECT-REGISTER-v1.md` | **Created** |
| 4 | `projects/atlas/population/ATLAS-CORVONERO-PROJECT-RELATIONSHIP-REGISTER-v1.md` | **Created** |
| 5 | `projects/atlas/population/ATLAS-CORVONERO-WEBSITE-REGISTER-v1.md` | **Created** |
| 6 | `projects/atlas/population/ATLAS-CORVONERO-WEBSITE-RELATIONSHIP-REGISTER-v1.md` | **Created** |
| 7 | `projects/atlas/population/ATLAS-CORVONERO-DOMAIN-REGISTER-v1.md` | **Created** |
| 8 | `projects/atlas/population/ATLAS-CORVONERO-DOMAIN-RELATIONSHIP-REGISTER-v1.md` | **Created** |
| 9 | `projects/atlas/population/ATLAS-CORVONERO-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md` | **Created** |
| 10 | `projects/atlas/population/ATLAS-CORVONERO-PROJECT-ATTESTATION-v1.md` | **Created** |
| 11 | `projects/atlas/population/ATLAS-CORVONERO-WEBSITE-ATTESTATION-v1.md` | **Created** |
| 12 | `projects/atlas/population/ATLAS-CORVONERO-DOMAIN-ATTESTATION-v1.md` | **Created** |
| 13 | `projects/atlas/population/ATLAS-CORVONERO-RELATIONSHIP-ATTESTATION-v1.md` | **Created** |
| 14 | `projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md` | **Created** |

### 7.2 Relationship correction *(2026-06-21)*

| # | Path | Action |
|---|------|--------|
| 1 | `projects/atlas/population/ATLAS-CORVONERO-WEBSITE-RELATIONSHIP-REGISTER-v1.md` | **Modified** — REL-CORV-WB-02 deprecated |
| 2 | `projects/atlas/population/ATLAS-CORVONERO-DOMAIN-RELATIONSHIP-REGISTER-v1.md` | **Modified** — REL-CORV-DM-01 replaced; REL-CORV-DM-02 minted |
| 3 | `projects/atlas/population/ATLAS-CORVONERO-RELATIONSHIP-ATTESTATION-v1.md` | **Modified** — AT-CORV-REL-02 |
| 4 | `projects/atlas/population/ATLAS-CORVONERO-WEBSITE-REGISTER-v1.md` | **Modified** — contextual note |
| 5 | `projects/atlas/population/ATLAS-CORVONERO-WEBSITE-ATTESTATION-v1.md` | **Modified** — OWNS withdrawal note |
| 6 | `projects/atlas/population/ATLAS-CORVONERO-DOMAIN-REGISTER-v1.md` | **Modified** — POINTS_TO policy note |
| 7 | `projects/atlas/population/ATLAS-CORVONERO-DOMAIN-ATTESTATION-v1.md` | **Modified** — POINTS_TO note |
| 8 | `projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md` | **Modified** — correction summary |

**Not changed:** MIG, ORCA, Website Factory, OPS, MARS project registry, `workspaces/corvonero-yandex-direct/*`, existing Wave 1–6B registers.

---

## 8. Validation

| Check | Result |
|-------|--------|
| No duplicate INN `540200831636` | **Pass** |
| No duplicate OGRNIP `324547600100482` | **Pass** |
| No duplicate hostname `corvonero.ru` / `lk.corvonero.ru` | **Pass** |
| Assigned IDs unique | **Pass** |
| Schema conformance | **Pass** — CLIENT_OF, COMMISSIONED_BY, BELONGS_TO, POINTS_TO only *(active)* |
| No active ORG-0009 **OWNS** WEB-CORV-01 | **Pass** — REL-CORV-WB-02 **deprecated** |
| No active SECONDARY_DOMAIN DOM-CORV-01 → WEB-CORV-01 | **Pass** — superseded by POINTS_TO |
| Website owner SAFE UNKNOWN | **Pass** |
| Domain owner / registrant SAFE UNKNOWN | **Pass** |
| No new relationship types | **Pass** |
| No ORG-0001 edge | **Pass** |
| No fabricated domain / site owner | **Pass** |
| Changes within ATLAS scope only | **Pass** |
| No commit | **Pass** |
| No push | **Pass** |

---

## 9. Git Status

| Item | Value |
|------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| HEAD | `1d17429` |
| Corvonero ATLAS artifacts | **14 files** under `projects/atlas/` *(8 modified in correction pass)* |
| Unrelated repo WIP | **Present** — do not batch-commit with Corvonero pass |

---

## 10. Recommended Selective Git Scope

When operator approves commit, stage **only**:

```text
projects/atlas/population/ATLAS-CORVONERO-*.md
projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md
```

**Exclude from commit:** all unrelated modified files, MIG/ORCA/OPS/Website Factory paths, workspace intake files (unless separately approved).

**Suggested commit message (when requested):**

```text
Register Corvonero entities in ATLAS population registers (ORG-0009, PRJ-0013, WEB/DOM, REL-0042).
```

---

## 11. Stop Condition

| Gate | Status |
|------|--------|
| ATLAS population | **COMPLETE** *(relationship correction applied)* |
| MIG Research Request | **NOT STARTED** — per stop condition |
| Market / competitor / demand research | **NOT STARTED** |
| Commit | **NOT PERFORMED** |
| Push | **NOT PERFORMED** |

**STOP** — Lane B ATLAS registration complete. Next allowed Lane A action after operator approval: MIG Research Request preparation (separate workflow).

---

*CORVONERO ATLAS Registration Report v1 · 2026-06-21 · documentation only*

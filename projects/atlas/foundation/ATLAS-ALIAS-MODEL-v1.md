# ATLAS Alias Model v1

**Status:** **documented** — Phase 3 normative alias and naming governance.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) · [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md)  
**Is not:** search index design, fuzzy matching implementation, i18n slug generator, trademark registry, SEO keyword taxonomy.

---

## 1. Purpose

Define how **multiple linguistic forms** refer to **one canonical entity** without creating duplicate identities — covering trade names, transliterations, abbreviations, former brands, and display preferences.

**Core rule:**

> Many names → **one** `ORG-*` / `PER-*` / … id. Names never mint parallel canonical entities.

---

## 2. Naming concepts

### 2.1 Terminology

| Term | Definition | Canonical for communication? |
|------|------------|------------------------------|
| **Stable identifier** | `ORG-00042` etc. | **Yes** — durable contracts |
| **Canonical name** | Single attested primary label for humans | **Display default** — not a key |
| **Display name** | Context-specific label (UI locale, report header) | Optional override |
| **Alias** | Additional accepted reference to same entity | Search / intake matching |
| **Former name** | Historical label no longer primary | Audit + disambiguation |
| **Proposed name** | Intake suggestion not yet attested | **No** |

### 2.2 Canonical name

| Attribute | Rule |
|-----------|------|
| **Cardinality** | Exactly one canonical name per **active** entity at a time |
| **Selection** | Human attested — prefer operator-recognized business label |
| **Language** | May be RU or EN; not both required |
| **Change** | Rename updates canonical name; prior → **former name** alias |
| **Not unique globally** | Two orgs may share display-like canonical names until disambiguated — ids differ |

**Exemplar:**

| Entity | Canonical name | Notes |
|--------|----------------|-------|
| `ORG-0042` | Polygon | Attested English trade form |
| `ORG-0103` | i-SEO | Hyphenation preserved |

### 2.3 Alias

| Attribute | Rule |
|-----------|------|
| **Purpose** | Capture known alternate references |
| **Cardinality** | Zero to many |
| **Uniqueness** | Alias string may appear on **multiple** entities only with **disambiguation policy** (governance) |
| **Evidence** | E0 for operator-known; E1 for external docs |

**Program exemplars — Organization Polygon:**

| Alias | Type |
|-------|------|
| Полигон | Transliteration / RU trade |
| ООО Полигон | Legal-style label |
| Web Studio Polygon | Descriptive trade |
| WSP | Abbreviation |

**Program exemplars — Organization i-SEO:**

| Alias | Type |
|-------|------|
| ISEO | Latin variant |
| Ай-СЕО | Cyrillic marketing form |

**Program exemplars — Organization MetaCode:**

| Alias | Type |
|-------|------|
| Метакод | Cyrillic transliteration |

### 2.4 Former name

| Attribute | Rule |
|-----------|------|
| **Trigger** | Rebrand, legal rename, canonical name change |
| **Retention** | Permanent alias with role `former` |
| **Use** | Historical documents, old contracts referencing old brand |
| **Not** | Separate entity id |

### 2.5 Display name

| Attribute | Rule |
|-----------|------|
| **Purpose** | Locale- or consumer-specific presentation |
| **Optional** | May equal canonical name |
| **Override** | Does not change canonical name or id |
| **Example** | HomeGateway shows “Полигон” while canonical name remains “Polygon” |

---

## 3. Alias roles (governance taxonomy)

| Role | Meaning | Example |
|------|---------|---------|
| **alias** | Accepted alternate current reference | WSP |
| **former** | Historical only | Old agency name before merger |
| **legal** | Legal form string (non-primary key) | ООО «Полигон» |
| **trade** | Marketing / DBA | Web Studio Polygon |
| **abbreviation** | Short form | WSP, ISEO |
| **transliteration** | Cross-script equivalent | Метакод |
| **import_label** | Label from CRM/import | ACCOUNT-4421 name snapshot |
| **proposed** | Not attested | Chat mention pending review |

**Rule ALS-01:** Only roles **`alias`**, **`former`**, **`legal`**, **`trade`**, **`abbreviation`**, **`transliteration`** may appear on **canonical active** entity without `proposed` flag.

---

## 4. Alias philosophy

### 4.1 Aliases reduce friction; ids reduce ambiguity

| Without aliases | With aliases |
|-----------------|--------------|
| Operators re-type canonical name only | Intake matches “Полигон” → `ORG-0042` |
| Consumers invent duplicate orgs | Steward links alias instead |
| Search fails on Cyrillic | Transliteration in alias set |

### 4.2 Alias ≠ evidence of sameness

Shared alias text **does not prove** merge:

| Situation | Action |
|-----------|--------|
| Two orgs both known as “Delta” in different cities | Separate ids + disambiguation note |
| CRM import “Polygon” vs existing Polygon | Steward: merge or alias — not automatic |
| String similarity 0.95 | **Proposed** match only |

### 4.3 Abbreviation ambiguity

**WSP** may mean Polygon internally **or** an unrelated brand elsewhere.

| Step | Action |
|------|--------|
| 1 | Record alias with `context_note` (conceptual field) |
| 2 | If collision with another entity’s alias → flag **disputed alias** |
| 3 | Never auto-merge on abbreviation alone |

---

## 5. Governance rules

### 5.1 Who may add or change aliases

| Action | Program owner | Steward | Consumer | Agent |
|--------|---------------|---------|----------|-------|
| Add **proposed** alias | Yes | Yes | Yes (future) | Propose only |
| Promote to **attested** alias | Yes | Yes (delegated) | No | No |
| Change **canonical name** | Yes | Yes (delegated) | No | No |
| Remove alias | Yes | Yes | No | No |
| Mark alias **disputed** | Yes | Yes | Flag | Flag |

**Rule ALS-G01:** No autonomous promotion of proposed alias to attested canonical set.

### 5.2 Adding an alias (workflow)

```text
Request → Classify role (alias | former | …)
        → Check collision registry (same string, other entity)
        → If collision: disputed alias OR disambiguation note
        → Attest → attach to entity id
```

### 5.3 Removing an alias

| Situation | Action |
|-----------|--------|
| Typo | Remove after steward review |
| Former name incorrectly deleted | Restore with `former` role |
| Alias actually meant second entity | Remove alias; **create or activate second entity** — not alias on wrong id |

### 5.4 Canonical name change

| Step | Requirement |
|------|-------------|
| 1 | Move old canonical name to `former` alias |
| 2 | Set new canonical name |
| 3 | Attestation note + date |
| 4 | **Do not** change `ORG-*` id |

### 5.5 Alias on merged entities

| Rule | Detail |
|------|--------|
| **ALS-M01** | Survivor receives **union** of alias sets from absorbed entities |
| **ALS-M02** | Duplicate alias strings dedupe to one row |
| **ALS-M03** | `import_label` from absorbed id may retain source note |

---

## 6. Entity-type notes

### 6.1 Organization

Highest alias volume. Legal names, trade names, abbreviations common.

| Pitfall | Mitigation |
|---------|------------|
| Separate org per DBA | Default: alias unless attested separate business unit |
| ООО prefix treated as different company | Legal role alias on same org |

### 6.2 Person

| Allowed | Caution |
|---------|---------|
| Patronymic variants, nicknames | Homonyms require separate `PER-*` |
| Latin ↔ Cyrillic spellings | Aliases, not second person |

### 6.3 Project

| Allowed | Caution |
|---------|---------|
| Codename, client-facing title | Renamed initiative: former + same `PRJ-*` |
| Same codename reused years later | New project id if **new** initiative attested |

### 6.4 Website

| Allowed | Caution |
|---------|---------|
| Old brand title | Domain hostname is on `DOM-*`, not website alias substitute |

### 6.5 Domain

| Allowed | Caution |
|---------|------------|
| Punycode vs Unicode presentation | Attest both as aliases on one `DOM-*` if same hostname |
| `www` vs apex | Policy per identifier doc — alias or separate `DOM-*` |

### 6.6 Relationship

Relationships use **derived labels** (“Andrey OWNER Polygon”) — not alias model. Type names come from [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md).

---

## 7. SAFE UNKNOWN handling (naming)

### 7.1 When naming triggers SAFE UNKNOWN

| Situation | Posture |
|-----------|---------|
| Cannot tell if two names are same org | **SAFE UNKNOWN** sameness; no second canonical |
| Alias target entity unclear | No alias attach; proposed intake |
| Which canonical name to prefer (EN vs RU) | Steward attestation; temporary **proposed** display |
| Person name matches multiple `PER-*` | UNKNOWN until disambiguated |

### 7.2 SAFE UNKNOWN is not an alias

| Concept | What it is |
|---------|------------|
| **SAFE UNKNOWN** | Explicit “we do not know” — [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §7 |
| **TBD placeholder name** | Forbidden as permanent canonical |
| **alias `proposed`** | “We have a string but not sure mapping” — not canonical |

**Rule ALS-U01:** Do not create alias `UNKNOWN` on an active entity to silence intake.

### 7.3 Naming collision with relationships

Per [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) A4: resolve **entity identity** before asserting canonical relationships.

---

## 8. Matching principles (no implementation)

Future intake may **suggest** entity matches. Phase 3 defines **governance of suggestions** only:

| Signal strength | Steward action |
|-----------------|----------------|
| Exact alias hit on one active entity | Link intake to that id |
| Exact hit on multiple entities | Disambiguation required |
| Fuzzy transliteration | **proposed** merge review |
| No hit | New **proposed** entity |

**Prohibition ALS-X01:** Auto-canonical entity creation from single name match.

---

## 9. Required architectural analysis (alias-specific)

### 9.1 How should aliases work?

**Decision:** Many-to-one labeled strings with roles; canonical name is singular attested default; ids unchanged on alias churn.

### 9.2 Same entity with multiple names?

**Decision:** **Aliases on one id** when attested same business subject; **separate ids** when attested different subjects despite similar strings.

### 9.3 Uncertain identity?

**Decision:** **SAFE UNKNOWN** or **proposed** — never resolve by picking favorite alias as new org.

---

## 10. Prohibitions

| # | Prohibition |
|---|-------------|
| **ALS-X02** | Second canonical org because “Полигон” and “Polygon” differ by script |
| **ALS-X03** | Deleting `former` names to simplify UI |
| **ALS-X04** | Business Scope label stored as alias |
| **ALS-X05** | CRM name as canonical name without human attestation |
| **ALS-X06** | Using alias string in consumer durable contract instead of id |

---

## 11. Related documents

| Document | Role |
|----------|------|
| [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) | Sameness, lifecycle |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) | Merge alias union |
| [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) | DBA as alias note |
| [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) | Display name change tier |

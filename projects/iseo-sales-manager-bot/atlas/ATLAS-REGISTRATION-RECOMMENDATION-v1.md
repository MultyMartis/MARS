# ATLAS REGISTRATION RECOMMENDATION v1

**Product:** i-SEO Sales Manager Bot  
**Status:** **RECOMMENDATION ONLY** — no ATLAS IDs minted · no population registers edited in Phase 2

---

## 1. Confirmed existing IDs (do not mint)

| ID | Canonical name | Role in this product |
|----|----------------|----------------------|
| **ORG-0003** | i-SEO Studio | Business organization / vendor agency |
| **PER-0001** | Русецкий Андрей Анатольевич | Ops/architect operator (multi-hat; Polygon/MetaCode) |
| **PER-0010** | Дягилева Ольга (Оля) | Primary manager user v1 |
| **PER-0011** | Шваков Никита Алексеевич | Business owner signal / i-SEO owner |

Evidence: ATLAS Wave 1–2 population / attestation registers (repo).

---

## 2. DRAFT relationships (not attested)

| Draft | From | Type (candidate) | To | Notes |
|-------|------|------------------|----|-------|
| D-REL-A | PER-0010 | EMPLOYEE / uses-tool | ORG-0003 | Already has REL-0009 EMPLOYEE→ORG-0003 in Wave 2B — **reuse**, do not duplicate |
| D-REL-B | PER-0011 | OWNER | ORG-0003 | Already REL-0006 — **reuse** |
| D-REL-C | PER-0001 | CONTRIBUTES_TO / operates | *(system)* | Person↔system edges **not** in ATLAS v1 taxonomy as first-class “bot” — **defer** |
| D-REL-D | ORG-0003 | OPERATES / SPONSORS | Sales Manager Bot | Bot is **not** an ATLAS Organization/Project entity yet — **do not mint PRJ without charter** |

**Recommendation:** treat the bot as an **external operational system** documented in MARS `project_id=iseo-sales-manager-bot`, with ATLAS limited to **person/org context** until a Wave explicitly adds “systems/tools” entity class (currently out of ATLAS boundaries as CRM/runtime).

---

## 3. Required operator attestation (before any ATLAS write)

1. Confirm Оля (PER-0010) is the v1 primary Telegram manager consumer.
2. Confirm whether Андрей (PER-0001) is product owner vs Nikita (PER-0011).
3. Confirm no new ORG/PER IDs are needed.
4. Explicit charter if a structural **PRJ-*** for “Sales Manager Bot” is desired (default: **not required for v1**).

---

## 4. Out of scope this phase

- Editing ATLAS population markdown registers
- Minting REL-/PRJ-/WEB-/DOM- IDs
- Claiming live usage attestation without operator sign-off

---

## 5. SAFE UNKNOWN

- Whether future ATLAS taxonomy will include external automation systems.
- Exact employment/role wording for Оля beyond existing EMPLOYEE edge.

---

*Related: OPERATIONAL-INDEX.md · registry decision in Phase 2 report.*

# Website Factory — Runtime Foundation Snapshot v1

**Snapshot ID:** `runtime-foundation-v1`  
**Дата snapshot:** 2026-06-01 (status sync 2026-06-04 — [FOUNDATION-FINALIZATION-PASS-v1.md](FOUNDATION-FINALIZATION-PASS-v1.md))  
**Operator:** documentation snapshot (human-operated)  
**Область:** `workspaces/website-factory-reference-v1/`  
**Manifest:** [snapshots/runtime-foundation-v1/SNAPSHOT-MANIFEST-v1.json](snapshots/runtime-foundation-v1/SNAPSHOT-MANIFEST-v1.json)

**Не является:** git tag, filesystem copy archive, runtime product, CI snapshot, deploy authorization, operator acceptance record.

**Связанные документы:** [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md), [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md), [runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md), [runtime-architecture/RUNTIME-ROADMAP-v1.md](runtime-architecture/RUNTIME-ROADMAP-v1.md)

---

## 1. Purpose

Runtime Foundation Snapshot v1 — **точка фиксации** полного стека архитектурных слоёв Website Factory на дату завершения поставки **Factory Runtime Architecture v1** (documentation) и перед следующим целевым workstream **Factory Engine Architecture v1**.

Snapshot:

- инвентаризирует **14 канонических каталогов** слоёв (live tree, не дублирует файлы);
- фиксирует статусы **FROZEN / ACCEPTED** (inventory baseline; operational register — NEXT-PRIORITIES);
- согласует roadmap с [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) и [runtime-architecture/RUNTIME-ROADMAP-v1.md](runtime-architecture/RUNTIME-ROADMAP-v1.md);
- служит baseline для operator acceptance Runtime v1 и charter Factory Engine v1.

**Honesty:** в репозитории **нет** shipped Website Factory runtime, workflow engine, validators CLI или Factory Engine — только документация и reference `src/`.

---

## 2. Snapshot scope (included layers)

| # | Layer directory | Files (2026-06-01) | Entry document |
|---|-----------------|-------------------|----------------|
| 1 | [legal/](legal/) | 21 | [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| 2 | [legal-entity/](legal-entity/) | 8 | [legal-entity/LEGAL-ENTITY-WORKFLOW-v1.md](legal-entity/LEGAL-ENTITY-WORKFLOW-v1.md) |
| 3 | [registry/](registry/) | 6 | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) |
| 4 | [blueprints/](blueprints/) | 10 | [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md) |
| 5 | [page-architecture/](page-architecture/) | 9 | [page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md](page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md) |
| 6 | [block-registry/](block-registry/) | 14 | [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md) |
| 7 | [page-block-validation/](page-block-validation/) | 9 | [page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md) |
| 8 | [seo-architecture/](seo-architecture/) | 8 | [seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md](seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md) |
| 9 | [design-system/](design-system/) | 8 | [design-system/DESIGN-SYSTEM-MAPPING-v1.md](design-system/DESIGN-SYSTEM-MAPPING-v1.md) |
| 10 | [content-contracts/](content-contracts/) | 8 | [content-contracts/CONTENT-SYSTEM-v1.md](content-contracts/CONTENT-SYSTEM-v1.md) |
| 11 | [content-validation/](content-validation/) | 8 | [content-validation/CONTENT-VALIDATION-SYSTEM-v1.md](content-validation/CONTENT-VALIDATION-SYSTEM-v1.md) |
| 12 | [generation-contracts/](generation-contracts/) | 8 | [generation-contracts/GENERATION-SYSTEM-v1.md](generation-contracts/GENERATION-SYSTEM-v1.md) |
| 13 | [production-qa/](production-qa/) | 9 | [production-qa/PRODUCTION-QA-SYSTEM-v1.md](production-qa/PRODUCTION-QA-SYSTEM-v1.md) |
| 14 | [runtime-architecture/](runtime-architecture/) | 9 | [runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) |

**Total documented artefacts in scope:** 135 files (see manifest).

**Out of snapshot scope (by design):** `src/` reference implementation, `projects/mars-website-factory/` governance pack, external `_snapshots/` paths (historical, not in-repo).

---

## 3. Canonical layer chain (accepted architecture)

```text
Legal Pack (FROZEN) ── parallel track ─────────────────────────┐
                                                             │
Site Type Registry → Blueprints → Page Architecture        │
        → Block Registry → Page Block Validation           │
        → SEO Architecture v2 (ACCEPTED)                   │
        → Design System Mapping (ACCEPTED 2026-06-04)        │
        → Content Contracts (ACCEPTED)                     │
        → Content Validation (ACCEPTED)                      │
        → Generation Contracts (ACCEPTED)                  │
        → Production QA (ACCEPTED)                           │
        → Runtime Architecture v1 (ACCEPTED)  ← this snapshot
        ↓
Factory Engine Architecture v1 (NEXT — NOT QUEUED)
```

**Movement discipline:** [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) — 14 canonical states; **no execution engine**.

---

## 4. Frozen layers

| System | Location | Freeze date | Authority |
|--------|----------|-------------|-----------|
| **Legal Pack v1** | [legal/](legal/) + [legal-entity/](legal-entity/) | 2026-05-30 | [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| **Website Factory Foundation v1** (Registry → Page Block Validation chain) | foundation dirs §2 #3–7 | 2026-06-01 | [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) |

**Frozen rule:** no architectural expansion without operator charter + validation path. Typo/clarity and supersession banners — only by explicit operator instruction.

---

## 5. Accepted layers

| System | Location | Accepted | Entry |
|--------|----------|----------|-------|
| Legal Entity Discovery v1 | [legal-entity/](legal-entity/) | with Legal Pack freeze | [legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md](legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md) |
| Site Type Registry v1 | [registry/](registry/) | 2026-05-30+ | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) |
| Site Type Blueprints v1 (Core 5) | [blueprints/](blueprints/) | 2026-05-31 | [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md) |
| Page Architecture Contracts v1 | [page-architecture/](page-architecture/) | 2026-05-31 | [page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md](page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md) |
| Block Registry Alignment v1 | [block-registry/](block-registry/) | 2026-05-31 | [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md) |
| Page Block Validation v1 | [page-block-validation/](page-block-validation/) | 2026-06-01 | [page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md) |
| SEO Architecture Layer v2 | [seo-architecture/](seo-architecture/) | 2026-06-01 | [seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md](seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md) |
| Architecture Foundation v1 (consolidation) | root | 2026-06-01 | [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) |

**Historical superseded (retained, not deleted):** [registry/SITE-TYPE-SEO-MAPPING-v1.md](registry/SITE-TYPE-SEO-MAPPING-v1.md), [registry/SITE-TYPE-BLOCK-MAPPING-v1.md](registry/SITE-TYPE-BLOCK-MAPPING-v1.md), [registry/SITE-TYPE-LEGAL-MAPPING-v1.md](registry/SITE-TYPE-LEGAL-MAPPING-v1.md) — banners per [HYGIENE-PASS-v1.md](HYGIENE-PASS-v1.md).

---

## 6. Post-freeze accepted layers (2026-06-04)

| Workstream | Location | Delivered | Accepted | Artefacts |
|------------|----------|-----------|----------|-----------|
| Design System Mapping v1 | [design-system/](design-system/) | 2026-06-01 | 2026-06-04 | 8 |
| Content Contracts v1 | [content-contracts/](content-contracts/) | 2026-06-01 | 2026-06-04 | 8 |
| Content Validation v1 | [content-validation/](content-validation/) | 2026-06-01 | 2026-06-04 | 8 |
| Generation Contracts v1 | [generation-contracts/](generation-contracts/) | 2026-06-01 | 2026-06-04 | 8 |
| Production QA Architecture v1 | [production-qa/](production-qa/) | 2026-06-01 | 2026-06-04 | 9 |
| **Factory Runtime Architecture v1** | [runtime-architecture/](runtime-architecture/) | 2026-06-01 | 2026-06-04 | 9 |

Acceptance record: [FOUNDATION-FINALIZATION-PASS-v1.md](FOUNDATION-FINALIZATION-PASS-v1.md). Authoritative register: [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md).

---

## 7. Current roadmap (snapshot-aligned)

**Authoritative register:** [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)  
**Runtime evolution:** [runtime-architecture/RUNTIME-ROADMAP-v1.md](runtime-architecture/RUNTIME-ROADMAP-v1.md)

| Phase | Workstream | Status |
|-------|------------|--------|
| Foundation | Registry → Validation + Legal + SEO v2 | **FROZEN / ACCEPTED** |
| Downstream docs | Design → Content → Generation → Production QA | **ACCEPTED** (2026-06-04) |
| Movement | Factory Runtime Architecture v1 | **ACCEPTED** (2026-06-04) |
| **Next target** | **Factory Engine Architecture v1** | **NOT QUEUED** — charter required ([runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G09) |
| Future | Project manifest (R2), MIG semantics (R5), validators CLI (R6), workflow engine (R7) | **NOT QUEUED** |

**Post-v1 runtime phases (documentation only):** R2 manifest → R3 state log → **R4 Factory Engine** → R5 MIG → R6 advisors → R7 workflow evaluation.

---

## 8. Next target workstream: Factory Engine Architecture v1

| Attribute | Value |
|-----------|-------|
| **Name** | Factory Engine Architecture v1 |
| **Status** | **NOT QUEUED** |
| **Prerequisite** | Runtime Architecture v1 **ACCEPTED**; recommended batch acceptance of Design → Production QA layers |
| **Gap register** | [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) — RT-G09 |
| **Explicit non-claims** | No workflow engine, agents, n8n, DB, queue, code generation until separate charters |

**Scope boundary (expected charter):** execution semantics *above* movement discipline — still documentation-first unless operator opens implementation charter.

---

## 9. Validation record (snapshot creation)

| Check | Result | Notes |
|-------|--------|-------|
| All 14 layer directories exist | **PASS** | Verified 2026-06-01 — 135 files total |
| Runtime Architecture present | **PASS** | 9 artefacts; entry [RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) |
| Roadmap vs NEXT-PRIORITIES | **PASS** | Runtime **ACCEPTED**; Factory Engine = next charter |
| Roadmap vs RUNTIME-ROADMAP-v1 | **PASS** | R4 Factory Engine; Runtime v1 **ACCEPTED** (2026-06-04) |
| References to deleted layers | **PASS** | No `deleted layer` refs; superseded v1 mappings retained with banners |
| Broken snapshot path `../_snapshots/snap-20260530-*` | **PASS (marked historical)** | [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md) — not used as current truth |
| FREEZE / ARCHITECTURE-FOUNDATION roadmap sync | **PASS** | Synced 2026-06-04 — FOUNDATION-FINALIZATION-PASS-v1 |
| External v0 as canonical | **PASS** | `block-registry-v0` cited only as **not canon** with pointer discipline |
| Runtime / engine implementation claims | **PASS** | No false runtime product claims in runtime-architecture/ |

**Snapshot verdict:** **PASS** — safe inventory baseline; layer acceptance via NEXT-PRIORITIES + FOUNDATION-FINALIZATION-PASS-v1 (2026-06-04).

---

## 10. Reference implementation (context, not snapshotted)

| Asset | Path | Role |
|-------|------|------|
| Reference workspace `src/` | `workspaces/website-factory-reference-v1/src/` | LANDING block partials — partial canon |
| Triumph V6 legal pilot | `workspaces/triumph-manipulator-landing-v6/` | Legal Pack validation — **COMPLETE** |

---

## 11. Operator actions (suggested)

1. **Charter** Factory Engine Architecture v1 before any RT-G09 work.
2. Maintain status discipline via [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md).

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Operator acceptance dates for post-freeze layers | **2026-06-04** — FOUNDATION-FINALIZATION-PASS-v1 |
| Factory Engine v1 calendar | **not scheduled** |
| Whether physical `_snapshots/` copy exists outside this clone | **UNKNOWN** — manifest references live tree only |
| CI / validator CLI binding | **FUTURE** — no implementation proof in-repo |

---

*Runtime Foundation Snapshot v1 — 2026-06-01. Canonical location: `workspaces/website-factory-reference-v1/`.*

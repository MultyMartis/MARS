# I-SEO Report Hub — Nikita Implementation Sequence v0.1

**Status:** CHARTER / SEQUENCE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Nikita Report Template Data Model Charter 01

---

## 1. Immediate next step (recommended)

**`I-SEO Report Hub — Nikita Catalogue Seed and Work Entry Model Implementation 01`**

Scope:

- Apply additive migrations for `seo_work_categories`, `seo_work_items`, `monthly_report_work_entries`.  
- Sanitized Nikita seed (no access/credentials).  
- Minimal read/CRUD API or internal UI sufficient to prove entries attach to monthly report.  
- **No** PDF regen, **no** share mutation, **no** REQUIRED_BLOCK_KEYS change, **no** client template redesign.

Rationale: Option B needs real tables before UI polish and assembly; another pure charter (02) is **not** required unless operator rejects Migration Charter shapes.

---

## 2. Wave sequence (3–5)

| # | Wave | Purpose | Depends on |
|---|------|---------|------------|
| 1 | **Nikita Catalogue Seed and Work Entry Model Implementation 01** | Schema + seed + minimal entry persistence | This charter |
| 2 | **Work Entry UI Implementation 01** | Specialist UX: catalogue picker, statuses, visibility, monthly list | Wave 1 |
| 3 | **Monthly Report Summary Assembly Implementation 01** | Assistive fill/rollup into 6 shells; keep manual edit | Wave 2 |
| 4 | **Client Report Template Visual Alignment Charter 01** | PDF/HTML chrome + section presentation (docs) | Wave 3 content stable enough |
| 5 | **Client Report Template Implementation 01** | Implement aligned client artifact | Charter 4 |

Optional parallel (not blockers):

- Local Share QA Cleanup 01  
- Production Environment Operator Decision 01  
- Fixture Demo* Russianization (copy-only)

---

## 3. Explicitly deferred / rejected as next

| Candidate | Why not next |
|-----------|--------------|
| Nikita Catalogue Seed Charter 02 | Redundant — Migration Charter v0.1 sufficient |
| Option C full workflow | Too large; high MVP break risk |
| Client PDF visual alignment before entries | Would redesign empty shells again |
| AI fill implementation | Needs structured entries first |

---

## 4. Exit criteria before Client Template Charter

1. Catalogue seeded and reviewable.  
2. Specialist can log ≥1 month of categorized work entries on fixture.  
3. Six shells still finalize/snapshot/export on unchanged keys.  
4. Operator accepts that client visual wave consumes assembled content, not catalogue raw dumps.

---

## 5. Risk controls across waves

- Exact-path git; foreign WIP preserved.  
- No broad migrate on production.  
- Dual-path: empty entries must not block current MVP.  
- Checksums: only regenerate artifacts in waves that explicitly charter regen.  
- Secrets: continuous exclusion of Nikita access sheet.

---

## 6. SAFE UNKNOWN

- Whether waves 1–2 can merge into one operator session if implementation is small.  
- Exact scheduling vs production environment track.

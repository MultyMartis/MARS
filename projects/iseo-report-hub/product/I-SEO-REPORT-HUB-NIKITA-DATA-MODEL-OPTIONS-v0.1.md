# I-SEO Report Hub — Nikita Data Model Options v0.1

**Status:** CHARTER / OPTIONS — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Nikita Report Template Data Model Charter 01

---

## 1. Option A — Minimal extension

**Idea:** Keep current 6 blocks; improve labels/templates/help; add limited metadata in `data_json` or monthly notes.

| Dimension | Assessment |
|-----------|------------|
| Schema changes | None or tiny nullable metadata |
| Implementation complexity | Low |
| Migration risk | Low |
| UI impact | Copy/help only |
| PDF impact | None unless regen |
| AI-fill potential | Weak (unstructured blobs) |
| Nikita alignment | **Poor** — taxonomy stays outside system |
| Compatibility with MVP | Excellent |

**Verdict:** Acceptable only as interim polish — **not** the product target after operator accepted structure debt.

---

## 2. Option B — Catalogue-backed work items (recommended)

**Idea:** Add work catalogue + monthly work entries. Current 6 blocks become **client summary / assembly** sections (manual + optional generation). Preserve finalize/snapshot/export/share.

| Dimension | Assessment |
|-----------|------------|
| Schema changes | New tables: categories, items, monthly entries; optional FKs |
| Implementation complexity | Medium |
| Migration risk | Medium — additive if old path kept |
| UI impact | New work-entry UI + keep block CRUD |
| PDF impact | Later, when assembly changes export content |
| AI-fill potential | Good (per-item drafts + summary rollup) |
| Nikita alignment | **Strong** |
| Compatibility with MVP | High if dual-path: entries optional, shells still required |

**Phased shape:**

1. DB migration + Nikita seed (sanitized).  
2. Admin/manager UI for work entries.  
3. Summary generation / manual polish of 6 shells.  
4. Client report template visual alignment (separate charter).

---

## 3. Option C — Full workflow model

**Idea:** Catalogue + weekly structured tasks + approvals per item + evidence store + metrics + AI fields + plan quotas in one wave.

| Dimension | Assessment |
|-----------|------------|
| Schema changes | Large (5+ tables, status machines) |
| Implementation complexity | High |
| Migration risk | High |
| UI impact | Major rewrite of specialist UX |
| PDF impact | Coupled risk |
| AI-fill potential | Highest |
| Nikita alignment | Highest eventually |
| Compatibility with MVP | Fragile if done as big-bang |

**Verdict:** Right **long-term** north star; **wrong** next implementation bite.

---

## 4. Comparison

| Criterion | A | B | C |
|-----------|---|---|---|
| Speed | ★★★ | ★★ | ★ |
| Nikita fidelity | ★ | ★★★ | ★★★★ |
| MVP safety | ★★★★ | ★★★ | ★★ |
| AI readiness | ★ | ★★★ | ★★★★ |
| Operator clarity | ★★ | ★★★★ | ★★ (overbuild risk) |

---

## 5. Recommendation

**Adopt Option B as target**, implemented in phases (not one mega-PR).

**Do not** spend another pure seed-only charter unless operator rejects table shapes in Migration Charter — the migration charter in this wave is sufficient to start:

`I-SEO Report Hub — Nikita Catalogue Seed and Work Entry Model Implementation 01`

Option A may still land as micro-copy tweaks inside UI waves without blocking B.  
Option C items (evidence table, metrics, weekly entries, AI columns) are **explicit later** backlog after B proves dual-path.

---

## 6. Compatibility rules for Option B

1. Do not remove `monthly_report_contents` flat columns day-1.  
2. Do not change `REQUIRED_BLOCK_KEYS` day-1.  
3. Do not regenerate existing PDFs/shares in catalogue impl wave.  
4. Fixture gets optional sample entries; Demo* names may remain.  
5. Exclude access/credential items from seed.

---

## 7. SAFE UNKNOWN

- Whether specialists will prefer catalogue pickers vs free-text for month 1 of adoption.  
- Volume of custom (non-catalogue) entries in real projects.

# I-SEO Report Hub — Russian UX Implementation Plan v0.1

**Status:** FUTURE IMPLEMENTATION PLAN — **do not implement in this charter wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Recommended next wave name:** **I-SEO Report Hub — Russian UX and Demo Alignment Implementation 01**

**Inputs:**
- [I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-ALIGNMENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-ALIGNMENT-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-INVENTORY-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-INVENTORY-v0.1.md)
- [I-SEO-REPORT-HUB-RUSSIAN-UX-COPY-DICTIONARY-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-COPY-DICTIONARY-v0.1.md)
- [I-SEO-REPORT-HUB-RUSSIAN-UX-MANAGER-FLOW-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-MANAGER-FLOW-v0.1.md)

---

## 1. Principle

Keep the **PHP+SQL engine**. Change **labels, hierarchy, progressive disclosure, footer truth, and client PDF surface**. Optional visual shell alignment to static demo v0.4 comes **after** copy+flow clarity.

**No production deployment** until Russian UX is operator-accepted. Production Environment Decision / Operator Decision may continue on a parallel track, but day-to-day product UX cleanup is the recommended next product layer.

---

## 2. Phased plan

| Phase | Name | Scope | Out of scope |
|-------|------|-------|--------------|
| 1 | Russian copy dictionary / labels | Wire dictionary into views/controllers strings; nav; badges; buttons | Schema changes |
| 2 | Footer cleanup | Replace stale Phase 1A skeleton footer / phase label with truthful local status | Claiming production |
| 3 | Dashboard simplification | Screen A: headlines + quick actions; demote status cards | New analytics |
| 4 | Exports page simplification | Screen C: primary PDF card; archive legacy | Changing export engine |
| 5 | Export detail simplification | Manager facts + download + handoff; tech in `<details>` | Artifact rewrite |
| 6 | Shares / copy pack Russian UX | Screen D chrome in RU; keep Copy Pack v0.1 bodies | Email delivery / portal |
| 7 | Technical details collapsible | Consistent pattern across export/snapshot/shares | Removing fields from DB |
| 8 | Report/PDF Russian client-facing | Title + sections; strip fixture/local/tech from **real** reports | Changing share crypto |
| 9 | Visual QA | Operator screenshots vs checklist | Production deploy |
| 10 | Manual click-through | A→D flow with test user | Broad refactor |

### Optional later (not required to start Implementation 01)

- Light INTLSEO shell / sidebar CSS port from `iseo-report-hub-prototype`  
- Demo v0.5 backlog items  
- Full bilingual UI  

---

## 3. Suggested file touch zones (future only)

| Zone | Likely paths (app-source) |
|------|---------------------------|
| Layout chrome | `Views/partials/header.php`, `footer.php`, `layout.php` |
| Pages | `Views/pages/dashboard.php`, `login.php`, `health.php`, reporting/monthly/export/share views |
| CSS | `public/assets/css/app.css` |
| Controllers pageTitle / cards | `DashboardController.php` and related |
| PDF/HTML render | `Support/ReportTemplateRenderer.php`, template services |
| Handoff labels | Share/handoff views + any label builders in services |

Runtime sync only under an explicit source→runtime charter **after** source edits.

---

## 4. Validation gates (Implementation 01)

1. Exact-path app-source edits only; selective staging.  
2. Local click-through: login → periods → monthly → exports → export 4 → shares.  
3. No DB schema required unless a later charter reopens.  
4. No share/token smoke that leaves production-like secrets in docs.  
5. Operator Visual QA PASS on Russian UX checklist.  
6. Smoke suite regression if existing smoke covers UI strings — update expectations carefully.  
7. Still **no** production claim.

---

## 5. Ordering vs production environment

| Track | Status after this charter |
|-------|---------------------------|
| Production Environment Decision 01 | `RECOMMENDATION_READY` — operator Decision 01 still pending |
| Russian UX Implementation 01 | **Recommended next product wave** |
| Production pilot | Blocked until environment gates **and** UX acceptance |

---

## 6. Risks

| Risk | Mitigation |
|------|------------|
| Partial EN leftovers | Dictionary audit + Visual QA |
| Breaking smoke asserting English strings | Update smoke in same wave |
| Over-scoping full demo CSS port | Ship copy+flow first |
| Fixture labels leaking to “real” mental model | Explicit fixture banner; PDF rules for real vs fixture |
| Footer overclaiming production | Keep «локальный запуск» until production charter says otherwise |

---

## 7. Definition of done (Implementation 01)

- Manager flow screens A–D usable in Russian.  
- Technical details default-collapsed.  
- Footer truthful.  
- Client PDF target applied or explicitly deferred with operator note.  
- Visual QA + closeout report.  
- No production deploy in that wave unless a **separate** explicit production charter says otherwise (default: no).

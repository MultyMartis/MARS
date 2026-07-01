# FP-0002 V8 — Static Client Demo Specification v1

**Date:** 2026-07-01  
**Phase:** 07C execution spec — **do not assemble in 07B**

---

## 1. Authorities

| Authority | Role |
|-----------|------|
| Excel inventory | Expected **client-facing site structure** |
| V8 source + `npm run build` | **Implemented frontend reality** |
| Phase 07C | Reconcile both into standalone demo package |

---

## 2. Excel inventory

| Field | Value |
|-------|-------|
| Path | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` |
| SHA-256 | `64741FDDBD61199D6B3D80E8770576DAE86C374099C6AFEC292F9BD744512696` |
| Size | 14 102 bytes |
| Sheets | `Структура`, `Спрос набросок` (per production standards intake) |

**Rule:** Do not edit Excel in 07B or 07C without operator charter.

---

## 3. Reconciliation model

Each Excel row (URL / page node) receives a **disposition**:

| Disposition | Meaning |
|-------------|---------|
| IMPLEMENTED_DIRECT | V8 page exists; map route in demo |
| IMPLEMENTED_TEMPLATE_REUSE | Clone from template page; swap content |
| IMPLEMENTED_PLACEHOLDER_CONTENT | Route exists with stub copy |
| NEEDS_STATIC_ASSEMBLY | New HTML from template + Excel metadata |
| DEFERRED_NOT_IN_DEMO | Excluded with manifest note |
| REQUIRES_OPERATOR_DECISION | Missing mapping — halt for operator |

**No page may be invented** without explicit mapping decision.

---

## 4. V8 implemented routes (input)

10 pages per [FP-0002-V8-PAGE-AND-ROUTE-REGISTER-v1.md](FP-0002-V8-PAGE-AND-ROUTE-REGISTER-v1.md).

Current `dist/` after clean build is **input** — not automatically final demo (URLs, nav, missing pages).

---

## 5. Proposed Excel row dispositions (high level)

| Excel / IA node | Disposition | Notes |
|-----------------|-------------|-------|
| Home `/` | IMPLEMENTED_DIRECT | `index.html` |
| O-Centre | IMPLEMENTED_DIRECT | |
| Contacts | IMPLEMENTED_DIRECT | |
| Reviews | IMPLEMENTED_DIRECT | |
| Blog archive | IMPLEMENTED_DIRECT | |
| Blog article(s) | IMPLEMENTED_TEMPLATE_REUSE | One fixture; more via template |
| Services hub | IMPLEMENTED_DIRECT | Prefer `uslugi-v2` canonical URL mapping |
| Service section example | IMPLEMENTED_DIRECT | `usluga-podrazdel-v1` |
| Service leaf examples | IMPLEMENTED_TEMPLATE_REUSE | Excel lists many leaves |
| Genotyping leaf | NEEDS_STATIC_ASSEMBLY or DEFERRED | Operator decision in 07C gate |
| Legal hub | NEEDS_STATIC_ASSEMBLY or DEFERRED | Not in V8 |
| 404 | NEEDS_STATIC_ASSEMBLY or DEFERRED | Not in V8 |

**Unresolved:** Full leaf URL list from Excel vs demo scope — **operator review required** in 07C gate 5.

---

## 6. Demo package requirements

| Requirement | Detail |
|-------------|--------|
| Format | Standalone HTML/CSS/JS/assets |
| Paths | Relative only — no `X:\`, no `file://` absolute |
| Direct open | Every page opens from filesystem or static host |
| Navigation | Covers demo structure; active states consistent |
| Forms | Visual-only — labeled in README |
| WordPress | Not required |

---

## 7. Deliverables (07C)

| Artifact | Purpose |
|----------|---------|
| `manifest.json` | Page list, dispositions, versions |
| `checksums.sha256` | Integrity |
| `PAGE-MAP.md` | Human-readable routes |
| `KNOWN-LIMITATIONS.md` | Client expectations |
| `DEPLOY-README.md` | How to host static demo |

---

## 8. Phase 07C gate sequence

1. Excel authority verification (hash + path)  
2. Excel row extraction  
3. Source route inventory  
4. Reconciliation matrix  
5. **Operator review** of missing-page decisions  
6. Static page assembly  
7. Navigation reconciliation  
8. Clean build  
9. Route and asset validation  
10. Client-demo package zip  
11. **No Git checkpoint** until operator review unless explicitly authorized  

---

## 9. Reference

V7 static demo evidence: `workspaces/fp-0002-shpigovsky-v7/plans/static-client-demo/` — **historical process reference**, not V8 output authority.

---

*Static client demo spec — Phase 07C input.*

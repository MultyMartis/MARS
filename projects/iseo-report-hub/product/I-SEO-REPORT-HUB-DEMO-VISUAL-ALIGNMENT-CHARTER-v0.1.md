# I-SEO Report Hub — Demo Visual Alignment Charter v0.1

**Status:** CHARTER / DOCS ONLY — no app-source, runtime, DB, PDF, or share mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-31  
**Wave:** I-SEO Report Hub — Demo Visual Alignment Charter 01  
**Authority:** Operator charter (docs / visual specification)

**Related:**
- [I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md](I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md)
- [I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md](I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md)
- [I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-RUSSIAN-UX-DEMO-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-DEMO-ALIGNMENT-IMPLEMENTATION-RESULT-v0.1.md)
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md)

**Visual reference:** `X:\AI MARS\workspaces\website-factory-operations\iseo-report-hub-prototype\` (static demo **v0.4**)

---

## 1. Purpose

Подготовить точный **visual alignment charter / gap map** для приведения живого PHP+SQL i-SEO Report Hub к визуальному направлению static demo **v0.4**, **без** implementation в этой волне.

Это **docs / planning / visual specification** wave. Следующая implementation wave — отдельно.

---

## 2. Operator feedback captured

| Point | Status |
|-------|--------|
| Laragon запущен; локальный live-интерфейс работает | Confirmed (GET `/health` 200, `/login` 200) |
| Russian UX base принят как нормальный для локального MVP | Accepted baseline after Implementation 01 |
| Live всё ещё визуально не похож на demo v0.4 | Confirmed — dark top-nav shell vs light sidebar shell |
| Полная визуальная натяжка на demo v0.4 ранее **не** ставилась | Confirmed — Implementation 01 reused labels/IA/flow only; **no** CSS shell port |
| Цель: локально привести live UI к demo visual direction, не ломая мотор | In scope for Implementation 02 planning |

---

## 3. Problem statement

| Layer | State after Russian UX Implementation 01 |
|-------|------------------------------------------|
| Language / manager flow | **Russian UX PASS** — A–D screens usable |
| Footer / tech disclosure | Truthful footer; technical details collapsed |
| Visual shell | **Not aligned** — dark `#0f1c24` container + top `site-header` nav |
| Demo v0.4 shell | Light `#f7f7f8` + dark left sidebar + red `#c8102e` accent + wide content |
| PDF / client report | Existing artifact unchanged; not visually aligned to `client-report.html` |

**Вывод:** copy/flow слой принят; следующий слой — **visual shell alignment**, не новый workflow и не PDF regeneration.

---

## 4. Non-goals (this wave)

- No app-source / runtime / DB / SQL / migration edits  
- No share create/revoke; no export/PDF regeneration  
- No demo prototype HTML/CSS/JS edits  
- No production / DNS / HTTPS / server ops  
- No source→runtime sync; no secrets printed  
- No Git push / fetch / pull / reset / clean / stash; no broad `git add`

---

## 5. Decisions (product / visual)

| Decision | Value |
|----------|-------|
| Visual reference | Static demo **v0.4** at `workspaces/website-factory-operations/iseo-report-hub-prototype/` |
| Implementation 02 target | **Close visual shell alignment, not pixel-perfect** |
| Engine / routes / data | **Retain** — no route redesign, no schema, no share/PDF regen |
| Russian copy | **Retain** from Implementation 01 |
| Manager flow | **Retain** (периоды → отчет → файлы → PDF → ссылка → копировать) |
| Client PDF / `client-report.html` | **Separate wave** — not in Implementation 02 |
| Brand mark | **INTLSEO** may remain as brand accent |
| Fixture labels | Demo Client / Demo SEO Project may remain for LOCAL_FIXTURE_ONLY |
| Pixel-perfect | **Not required** unless operator later mandates |

---

## 6. What transfers from demo → live (shell)

**Transfer now (Implementation 02):**
- Left dark sidebar (`#1e293b`) with brand + sectioned nav
- Light main content frame (`#f7f7f8` / white surfaces)
- Red accent `#c8102e` (buttons, active nav border, section numbers optional)
- Card / table / badge / button / alert token patterns inspired by demo CSS
- Wider content area (drop `min(960px, …)` narrow column as primary constraint)
- Topbar / page header pattern instead of full-width dark hero header

**Do not transfer as-is:**
- Demo-only JS fixtures / staged project cards / fake lifecycle %  
- Full specialist workspace UI (no live equivalent yet)  
- Full review queue UI (no live equivalent yet)  
- Full `client-report.html` document chrome into current PDF artifact  
- Prototype banners («Платформа не выбрана», «Демо v0.4») as permanent product chrome

---

## 7. Success criteria (future Implementation 02)

- Live `/` visually resembles demo admin shell (sidebar + light content).  
- Exports / export detail / shares / periods / health (if in scope) share the same shell, typography, buttons, card/table style.  
- Top nav reduced or moved into sidebar (+ compact topbar).  
- Stale dark central skeleton tokens removed from primary chrome.  
- Russian copy retained; manager flow still works.  
- Technical details remain collapsed.  
- Auth / export / share flows still work; DB counts stable; no PDF regen; no share create in smoke unless operator requests.

---

## 8. Recommended next wave

**I-SEO Report Hub — Demo Visual Shell Alignment Implementation 02**

See [I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md).

Separate later:
**I-SEO Report Hub — Client Report Template Visual Alignment Charter 01**

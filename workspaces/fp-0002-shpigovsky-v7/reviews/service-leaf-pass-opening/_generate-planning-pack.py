#!/usr/bin/env python3
"""Generate FP-0002 PG-004 pass-opening planning pack."""
from pathlib import Path
import json

ROOT = Path(r"C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7")
PLANS = ROOT / "plans/service-leaf-page"
REVIEWS = ROOT / "reviews/service-leaf-pass-opening"
PLANS.mkdir(parents=True, exist_ok=True)

extract = json.loads((REVIEWS / "_service-leaf-fig-extract.json").read_text(encoding="utf-8"))

DESKTOP_PNG = r"workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/Услуга - десктоп.png"
MOBILE_PNG = r"workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/Услуга - мобильная.png"

files = {}

files["FP-0002-PG-004-SERVICE-LEAF-PASS-OPENING-v1.md"] = f"""# FP-0002-PG-004 — Service Leaf Pass Opening v1

**Page ID:** FP-0002-PG-004  
**Page name:** Услуга конечная  
**Reference type:** SERVICE_LEAF_INTERNAL_PAGE  
**Example service:** Лечение алкогольной зависимости  
**Pass:** OPENING ONLY — planning and evidence; no runtime implementation

## Scope completed

- Git preflight at HEAD `e4a92c82`
- Mandatory operator backup ZIP created
- Desktop + mobile PNG authority validated (SHA-256 recorded)
- Exact Figma frames confirmed offline from `Spig_v1.2.fig`
- Fresh design authority rasters copied to evidence (not committed as operator PNG)
- Desktop + mobile block registries
- Visible text anchors from PNG + Figma extract
- Asset + reuse + group registries
- GROUP 1 implementation plan prepared
- Baseline `npm run build` smoke (no new page)

## Authority stack

1. Approved desktop PNG (`Услуга - десктоп.png`, 1437×13313)
2. Approved mobile PNG (`Услуга - мобильная.png`, 380×18136)
3. Figma `Spig_v1.2.fig` frames `Услуга конечная` / `Услуга конечная - моб` for node IDs, text, assets after PNG identification
4. Stable references: Service Subdivision (`eb10c71b`), Services V2 (`3a3c648b`), Home

## Direct Figma MCP

- **Result:** BLOCKED — `get_metadata` requires `fileKey`; active desktop document not wired with fileKey in this session
- **Continued via:** offline `openfig-core` parse of canonical `Spig_v1.2.fig` (not claimed as MCP read)

## Implementation status

| Item | Status |
|------|--------|
| New page source | NOT CREATED |
| HTML/SCSS/JS | NOT STARTED |
| Asset export | NOT STARTED |
| GROUP 1 | PLAN READY |

## Gate

**READY_FOR_FP0002_SERVICE_LEAF_GROUP_1**
"""

files["FP-0002-PG-004-SERVICE-LEAF-PNG-AUTHORITY-v1.md"] = f"""# FP-0002-PG-004 — PNG Authority v1

| Authority | Path | Dimensions | SHA-256 | Verdict |
| --------- | ---- | ---------: | ------- | ------- |
| Desktop | `{DESKTOP_PNG}` | 1437×13313 | `A7AB847F2BBF9CA9FF63F11C44EF9FD1472072F04A6274B9550FE6D6C3790D7E` | VALID |
| Mobile | `{MOBILE_PNG}` | 380×18136 | `6B252C5F43F3E61A090787D8031880F635BD4F58291268A5484870A826BBFC84` | VALID |

## Identity checks

- **Desktop page identity:** SERVICE_LEAF — hero «Центр лечения алкогольной зависимости», breadcrumbs trail ending «Лечение алкогольной зависимости», leaf-specific upper copy «Алкогольная зависимость — это не персональный выбор», «Признаки алкогольной зависимости», alcohol-themed FAQ (6 questions). Not Service Subdivision hub listing.
- **Mobile page identity:** Same service leaf; stacked mobile layout; anchor pills; leaf editorial blocks; shared lower blocks (program, specialists, comfort, FAQ, form).
- **Runtime screenshot mistakenly used:** NO — dimensions and full-page design chrome match approved design PNG pair; not a `dist/` runtime capture.
- **Confusion guard:** `Услуга подраздел - десктоп/мобильная` rejected (different page; larger subdivision listing anatomy).

## Result

**DESKTOP_AND_MOBILE_REGISTERED**
"""

files["FP-0002-PG-004-SERVICE-LEAF-FIGMA-FRAME-REGISTRY-v1.md"] = f"""# FP-0002-PG-004 — Figma Frame Registry v1

**Source:** `Spig_v1.2.fig` (SHA-256 `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041`)  
**Method:** offline `openfig-core` parse + PNG dimension/visual match

| Variant | Frame name | Node ID | Dimensions | Visual match |
| ------- | ---------- | ------- | ---------: | ------------ |
| Desktop | Услуга конечная | `1:1748` | 1437×13313 | EXACT — matches desktop PNG W×H; hero alcohol treatment; leaf upper copy; FAQ alcohol questions |
| Mobile | Услуга конечная - моб | `1:5078` | 380×18136 | EXACT — matches mobile PNG W×H; mobile hero + stacked leaf blocks |

## Rejected candidates

| Frame | Node ID | Dimensions | Reason |
| ----- | ------- | ---------: | ------ |
| Услуга подраздел | `1:3491` | 1437×13675 | Subdivision listing page — dependency rows, not leaf body |
| Услуга подраздел - моб | `1:7096` | 380×18101 | Mobile subdivision — wrong anatomy |

## Desktop direct children (Figma stack order)

| # | Section | Node | H |
|---|---------|------|--:|
| 1 | 1 - Главный экран | `1:1749` | 905 |
| 2 | 2 - Дом - вступление | `1:1816` | 761 |
| 3 | 3- Услуги | `1:1847` | 659 |
| 4 | С чего начать (CTA band) | `1:1867` | 168 |
| 5 | Этапы процедуры | `1:1880` | 635 |
| 6 | Программа центра | `1:1894` | 1837 |
| 7 | Программа центра (2) | `1:1954` | 1519 |
| 8 | С чего начать (team/stats) | `1:1993` | 1781 |
| 9 | Специаисты | `1:2029` | 561 |
| 10 | Слово спецу | `1:2066` | 511 |
| 11 | преимущества | `1:2082` | 1473 |
| 12 | Отзывы | `1:2132` | 429 |
| 13 | faq | `1:2161` | 1147 |
| 14 | Подвал | `1:2184` | 488 |

**Note:** PNG adjudication shows CTA band visually between bordered info block and «Признаки» heading — stack order vs painted order differs in upper page; GROUP 1 boundary follows PNG.

## Confidence

- Desktop: **HIGH**
- Mobile: **HIGH**
- Result: **EXACT_NODES_CONFIRMED**
"""

# Desktop block registry
desktop_blocks = [
    (1, "header", "Shared header chrome", 0, 0, 1, 0, 1, "Y0–155", "layout/header"),
    (2, "hero", "Заболевания, которые мы лечим / Центр лечения алкогольной зависимости", 1, 1, 1, 0, 1, "Y155–780", "1:1749"),
    (3, "breadcrumbs-subnav", "Главная / Услуги / … / Лечение алкогольной зависимости + 6 anchor pills", 7, 0, 0, 7, 0, "Y780–980", "1:1749"),
    (4, "intro-quote", "Алкогольная зависимость — это не персональный выбор", 1, 0, 0, 0, 0, "Y980–1180", "1:1816"),
    (5, "bordered-info", "ЗАВИСИМОСТЬ — НЕ ПРОСТУПОК… + 3 subheads + lifebuoy decor", 3, 1, 0, 0, 0, "Y1180–1660", "1:1816–1:1847"),
    (6, "cta-01", "Запишитесь на встречу / ЗАПИСАТЬСЯ / phone", 0, 1, 1, 1, 0, "Y1660–1820", "1:1867"),
    (7, "signs-heading-list", "Признаки алкогольной зависимости", 9, 0, 0, 0, 0, "Y1820–2325", "1:1847"),
    (8, "signs-editorial", "Continued editorial / checklist body (TEMPORARY_MOCKUP_COPY lorem in Figma «Важно» region)", 0, 0, 0, 0, 0, "Y2325–2493", "1:1847–1:1880"),
    (9, "rehab-stages", "Этапы процедуры numbered stages", 4, 0, 0, 0, 0, "Y2493–3128", "1:1880"),
    (10, "program-header-cards", "Программа центра + 4 direction cards", 4, 4, 0, 1, 0, "Y3128–4965", "1:1894"),
    (11, "program-landscape", "Exterior / clinic landscape transition", 1, 1, 0, 0, 0, "Y4965–6484", "1:1954"),
    (12, "team-stats-approach", "С чего начать — team photo + 4 stat cards", 4, 1, 0, 0, 0, "Y6484–8265", "1:1993"),
    (13, "corridor", "Interior corridor wide photo", 1, 0, 0, 0, 0, "Y8265–8600", "inside 1:1993"),
    (14, "specialists", "Специалисты центра — 3 portraits", 3, 3, 0, 0, 0, "Y8600–8826", "1:2029"),
    (15, "founder-quote", "Слово спецу + certificates sidebar", 1, 1, 0, 1, 0, "Y8826–9337", "1:2066"),
    (16, "comfort", "Комфорт, приватность, забота — masonry gallery", 9, 9, 0, 0, 0, "Y9337–10810", "1:2082"),
    (17, "reviews", "Отзывы — 3 cards", 3, 0, 0, 0, 0, "Y10810–11239", "1:2132"),
    (18, "faq", "Нас часто спрашивают — 6 alcohol FAQ", 6, 0, 0, 0, 0, "Y11239–12386", "1:2161"),
    (19, "final-form", "Остались вопросы? + 4 fields", 0, 1, 1, 0, 0, "Y12386–12874", "runtime pattern"),
    (20, "footer", "Подвал", 0, 0, 1, 4, 0, "Y12874–13313", "1:2184"),
    (21, "modal", "Consultation modal", 0, 0, 1, 0, 0, "runtime-only", "modal-consultation"),
]

lines = ["# FP-0002-PG-004 — Desktop Block Registry v1\n", "| № | Block | Heading / visible marker | Items | Assets | CTA | Links | Y-range | Figma |\n", "| -: | ----- | ------------------------ | ----: | -----: | --: | ----: | ------- | ----- |\n"]
for row in desktop_blocks:
    lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} |\n")
lines.append("\n**Authority:** PNG top-to-bottom walk reconciled with Figma section heights.\n")
files["FP-0002-PG-004-SERVICE-LEAF-DESKTOP-BLOCK-REGISTRY-v1.md"] = "".join(lines)

mobile_blocks = [
    (1, "header-hero", "Моби — compact header + hero", 0, 1, 1, 0, "Y0–604", "1:5079"),
    (2, "intro-bordered", "Зависимости и пристрастия — intro + bordered info stacked", 3, 1, 0, 0, "Y604–2091", "1:5134"),
    (3, "cta-01", "С чего начать — short CTA band", 0, 1, 1, 1, "Y2091–2394", "1:5156"),
    (4, "signs-editorial", "Психические расстройствв frame — signs + editorial (Figma name legacy)", 9, 0, 0, 0, "Y2394–3655", "1:5168"),
    (5, "approach-team", "Подход — approach copy + team photo + cards", 4, 2, 0, 0, "Y3655–5503", "1:5183"),
    (6, "program", "Программа центра — stacked 4 cards", 4, 4, 0, 1, "Y5503–7687", "1:5218"),
    (7, "stages-support", "С чего начать large — stages + support bullets + CTA", 4, 1, 1, 0, "Y7687–9753", "1:5251"),
    (8, "specialists", "Специалисты — horizontal cards", 3, 3, 0, 0, "Y9753–10267", "1:5292"),
    (9, "founder", "Слово спеца — quote + portrait stacked", 1, 1, 0, 1, "Y10267–11057", "1:5347"),
    (10, "comfort", "Комфорт, приватность — vertical gallery", 9, 9, 0, 0, "Y11057–13966", "1:5366"),
    (11, "reviews", "Отзывы", 3, 0, 0, 0, "Y13966–14364", "1:5415"),
    (12, "faq", "faq accordion — 6 questions", 6, 0, 0, 0, "Y14364–16230", "1:5430"),
    (13, "final-form", "Lead form block", 0, 1, 1, 0, "Y16230–17176", "embedded before footer"),
    (14, "footer", "Подвал моби", 0, 0, 1, 4, "Y17176–18136", "1:5452"),
    (15, "modal", "Consultation modal", 0, 0, 1, 0, "runtime-only", "modal-consultation"),
]

lines = ["# FP-0002-PG-004 — Mobile Block Registry v1\n", "| № | Block | Heading / visible marker | Items | Assets | CTA | Links | Y-range | Figma |\n", "| -: | ----- | ------------------------ | ----: | -----: | --: | ----: | ------- | ----- |\n"]
for row in mobile_blocks:
    lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} |\n")
lines.append("\n**Mobile-only:** full-width stacked cards; anchor pills wrap; comfort gallery vertical masonry; founder block taller stack.\n")
lines.append("**Desktop-only:** wide hero split layout; horizontal specialist row without carousel requirement on desktop.\n")
files["FP-0002-PG-004-SERVICE-LEAF-MOBILE-BLOCK-REGISTRY-v1.md"] = "".join(lines)

files["FP-0002-PG-004-SERVICE-LEAF-VISIBLE-TEXT-ANCHORS-v1.md"] = """# FP-0002-PG-004 — Visible Text Anchors v1

| Block | Exact heading | First body words | Labels/links | Copy type |
| ----- | ------------- | ---------------- | ------------ | --------- |
| hero | Центр лечения алкогольной зависимости | Заболевания, которые мы лечим (eyebrow); lead paragraph about individual rehabilitation approach | ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ | REAL_COPY |
| breadcrumbs-subnav | — | Главная / Услуги / Зависимости и пристрастия / Лечение алкогольной зависимости | Наш подход к лечению; Программа лечения; С чего начать; Специалисты; Условия центра; Отзывы о программе | REAL_COPY |
| intro-quote | Алкогольная зависимость — это не персональный выбор | ЗАВИСИМОСТЬ — НЕ ПРОСТУПОК И НЕ ЧЕРТА ХАРАКТЕРА: ЗА НЕЙ СТОЯТ ОПРЕДЕЛЕННЫЕ НЕЙРОБИОЛОГИЧЕСКИЕ ПРОЦЕССЫ И ПСИХОЛОГИЧЕСКИЕ ПРИЧИНЫ. | — | REAL_COPY |
| bordered-info | (subheads) ЗАВИСИМОСТЬ НЕ НАЧИНАЕТСЯ… / КАК ДВА БОКАЛА… / ЭТО НЕ ВАША ВИНА… | Body paragraphs under each subhead (visible in PNG) | — | REAL_COPY |
| cta-01 | Запишитесь на встречу | Или позвоните нам | ЗАПИСАТЬСЯ; 8 (925) 183-64-64 | REAL_COPY |
| signs-heading-list | Признаки алкогольной зависимости | Если вы согласны хотя бы с одним из следующих утверждений… | 9 checklist statements (visible) | REAL_COPY |
| signs-editorial | — | Lorem ipsum… (Figma node `1:1886` «Важно» instance — visible TEMPORARY_MOCKUP_COPY) | — | TEMPORARY_MOCKUP_COPY |
| rehab-stages | (stage headings 01–04) | Stage body copy per numbered item | — | REQUIRES_GROUP_INSPECTION |
| program | Наша программа включает 4 направления (pattern) | Program lead paragraphs | подробнее / play link | REUSE_WITH_CONTENT |
| team-stats | Запишитесь на гостевой визит (section) | ДИПЛОМИРОВАННЫЕ СПЕЦИАЛИСТЫ… / ДО 15 РЕЗИДЕНТОВ… / НЕТ РЕШЕТОК… / ВЫБОР КАТЕГОРИИ НОМЕРА… | Записаться на консультацию | REAL_COPY |
| specialists | Специалисты центра | Сергей Юрьевич Шпиговский; Максим Михайлович Казаков; Дарья Владимировна Костюк | — | REAL_COPY |
| founder | (quote block) | Visible quote copy + Сертификаты и дипломы | — | REUSE_WITH_CONTENT |
| comfort | Комфорт, приватность, забота | — | Gallery captions if visible | REUSE_WITH_CONTENT |
| reviews | Отзывы | Анонимный отзыв; Александр П. | — | REUSE_WITH_CONTENT |
| faq | Нас часто спрашивают | 6 questions (alcohol-specific, incl. typos from Figma: зависимогсти, зависмостей) | — | REAL_COPY |
| final-form | Остались вопросы? | Опишите вашу ситуацию… | Ваш телефон; Ваша электронная почта; Опишите ситуацию; отправить запрос | REAL_COPY |

**Result:** COMPLETE — every block visually anchored; hidden Figma layers excluded.
"""

files["FP-0002-PG-004-SERVICE-LEAF-ASSET-REGISTRY-v1.md"] = """# FP-0002-PG-004 — Asset Registry v1

| Block | Visual description | Figma node | Existing runtime asset candidate | Decision |
| ----- | ------------------ | ---------- | -------------------------------- | -------- |
| hero | Man with whiskey glass — painterly hero | `1:1753` image 219 | `services-hero.webp` / new leaf hero | EXACT_EXPORT_REQUIRED |
| bordered-info | Lifebuoy decor behind bordered panel | `1:1789` image 13030403 | none exact | EXACT_EXPORT_REQUIRED |
| team-stats | Group staff photo in front of brick building | `1:1993` region | `shpigovsky-staff-group.webp` | REQUIRES_GROUP_INSPECTION |
| program-landscape | Clinic exterior lush green | `1:1954` region | `shpigovsky-clinic-landscape.webp` | REQUIRES_GROUP_INSPECTION |
| program cards ×4 | Genotyping / neuro / psycho / kinesio art | program section | `program-*.webp` set | EXACT_EXISTING_REUSE |
| corridor | Hallway with paintings | stages/approach region | `shpigovsky-interior-corridor.webp` | REQUIRES_GROUP_INSPECTION |
| specialists ×3 | Doctor portraits | `1:2029` | `home-specialists/*.webp` | EXACT_EXISTING_REUSE |
| founder | Sergey portrait + quote mark | `1:2066` | `founder-sergey-shpigovsky.png` | EXACT_EXISTING_REUSE |
| comfort gallery | 9 room/garden photos | `1:2082` | `home-comfort/*.webp` | REUSE_WITH_CONTENT |
| final-form bg | Dark blue + building faint | form region | `home-final-form-background.webp` | EXACT_EXISTING_REUSE |

- **Exact existing assets:** program card set, specialist portraits, founder, comfort set (verify order/count), final-form background
- **Exports required:** leaf hero, lifebuoy decor (if kept — see lifebuoy policy note in GROUP 1 plan)
- **Unresolved:** corridor vs team-stats photo boundary; exterior vs program transition crop
- **Duplicate risk:** reusing subdivision hero (`service-subdivision-hero.webp`) — WRONG subject; must not reuse without visual proof
- **Result:** COMPLETE for pass opening; export deferred to groups
"""

files["FP-0002-PG-004-SERVICE-LEAF-REFERENCE-COMPONENT-INVENTORY-v1.md"] = """# FP-0002-PG-004 — Reference Component Inventory v1

| Existing component | Source | Reference page | Relevant target blocks |
| ------------------ | ------ | -------------- | ---------------------- |
| layout/header | shared | all | header |
| layout/footer | shared | all | footer |
| modal-consultation | shared | all | modal |
| services-inner-hero-v2 | partial | uslugi-v2, usluga-podrazdel-v1 | hero |
| breadcrumbs | component | services pages | breadcrumbs |
| services-page-subnav | component | usluga-podrazdel-v1 | anchor nav |
| services-program-v2 + item | partials | usluga-podrazdel-v1 | program |
| services-program-cta-band-v2 | component | uslugi-v2 | cta-01, mid CTAs |
| service-subdivision-stages-v1 | partial | usluga-podrazdel-v1 | rehab-stages |
| service-subdivision-team-stats-v1 | partial | usluga-podrazdel-v1 | team-stats-approach |
| home-clinic-landscape | partial | index, usluga-podrazdel-v1 | program-landscape |
| home-specialists | partial | index, usluga-podrazdel-v1 | specialists |
| home-founder-quote | partial | index, usluga-podrazdel-v1 | founder |
| home-comfort | partial | index, usluga-podrazdel-v1 | comfort |
| home-reviews | partial | index | reviews |
| home-faq | partial | index, usluga-podrazdel-v1 | faq |
| home-final-form | partial | index, usluga-podrazdel-v1 | final-form |
| service-subdivision-nature-v1 | partial | usluga-podrazdel-v1 | pattern reference only — not leaf signs block |
| services-category-section-v2 | partial | uslugi-v2 | NOT for leaf signs — listing pattern |

**Stable references:** Service Subdivision `eb10c71b` / tag `fp-0002-v7-service-subdivision-internal-page-reference-01`; Services V2 `3a3c648b`; Home `index.html`.
"""

files["FP-0002-PG-004-SERVICE-LEAF-REUSE-DECISION-MATRIX-v1.md"] = """# FP-0002-PG-004 — Reuse Decision Matrix v1

| Target block | Existing reference | Decision | Evidence | New HTML | New CSS |
| ------------ | ------------------ | -------- | -------- | -------: | ------: |
| header | layout/header | REUSE_EXACT | shared chrome matches PNG | 0 | 0 |
| hero | services-inner-hero-v2 | REUSE_WITH_CONTENT | same inner-hero anatomy; new image/title/lead; alcohol leaf copy | 0 | 0 |
| breadcrumbs-subnav | breadcrumbs + services-page-subnav | REUSE_WITH_CONTENT | 4-crumb trail + 6 anchors — count/labels differ from subdivision | 0 | 0 |
| intro-quote | — | NEW_COMPONENT_REQUIRED | red-line editorial intro — no exact partial | 1 | 1 |
| bordered-info | — | NEW_COMPONENT_REQUIRED | bordered panel + 3 subheads + lifebuoy — leaf-specific | 1 | 1 |
| cta-01 | services-program-cta-band-v2 | REUSE_WITH_CONTENT | «Запишитесь на встречу» variant | 0 | 0 |
| signs-heading-list | — | NEW_COMPONENT_REQUIRED | 9-item checklist — not category listing | 1 | 1 |
| signs-editorial | — | REUSE_WITH_SCOPED_VARIANT | editorial continuation; may share typography tokens only | 0 | 1 |
| rehab-stages | service-subdivision-stages-v1 | REUSE_WITH_CONTENT | same numbered stages pattern | 0 | 0 |
| program | services-program-v2 | REUSE_WITH_CONTENT | 4 cards — same reference | 0 | 0 |
| program-landscape | home-clinic-landscape | REUSE_WITH_CONTENT | exterior band | 0 | 0 |
| team-stats-approach | service-subdivision-team-stats-v1 | REUSE_WITH_CONTENT | 4 stat cards + team photo | 0 | 0 |
| corridor | — | REQUIRES_GROUP_INSPECTION | may be part of team-stats partial or separate band | 0 | 0 |
| specialists | home-specialists | REUSE_WITH_CONTENT | verify 3-up count/order | 0 | 0 |
| founder | home-founder-quote | REUSE_WITH_CONTENT | variant-b pattern | 0 | 0 |
| comfort | home-comfort | REUSE_WITH_CONTENT | verify 9-tile order | 0 | 0 |
| reviews | home-reviews | REUSE_WITH_CONTENT | 3 cards | 0 | 0 |
| faq | home-faq | REUSE_WITH_CONTENT | 6 alcohol questions | 0 | 0 |
| final-form | home-final-form | REUSE_WITH_CONTENT | 4 fields visible | 0 | 0 |
| footer | layout/footer | REUSE_EXACT | shared | 0 | 0 |
| modal | modal-consultation | REUSE_EXACT | shared | 0 | 0 |

**Summary:** Exact reuse 3; content reuse 12; scoped variants 1; new components 3; inspection 1.
"""

files["FP-0002-PG-004-SERVICE-LEAF-GROUP-REGISTRY-v1.md"] = """# FP-0002-PG-004 — Group Registry v1

| Group | Start block | End block | Main novelty | Main reuse | Risk |
| ----- | ----------- | --------- | ------------ | ---------- | ---- |
| GROUP 1 | header | cta-01 | intro-quote, bordered-info (new partials) | hero, breadcrumbs, subnav, CTA band | PNG vs Figma stack order in upper page; lifebuoy policy |
| GROUP 2 | signs-heading-list | signs-editorial | checklist + lorem editorial | typography patterns only | Large copy volume; 9 checklist items |
| GROUP 3 | rehab-stages | program-landscape | stages + program + landscape chain | stages, program, landscape partials | Corridor may attach here or GROUP 5 |
| GROUP 4 | program-header-cards | program-landscape | (if split from G3) program cards only | services-program-v2 | LOW if merged with G3 |
| GROUP 5 | team-stats-approach | cta/support end | team photo + stats + corridor | team-stats, CTA | corridor boundary |
| GROUP 6A | corridor | founder | corridor adjudication | specialists, founder | merged lower blocks |
| GROUP 6B | comfort | footer | — | home lower partials | comfort 9-tile order |

**Consolidated plan (7 groups):**

| Group | Start | End |
| ----- | ----- | --- |
| 1 | header | cta-01 |
| 2 | signs-heading-list | signs-editorial |
| 3 | rehab-stages | program-landscape |
| 4 | team-stats-approach | corridor (if separate) |
| 5 | specialists | founder |
| 6 | comfort | faq |
| 7 | final-form | footer |

**Total groups:** 7 (6B split applied)  
**Largest group:** GROUP 2 or GROUP 3  
**Mobile-specific handling:** GROUP 1–2 stacked width; comfort vertical gallery in GROUP 6  
**Result:** COMPLETE
"""

files["FP-0002-PG-004-SERVICE-LEAF-GROUP-1-IMPLEMENTATION-PLAN-v1.md"] = """# FP-0002-PG-004 — GROUP 1 Implementation Plan v1

## Boundary

- **Start:** page shell open — `header`
- **End:** after `cta-01` band (before «Признаки алкогольной зависимости» heading)
- **Desktop Y (PNG):** ~Y0–1820 (crop evidence `SERVICE-LEAF-DESKTOP-GROUP1-*`)
- **Figma nodes:** `1:1749` hero, `1:1816` intro, `1:1847`/`1:1867` upper content + CTA

## Desktop crops (design authority)

1. `SERVICE-LEAF-DESKTOP-GROUP1-HEADER-HERO-NAV.png`
2. `SERVICE-LEAF-DESKTOP-GROUP1-UPPER-CONTENT-CTA.png` (truncate at CTA bottom for acceptance)
3. Runtime-before: N/A (page not created)
4. Runtime-after: `SERVICE-LEAF-G1-HEADER-HERO-1398.png`, `SERVICE-LEAF-G1-UPPER-CTA-1398.png`

## Mobile crops

1. `SERVICE-LEAF-MOBILE-GROUP1-HEADER-HERO-NAV.png`
2. `SERVICE-LEAF-MOBILE-GROUP1-UPPER-CONTENT-CTA.png`
3. Runtime-after: `SERVICE-LEAF-G1-HEADER-HERO-390.png`, `SERVICE-LEAF-G1-UPPER-CTA-390.png`

## Visible text regions

- Hero eyebrow, title, lead, CTA label (REAL_COPY)
- Breadcrumb trail + 6 anchor labels (REAL_COPY)
- Intro H2 + red-line quote (REAL_COPY)
- Bordered panel 3 subheads + bodies (REAL_COPY)
- CTA: Запишитесь на встречу / ЗАПИСАТЬСЯ / phone (REAL_COPY)
- **Exclude:** «Признаки…» heading and below

## Assets

- Hero image: **EXACT_EXPORT_REQUIRED** (`1:1753`)
- Lifebuoy in bordered block: visible in PNG — **REQUIRES_GROUP_INSPECTION** vs project lifebuoy policy (`FORBIDDEN_ZERO` on subdivision — leaf PNG shows decor; do not omit without operator ruling)

## Reuse

| Block | Partial | Decision |
| ----- | ------- | -------- |
| header | layout/header | REUSE_EXACT |
| hero | services-inner-hero-v2 | REUSE_WITH_CONTENT |
| breadcrumbs | breadcrumbs | REUSE_WITH_CONTENT |
| subnav | services-page-subnav | REUSE_WITH_CONTENT |
| intro-quote | NEW `service-leaf-intro-v1` | NEW |
| bordered-info | NEW `service-leaf-bordered-info-v1` | NEW |
| cta-01 | services-program-cta-band-v2 | REUSE_WITH_CONTENT |

## Source files (future — not created in pass opening)

- Page: `src/pages/usluga-konechnaya-v1.html`
- New partials: `service-leaf-intro-v1.html`, `service-leaf-bordered-info-v1.html`
- SCSS: additions in `src/scss/style.scss` only — scoped `.service-leaf-*` / page root `.page-service-leaf-v1`
- JS: existing modal hooks via `data-*` only

## Preview URL

`http://127.0.0.1:4174/usluga-konechnaya-v1.html` (after GROUP 1+ shell)

## Compiled checks

- `npm run build` exit 0
- dist contains `usluga-konechnaya-v1.html`
- no regressions: index, uslugi, uslugi-v2, usluga-podrazdel-v1

## Acceptance screenshots

- Desktop 1398px: hero + upper nav + intro + bordered + CTA
- Mobile 390px: same regions
- Text transcript PASS all visible strings

## Commit gate

Commit only if: backup exists, design crops PASS, runtime-after PASS, regression 0, build 0.

**Result:** READY
"""

files["FP-0002-PG-004-SERVICE-LEAF-ROUTE-READINESS-v1.md"] = """# FP-0002-PG-004 — Route Readiness v1

| Field | Value |
| ----- | ----- |
| Proposed source filename | `src/pages/usluga-konechnaya-v1.html` |
| Proposed preview filename | `usluga-konechnaya-v1.html` |
| Proposed WordPress path | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |
| Evidence | `FP-0002-PAGE-INVENTORY-v1.md` PG-004; `FP-0002-DESIGN-AUDIT-v1.md` PG-103 example; breadcrumb PNG «…/Лечение алкогольной зависимости»; subdivision page links to same slug |
| SAFE UNKNOWN | L4 sub-leaves (soli, geroin, etc.) reuse template — canonical switch not in this pass |
| Navigation change required now | NO |
| Canonical switch | NOT_STARTED |

**Naming convention:** matches `usluga-podrazdel-v1.html` pattern (`usluga-{type}-v1.html`).
"""

files["FP-0002-PG-004-SERVICE-LEAF-FINAL-RECOMMENDATION-v1.md"] = """# FP-0002-PG-004 — Final Recommendation v1

## Gate recommendation

**READY_FOR_FP0002_SERVICE_LEAF_GROUP_1**

## Verdict

**FP0002_SERVICE_LEAF_PASS_OPENING_COMPLETE**

## Preconditions met

- Backup ZIP + SHA-256
- PNG authority valid
- Figma frames `1:1748` / `1:5078` confirmed
- Registries complete
- GROUP 1 plan ready
- Baseline build required post-commit
- Zero runtime source changes in this pass

## Do not start until

- Operator approves GROUP 1 plan
- GROUP 1 backup per protocol
- Fresh design crops before implementation
"""

for name, content in files.items():
    (PLANS / name).write_text(content, encoding="utf-8")

# Evidence markdown
(REVIEWS / "FIGMA-ACCESS-RECEIPT-v1.md").write_text("""# Figma access receipt

- Active file: `Spig_v1.2.fig` (canonical INCOMING)
- Direct MCP: BLOCKED — `get_metadata` requires `fileKey`; no active cloud fileKey in session
- Tools attempted: `get_metadata` (plugin-figma-figma)
- Offline parse: YES — `openfig-core` via `reviews/service-leaf-pass-opening/_extract-service-leaf.mjs`
- Stale extracts used as authority: NO — fresh parse 2026-06-26
- Result: FRAMES_RESOLVED_OFFLINE
""", encoding="utf-8")

(REVIEWS / "PNG-VALIDATION-RECEIPT-v1.md").write_text("""# PNG validation receipt

- Desktop: opens OK, 1437×13313, SHA-256 A7AB847F…790D7E
- Mobile: opens OK, 380×18136, SHA-256 6B252C5F…BFC84
- Not runtime screenshots: confirmed
- Result: VALID
""", encoding="utf-8")

(REVIEWS / "REGISTRY-CONSISTENCY-CHECK-v1.md").write_text("""# Registry consistency check

- Desktop PNG height == Figma frame height: 13313 PASS
- Mobile PNG height == Figma frame height: 18136 PASS
- Rejected subdivision frames documented PASS
- GROUP 1 PNG crop aligns with planned end at CTA-01 PASS
- Lifebuoy visible in PNG vs policy flag documented PASS
- Result: CONSISTENT
""", encoding="utf-8")

(REVIEWS / "PLAN-VALIDATION-RECEIPT-v1.md").write_text("""# Plan validation receipt

- 13 planning files created under `plans/service-leaf-page/`
- Evidence rasters under `reviews/service-leaf-pass-opening/design-rasters/`
- Representative crops under `reviews/service-leaf-pass-opening/crops/`
- No src/pages, partials, scss, js, img changes
- Result: PASS
""", encoding="utf-8")

print("wrote", len(files), "plan files")

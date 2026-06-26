"""Generate GROUP 1 evidence markdown pack."""
from datetime import datetime, timezone
from pathlib import Path

review = Path(__file__).parent
ts = datetime.now(timezone.utc).isoformat()
zip_sha = "F4777376206DC2A3D517CB5E41C74178B763B07414A55F36E70F7C5F0B8DF120"

docs = {
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-BACKUP-v1.md": f"""# BACKUP v1

- ZIP: `C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v7\\operator-checkpoints\\FP-0002-V7-PG-004-SERVICE-LEAF-GROUP-1-BEFORE-SOURCE.zip`
- SHA-256: `{zip_sha}`
- HEAD: `624492b3`
- Entries: 142
- Verdict: COMPLETE
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-AUTHORITY-v1.md": """# AUTHORITY v1

- Desktop PNG: `Услуга - десктоп.png` SHA `A7AB847F…D7E`
- Mobile PNG: `Услуга - мобильная.png` SHA `6B252C5F…C84`
- Figma desktop `1:1748` 1437×13313; mobile `1:5078` 380×18136
- Stale JSON: not used as visual authority
- Verdict: PASS
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-BOUNDARY-v1.md": """# BOUNDARY v1

- Start: header
- End: after CTA-01 (`service-leaf-cta-01-v1`)
- Next block: «Признаки алкогольной зависимости» — NOT IMPLEMENTED
- Marker: `<!-- SERVICE-LEAF-GROUP-1-BOUNDARY -->`
- Desktop Y ~0–1820; mobile boundary crop `SERVICE-LEAF-M-G1-06-BOUNDARY.png`
- Verdict: PASS
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-DESIGN-CROPS-v1.md": """# DESIGN CROPS v1

Desktop: `design-crops/desktop/SERVICE-LEAF-D-G1-01..06-*.png`
Mobile: `design-crops/mobile/SERVICE-LEAF-M-G1-01..06-*.png`
- Verdict: COMPLETE
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-TEXT-TRANSCRIPT-v1.md": """# TEXT TRANSCRIPT v1

| Region | Exact visible text | CTA/link | Copy type |
|---|---|---|---|
| Hero eyebrow | Заболевания, которые мы лечим | — | REAL_COPY |
| Hero title | Центр лечения алкогольной зависимости | — | REAL_COPY |
| Hero description | В центре реабилитации Шпиговский Дом мы понимаем, что каждый человек уникален, поэтому мы не предложим вам универсальный подход к лечению. Путь в борьбе с алкогольной зависимостью может быть только индивидуальным. | — | REAL_COPY |
| Hero CTA | Записаться на консультацию | modal | REAL_COPY |
| Breadcrumb 1 | Главная | / | REAL_COPY |
| Breadcrumb 2 | Услуги | /uslugi-v2.html | REAL_COPY |
| Breadcrumb 3 | Зависимости и пристрастия | /usluga-podrazdel-v1.html | REAL_COPY |
| Breadcrumb 4 | Лечение алкогольной зависимости | current | REAL_COPY |
| Subnav ×6 | Наш подход к лечению; Программа лечения; С чего начать; Специалисты; Условия центра; Отзывы о программе | section anchors | REAL_COPY |
| Intro heading | Алкогольная зависимость — это не персональный выбор | — | REAL_COPY |
| Intro lead | ЗАВИСИМОСТЬ — НЕ ПРОСТУПОК И НЕ ЧЕРТА ХАРАКТЕРА: ЗА НЕЙ СТОЯТ ОПРЕДЕЛЕННЫЕ НЕЙРОБИОЛОГИЧЕСКИЕ ПРОЦЕССЫ И ПСИХОЛОГИЧЕСКИЕ ПРИЧИНЫ. | — | REAL_COPY |
| Bordered h1 | ЗАВИСИМОСТЬ НЕ НАЧИНАЕТСЯ С ЖЕЛАНИЯ РАЗРУШИТЬ СЕБЯ | — | REAL_COPY |
| Bordered h2 | КАК ДВА БОКАЛА ПРЕВРАЩАЮТСЯ В БУТЫЛКУ С УТРА | — | REAL_COPY |
| Bordered h3 | ЭТО НЕ ВАША ВИНА — И ВЫХОД ЕСТЬ | — | REAL_COPY |
| CTA-01 heading | Запишитесь на встречу | — | REAL_COPY |
| CTA-01 supporting | Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам. | — | REAL_COPY |
| CTA-01 phone | 8 (925) 183-64-64 | tel | REAL_COPY |
| CTA-01 hint | Или позвоните нам | — | REAL_COPY |
| CTA-01 button | Записаться | modal `service-leaf-cta-01` | REAL_COPY |

- Verdict: COMPLETE
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-LIFEBUOY-OVERRIDE-v1.md": """# LIFEBUOY OVERRIDE v1

- Design presence in bordered block: YES (PNG/Figma decor)
- Operator decision: `LIFEBUOY DECOR — FORBIDDEN_ZERO`
- Runtime markup: 0
- Runtime asset refs: 0
- Reserved blank space: 0
- Evidence: `OPERATOR_OVERRIDE_OMITTED_FROM_RUNTIME`
- Verdict: PASS (allowed deviation)
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-HERO-v1.md": """# HERO v1

- Partial: `services-inner-hero-v2` REUSE_WITH_CONTENT
- Asset: `service-leaf-alcohol-hero.webp` (Figma node `1:1789`, hash `692745a6…`)
- Dimensions: 850×567
- Desktop/mobile: PASS vs PNG crops
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-COMPILED-VALIDATION-v1.md": """# COMPILED VALIDATION v1

See `qa-results.json`. Key counts: page class 1, hero asset 1, bordered subsections 3, boundary 1, lifebuoy 0, template garbage 0, duplicate IDs 0.
- Verdict: PASS
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-DESKTOP-ACCEPTANCE-v1.md": """# DESKTOP ACCEPTANCE v1

| Region | Visual | Text | Structure | Count | Asset | Order | Final |
|---|---|---|---|---|---|---|---|
| Header | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Hero | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Breadcrumbs | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Subnav | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Intro quote | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Bordered info | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| CTA-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Boundary | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

Lifebuoy omission: operator override — not FAIL.
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-MOBILE-ACCEPTANCE-v1.md": """# MOBILE ACCEPTANCE v1

| Region | Visual | Text | Structure | Count | Asset | Order | Final |
|---|---|---|---|---|---|---|---|
| Header | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Hero | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Breadcrumbs | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Subnav | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Intro quote | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Bordered info | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| CTA-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Boundary | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-REGRESSION-v1.md": """# REGRESSION v1

- Home HTML: unchanged source
- Services V1 HTML: unchanged source
- Services V2 HTML: breadcrumb include params only (`crumbMiddle2` empty) — compiled nav unchanged
- Service Subdivision HTML: breadcrumb include params only — compiled nav unchanged
- Shared partials: `breadcrumbs.html` optional 4th level; no output change when empty
- SCSS: only `.page-service-leaf-v1` scoped additions
- Regression count: 0
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-1-FINAL-v1.md": f"""# FINAL v1

- Timestamp: {ts}
- GROUP 1: COMPLETE
- Desktop: PASS
- Mobile: PASS
- Build: exit 0
- Gate: `READY_FOR_FP0002_SERVICE_LEAF_GROUP_1_OPERATOR_REVIEW`
""",
}

for name, body in docs.items():
    (review / name).write_text(body, encoding="utf-8")
print("wrote", len(docs), "evidence files")

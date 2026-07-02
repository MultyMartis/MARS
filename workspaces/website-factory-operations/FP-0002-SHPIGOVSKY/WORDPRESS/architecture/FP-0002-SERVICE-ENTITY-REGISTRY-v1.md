# FP-0002 Service Entity Registry v1

**Task:** V9-06A.1 | **Date:** 2026-07-03  
**Authority:** [FP-0002-SERVICE-ENTITY-REGISTRY-v1.json](FP-0002-SERVICE-ENTITY-REGISTRY-v1.json)

Machine registry: 15 Service entities. `/uslugi/` hub Page is **excluded**. `/uslugi/genotipirovanie/` is **excluded**.

---

## Summary

| Metric | Value |
|--------|------:|
| Service records | 15 |
| Parent services (depth 1) | 3 |
| Leaf services (depth 2) | 12 |
| Page→Service migration | 3 |
| Create new Service | 12 |
| Alcohol-special | 1 |
| Services hub as Service | **NO** |
| Genotipirovanie as Service | **NO** |

---

## 15-Service table

| service_id | Route | Title | Parent | Role | Layout | Migration |
|------------|-------|-------|--------|------|--------|-----------|
| SVC-ZAVISIMOSTI | `/uslugi/zavisimosti/` | Зависимости | — | parent | subdivision | MIGRATE_PAGE_TO_SERVICE |
| SVC-ALKOGOL | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Лечение алкогольной зависимости | SVC-ZAVISIMOSTI | leaf | **alcohol-special** | CREATE_SERVICE |
| SVC-PROFILAKTIKA | `/uslugi/zavisimosti/profilakticheskiy-analiz/` | Профилактический анализ | SVC-ZAVISIMOSTI | leaf | placeholder | CREATE_SERVICE |
| SVC-SPECIALISTAM-ZAV | `/uslugi/zavisimosti/specialistam/` | Специалистам | SVC-ZAVISIMOSTI | leaf | placeholder | CREATE_SERVICE |
| SVC-PSYCH | `/uslugi/psihicheskoe-zdorovie/` | Психическое здоровье | — | parent | subdivision | MIGRATE_PAGE_TO_SERVICE |
| SVC-DEPRESSIYA | `/uslugi/psihicheskoe-zdorovie/depressiya/` | Депрессия | SVC-PSYCH | leaf | placeholder | CREATE_SERVICE |
| SVC-PTRS | `/uslugi/psihicheskoe-zdorovie/ptrs/` | ПТСР | SVC-PSYCH | leaf | placeholder | CREATE_SERVICE |
| SVC-VYGORANIE | `/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/` | Эмоциональное выгорание | SVC-PSYCH | leaf | placeholder | CREATE_SERVICE |
| SVC-TREVOGA | `/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/` | Тревожные расстройства | SVC-PSYCH | leaf | placeholder | CREATE_SERVICE |
| SVC-SON | `/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/` | Расстройства сна | SVC-PSYCH | leaf | placeholder | CREATE_SERVICE |
| SVC-TRAVMA | `/uslugi/psihicheskoe-zdorovie/travma/` | Травма | SVC-PSYCH | leaf | placeholder | CREATE_SERVICE |
| SVC-RPP | `/uslugi/rasstroystva-pischevogo-povedeniya/` | Расстройства пищевого поведения | — | parent | subdivision | MIGRATE_PAGE_TO_SERVICE |
| SVC-ANOREKSIYA | `/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/` | Нервная анорексия | SVC-RPP | leaf | placeholder | CREATE_SERVICE |
| SVC-BULIMIYA | `/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/` | Нервная булимия | SVC-RPP | leaf | placeholder | CREATE_SERVICE |
| SVC-KOMPULSIV | `/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/` | Компульсивное переедание | SVC-RPP | leaf | placeholder | CREATE_SERVICE |

---

## Hierarchy

```text
/uslugi/                          ← PAGE (services_hub) — NOT in this registry
├── zavisimosti/                    SVC-ZAVISIMOSTI
│   ├── lechenie-alkogolnoy-zavisimosti/   SVC-ALKOGOL (alcohol-special)
│   ├── profilakticheskiy-analiz/          SVC-PROFILAKTIKA
│   └── specialistam/                      SVC-SPECIALISTAM-ZAV
├── psihicheskoe-zdorovie/          SVC-PSYCH
│   ├── depressiya/                 SVC-DEPRESSIYA
│   ├── ptrs/                       SVC-PTRS
│   ├── emocionalnoe-vygoranie/     SVC-VYGORANIE
│   ├── trevozhnye-rasstroystva/    SVC-TREVOGA
│   ├── rasstroystva-sna/           SVC-SON
│   └── travma/                     SVC-TRAVMA
└── rasstroystva-pischevogo-povedeniya/  SVC-RPP
    ├── anoreksiya/                 SVC-ANOREKSIYA
    ├── nervnaya-bulimiya/          SVC-BULIMIYA
    └── kompulsivnoe-pereedanie/    SVC-KOMPULSIV
```

---

*Review view — planning authority only.*

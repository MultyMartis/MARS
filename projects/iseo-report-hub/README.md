# i-SEO Report Hub

**project_id:** `iseo-report-hub`  
**Статус:** planned / product architecture  
**Lane:** Lane B — product formation and architecture  
**Реестр:** [registry/project-registry.md](../../registry/project-registry.md)

**Навигация сессии:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

## Назначение

**i-SEO Report Hub** — внутренний reporting workspace для i-SEO: подготовка, управление, ревью, публикация и доставка SEO-отчётов клиентам.

Это **не** просто PDF-генератор. Это операционная система отчётности, где финальный отчёт — структурированный рендер цикла отчётности, weekly checkpoints, monthly final report, work log, метрик, evidence, комментариев SEO-специалиста, approvals и состояния export/publication.

---

## Каноническая архитектура (кратко)

| Компонент | Роль |
|-----------|------|
| **WordPress на i-seo.su** | Source of truth Report Hub; admin/workspace SEO-специалистов; рендер client web reports |
| **n8n** | Внешний automation/AI helper; **не** source of truth |
| **MVP** | Internal-first; controlled client web report links |

---

## Канонические документы

| Документ | Назначение |
|----------|------------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Навигация и operating rules программы |
| [product/I-SEO-REPORT-HUB-PRODUCT-CHARTER-v0.1.md](product/I-SEO-REPORT-HUB-PRODUCT-CHARTER-v0.1.md) | Утверждённый charter |
| [product/I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md](product/I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md) | WordPress-архитектура |
| [product/I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](product/I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md) | Модель отчётности |
| [product/I-SEO-REPORT-HUB-MVP-SCOPE-v0.1.md](product/I-SEO-REPORT-HUB-MVP-SCOPE-v0.1.md) | MVP in/out |

---

## Предупреждения

- **Runtime/code в этой программе пока отсутствует** — только documentation-first persist.
- **Секреты и access-материалы не включаются** в product docs, client reports, AI prompts или exports.
- **API-интеграции не реализованы** — MVP может стартовать без API.
- **n8n workflows для Report Hub не существуют** — только boundary и event model для будущего.
- **Client portal с login не входит в MVP.**

---

## Source corpus (evidence)

**Расположение:** `X:\AI MARS STORAGE\incoming\iseo-report-hub\`

Известные папки: materials from Nikita, reports from Denis, reports from Ilya. Полный re-audit корпуса **не** входит в текущую задачу.

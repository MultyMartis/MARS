# OCPilot

**Classification:** Program / Operational System (MARS External Systems lane).  
**Chat type:** External Systems.  
**Status:** Phase 0 skeleton + Run 1.5 alignment — documentation baseline only; **no runtime claimed**.  
**Registry:** `ocpilot` — [registry/project-registry.md](../../registry/project-registry.md)  
**Model reference:** [System Entity Model](../../governance/system-entity-model.md).  
**Family:** [CMS / Ecommerce Pilots](cms-ecommerce-pilots-family.md) — OCPilot is a standalone member, not a child of WPilot.

OCPilot — **самостоятельная** human-supervised система MARS для AI-assisted работы с **OpenCart / ocStore**: инспекция, разделение core/custom, подготовка контролируемых изменений каталога, темы и backend. Не дочерний проект WPilot.

## Что такое OCPilot

- Документационно-операционный пакет под `projects/ocpilot/`.
- OpenCart-specific **bridge system**: файлы, БД, каталог, темы, модули, ocMod/vQmod (если есть).
- Human-supervised workflow: read-only аудит → паспорт сайта → сравнение с versioned clean baseline → план → HITL перед любыми записями.
- Целевые сценарии (планируемые, не заявленные как runtime): адаптация дилерских OpenCart-сайтов, battle pilot read-only, будущий controlled catalog import, будущие theme/controller changes.

## Чем OCPilot не является

- Не автономный OpenCart-админ и не deploy-bot.
- Не компонент WPilot, ORCA или mars-survivability (только **паттерны**, не наследование реализации).
- Не MARS runtime, не orchestration product, не proof хостинга/FTP/PMA/браузера.
- Не хранилище credentials, дампов БД с секретами, production-файлов клиента в git.
- Не заявление о существующих плагинах, адаптерах или live-интеграциях — пока нет кода в-repo.

## CMS / Ecommerce Pilots family

OCPilot входит в архитектурное семейство **CMS / Ecommerce Pilots** вместе с WPilot (WordPress), возможным MODxPilot и CustomSitePilot. См. [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md). JoomlaPilot не планируется.

## Sibling-связь с WPilot

| | WPilot | OCPilot |
|---|--------|---------|
| CMS | WordPress | OpenCart / ocStore |
| Класс | External CMS bridge | External ecommerce CMS bridge |
| Отношение | **Sibling** (один класс систем) | **Sibling** — не родитель и не потомок |

Общие паттерны доступа: [shared/external-access-patterns/](../../shared/external-access-patterns/README.md) — **не** WPilot-owned.

OCPilot может переиспользовать **идеи** из WPilot (read-only, dry-run, rollback, refusal-first), ORCA (battle pilot, freeze, lessons), mars-survivability (backup, risk classes, protected zones) и MARS Core (HITL, REPORT, SAFE UNKNOWN). Это не формула «WPilot + ORCA = OCPilot».

## Phase 0 + Run 1.5

Скелет репозитория, versioned baselines, расширенная структура `sites/`, shared access patterns. См. [phase-0-charter.md](phase-0-charter.md), [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md).

## Human-supervised execution

- Финальное решение — у оператора (HITL).
- Любой FTP/PMA/браузер/admin — только после подтверждения цели, бэкапа и scope; отчёт обязателен.
- Агент/Cursor **не** выполняет production-правки, destructive SQL, перезапись БД без явного charter.
- Паттерны доступа: [shared/external-access-patterns/](../../shared/external-access-patterns/README.md).

## Document map

| Doc | Purpose |
|-----|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Core Run rows, текущая фаза |
| [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md) | Family classification |
| [architecture.md](architecture.md) | Standalone bridge, паттерны vs siblings |
| [boundaries.md](boundaries.md) | Запреты и ownership |
| [access-and-safety.md](access-and-safety.md) | Доступ, FTP/PMA/браузер, секреты |
| [clean-opencart-baseline.md](clean-opencart-baseline.md) | Versioned clean baseline vs project custom |
| [project-sites-workflow.md](project-sites-workflow.md) | `sites/` layout + analysis zones |
| [battle-pilot-workflow.md](battle-pilot-workflow.md) | Первый battle pilot: read-only audit |
| [shared/external-access-patterns/](../../shared/external-access-patterns/README.md) | Shared CMS/ecommerce access patterns |

## SAFE UNKNOWN

- Конкретные OpenCart-версии, хостинг, модули и ocMod на целевых сайтах — до read-only инспекции.
- Наполнение versioned baseline folders — до Run 2 и upload оператором.

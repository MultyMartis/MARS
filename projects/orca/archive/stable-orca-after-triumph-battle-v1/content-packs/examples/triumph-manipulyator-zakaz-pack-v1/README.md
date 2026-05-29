# Triumph Manipulyator Zakaz Pack v1

**Первый полностью калиброванный ORCA semantic pack** для маршрута master hot «Аренда манипулятора в Краснодаре».

## Назначение

Этот pack — **не** лендинг и **не** HTML. Это канонический слой **semantic + visual implementation intelligence** между:

- ORCA research / PPC (`grp_fc12_zakaz`)
- калибровкой Triumph v5 (`workspaces/triumph-manipulator-landing-v5`)
- visual semantics (`projects/orca/visual-semantics/`)
- Website Factory (Lane A, MODE 1)

## Маршрут

| Поле | Значение |
|------|----------|
| Human name | Аренда манипулятора в Краснодаре |
| `pack_id` | `triumph-manipulyator-zakaz-pack-v1` |
| URL | `https://manipulator-triumph.ru/` |
| `data-page-type` | `ppc-zakaz-manip` |
| PPC group | `grp_fc12_zakaz` — «12 — Заказать манипулятор» |
| Blueprint | `projects/orca/ppc/triumph-manipulator/landing-pages/01-master-hot-general.md` |
| As-built workspace | `workspaces/triumph-manipulator-landing-v5/` |

## Структура pack

| Папка | Содержание |
|-------|------------|
| `content/` | Секционные контракты и copy locks по as-built v5 |
| `ppc/` | Continuity с `triumph-s-tier-draft-v1.json` |
| `visual-semantics/` | Калиброванные visual fields + зоны hero |
| `factory/` | Что Factory обязан сохранить / может эволюционировать |
| `calibration/` | Productive vs destructive drift, уроки ORCA |
| `exports/` | Готовность к DOCX (без реализации exporter) |

## Источники доказательств (repo)

- `projects/orca/calibration/triumph-manipulator/`
- `projects/orca/visual-semantics/examples/triumph-zakaz-hero-visual-semantics-v1.md`
- `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` → `grp_fc12_zakaz`
- `workspaces/triumph-manipulator-landing-v5/src/partials/sections/v5-ppc/zakaz/*`

## Статус

См. [PACK-STATUS.md](PACK-STATUS.md). Gates по умолчанию **false** до подписи оператора.

## Связанные артефакты

- Pattern donor (не SoT для zakaz): `examples/triumph-manipulyator-5-tonn-pack-v0.md`
- Visual semantics example: `visual-semantics/examples/triumph-zakaz-hero-visual-semantics-v1.md`

## Границы

- Не изменяет workspace, Factory runtime, exporter-cli, validation-cli
- Не утверждает live conversion, SLA «30 минут», device QA

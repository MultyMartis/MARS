# FP-0002 V9-06D.3 Legacy / Redirect / Rewrite Plan v1

**Phase:** V9-06D.3 — PLANNING ONLY

## Decisions (required)

| Item | Decision |
|---|---|
| `/specyalisty/` | Remains pre-existing legacy Page ID 10 for now |
| Canonical specialist route | `/uslugi/zavisimosti/specialistam/` (Service ID 76) |
| Redirect | Deferred to later explicit micro-gate |
| Rewrite flush | Deferred unless route HTTP checks prove needed |

## Deferred routes

| Route | Object | Plan |
|---|---|---|
| `/specyalisty/` | Page 10 | Keep; later 301 to `/uslugi/zavisimosti/specialistam/` |
| `/uslugi/genotipirovanie/` | Page 9 | Retire after migration; not in 31-route set |
| `/o-centre/intervyu-i-smi/` | Page 17 | Retire after migration |
| `/pravovaya-informaciya-pilzovatelyu/` | Page 21 | Retire after migration |
| `/privacy-policy-page/` | Page 25 | Review/retire; not canonical legal route |

## PAGE_TO_SERVICE_SOURCE pages

Pages 6/7/8 (`zavisimosti`, `psihicheskoe-zdorovie`, `rasstroystva-pischevogo-povedeniya`) remain as legacy sources after Service CPT creation. Retirement only after Service content validated and menus repointed (later gate).

## Service permalink HTTP readiness

D.2 recorded permalink readiness without rewrite flush. D.4 visual QA may detect 404s; only then authorize a dedicated rewrite-flush micro-gate.

## Immediate execution

- Redirects immediate: **NO**
- Rewrite flush immediate: **NO**

## Result

READY — deferred only.

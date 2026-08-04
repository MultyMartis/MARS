# REUSABLE DEPLOYMENT MODEL v1

## Current reality

Один production-клиент i-SEO, два активных workflow и один неактивный rollback workflow. Конфигурация и операционные данные относятся к этому контуру. Централизованной fleet-платформы нет.

## Target model

- canonical shared core;
- отдельные client configs, bots, secrets, sources, storage и staff registries;
- versioned templates и явно объявленная compatibility matrix;
- migration и rollback на каждое обновление;
- staged rollout и fleet visibility без раскрытия tenant secrets/PII.

## Not yet implemented

Нет автоматического tenant provisioning, registry federation, fleet dashboard, централизованного deploy controller, автоматических migrations или массового rollback. Документ не подтверждает существование этих компонентов.

## Isolation contract

Ни client secrets, ни bot credentials, ни staff identities не переносятся в shared core. Любая будущая автоматизация должна быть default-deny и раздельно подтверждать config, storage и recipient boundaries.
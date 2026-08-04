# VERSIONING AND ROLLOUT STRATEGY v1

## Версии

Версионировать независимо: shared workflow template, parser, message format, client profile/schema и migration. Совместимость фиксировать до rollout; breaking change требует migration и rollback package.

## Обязательный rollout

`development → harness → reference i-SEO → operator acceptance → selected pilots → wider rollout → health observation → stop/rollback`.

Переход к следующему этапу разрешён только после evidence receipt предыдущего. Ошибка compatibility, duplicate delivery, recipient leak, lifecycle regression или client auto-send — stop condition.

## Rollback

Сохранять предыдущую активную версию, sanitized manifest и private backup отдельно. Rollback не должен возвращать отозванные роли, старые secrets или устаревшие recipient lists. Массовый rollout без pilot cohort не допускается.
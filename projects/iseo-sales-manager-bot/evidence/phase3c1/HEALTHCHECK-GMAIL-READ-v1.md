# HEALTHCHECK GMAIL READ v1

## Production wording verified

```
Gmail: доступен, запрос выполнен
Найдено подходящих писем: 0
```

## Probe properties

- Node: `Gmail Health Probe` on Admin.dev
- Same incoming `labelIds` filter as Operational fetch
- Bounded limit 10; no label mutations; bodies not used in reply
- Does **not** claim `доступен` from credential reference alone

## Evidence execution

Admin temp-webhook health execution observed with nodes including `Gmail Health Probe` + `Health`.

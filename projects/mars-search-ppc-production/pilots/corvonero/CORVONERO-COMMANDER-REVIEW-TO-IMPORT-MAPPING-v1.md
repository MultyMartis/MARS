# CORVONERO Review → Import Mapping v1

**Compatibility:** PARTIAL

| Corvonero source field | Commander column | Compatibility | Transformation | Final value source |
|---|---|---|---|---|
| campaign_name | N/A — metadata block only | PARTIAL | Single Commander import = one Yandex campaign; 5 logical campaigns documented in SUPPORT | CAMPAIGN_SETTINGS support sheet |
| campaign_type | Тип кампании: | FULL | Metadata row — «Текстово-графическая кампания» | CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2.json |
| placement / search | Места показа-фразы на кампанию: | FULL | Metadata «search» literal | Operator: SEARCH ENABLED, networks DISABLED |
| daily_budget | N/A in template data table | NOT_IN_TEMPLATE | Post-import Commander UI — 5000 RUB × 5 campaigns | CAMPAIGN_SETTINGS support sheet |
| schedule | N/A | NOT_IN_TEMPLATE | Post-import — daily 06:00–21:00 Novosibirsk | CAMPAIGN_SETTINGS support sheet |
| region / geography | col 52 «Регион» | FULL | Новосибирск и Новосибирская область | Review COMMANDER_IMPORT col Регион |
| group_name | col 5 | FULL | Verbatim | Review ID группы / Название группы |
| keyword / phrase | col 8 | FULL | One row per keyword; ad fields blank on keyword rows | Review KEYWORD rows |
| keyword bid (manual search CPC) | col 54 «Ставка» | FULL | Numeric RUB integer; per-campaign: CA-01=500, others=400 | Operator approved initial manual bids |
| campaign_negatives | Минус-фразы на кампанию: (metadata) | PARTIAL | Single metadata cell — per-campaign variants in SUPPORT (CA-05 extra) | CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.json |
| group_negatives | col 68 | FULL | Cross-negatives NONE — column blank | Operator decision |
| headline_1 / headline_2 / ad text | cols 10-12 | FULL | AD rows only | Review AD rows |
| final URL | col 48 «Ссылка» | FULL | UTM appended; no utm_term | URL_UTM_MAP / review Ссылка |
| display_path | col 49 | FULL | Short path only | Review Отображаемая ссылка |
| callouts | col 67 «Уточнения» | FULL | Combined cell joined with '||'; AD rows only | CORVONERO-EXT-W1-CALLOUTS-v2.json |
| sitelinks | cols 58-60 | OMITTED | Empty — anchors PENDING; preserved in SITELINKS_PENDING | CORVONERO-EXT-W1-SITELINKS-v2.json (20 pending) |
| ad_status / phrase_status | cols 56, 57 | FULL | Empty = Commander default on import | Review workbook |
| yandex_metrica / conversion_goals | N/A | OMITTED_BY_OPERATOR | Blank / not populated | Production scope: OMITTED |
| network bid | N/A — networks DISABLED | N/A | Blank | Operator: advertising network DISABLED |
| auto-targeting | N/A | DISABLED | No autotarget rows exported | Operator: DISABLED |

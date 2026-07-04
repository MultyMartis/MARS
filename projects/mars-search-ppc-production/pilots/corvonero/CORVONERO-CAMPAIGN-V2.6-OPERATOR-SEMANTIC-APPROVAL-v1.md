# Corvonero Campaign V2.6 — Operator Semantic Approval Receipt v1

**Status:** `OPERATOR_SEMANTIC_APPROVED`  
**Project:** corvonero  
**Semantic authority:** V2.6  
**Deployable package:** V2.6.1  
**Approval scope:** semantic authority only  
**Operator identity:** operator  
**Approval timestamp:** 2026-06-30T20:45:00+07:00

## Operator statement

> Утверждаю семантическую authority Corvonero V2.6: 487 KEEP, 271 REJECT, 2 MOVE, 71 группа и 71 объявление. Разрешаю оформить OPERATOR_SEMANTIC_APPROVED и проверить пакет V2.6.1 через Campaign Release Gate. Импорт в Commander и запуск в Яндекс Директе пока не разрешаю.

## Approved totals

| Metric | Count |
|--------|------:|
| Unique source phrases | 760 |
| KEEP | 487 |
| REJECT | 271 |
| MOVE | 2 |
| HOLD (unresolved) | 0 |
| Final groups | 71 |
| Final ads | 71 |
| Phrase slots | 926 |
| Campaigns | 10 |

## Policies

- **GEO:** LOCAL = Новосибирск и НСО; REMOTE = Россия excluding Новосибирск and НСО after manual post-import exclusion
- **Negatives:** campaign negatives are separate TXT; embedded campaign negatives must be blank; cross-campaign negatives not applied
- **URLs:** clean URLs without UTM
- **Organization:** blank

## Known accepted operational requirements

- REMOTE NSO exclusion must be applied manually after import
- TXT negatives must be imported manually
- Post-import reconciliation required

## Explicitly not approved

- Commander import
- Yandex Direct launch
- Campaign launch
- Automatic cross-negatives
- Semantic changes
- New generation

## Authority artifacts

Machine-readable receipt: `CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json`

Authority paths and SHA-256 hashes are recorded in the JSON receipt.

## Deployable package under review

`X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30`

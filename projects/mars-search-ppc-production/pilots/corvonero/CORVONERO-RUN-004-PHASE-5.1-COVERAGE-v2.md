# CORVONERO RUN 004 — Phase 5.1 Coverage v2

**Run:** `corv-semantic-v2-20260626-004`  
**Partial dataset:** 1599 / 2368  
**Unprocessed:** 769 / 2368

## Verdict distribution

| Stage | ACCEPT | REJECT | ABSTAIN |
|-------|--------|--------|---------|
| Phase 4 | 529 | 762 | 308 |
| Phase 5 | 531 | 578 | 490 |
| Phase 5.1 | 926 | 358 | 315 |

## Review flag reconciliation

- Phase 5 OPERATOR_REVIEW_REQUIRED: **350**
- Phase 5.1 OPERATOR_REVIEW_REQUIRED: **47**
- Genuine operator packet: **47**

## Troubleshooting (1С не работает family)

{
  "total_assessed": 16,
  "accept": 1,
  "reject": 1,
  "abstain": 14,
  "zero_accept_phase5_validity": "Phase 5 zero ACCEPT was partially caused by taxonomy mapping — sync-error phrases classified as integration troubleshooting, not SF-TROUBLESHOOTING-NOT-WORKING; classic program-not-working phrases remain ambiguous DIY vs service"
}

## TS ПИОТ

{
  "total_assessed": 7,
  "accept": 1,
  "reject": 2,
  "abstain": 4,
  "accept_explanation": "Only explicit setup/service-demand phrases (e.g. настройка тс пиот) map to SF-TS-PIOT ACCEPT; combined marking+TS ПИОТ and DIY install queries remain ABSTAIN/REJECT",
  "records": [
    {
      "phrase_id": "CR2-PHR-01145",
      "phrase": "тс пиот честный знак 1с",
      "phase51_verdict": "ABSTAIN",
      "service_family": null
    },
    {
      "phrase_id": "CR2-PHR-01239",
      "phrase": "тс пиот честный знак 1с розница",
      "phase51_verdict": "ABSTAIN",
      "service_family": null
    },
    {
      "phrase_id": "CR2-PHR-02315",
      "phrase": "настройка тс пиот в 1с ут 11.5",
      "phase51_verdict": "ACCEPT",
      "service_family": "SF-TS-PIOT"
    },
    {
      "phrase_id": "CR2-PHR-02324",
      "phrase": "тс пиот как установить в 1с",
      "phase51_verdict": "REJECT",
      "service_family": null
    },
    {
      "phrase_id": "CR2-PHR-02331",
      "phrase": "1с тс пиот сертификация",
      "phase51_verdict": "REJECT",
      "service_family": null
    },
    {
      "phrase_id": "CR2-PHR-02338",
      "phrase": "1с встроенный тс пиот",
      "phase51_verdict": "ABSTAIN",
      "service_family": null
    },
    {
      "phrase_id": "CR2-PHR-02354",
      "phrase": "1с не видит тс пиот",
      "phase51_verdict": "ABSTAIN",
      "service_family": null
    }
  ]
}

## Geography

{
  "primary_novosibirsk_nso": 4,
  "expansion_krasnodar": 2,
  "expansion_ekaterinburg": 8,
  "expansion_krasnoyarsk": 5,
  "other_russian_cities": 57,
  "russia_wide_remote": 3,
  "irrelevant_or_unknown": 8,
  "expansion_other": 0
}

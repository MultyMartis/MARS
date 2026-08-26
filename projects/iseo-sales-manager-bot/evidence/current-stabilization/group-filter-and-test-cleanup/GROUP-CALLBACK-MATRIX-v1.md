# GROUP-CALLBACK-MATRIX-v1

Source: natural exec `40846` + operator click execs `40887`–`40928` (ADMIN_A).

## Main digest buttons → callbacks

| Label | Expected filter | Actual callback_data | Match |
|-------|-----------------|----------------------|-------|
| Аудит · 14 | Audit / category token | `sm:g:c:aa2771a403` | YES |
| SEO · 1 | SEO / category token | `sm:g:c:ade3cbdc59` | YES |
| Другое · 7 | Other / category token | `sm:g:c:e130bfb8c3` | YES |
| Старше суток · 18 | older24 | `sm:g:o24` | YES |
| Все · 22 | all | `sm:g:all` | YES |

## Operator clicks (selected)

| Exec | MSK (approx) | callback_data | Decoded | Observed lead count (pre-fix) |
|------|--------------|---------------|---------|--------------------------------:|
| 40887 / 40893 / 40894 | 11:14+ | `sm:g:c:ade3cbdc59` | SEO cat token | **27** (expected 1) |
| 40928 | 12:10 | `sm:g:c:aa2771a403` | Audit cat token | **47** (expected 14) |
| 40888 / 40890 | — | `sm:g:all` | all | **124** (expected 22) |
| 40889 | — | `sm:q:e64921b60ff5` | lead queue | verify error |

## Conclusion

Button labels and `callback_data` packing on the digest are correct. Divergence is **not** BUTTON_SLOT_MAPPING_DRIFT. Failure is downstream in `group_open` selector vs reminder authoritative selector.

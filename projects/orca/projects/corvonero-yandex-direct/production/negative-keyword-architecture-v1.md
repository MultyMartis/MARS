# Negative Keyword Architecture — Корво Неро v1

**Stage:** 2A — architecture for Stage 2B production  
**Scope:** All 8 campaigns · 48 ad groups

---

## Layer model

```text
L0 — Global (all campaigns)
L1 — Campaign-level negatives
L2 — Service-direction negatives
L3 — Group cross-negatives (conflict matrix)
L4 — Phrase-level negatives (inline in «Фраза (с минус-словами)»)
```

---

## L0 — Global negatives (all campaigns)

Apply to every campaign metadata block «Минус-фразы на кампанию»:

```text
вакансия, вакансии, работа, резюме, зарплата, стажер, стажировка,
обучение, курсы, курс, с нуля, бесплатно, скачать, торрент, кряк,
crack, torrent, форум, инструкция, документация, своими руками,
реферат, диплом, школа, студент, тест, сертификация, экзамен,
hh.ru, zarplata.ru, gorodrabot.ru, superjob
```

**Caution:** Do not minus «работа» globally on troubleshooting campaign without phrase-level review — use campaign-specific subset where conflict exists.

---

## L1 — Campaign-level negatives

### CORV-C01 (General 1C)
```text
маркировка, честный знак, битрикс, сайт интеграция, не работает,
ошибка, вакансия программист
```

### CORV-C02 (Modifications)
```text
маркировка, честный знак, вакансия, курсы, отчет печатная форма
```

### CORV-C03 (Reports/forms)
```text
маркировка, программист вакансия, битрикс, не работает
```

### CORV-C04 (Management)
```text
маркировка, вакансия, курсы, битрикс
```

### CORV-C05 (Integrations)
```text
маркировка, вакансия программист, доработка отчета, не работает
```

### CORV-C06 (Marking)
```text
программист вакансия, доработка 1с, сопровождение абонент,
битрикс, интеграция сайт
```

### CORV-C07 (Troubleshooting)
```text
вакансия, работа программист, курсы, маркировка, битрикс
```

### CORV-C08 (Specialist TS PIOT)
```text
вакансия, курсы, маркировка пива, маркировка воды
```

---

## L2 — Service-direction negatives

| Direction | Additional negatives |
|-----------|---------------------|
| general_1c | `-вакансия`, `-обучение`, `-резюме`, `-зарплата` |
| modifications | `-печатная форма`, `-отчет`, `-маркировка` |
| reports_forms | `-программист`, `-маркировка`, `-интеграция` |
| management | `-маркировка`, `-вакансия`, `-скачать` |
| integrations | `-маркировка`, `-вакансия`, `-доработка отчета` |
| marking | `-программист`, `-вакансия`, `-доработка`, `-битрикс` |
| troubleshooting | `-вакансия`, `-работа`, `-стажер`, `-курсы` |
| specialist | `-вакансия`, `-курсы`, `-скачать` |

---

## L3 — Group cross-negatives

Full matrix: [conflict-negative-matrix-v1.md](conflict-negative-matrix-v1.md)

**Pattern (Triumph-derived):** sibling groups within same campaign receive discriminators blocking bleed into adjacent intent families.

---

## L4 — Phrase-level negatives

Used when global/campaign minus would harm legitimate commercial phrases.

| Group | Example phrase-level pattern |
|-------|------------------------------|
| G01-01 | `услуги программиста 1с -вакансия -обучение -курсы` |
| G06-03 | `честный знак 1с -скачать -инструкция` |
| G07-01 | `1с не работает -вакансия -работа программист` |

Match encoding: per Commander template — phrase text with inline minus words (no dedicated match-type column in template v1).

---

## Wordstat evidence classes → negative action

| MIG noise class | Action |
|-----------------|--------|
| job-seeking | Global + phrase negative |
| training | Global negative |
| salary | Global negative |
| regulatory (non-commercial) | Phrase reject or Tier 4 only |
| informational | Group negative or reject |
| download | Global negative |
| remote-work (employment) | Phrase negative on geo groups |

---

## Production notes (Stage 2B)

1. Build cross-negative matrix before XLSX export (Triumph pattern).  
2. Validate no primary commercial phrase is negated by sibling rule.  
3. Campaign negatives in metadata block; group negatives in column «Минус-фразы на группу».  
4. Human hygiene audit before Commander import.

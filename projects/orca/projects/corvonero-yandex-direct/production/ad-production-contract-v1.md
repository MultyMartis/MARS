# Ad Production Contract — Корво Неро v1

**Stage:** 2A contract — creative production in Stage 2B  
**Requirement:** ≥1 text-and-image search ad per group (48 groups)  
**Optional:** 2nd ad variant where semantically useful — max 2 per group

---

## Per-ad fields (Commander «Тексты» sheet)

| Field | Commander column | Limit | Rule |
|-------|------------------|-------|------|
| headline_1 | Заголовок 1 | 56 chars | Primary benefit + service |
| headline_2 | Заголовок 2 | 30 chars | Geo or terms — optional |
| ad_text | Текст | 81 chars | CTA + fact |
| display_link | Отображаемая ссылка | path | `lk.corvonero.ru/{path}` |
| landing_url | Ссылка | full URL | Planned URL + UTM |
| ad_type | Тип объявления | — | «Текстово-графическое» |
| sitelinks | Заголовки/Описания/Адреса быстрых ссылок | combined | 2–4 sitelinks where supported |
| callouts | Уточнения | combined | 2–4: «Договор», «Безнал», «От 6000₽», «Удалённо» |
| ad_status | Статус объявления | — | draft at export |

---

## Confirmed facts (allowed)

Корво Неро · Новосибирск · удалённая работа · договор · безнал · 3 000 ₽/час · от 6 000 ₽ · 1С:УТ/УНФ/Розница/КА/БП · услуги по задаче

---

## Prohibited (unless verified later)

Partner 1C status · 24/7 · guaranteed deadlines · free · certifications · case metrics · team size · years experience · VAT claims

---

## Ad angle by campaign

| Campaign | Primary angle |
|----------|---------------|
| C01 | B2B outsource — programmer/support for business |
| C02 | Customization — task-based mod work |
| C03 | Deliverable — report/form/RMK done in 1C |
| C04 | Management feature setup |
| C05 | Integration — 1C ↔ site/Bitrix/cash/sync |
| C06 | Compliance marking — setup in 1C |
| C07 | Urgent fix — restore 1C operation |
| C08 | TS PIOT specialist setup |

---

## Price in ads

| Use price | Groups |
|-----------|--------|
| Yes (selective) | T1 commercial: G01-01, G02-01, G03-01, G06-03, G07-01 |
| Soft («оценка по задаче») | T2–T3 narrow groups |
| No specific price | T4 regulatory-adjacent |

---

## Sitelink pattern (per landing family)

| LP family | Sitelinks |
|-----------|-----------|
| General | Услуги · Сопровождение · Доработки · Контакты |
| Mod | Доработка · Обновление · Цена · Заявка |
| Marking | Честный знак · Настройка · Ошибки · Контакты |
| Troubleshooting | Не работает · Обмен · Восстановление · Заявка |

---

## Validation (Stage 2B)

- [ ] Character limits enforced before export  
- [ ] URL matches group landing map  
- [ ] No prohibited claims  
- [ ] Headline matches group keyword intent  
- [ ] legal_and_factual_validation: pass per ad record

---

## Output (Stage 2B)

`production/ad-copy-registry-v1.json` — all ads keyed by `group_id` + `ad_id`.

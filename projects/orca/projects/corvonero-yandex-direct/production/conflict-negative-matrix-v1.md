# Conflict-Negative Matrix — Корво Неро v1

**Stage:** 2A — mandatory pre-export artifact (Triumph pattern)  
**Groups:** 48 · **Campaigns:** 8

---

## Matrix rules

1. Cross-negatives are **discriminators** between sibling groups — not global junk.  
2. Applied at **group level** («Минус-фразы на группу») unless phrase-level precision required.  
3. Do not negate group's own primary seed phrases.  
4. Review before every XLSX export.

---

## Cross-campaign conflicts

| Source group family | Block tokens on siblings | Target campaigns |
|--------------------|--------------------------|------------------|
| General programmer (G01-01/02) | `маркировка`, `честный знак`, `битрикс`, `не работает` | C06, C05, C07 |
| Marking generic (G06-01/02) | `программист`, `доработка`, `сопровождение`, `битрикс` | C01, C02, C05 |
| Honest Sign (G06-03) | `доработка`, `программист`, `отчет` | C01–C03 |
| Website integration (G05-01) | `битрикс`, `маркировка`, `не работает` | C05-G05-02, C06, C07 |
| Bitrix (G05-02) | `сайт`, `маркировка`, `программист вакансия` | C05-G05-01, C06 |
| Troubleshooting (G07-*) | `маркировка`, `вакансия`, `курсы` | C06, C01 |
| Product marking (G06-05…) | other product tokens | sibling G06-05…G06-13 |

---

## Intra-campaign matrix (selected high-risk pairs)

### CORV-C01 — General

| Group | Cross-negative tokens |
|-------|----------------------|
| G01-01 Услуги программиста | `новосибирск` (owned by G01-02), `сопровождение`, `доработка`, `маркировка` |
| G01-02 Новосибирск | `удаленно` (unless ad claims remote), `маркировка`, `не работает` |
| G01-05 Сопровождение | `программист`, `доработка`, `маркировка`, `не работает` |
| G01-03 Настройка | `внедрение`, `маркировка`, `интеграция` |
| G01-04 Внедрение | `настройка`, `сопровождение`, `маркировка` |

### CORV-C05 — Integrations

| Group | Cross-negative tokens |
|-------|----------------------|
| G05-01 Сайт | `битрикс`, `касса`, `маркировка` |
| G05-02 Битрикс | `сайт`, `касса`, `маркировка` |
| G05-03 Касса | `сайт`, `битрикс` |
| G05-04 Синхронизация | `сайт`, `битрикс`, `перенос данных` |
| G05-06 Перенос данных | `синхронизация`, `обмен` |

### CORV-C06 — Marking (product categories)

| Group | Cross-negative tokens |
|-------|----------------------|
| G06-05 Напитки/алкоголь | `вода`, `лекарств`, `косметик`, `автозапчаст` |
| G06-06 Вода | `пив`, `алкогол`, `лекарств` |
| G06-08 Лекарства | `пив`, `вода`, `косметик` |
| G06-10 Автозапчасти | `лекарств`, `пив`, `вода` |
| G06-01 Generic marking | `честный знак` (owned by G06-03), product category names |

### CORV-C07 — Troubleshooting

| Group | Cross-negative tokens |
|-------|----------------------|
| G07-01 Не работает | `ошибка`, `обмен`, `синхронизация` (route to G07-02/03) |
| G07-02 Ошибка | `не работает`, `обмен` |
| G07-03 Обмен/синхронизация | `не работает`, `ошибка после обновления` |

---

## Machine-readable export hook

Stage 2C exporter should emit `group_negatives[]` per group from this matrix + [negative-keyword-architecture-v1.md](negative-keyword-architecture-v1.md).

---

## Validation checklist

- [ ] No primary seed phrase appears in own cross-negative list  
- [ ] Marking groups do not capture general 1C queries  
- [ ] Integration groups cross-block sibling integration intents  
- [ ] Troubleshooting groups block vacancy variants  
- [ ] Product marking groups block sibling product categories

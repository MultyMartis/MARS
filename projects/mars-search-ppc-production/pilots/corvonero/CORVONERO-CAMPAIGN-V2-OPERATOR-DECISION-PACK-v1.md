# CORVONERO CAMPAIGN V2 — OPERATOR DECISIONS

**Статус:** PROPOSED — NOT OPERATOR APPROVED  
**Checkpoint:** `ebff109061932faecdff63456a27aa7fe3823be7`  
**Сгенерировано:** 2026-06-30T11:13:36.000Z

## 1. What is already resolved

- Preflight: диск `X:` / метка `AI WS` / репозиторий `X:\AI MARS` — OK.
- Pass 1 архитектура: 10 кампаний (5 LOCAL + 5 REMOTE), 833 исходных фраз — принято.
- **833→828 reconciliation:** DEFERRED TO V2 COMMANDER POST-IMPORT EXPORT OR OBSERVATION — не блокирует Pass 2.
- Все 833 строки сохранены в proposed authority; 5 строк Commander не идентифицированы — не удалять.
- NEUTRAL (791), LOCAL_EXPLICIT (2), REMOTE_EXPLICIT (7): распределены детерминированно Pass 1.
- Из 33 спорных позиций **33 auto-resolved** с confidence HIGH без operator_decision_required.
- **41 из 42** объявлений: AUTO_APPROVE (не требуют строки в очереди оператора).
- Campaign negatives: **197** терминов auto-approved в proposed sets.

### Pass 2 phrase summary

| Метрика | Значение |
|---------|----------|
| Reviewed | 33 |
| High-confidence auto-resolved | 33 |
| Operator phrase decisions required | 0 |
| Recommended REJECT | 32 |
| Recommended LOCAL_ONLY | 0 |
| Recommended REMOTE_ONLY | 0 |
| Recommended INCLUDE_BOTH | 1 |

## 2. Decisions required from operator

*Нет обязательных phrase-решений — все 33 позиции auto-resolved.*
## 3. Ambiguous phrases

Все 33 позиции разрешены автоматически. Сводка auto-resolved:

- `CR2-PHR-00010` — программист 1с москва → **REJECT** (Запрос с чужим городом «москва» — вне зоны LOCAL и нецелевой для REMOTE)
- `CR2-PHR-00029` — программисты 1с спб → **REJECT** (Запрос с чужим городом «спб» — вне зоны LOCAL и нецелевой для REMOTE)
- `CR2-PHR-00059` — 1с программист красноярск → **REJECT** (Запрос с чужим городом «красноярск» — вне зоны LOCAL и нецелевой для REMOTE)
- `CR2-PHR-00061` — программисты 1с екатеринбург → **REJECT** (Запрос с чужим городом «екатеринбург» — вне зоны LOCAL и нецелевой для REMOTE)
- `CR2-PHR-00067` — программист 1с нижний → **REJECT** (Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания)
- `CR2-PHR-00072` — программист 1с нижний новгород → **REJECT** (Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания)
- `CR2-PHR-00086` — 1с программисты ростов → **REJECT** (Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания)
- `CR2-PHR-00099` — программист 1с санкт петербург → **REJECT** (Запрос с чужим городом «петербург» — вне зоны LOCAL и нецелевой для REMOTE)
- `CR2-PHR-00104` — программисты 1с самара → **REJECT** (Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания)
- `CR2-PHR-00105` — программисты 1с краснодар → **REJECT** (Сигнал other_ru_city — запрос привязан к чужому городу, вне зоны обслуживания)
- … и ещё 23 (см. `CORVONERO-CAMPAIGN-V2-PASS2-DECISIONS-v1.json`)

## 4. Ad rewrites requiring review

### A-01
**Campaign/group:** CA-01-REMOTE / ca-01-price-intent
**Current:** H1: Программист 1С — от 3 000 ₽ в час | H2: Удалённо по России | Text: Минимальный заказ — 2 часа. Работаем удалённо и.
**Problem:** Обрыв текста: незавершённое предложение «…и.»
**Recommended:** H1: Программист 1С — от 3 000 ₽ в час | H2: Удалённо по России | Text: Минимальный заказ — 2 часа. Работаем удалённо по России.
**Character counts:** H1=33, H2=18, Text=56
**Options:** APPROVE / EDIT

## 5. Campaign negatives requiring review

### N-01
**Campaign:** CA-01-LOCAL
**Negative:** удалённый
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «удалённый» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-02
**Campaign:** CA-01-LOCAL
**Negative:** удаленный
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «удаленный» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-03
**Campaign:** CA-01-LOCAL
**Negative:** онлайн
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «онлайн» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-04
**Campaign:** CA-01-REMOTE
**Negative:** нск
**Recommendation:** HOLD_OPERATOR
**Reason:** Есть конфликт с включёнными фразами
**Options:** APPROVE / REJECT / NARROW

### N-05
**Campaign:** CA-01-REMOTE
**Negative:** выезд
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «выезд» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-06
**Campaign:** CA-02-LOCAL
**Negative:** удалённый
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «удалённый» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-07
**Campaign:** CA-02-LOCAL
**Negative:** удаленный
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «удаленный» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-08
**Campaign:** CA-02-LOCAL
**Negative:** онлайн
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «онлайн» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-09
**Campaign:** CA-02-REMOTE
**Negative:** нск
**Recommendation:** HOLD_OPERATOR
**Reason:** Есть конфликт с включёнными фразами
**Options:** APPROVE / REJECT / NARROW

### N-10
**Campaign:** CA-02-REMOTE
**Negative:** выезд
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «выезд» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-11
**Campaign:** CA-03-LOCAL
**Negative:** удалённый
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «удалённый» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-12
**Campaign:** CA-03-LOCAL
**Negative:** удаленный
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «удаленный» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-13
**Campaign:** CA-03-LOCAL
**Negative:** онлайн
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «онлайн» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

### N-14
**Campaign:** CA-03-REMOTE
**Negative:** нск
**Recommendation:** HOLD_OPERATOR
**Reason:** Есть конфликт с включёнными фразами
**Options:** APPROVE / REJECT / NARROW

### N-15
**Campaign:** CA-03-REMOTE
**Negative:** выезд
**Recommendation:** HOLD_OPERATOR
**Reason:** Широкое слово «выезд» — возможны ложные срабатывания
**Options:** APPROVE / REJECT / NARROW

*… и ещё 10 позиций в JSON.*

## 6. Cross-campaign negatives requiring review

### X-01
**Source → protected:** CA-01 → CA-02
**Negative:** обслуживание
**Conflicts:** 2 included phrases
**Recommendation:** HOLD_OPERATOR
**Reason:** Умеренный конфликт (2) — оценить коммерческую ценность
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-02
**Source → protected:** CA-01 → CA-03
**Negative:** доработка
**Conflicts:** 43 included phrases
**Recommendation:** HOLD_OPERATOR
**Reason:** Высокий конфликт (43) — широкий минус «доработка» блокирует смежные запросы
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-03
**Source → protected:** CA-01 → CA-03
**Negative:** разработка
**Conflicts:** 4 included phrases
**Recommendation:** NARROW
**Reason:** Конфликт 4 — рекомендуется узкий минус вместо «разработка»
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-04
**Source → protected:** CA-01 → CA-04
**Negative:** интеграция
**Conflicts:** 30 included phrases
**Recommendation:** HOLD_OPERATOR
**Reason:** Высокий конфликт (30) — широкий минус «интеграция» блокирует смежные запросы
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-05
**Source → protected:** CA-02 → CA-03
**Negative:** доработка
**Conflicts:** 43 included phrases
**Recommendation:** HOLD_OPERATOR
**Reason:** Высокий конфликт (43) — широкий минус «доработка» блокирует смежные запросы
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-06
**Source → protected:** CA-02 → CA-03
**Negative:** разработка
**Conflicts:** 4 included phrases
**Recommendation:** NARROW
**Reason:** Конфликт 4 — рекомендуется узкий минус вместо «разработка»
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-07
**Source → protected:** CA-02 → CA-04
**Negative:** интеграция
**Conflicts:** 30 included phrases
**Recommendation:** HOLD_OPERATOR
**Reason:** Высокий конфликт (30) — широкий минус «интеграция» блокирует смежные запросы
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-08
**Source → protected:** CA-03 → CA-02
**Negative:** обслуживание
**Conflicts:** 2 included phrases
**Recommendation:** HOLD_OPERATOR
**Reason:** Умеренный конфликт (2) — оценить коммерческую ценность
**Options:** APPROVE / REJECT / NARROW / HOLD

### X-09
**Source → protected:** CA-03 → CA-04
**Negative:** интеграция
**Conflicts:** 30 included phrases
**Recommendation:** HOLD_OPERATOR
**Reason:** Высокий конфликт (30) — широкий минус «интеграция» блокирует смежные запросы
**Options:** APPROVE / REJECT / NARROW / HOLD


## 7. Recommended final totals

| campaign_id | groups | phrases | ads | neutral | geo-explicit | review-pending |
|-------------|--------|---------|-----|---------|--------------|----------------|
| CA-01-LOCAL | 7 | 311 | 7 | 308 | 1 | 0 |
| CA-01-REMOTE | 7 | 316 | 7 | 309 | 6 | 0 |
| CA-02-LOCAL | 4 | 143 | 4 | 142 | 1 | 0 |
| CA-02-REMOTE | 4 | 143 | 4 | 142 | 1 | 0 |
| CA-03-LOCAL | 3 | 76 | 3 | 76 | 0 | 0 |
| CA-03-REMOTE | 3 | 76 | 3 | 76 | 0 | 0 |
| CA-04-LOCAL | 1 | 48 | 1 | 48 | 0 | 0 |
| CA-04-REMOTE | 1 | 48 | 1 | 48 | 0 | 0 |
| CA-05-LOCAL | 6 | 216 | 6 | 216 | 0 | 0 |
| CA-05-REMOTE | 6 | 216 | 6 | 216 | 0 | 0 |

**Aggregate phrase slots (LOCAL+REMOTE):** 1593
**Recommended total (after auto-resolved rejects):** 1593
**Minimum / Maximum (if pending BOTH approved):** 1593 / 1593

### Verification

- ✓ No phrase disappeared without reason
- ✓ No LOCAL-explicit phrase enters REMOTE-only incorrectly
- ✓ No REMOTE-explicit phrase enters LOCAL
- ✓ No group exceeds 200 phrases
- ✓ No empty groups

## 8. Approval form

```text
OPERATOR: ______________________  DATE: __________

[ ] Phrase decisions D-01… acknowledged
[ ] Ad rewrites A-01… approved or edited
[ ] Campaign negatives N-01… resolved
[ ] Cross-campaign X-01… resolved (separate Direct layer)
[ ] Proposed final authority ready for Pass 3 / XLSX
```

---

**PROPOSED — NOT OPERATOR APPROVED**
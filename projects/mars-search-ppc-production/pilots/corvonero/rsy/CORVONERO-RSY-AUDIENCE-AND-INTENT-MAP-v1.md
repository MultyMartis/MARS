# CORVONERO — РСЯ audience and intent map v1

**Status:** PLANNING / NOT_A_METRICA_AUDIENCE_EXPORT  
**Created:** 2026-08-18  
**Project:** CorvoNero / Корво Неро  

Metrica goal names, ready-made retargeting lists, and Networks audience IDs are **SAFE UNKNOWN / TO_CONFIRM**. This file is thematic planning, not a Direct audience upload.

---

## 1. Shared B2B audience (all directions)

Primary:

- владельцы бизнеса / ИП
- директора
- главные бухгалтеры и бухгалтеры, работающие в 1С
- руководители операций / производства / розницы
- IT-ответственные лица внутри компании
- пользователи 1С внутри компании (не соискатели)

Exclude from message targeting (planning):

- соискатели / вакансии / резюме
- обучающий how-to трафик без коммерческого запроса услуги
- чужая вендорская техподдержка
- покупатели лицензий 1С как продукта

Device mix from Search detailed report (not РСЯ proof): smartphones 4 conversions / 18 900 ₽ vs desktops 2 conversions / 8 200 ₽. Useful later for РСЯ device assumptions only.

---

## 2. Intent themes (shared)

| Theme code | Intent | Typical need |
|------------|--------|--------------|
| URGENT_PROBLEM | Срочная проблема | Ошибка 1С, база не открывается, маркировка не проходит |
| REGULAR_SUPPORT | Регулярная поддержка | Абонентское сопровождение, консультации, обновления |
| CONFIG_IMPROVEMENT | Улучшение конфигурации | Доработка типовой, расширение функционала |
| INTEGRATION_NEED | Потребность в интеграции | Сайт, Битрикс, Битрикс24, API, обмен |
| MARKING_COMPLIANCE | Маркировка / ошибки ЧЗ | Настройка, обмен, локальный модуль, остатки |
| LOCAL_SPECIALIST | Нужен местный специалист | Новосибирск, возможный выезд |
| REMOTE_SPECIALIST | Нужен удалённый специалист | Россия, без выезда |

---

## 3. By direction

### Программист 1С

| Item | Content |
|------|---------|
| B2B audience | Владелец, директор, IT-ответственный; реже бухгалтер, если ищет «человека на задачу». |
| Intent themes | LOCAL_SPECIALIST; REMOTE_SPECIALIST; URGENT_PROBLEM (разово); CONFIG_IMPROVEMENT (частично пересекается с доработкой — keep landing LP-01). |
| Search seed | «программист 1с новосибирск» (converting, LOCAL). |
| Warm notes | Посетители LP-01; клики по объявлениям программиста. Metrica segments: TO_CONFIRM. |

### Сопровождение 1С / техподдержка / ошибки 1С

| Item | Content |
|------|---------|
| B2B audience | Бухгалтер, владелец, операции, IT; пользователь, у которого «1С упала». |
| Intent themes | URGENT_PROBLEM; REGULAR_SUPPORT; LOCAL_SPECIALIST; REMOTE_SPECIALIST. |
| Search seeds | Восстановление базы; УНФ Фреш; непредвиденная ошибка; информационно-консультационное обслуживание. |
| Caution | ITS / «итс 1с» — большой показ, почти без конверсий; не строить холодный РСЯ только вокруг ИТС-любопытств. |
| Warm notes | Посетители LP-02; самые сильные Search working signals. |

### Доработка / разработка 1С

| Item | Content |
|------|---------|
| B2B audience | Владелец, IT-ответственный, руководитель учёта, которому не хватает типового функционала. |
| Intent themes | CONFIG_IMPROVEMENT; LOCAL_SPECIALIST; REMOTE_SPECIALIST. |
| Search status | Weak / not confirmed. Still include. |
| Warm notes | Посетители LP-03; мало Search-доказательств коммерческого intent. |

### Интеграции 1С

| Item | Content |
|------|---------|
| B2B audience | IT-ответственный, владелец интернет-магазина / компании с сайтом, операции. |
| Intent themes | INTEGRATION_NEED; CONFIG_IMPROVEMENT (secondary). |
| Search status | Clicks on REMOTE, zero on LOCAL. How-to leakage caution. |
| Warm notes | Посетители LP-04. |

### Маркировка / Честный знак

| Item | Content |
|------|---------|
| B2B audience | Розница, учёт, владелец, бухгалтер, операции; IT при внедрении ЧЗ в 1С. |
| Intent themes | MARKING_COMPLIANCE; URGENT_PROBLEM (ошибки обмена/сканера); LOCAL_SPECIALIST; REMOTE_SPECIALIST. |
| Search seed | Настройка 1С для работы с маркировкой (LOCAL converting). |
| Caution | DIY «как настроить честный знак» — не основной холодный угол. |
| Warm notes | Посетители LP-05. |

---

## 4. Retargeting / warm audience notes

| Audience idea | Status | Notes |
|---------------|--------|-------|
| Site visitors (lk.corvonero.ru) | TO_CONFIRM | Need Metrica / Direct audience availability. |
| Landing visitors by service (LP-01…LP-05) | TO_CONFIRM | Thematically useful; IDs not proven. |
| Form visitors without submission | TO_CONFIRM / SAFE UNKNOWN | Goal names unknown. |
| Messenger clickers if tracked | TO_CONFIRM / SAFE UNKNOWN | Tracking not proven in this task. |
| Metrica goal audience | SAFE UNKNOWN | Exact goal names not in Search exports. |
| Search clickers / campaign converters | TO_CONFIRM | Could be a warm layer later; not built here. |

Whether to separate remarketing from cold РСЯ is an **open confirmation**. Architecture default suggestion (not approved): keep cold РСЯ groups as described; add remarketing as a later separate campaign or set of groups if audiences exist.

Do not invent audience IDs. Do not claim retargeting is ready.

---

**Storage package:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-PACK-2026-08-18\`  
XLSX workbooks live in Storage only (not in Git).

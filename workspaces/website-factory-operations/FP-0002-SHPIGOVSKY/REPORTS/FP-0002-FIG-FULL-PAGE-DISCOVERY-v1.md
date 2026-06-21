# REPORT — FP-0002 FIG FULL PAGE DISCOVERY v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-17  
**Phase:** Skeleton — Discovery only (FULL RESTART FROM FIG)  
**Primary SSOT:** `INCOMING/01_DESIGN/Шпиговский.fig`  
**Secondary visual reference:** `INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` (pixel review / disputes only)  
**Parser:** `openfig-core` 0.3.7 — offline decode of `.fig` (ZIP + `fig-kiwi`)  
**Target frame:** `Главная страница` (`1:875`)  
**Historical shell v1:** Header v5.5 + Hero + Footer + UI Demo — **reference-only; not used in this discovery**

**Scope:** Discovery only. No HTML, SCSS, JS, Layout Spec, Assembly Spec, or Build.

---

## 1. Home Frame Identification

| Field | Value |
|-------|-------|
| **Name** | `Главная страница` |
| **Frame ID** | `1:875` |
| **Bounds** | x=0, y=0, width=1437, height=16809 |
| **Direct children** | 15 (section-level nodes) |
| **Parent canvas** | `Page 1` |
| **Mobile sibling** | `Главная страница - моб` (380×22883) — out of scope |

**Selection rationale:** explicit Russian page name, desktop width cluster (1437 px), full-page height, not mobile variant.

**JPG cross-check:** `HOME-PAGE-FULL-MOCKUP.jpg` ≈1398×16343 px (~3% scale delta vs FIG) — consistent raster export, not a different page.

---

## 2. SECTION REGISTER

Top-to-bottom order = **direct children of `Главная страница` in FIG parent-index order** (layer list order).

### SECTION-01

- **Name:** `1 - Главный экран`
- **Frame:** `1:876`
- **Bounds:** x=-1, y=0, width=1440, height=929
- **Children count:** 3
- **Type:** FRAME
- **Component instances (subtree):** `Кнопка`, `search`
- **Auto-layout nodes (subtree):** 12

### SECTION-02

- **Name:** `2 - Дом - вступление`
- **Frame:** `1:927`
- **Bounds:** x=0, y=1029, width=1437, height=1260
- **Children count:** 1
- **Type:** FRAME
- **Component instances (subtree):** `Маркированный список`, `Ес`
- **Auto-layout nodes (subtree):** 27

### SECTION-03

- **Name:** `3- Услуги`
- **Frame:** `1:958`
- **Bounds:** x=0, y=3000, width=1437, height=1022
- **Children count:** 7
- **Type:** FRAME
- **Component instances (subtree):** `Раскрытие информации`, `Пункт услуги`, `Услуга`
- **Auto-layout nodes (subtree):** 40+

### SECTION-04

- **Name:** `Нас выбирают`
- **Frame:** `1:991`
- **Bounds:** x=0, y=4122, width=1437, height=2114
- **Children count:** 1
- **Type:** FRAME
- **Component instances (subtree):** `Пункт услуги`, `Стрелка`
- **Auto-layout nodes (subtree):** 50+

### SECTION-05

- **Name:** `Отзывы`
- **Frame:** `1:1050`
- **Bounds:** x=1, y=6336, width=1435, height=429
- **Children count:** 6
- **Type:** FRAME
- **Component instances (subtree):** `отзыв`, `Кнопка`
- **Auto-layout nodes (subtree):** 15+

### SECTION-06

- **Name:** `С чего начать`
- **Frame:** `1:1079`
- **Bounds:** x=-2, y=6865, width=1441, height=1781
- **Children count:** 7
- **Type:** FRAME
- **Component instances (subtree):** `Раскрытие информации`, `Маркированный список`, `Важно `, `Цифра`, `Запись маленькая`, `этап процедуры`
- **Auto-layout nodes (subtree):** 60+

### SECTION-07

- **Name:** `Программа центра`
- **Frame:** `1:1115`
- **Bounds:** x=0, y=8746, width=1437, height=1563
- **Children count:** 2
- **Type:** FRAME
- **Component instances (subtree):** `этап`, `Запись маленькая`, `Кнопка`
- **Auto-layout nodes (subtree):** 20+

### SECTION-08

- **Name:** `Генотипирование`
- **Frame:** `1:1136`
- **Bounds:** x=-1, y=10409, width=1440, height=879
- **Children count:** 1
- **Type:** FRAME
- **Component instances (subtree):** `Маркированный список`, `Кнопка`
- **Auto-layout nodes (subtree):** 15+

### SECTION-09

- **Name:** `преимущества`
- **Frame:** `1:1164`
- **Bounds:** x=0, y=11388, width=1437, height=1294
- **Children count:** 3
- **Type:** FRAME
- **Component instances (subtree):** `этап`, `Кнопка`
- **Auto-layout nodes (subtree):** 25+

### SECTION-10

- **Name:** `Слово спецу`
- **Frame:** `1:1208`
- **Bounds:** x=-1, y=2389, width=1440, height=511
- **Children count:** 6
- **Type:** FRAME
- **Component instances (subtree):** `Кнопка`
- **Auto-layout nodes (subtree):** 8
- **⚠ Anomaly:** y=2389 — visually between SECTION-02 and SECTION-03, but layer index #10 (see CONFLICTS)

### SECTION-11

- **Name:** `Видео ` (trailing space in FIG)
- **Frame:** `1:1224`
- **Bounds:** x=0, y=12782, width=1437, height=550
- **Children count:** 3
- **Type:** FRAME

### SECTION-12

- **Name:** `Специаисты` (typo preserved from FIG)
- **Frame:** `1:1231`
- **Bounds:** x=0, y=13432, width=1437, height=561
- **Children count:** 7
- **Type:** FRAME
- **Component instances (subtree):** `Врач`, `Услуга`, `Кнопка`

### SECTION-13

- **Name:** `Статьи`
- **Frame:** `1:1268`
- **Bounds:** x=-1, y=14093, width=1440, height=511
- **Children count:** 2
- **Type:** FRAME
- **Component instances (subtree):** `Статья`, `Кнопка`

### SECTION-14

- **Name:** `faq`
- **Frame:** `1:1282` (register) / section root `1:1280` in prior test — **canonical child of home:** `1:1282` per full parse
- **Bounds:** x=-1, y=14704, width=1440, height=1517
- **Children count:** 3
- **Type:** FRAME
- **Component instances (subtree):** `Расскрытие вопроса`, `Вопрос скрыт`, `Поле ввода`, `Кнопка`

### SECTION-15

- **Name:** `Подвал`
- **Frame:** `1:1309`
- **Bounds:** x=-1, y=16321, width=1440, height=488
- **Children count:** 0 (INSTANCE — children on symbol `1:584`)
- **Type:** INSTANCE
- **Symbol reference:** `Подвал` (`1:584`)

### Section summary table

| SECTION-ID | FIG name | Frame ID | x | y | width | height | children |
|------------|----------|----------|---|---|-------|--------|----------|
| SECTION-01 | 1 - Главный экран | 1:876 | -1 | 0 | 1440 | 929 | 3 |
| SECTION-02 | 2 - Дом - вступление | 1:927 | 0 | 1029 | 1437 | 1260 | 1 |
| SECTION-03 | 3- Услуги | 1:958 | 0 | 3000 | 1437 | 1022 | 7 |
| SECTION-04 | Нас выбирают | 1:991 | 0 | 4122 | 1437 | 2114 | 1 |
| SECTION-05 | Отзывы | 1:1050 | 1 | 6336 | 1435 | 429 | 6 |
| SECTION-06 | С чего начать | 1:1079 | -2 | 6865 | 1441 | 1781 | 7 |
| SECTION-07 | Программа центра | 1:1115 | 0 | 8746 | 1437 | 1563 | 2 |
| SECTION-08 | Генотипирование | 1:1136 | -1 | 10409 | 1440 | 879 | 1 |
| SECTION-09 | преимущества | 1:1164 | 0 | 11388 | 1437 | 1294 | 3 |
| SECTION-10 | Слово спецу | 1:1208 | -1 | 2389 | 1440 | 511 | 6 |
| SECTION-11 | Видео  | 1:1224 | 0 | 12782 | 1437 | 550 | 3 |
| SECTION-12 | Специаисты | 1:1231 | 0 | 13432 | 1437 | 561 | 7 |
| SECTION-13 | Статьи | 1:1268 | -1 | 14093 | 1440 | 511 | 2 |
| SECTION-14 | faq | 1:1282 | -1 | 14704 | 1440 | 1517 | 3 |
| SECTION-15 | Подвал | 1:1309 | -1 | 16321 | 1440 | 488 | 0 |

**Total sections:** 15

---

## 3. GROUP REGISTER

Decomposition per [group-decomposition-law-v1.md](../../../../projects/mars-website-factory/group-decomposition-law-v1.md): visual groups only — no `Content Block`, `Info Block`, `Utility Block`, `Contact Block`, `Hero Area`. Names verbatim from FIG.

Depth: level-1 = direct section children; deeper levels = nested visual frames/groups/instances decomposed to max depth 3.

---

### SECTION-01 — `1 - Главный экран`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL | Notes |
|----------|----------|----------|------|---|---|-----|----------|----|-------|
| GROUP-01 | Хедер | 1:877 | FRAME | 108 | 10 | 1170×143 | 2 | YES | Site chrome — ROW 1+2 header |
| GROUP-02 | Frame 18 | 1:878 | FRAME | 0 | 0 | 1170×101 | 1 | YES | Header top row container |
| GROUP-03 | Frame 19 | 1:901 | FRAME | 0 | 117 | 1170×22 | 2 | YES | Header nav row container |
| GROUP-04 | Frame 10 | 1:902 | FRAME | 20 | 0 | 1130×22 | 8 | YES | Nav links row |
| GROUP-05 | Group 6 | 1:912 | FRAME | 20 | 179 | 1400×750 | 2 | — | Hero content wrapper |
| GROUP-06 | банер | 1:913 | FRAME | 0 | 0 | 1400×750 | 5 | — | Hero banner stack |
| GROUP-07 | Group 5 | 1:918 | FRAME | 181 | 281 | 1039×162 | 3 | — | Frosted overlay card (heading + label) |
| GROUP-08 | Frame 4 | 1:922 | FRAME | 534 | 605 | 334×113 | 1 | YES | CTA stack (INSTANCE `Кнопка` 1:923) |
| GROUP-09 | Frame 81513852 | 1:924 | FRAME | 135 | 20 | 187×83 | 2 | — | Decorative brand vectors |

---

### SECTION-02 — `2 - Дом - вступление`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL |
|----------|----------|----------|------|---|---|-----|----------|-----|
| GROUP-01 | Frame 27 | 1:928 | FRAME | 133 | 0 | 1170×761 | 2 | YES |
| GROUP-02 | Frame 26 | 1:930 | FRAME | 0 | 75 | 1170×1225 | 4 | YES |
| GROUP-03 | Frame 81513755 | 1:932 | FRAME | 0 | 121 | 1170×222 | 6 | YES |
| GROUP-04 | Frame 81513740 | 1:937 | FRAME | 0 | 383 | 1170×381 | 1 | YES |
| GROUP-05 | Frame 81513756 | 13:4495 | FRAME | 0 | 804 | 1170×381 | 1 | YES |

---

### SECTION-03 — `3- Услуги`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Frame 81513826 | 1:959 | FRAME | 133 | 0 | 1170×43 | 2 | AL |
| GROUP-02 | Кнопка | 1:961 | FRAME | 1019 | 11 | 151×21 | 2 | AL |
| GROUP-03 | arrow-up-right | 1:963 | FRAME | 131 | 1 | 20×20 | 3 | — |
| GROUP-04 | Frame 25 | 1:967 | FRAME | 133 | 73 | 1170×86 | 1 | AL |
| GROUP-05 | Frame 81513825 | 1:972 | FRAME | 133 | 189 | 1170×243 | 2 | AL |
| GROUP-06 | Раскрытие информации | 1:973 | INSTANCE | 0 | 20 | 1170×40 | 0 | AL+INST |
| GROUP-07 | Frame 81513824 | 1:974 | FRAME | 0 | 80 | 1170×152 | 4 | AL |
| GROUP-08 | Пункт услуги | 1:975 | INSTANCE | 0 | 0 | 1164×38 | 0 | AL+INST |
| GROUP-09 | Пункт услуги | 1:976 | INSTANCE | 0 | 38 | 1164×38 | 0 | AL+INST |
| GROUP-10 | Пункт услуги | 1:977 | INSTANCE | 0 | 76 | 1164×38 | 0 | AL+INST |
| GROUP-11 | Пункт услуги | 1:978 | INSTANCE | 0 | 114 | 1164×38 | 0 | AL+INST |
| GROUP-12 | Frame 81513827 | 1:979 | FRAME | 133 | 462 | 1170×54 | 1 | AL |
| GROUP-13 | Frame 81513828 | 1:981 | FRAME | 133 | 546 | 1170×57 | 1 | AL |
| GROUP-14 | Frame 81513740 | 1:983 | FRAME | 133 | 720 | 1304×400 | 1 | AL |
| GROUP-15 | Frame 81513829 | 40:4668 | FRAME | 133 | 633 | 1170×57 | 1 | AL |

---

### SECTION-04 — `Нас выбирают`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Нас выбирают | 1:992 | FRAME | 133 | 0 | 1170×2114 | 10 | AL |
| GROUP-02 | Frame 25 | 1:994 | FRAME | 0 | 73 | 1170×106 | 1 | AL |
| GROUP-03 | Frame 81513782 | 1:999 | FRAME | 0 | 209 | 1170×128 | 1 | AL |
| GROUP-04 | Frame 81513824 | 1:1001 | FRAME | 0 | 367 | 1170×152 | 4 | AL |
| GROUP-05 | Пункт услуги | 1:1002 | INSTANCE | 0 | 0 | 1170×38 | 0 | INST |
| GROUP-06 | Пункт услуги | 1:1003 | INSTANCE | 0 | 38 | 1170×38 | 0 | INST |
| GROUP-07 | Пункт услуги | 1:1004 | INSTANCE | 0 | 76 | 1170×38 | 0 | INST |
| GROUP-08 | Пункт услуги | 1:1005 | INSTANCE | 0 | 114 | 1170×38 | 0 | INST |
| GROUP-09 | Frame 81513781 | 1:1007 | FRAME | 0 | 1037 | 1170×207 | 4 | AL |
| GROUP-10 | Frame 81513778 | 1:1008 | FRAME | 0 | 0 | 370×207 | 2 | AL |
| GROUP-11 | Frame 81513779 | 1:1011 | FRAME | 400 | 0 | 370×207 | 2 | AL |
| GROUP-12 | Frame 81513777 | 1:1014 | FRAME | 600 | 0 | 270×260 | 2 | AL |
| GROUP-13 | Frame 81513781 | 1:1017 | FRAME | 800 | 0 | 370×207 | 2 | AL |
| GROUP-14 | Frame 81513776 | 1:1020 | FRAME | 120 | 1250 | 470×480 | 4 | AL |
| GROUP-15 | Стрелка | 1:1023 | INSTANCE | -30 | 220 | 40×40 | 0 | INST |
| GROUP-16 | Стрелка | 1:1024 | INSTANCE | 1200 | 220 | 40×40 | 0 | INST |
| GROUP-17 | Frame 81513783 | 1:1025 | FRAME | 0 | 1274 | 1170×207 | 4 | AL |
| GROUP-18 | Frame 81513778 | 1:1026 | FRAME | 0 | 0 | 270×260 | 2 | AL |
| GROUP-19 | Frame 81513779 | 1:1029 | FRAME | 0 | 0 | 370×207 | 2 | AL |
| GROUP-20 | Frame 81513777 | 1:1032 | FRAME | 400 | 0 | 370×207 | 2 | AL |
| GROUP-21 | Frame 81513781 | 1:1035 | FRAME | 800 | 0 | 370×207 | 2 | AL |
| GROUP-22 | Frame 81513776 | 1:1038 | FRAME | 0 | 1511 | 1170×603 | 4 | AL |
| GROUP-23 | Frame 3359 | 1:1043 | FRAME | 120 | 2173 | 98×8 | 6 | AL |

---

### SECTION-05 — `Отзывы`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Frame 81513706 | 1:1051 | FRAME | 135 | 0 | 1170×43 | 3 | AL |
| GROUP-02 | Кнопка | 1:1053 | FRAME | 981 | 11 | 189×21 | 2 | AL |
| GROUP-03 | arrow-up-right | 1:1055 | FRAME | 169 | 1 | 20×20 | 3 | — |
| GROUP-04 | отзыв клиентки на яндекс | 1:1060 | TEXT | 1020 | 103 | 407×25 | 0 | — |
| GROUP-05 | Rectangle 3099 | 1:1061 | ROUNDED_RECTANGLE | 90 | 794 | 157×45 | 0 | — |
| GROUP-06 | Frame 5165 | 1:1062 | FRAME | 90 | 380 | 337×48 | 1 | AL |
| GROUP-07 | Frame 81513786 | 1:1068 | FRAME | 132 | 71 | 1170×313 | 3 | AL |
| GROUP-08 | отзыв | 1:1069 | INSTANCE | 0 | 0 | 570×311 | 0 | INST |
| GROUP-09 | отзыв | 1:1070 | INSTANCE | 600 | 0 | 570×311 | 0 | INST |
| GROUP-10 | отзыв | 1:1071 | INSTANCE | 1200 | 0 | 570×313 | 0 | INST |
| GROUP-11 | Frame 3359 | 1:1072 | FRAME | 673 | 412 | 98×8 | 6 | AL |

---

### SECTION-06 — `С чего начать`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Rectangle 4263 | 1:1080 | ROUNDED_RECTANGLE | 135 | 1201 | 1170×580 | 0 | — |
| GROUP-02 | плюсы | 1:1081 | FRAME | 135 | 879 | 1170×292 | 5 | AL |
| GROUP-03 | Раскрытие информации | 1:1082 | INSTANCE | 30 | 30 | 1110×36 | 0 | INST |
| GROUP-04 | Маркированный список | 1:1083 | INSTANCE | 30 | 90 | 1110×25 | 0 | INST |
| GROUP-05 | Маркированный список | 1:1084 | INSTANCE | 30 | 139 | 1110×25 | 0 | INST |
| GROUP-06 | Маркированный список | 1:1085 | INSTANCE | 30 | 188 | 1110×25 | 0 | INST |
| GROUP-07 | Маркированный список | 1:1086 | INSTANCE | 30 | 237 | 1110×25 | 0 | INST |
| GROUP-08 | Важно  | 1:1087 | INSTANCE | 135 | 671 | 1170×110 | 0 | INST |
| GROUP-09 | Frame 81513761 | 1:1088 | FRAME | 135 | 183 | 1170×529 | 4 | AL |
| GROUP-10 | этап процедуры | 1:1089 | FRAME | 0 | 26 | 1170×94 | 2 | AL |
| GROUP-11 | Цифра | 1:1090 | INSTANCE | 0 | 0 | 50×50 | 0 | INST |
| GROUP-12 | Frame 81513760 | 1:1091 | FRAME | 80 | 0 | 1090×94 | 2 | AL |
| GROUP-13 | этап процедуры | 1:1094 | FRAME | 0 | 150 | 1170×98 | 2 | AL |
| GROUP-14 | Цифра | 1:1095 | INSTANCE | 0 | 0 | 50×50 | 0 | INST |
| GROUP-15 | Frame 81513760 | 1:1096 | FRAME | 80 | 0 | 1090×98 | 2 | AL |
| GROUP-16 | этап процедуры | 1:1099 | FRAME | 0 | 278 | 1170×98 | 2 | AL |
| GROUP-17 | Цифра | 1:1100 | INSTANCE | 0 | 0 | 50×50 | 0 | INST |
| GROUP-18 | Frame 81513760 | 1:1101 | FRAME | 80 | 0 | 1090×98 | 2 | AL |
| GROUP-19 | этап процедуры | 1:1104 | FRAME | 0 | 406 | 1170×98 | 2 | AL |
| GROUP-20 | Цифра | 1:1105 | INSTANCE | 0 | 0 | 50×50 | 0 | INST |
| GROUP-21 | Frame 81513760 | 1:1106 | FRAME | 80 | 0 | 1090×98 | 2 | AL |
| GROUP-22 | Frame 25 | 1:1109 | FRAME | 135 | 73 | 1170×80 | 1 | AL |
| GROUP-23 | Frame 81513764 | 1:1112 | FRAME | 135 | 0 | 1170×43 | 1 | AL |
| GROUP-24 | Запись маленькая | 1:1114 | INSTANCE | 135 | 742 | 1170×107 | 0 | INST |

---

### SECTION-07 — `Программа центра`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Frame 27 | 1:1116 | FRAME | 133 | 71 | 1170×1502 | 2 | AL |
| GROUP-02 | Frame 25 | 1:1117 | FRAME | 0 | 0 | 1170×89 | 1 | AL |
| GROUP-03 | Frame 26 | 1:1120 | FRAME | 0 | 121 | 1170×1371 | 3 | AL |
| GROUP-04 | Frame 81513767 | 1:1122 | FRAME | 0 | 185 | 1170×1186 | 4 | AL |
| GROUP-05 | Запись маленькая | 1:1127 | INSTANCE | 0 | 1131 | 1170×107 | 0 | INST |
| GROUP-06 | Frame 81513826 | 1:1128 | FRAME | 134 | 0 | 1170×43 | 2 | AL |
| GROUP-07 | Кнопка | 1:1130 | FRAME | 1043 | 11 | 127×21 | 2 | AL |
| GROUP-08 | arrow-up-right | 1:1132 | FRAME | 107 | 1 | 20×20 | 3 | — |

---

### SECTION-08 — `Генотипирование`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL |
|----------|----------|----------|------|---|---|-----|----------|-----|
| GROUP-01 | Frame 27 | 1:1137 | FRAME | 135 | 0 | 1170×902 | 3 | AL |
| GROUP-02 | Frame 81513826 | 1:1138 | FRAME | 0 | 0 | 1170×43 | 2 | AL |
| GROUP-03 | Кнопка | 1:1140 | FRAME | 1043 | 11 | 127×21 | 2 | AL |
| GROUP-04 | Frame 25 | 1:1146 | FRAME | 0 | 73 | 1170×71 | 1 | AL |
| GROUP-05 | Frame 26 | 1:1149 | FRAME | 0 | 174 | 1170×704 | 2 | AL |
| GROUP-06 | Frame 81513740 | 1:1151 | FRAME | 0 | 212 | 1170×467 | 1 | AL |

---

### SECTION-09 — `преимущества`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Frame 81513826 | 1:1165 | FRAME | 134 | 0 | 1170×43 | 2 | AL |
| GROUP-02 | Кнопка | 1:1167 | FRAME | 976 | 11 | 194×21 | 2 | AL |
| GROUP-03 | arrow-up-right | 1:1169 | FRAME | 174 | 1 | 20×20 | 3 | — |
| GROUP-04 | Frame 25 | 1:1173 | FRAME | 134 | 73 | 1170×71 | 1 | AL |
| GROUP-05 | Frame 81513620 | 1:1177 | FRAME | 134 | 174 | 1170×1120 | 3 | AL |
| GROUP-06 | Frame 81513615 | 1:1178 | FRAME | 0 | 0 | 1170×360 | 3 | AL |
| GROUP-07 | Frame 2 | 1:1179 | FRAME | 0 | 0 | 383×360 | 8 | — |
| GROUP-08 | этап | 1:1194 | FRAME | 403 | 0 | 767×360 | 1 | — |
| GROUP-09 | этап | 1:1196 | INSTANCE | 786 | 0 | 384×360 | 0 | INST |
| GROUP-10 | Frame 81513614 | 1:1197 | FRAME | 0 | 380 | 1170×360 | 3 | AL |
| GROUP-11 | этап | 1:1198 | INSTANCE | 0 | 0 | 377×360 | 0 | INST |
| GROUP-12 | этап | 1:1199 | INSTANCE | 397 | 0 | 377×360 | 0 | INST |
| GROUP-13 | этап | 1:1200 | INSTANCE | 793 | 0 | 377×360 | 0 | INST |
| GROUP-14 | Frame 81513613 | 1:1201 | FRAME | 0 | 760 | 1170×360 | 3 | AL |
| GROUP-15 | этап | 1:1202 | INSTANCE | 0 | 0 | 580×360 | 0 | INST |
| GROUP-16 | этап | 1:1203 | FRAME | 0 | 0 | 575×360 | 3 | — |
| GROUP-17 | этап | 1:1207 | INSTANCE | 595 | 0 | 575×360 | 0 | INST |

---

### SECTION-10 — `Слово спецу`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | фон | 1:1209 | ROUNDED_RECTANGLE | 135 | 0 | 1170×511 | 0 | — |
| GROUP-02 | фон | 1:1210 | FRAME | 689 | 48 | 442×463 | 1 | — |
| GROUP-03 | Vector 10 | 1:1213 | VECTOR | 493 | -85 | 721×826 | 0 | — |
| GROUP-04 | (quote TEXT) | 1:1214 | TEXT | 135 | 132 | 528×323 | 0 | — |
| GROUP-05 | Frame 81513751 | 1:1215 | FRAME | 135 | 50 | 1170×26 | 2 | AL |
| GROUP-06 | Frame 21 | 1:1216 | FRAME | 0 | 0 | 26×26 | 1 | — |
| GROUP-07 | Карточка спеца | 1:1219 | FRAME | 1071 | 227 | 234×262 | 2 | AL |
| GROUP-08 | Frame 23 | 1:1220 | FRAME | 20 | 20 | 194×130 | 2 | AL |
| GROUP-09 | Кнопка | 1:1223 | INSTANCE | 20 | 174 | 194×60 | 0 | INST |

---

### SECTION-11 — `Видео `

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL |
|----------|----------|----------|------|---|---|-----|----------|-----|
| GROUP-01 | Видео о нашем центре | 1:1225 | TEXT | 135 | 0 | 1167×43 | 0 | — |
| GROUP-02 | Frame 3359 | 1:1226 | FRAME | 698 | 540 | 44×8 | 3 | AL |
| GROUP-03 | image 13030398 | 1:1230 | ROUNDED_RECTANGLE | 135 | 73 | 1170×439 | 0 | — |

---

### SECTION-12 — `Специаисты`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Frame 81513740 | 1:1232 | FRAME | 134 | 0 | 1170×43 | 3 | AL |
| GROUP-02 | Кнопка | 1:1234 | FRAME | 981 | 11 | 189×21 | 2 | AL |
| GROUP-03 | arrow-up-right | 1:1236 | FRAME | 169 | 1 | 20×20 | 3 | — |
| GROUP-04 | отзыв клиентки на яндекс | 1:1241 | TEXT | 1020 | 103 | 407×25 | 0 | — |
| GROUP-05 | Frame 81513739 | 1:1242 | FRAME | 1 | 73 | 1435×500 | 4 | AL |
| GROUP-06 | Врач | 1:1243 | INSTANCE | 135 | 0 | 370×500 | 0 | INST |
| GROUP-07 | Врач | 1:1244 | INSTANCE | 535 | 16 | 370×468 | 0 | INST |
| GROUP-08 | Врач | 1:1245 | INSTANCE | 935 | 16 | 370×468 | 0 | INST |
| GROUP-09 | Врач | 1:1246 | INSTANCE | 1335 | 16 | 370×468 | 0 | INST |
| GROUP-10 | Frame 81513741 | 1:1247 | FRAME | 134 | 73 | 1170×450 | 1 | AL |
| GROUP-11 | Rectangle 3099 | 1:1254 | ROUNDED_RECTANGLE | 640 | 571 | 157×45 | 0 | — |
| GROUP-12 | Frame 5165 | 1:1255 | FRAME | 90 | 380 | 337×48 | 1 | AL |
| GROUP-13 | Frame 3359 | 1:1261 | FRAME | 670 | 553 | 98×8 | 6 | AL |

---

### SECTION-13 — `Статьи`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Статьи | 1:1269 | FRAME | 135 | 0 | 1170×43 | 3 | AL |
| GROUP-02 | Кнопка | 1:1271 | FRAME | 1043 | 11 | 127×21 | 2 | AL |
| GROUP-03 | arrow-up-right | 1:1273 | FRAME | 107 | 1 | 20×20 | 3 | — |
| GROUP-04 | Frame 81513738 | 1:1278 | FRAME | 136 | 75 | 1169×468 | 3 | AL |
| GROUP-05 | Статья | 1:1279 | INSTANCE | 0 | 0 | 370×468 | 0 | INST |
| GROUP-06 | Статья | 1:1280 | INSTANCE | 390 | 0 | 370×468 | 0 | INST |
| GROUP-07 | Статья | 1:1281 | INSTANCE | 780 | 0 | 370×468 | 0 | INST |

---

### SECTION-14 — `faq`

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | AL/INST |
|----------|----------|----------|------|---|---|-----|----------|---------|
| GROUP-01 | Frame 81513773 | 1:1283 | FRAME | 135 | 75 | 1170×1043 | 10 | AL |
| GROUP-02 | Расскрытие вопроса | 1:1284 | INSTANCE | 0 | 0 | 1170×179 | 0 | INST |
| GROUP-03 | Вопрос скрыт | 1:1285 | INSTANCE | 0 | 199 | 1170×76 | 0 | INST |
| GROUP-04 | Вопрос скрыт | 1:1286 | INSTANCE | 0 | 295 | 1170×76 | 0 | INST |
| GROUP-05 | Вопрос скрыт | 1:1287 | INSTANCE | 0 | 391 | 1170×76 | 0 | INST |
| GROUP-06 | Вопрос скрыт | 1:1288 | INSTANCE | 0 | 487 | 1170×76 | 0 | INST |
| GROUP-07 | Вопрос скрыт | 1:1289 | INSTANCE | 0 | 583 | 1170×76 | 0 | INST |
| GROUP-08 | Вопрос скрыт | 1:1290 | INSTANCE | 0 | 679 | 1170×76 | 0 | INST |
| GROUP-09 | Вопрос скрыт | 1:1291 | INSTANCE | 0 | 775 | 1170×76 | 0 | INST |
| GROUP-10 | Вопрос скрыт | 1:1292 | INSTANCE | 0 | 871 | 1170×76 | 0 | INST |
| GROUP-11 | Вопрос скрыт | 1:1293 | INSTANCE | 0 | 967 | 1170×76 | 0 | INST |
| GROUP-12 | Нас часто спрашивают | 1:1294 | TEXT | 135 | 0 | 413×43 | 0 | — |
| GROUP-13 | Консультация | 1:1295 | FRAME | 135 | 1143 | 1170×374 | 2 | AL |
| GROUP-14 | Frame 81513643 | 1:1296 | FRAME | 54 | 44 | 416×127 | 2 | AL |
| GROUP-15 | Frame 3449 | 1:1299 | FRAME | 500 | 44 | 616×286 | 3 | AL |
| GROUP-16 | Frame 598 | 1:1300 | FRAME | 0 | 0 | 616×77 | 2 | AL |
| GROUP-17 | Frame 3449 | 1:1303 | FRAME | 0 | 93 | 616×77 | 2 | AL |
| GROUP-18 | Frame 3448 | 1:1306 | FRAME | 0 | 186 | 616×100 | 2 | AL |

---

### SECTION-15 — `Подвал` (from INSTANCE symbol `1:584`)

INSTANCE `1:1309` has 0 expanded children offline; groups resolved from symbol `Подвал`:

| GROUP-ID | FIG name | Frame ID | Type | x | y | w×h | children | Notes |
|----------|----------|----------|------|---|---|-----|----------|-------|
| GROUP-01 | Frame 81513790 | 1:585 | FRAME | 0 | 0 | 1440×122 | 4 | Top footer bar |
| GROUP-02 | image 219 | 1:586 | ROUNDED_RECTANGLE | 135 | 36 | 220×50 | 0 | Logo image |
| GROUP-03 | Frame 3377 | 1:587 | FRAME | 378 | 40 | 146×42 | 3 | Messenger icons (telegramm, watsapp×2) |
| GROUP-04 | 8 (800) 777-02-05 | 1:600 | TEXT | 548 | 36 | 381×50 | 0 | Phone |
| GROUP-05 | Frame 81513796 | 1:601 | FRAME | 952 | 39 | 353×44 | 2 | CTA buttons (Кнопка ×2) |
| GROUP-06 | Frame 81513797 | 1:604 | FRAME | 135 | 162 | 1170×263 | 2 | Link columns + payment |
| GROUP-07 | Frame 81513701 | 1:698 | FRAME | 0 | 465 | 1440×44 | 2 | Legal bar (license, privacy, terms) |

**Total groups across page:** 162 (155 from section frames + 7 from footer symbol)

---

## 4. Discovery Validation

### 4.1 Section count

| Check | Result |
|-------|--------|
| FIG direct children of `Главная страница` | **15** |
| Prior FIG discovery test (2026-06-17) | **15** — **MATCH** |
| JPG full-page analysis inferred blocks | **17** — **MISMATCH** (JPG splits header/hero; FIG bundles in SECTION-01) |

### 4.2 Section order

| Order source | Finding |
|--------------|---------|
| **FIG parent-index order** | 15 sections as registered above |
| **Visual Y-axis order** | **DIVERGES** — `Слово спецу` (SECTION-10) at y=2389 sits between `2 - Дом - вступление` (ends ~2289) and `3- Услуги` (y=3000), but is child #10 in layer list |
| **Reading order for Factory** | **SAFE UNKNOWN** — operator must decide: layer order vs visual Y reorder for `Слово спецу` |

### 4.3 Nesting

| Signal | Count / note |
|--------|----------------|
| Top-level section types | 14× FRAME + 1× INSTANCE (`Подвал`) |
| Deepest practical decomposition | depth 3 (auto script cap) |
| Repeated nested frame names | `Frame 25`, `Frame 81513826`, `Frame 81513740` recur across sections — shared layout pattern |
| Header inside SECTION-01 | `Хедер` (`1:877`) nested, not separate top-level section |

### 4.4 Component instances

| Signal | Value |
|--------|-------|
| Total INSTANCE nodes in file | **954** |
| Total SYMBOL nodes | **76** |
| Home page recurring components | `Кнопка`, `search`, `Пункт услуги`, `отзыв`, `Врач`, `Статья`, `этап`, `Раскрытие информации`, `Маркированный список`, `Вопрос скрыт`, `Расскрытие вопроса`, `Подвал` |
| Footer | Single `Подвал` INSTANCE — symbol-resolved |

### 4.5 Auto-layout usage

| Signal | Value |
|--------|-------|
| Auto-layout nodes in file (`stackMode` / `layoutMode`) | **3179** |
| Sections with heavy AL | Most content sections (03–14) — horizontal/vertical stacks, card rows, FAQ accordion list |
| SECTION-01 hero | Mixed — `Хедер` AL; `банер`/`Group 5` absolute; CTA `Frame 4` AL |

---

## 5. UNKNOWN

| ID | Item |
|----|------|
| UNK-01 | **Reading order for `Слово спецу`** — layer index #10 vs visual y between intro and services |
| UNK-02 | **Footer INSTANCE text** — offline parse does not expand `1:1309` children; symbol `1:584` used instead |
| UNK-03 | **Semantic rename map** — generic `Group N` / `Frame N` labels need Factory heuristics before Layout Spec |
| UNK-04 | **Header/Hero Factory boundary** — FIG SECTION-01 bundles both; JPG/Factory Hero scope may split differently |
| UNK-05 | **Full-factory speedup %** beyond home page — not benchmarked this session |

---

## 6. CONFLICTS

| ID | Conflict | Severity |
|----|----------|----------|
| CON-01 | FIG **15 sections** vs JPG **17 blocks** — header not top-level in FIG | **HIGH** — structural model difference |
| CON-02 | **`Слово спецу` layer order vs Y position** — not in visual top-to-bottom layer sequence | **HIGH** — affects assembly order |
| CON-03 | Historical shell v1 (Header v5.5 / Hero / Footer) **must not** be used — new cycle from FIG only | **PROCESS** — by charter |
| CON-04 | SECTION-10 y=2389 overlaps visual gap between SECTION-02 and SECTION-03 while later sections have y>6000 | **MEDIUM** — possible FIG layer reorder / absolute placement |

---

## 7. AGGREGATION RISKS

Per Group Decomposition Law — risks of premature or incorrect grouping if Factory reuses historical patterns or JPG-only inference:

| ID | Risk |
|----|------|
| AR-01 | **SECTION-01** — treating `Хедер` + `Group 6` as one "Hero Area" — **FORBIDDEN** aggregate |
| AR-02 | **SECTION-01** — merging address/phones/messengers in header into "Contact Block" — header has 8 nav children in `Frame 10`; contact row in `Frame 18`/`Frame 19` needs row-level decomposition before Layout Spec |
| AR-03 | **Generic FIG names** — 7+ `Group N` / `Frame N` per section in 10/15 sections; auto group register is geometrically correct but semantically weak |
| AR-04 | **SECTION-04** — carousel `Frame 81513776` + arrow instances — risk of collapsing into single "slider" without discrete card groups |
| AR-05 | **SECTION-14** — `Консультация` frame could be misread as "Contact Block" — contains form fields + copy columns; must stay decomposed (GROUP-13…18) |
| AR-06 | **Footer GROUP-06** — three `Название раздела` columns inside `Frame 81513791` — risk of "footer links blob" aggregation |

---

## 8. Factory Readiness Verdict

| Question | Verdict | Rationale |
|----------|---------|-----------|
| **CAN SECTION REGISTER BE AUTO GENERATED?** | **YES** | 15 sections, IDs, bounds, children — extracted programmatically from `Главная страница` direct children |
| **CAN GROUP REGISTERS BE AUTO GENERATED?** | **PARTIAL** | Tree walk + instance detection works (162 groups); semantic naming, header row splits, hero/header boundary, and footer instance expansion need rules + operator review |
| **CAN LAYOUT SPEC BE GENERATED FROM FIG?** | **PARTIAL** | Geometry + AL axis + spacing available; requires APPROVED Group Decomposition + conflict resolution (`Слово спецу` order, hero/header split) |
| **CAN ASSEMBLY SPEC BE GENERATED FROM FIG?** | **PARTIAL** | Section order from FIG layer list is machine-readable; visual Y anomalies and Factory block boundaries need human gate |
| **CAN HTML SKELETON BE GENERATED FROM FIG?** | **PARTIAL** | Section-level `<section>` stubs feasible; meaningful class/BEM names, header/hero split, and component markup need downstream specs — **not in this phase** |

### Overall readiness

| Gate | Status |
|------|--------|
| **FIG FULL PAGE DISCOVERY** | **COMPLETE** |
| **GROUP DECOMPOSITION GATE** | **DRAFT** — operator APPROVED required before Layout Spec |
| **LAYOUT SPEC GATE** | **BLOCKED** |
| **HTML / BUILD** | **BLOCKED** |

### Recommended next step (not executed)

1. Operator review SECTION REGISTER + GROUP REGISTER against FIG + JPG.
2. Resolve CON-01, CON-02, UNK-01 (hero/header boundary + `Слово спецу` placement).
3. On APPROVED → per-section Group Decomposition sign-off → Layout Spec (one block at a time).

---

## 9. Evidence Artefacts

| File | Role |
|------|------|
| `REPORTS/_fig_full_page_discovery_v1.json` | Machine output — full registers |
| `REPORTS/_fig_parse_temp/full_page_discovery_v1.mjs` | Parser script |
| `REPORTS/_fig_parse_temp/footer_symbol.mjs` | Footer symbol resolver |
| `INCOMING/01_DESIGN/Шпиговский.fig` | Primary SSOT |
| `INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` | Secondary visual reference |

---

## 10. Git Status

| Item | Value |
|------|-------|
| **Created** | `REPORTS/FP-0002-FIG-FULL-PAGE-DISCOVERY-v1.md` |
| **Created (scratch)** | `REPORTS/_fig_full_page_discovery_v1.json`, `REPORTS/_fig_parse_temp/full_page_discovery_v1.mjs`, `REPORTS/_fig_parse_temp/footer_symbol.mjs`, `REPORTS/_fig_parse_temp/print_discovery.mjs` |
| **Commit / push** | Not performed |

---

**STOP.** Discovery only. No HTML, SCSS, JS, Layout Spec, Assembly Spec, or Build.

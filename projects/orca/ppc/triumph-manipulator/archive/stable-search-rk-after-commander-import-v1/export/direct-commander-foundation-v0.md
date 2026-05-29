## ORCA PPC EXPORT SYSTEM FOUNDATION

---

# DOCUMENT PURPOSE

Этот документ фиксирует:

# production contract

между:

- ORCA
- internal PPC model
- validation layer
- Direct Commander export

---

# IMPORTANT

Excel:  
НЕ является source-of-truth.

Excel =

# transport/export format.

---

# SOURCE OF TRUTH

Source-of-truth =

# ORCA PPC KNOWLEDGE + INTERNAL MODEL.

---

# CORE PRINCIPLE

ORCA:  
НЕ:

> “генерирует объявления в Excel”

ORCA:

# строит structured PPC architecture.

---

# PRODUCTION PIPELINE

## STEP 1

Search intent analysis

---

## STEP 2

Intent segmentation

---

## STEP 3

Campaign structure generation

---

## STEP 4

Group generation

---

## STEP 5

Keyword clustering

---

## STEP 6

Ad generation

---

## STEP 7

Validation layer

---

## STEP 8

Export layer

→ Direct Commander Excel

---

# VERY IMPORTANT

Validation:  
идёт:

# ДО Excel export.

НЕ после.

---

# EXCEL TEMPLATE ROLE

Excel template:  
используется:

- как Direct Commander transport schema
- как import format
- как field contract
- как limit contract

---

# TEMPLATE STATUS

Текущий шаблон:

- production-proven
- based on live campaign export
- includes real Commander structure
- includes draft examples
- includes field limitation notes

---

# SEARCH-ONLY STATUS

Текущая версия ORCA:

# SEARCH ONLY.

---

# IMPORTANT

Пока:  
НЕ:

- РСЯ
- мастер кампаний
- ретаргет
- автотаргетинг architecture
- performance campaigns

---

# Потому что

Search:

- deterministic
- intent-clean
- easier to validate
- easier to train ORCA on

---

# ORCA PPC ENTITY MODEL

---

# ENTITY 1 — CAMPAIGN

## Campaign contains

- campaign_name
- geo
- strategy
- negatives
- schedule
- bid_model
- device adjustments
- extensions
- tracking settings

---

# IMPORTANT

Campaign =

# semantic container.

НЕ giant keyword dump.

---

# CAMPAIGN SPLIT RULE

Если:  
интенты:

- сильно различаются
- требуют different semantics
- different landing logic
- different psychology

То:

# split into separate campaigns.

---

# OTHERWISE

Intent separation:  
идёт:

# на уровне групп.

---

# ENTITY 2 — GROUP

## Group contains

- group_name
- intent
- keyword cluster
- negatives
- landing URL
- ads

---

# MOST IMPORTANT RULE

Group =

# one semantic intent.

---

# FORBIDDEN

НЕ:

- mixed intent groups
- giant unrelated keyword sets
- broad chaos grouping

---

# GOOD EXAMPLES

- 01 — Заказать манипулятор
- 02 — Вызвать манипулятор
- 03 — Манипулятор 5 тонн
- 04 — Перевозка бытовки

---

# GROUP NAMING DOCTRINE

Naming:

- human-readable
- Russian language
- operationally understandable
- sequential numbering

---

# WHY IMPORTANT

Campaigns later:

- debugged
- optimized
- expanded
- cleaned manually

Human readability =

# survivability.

---

# ENTITY 3 — KEYWORDS

## Keyword rules

Keywords inside group:  
must belong:

# to same semantic intent.

---

# EXAMPLES

GOOD:

- заказать манипулятор
- вызвать манипулятор

---

# BAD:

- заказать манипулятор
- работа манипулятор
- эвакуатор
- купить манипулятор

---

# ENTITY 4 — ADS

Each group:  
contains:

- one or more ads

---

# IMPORTANT RULE

Ad:  
must:

# continue exact search intent.

---

# KEYWORD → HEADLINE ALIGNMENT

CRITICAL ORCA RULE.

---

# PRIMARY RULE

Keyword phrase:  
should appear:

- in headline
- in description
- optionally in fast links

---

# WHY IMPORTANT

This improves:

- Yandex bold highlighting
- relevance
- CTR
- continuation
- intent match

---

# EXAMPLE

## Keyword

заказать манипулятор

---

## Headline

Заказать манипулятор  
в Краснодаре

---

## Description

Заказать манипулятор  
для стройматериалов, бытовок и оборудования.

---

# THIS IS:

# core Yandex search doctrine.

---

# AD STRUCTURE

## Ad contains

- headline_1
- headline_2
- description
- display_url
- fastlinks
- callouts
- landing_url

---

# SYMBOL LIMITS

IMPORTANT:  
All generation:  
must obey:

# Direct field limits.

---

# VALIDATION REQUIRED

Before export:  
ORCA must validate:

- symbol counts
- spaces included
- field overflow
- truncation risks

---

# IMPORTANT

Template annotations:  
with symbol limits:  
become:

# validation contract.

---

# FAST LINKS

Fast links:  
НЕ:

- decorative.

Fast links:  
must:

- continue intent
- increase relevance
- strengthen qualification

---

# GOOD FAST LINKS

- Перевозка бытовок
- Манипулятор 5 т
- Работа по краю
- Безналичный расчёт

---

# BAD FAST LINKS

- О компании
- Наши услуги
- Главная

---

# CALLOUTS

Callouts:  
must:

- reinforce capability
- reinforce trust
- reinforce qualification

---

# GOOD EXAMPLES

- Борт 5 т
- Стрела 14 м
- Без посредников
- Работа по краю
- Безналичный расчёт

---

# LANDING ROUTING RULE

Each group:  
must map:

# to best-fit landing.

---

# IMPORTANT

НЕ:  
one landing for everything forever.

---

# Routing examples

## Group

Перевозка бытовки

→ бытовка landing

---

## Group

Манипулятор 5 тонн

→ capability landing

---

## Group

Манипулятор для юрлиц

→ B2B landing

---

# NEGATIVE LOGIC

ORCA:  
must support:

- campaign negatives
- group negatives
- conditional negatives

---

# GLOBAL NEGATIVES

Examples:

- вакансии
- работа
- купить
- ремонт
- эвакуатор

---

# CONDITIONAL NEGATIVES

Handled carefully:

- дешево
- бесплатно
- фото

---

# IMPORTANT

Negatives:  
must:

# protect semantic purity.

---

# DRAFT SUPPORT

IMPORTANT:  
Template:  
supports:

# draft ads.

---

# WHY IMPORTANT

Production workflow:  
often includes:

- testing
- drafts
- staging before publish

---

# Therefore

ORCA export:  
must support:

- active ads
- draft ads

---

# INTERNAL ORCA MODEL

IMPORTANT:  
ORCA internal representation:  
should be:

# structured data model.

NOT Excel-native.

---

# CORRECT ARCHITECTURE

## ORCA CORE

Generates:

- campaigns
- groups
- ads
- routing
- negatives
- extensions

---

## VALIDATION LAYER

Checks:

- limits
- relevance
- duplicates
- intent purity
- broadness risks
- keyword alignment

---

## EXPORT LAYER

Converts:  
→ Direct Commander Excel

---

# WHY THIS ARCHITECTURE IS CORRECT

Because:  
Excel:

- fragile
- transport-specific
- hard to validate
- hard to scale

Structured PPC model:

- scalable
- testable
- reusable
- exportable to multiple systems

---

# HUMAN SUPERVISION RULE

ORCA =

# PPC copilot.

NOT:

- autonomous advertiser
- autonomous launcher
- autonomous optimizer

---

# FINAL HUMAN ROLE

Human:

- reviews
- edits
- validates
- imports
- launches campaigns

---

# ORCA ROLE

ORCA:

- structures
- assists
- validates
- prepares
- reduces chaos
- accelerates PPC production

---

# FUTURE ORCA PPC KNOWLEDGE MODULES

Future modules should include:

- Yandex search doctrine
- intent isolation doctrine
- keyword/ad alignment doctrine
- anti-garbage generation
- commercial semantics
- mobile-first search behavior
- Direct moderation survivability
- landing/ad continuation
- PPC qualification logic
- Direct Commander operational workflow

---

# FINAL STRATEGIC SUMMARY

ORCA PPC System:  
должна стать:

# AI-assisted PPC production methodology

А НЕ:

> “генератором объявлений”.
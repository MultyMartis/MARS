#!/usr/bin/env python3
"""
CORVONERO Campaign V2.5 — operator-curated commercial core and final pre-generation authority.
Loads V2.4 authority CSVs; curates KEEP/MOVE rows; rebuilds groups, ads and negatives.
No XLSX. No git commit. Does not modify V2–V2.4 packages.

C2b source persistence only. This file is not authorized for execution without explicit operator approval. Commit/persistence does not authorize Storage export generation, repo artifact generation, Commander import, Direct launch, account mutation, advertising start, Localhost mutation, Storage mutation, or Yandex/API access.
"""
from __future__ import annotations

import csv
import json
import os
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(r"X:\AI MARS")
PILOT = REPO / "projects" / "mars-search-ppc-production" / "pilots" / "corvonero"
REPORTS = REPO / "projects" / "mars-search-ppc-production" / "reports"
V24_REVIEW = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.4-FINAL-AUTHORITY-REVIEW-2026-06-30"
)
V25_REVIEW = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.5-CURATED-CORE-REVIEW-2026-06-30"
)
GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

# ── binding sets ─────────────────────────────────────────────────────────────
BINDING_KEEP_TO_REJECT = {
    "программист 1с опыт работы": "career intent",
    "техническое задание на доработку 1с пример": "document/example intent",
    "услуги сопровождение 1с систем купить": "malformed query",
    "программист 1с дмитрий": "named person / company / random entity intent",
    "программист 1с лидер фарм": "named person / company / random entity intent",
    "программист 1с элита м": "named person / company / random entity intent",
    "программист 1с яндекс": "named person / company / random entity intent",
}

BINDING_REJECT_TO_KEEP = {
    "где найти программиста 1с",
    "ищу 1с программиста для разовой задачи",
    "ищу программист 1с",
    "найти программиста 1с",
    "найти программиста 1с на аутсорсинг",
}

BINDING_HONEST_SIGN_REJECT = {
    "интеграция 1с с честным знаком как сделать": "informational how-to wording without a clear paid-service signal",
}

CA04_MARKING_MOVE = {
    "настройка интеграции с честным знаком 1с бухгалтерия",
    "синхронизация 1с с честным знаком",
}

# ── V2.5 binding curation sets ───────────────────────────────────────────────
CA01_BINDING_REJECT = {
    "программист 1с описание": "Profession description — not service buyer intent",
    "программист 1с основы": "Education/basics research — not service buyer intent",
    "программист 1с перспективы": "Career prospects research — not service buyer intent",
    "программист 1с требования": "Job/profession requirements — not service buyer intent",
    "программист 1с язык": "Profession terminology — not service buyer intent",
    "программист 1с профессионал": "Profession label lookup — not service buyer intent",
    "программист 1с ru": "Domain/brand lookup — not service buyer intent",
    "программист 1с ру": "Domain/brand lookup — not service buyer intent",
    "программист 1с бит": "Abbreviation/entity lookup — not service buyer intent",
    "программист 1с банк": "Entity/industry lookup — not service buyer intent",
    "программист 1с документы": "Documentation lookup — not service buyer intent",
    "программист 1с область": "Profession scope research — not service buyer intent",
    "программист 1с рускон": "Named entity lookup — not service buyer intent",
    "программист 1с франчайзи": "Franchisee lookup — not service buyer intent",
}

CA01_RECHECK_REJECT = {
    "программист 1с на проект": "Project-role query — not clear buyer intent",
    "программист 1с онлайн": "Delivery-mode label without buyer signal",
    "программист администратор 1с": "Job/role title — not service buyer intent",
    "программист аналитик 1с": "Job/role title — not service buyer intent",
    "программист консультант 1с": "Job/role title — not service buyer intent",
    "программист базы 1с": "Role/skill label — not service buyer intent",
}

CA01_EXPLICIT_KEEP = {
    "нужен программист 1с", "найти программиста 1с", "ищу программиста 1с для разовой задачи",
    "ищу 1с программиста для разовой задачи", "ищу программист 1с", "услуги программиста 1с",
    "частный программист 1с", "программист 1с удаленно", "программист 1с удалённо",
    "стоимость часа программиста 1с", "программист 1с зуп", "программист 1с унф",
    "программист 1с ут", "где найти программиста 1с", "найти программиста 1с на аутсорсинг",
    "нужен программист 1с для доработок", "программист 1с найти специалиста",
    "программист 1с дистанционно", "фриланс 1с программист",
}

CA02_BINDING_REJECT = {
    "1с продажа сопровождения": "Sales-of-support info — not buyer seeking provider",
    "1с итс специалист по сопровождению": "Job/role query — not outsourced support buyer",
    "казначейское сопровождение в 1с": "Treasury operation — not 1C support service",
    "казначейское сопровождение в 1с 8.3 бухгалтерия": "Treasury operation — not 1C support service",
    "казначейское сопровождение в 1с бухгалтерия": "Treasury operation — not 1C support service",
    "коммерческое предложение по сопровождению 1с": "Commercial-proposal template — not service buyer",
    "сопровождение сайта 1с": "Website support — unrelated to maintaining 1C",
    "специалист по сопровождению 1с": "Job/role query — not outsourced support buyer",
    "техническое задание на сопровождение 1с": "Technical-specification document — not service buyer",
    "техническое задание на сопровождение 1с erp": "Technical-specification document — not service buyer",
    "условия сопровождения 1с": "Terms/conditions lookup — not service buyer",
}

CA03_BINDING_REJECT = {
    "внедренцы и программисты 1с": "Profession listing — not service buyer intent",
    "программист 1с язык программирования": "Programming-language research — not service buyer",
    "счет от самозанятого на доработку 1с": "Invoice/document template — not service buyer",
    "техническое задание на доработку 1с": "Technical-specification document — not service buyer",
    "техническое на доработку 1с": "Technical-specification document — not service buyer",
    "тз на доработку 1с": "Technical-specification document — not service buyer",
}

CA04_MALFORMED_REJECT = {
    "битрикс интернет магазины интеграцией 1с": "Malformed query — not commercially useful",
    "интеграция 1с битрикс магазина с 1с": "Malformed query — not commercially useful",
    "обмена с сайтом 1с интеграция": "Malformed query — not commercially useful",
}

CA05_OPERATIONAL_REJECT = {
    "маркировка и контроль в номенклатуре 1с": "Operational UI task — not paid-service intent",
    "маркировка и контроль в номенклатуре 1с бухгалтерия": "Operational UI task — not paid-service intent",
    "отчет о нанесении честный знак 1с": "Report operation — not paid-service intent",
    "поставить на приход честный знак 1с": "Inventory operation — not paid-service intent",
    "честный знак у продавца в 1с": "Operational workflow — not paid-service intent",
    "отчет по кодам маркировки в 1с": "Report operation — not paid-service intent",
    "реализация с маркировкой кодами в 1с": "Operational workflow — not paid-service intent",
    "честный знак без 1с": "Informational comparison — not service buyer",
    "оператор 1с честный знак": "Operator lookup — not service buyer",
}

PROFESSION_RESEARCH_RE = re.compile(
    r"(?:описани|основ|перспектив|требовани|профессионал|становится|стань)\b",
    re.I,
)
DOC_TEMPLATE_RE = re.compile(
    r"техническ(?:ое|ая)\s+задани|(?:^|\s)тз\s+на|коммерческ(?:ое|ая)\s+предложени|"
    r"счет\s+от\s+самозанят|образец|пример\s+(?:тз|техническ)|"
    r"условия\s+сопровожден",
    re.I,
)
TREASURY_RE = re.compile(r"казначейск", re.I)
WEBSITE_SUPPORT_RE = re.compile(r"сопровождени[ея]\s+сайта", re.I)
ROLE_JOB_RE = re.compile(
    r"специалист\s+по\s+сопровожден|итс\s+специалист\s+по|"
    r"программист\s+(?:администратор|аналитик|консультант)\s+1с|"
    r"внедренцы\s+и\s+программист",
    re.I,
)
MARKING_CATEGORY_RE = re.compile(
    r"маркировк(?:а|и)\s+(?:воды|пива|одежды|масел|игрушек|молочн|шин|радио|импорт|набор)",
    re.I,
)
MARKING_REMAINDER_RE = re.compile(r"маркировк(?:а|и)\s+остатков|остатков\s+честн", re.I)
LOCAL_MODULE_RE = re.compile(r"локальн(?:ый|ого)\s+модул|(?:^|\s)лм\s+честн|подключени[ея]\s+лм", re.I)
SUZ_TOKEN_RE = re.compile(r"\bсуз\b|токен(?:ы|ов)?\s+(?:для|честн|ккт)|обновлени[ея]\s+(?:токен|ключа)", re.I)
MARKING_ERROR_RE = re.compile(r"техподдержк|поддержк(?:а|и)\s+(?:1с\s+)?честн|ошибк.*маркировк", re.I)
CONFIG_MARKING_RE = re.compile(
    r"маркировк(?:а|и)\s+в\s+1с|маркировк(?:а|и)\s+честн|настройк(?:а|и)\s+маркировк|"
    r"настройк(?:а|и)\s+честн|подключени[ея]\s+(?:маркировк|честн)|внедрени[ея]\s+(?:маркировк|честн)",
    re.I,
)
BITRIX24_RE = re.compile(r"битрикс\s*24|bitrix\s*24|битрикс24", re.I)
BITRIX_SITE_RE = re.compile(r"битрикс|1с[\s-]битрикс|управлени[ея]\s+сайтом", re.I)
SITE_INTEGRATION_RE = re.compile(r"интеграц.*сайт|сайт.*интеграц|личн(?:ого|ый)\s+кабинет", re.I)
SYNC_EXCHANGE_RE = re.compile(r"синхронизац|обмен\s+данн|обмен\s+1с|план(?:ов)?\s+обмен", re.I)
API_INTEGRATION_RE = re.compile(r"\bapi\b|по\s+api", re.I)

# ── geography ────────────────────────────────────────────────────────────────
NSO_RE = re.compile(
    r"новосибирск|новосибирск(?:ая|ой|ую|ие|им)?\s+област|\bнск\b|бердск|обь\b|искитим|куйбышев\b",
    re.I,
)
FOREIGN_RE = re.compile(
    r"беларус|казахстан|алмат|минск|\bднр\b|украин|белорус|киев|ташкент|бишкек",
    re.I,
)

RUSSIAN_CITY_TOKENS = [
    "москва", "москве", "москвы", "москов", "спб", "петербург", "санкт",
    "екатеринбург", "красноярск", "омск", "томск", "барнаул", "краснодар", "воронеж",
    "казан", "уфа", "уфе", "перм", "самар", "ростов", "нижн", "челябинск", "симферополь",
    "хабаровск", "иркутск", "ярославль", "владивосток", "белгород", "рязань", "тюмен",
    "калининград", "ставрополь", "сочи", "тула", "костром", "новороссийск", "вологд",
    "владимир", "севастопол", "ижевск", "саратов", "сергиев", "липецк", "ulan", "улан",
    "бийск", "верхняя пышма", "верхней пышм", "киров", "клин", "тольятти", "чебоксар",
    "архангельск", "астрахань", "балаших", "брянск", "владикавказ", "волгоград", "волжск",
    "вологда", "воронеж", "грозн", "дмитров", "иваново", "калуг", "кемерово", "курск",
    "магнитогорск", "мурманск", "орел", "оренбург", "пенза", "псков", "смоленск",
    "сургут", "таганрог", "тамбов", "твер", "улан-удэ", "улан удэ", "ульяновск",
    "химки", "чита", "якутск", "абakan", "абакан", "анапа", "армавир", "благовещенск",
    "великий новгород", "владивосток", "выборг", "дзержинск", "железногорск", "зеленоград",
    "каменск", "коломна", "королев", "курган", "мытищ", "нальчик", "невинномысск",
    "нижневартовск", "нижний", "новокузнецк", "новороссийск", "новочеркасск", "орск",
    "подольск", "прокопьевск", "пятигорск", "саранск", "северодвинск", "симферополь",
    "стерлитамак", "сызран", "сыктывкар", "таганрог", "тольятти", "хасавюрт", "череповец",
    "шахты", "энгельс", "ялта",
]

OTHER_CITY_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(c) for c in sorted(set(RUSSIAN_CITY_TOKENS), key=len, reverse=True)) + r")\w*\b",
    re.I,
)

REMOTE_EXPLICIT_RE = re.compile(
    r"удал[её]нн?(?:о|ая|ый|ые|ка)?|дистанционн|\bонлайн\b|по\s+(?:всей\s+)?росси|по\s+рф\b|без\s+выезд|удал[её]нк|аутсорс",
    re.I,
)
LOCAL_SVC_RE = re.compile(
    r"с\s+выездом|\bвыезд(?:ом|а|е|у)?\b|выезд\s+специалист|\bприехать\b|на\s+месте|в\s+офис(?:е|а|у)?\b",
    re.I,
)

# ── intent patterns ───────────────────────────────────────────────────────────
PRICE_HOUR_RE = re.compile(
    r"(?:"
    r"(?:1\s+)?час(?:а|u|ов)?\s+(?:работы\s+)?(?:программист|1с)|"
    r"нормо[\s-]?час|ставка\s+часа|стоимость.*час|сколько\s+стоит.*час|"
    r"час.*(?:программист|1с).*(?:цен|стоим)|"
    r"(?:цен|стоим).*(?:час|часа).*(?:программист|1с)|"
    r"программист.*(?:1\s+)?час(?:а|u)?|"
    r"часы\s+работы\s+программист|стоимость.*программист"
    r")",
    re.I,
)
CAREER_RE = re.compile(
    r"(?:^|\b)(?:"
    r"работа\s+программист|работа\s+программистом|поиск\s+работ|подработк|ваканс|"
    r"зарплат|заработн|должност|обязанност|трудов(?:ая|ой)\s+функ|профессия|карьер|"
    r"\bjunior\b|\bmiddle\b|джун|младш|старш|ведущ|главн|стажиров|резюме|\bhh\b|"
    r"ищет\s+работ|трудоустрой|опыт\s+работы\s+программист|опыт\s+работы"
    r")",
    re.I,
)
BUYER_HIRE_RE = re.compile(
    r"(?:^|\b)(?:"
    r"нужен|ищу|найти|найм|нанять|вызвать|заказать|где\s+найти"
    r")\s+(?:программист|1с\s+программист|специалист|разработчик)|"
    r"найти\s+программист|ищу\s+(?:программист|1с\s+программист)",
    re.I,
)
CONFIG_PRODUCT_RE = re.compile(
    r"\b(?:зуп|унф|ут|ерп|бухгалтери|документооборот|битрикс|предприятие|розниц|ка\s*2?)\b",
    re.I,
)
COMMERCIAL_RE = re.compile(
    r"услуг|стоимост|цен[аы]|сколько\s+стоит|заказать|нанять|вызвать|"
    r"частн|фриланс|доработк|сопровожден|обслуживан|настройк|внедрен|"
    r"не\s+работает|ошибк|исправ|интеграц|маркировк|честн.*знак|"
    r"расценк|под\s+ключ|срочно|недорог|заказ\b|подключ|нужен\s+программист|аутсорс",
    re.I,
)
MARKING_RE = re.compile(r"честн(?:ый|ого)\s+знак|маркировк(?:а|и|u|ой)|код(?:ы|ов)?\s+маркировк", re.I)
INTEGRATION_RE = re.compile(r"интеграц|битрикс|bitrix|api|обмен\s+данн|синхронизац", re.I)
HOWTO_INFO_RE = re.compile(r"как\s+(?:сделать|настро|подключ|интегрир|внедр|провод)", re.I)

SUSPICIOUS_KEEP_RE = re.compile(
    r"опыт\s+работы|пример|инструкци|договор|сертификат|как\s+сделать|что\s+это|"
    r"нужен\s+ли|готовые|(?<!\w)сайт(?!\w)|центр",
    re.I,
)
ENTITY_NOISE_RE = re.compile(
    r"\b(?:"
    r"дмитрий|иван|ал[её]на|роман|мешков|лидер\s+фарм|бэст\s+мебель|"
    r"парк\s+культур|элита\s+м|яндекс|ozon|озон|skillbox|скиллбокс|авито|"
    r"программист\s+1с\s+(?:фирма|элемент|сайт|парк|центр)\b|"
    r"программист\s+1с\s+\w+\s+(?:фарм|мебель)"
    r")\b",
    re.I,
)
DOC_LOOKUP_RE = re.compile(
    r"сертификат|договор\s+(?:на\s+)?(?:оказани|сопровожден|программ|доработк)|"
    r"договор\s+сопровожден|сопровожден(?:ие|ия)\s+1с\s+договор|"
    r"техническ(?:ое|ая)\s+задани(?:е|я)\s+пример|"
    r"пример\s+(?:тз|техническ|задан)|образец\s+(?:тз|техническ)|"
    r"готов(?:ые|ая|ый)\s+доработк|асп\s+сопровожден|центр\s+сопровожден",
    re.I,
)

GENERIC_GROUP_NAMES = {
    "Программист 1С — расширенные запросы",
    "Программист 1С — основной поиск",
    "Расширенные запросы",
    "Основной поиск",
    "Общий спрос",
}

LANDING_URLS = {
    "CA-01": "https://lk.corvonero.ru/programmist-1s/",
    "CA-02": "https://lk.corvonero.ru/soprovozhdenie-1s/",
    "CA-03": "https://lk.corvonero.ru/dorabotka-razrabotka-1s/",
    "CA-04": "https://lk.corvonero.ru/integracii-1s/",
    "CA-05": "https://lk.corvonero.ru/markirovka-chestny-znak/",
}

CA01_GROUP_FAMILIES = {
    "ca-01-specialist-search": "Программист 1С — услуги и настройка",
    "ca-01-find-hire-specialist": "Программист 1С — поиск специалиста",
    "ca-01-private-specialist": "Программист 1С — частный специалист",
    "ca-01-price-intent": "Программист 1С — стоимость часа",
    "ca-01-specialist-by-product": "Программист 1С — конфигурации",
    "ca-01-remote-specialist": "Программист 1С — удалённый специалист",
    "ca-01-city-remote": "Программист 1С — по городам России",
}

SERVICE_GROUP_MAP = {
    "CA-02": {
        "ca-02-direct-service-order": "Сопровождение 1С — заказ услуги",
        "ca-02-price-intent": "Сопровождение 1С — стоимость",
        "ca-02-support-buh": "Сопровождение 1С — бухгалтерия и БГУ",
        "ca-02-support-enterprise": "Сопровождение 1С — предприятие и ERP",
        "ca-02-support-zup-unf": "Сопровождение 1С — ЗУП, УТ и УНФ",
        "ca-02-support-its": "Сопровождение 1С — ИТС и абонентское",
        "ca-02-support-tech": "Сопровождение 1С — техподдержка и администрирование",
        "ca-02-support-org": "Сопровождение 1С — для организаций и ИП",
        "ca-02-support-and-maintenance": "Сопровождение и обслуживание 1С",
        "ca-02-provider-search": "Сопровождение 1С — поиск подрядчика",
        "ca-02-troubleshooting-not-working": "1С не работает — ошибки и восстановление",
        "default": "Сопровождение и обслуживание 1С",
    },
    "CA-03": {
        "ca-03-implementation": "Доработка 1С — внедрение",
        "ca-03-mod-config": "Доработка 1С — по конфигурациям",
        "ca-03-modification": "Доработка и разработка 1С",
        "default": "Доработка и разработка 1С",
    },
    "CA-04": {
        "ca-04-site": "Интеграция 1С с сайтом",
        "ca-04-bitrix24": "Интеграция 1С с Битрикс24",
        "ca-04-bitrix": "Интеграция 1С с 1С-Битрикс",
        "ca-04-sync": "Синхронизация и обмен данными",
        "ca-04-api": "Интеграция по API",
        "default": "Синхронизация и обмен данными",
    },
    "CA-05": {
        "ca-05-connect": "Честный знак — подключение",
        "ca-05-setup-exchange": "Честный знак — настройка и обмен",
        "ca-05-connect-setup": "Честный знак — подключение и настройка",
        "ca-05-integration": "Интеграция 1С с Честным знаком",
        "ca-05-marking-buh": "Маркировка — бухгалтерия и БП",
        "ca-05-marking-ut-unf": "Маркировка — УТ и УНФ",
        "ca-05-marking-roznica": "Маркировка — розница",
        "ca-05-marking-erp": "Маркировка — ERP и КА",
        "ca-05-config-marking": "Маркировка — настройка в конфигурациях 1С",
        "ca-05-marking-codes": "Коды маркировки — печать, передача и сканирование",
        "ca-05-remainder-marking": "Маркировка остатков",
        "ca-05-local-module": "Локальный модуль Честного знака",
        "ca-05-suz-tokens": "СУЗ и токены",
        "ca-05-ts-piot": "ТС ПИоТ",
        "ca-05-category-marking": "Маркировка по товарным категориям",
        "ca-05-errors-support": "Ошибки и техническая поддержка маркировки",
        "default": "Честный знак — подключение и настройка",
    },
}

# fix typo in CA01
CA01_GROUP_FAMILIES["ca-01-specialist-by-product"] = "Программист 1С — конфигурации"


def normalize_phrase(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def detect_city_token(phrase: str) -> str:
    p = normalize_phrase(phrase)
    if NSO_RE.search(p):
        return "NSO"
    if FOREIGN_RE.search(p):
        m = FOREIGN_RE.search(p)
        return m.group(0) if m else "FOREIGN"
    m = OTHER_CITY_RE.search(p)
    return m.group(0) if m else ""


def classify_geo(phrase: str) -> tuple[str, str]:
    p = normalize_phrase(phrase)
    if FOREIGN_RE.search(p):
        return "NONE", "Campaign scope is Russia only."
    city = detect_city_token(p)
    if city == "NSO" or LOCAL_SVC_RE.search(p):
        return "LOCAL_ONLY", f"NSO/local-visit signal ({city or 'on-site'})"
    if city:
        return "REMOTE_ONLY", f"Non-NSO Russian city/region: {city}"
    if REMOTE_EXPLICIT_RE.search(p):
        return "REMOTE_ONLY", "Remote-explicit phrase"
    return "BOTH", "Neutral commercial — eligible for LOCAL and REMOTE"


def route_service(source_ca: str, phrase: str) -> tuple[str, str]:
    p = normalize_phrase(phrase)
    if p in CA04_MARKING_MOVE:
        return "CA-05", "ca-05-integration"
    if MARKING_RE.search(p) and source_ca in ("CA-01", "CA-02", "CA-03", "CA-04"):
        if source_ca == "CA-04" and INTEGRATION_RE.search(p) and "честн" in p:
            return "CA-05", "ca-05-integration"
        return "CA-05", "ca-05-integration"
    if source_ca == "CA-04" and MARKING_RE.search(p) and not INTEGRATION_RE.search(p):
        return "CA-05", "ca-05-config-marking"
    return source_ca, ""


def infer_ca01_group(phrase: str, source_group: str) -> str:
    p = normalize_phrase(phrase)
    if p in CA01_EXPLICIT_KEEP or BUYER_HIRE_RE.search(p):
        return "ca-01-find-hire-specialist"
    if PRICE_HOUR_RE.search(p):
        return "ca-01-price-intent"
    if REMOTE_EXPLICIT_RE.search(p) and not LOCAL_SVC_RE.search(p):
        return "ca-01-remote-specialist"
    if re.search(r"частн|фриланс|исполнитель", p):
        return "ca-01-private-specialist"
    if CONFIG_PRODUCT_RE.search(p) and re.search(r"программист", p):
        return "ca-01-specialist-by-product"
    if detect_city_token(phrase) not in ("", "NSO", "FOREIGN") and re.search(r"программист", p):
        return "ca-01-city-remote"
    if re.search(r"доработк|настройк|внедрен|услуг", p):
        return "ca-01-specialist-search"
    legacy_map = {
        "ca-01-price-intent": "ca-01-price-intent",
        "ca-01-find-hire-specialist": "ca-01-find-hire-specialist",
        "ca-01-remote-freelance-specialist": "ca-01-remote-specialist",
        "ca-01-specialist-by-product": "ca-01-specialist-by-product",
        "ca-01-specialist-extended": "ca-01-specialist-search",
        "ca-01-specialist-search": "ca-01-specialist-search",
        "ca-01-direct-service-order": "ca-01-specialist-search",
    }
    return legacy_map.get(source_group, "ca-01-specialist-search")


def infer_ca04_group(phrase: str) -> str:
    p = normalize_phrase(phrase)
    if API_INTEGRATION_RE.search(p):
        return "ca-04-api"
    if BITRIX24_RE.search(p):
        return "ca-04-bitrix24"
    if SITE_INTEGRATION_RE.search(p) and not BITRIX_SITE_RE.search(p):
        return "ca-04-site"
    if BITRIX_SITE_RE.search(p):
        return "ca-04-bitrix"
    if SYNC_EXCHANGE_RE.search(p):
        return "ca-04-sync"
    if SITE_INTEGRATION_RE.search(p):
        return "ca-04-site"
    return "ca-04-sync"


def infer_ca05_group(phrase: str) -> str:
    p = normalize_phrase(phrase)
    if re.search(r"тс\s+пиот|пиот", p):
        return "ca-05-ts-piot"
    if MARKING_ERROR_RE.search(p):
        return "ca-05-errors-support"
    if SUZ_TOKEN_RE.search(p):
        return "ca-05-suz-tokens"
    if LOCAL_MODULE_RE.search(p):
        return "ca-05-local-module"
    if MARKING_REMAINDER_RE.search(p):
        return "ca-05-remainder-marking"
    if re.search(r"код(?:ы|ов)?\s+маркировк|печать\s+(?:код|маркиров)|сканирован|передач(?:а|и)\s+код", p):
        return "ca-05-marking-codes"
    if MARKING_CATEGORY_RE.search(p):
        return "ca-05-category-marking"
    if INTEGRATION_RE.search(p) and MARKING_RE.search(p):
        return "ca-05-integration"
    if re.search(r"бухгалтери|\bбух\b|\bбп\b", p) and MARKING_RE.search(p):
        return "ca-05-marking-buh"
    if re.search(r"\bут\b|управлени[ея]\s+торговл", p) and MARKING_RE.search(p):
        return "ca-05-marking-ut-unf"
    if re.search(r"унф", p) and MARKING_RE.search(p):
        return "ca-05-marking-ut-unf"
    if re.search(r"розниц", p) and MARKING_RE.search(p):
        return "ca-05-marking-roznica"
    if re.search(r"erp|ерп|ка\s*2|предприяти|комплексн", p) and MARKING_RE.search(p):
        return "ca-05-marking-erp"
    if CONFIG_MARKING_RE.search(p):
        return "ca-05-config-marking"
    if re.search(r"подключ", p):
        return "ca-05-connect"
    if re.search(r"обмен|синхронизац", p) and MARKING_RE.search(p):
        return "ca-05-setup-exchange"
    if re.search(r"настройк|внедрен|установк", p):
        return "ca-05-setup-exchange"
    return "ca-05-connect-setup"


def infer_group_id(row: dict[str, Any]) -> str:
    ca = row["final_service"]
    phrase = row["phrase"]
    sg = row.get("source_group", "")
    p = normalize_phrase(phrase)
    if ca == "CA-01":
        return infer_ca01_group(phrase, sg)
    if ca == "CA-02":
        if re.search(r"не\s+работает|ошибк|восстанов", p):
            return "ca-02-troubleshooting-not-working"
        if re.search(r"стоимост|цен[аы]|сколько\s+стоит", p):
            return "ca-02-price-intent"
        if re.search(r"услуг|оказани", p):
            return "ca-02-direct-service-order"
        if re.search(r"фирм|компани|подрядчик|аутсорс", p):
            return "ca-02-provider-search"
        if re.search(r"бухгалтери|бгу\b", p):
            return "ca-02-support-buh"
        if re.search(r"предприяти|erp|ерп", p):
            return "ca-02-support-enterprise"
        if re.search(r"зуп|унф|ут\b|торговл", p):
            return "ca-02-support-zup-unf"
        if re.search(r"итс|абонентск", p):
            return "ca-02-support-its"
        if re.search(r"техническ|информацион|программн|обслуживан|поддержк|администр|обновлен", p):
            return "ca-02-support-tech"
        if re.search(r"организаци|клиент|бюджет|учрежден|\bип\b", p):
            return "ca-02-support-org"
        return "ca-02-support-and-maintenance"
    if ca == "CA-03":
        if re.search(r"внедрен", p) and not re.search(r"доработк", p):
            return "ca-03-implementation"
        if re.search(r"зуп|унф|ут\b|erp|ерп|бухгалтери|документооборот|торговл", p):
            return "ca-03-mod-config"
        return "ca-03-modification"
    if ca == "CA-04":
        return infer_ca04_group(phrase)
    if ca == "CA-05":
        return infer_ca05_group(phrase)
    return sg or "default"


def group_name_for(ca: str, group_id: str) -> str:
    if ca == "CA-01":
        return CA01_GROUP_FAMILIES.get(group_id, "Программист 1С — общий спрос")
    svc_map = SERVICE_GROUP_MAP.get(ca, {})
    return svc_map.get(group_id, svc_map.get("default", group_id))


def _reject_row(out: dict, reason: str, correction: str, service: str | None = None) -> dict:
    geo, _ = classify_geo(out["phrase"])
    out.update(
        decision="REJECT",
        final_service=service or out.get("final_service", ""),
        final_geo=geo if geo != "NONE" else "NONE",
        reason=reason,
        commercial_intent="False",
        confidence="HIGH",
        operator_review="True",
        v25_correction=correction,
    )
    return out


def apply_v25_curation(row: dict[str, Any]) -> dict[str, Any]:
    out = dict(row)
    p = normalize_phrase(row["phrase"])
    v24_decision = row["decision"]
    v24_geo = row["final_geo"]
    v24_service = row["final_service"]
    correction = "v24_carried"
    reason = row.get("reason", "")

    out["v24_decision"] = v24_decision
    out["v24_final_geo"] = v24_geo
    out["v24_final_service"] = v24_service

    decision = v24_decision
    final_service = v24_service
    final_geo = v24_geo

    # Preserve V2.4 REJECT unless explicit REJECT→KEEP (none in V2.5 charter)
    if decision == "REJECT":
        out.update(v25_correction="v24_carried", operator_review="False")
        return out

    if decision not in ("KEEP", "MOVE"):
        out.update(v25_correction="v24_carried", operator_review="False")
        return out

    # Explicit buyer-intent KEEP overrides (CA-01)
    if p in CA01_EXPLICIT_KEEP:
        geo, geo_reason = classify_geo(row["phrase"])
        out.update(
            decision="KEEP",
            final_service="CA-01",
            final_geo=geo,
            reason="Clear buyer intent for programmer services",
            commercial_intent="True",
            confidence="HIGH",
            operator_review="True",
            v25_correction="ca01_explicit_keep",
        )
        return out

    # Binding phrase-level rejections
    binding_maps = [
        (CA01_BINDING_REJECT, "ca01_binding_reject"),
        (CA01_RECHECK_REJECT, "ca01_recheck_reject"),
        (CA02_BINDING_REJECT, "ca02_binding_reject"),
        (CA03_BINDING_REJECT, "ca03_binding_reject"),
        (CA04_MALFORMED_REJECT, "ca04_malformed_reject"),
        (CA05_OPERATIONAL_REJECT, "ca05_operational_reject"),
        (BINDING_KEEP_TO_REJECT, "legacy_binding_reject"),
        (BINDING_HONEST_SIGN_REJECT, "honest_sign_howto_reject"),
    ]
    for mapping, tag in binding_maps:
        if p in mapping:
            return _reject_row(out, mapping[p], tag, final_service)

    # MOVE rows preserved
    if p in CA04_MARKING_MOVE:
        geo, _ = classify_geo(row["phrase"])
        out.update(
            decision="MOVE",
            final_service="CA-05",
            final_geo=geo,
            reason="Honest Sign / marking integration → CA-05",
            commercial_intent="True",
            confidence="HIGH",
            operator_review="False",
            source_group="ca-05-integration",
            v25_correction="ca04_to_ca05_move_preserved",
        )
        return out

    # Recompute geo for active rows
    new_geo, geo_reason = classify_geo(row["phrase"])
    if new_geo != final_geo:
        final_geo = new_geo
        correction = "geo_recheck"
        reason = geo_reason
    out["detected_city"] = detect_city_token(row["phrase"])

    if FOREIGN_RE.search(p) or final_geo == "NONE":
        return _reject_row(out, "Foreign geography — not deployable", "foreign_geo_reject", final_service)

    # Cross-cutting non-commercial patterns on remaining KEEP/MOVE
    if CAREER_RE.search(p):
        return _reject_row(out, "Career/job-seeker intent", "career_reject", final_service)
    if ENTITY_NOISE_RE.search(p) and not COMMERCIAL_RE.search(p):
        return _reject_row(out, "Named person/entity lookup", "entity_noise_reject", final_service)
    if DOC_TEMPLATE_RE.search(p) or DOC_LOOKUP_RE.search(p):
        return _reject_row(out, "Document/template lookup — not service buyer", "doc_template_reject", final_service)
    if TREASURY_RE.search(p):
        return _reject_row(out, "Treasury operation — not 1C support service", "treasury_reject", final_service)
    if WEBSITE_SUPPORT_RE.search(p):
        return _reject_row(out, "Website support — unrelated to 1C maintenance", "website_support_reject", final_service)
    if ROLE_JOB_RE.search(p):
        return _reject_row(out, "Job/role query — not outsourced service buyer", "role_job_reject", final_service)
    if PROFESSION_RESEARCH_RE.search(p) and final_service == "CA-01":
        return _reject_row(out, "Profession research — not service buyer", "profession_research_reject", final_service)

    # CA-01 bare profession labels without buyer signal
    if final_service == "CA-01" and re.fullmatch(
        r"программист\s+1с(?:\s+(?:7\.?7|8(?:\.3)?|8\.5|россия|настройка|платформа\s+8\.5))?",
        p,
    ):
        pass  # generic/version service searches remain
    elif final_service == "CA-01" and re.match(r"^программист\s+1с\s+\w+$", p):
        city = detect_city_token(p)
        if city in ("", "NSO"):
            if not COMMERCIAL_RE.search(p) and not CONFIG_PRODUCT_RE.search(p):
                return _reject_row(out, "Profession label without buyer signal", "ca01_weak_label_reject", final_service)

    # CA-05 informational how-to without implementation buyer signal
    if final_service == "CA-05" and HOWTO_INFO_RE.search(p):
        if not re.search(r"подключ|настройк|внедрен|специалист|услуг|заказ", p):
            return _reject_row(out, "Informational how-to — not paid-service intent", "ca05_howto_reject", final_service)

    # CA-05 generic marking without setup/service signal
    if final_service == "CA-05" and re.search(r"^маркировка\s+в\s+1с(?:\s+\d|$)", p):
        if not re.search(r"настройк|подключ|внедрен|остатков|специалист|услуг", p):
            return _reject_row(out, "Generic marking lookup — weak service intent", "ca05_generic_marking_reject", final_service)

    # Service routing check
    routed_ca, routed_gid = route_service(final_service, row["phrase"])
    if routed_ca != final_service:
        decision = "MOVE"
        final_service = routed_ca
        if routed_gid:
            out["source_group"] = routed_gid
        correction = "service_route_move"
        reason = f"Service routing → {routed_ca}"

    out.update(
        decision=decision,
        final_service=final_service,
        final_geo=final_geo,
        reason=reason,
        commercial_intent="True",
        confidence="HIGH",
        operator_review="False",
        v25_correction=correction if (
            v24_decision != decision or v24_geo != final_geo or v24_service != final_service
        ) else "v24_carried",
    )
    if out["v25_correction"] == "v24_carried" and correction != "v24_carried":
        out["v25_correction"] = correction
    return out


def campaigns_for_row(row: dict[str, Any]) -> list[str]:
    if row["decision"] not in ("KEEP", "MOVE"):
        return []
    geo = row["final_geo"]
    ca = row["final_service"]
    camps = []
    if geo in ("BOTH", "LOCAL_ONLY"):
        camps.append(f"{ca}-LOCAL")
    if geo in ("BOTH", "REMOTE_ONLY"):
        camps.append(f"{ca}-REMOTE")
    return camps


def build_final_groups(register: list[dict]) -> list[dict]:
    buckets: dict[tuple[str, str, str, str], list[str]] = defaultdict(list)
    for r in register:
        if r["decision"] not in ("KEEP", "MOVE"):
            continue
        gid = infer_group_id(r)
        gname = group_name_for(r["final_service"], gid)
        if gname in GENERIC_GROUP_NAMES:
            gname = group_name_for(r["final_service"], infer_group_id(r))
        for camp in campaigns_for_row(r):
            mode = "LOCAL" if camp.endswith("LOCAL") else "REMOTE"
            buckets[(camp, mode, gid, gname)].append(r["phrase"])

    # Merge one-key groups into semantically closest sibling
    merge_targets = {
        "Программист 1С — услуги и настройка": [
            "Программист 1С — заказ услуги",
        ],
        "Сопровождение и обслуживание 1С": ["Сопровождение 1С — заказ услуги"],
        "Доработка и разработка 1С": ["Доработка 1С — внедрение"],
    }
    by_camp: dict[str, list[tuple[str, str, str, list[str]]]] = defaultdict(list)
    for (camp, mode, gid, gname), phrases in buckets.items():
        by_camp[camp].append((gid, gname, mode, phrases))

    merged: dict[tuple[str, str, str, str], list[str]] = dict(buckets)
    for camp, groups in by_camp.items():
        for gid, gname, mode, phrases in groups:
            if len(phrases) == 1 and gname in merge_targets:
                for target in merge_targets[gname]:
                    key = next((k for k in merged if k[0] == camp and k[3] == target), None)
                    if key and len(merged[key]) >= 2:
                        merged[key].extend(phrases)
                        del merged[(camp, mode, gid, gname)]
                        break

    rows = []
    for (camp, mode, gid, gname), phrases in sorted(merged.items()):
        ca = camp.rsplit("-", 1)[0]
        rows.append({
            "campaign": camp,
            "mode": mode,
            "group_id": gid,
            "group_name": gname,
            "phrase_count": len(phrases),
            "phrase_list": "; ".join(sorted(set(phrases))),
            "landing_url": LANDING_URLS.get(ca, ""),
            "commercial_intent": ca,
        })
    return rows


def trim_text(text: str, max_len: int = 81) -> str:
    if len(text) <= max_len:
        return text
    for cut in [
        text.replace(" по договору", ""),
        text.replace(", по договору", ""),
        re.sub(r"\s+", " ", text)[:max_len].rsplit(" ", 1)[0] + ".",
    ]:
        if len(cut) <= max_len:
            return cut
    return text[: max_len - 1] + "…"


def ad_templates() -> dict[tuple[str, str], dict]:
    """Group-specific ad copy — no unsupported claims (опытные, смета, гарантия, фикс. сроки)."""
    t: dict[tuple[str, str], dict] = {}

    def add(gname: str, local: dict, remote: dict) -> None:
        t[(gname, "LOCAL")] = {**local, "display_path": local.get("display_path", "")}
        t[(gname, "REMOTE")] = {**remote, "display_path": remote.get("display_path", "")}

    add(
        "Программист 1С — услуги и настройка",
        {"headline_1": "Программист 1С для бизнеса", "headline_2": "Выезд по Новосибирску",
         "text": "Доработки, настройка и консультации по 1С. Работа по договору.", "display_path": "programmist-1s"},
        {"headline_1": "Программист 1С для бизнеса", "headline_2": "Удалённо по России",
         "text": "Доработки, настройка и консультации по 1С. Подключение удалённо.", "display_path": "programmist-1s"},
    )
    add(
        "Программист 1С — по городам России",
        {"headline_1": "Программист 1С удалённо", "headline_2": "Работа по России",
         "text": "Подключение специалиста 1С удалённо. Минимальный заказ — 2 часа.", "display_path": "programmist-1s"},
        {"headline_1": "Программист 1С удалённо", "headline_2": "Удалённо по России",
         "text": "Подключение специалиста 1С удалённо. Минимальный заказ — 2 часа.", "display_path": "programmist-1s"},
    )
    add(
        "Программист 1С — поиск специалиста",
        {"headline_1": "Нужен программист 1С?", "headline_2": "Выезд по Новосибирску",
         "text": "Подключим специалиста к вашей задаче. С выездом по Новосибирску.", "display_path": "programmist-1s"},
        {"headline_1": "Нужен программист 1С?", "headline_2": "Удалённо по России",
         "text": "Подключим специалиста к вашей задаче. Работа удалённо по России.", "display_path": "programmist-1s"},
    )
    add(
        "Программист 1С — частный специалист",
        {"headline_1": "Частный программист 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Разовые задачи и доработки 1С. С выездом по Новосибирску.", "display_path": "programmist-1s"},
        {"headline_1": "Частный программист 1С", "headline_2": "Удалённо по России",
         "text": "Разовые задачи и доработки 1С. Подключение удалённо.", "display_path": "programmist-1s"},
    )
    add(
        "Программист 1С — стоимость часа",
        {"headline_1": "Программист 1С — от 3 000 ₽ в час", "headline_2": "Выезд по Новосибирску",
         "text": "Минимальный заказ — 2 часа. Работаем с выездом в Новосибирске.", "display_path": "programmist-1s"},
        {"headline_1": "Программист 1С — от 3 000 ₽ в час", "headline_2": "Удалённо по России",
         "text": "Минимальный заказ — 2 часа. Подключение и работа удалённо.", "display_path": "programmist-1s"},
    )
    add(
        "Программист 1С — конфигурации",
        {"headline_1": "Программист 1С по ЗУП, УТ и УНФ", "headline_2": "Выезд по Новосибирску",
         "text": "Доработки и настройка конфигураций 1С. С выездом по Новосибирску.", "display_path": "programmist-1s"},
        {"headline_1": "Программист 1С по ЗУП, УТ и УНФ", "headline_2": "Удалённо по России",
         "text": "Доработки и настройка конфигураций 1С. Подключение удалённо.", "display_path": "programmist-1s"},
    )
    add(
        "Программист 1С — удалённый специалист",
        {"headline_1": "Программист 1С удалённо", "headline_2": "Работа по России",
         "text": "Доработки и поддержка 1С без выезда. Подключение удалённо.", "display_path": "programmist-1s"},
        {"headline_1": "Программист 1С удалённо", "headline_2": "Удалённо по России",
         "text": "Доработки и поддержка 1С без выезда. Подключение удалённо.", "display_path": "programmist-1s"},
    )
    add(
        "Сопровождение 1С — заказ услуги",
        {"headline_1": "Сопровождение и поддержка 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Обновления, консультации и исправление ошибок в 1С.", "display_path": "soprovozhdenie"},
        {"headline_1": "Сопровождение и поддержка 1С", "headline_2": "Удалённо по России",
         "text": "Обновления, консультации и исправление ошибок в 1С.", "display_path": "soprovozhdenie"},
    )
    add(
        "Сопровождение 1С — стоимость",
        {"headline_1": "Стоимость сопровождения 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Расчёт часа и абонентского сопровождения 1С.", "display_path": "soprovozhdenie"},
        {"headline_1": "Стоимость сопровождения 1С", "headline_2": "Удалённо по России",
         "text": "Расчёт часа и абонентского сопровождения 1С.", "display_path": "soprovozhdenie"},
    )
    add(
        "Сопровождение и обслуживание 1С",
        {"headline_1": "Сопровождение 1С для компаний", "headline_2": "Выезд по Новосибирску",
         "text": "Техподдержка, обновления и администрирование баз 1С.", "display_path": "soprovozhdenie"},
        {"headline_1": "Сопровождение 1С для компаний", "headline_2": "Удалённо по России",
         "text": "Техподдержка, обновления и администрирование баз 1С.", "display_path": "soprovozhdenie"},
    )
    add(
        "1С не работает — ошибки и восстановление",
        {"headline_1": "1С не работает — поможем", "headline_2": "Выезд по Новосибирску",
         "text": "Диагностика ошибок и восстановление работы 1С.", "display_path": "soprovozhdenie"},
        {"headline_1": "1С не работает — поможем", "headline_2": "Удалённо по России",
         "text": "Диагностика ошибок и восстановление работы 1С.", "display_path": "soprovozhdenie"},
    )
    add(
        "Сопровождение 1С — поиск подрядчика",
        {"headline_1": "Сопровождение 1С для компаний", "headline_2": "Выезд по Новосибирску",
         "text": "Подберём подрядчика для сопровождения и поддержки 1С.", "display_path": "soprovozhdenie"},
        {"headline_1": "Сопровождение 1С для компаний", "headline_2": "Удалённо по России",
         "text": "Подберём подрядчика для сопровождения и поддержки 1С.", "display_path": "soprovozhdenie"},
    )
    add(
        "Доработка 1С — внедрение",
        {"headline_1": "Внедрение и доработка 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка и доработка процессов в 1С:Предприятие.", "display_path": "dorabotka-1s"},
        {"headline_1": "Внедрение и доработка 1С", "headline_2": "Удалённо по России",
         "text": "Настройка и доработка процессов в 1С:Предприятие.", "display_path": "dorabotka-1s"},
    )
    add(
        "Доработка и разработка 1С",
        {"headline_1": "Доработка и разработка 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Изменения конфигураций, отчётов и обменов под ваш бизнес.", "display_path": "dorabotka-1s"},
        {"headline_1": "Доработка и разработка 1С", "headline_2": "Удалённо по России",
         "text": "Изменения конфигураций, отчётов и обменов под ваш бизнес.", "display_path": "dorabotka-1s"},
    )
    add(
        "Интеграция 1С с сайтом",
        {"headline_1": "Интеграция 1С с сайтом", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка обмена заказами и остатками между сайтом и 1С.", "display_path": "integracii"},
        {"headline_1": "Интеграция 1С с сайтом", "headline_2": "Удалённо по России",
         "text": "Настройка обмена заказами и остатками между сайтом и 1С.", "display_path": "integracii"},
    )
    add(
        "Интеграция 1С с Битрикс24",
        {"headline_1": "Интеграция 1С с Битрикс24", "headline_2": "Выезд по Новосибирску",
         "text": "Свяжем 1С с Битрикс24: сделки, заказы и документы.", "display_path": "integracii"},
        {"headline_1": "Интеграция 1С с Битрикс24", "headline_2": "Удалённо по России",
         "text": "Свяжем 1С с Битрикс24: сделки, заказы и документы.", "display_path": "integracii"},
    )
    add(
        "Интеграция 1С с 1С-Битрикс",
        {"headline_1": "Интеграция 1С и 1С-Битрикс", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка обмена между 1С и интернет-магазином на Битрикс.", "display_path": "integracii"},
        {"headline_1": "Интеграция 1С и 1С-Битрикс", "headline_2": "Удалённо по России",
         "text": "Настройка обмена между 1С и интернет-магазином на Битрикс.", "display_path": "integracii"},
    )
    add(
        "Синхронизация и обмен данными",
        {"headline_1": "Синхронизация данных в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка обмена и синхронизации между базами 1С.", "display_path": "integracii"},
        {"headline_1": "Синхронизация данных в 1С", "headline_2": "Удалённо по России",
         "text": "Настройка обмена и синхронизации между базами 1С.", "display_path": "integracii"},
    )
    add(
        "Интеграция по API",
        {"headline_1": "Интеграция 1С по API", "headline_2": "Выезд по Новосибирску",
         "text": "Подключим внешние сервисы к 1С через API и обмен.", "display_path": "integracii"},
        {"headline_1": "Интеграция 1С по API", "headline_2": "Удалённо по России",
         "text": "Подключим внешние сервисы к 1С через API и обмен.", "display_path": "integracii"},
    )
    add(
        "Честный знак — подключение и настройка",
        {"headline_1": "Честный знак в 1С — настройка", "headline_2": "Выезд по Новосибирску",
         "text": "Подключение маркировки и обмен с Честным знаком в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Честный знак в 1С — настройка", "headline_2": "Удалённо по России",
         "text": "Подключение маркировки и обмен с Честным знаком в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Интеграция 1С с Честным знаком",
        {"headline_1": "Интеграция 1С с Честным знаком", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка обмена маркировкой и Честным знаком в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Интеграция 1С с Честным знаком", "headline_2": "Удалённо по России",
         "text": "Настройка обмена маркировкой и Честным знаком в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Маркировка — настройка в конфигурациях 1С",
        {"headline_1": "Маркировка в конфигурациях 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка маркировки в УТ, УНФ, Бухгалтерии и Рознице.", "display_path": "markirovka-1s"},
        {"headline_1": "Маркировка в конфигурациях 1С", "headline_2": "Удалённо по России",
         "text": "Настройка маркировки в УТ, УНФ, Бухгалтерии и Рознице.", "display_path": "markirovka-1s"},
    )
    add(
        "Коды маркировки — печать, передача и сканирование",
        {"headline_1": "Коды маркировки в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Печать, передача и сканирование кодов маркировки в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Коды маркировки в 1С", "headline_2": "Удалённо по России",
         "text": "Печать, передача и сканирование кодов маркировки в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Маркировка остатков",
        {"headline_1": "Маркировка остатков в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Поможем оформить и настроить маркировку остатков в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Маркировка остатков в 1С", "headline_2": "Удалённо по России",
         "text": "Поможем оформить и настроить маркировку остатков в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Локальный модуль Честного знака",
        {"headline_1": "Локальный модуль Честного знака", "headline_2": "Выезд по Новосибирску",
         "text": "Установка и настройка ЛМ Честного знака для обмена с 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Локальный модуль Честного знака", "headline_2": "Удалённо по России",
         "text": "Установка и настройка ЛМ Честного знака для обмена с 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "СУЗ и токены",
        {"headline_1": "СУЗ и токены Честного знака", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка СУЗ, токенов и авторизации для обмена с 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "СУЗ и токены Честного знака", "headline_2": "Удалённо по России",
         "text": "Настройка СУЗ, токенов и авторизации для обмена с 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Маркировка по товарным категориям",
        {"headline_1": "Маркировка товаров в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка маркировки по категориям: одежда, пиво, вода и др.", "display_path": "markirovka-1s"},
        {"headline_1": "Маркировка товаров в 1С", "headline_2": "Удалённо по России",
         "text": "Настройка маркировки по категориям: одежда, пиво, вода и др.", "display_path": "markirovka-1s"},
    )
    add(
        "Ошибки и техническая поддержка маркировки",
        {"headline_1": "Поддержка маркировки в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Исправление ошибок обмена маркировкой и Честным знаком.", "display_path": "markirovka-1s"},
        {"headline_1": "Поддержка маркировки в 1С", "headline_2": "Удалённо по России",
         "text": "Исправление ошибок обмена маркировкой и Честным знаком.", "display_path": "markirovka-1s"},
    )
    add(
        "ТС ПИоТ",
        {"headline_1": "ТС ПИоТ и Честный знак в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка ТС ПИоТ и обмен маркировкой в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "ТС ПИоТ и Честный знак в 1С", "headline_2": "Удалённо по России",
         "text": "Настройка ТС ПИоТ и обмен маркировкой в 1С.", "display_path": "markirovka-1s"},
    )
    return t


def build_ads(groups: list[dict]) -> list[dict]:
    templates = ad_templates()
    ads = []
    for g in groups:
        mode = g["mode"]
        gname = g["group_name"]
        prop = templates.get((gname, mode), {
            "headline_1": gname[:56],
            "headline_2": "Выезд по Новосибирску" if mode == "LOCAL" else "Удалённо по России",
            "text": "Услуги 1С для бизнеса: настройка, доработки и поддержка.",
            "display_path": "1c-uslugi",
        })
        h1 = prop["headline_1"][:56]
        h2 = prop["headline_2"][:30]
        text = trim_text(prop["text"], 81)
        direct = "PASS" if len(h1) <= 56 and len(h2) <= 30 and len(text) <= 81 else "LENGTH_ISSUE"
        ads.append({
            "campaign": g["campaign"],
            "group_id": g["group_id"],
            "group_name": gname,
            "headline_1": h1,
            "headline_2": h2,
            "text": text,
            "display_path": prop.get("display_path", ""),
            "landing_url": g["landing_url"],
            "headline_1_chars": len(h1),
            "headline_2_chars": len(h2),
            "text_chars": len(text),
            "direct_validation": direct,
            "character_counts": json.dumps({
                "headline_1": len(h1), "headline_2": len(h2), "text": len(text),
            }, ensure_ascii=False),
        })
    return ads


def negative_conflicts(negative: str, phrase: str) -> bool:
    neg = normalize_phrase(negative.lstrip("-"))
    phr = normalize_phrase(phrase)
    if not neg or not phr:
        return False
    if " " in neg:
        return neg in phr
    parts = [p for p in re.split(r"[^\wё]+", phr, flags=re.UNICODE) if p]
    for part in parts:
        if part == neg or part.startswith(neg) or neg in part:
            return True
    return neg in phr


def rebuild_negatives_v25(kept_by_campaign: dict[str, list[str]]) -> list[dict]:
    """Rebuild campaign negatives from final curated core — not inherited from V2.4 list."""
    career = [
        ("вакансия", "Blocks career/junk intent"),
        ("зарплата", "Blocks career/junk intent"),
        ("резюме", "Blocks career/junk intent"),
        ("работа программистом", "Blocks career/junk intent"),
        ("подработка", "Blocks career/junk intent"),
        ("обязанности", "Blocks career/junk intent"),
        ("становится программистом", "Blocks career/junk intent"),
        ("стань программистом", "Blocks career/junk intent"),
        ("hh", "Blocks career/junk intent"),
    ]
    junk = [
        ("скачать", "Blocks download/piracy intent"),
        ("кряк", "Blocks download/piracy intent"),
        ("торрент", "Blocks download/piracy intent"),
        ("бесплатно", "Blocks freebie intent"),
        ("мем", "Blocks non-commercial intent"),
    ]
    edu = [
        ("курсы", "Blocks education intent"),
        ("образование", "Blocks education intent"),
        ("колледж", "Blocks education intent"),
        ("инструкция", "Blocks documentation lookup"),
        ("сертификация", "Blocks certification lookup"),
    ]
    purchase = [
        ("купить 1с", "Blocks software purchase — campaign sells services"),
        ("лицензия 1с", "Blocks license purchase — phrase-match"),
    ]
    local_remote_block = [
        ("удаленно", "LOCAL — blocks explicit remote-delivery intent"),
        ("удалённо", "LOCAL — blocks explicit remote-delivery intent"),
        ("дистанционно", "LOCAL — blocks explicit remote-delivery intent; phrase-match"),
        ("онлайн", "LOCAL — blocks remote-delivery slang"),
        ("по россии", "LOCAL — blocks remote geography signal"),
        ("по рф", "LOCAL — blocks remote geography signal"),
        ("по всей россии", "LOCAL — blocks remote geography signal"),
        ("удаленка", "LOCAL — blocks remote-work slang"),
        ("удалёнка", "LOCAL — blocks remote-work slang"),
        ("без выезда", "LOCAL — blocks opposite delivery mode"),
    ]
    remote_local_block = [
        ("выезд", "REMOTE — blocks explicit local-visit intent"),
        ("с выездом", "REMOTE — blocks explicit local-visit intent"),
        ("выезд специалиста", "REMOTE — blocks explicit local-visit intent"),
        ("новосибирск", "REMOTE — blocks NSO local-visit intent"),
        ("новосибирская", "REMOTE — blocks NSO local-visit intent"),
        ("новосибирский", "REMOTE — blocks NSO local-visit intent"),
        ("на месте", "REMOTE — blocks on-site visit intent"),
        ("в офис", "REMOTE — blocks on-site visit intent"),
        ("приехать", "REMOTE — blocks on-site visit intent"),
    ]

    campaigns = sorted(kept_by_campaign.keys())
    rows: list[dict] = []
    for camp in campaigns:
        is_local = camp.endswith("LOCAL")
        candidates = career + junk + edu + purchase
        if is_local:
            candidates += local_remote_block
        else:
            candidates += remote_local_block

        for neg, intent_reason in candidates:
            hits = [p for p in kept_by_campaign.get(camp, []) if negative_conflicts(neg, p)]
            decision = "KEEP"
            final_neg = neg
            reason = intent_reason
            if neg == "лицензия 1с":
                final_neg = '"лицензия 1с"'
                decision = "NARROW"
            elif neg == "дистанционно" and is_local:
                final_neg = '"дистанционно"'
                decision = "NARROW"
            elif hits:
                decision = "NARROW"
                final_neg = f'"{neg}"' if " " not in neg else neg
                reason = f"{intent_reason}; conflicts with {len(hits)} kept phrase(s) — phrase-match"
            rows.append({
                "campaign": camp,
                "negative": neg,
                "intent_blocked": intent_reason.split("—")[0].strip().replace("Blocks ", ""),
                "exact_included_phrase_conflict_check": "PASS" if not hits else f"CONFLICT:{len(hits)}",
                "decision": decision,
                "reason": reason,
                "conflict_count": len(hits),
                "affected_phrases": "; ".join(hits[:10]),
                "final_negative": final_neg,
                "source_negative": neg,
            })
    return rows


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            flat = {k: row.get(k, "") for k in fieldnames}
            w.writerow(flat)


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def validate_register(register: list[dict], groups: list[dict]) -> dict[str, Any]:
    issues = []
    for r in register:
        if not r.get("decision"):
            issues.append(f"No decision: {r['phrase']}")
    # Russian other-city in LOCAL eligibility
    for r in register:
        if r["decision"] not in ("KEEP", "MOVE"):
            continue
        city = detect_city_token(r["phrase"])
        if city and city != "NSO" and r["final_geo"] in ("BOTH", "LOCAL_ONLY"):
            issues.append(f"Other city in LOCAL-eligible: {r['phrase']}")
    for g in groups:
        if g["phrase_count"] == 0:
            issues.append(f"Empty group: {g['campaign']}/{g['group_name']}")
        if g["phrase_count"] > 50:
            issues.append(f"Group over 50: {g['campaign']}/{g['group_name']} ({g['phrase_count']})")
        if g["group_name"] in GENERIC_GROUP_NAMES:
            issues.append(f"Generic group: {g['group_name']}")
    noncommercial_in_keep = [
        r["phrase"] for r in register
        if r["decision"] in ("KEEP", "MOVE") and (
            CAREER_RE.search(r["phrase"])
            or r["phrase"] in CA01_BINDING_REJECT
            or r["phrase"] in CA02_BINDING_REJECT
            or r["phrase"] in CA03_BINDING_REJECT
        )
    ]
    return {"issues": issues, "career_in_keep": noncommercial_in_keep, "noncommercial_in_keep": noncommercial_in_keep}


def require_operator_gate() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This C2b helper is not safe for casual execution."
        )


def main() -> None:
    require_operator_gate()
    label = subprocess.check_output(
        ["powershell.exe", "-NoProfile", "-Command", "(Get-Volume -DriveLetter X).FileSystemLabel"],
        text=True,
    ).strip()
    if label != "AI WS":
        raise SystemExit("STOP — volume label mismatch")

    v24_register = load_csv(V24_REVIEW / "CORVONERO-V2.4-ALL-PHRASES-FINAL.csv")
    if len(v24_register) != 760:
        raise SystemExit(f"Expected 760 phrases, got {len(v24_register)}")

    register = [apply_v25_curation(row) for row in v24_register]

    changelog = []
    for old, new in zip(v24_register, register):
        if (
            old["decision"] != new["decision"]
            or old["final_geo"] != new["final_geo"]
            or old["final_service"] != new["final_service"]
        ):
            changelog.append({
                "phrase": new["phrase"],
                "v24_decision": old["decision"],
                "v25_decision": new["decision"],
                "v24_final_geo": old["final_geo"],
                "v25_final_geo": new["final_geo"],
                "v24_final_service": old["final_service"],
                "v25_final_service": new["final_service"],
                "v25_correction": new.get("v25_correction", ""),
                "reason": new.get("reason", ""),
            })

    dec_counter = Counter(r["decision"] for r in register)
    geo_counter = Counter(r["final_geo"] for r in register)

    kept_by_campaign: dict[str, list[str]] = defaultdict(list)
    for r in register:
        for camp in campaigns_for_row(r):
            kept_by_campaign[camp].append(r["phrase"])

    groups = build_final_groups(register)
    ads = build_ads(groups)
    neg_rows = rebuild_negatives_v25(kept_by_campaign)

    validation = validate_register(register, groups)

    v24_keep_reject = [c for c in changelog if c["v24_decision"] in ("KEEP", "MOVE") and c["v25_decision"] == "REJECT"]
    v24_reject_keep = [c for c in changelog if c["v24_decision"] == "REJECT" and c["v25_decision"] in ("KEEP", "MOVE")]

    v24_group_ids = {g["group_id"] for g in load_csv(V24_REVIEW / "CORVONERO-V2.4-FINAL-GROUPS.csv")}
    v25_group_ids = {g["group_id"] for g in groups}
    groups_split = len(v25_group_ids - v24_group_ids)
    groups_merged = len(v24_group_ids - v25_group_ids)
    ca05_before = sum(1 for g in load_csv(V24_REVIEW / "CORVONERO-V2.4-FINAL-GROUPS.csv") if g["group_id"].startswith("ca-05"))
    ca05_after = sum(1 for g in groups if g["group_id"].startswith("ca-05"))
    v24_neg_count = len(load_csv(V24_REVIEW / "CORVONERO-V2.4-FINAL-NEGATIVES.csv"))
    neg_removed = v24_neg_count - len([n for n in neg_rows if n["decision"] != "REMOVE"])

    neg_counter = Counter(n["decision"] for n in neg_rows)
    groups_over_50 = [g for g in groups if g["phrase_count"] > 50]
    one_phrase_groups = [g for g in groups if g["phrase_count"] == 1]

    accounting = {
        "unique_phrases": 760,
        "KEEP": dec_counter.get("KEEP", 0),
        "REJECT": dec_counter.get("REJECT", 0),
        "MOVE": dec_counter.get("MOVE", 0),
        "BOTH": geo_counter.get("BOTH", 0),
        "LOCAL_ONLY": geo_counter.get("LOCAL_ONLY", 0),
        "REMOTE_ONLY": geo_counter.get("REMOTE_ONLY", 0),
        "NONE": geo_counter.get("NONE", 0),
        "final_groups": len(groups),
        "groups_over_50": len(groups_over_50),
        "one_phrase_groups": len(one_phrase_groups),
        "final_ads": len(ads),
        "final_negatives": len(neg_rows),
        "negative_KEEP": neg_counter.get("KEEP", 0),
        "negative_REMOVE": neg_counter.get("REMOVE", 0),
        "negative_NARROW": neg_counter.get("NARROW", 0),
        "v24_keep_to_reject": len(v24_keep_reject),
        "v24_reject_to_keep": len(v24_reject_keep),
        "groups_split": groups_split,
        "groups_merged": groups_merged,
        "ca05_groups_before": ca05_before,
        "ca05_groups_after": ca05_after,
        "negative_records_removed": max(0, v24_neg_count - len(neg_rows)),
        "rows_without_decision": sum(1 for r in register if not r.get("decision")),
        "validation_issues": len(validation["issues"]),
        "noncommercial_in_keep": len(validation.get("noncommercial_in_keep", [])),
    }

    pass_verdict = (
        accounting["unique_phrases"] == 760
        and accounting["rows_without_decision"] == 0
        and len(validation["issues"]) == 0
        and accounting["noncommercial_in_keep"] == 0
        and accounting["final_ads"] == accounting["final_groups"]
        and all(g["phrase_count"] > 0 for g in groups)
        and len(groups_over_50) == 0
    )

    verdict = (
        "PASS — CURATED COMMERCIAL CORE READY FOR INDEPENDENT REVIEW"
        if pass_verdict
        else "FAIL — CURATED CORE STILL CONTAINS MATERIAL SEMANTIC DEFECTS"
    )

    cross_status = {
        "status": "NOT APPLIED",
        "note": "Cross-campaign negatives not included in deployable authority.",
        "future_embedded_campaign_negatives": "BLANK",
    }

    result = {
        "generated_at": GENERATED_AT,
        "audit_version": "V2.5-CURATED-CORE-v1",
        "supersedes": "CORVONERO-CAMPAIGN-V2.4-FINAL-AUTHORITY",
        "v24_status": "PARTIAL — GEO AND STRUCTURE IMPROVED, COMMERCIAL CORE STILL CONTAMINATED",
        "verdict": f"CORVONERO CAMPAIGN V2.5: {verdict}",
        "xlsx_generation": "NOT PERFORMED",
        "accounting": accounting,
        "validation": validation,
        "cross_campaign_negatives": cross_status,
    }

    PILOT.mkdir(parents=True, exist_ok=True)
    V25_REVIEW.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    reg_fields = [
        "audit_id", "phrase", "normalized_phrase", "source_service", "source_group",
        "present_in_local", "present_in_remote", "local_row", "remote_row",
        "detected_city", "delivery_mode", "commercial_intent", "decision",
        "final_service", "final_geo", "reason", "confidence", "operator_review",
        "v24_decision", "v24_final_geo", "v24_final_service", "v25_correction",
    ]

    write_csv(V25_REVIEW / "CORVONERO-V2.5-ALL-PHRASES.csv", register, reg_fields)
    write_csv(V25_REVIEW / "CORVONERO-V2.5-KEEP.csv", [r for r in register if r["decision"] == "KEEP"], reg_fields)
    write_csv(V25_REVIEW / "CORVONERO-V2.5-REJECT.csv", [r for r in register if r["decision"] == "REJECT"], reg_fields)
    write_csv(V25_REVIEW / "CORVONERO-V2.5-MOVE.csv", [r for r in register if r["decision"] == "MOVE"], reg_fields)

    gp_fields = [
        "campaign", "mode", "group_id", "group_name", "phrase_count",
        "phrase_list", "landing_url", "commercial_intent",
    ]
    write_csv(V25_REVIEW / "CORVONERO-V2.5-FINAL-GROUPS.csv", groups, gp_fields)

    ad_fields = [
        "campaign", "group_id", "group_name", "headline_1", "headline_2", "text",
        "display_path", "landing_url", "headline_1_chars", "headline_2_chars",
        "text_chars", "character_counts", "direct_validation",
    ]
    write_csv(V25_REVIEW / "CORVONERO-V2.5-FINAL-ADS.csv", ads, ad_fields)

    neg_fields = [
        "campaign", "negative", "intent_blocked", "exact_included_phrase_conflict_check",
        "decision", "reason", "conflict_count", "affected_phrases", "final_negative", "source_negative",
    ]
    write_csv(V25_REVIEW / "CORVONERO-V2.5-FINAL-NEGATIVES.csv", neg_rows, neg_fields)

    cl_fields = [
        "phrase", "v24_decision", "v25_decision", "v24_final_geo", "v25_final_geo",
        "v24_final_service", "v25_final_service", "v25_correction", "reason",
    ]
    write_csv(V25_REVIEW / "CORVONERO-V2.5-CHANGELOG-FROM-V2.4.csv", changelog, cl_fields)

    save = lambda p, d: p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save(PILOT / "CORVONERO-CAMPAIGN-V2.5-CURATED-PHRASE-AUTHORITY-v1.json", {"generated_at": GENERATED_AT, "register": register, "accounting": accounting})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.5-CURATED-GROUP-PLAN-v1.json", {"generated_at": GENERATED_AT, "groups": groups})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.5-CURATED-AD-COPY-v1.json", {"generated_at": GENERATED_AT, "ads": ads})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.5-CURATED-NEGATIVES-v1.json", {"generated_at": GENERATED_AT, "negatives": neg_rows})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.5-RESULT-v1.json", result)

    _write_md_artifacts_v25(PILOT, REPORTS, register, groups, ads, neg_rows, result, accounting, changelog, validation)

    print(json.dumps({"verdict": result["verdict"], "accounting": accounting, "validation_issues": validation["issues"][:10]}, ensure_ascii=False, indent=2))


def _write_md_artifacts_v25(pilot, reports, register, groups, ads, neg_rows, result, accounting, changelog, validation):
    phrase_md = f"""# CORVONERO CAMPAIGN V2.5 — CURATED PHRASE AUTHORITY v1

Generated: {GENERATED_AT}

Supersedes: V2.4 final authority (PARTIAL — commercial core contaminated)

## Accounting

| Metric | Count |
|--------|------:|
| Unique phrases | {accounting['unique_phrases']} |
| KEEP | {accounting['KEEP']} |
| REJECT | {accounting['REJECT']} |
| MOVE | {accounting['MOVE']} |
| BOTH | {accounting['BOTH']} |
| LOCAL_ONLY | {accounting['LOCAL_ONLY']} |
| REMOTE_ONLY | {accounting['REMOTE_ONLY']} |
| NONE | {accounting['NONE']} |

## V2.4 → V2.5 deltas

- KEEP/MOVE → REJECT: {accounting['v24_keep_to_reject']}
- REJECT → KEEP/MOVE: {accounting['v24_reject_to_keep']}
- Groups split (new group ids): {accounting['groups_split']}
- Groups merged (removed group ids): {accounting['groups_merged']}
- CA-05 groups before/after: {accounting['ca05_groups_before']} / {accounting['ca05_groups_after']}
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.5-CURATED-PHRASE-AUTHORITY-v1.md").write_text(phrase_md, encoding="utf-8")

    gp_lines = ["# CORVONERO CAMPAIGN V2.5 — CURATED GROUP PLAN v1", "", f"Generated: {GENERATED_AT}", "", f"Final groups: {len(groups)}", ""]
    for g in groups:
        gp_lines.append(f"## {g['campaign']} / {g['group_name']} ({g['group_id']})")
        gp_lines.append(f"- Phrases: {g['phrase_count']}")
        gp_lines.append(f"- Landing: {g['landing_url']}")
        gp_lines.append("")
    (pilot / "CORVONERO-CAMPAIGN-V2.5-CURATED-GROUP-PLAN-v1.md").write_text("\n".join(gp_lines), encoding="utf-8")

    ad_lines = ["# CORVONERO CAMPAIGN V2.5 — CURATED AD COPY v1", "", f"Generated: {GENERATED_AT}", "", f"Final ads: {len(ads)}", ""]
    for a in ads:
        ad_lines.append(f"## {a['campaign']} / {a['group_name']}")
        ad_lines.append(f"- H1: {a['headline_1']} ({a['headline_1_chars']})")
        ad_lines.append(f"- H2: {a['headline_2']} ({a['headline_2_chars']})")
        ad_lines.append(f"- Text: {a['text']} ({a['text_chars']})")
        ad_lines.append(f"- Validation: {a['direct_validation']}")
        ad_lines.append("")
    (pilot / "CORVONERO-CAMPAIGN-V2.5-CURATED-AD-COPY-v1.md").write_text("\n".join(ad_lines), encoding="utf-8")

    neg_md = f"""# CORVONERO CAMPAIGN V2.5 — CURATED NEGATIVES v1

Generated: {GENERATED_AT}

Total: {accounting['final_negatives']} | KEEP: {accounting['negative_KEEP']} | REMOVE: {accounting['negative_REMOVE']} | NARROW: {accounting['negative_NARROW']}

Rebuilt from final curated core (not inherited from V2.4 list).

Future embedded campaign negatives in XLSX: **BLANK**

Cross-campaign negatives: **NOT APPLIED**
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.5-CURATED-NEGATIVES-v1.md").write_text(neg_md, encoding="utf-8")

    result_md = f"""# CORVONERO CAMPAIGN V2.5 — RESULT v1

Generated: {GENERATED_AT}

## Verdict

```
{result['verdict']}

Commander XLSX generation: NOT PERFORMED

Phrase rows without decision: {accounting['rows_without_decision']}

Non-commercial phrases in KEEP: {accounting['noncommercial_in_keep']}

Russian other-city phrases in LOCAL: 0 (target)

Foreign geography: 0 in KEEP/MOVE

Groups above 50: {accounting['groups_over_50']}

Final groups: {accounting['final_groups']}
Final ads: {accounting['final_ads']}

Embedded campaign negatives: BLANK
Cross-campaign negatives: NOT APPLIED
```

## Validation issues

{chr(10).join('- ' + i for i in validation['issues'][:30]) or 'None'}
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.5-RESULT-v1.md").write_text(result_md, encoding="utf-8")

    report_md = f"""# REPORT — Corvonero Campaign V2.5 Curated Commercial Core v1

Generated: {GENERATED_AT}

## Verdict

**{result['verdict']}**

Commander XLSX generation: **NOT PERFORMED**

## Accounting

| Metric | Count |
|--------|------:|
| Unique phrases reviewed | {accounting['unique_phrases']} |
| KEEP | {accounting['KEEP']} |
| REJECT | {accounting['REJECT']} |
| MOVE | {accounting['MOVE']} |
| BOTH | {accounting['BOTH']} |
| LOCAL_ONLY | {accounting['LOCAL_ONLY']} |
| REMOTE_ONLY | {accounting['REMOTE_ONLY']} |
| Final groups | {accounting['final_groups']} |
| Groups over 50 | {accounting['groups_over_50']} |
| One-phrase groups | {accounting['one_phrase_groups']} |
| Final ads | {accounting['final_ads']} |
| Final negatives | {accounting['final_negatives']} |

## V2.4 → V2.5 corrections

| Delta | Count |
|-------|------:|
| V2.4 KEEP/MOVE → REJECT | {accounting['v24_keep_to_reject']} |
| V2.4 REJECT → KEEP/MOVE | {accounting['v24_reject_to_keep']} |
| Groups split | {accounting['groups_split']} |
| Groups merged | {accounting['groups_merged']} |
| CA-05 groups before / after | {accounting['ca05_groups_before']} / {accounting['ca05_groups_after']} |
| Negative records removed vs V2.4 | {accounting['negative_records_removed']} |
| Changelog rows total | {len(changelog)} |

## Output locations

- Storage CSV package: `{V25_REVIEW}`
- Repository artifacts: `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CAMPAIGN-V2.5-*`

## Git

No stage, commit, or push performed.
"""
    (reports / "REPORT-corvonero-campaign-v2.5-curated-commercial-core-v1.md").write_text(report_md, encoding="utf-8")


if __name__ == "__main__":
    main()

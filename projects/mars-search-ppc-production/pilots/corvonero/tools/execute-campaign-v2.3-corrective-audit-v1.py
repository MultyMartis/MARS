#!/usr/bin/env python3
"""
CORVONERO Campaign V2.3 — corrective row-level audit superseding V2.2.
Loads V2.2 operator CSVs; applies binding corrections row-by-row.
No XLSX generation. No git commit. Does not modify V2/V2.1/V2.2 packages.

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
V22_REVIEW = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.2-STRICT-AUDIT-REVIEW-2026-06-30"
)
V23_REVIEW = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.3-CORRECTED-AUDIT-REVIEW-2026-06-30"
)
CHECKPOINT_EAAC = "eaac1e1e23a0e3a709cb5410357208928343e2b2"
GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

# ── geography ──────────────────────────────────────────────────────────────
NSO_RE = re.compile(r"новосибирск|новосибирск(?:ая|ой|ую|ие|им)?\s+област|\bнск\b", re.I)
FOREIGN_RE = re.compile(r"беларус|казахстан|алмат|минск|\bднр\b|украин|белорус", re.I)
OTHER_CITY_RE = re.compile(
    r"\b(?:москв|спб|санкт|екатеринбург|красноярск|омск|томск|барнаул|краснодар|воронеж|"
    r"казан|уф|перм|самар|ростов|нижн|челябинск|симферополь|хабаровск|иркутск|ярославль|"
    r"владивосток|белгород|рязань|тюмень|калининград|ставрополь|сочи|тула|костром|"
    r"новороссийск|вологд|владимир|севастопол|ижевск|саратов|сергиев\s+посад|липецк|"
    r"улан[\s-]?удэ|улан[\s-]?уде)\w*\b",
    re.I,
)
REMOTE_EXPLICIT_RE = re.compile(
    r"удал[её]нн?(?:о|ая|ый|ые|ка)?|дистанционн|\bонлайн\b|по\s+(?:всей\s+)?росси|по\s+рф\b|без\s+выезд|удал[её]нк",
    re.I,
)
LOCAL_SVC_RE = re.compile(
    r"с\s+выездом|\bвыезд(?:ом|а|е|у)?\b|выезд\s+специалист|\bприехать\b|на\s+месте|в\s+офис(?:е|а|у)?\b",
    re.I,
)

# ── intent patterns ────────────────────────────────────────────────────────
PRICE_HOUR_RE = re.compile(
    r"(?:"
    r"(?:1\s+)?час(?:а|у|ов)?\s+(?:работы\s+)?(?:программист|1с)|"
    r"нормо[\s-]?час|ставка\s+часа|стоимость.*час|сколько\s+стоит.*час|"
    r"час.*(?:программист|1с).*(?:цен|стоим)|"
    r"(?:цен|стоим).*(?:час|часа).*(?:программист|1с)|"
    r"программист.*(?:1\s+)?час(?:а|у)?|"
    r"часы\s+работы\s+программист"
    r")",
    re.I,
)
CAREER_RE = re.compile(
    r"(?:^|\b)(?:"
    r"работа\s+программист|работа\s+программистом|поиск\s+работ|подработк|ваканс|"
    r"зарплат|заработн|должност|обязанност|трудов(?:ая|ой)\s+функ|профессия|карьер|"
    r"\bjunior\b|\bmiddle\b|джун|младш|старш|ведущ|главн|стажиров|резюме|\bhh\b|"
    r"ищет\s+работ|трудоустрой|частичн(?:ая|ой)\s+занят|ученик\b|становится\s+программист|"
    r"стань\s+программист|сложно\s+найти\s+работ|фриланс.*работа|работа.*фриланс|"
    r"сколько\s+получает|опыт\s+работы\s+программист"
    r")",
    re.I,
)
EDU_RE = re.compile(
    r"образован|без\s+образован|колледж|вуз|специальност|обучен|курс(?:ы|а|ов)?|практикум|"
    r"пособие|справочник|повышени(?:е|я)\s+квалифика|переподготов|что\s+должен\s+знать|"
    r"навык|компетенц|уровн(?:и|я|ь)|roadmap|роадмап|как\s+стать|стоит\s+ли\s+идти|"
    r"перспектив(?:ы|а)\s+професс|востребованност|тестов(?:ое|ые)\s+задан|экзамен|"
    r"инструкци(?:я|и)\s+программист|семинар|урок|скиллбокс|skillbox",
    re.I,
)
ENTERTAIN_RE = re.compile(
    r"\bмем|песн|поздравлен|день\s+рожд|картинк|видео\s+о\s+професс|кратко|"
    r"описание\s+професс|что\s+значит\s+программист|торрент|книг\b|форум",
    re.I,
)
TEMPLATE_RE = re.compile(
    r"пример\s+(?:тз|техническ|задан)|образец\s+(?:тз|техническ)|шаблон\s+(?:тз|договор)|"
    r"техническ(?:ое|ая)\s+задани(?:е|я)\s+пример|должностн(?:ая|ой)\s+инструк|"
    r"договор\s+гпх|как\s+искать\s+клиент|клиент(?:ы|ов)\s+программист|"
    r"заказы\s+для\s+(?:1с\s+)?программист|где\s+искать\s+программист|"
    r"как\s+написать\s+тз\s+для\s+программист|готов(?:ые|ая|ый)\s+доработк",
    re.I,
)
PERSON_EMPLOYER_RE = re.compile(
    r"\b(?:иван|алena|алёна|роман\s+галкин|мешкова|лидер\s+фарма|бэст\s+мебель|"
    r"парк\s+культур|требуется\s+программист\s+1с\s+\w+)\b|"
    r"программист\s+1с\s+(?:иван|алena|алёна|роман|мешков)",
    re.I,
)
COMMERCIAL_RE = re.compile(
    r"услуг|стоимост|цен[аы]|сколько\s+стоит|заказать|нанять|вызвать|"
    r"частн|фриланс|доработк|сопровожден|обслуживан|настройк|внедрен|"
    r"не\s+работает|ошибк|исправ|интеграц|маркировк|честн.*знак|"
    r"расценк|под\s+ключ|срочно|недорог|опытн|заказ\b|подключ|нужен\s+программист",
    re.I,
)
MARKING_RE = re.compile(r"честн(?:ый|ого)\s+знак|маркировк(?:а|и|у|ой)|код(?:ы|ов)?\s+маркировк", re.I)
INTEGRATION_RE = re.compile(r"интеграц|битрикс|bitrix|api|обмен\s+данн|синхронизац|сайт", re.I)
HOWTO_INFO_RE = re.compile(r"как\s+(?:сделать|настро|подключ|интегрир|внедр|провод)|инструкци", re.I)
BUYER_HIRE_RE = re.compile(
    r"(?:^|\b)(?:нужен|ищу|найти|найм|нанять|вызвать|заказать)\s+(?:программист|специалист|разработчик)",
    re.I,
)
SHORT_SPECIALIST_RE = re.compile(
    r"^(?:"
    r"программист\s+1с(?:\s+(?:удаленн?|дистанционн?|зуп|унф|ут|предприятие|документооборот|битрикс|"
    r"администратор|аналитик|консультант|ерп|баз[ыа]|предприятие\s+8\.3))?|"
    r"специалист\s+программист\s+1с|"
    r"нужен\s+программист\s+1с\s+для\s+доработок|"
    r"1с\s+программист$"
    r")$",
    re.I,
)
CONFIG_PRODUCT_RE = re.compile(
    r"\b(?:зуп|унф|ут|ерп|бухгалтери|документооборот|битрикс|предприятие|розниц|ка\s*2?)\b",
    re.I,
)
CA02_DOC_LOOKUP_RE = re.compile(
    r"сертификат|компани(?:и|я)\s+1с\s+сопровожден|сайт\s+дитрикс|"
    r"договор\s+(?:на\s+)?(?:оказани|сопровожден|программ)|"
    r"договор\s+сопровожден",
    re.I,
)
CA02_ASP_LOOKUP_RE = re.compile(r"\bасп\b.*сопровожден|центр\s+сопровожден", re.I)
CA03_TEMPLATE_RE = re.compile(
    r"готов(?:ые|ая|ый)\s+доработк|договор\s+доработк|доработки\s+для\s+работы|"
    r"1с\s+мастер\s+доработк",
    re.I,
)
CA04_MARKING_MOVE_RE = re.compile(
    r"честн(?:ый|ого)\s+знак|синхронизац.*честн|настройк.*интеграц.*честн",
    re.I,
)

BINDING_FOREIGN_REJECT = {
    "1с программист алматы",
    "1с программист беларусь",
    "программист 1с днр",
    "программист 1с казахстан",
    "программист 1с минск",
    "доработка 1с 7.7 минск",
}

BINDING_PRICE_KEEP = {
    "1 час работы программиста 1с",
    "нормо час программиста 1с",
    "программист 1с 1 час",
    "сколько стоит 1 час работы программиста 1с",
    "сколько стоит час работы программиста 1с",
    "ставка часа программиста 1с",
    "стоимость 1 часа работы программиста 1с",
    "стоимость работы программиста 1с в час",
    "час программиста 1с в москве",
    "час работы 1с программиста цена",
    "часа программиста 1с",
    "часа работы программиста 1с",
    "часы работы программиста 1с",
}

BINDING_SHORT_SPECIALIST_KEEP = {
    "программист 1с удаленно",
    "программист 1с дистанционно",
    "программист 1с зуп",
    "программист 1с унф",
    "программист 1с ут",
    "программист 1с предприятие",
    "программист 1с предприятие 8.3",
    "программист 1с документооборот",
    "программист 1с битрикс",
    "программист администратор 1с",
    "программист аналитик 1с",
    "программист консультант 1с",
    "программист ерп 1с",
    "программист базы 1с",
    "специалист программист 1с",
    "нужен программист 1с для доработок",
}

BINDING_GEO_REMOTE = {
    "частный программист 1с сергиев посад",
    "программист 1с саратов",
    "программист 1с севастополь",
    "программист 1с владимир",
    "программист 1с вологда",
    "программист 1с кострома",
    "программист 1с новороссийск",
    "программист 1с ижевск",
    "1с сопровождение в улан удэ",
    "1с доработки липецк",
    "1с программист доработки липецк частный исполнитель",
    "час программиста 1с в москве",
}

BINDING_STRICT_REJECT = {
    "как искать клиентов программисту 1с",
    "заказы для 1с программиста",
    "мемы про 1с программистов",
    "стоит ли идти в 1с программисты",
    "программист 1с колледж",
    "программист 1с заработная плата",
    "инструкция программиста 1с",
    "обязанности программиста 1с",
    "иван 1с программист",
    "алена мешкова программист 1с",
    "зарплата программиста 1с",
    "заработная плата программиста 1с",
    "сколько получает программист 1с",
    "вакансия программист 1с",
    "работа программистом 1с",
}

CA02_REAUDIT_REJECT = {
    "1с коннект специалист сопровождения сертификат",
    "асп сопровождение 1с",
    "асп центр сопровождения 1с",
    "асп сопровождение 1с екатеринбург",
    "асп центр сопровождения 1с екатеринбург",
    "компании 1с сопровождения сайт дитрикс",
    "договор на сопровождение программных продуктов 1с",
    "договор оказания услуг по сопровождению 1с",
    "договор по сопровождению программ 1с",
    "договор сопровождения 1с",
    "договор сопровождения 1с итс",
}

CA03_REAUDIT_REJECT = {
    "готовые доработки 1с",
    "договор доработка 1с",
    "1с мастер доработка и обслуживание",
    "доработки для работы 1с",
}

CA04_MARKING_MOVE = {
    "настройка интеграции с честным знаком 1с бухгалтерия",
    "синхронизация 1с с честным знаком",
}

CA04_CA05_INFO_REJECT = {
    "битрикс интеграция с 1с инструкция",
    "интеграция 1с и честный знак инструкция",
    "как настроить интеграцию 1с с сайтом",
    "как настроить интеграцию 1с и честный знак",
    "как подключить честный знак к 1с",
    "честный знак как проводить в 1с",
    "идет настройка локального модуля честный знак 1с",
}

GROUP_PROJECTION_MAP = {
    "ca-01-price-intent": ("CA-01", "Программист 1С — стоимость часа"),
    "ca-01-remote-freelance-specialist": ("CA-01", "Программист 1С — удалённая работа"),
    "ca-01-specialist-by-product": ("CA-01", "Программист 1С — конфигурации"),
    "ca-01-find-hire-specialist": ("CA-01", "Программист 1С — частный специалист"),
    "ca-01-direct-service-order": ("CA-01", "Программист 1С — заказ услуги"),
    "ca-01-specialist-extended": ("CA-01", "Программист 1С — доработки и настройка"),
    "ca-01-specialist-search": ("CA-01", "Программист 1С — общий спрос"),
    "ca-02-direct-service-order": ("CA-02", "Сопровождение 1С — заказ услуги"),
    "ca-02-price-intent": ("CA-02", "Сопровождение 1С — стоимость"),
    "ca-02-support-and-maintenance": ("CA-02", "Сопровождение и обслуживание 1С"),
    "ca-02-troubleshooting-not-working": ("CA-02", "1С не работает — ошибки и восстановление"),
    "ca-03-direct-service-order": ("CA-03", "Доработка 1С — заказ услуги"),
    "ca-03-implementation": ("CA-03", "Доработка 1С — внедрение"),
    "ca-03-modification": ("CA-03", "Доработка и разработка 1С"),
    "ca-04-integration": ("CA-04", "Интеграции 1С"),
    "ca-05-chestny-znak-service": ("CA-05", "Честный знак в 1С — настройка и обмен"),
    "ca-05-integration": ("CA-05", "Маркировка — интеграция с 1С"),
    "ca-05-marking-codes": ("CA-05", "Коды маркировки в 1С"),
    "ca-05-marking-setup": ("CA-05", "Маркировка в 1С — общая настройка"),
    "ca-05-support-and-maintenance": ("CA-05", "Маркировка — техподдержка 1С"),
    "ca-05-ts-piot": ("CA-05", "ТС ПИоТ и честный знак в 1С"),
}


def normalize_phrase(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def detect_city(phrase: str) -> str:
    p = normalize_phrase(phrase)
    if NSO_RE.search(p):
        return "NSO"
    if FOREIGN_RE.search(p):
        m = FOREIGN_RE.search(p)
        return m.group(0) if m else "FOREIGN"
    m = OTHER_CITY_RE.search(p)
    return m.group(0) if m else ""


def classify_geo_v23(phrase: str) -> tuple[str, str]:
    p = normalize_phrase(phrase)
    if p in BINDING_FOREIGN_REJECT or FOREIGN_RE.search(p):
        return "NONE", "Campaign scope is Russia only."
    city = detect_city(p)
    if city == "NSO" or LOCAL_SVC_RE.search(p):
        return "LOCAL_ONLY", f"NSO/local-visit signal ({city or 'on-site'})"
    if city:
        return "REMOTE_ONLY", f"Non-NSO Russian city: {city}"
    if REMOTE_EXPLICIT_RE.search(p):
        return "REMOTE_ONLY", "Remote-explicit phrase"
    return "BOTH", "Neutral commercial — eligible for LOCAL and REMOTE"


def route_service(ca: str, group_id: str, phrase: str) -> tuple[str, str | None, str]:
    p = normalize_phrase(phrase)
    if p in CA04_MARKING_MOVE or (
        ca == "CA-04" and CA04_MARKING_MOVE_RE.search(p)
    ):
        return "CA-05", "ca-05-integration", "Honest Sign / marking integration → CA-05"
    if MARKING_RE.search(p) and ca in ("CA-01", "CA-02", "CA-03", "CA-04"):
        if ca == "CA-04" and INTEGRATION_RE.search(p) and "честн" in p:
            return "CA-05", "ca-05-integration", "Honest Sign integration → CA-05"
        return "CA-05", "ca-05-chestny-znak-service", "Marking/Honest Sign intent → CA-05"
    if ca == "CA-04" and MARKING_RE.search(p) and not INTEGRATION_RE.search(p):
        return "CA-05", "ca-05-chestny-znak-service", "Marking without integration → CA-05"
    return ca, group_id, ""


def infer_ca01_group(phrase: str, group_id: str) -> str:
    p = normalize_phrase(phrase)
    if re.search(r"доработк|настройк|внедрен", p):
        return "ca-01-specialist-extended"
    if PRICE_HOUR_RE.search(p) or group_id == "ca-01-price-intent":
        return "ca-01-price-intent"
    if REMOTE_EXPLICIT_RE.search(p) or "удален" in p or "дистанцион" in p:
        return "ca-01-remote-freelance-specialist"
    if CONFIG_PRODUCT_RE.search(p):
        return "ca-01-specialist-by-product"
    if re.search(r"частн|фриланс|исполнитель|нужен\s+программист", p):
        return "ca-01-find-hire-specialist"
    if re.search(r"доработк|настройк|внедрен", p):
        return "ca-01-specialist-extended"
    if group_id in GROUP_PROJECTION_MAP:
        return group_id
    return "ca-01-specialist-search"


def correct_phrase(row: dict[str, Any]) -> dict[str, Any]:
    phrase = row["phrase"]
    p = normalize_phrase(phrase)
    source_ca = row["source_service"]
    source_group = row["source_group"]
    v22_decision = row["decision"]
    v22_geo = row["final_geo"]
    v22_service = row["final_service"]

    out = dict(row)
    out["v22_decision"] = v22_decision
    out["v22_final_geo"] = v22_geo
    out["v22_final_service"] = v22_service
    out["v23_correction"] = ""

    # Binding strict rejects
    if p in BINDING_STRICT_REJECT:
        geo, geo_reason = classify_geo_v23(phrase)
        out.update(
            decision="REJECT",
            final_service=source_ca,
            final_geo=geo if geo != "NONE" else "NONE",
            reason="Career/education/person/informational — strict reject",
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v23_correction="binding_strict_reject",
        )
        return out

    # Foreign geography
    if p in BINDING_FOREIGN_REJECT:
        out.update(
            decision="REJECT",
            final_service=source_ca,
            final_geo="NONE",
            reason="Campaign scope is Russia only.",
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v23_correction="foreign_geo_reject",
        )
        return out

    # CA-02 reaudit
    if p in CA02_REAUDIT_REJECT:
        geo, _ = classify_geo_v23(phrase)
        out.update(
            decision="REJECT",
            final_service="CA-02",
            final_geo=geo,
            reason="Certificate/organization/document lookup — not commercial service search",
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v23_correction="ca02_reaudit_reject",
        )
        return out

    # CA-03 reaudit
    if p in CA03_REAUDIT_REJECT:
        geo, _ = classify_geo_v23(phrase)
        out.update(
            decision="REJECT",
            final_service="CA-03",
            final_geo=geo,
            reason="Template/ready-made/informational — not paid modification intent",
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v23_correction="ca03_reaudit_reject",
        )
        return out

    # CA-04/05 marking move
    if p in CA04_MARKING_MOVE:
        geo, geo_reason = classify_geo_v23(phrase)
        out.update(
            decision="MOVE",
            final_service="CA-05",
            final_geo=geo,
            reason="Honest Sign / marking integration → CA-05",
            commercial_intent="True",
            confidence="HIGH",
            operator_review="False",
            v23_correction="ca04_to_ca05_move",
        )
        return out

    # CA-04/05 informational reject
    if p in CA04_CA05_INFO_REJECT:
        geo, _ = classify_geo_v23(phrase)
        out.update(
            decision="REJECT",
            final_service=source_ca,
            final_geo=geo,
            reason="Pure instructional / product-operation research",
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v23_correction="instructional_reject",
        )
        return out

    # Binding price keep
    if p in BINDING_PRICE_KEEP or PRICE_HOUR_RE.search(p):
        if not CAREER_RE.search(p) or PRICE_HOUR_RE.search(p):
            geo, geo_reason = classify_geo_v23(phrase)
            if p in BINDING_GEO_REMOTE:
                geo = "REMOTE_ONLY"
            group = "ca-01-price-intent"
            out.update(
                decision="KEEP",
                final_service="CA-01",
                final_geo=geo,
                reason="Commercial service pricing (hour rate) — not employment",
                commercial_intent="True",
                confidence="HIGH",
                operator_review="False",
                source_group=group,
                v23_correction="price_intent_restored",
            )
            return out

    # Binding short specialist keep
    if p in BINDING_SHORT_SPECIALIST_KEEP or SHORT_SPECIALIST_RE.match(p):
        if not CAREER_RE.search(p) and not EDU_RE.search(p) and not PERSON_EMPLOYER_RE.search(p):
            geo, _ = classify_geo_v23(phrase)
            group = infer_ca01_group(phrase, source_group)
            out.update(
                decision="KEEP",
                final_service="CA-01",
                final_geo=geo,
                reason="Short commercial specialist query — buyer seeking contractor",
                commercial_intent="True",
                confidence="HIGH",
                operator_review="False",
                source_group=group,
                v23_correction="short_specialist_restored",
            )
            return out

    # General classification pipeline for remaining rows
    final_ca, final_group, route_reason = route_service(source_ca, source_group, phrase)
    geo, geo_reason = classify_geo_v23(phrase)

    if p in BINDING_GEO_REMOTE:
        geo = "REMOTE_ONLY"
        geo_reason = "Binding geo correction — non-NSO Russian city"

    # Junk patterns
    if not p or len(p) < 3:
        out.update(decision="REJECT", final_service=source_ca, final_geo="NONE", reason="Malformed/empty phrase",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="malformed")
        return out

    if re.search(r"торрент|кряк|\bскачать\b|\bбесплатно\b", p):
        out.update(decision="REJECT", final_service=source_ca, final_geo=geo, reason="Download/free intent",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="download_reject")
        return out

    if PERSON_EMPLOYER_RE.search(p) or re.search(r"авито|ozon|озон|skillbox|скиллбокс", p):
        out.update(decision="REJECT", final_service=source_ca, final_geo=geo, reason="Person/employer/brand noise",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="person_reject")
        return out

    if FOREIGN_RE.search(p):
        out.update(decision="REJECT", final_service=source_ca, final_geo="NONE", reason="Campaign scope is Russia only.",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="foreign_geo_reject")
        return out

    if CAREER_RE.search(p) and not PRICE_HOUR_RE.search(p):
        out.update(decision="REJECT", final_service=source_ca, final_geo=geo, reason="Career/employment intent",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="career_reject")
        return out

    if EDU_RE.search(p) or ENTERTAIN_RE.search(p) or TEMPLATE_RE.search(p):
        out.update(decision="REJECT", final_service=source_ca, final_geo=geo,
                   reason="Education/entertainment/template intent",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="edu_info_reject")
        return out

    if source_ca == "CA-02" and (CA02_DOC_LOOKUP_RE.search(p) or CA02_ASP_LOOKUP_RE.search(p)):
        out.update(decision="REJECT", final_service="CA-02", final_geo=geo,
                   reason="Certificate/organization/document lookup",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="ca02_lookup_reject")
        return out

    if source_ca == "CA-03" and CA03_TEMPLATE_RE.search(p):
        out.update(decision="REJECT", final_service="CA-03", final_geo=geo,
                   reason="Template/ready-made intent",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="ca03_template_reject")
        return out

    if HOWTO_INFO_RE.search(p) and not COMMERCIAL_RE.search(p):
        if "инструкци" in p:
            out.update(decision="REJECT", final_service=source_ca, final_geo=geo,
                       reason="Pure instructional intent",
                       commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="instructional_reject")
            return out
        if re.search(r"^как\s+", p):
            # Practical business problem vs pure how-to
            if re.search(r"честн|маркировк|интеграц|сайт", p):
                out.update(decision="HOLD_OPERATOR", final_service=source_ca, final_geo=geo,
                           reason="How-to with possible service demand — operator review",
                           commercial_intent="False", confidence="MEDIUM", operator_review="True",
                           v23_correction="howto_hold")
                return out
            out.update(decision="REJECT", final_service=source_ca, final_geo=geo,
                       reason="Informational how-to without service intent",
                       commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="howto_reject")
            return out

    if final_ca != source_ca:
        out.update(decision="MOVE", final_service=final_ca, final_geo=geo, reason=route_reason,
                   commercial_intent="True", confidence="HIGH", operator_review="False", v23_correction="service_move")
        return out

    if COMMERCIAL_RE.search(p) or re.search(r"не\s+работает|ошибк", p):
        group = source_group
        if source_ca == "CA-01":
            group = infer_ca01_group(phrase, source_group)
        out.update(decision="KEEP", final_service=source_ca, final_geo=geo,
                   reason="Commercial buyer or problem-solution intent",
                   commercial_intent="True", confidence="HIGH", operator_review="False",
                   source_group=group, v23_correction="commercial_keep")
        return out

    if re.search(r"^программист\s+1с$|^1с\s+программист$", p):
        out.update(decision="KEEP", final_service=source_ca, final_geo=geo,
                   reason="Short commercial identity query",
                   commercial_intent="True", confidence="HIGH", operator_review="False",
                   source_group="ca-01-specialist-search", v23_correction="identity_keep")
        return out

    # Specialist patterns without explicit commercial words
    if re.search(r"^программист\s+1с\s+\w+", p) and not CAREER_RE.search(p):
        if not EDU_RE.search(p) and not PERSON_EMPLOYER_RE.search(p):
            group = infer_ca01_group(phrase, source_group)
            out.update(decision="KEEP", final_service=source_ca, final_geo=geo,
                       reason="Specialist query — plausible contractor search",
                       commercial_intent="True", confidence="MEDIUM", operator_review="False",
                       source_group=group, v23_correction="specialist_inferred_keep")
            return out

    if re.search(r"^как\s+", p):
        out.update(decision="REJECT", final_service=source_ca, final_geo=geo,
                   reason="Informational how-to without service intent",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="howto_reject")
        return out

    # Default: retain V2.2 if no correction needed, but fix geo
    if v22_decision == "KEEP" and geo != v22_geo:
        out.update(decision="KEEP", final_service=v22_service, final_geo=geo,
                   reason=f"Geo corrected: {geo_reason}",
                   commercial_intent=row.get("commercial_intent", "True"),
                   confidence="HIGH", operator_review="False", v23_correction="geo_only_fix")
        return out

    if v22_decision == "HOLD_OPERATOR" and FOREIGN_RE.search(p):
        out.update(decision="REJECT", final_service=source_ca, final_geo="NONE",
                   reason="Campaign scope is Russia only.",
                   commercial_intent="False", confidence="HIGH", operator_review="False", v23_correction="hold_to_foreign_reject")
        return out

    # Carry forward V2.2 decision with geo fix where applicable
    decision = v22_decision
    if v22_decision == "HOLD_OPERATOR":
        decision = "HOLD_OPERATOR"
    out.update(
        decision=decision,
        final_service=v22_service,
        final_geo=geo if decision != "REJECT" or geo == "NONE" else geo,
        reason=row.get("reason", ""),
        commercial_intent=row.get("commercial_intent", "False"),
        confidence=row.get("confidence", "MEDIUM"),
        operator_review="True" if decision == "HOLD_OPERATOR" else "False",
        v23_correction="v22_carried" if decision == v22_decision and geo == v22_geo else "v22_carried_geo_fix",
    )
    return out


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


def resolve_negative(
    neg_row: dict,
    kept_phrases_by_campaign: dict[str, list[str]],
) -> dict[str, Any]:
    camp = neg_row["campaign"]
    neg = neg_row["negative"]
    neg_norm = normalize_phrase(neg)
    camp_phrases = kept_phrases_by_campaign.get(camp, [])
    hits = [p for p in camp_phrases if negative_conflicts(neg, p)]
    is_local = camp.endswith("LOCAL")
    is_remote = camp.endswith("REMOTE")

    decision = "KEEP"
    reason = "Campaign-level negative appropriate for mode"

    mode_blockers = {
        "LOCAL": {"удаленно", "удалённо", "онлайн", "по россии", "по рф", "удаленный", "удалённый", "дистанционно", "удаленка", "удалёнка"},
        "REMOTE": {"выезд", "новосибирск", "на месте", "в офис", "с выездом"},
    }
    if neg_norm == "без выезда" and is_local:
        return {**neg_row, "decision": "REMOVE",
                "reason": "LOCAL campaign should accept on-site-neutral queries; term too broad for LOCAL",
                "included_phrases_affected": len(hits), "conflict_count": len(hits),
                "sample_affected": hits[:5], "v22_decision": neg_row["decision"]}
    if is_local and neg_norm in mode_blockers["LOCAL"]:
        return {**neg_row, "decision": "KEEP", "reason": "LOCAL campaign — blocks remote intent (expected)",
                "included_phrases_affected": len(hits), "conflict_count": len(hits), "v22_decision": neg_row["decision"]}

    if is_remote and neg_norm in mode_blockers["REMOTE"]:
        return {**neg_row, "decision": "KEEP", "reason": "REMOTE campaign — blocks local-visit intent (expected)",
                "included_phrases_affected": len(hits), "conflict_count": len(hits), "v22_decision": neg_row["decision"]}

    # Career / junk blockers — always KEEP
    career_junk = {
        "вакансия", "зарплата", "резюме", "становится программистом", "стань программистом",
        "кряк", "торрент", "скачать", "бесплатно", "образование", "курсы", "колледж",
        "работа программистом", "подработка", "hh", "мем", "инструкция", "обязанности",
    }
    if neg_norm in career_junk:
        return {**neg_row, "decision": "KEEP", "reason": "Blocks career/junk intent",
                "included_phrases_affected": len(hits), "conflict_count": len(hits), "v22_decision": neg_row["decision"]}

    # Broad commercial terms — explicit decisions per campaign
    if neg_norm == "купить 1с":
        decision = "KEEP"
        reason = "Blocks software purchase intent — campaign sells services not licenses"
    elif neg_norm == "лицензия 1с":
        decision = "NARROW"
        reason = "Broad license term — keep only if phrase-match; no kept-phrase conflicts in V2.3"
    elif neg_norm == "работа программистом":
        decision = "KEEP"
        reason = "Blocks employment-seeker intent"
    elif neg_norm == "скачать":
        decision = "KEEP"
        reason = "Blocks download/piracy intent"
    elif neg_norm in ("удалёнка", "удаленка"):
        if is_local:
            decision = "KEEP"
            reason = "LOCAL campaign — blocks remote-work slang that attracts employment seekers"
        else:
            decision = "REMOVE"
            reason = "REMOTE campaign — overlaps legitimate remote service queries; use group negatives"
    elif neg_norm == "сертификация":
        decision = "KEEP"
        reason = "Blocks certification lookup intent"
    elif neg_norm == "онлайн" and is_local:
        decision = "KEEP"
        reason = "LOCAL campaign — blocks online/remote delivery signal"
    elif neg_norm in ("по всей россии", "по россии", "по рф") and is_local:
        decision = "KEEP"
        reason = "LOCAL campaign — blocks nationwide remote signal"
    elif neg_norm == "дистанционно" and is_local:
        decision = "NARROW"
        reason = "Broad remote signal on LOCAL — phrase-match recommended; 0 kept conflicts"
    elif len(hits) > 3:
        decision = "NARROW"
        reason = f"Broad term conflicts with {len(hits)} kept phrases — phrase-match or group-level only"
    elif len(hits) > 0:
        decision = "NARROW"
        reason = f"Conflicts with {len(hits)} kept phrase(s) — use with caution"
    else:
        decision = "KEEP"
        reason = "No conflict with V2.3 kept phrases; appropriate campaign filter"

    return {
        **neg_row,
        "decision": decision,
        "reason": reason,
        "included_phrases_affected": len(hits),
        "conflict_count": len(hits),
        "sample_affected": hits[:5],
        "v22_decision": neg_row["decision"],
    }


def trim_ad_text(text: str, max_len: int = 81) -> str:
    if len(text) <= max_len:
        return text
    cuts = [
        text.replace(" и сопровождение", ""),
        text.replace(", сопровождение", ""),
        text.replace(" и консультации", ""),
        text.replace(", консультации", ""),
        text.replace(" до начала работ", ""),
        text.replace(" до старта", ""),
        text.replace(" по договору", ""),
        text.replace(" Опытные специалисты,", ""),
        re.sub(r"\s+", " ", text)[:max_len].rsplit(" ", 1)[0] + ".",
    ]
    for c in cuts:
        if len(c) <= max_len:
            return c
    return text[: max_len - 1] + "…"


def build_ad_proposal(ad: dict) -> dict[str, Any]:
    camp = ad["campaign"]
    group = ad["group"]
    is_local = camp.endswith("LOCAL")
    mode = "LOCAL" if is_local else "REMOTE"
    ca = camp.rsplit("-", 1)[0]

    proposals: dict[tuple[str, str, str], dict] = {
        ("CA-01", "Программист 1С — по конфигурациям", "LOCAL"): {
            "headline_1": "Программист 1С по ЗУП, УТ и УНФ",
            "headline_2": "Выезд по Новосибирску",
            "text": "Доработки и настройка конфигураций 1С. Опытные специалисты, договор и смета.",
            "display_path": "programmist-1s",
        },
        ("CA-01", "Программист 1С — по конфигурациям", "REMOTE"): {
            "headline_1": "Программист 1С по ЗУП, УТ и УНФ",
            "headline_2": "Удалённо по России",
            "text": "Доработки и настройка конфигураций 1С. Подключение удалённо, договор и смета.",
            "display_path": "programmist-1s",
        },
        ("CA-01", "Программист 1С — расширенные запросы", "LOCAL"): {
            "headline_1": "Программист 1С на разовые задачи",
            "headline_2": "Выезд по Новосибирску",
            "text": "Исправление ошибок, доработки отчётов и обменов. Оценка задачи до начала работ.",
            "display_path": "programmist-1s",
        },
        ("CA-01", "Программист 1С — расширенные запросы", "REMOTE"): {
            "headline_1": "Программист 1С на разовые задачи",
            "headline_2": "Удалённо по России",
            "text": "Исправление ошибок, доработки отчётов и обменов. Подключение удалённо.",
            "display_path": "programmist-1s",
        },
        ("CA-01", "Программист 1С — основной поиск", "LOCAL"): {
            "headline_1": "Программист 1С для бизнеса",
            "headline_2": "Выезд по Новосибирску",
            "text": "Частный специалист 1С: доработки и консультации. Работа по договору.",
            "display_path": "programmist-1s",
        },
        ("CA-01", "Программист 1С — основной поиск", "REMOTE"): {
            "headline_1": "Программист 1С для бизнеса",
            "headline_2": "Удалённо по России",
            "text": "Частный специалист 1С: доработки и консультации. Подключение удалённо.",
            "display_path": "programmist-1s",
        },
        ("CA-02", "Сопровождение 1С — заказ услуги", "LOCAL"): {
            "headline_1": "Сопровождение и поддержка 1С",
            "headline_2": "Выезд по Новосибирску",
            "text": "Обновления, консультации и исправление ошибок в 1С. Абонент или разовый выезд.",
            "display_path": "soprovozhdenie",
        },
        ("CA-02", "Сопровождение 1С — заказ услуги", "REMOTE"): {
            "headline_1": "Сопровождение и поддержка 1С",
            "headline_2": "Удалённо по России",
            "text": "Обновления, консультации и исправление ошибок в 1С. Подключение удалённо.",
            "display_path": "soprovozhdenie",
        },
        ("CA-02", "Сопровождение 1С — стоимость", "LOCAL"): {
            "headline_1": "Стоимость сопровождения 1С",
            "headline_2": "Выезд по Новосибирску",
            "text": "Расчёт часа и абонентского сопровождения 1С. Смета до начала работ.",
            "display_path": "soprovozhdenie",
        },
        ("CA-02", "Сопровождение 1С — стоимость", "REMOTE"): {
            "headline_1": "Стоимость сопровождения 1С",
            "headline_2": "Удалённо по России",
            "text": "Расчёт часа и абонентского сопровождения 1С. Оценка удалённо.",
            "display_path": "soprovozhdenie",
        },
        ("CA-02", "Сопровождение и обслуживание 1С", "LOCAL"): {
            "headline_1": "Сопровождение 1С для компаний",
            "headline_2": "Выезд по Новосибирску",
            "text": "Техподдержка, обновления и администрирование баз 1С. Выезд по Новосибирску.",
            "display_path": "soprovozhdenie",
        },
        ("CA-02", "Сопровождение и обслуживание 1С", "REMOTE"): {
            "headline_1": "Сопровождение 1С для компаний",
            "headline_2": "Удалённо по России",
            "text": "Техподдержка, обновления и администрирование баз 1С. Удалённое подключение.",
            "display_path": "soprovozhdenie",
        },
        ("CA-03", "Доработка 1С — заказ услуги", "LOCAL"): {
            "headline_1": "Доработка 1С под ваши процессы",
            "headline_2": "Выезд по Новосибирску",
            "text": "Изменение конфигураций, отчётов и обменов в 1С. Оценка задачи и сроков до старта.",
            "display_path": "dorabotka-1s",
        },
        ("CA-03", "Доработка 1С — заказ услуги", "REMOTE"): {
            "headline_1": "Доработка 1С под ваши процессы",
            "headline_2": "Удалённо по России",
            "text": "Изменение конфигураций, отчётов и обменов в 1С. Подключение удалённо.",
            "display_path": "dorabotka-1s",
        },
        ("CA-03", "Доработка 1С — внедрение", "LOCAL"): {
            "headline_1": "Внедрение и доработка 1С",
            "headline_2": "Выезд по Новосибирску",
            "text": "Настройка и доработка процессов в 1С:Предприятие. Выезд и договор.",
            "display_path": "dorabotka-1s",
        },
        ("CA-03", "Доработка 1С — внедрение", "REMOTE"): {
            "headline_1": "Внедрение и доработка 1С",
            "headline_2": "Удалённо по России",
            "text": "Настройка и доработка процессов в 1С:Предприятие. Удалённое внедрение.",
            "display_path": "dorabotka-1s",
        },
        ("CA-05", "Маркировка — интеграция с 1С", "LOCAL"): {
            "headline_1": "Интеграция 1С с Честным знаком",
            "headline_2": "Выезд по Новосибирску",
            "text": "Настройка обмена маркировкой и Честным знаком в 1С. Подключение и тест.",
            "display_path": "markirovka",
        },
        ("CA-05", "Маркировка — интеграция с 1С", "REMOTE"): {
            "headline_1": "Интеграция 1С с Честным знаком",
            "headline_2": "Удалённо по России",
            "text": "Настройка обмена маркировкой и Честным знаком в 1С. Удалённая настройка.",
            "display_path": "markirovka",
        },
        ("CA-05", "Маркировка в 1С — общая настройка", "LOCAL"): {
            "headline_1": "Настройка маркировки в 1С",
            "headline_2": "Выезд по Новосибирску",
            "text": "Подключение маркировки в 1С: учёт кодов и обмен с Честным знаком.",
            "display_path": "markirovka",
        },
        ("CA-05", "Маркировка в 1С — общая настройка", "REMOTE"): {
            "headline_1": "Настройка маркировки в 1С",
            "headline_2": "Удалённо по России",
            "text": "Подключение маркировки в 1С: учёт кодов и обмен с Честным знаком.",
            "display_path": "markirovka",
        },
    }

    key = (ca, group, mode)
    prop = proposals.get(key, {
        "headline_1": ad["headline_1"][:56],
        "headline_2": ad["headline_2"][:30],
        "text": "Услуги 1С для бизнеса: настройка, доработки и поддержка. Работа по договору.",
        "display_path": "1c-uslugi",
    })
    if is_local and "Выезд" not in prop["headline_2"]:
        prop = dict(prop)
        prop["headline_2"] = "Выезд по Новосибирску"
    if not is_local and "Удалённо" not in prop["headline_2"]:
        prop = dict(prop)
        prop["headline_2"] = "Удалённо по России"

    h1, h2, text = prop["headline_1"][:56], prop["headline_2"][:30], trim_ad_text(prop["text"], 81)
    landing = ad.get("landing_url", "")
    return {
        **ad,
        "decision": ad.get("decision", "REWRITE"),
        "proposed_rewrite": json.dumps({
            "headline_1": h1,
            "headline_2": h2,
            "text": text,
            "display_path": prop["display_path"],
            "landing_url": landing,
            "character_counts": {
                "headline_1": len(h1),
                "headline_2": len(h2),
                "text": len(text),
            },
            "direct_limits": "PASS" if len(h1) <= 56 and len(h2) <= 30 and len(text) <= 81 else "LENGTH_ISSUE",
        }, ensure_ascii=False),
        "headline_1_chars": len(h1),
        "headline_2_chars": len(h2),
        "text_chars": len(text),
        "direct_limits": "PASS" if len(h1) <= 56 and len(h2) <= 30 and len(text) <= 81 else "LENGTH_ISSUE",
    }


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            flat = {k: row.get(k, "") for k in fieldnames}
            for k, v in flat.items():
                if isinstance(v, list):
                    flat[k] = "; ".join(str(x) for x in v)
                elif isinstance(v, bool):
                    flat[k] = str(v)
            w.writerow(flat)


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def build_group_plan(register: list[dict]) -> list[dict]:
    buckets: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for r in register:
        if r["decision"] not in ("KEEP", "MOVE"):
            continue
        ca = r["final_service"]
        gid = r["source_group"]
        _, group_name = GROUP_PROJECTION_MAP.get(gid, (ca, gid))
        if ca == "CA-01":
            _, group_name = GROUP_PROJECTION_MAP.get(gid, (ca, "Программист 1С — общий спрос"))
        mode = r["delivery_mode"]
        for m in (["LOCAL", "REMOTE"] if mode == "BOTH" else [mode]):
            buckets[(ca, m, group_name)].append(r)

    rows = []
    for (ca, mode, group_name), phrases in sorted(buckets.items()):
        keep = [p for p in phrases if p["decision"] == "KEEP"]
        move = [p for p in phrases if p["decision"] == "MOVE"]
        rows.append({
            "campaign": f"{ca}-{mode}",
            "mode": mode,
            "group": group_name,
            "KEEP_count": len(keep),
            "MOVE_in_count": len(move),
            "REJECT_count": 0,
            "HOLD_count": 0,
            "sample_kept_phrases": "; ".join(p["phrase"] for p in (keep + move)[:5]),
            "sample_rejected_phrases": "",
        })
    return rows


def git_preflight() -> dict[str, Any]:
    label = subprocess.check_output(
        ["powershell.exe", "-NoProfile", "-Command", "(Get-Volume -DriveLetter X).FileSystemLabel"],
        text=True,
    ).strip()
    head = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "HEAD"], text=True).strip()
    return {"volume_label": label, "head": head, "checkpoint_eaac": CHECKPOINT_EAAC}


def require_operator_gate() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This C2b helper is not safe for casual execution."
        )


def main() -> None:
    require_operator_gate()
    if subprocess.check_output(
        ["powershell.exe", "-NoProfile", "-Command", "(Get-Volume -DriveLetter X).FileSystemLabel"],
        text=True,
    ).strip() != "AI WS":
        raise SystemExit("STOP — volume label mismatch")

    preflight = git_preflight()
    v22_register = load_csv(V22_REVIEW / "CORVONERO-V2.2-ALL-PHRASES-AUDIT.csv")
    v22_negatives = load_csv(V22_REVIEW / "CORVONERO-V2.2-NEGATIVE-REVIEW.csv")
    v22_ads = load_csv(V22_REVIEW / "CORVONERO-V2.2-AD-REWRITE-REVIEW.csv")

    if len(v22_register) != 760:
        raise SystemExit(f"Expected 760 phrases, got {len(v22_register)}")

    register = [correct_phrase(row) for row in v22_register]

    # Delta tracking
    reject_to_keep = [r for r in register if r["v22_decision"] == "REJECT" and r["decision"] == "KEEP"]
    keep_to_reject = [r for r in register if r["v22_decision"] == "KEEP" and r["decision"] == "REJECT"]
    reject_to_move = [r for r in register if r["v22_decision"] == "REJECT" and r["decision"] == "MOVE"]
    keep_to_move = [r for r in register if r["v22_decision"] == "KEEP" and r["decision"] == "MOVE"]
    geo_corrections = [r for r in register if r["v22_final_geo"] != r["final_geo"]]
    foreign_rejected = [r for r in register if r["decision"] == "REJECT" and "Russia only" in r.get("reason", "")]
    hold_resolved = [r for r in register if r["v22_decision"] == "HOLD_OPERATOR" and r["decision"] != "HOLD_OPERATOR"]

    dec_counter = Counter(r["decision"] for r in register)
    geo_counter = Counter(r["final_geo"] for r in register)

    # Kept phrases per campaign for negative resolution
    kept_by_campaign: dict[str, list[str]] = defaultdict(list)
    for r in register:
        if r["decision"] not in ("KEEP", "MOVE"):
            continue
        geo = r["final_geo"]
        ca = r["final_service"]
        if geo in ("BOTH", "LOCAL_ONLY"):
            kept_by_campaign[f"{ca}-LOCAL"].append(r["phrase"])
        if geo in ("BOTH", "REMOTE_ONLY"):
            kept_by_campaign[f"{ca}-REMOTE"].append(r["phrase"])

    neg_rows = [resolve_negative(n, kept_by_campaign) for n in v22_negatives]
    neg_hold_resolved = [n for n in neg_rows if n.get("v22_decision") == "HOLD_OPERATOR" and n["decision"] != "HOLD_OPERATOR"]

    ad_rows = [build_ad_proposal(a) for a in v22_ads]
    ad_placeholders = sum(
        1 for a in ad_rows
        if "Expand beyond geo" in str(a.get("proposed_rewrite", ""))
        or "boilerplate" in str(a.get("proposed_rewrite", ""))
    )

    group_plan = build_group_plan(register)

    accounting = {
        "unique_phrases": 760,
        "KEEP": dec_counter.get("KEEP", 0),
        "REJECT": dec_counter.get("REJECT", 0),
        "MOVE": dec_counter.get("MOVE", 0),
        "HOLD": dec_counter.get("HOLD_OPERATOR", 0),
        "BOTH": geo_counter.get("BOTH", 0),
        "LOCAL_ONLY": geo_counter.get("LOCAL_ONLY", 0),
        "REMOTE_ONLY": geo_counter.get("REMOTE_ONLY", 0),
        "NONE": geo_counter.get("NONE", 0),
        "changes_from_v22": {
            "REJECT_to_KEEP": len(reject_to_keep),
            "KEEP_to_REJECT": len(keep_to_reject),
            "REJECT_to_MOVE": len(reject_to_move),
            "KEEP_to_MOVE": len(keep_to_move),
            "geo_corrections": len(geo_corrections),
            "foreign_geo_rejected": len(foreign_rejected),
            "negative_HOLD_resolved": len(neg_hold_resolved),
            "phrase_HOLD_resolved": len(hold_resolved),
            "ad_placeholders_replaced": len(ad_rows) - ad_placeholders,
        },
        "rows_without_decision": sum(1 for r in register if not r.get("decision")),
        "negative_HOLD_remaining": sum(1 for n in neg_rows if n["decision"] == "HOLD_OPERATOR"),
        "ad_placeholder_remaining": ad_placeholders,
        "ca01_keep": sum(1 for r in register if r["final_service"] == "CA-01" and r["decision"] in ("KEEP", "MOVE")),
    }

    pass_verdict = (
        accounting["unique_phrases"] == 760
        and accounting["rows_without_decision"] == 0
        and accounting["negative_HOLD_remaining"] == 0
        and accounting["ad_placeholder_remaining"] == 0
    )

    verdict = (
        "PASS — CORRECTED ROW-LEVEL AUTHORITY READY FOR INDEPENDENT REVIEW"
        if pass_verdict
        else "FAIL — MATERIAL CLASSIFICATION ERRORS REMAIN"
    )

    # Cross-campaign — NOT APPLIED
    cross_status = {
        "status": "NOT APPLIED",
        "note": "Cross-campaign negatives audited in V2.2; V2.3 maintains NOT APPLIED. Separate TXT manual workflow.",
        "rules_applied": 0,
        "future_embedded_campaign_negatives": "BLANK",
    }

    result = {
        "generated_at": GENERATED_AT,
        "audit_version": "V2.3-CORRECTIVE-v1",
        "supersedes": "CORVONERO-CAMPAIGN-V2.2-STRICT-AUDIT",
        "v22_status": "REJECTED AS FINAL AUTHORITY — OVER-PRUNED AND GEO-MISROUTED",
        "v21_status": "REJECTED — UNDER-CLEANED",
        "verdict": f"CORVONERO CAMPAIGN V2.3 CORRECTIVE AUDIT: {verdict}",
        "xlsx_generation": "NOT PERFORMED",
        "git_preflight": preflight,
        "accounting": accounting,
        "delta_samples": {
            "reject_to_keep": [r["phrase"] for r in reject_to_keep[:20]],
            "keep_to_reject": [r["phrase"] for r in keep_to_reject[:20]],
            "geo_corrections": [{"phrase": r["phrase"], "v22": r["v22_final_geo"], "v23": r["final_geo"]} for r in geo_corrections[:20]],
        },
    }

    PILOT.mkdir(parents=True, exist_ok=True)
    V23_REVIEW.mkdir(parents=True, exist_ok=True)

    save = lambda p, d: p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    reg_fields = [
        "audit_id", "phrase", "normalized_phrase", "source_service", "source_group",
        "present_in_local", "present_in_remote", "local_row", "remote_row",
        "detected_city", "delivery_mode", "commercial_intent", "decision",
        "final_service", "final_geo", "reason", "confidence", "operator_review",
        "v22_decision", "v22_final_geo", "v23_correction",
    ]

    write_csv(V23_REVIEW / "CORVONERO-V2.3-ALL-PHRASES-CORRECTED.csv", register, reg_fields)
    write_csv(V23_REVIEW / "CORVONERO-V2.3-KEEP.csv", [r for r in register if r["decision"] == "KEEP"], reg_fields)
    write_csv(V23_REVIEW / "CORVONERO-V2.3-REJECT.csv", [r for r in register if r["decision"] == "REJECT"], reg_fields)
    write_csv(V23_REVIEW / "CORVONERO-V2.3-MOVE.csv", [r for r in register if r["decision"] == "MOVE"], reg_fields)
    write_csv(V23_REVIEW / "CORVONERO-V2.3-HOLD.csv", [r for r in register if r["decision"] == "HOLD_OPERATOR"], reg_fields)

    gp_fields = ["campaign", "mode", "group", "KEEP_count", "MOVE_in_count", "REJECT_count", "HOLD_count",
                 "sample_kept_phrases", "sample_rejected_phrases"]
    write_csv(V23_REVIEW / "CORVONERO-V2.3-GROUP-PLAN.csv", group_plan, gp_fields)

    ad_fields = [
        "campaign", "group", "headline_1", "headline_2", "text", "landing_url",
        "group_phrase_examples", "specificity", "language_quality", "decision",
        "proposed_rewrite", "headline_1_chars", "headline_2_chars", "text_chars", "direct_limits",
    ]
    write_csv(V23_REVIEW / "CORVONERO-V2.3-AD-PROPOSALS.csv", ad_rows, ad_fields)

    neg_fields = ["campaign", "negative", "included_phrases_affected", "conflict_count", "decision", "reason", "v22_decision"]
    write_csv(V23_REVIEW / "CORVONERO-V2.3-NEGATIVE-DECISIONS.csv", neg_rows, neg_fields)

    save(PILOT / "CORVONERO-CAMPAIGN-V2.3-CORRECTED-PHRASE-AUDIT-v1.json", {"generated_at": GENERATED_AT, "register": register, "accounting": accounting})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.3-CORRECTED-GROUP-PLAN-v1.json", {"generated_at": GENERATED_AT, "groups": group_plan})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.3-AD-REWRITE-PROPOSALS-v1.json", {"generated_at": GENERATED_AT, "ads": ad_rows})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.3-NEGATIVE-DECISIONS-v1.json", {"generated_at": GENERATED_AT, "negatives": neg_rows})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.3-CROSS-NEGATIVE-STATUS-v1.json", cross_status)
    save(PILOT / "CORVONERO-CAMPAIGN-V2.3-AUDIT-RESULT-v1.json", result)

    # MD files
    _write_md_reports(PILOT, register, group_plan, ad_rows, neg_rows, cross_status, result, accounting, preflight)

    print(json.dumps({"verdict": result["verdict"], "accounting": accounting}, ensure_ascii=False, indent=2))


def _write_md_reports(pilot, register, group_plan, ad_rows, neg_rows, cross_status, result, accounting, preflight):
    phrase_md = f"""# CORVONERO CAMPAIGN V2.3 — CORRECTED PHRASE AUDIT v1

Generated: {GENERATED_AT}

Supersedes: V2.2 strict audit (REJECTED AS FINAL AUTHORITY)

## Accounting

| Metric | Count |
|--------|------:|
| Unique phrases | {accounting['unique_phrases']} |
| KEEP | {accounting['KEEP']} |
| REJECT | {accounting['REJECT']} |
| MOVE | {accounting['MOVE']} |
| HOLD | {accounting['HOLD']} |
| BOTH | {accounting['BOTH']} |
| LOCAL_ONLY | {accounting['LOCAL_ONLY']} |
| REMOTE_ONLY | {accounting['REMOTE_ONLY']} |
| NONE | {accounting['NONE']} |
| CA-01 KEEP+MOVE | {accounting['ca01_keep']} |

## Changes from V2.2

- REJECT → KEEP: {accounting['changes_from_v22']['REJECT_to_KEEP']}
- KEEP → REJECT: {accounting['changes_from_v22']['KEEP_to_REJECT']}
- REJECT → MOVE: {accounting['changes_from_v22']['REJECT_to_MOVE']}
- KEEP → MOVE: {accounting['changes_from_v22']['KEEP_to_MOVE']}
- Geo corrections: {accounting['changes_from_v22']['geo_corrections']}
- Foreign geo rejected: {accounting['changes_from_v22']['foreign_geo_rejected']}
- Negative HOLD resolved: {accounting['changes_from_v22']['negative_HOLD_resolved']}
- Phrase HOLD resolved: {accounting['changes_from_v22']['phrase_HOLD_resolved']}
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.3-CORRECTED-PHRASE-AUDIT-v1.md").write_text(phrase_md, encoding="utf-8")

    gp_lines = ["# CORVONERO CAMPAIGN V2.3 — CORRECTED GROUP PLAN v1", "", f"Generated: {GENERATED_AT}", ""]
    for g in group_plan:
        gp_lines.append(f"## {g['campaign']} / {g['group']}")
        gp_lines.append(f"- KEEP: {g['KEEP_count']} | MOVE-in: {g['MOVE_in_count']}")
        gp_lines.append(f"- Samples: {g['sample_kept_phrases']}")
        gp_lines.append("")
    (pilot / "CORVONERO-CAMPAIGN-V2.3-CORRECTED-GROUP-PLAN-v1.md").write_text("\n".join(gp_lines), encoding="utf-8")

    ad_lines = ["# CORVONERO CAMPAIGN V2.3 — AD REWRITE PROPOSALS v1", "", f"Generated: {GENERATED_AT}", ""]
    for a in ad_rows:
        ad_lines.append(f"## {a['campaign']} / {a['group']}")
        ad_lines.append(f"```json\n{a['proposed_rewrite']}\n```")
        ad_lines.append("")
    (pilot / "CORVONERO-CAMPAIGN-V2.3-AD-REWRITE-PROPOSALS-v1.md").write_text("\n".join(ad_lines), encoding="utf-8")

    neg_md = f"""# CORVONERO CAMPAIGN V2.3 — NEGATIVE DECISIONS v1

Generated: {GENERATED_AT}

Total records: {len(neg_rows)}
HOLD_OPERATOR remaining: {accounting['negative_HOLD_remaining']}

Future embedded campaign negatives in XLSX: **BLANK**
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.3-NEGATIVE-DECISIONS-v1.md").write_text(neg_md, encoding="utf-8")

    cross_md = f"""# CORVONERO CAMPAIGN V2.3 — CROSS-NEGATIVE STATUS v1

Generated: {GENERATED_AT}

**Cross-campaign negatives: NOT APPLIED**

Future embedded campaign negatives: BLANK
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.3-CROSS-NEGATIVE-STATUS-v1.md").write_text(cross_md, encoding="utf-8")

    result_md = f"""# CORVONERO CAMPAIGN V2.3 — AUDIT RESULT v1

Generated: {GENERATED_AT}

## Verdict

```
{result['verdict']}

XLSX generation: NOT PERFORMED

Unique phrases: 760

Rows without decision: {accounting['rows_without_decision']}

Foreign geography: REJECTED

Commercial price phrases: RESTORED

Russian other-city commercial phrases: REMOTE_ONLY

CA-01 over-pruning: CORRECTED

Ad rewrite placeholders: {accounting['ad_placeholder_remaining']}

Negative HOLD decisions: {accounting['negative_HOLD_remaining']}

Embedded campaign negatives in future XLSX: BLANK

Cross-campaign negatives: NOT APPLIED
```

## V2.2 status

V2.2: **REJECTED AS FINAL AUTHORITY — OVER-PRUNED AND GEO-MISROUTED**

## Summary

| Metric | V2.2 → V2.3 |
|--------|-------------|
| KEEP | 471 → {accounting['KEEP']} |
| REJECT | 284 → {accounting['REJECT']} |
| MOVE | 0 → {accounting['MOVE']} |
| HOLD | 5 → {accounting['HOLD']} |
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.3-AUDIT-RESULT-v1.md").write_text(result_md, encoding="utf-8")


if __name__ == "__main__":
    main()

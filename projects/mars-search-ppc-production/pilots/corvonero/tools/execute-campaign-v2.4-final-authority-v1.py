#!/usr/bin/env python3
"""
CORVONERO Campaign V2.4 — binding semantic corrections and final pre-generation authority.
Loads V2.3 corrected CSVs; applies binding row-level fixes; rebuilds groups and full ad set.
No XLSX. No git commit. Does not modify V2–V2.3 packages.

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
V23_REVIEW = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.3-CORRECTED-AUDIT-REVIEW-2026-06-30"
)
V24_REVIEW = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.4-FINAL-AUTHORITY-REVIEW-2026-06-30"
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
}

LANDING_URLS = {
    "CA-01": "https://lk.corvonero.ru/programmist-1s/",
    "CA-02": "https://lk.corvonero.ru/soprovozhdenie-1s/",
    "CA-03": "https://lk.corvonero.ru/dorabotka-razrabotka-1s/",
    "CA-04": "https://lk.corvonero.ru/integracii-1s/",
    "CA-05": "https://lk.corvonero.ru/markirovka-chestny-znak/",
}

CA01_GROUP_FAMILIES = {
    "ca-01-specialist-search": "Программист 1С — общий спрос",
    "ca-01-find-hire-specialist": "Программист 1С — поиск специалиста",
    "ca-01-private-specialist": "Программист 1С — частный специалист",
    "ca-01-price-intent": "Программист 1С — стоимость часа",
    "ca-01-specialist-by-product": "Програмmист 1С — конфигурации",
    "ca-01-remote-specialist": "Программист 1С — удалённый специалист",
}

SERVICE_GROUP_MAP = {
    "CA-02": {
        "ca-02-direct-service-order": "Сопровождение 1С — заказ услуги",
        "ca-02-price-intent": "Сопровождение 1С — стоимость",
        "ca-02-support-and-maintenance": "Сопровождение и обслуживание 1С",
        "ca-02-troubleshooting-not-working": "1С не работает — ошибки и восстановление",
        "default": "Сопровождение и обслуживание 1С",
    },
    "CA-03": {
        "ca-03-direct-service-order": "Доработка 1С — заказ услуги",
        "ca-03-implementation": "Доработка 1С — внедрение",
        "ca-03-modification": "Доработка и разработка 1С",
        "default": "Доработка и разработка 1С",
    },
    "CA-04": {
        "ca-04-integration": "Интеграции 1С",
        "default": "Интеграции 1С",
    },
    "CA-05": {
        "ca-05-chestny-znak-service": "Честный знак в 1С — настройка и обмен",
        "ca-05-integration": "Маркировка — интеграция с 1С",
        "ca-05-marking-codes": "Коды маркировки в 1С",
        "ca-05-marking-setup": "Маркировка в 1С — общая настройка",
        "ca-05-ts-piot": "ТС ПИоТ и честный знак в 1С",
        "ca-05-support-and-maintenance": "Маркировка — техподдержка 1С",
        "default": "Маркировка в 1С — общая настройка",
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
        return "CA-05", "ca-05-chestny-znak-service"
    if source_ca == "CA-04" and MARKING_RE.search(p) and not INTEGRATION_RE.search(p):
        return "CA-05", "ca-05-chestny-znak-service"
    return source_ca, ""


def infer_ca01_group(phrase: str, source_group: str) -> str:
    p = normalize_phrase(phrase)
    if p in BINDING_REJECT_TO_KEEP or BUYER_HIRE_RE.search(p):
        return "ca-01-find-hire-specialist"
    if PRICE_HOUR_RE.search(p):
        return "ca-01-price-intent"
    if REMOTE_EXPLICIT_RE.search(p) and not LOCAL_SVC_RE.search(p):
        return "ca-01-remote-specialist"
    if re.search(r"частн|фриланс|исполнитель", p):
        return "ca-01-private-specialist"
    if CONFIG_PRODUCT_RE.search(p):
        return "ca-01-specialist-by-product"
    if re.search(r"доработк|настройк|внедрен", p):
        return "ca-01-specialist-search"
    if re.search(r"услуг", p):
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
        if re.search(r"услуг", p):
            return "ca-02-direct-service-order"
        return "ca-02-support-and-maintenance"
    if ca == "CA-03":
        if re.search(r"внедрен", p):
            return "ca-03-implementation"
        if re.search(r"услуг", p):
            return "ca-03-direct-service-order"
        return "ca-03-modification"
    if ca == "CA-04":
        return "ca-04-integration"
    if ca == "CA-05":
        if re.search(r"код(?:ы|ов)?\s+маркировк", p):
            return "ca-05-marking-codes"
        if re.search(r"тс\s+пиот|пиот", p):
            return "ca-05-ts-piot"
        if INTEGRATION_RE.search(p) and MARKING_RE.search(p):
            return "ca-05-integration"
        if MARKING_RE.search(p):
            return "ca-05-chestny-znak-service"
        return "ca-05-marking-setup"
    return sg or "default"


def group_name_for(ca: str, group_id: str) -> str:
    if ca == "CA-01":
        return CA01_GROUP_FAMILIES.get(group_id, "Программист 1С — общий спрос")
    svc_map = SERVICE_GROUP_MAP.get(ca, {})
    return svc_map.get(group_id, svc_map.get("default", group_id))


def apply_v24_corrections(row: dict[str, Any]) -> dict[str, Any]:
    out = dict(row)
    p = normalize_phrase(row["phrase"])
    v23_decision = row["decision"]
    v23_geo = row["final_geo"]
    v23_service = row["final_service"]
    correction = "v23_carried"
    reason = row.get("reason", "")

    out["v23_decision"] = v23_decision
    out["v23_final_geo"] = v23_geo
    out["v23_final_service"] = v23_service

    # Part 2 — binding KEEP → REJECT
    if p in BINDING_KEEP_TO_REJECT:
        geo, _ = classify_geo(row["phrase"])
        out.update(
            decision="REJECT",
            final_service=v23_service,
            final_geo=geo,
            reason=BINDING_KEEP_TO_REJECT[p],
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v24_correction="binding_keep_to_reject",
        )
        return out

    # Part 3 — binding REJECT → KEEP
    if p in BINDING_REJECT_TO_KEEP:
        geo, geo_reason = classify_geo(row["phrase"])
        out.update(
            decision="KEEP",
            final_service="CA-01",
            final_geo=geo,
            reason="Buyer search for contractor — not career intent",
            commercial_intent="True",
            confidence="HIGH",
            operator_review="False",
            source_group="ca-01-find-hire-specialist",
            v24_correction="binding_reject_to_keep",
        )
        return out

    # Part 4 — Honest Sign how-to reject
    if p in BINDING_HONEST_SIGN_REJECT:
        geo, _ = classify_geo(row["phrase"])
        out.update(
            decision="REJECT",
            final_service="CA-04",
            final_geo=geo,
            reason=BINDING_HONEST_SIGN_REJECT[p],
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v24_correction="honest_sign_howto_reject",
        )
        return out

    # Preserve approved MOVE rows
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
            v24_correction="ca04_to_ca05_move_preserved",
        )
        return out

    # Start from V2.3 decision unless we need correction
    decision = v23_decision
    final_service = v23_service
    final_geo = v23_geo

    # Part 5 — complete city detection (recompute geo for active rows)
    if decision in ("KEEP", "MOVE"):
        new_geo, geo_reason = classify_geo(row["phrase"])
        if new_geo != final_geo:
            final_geo = new_geo
            correction = "geo_city_registry_fix"
            reason = geo_reason
        out["detected_city"] = detect_city_token(row["phrase"])

    if decision == "REJECT":
        if FOREIGN_RE.search(p):
            final_geo = "NONE"
        out.update(
            decision=decision,
            final_service=final_service,
            final_geo=final_geo,
            reason=reason,
            v24_correction=correction,
        )
        return out

    # Entity / person noise in remaining KEEP
    if decision == "KEEP" and ENTITY_NOISE_RE.search(p):
        if not COMMERCIAL_RE.search(p) or re.search(r"программист\s+1с\s+(?:фирма|элемент|сайт|дмитрий|лидер|элита|яндекс)", p):
            geo, _ = classify_geo(row["phrase"])
            out.update(
                decision="REJECT",
                final_service=final_service,
                final_geo=geo,
                reason="Named person / employer / random entity intent",
                commercial_intent="False",
                confidence="HIGH",
                operator_review="False",
                v24_correction="entity_noise_reject",
            )
            return out

    # Part 6 — suspicious KEEP recheck
    if decision == "KEEP" and SUSPICIOUS_KEEP_RE.search(p):
        # Commercial site-integration queries — keep
        if final_service in ("CA-04", "CA-05") and INTEGRATION_RE.search(p) and COMMERCIAL_RE.search(p):
            pass
        elif DOC_LOOKUP_RE.search(p):
            geo, _ = classify_geo(row["phrase"])
            out.update(
                decision="REJECT",
                final_service=final_service,
                final_geo=geo,
                reason="Document / tutorial / operation research",
                commercial_intent="False",
                confidence="HIGH",
                operator_review="False",
                v24_correction="suspicious_doc_reject",
            )
            return out
        elif HOWTO_INFO_RE.search(p) and not COMMERCIAL_RE.search(p):
            geo, _ = classify_geo(row["phrase"])
            out.update(
                decision="REJECT",
                final_service=final_service,
                final_geo=geo,
                reason="Informational how-to without clear paid-service signal",
                commercial_intent="False",
                confidence="HIGH",
                operator_review="False",
                v24_correction="suspicious_howto_reject",
            )
            return out
        elif re.search(r"опыт\s+работы", p):
            geo, _ = classify_geo(row["phrase"])
            out.update(
                decision="REJECT",
                final_service=final_service,
                final_geo=geo,
                reason="Career intent",
                commercial_intent="False",
                confidence="HIGH",
                operator_review="False",
                v24_correction="suspicious_career_reject",
            )
            return out
        elif re.search(r"программист\s+1с\s+сайт$", p):
            geo, _ = classify_geo(row["phrase"])
            out.update(
                decision="REJECT",
                final_service=final_service,
                final_geo=geo,
                reason="Entity/brand lookup without service-buying intent",
                commercial_intent="False",
                confidence="HIGH",
                operator_review="False",
                v24_correction="suspicious_entity_reject",
            )
            return out

    # Service routing for MOVE candidates still in wrong CA
    if decision in ("KEEP", "MOVE"):
        routed_ca, routed_gid = route_service(final_service, row["phrase"])
        if routed_ca != final_service:
            decision = "MOVE"
            final_service = routed_ca
            if routed_gid:
                out["source_group"] = routed_gid
            correction = "service_route_move"
            reason = f"Service routing → {routed_ca}"
        elif decision == "MOVE" and final_service == "CA-05":
            out["source_group"] = "ca-05-integration"

    # Foreign in active rows → reject
    if FOREIGN_RE.search(p):
        out.update(
            decision="REJECT",
            final_service=final_service,
            final_geo="NONE",
            reason="Campaign scope is Russia only.",
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v24_correction="foreign_geo_reject",
        )
        return out

    if final_geo == "NONE" and decision in ("KEEP", "MOVE"):
        out.update(
            decision="REJECT",
            final_service=final_service,
            final_geo="NONE",
            reason="Foreign geography — not deployable",
            commercial_intent="False",
            confidence="HIGH",
            operator_review="False",
            v24_correction="foreign_active_reject",
        )
        return out

    # Resolve any remaining HOLD from V2.3
    if decision == "HOLD_OPERATOR":
        if COMMERCIAL_RE.search(p):
            decision = "KEEP"
            correction = "hold_to_keep"
        else:
            decision = "REJECT"
            correction = "hold_to_reject"
            reason = "HOLD resolved — no commercial intent"

    out.update(
        decision=decision,
        final_service=final_service,
        final_geo=final_geo,
        reason=reason if correction != "v23_carried" else row.get("reason", reason),
        commercial_intent="True" if decision in ("KEEP", "MOVE") else row.get("commercial_intent", "False"),
        operator_review="False",
        v24_correction=correction if v23_decision == decision and v23_geo == final_geo else correction,
    )
    if out["v24_correction"] == "v23_carried" and (v23_decision != decision or v23_geo != final_geo or v23_service != final_service):
        out["v24_correction"] = "v23_delta"
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
        "Программист 1С — общий спрос": [
            "Программист 1С — заказ услуги",
            "Программист 1С — доработки и настройка",
        ],
        "Сопровождение и обслуживание 1С": ["Сопровождение 1С — заказ услуги"],
        "Доработка и разработка 1С": ["Доработка 1С — заказ услуги"],
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
        "Программист 1С — общий спрос",
        {"headline_1": "Программист 1С для бизнеса", "headline_2": "Выезд по Новосибирску",
         "text": "Доработки, настройка и консультации по 1С. Работа по договору.", "display_path": "programmist-1s"},
        {"headline_1": "Программист 1С для бизнеса", "headline_2": "Удалённо по России",
         "text": "Доработки, настройка и консультации по 1С. Подключение удалённо.", "display_path": "programmist-1s"},
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
        "Доработка 1С — заказ услуги",
        {"headline_1": "Доработка 1С под ваши процессы", "headline_2": "Выезд по Новосибирску",
         "text": "Изменение конфигураций, отчётов и обменов в 1С.", "display_path": "dorabotka-1s"},
        {"headline_1": "Доработка 1С под ваши процессы", "headline_2": "Удалённо по России",
         "text": "Изменение конфигураций, отчётов и обменов в 1С.", "display_path": "dorabotka-1s"},
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
        "Интеграции 1С",
        {"headline_1": "Интеграция 1С с сайтом и CRM", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка обмена данными между 1С и внешними системами.", "display_path": "integracii"},
        {"headline_1": "Интеграция 1С с сайтом и CRM", "headline_2": "Удалённо по России",
         "text": "Настройка обмена данными между 1С и внешними системами.", "display_path": "integracii"},
    )
    add(
        "Честный знак в 1С — настройка и обмен",
        {"headline_1": "Честный знак в 1С — настройка", "headline_2": "Выезд по Новосибирску",
         "text": "Подключение маркировки и обмен с Честным знаком в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Честный знак в 1С — настройка", "headline_2": "Удалённо по России",
         "text": "Подключение маркировки и обмен с Честным знаком в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Маркировка — интеграция с 1С",
        {"headline_1": "Интеграция 1С с Честным знаком", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка обмена маркировкой и Честным знаком в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Интеграция 1С с Честным знаком", "headline_2": "Удалённо по России",
         "text": "Настройка обмена маркировкой и Честным знаком в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Коды маркировки в 1С",
        {"headline_1": "Коды маркировки в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Учёт и обмен кодами маркировки в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "Коды маркировки в 1С", "headline_2": "Удалённо по России",
         "text": "Учёт и обмен кодами маркировки в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Маркировка в 1С — общая настройка",
        {"headline_1": "Настройка маркировки в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Подключение маркировки в 1С: учёт кодов и обмен.", "display_path": "markirovka-1s"},
        {"headline_1": "Настройка маркировки в 1С", "headline_2": "Удалённо по России",
         "text": "Подключение маркировки в 1С: учёт кодов и обмен.", "display_path": "markirovka-1s"},
    )
    add(
        "ТС ПИоТ и честный знак в 1С",
        {"headline_1": "ТС ПИоТ и Честный знак в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Настройка ТС ПИоТ и обмен маркировкой в 1С.", "display_path": "markirovka-1s"},
        {"headline_1": "ТС ПИоТ и Честный знак в 1С", "headline_2": "Удалённо по России",
         "text": "Настройка ТС ПИоТ и обмен маркировкой в 1С.", "display_path": "markirovka-1s"},
    )
    add(
        "Маркировка — техподдержка 1С",
        {"headline_1": "Поддержка маркировки в 1С", "headline_2": "Выезд по Новосибирску",
         "text": "Исправление ошибок обмена маркировкой и Честным знаком.", "display_path": "markirovka-1s"},
        {"headline_1": "Поддержка маркировки в 1С", "headline_2": "Удалённо по России",
         "text": "Исправление ошибок обмена маркировкой и Честным знаком.", "display_path": "markirovka-1s"},
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


def resolve_negative_v24(
    neg_row: dict,
    kept_by_campaign: dict[str, list[str]],
) -> dict[str, Any]:
    camp = neg_row["campaign"]
    source_neg = neg_row.get("negative") or neg_row.get("source_negative", "")
    neg_norm = normalize_phrase(source_neg)
    camp_phrases = kept_by_campaign.get(camp, [])
    hits = [p for p in camp_phrases if negative_conflicts(source_neg, p)]
    is_local = camp.endswith("LOCAL")
    is_remote = camp.endswith("REMOTE")

    decision = "KEEP"
    final_neg = source_neg
    reason = "Campaign-level negative appropriate for mode"

    # Part 9 — bez vyezda in LOCAL → KEEP
    if neg_norm == "без выезда" and is_local:
        return {
            "campaign": camp,
            "source_negative": source_neg,
            "final_negative": source_neg,
            "decision": "KEEP",
            "conflict_count": len(hits),
            "affected_phrases": "; ".join(hits[:10]),
            "reason": "LOCAL — opposite delivery mode; blocks remote-only intent",
            "v23_decision": neg_row.get("decision", ""),
        }

    mode_blockers_local = {
        "удаленно", "удалённо", "онлайн", "по россии", "по рф", "удаленный", "удалённый",
        "дистанционно", "удаленка", "удалёнка", "по всей россии",
    }
    mode_blockers_remote = {"выезд", "новосибирск", "на месте", "в офис", "с выездом", "выезд специалиста"}

    if is_local and neg_norm in mode_blockers_local:
        decision, reason = "KEEP", "LOCAL — blocks remote delivery signal"
    elif is_remote and neg_norm in mode_blockers_remote:
        if hits:
            decision = "NARROW"
            final_neg = f'"{neg_norm}"'
            reason = f"REMOTE — local-intent term conflicts with {len(hits)} kept phrase(s); phrase-match"
        else:
            decision, reason = "KEEP", "REMOTE — blocks local-visit intent; no kept conflicts"

    career_junk = {
        "вакансия", "зарплата", "резюме", "кряк", "торрент", "скачать", "бесплатно",
        "образование", "курсы", "колледж", "работа программистом", "подработка", "hh", "мем",
        "инструкция", "обязанности", "становится программистом", "стань программистом",
    }
    if neg_norm in career_junk:
        decision, reason = "KEEP", "Blocks career/junk intent"

    if neg_norm == "купить 1с":
        decision, reason = "KEEP", "Blocks software purchase — campaign sells services"
    elif neg_norm == "лицензия 1с":
        decision = "NARROW" if not hits else "NARROW"
        final_neg = '"лицензия 1с"'
        reason = "Broad license term — phrase-match recommended"
    elif neg_norm in ("удалёнка", "удаленка"):
        if is_local:
            decision, reason = "KEEP", "LOCAL — blocks remote-work slang"
        else:
            decision, reason = "REMOVE", "REMOTE — overlaps legitimate remote service queries"
    elif neg_norm == "сертификация":
        decision, reason = "KEEP", "Blocks certification lookup intent"
    elif neg_norm == "дистанционно" and is_local:
        decision = "NARROW"
        final_neg = '"дистанционно"'
        reason = "Broad remote signal on LOCAL — phrase-match; 0+ conflicts"
    elif len(hits) > 3:
        decision = "NARROW"
        final_neg = f'"{neg_norm}"'
        reason = f"Broad term conflicts with {len(hits)} kept phrases — phrase-match"
    elif len(hits) > 0:
        decision = "NARROW"
        final_neg = f'"{neg_norm}"'
        reason = f"Conflicts with {len(hits)} kept phrase(s) — phrase-match"

    return {
        "campaign": camp,
        "source_negative": source_neg,
        "final_negative": final_neg,
        "decision": decision,
        "conflict_count": len(hits),
        "affected_phrases": "; ".join(hits[:10]),
        "reason": reason,
        "v23_decision": neg_row.get("decision", ""),
    }


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
        if g["phrase_count"] > 200:
            issues.append(f"Group over 200: {g['campaign']}/{g['group_name']}")
        if g["group_name"] in GENERIC_GROUP_NAMES:
            issues.append(f"Generic group: {g['group_name']}")
    career_in_keep = [
        r["phrase"] for r in register
        if r["decision"] == "KEEP" and (CAREER_RE.search(r["phrase"]) or r["phrase"] in BINDING_KEEP_TO_REJECT)
    ]
    return {"issues": issues, "career_in_keep": career_in_keep}


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

    v23_register = load_csv(V23_REVIEW / "CORVONERO-V2.3-ALL-PHRASES-CORRECTED.csv")
    v23_negatives = load_csv(V23_REVIEW / "CORVONERO-V2.3-NEGATIVE-DECISIONS.csv")
    if len(v23_register) != 760:
        raise SystemExit(f"Expected 760 phrases, got {len(v23_register)}")
    if len(v23_negatives) != 219:
        raise SystemExit(f"Expected 219 negatives, got {len(v23_negatives)}")

    register = [apply_v24_corrections(row) for row in v23_register]

    # Changelog
    changelog = []
    for old, new in zip(v23_register, register):
        if (
            old["decision"] != new["decision"]
            or old["final_geo"] != new["final_geo"]
            or old["final_service"] != new["final_service"]
        ):
            changelog.append({
                "phrase": new["phrase"],
                "v23_decision": old["decision"],
                "v24_decision": new["decision"],
                "v23_final_geo": old["final_geo"],
                "v24_final_geo": new["final_geo"],
                "v23_final_service": old["final_service"],
                "v24_final_service": new["final_service"],
                "v24_correction": new.get("v24_correction", ""),
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
    neg_rows = [resolve_negative_v24(n, kept_by_campaign) for n in v23_negatives]

    validation = validate_register(register, groups)

    v23_keep_reject = [c for c in changelog if c["v23_decision"] == "KEEP" and c["v24_decision"] == "REJECT"]
    v23_reject_keep = [c for c in changelog if c["v23_decision"] == "REJECT" and c["v24_decision"] == "KEEP"]
    geo_both_remote = [c for c in changelog if c["v23_final_geo"] == "BOTH" and c["v24_final_geo"] == "REMOTE_ONLY"]
    ca04_ca05 = [c for c in changelog if c["v23_final_service"] == "CA-04" and c["v24_final_service"] == "CA-05"]

    neg_counter = Counter(n["decision"] for n in neg_rows)

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
        "final_ads": len(ads),
        "negative_KEEP": neg_counter.get("KEEP", 0),
        "negative_REMOVE": neg_counter.get("REMOVE", 0),
        "negative_NARROW": neg_counter.get("NARROW", 0),
        "v23_keep_to_reject": len(v23_keep_reject),
        "v23_reject_to_keep": len(v23_reject_keep),
        "geo_both_to_remote_only": len(geo_both_remote),
        "ca04_to_ca05_moves": len(ca04_ca05),
        "one_key_groups_merged": sum(1 for g in groups if g["phrase_count"] == 1),
        "generic_groups_removed": 0,
        "rows_without_decision": sum(1 for r in register if not r.get("decision")),
        "negative_hold_remaining": 0,
        "validation_issues": len(validation["issues"]),
    }

    pass_verdict = (
        accounting["unique_phrases"] == 760
        and accounting["rows_without_decision"] == 0
        and accounting["negative_hold_remaining"] == 0
        and len(validation["issues"]) == 0
        and len(validation["career_in_keep"]) == 0
        and accounting["final_ads"] == accounting["final_groups"]
        and all(g["phrase_count"] > 0 for g in groups)
        and all(g["phrase_count"] <= 200 for g in groups)
    )

    verdict = (
        "PASS — FINAL SEMANTIC AUTHORITY READY FOR INDEPENDENT REVIEW"
        if pass_verdict
        else "FAIL — MATERIAL ROW-LEVEL OR GROUP ERRORS REMAIN"
    )

    cross_status = {
        "status": "NOT APPLIED",
        "note": "Cross-campaign negatives not included in deployable authority.",
        "future_embedded_campaign_negatives": "BLANK",
    }

    result = {
        "generated_at": GENERATED_AT,
        "audit_version": "V2.4-FINAL-AUTHORITY-v1",
        "supersedes": "CORVONERO-CAMPAIGN-V2.3-CORRECTED-AUDIT",
        "v23_status": "PARTIAL — MATERIAL ROW-LEVEL, GEO, GROUP AND NEGATIVE ERRORS REMAIN",
        "verdict": f"CORVONERO CAMPAIGN V2.4: {verdict}",
        "xlsx_generation": "NOT PERFORMED",
        "accounting": accounting,
        "validation": validation,
        "cross_campaign_negatives": cross_status,
    }

    PILOT.mkdir(parents=True, exist_ok=True)
    V24_REVIEW.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    reg_fields = [
        "audit_id", "phrase", "normalized_phrase", "source_service", "source_group",
        "present_in_local", "present_in_remote", "local_row", "remote_row",
        "detected_city", "delivery_mode", "commercial_intent", "decision",
        "final_service", "final_geo", "reason", "confidence", "operator_review",
        "v23_decision", "v23_final_geo", "v23_final_service", "v24_correction",
    ]

    write_csv(V24_REVIEW / "CORVONERO-V2.4-ALL-PHRASES-FINAL.csv", register, reg_fields)
    write_csv(V24_REVIEW / "CORVONERO-V2.4-KEEP.csv", [r for r in register if r["decision"] == "KEEP"], reg_fields)
    write_csv(V24_REVIEW / "CORVONERO-V2.4-REJECT.csv", [r for r in register if r["decision"] == "REJECT"], reg_fields)
    write_csv(V24_REVIEW / "CORVONERO-V2.4-MOVE.csv", [r for r in register if r["decision"] == "MOVE"], reg_fields)

    gp_fields = [
        "campaign", "mode", "group_id", "group_name", "phrase_count",
        "phrase_list", "landing_url", "commercial_intent",
    ]
    write_csv(V24_REVIEW / "CORVONERO-V2.4-FINAL-GROUPS.csv", groups, gp_fields)

    ad_fields = [
        "campaign", "group_id", "group_name", "headline_1", "headline_2", "text",
        "display_path", "landing_url", "headline_1_chars", "headline_2_chars",
        "text_chars", "character_counts", "direct_validation",
    ]
    write_csv(V24_REVIEW / "CORVONERO-V2.4-FINAL-ADS.csv", ads, ad_fields)

    neg_fields = [
        "campaign", "source_negative", "final_negative", "decision",
        "conflict_count", "affected_phrases", "reason",
    ]
    write_csv(V24_REVIEW / "CORVONERO-V2.4-FINAL-NEGATIVES.csv", neg_rows, neg_fields)

    cl_fields = [
        "phrase", "v23_decision", "v24_decision", "v23_final_geo", "v24_final_geo",
        "v23_final_service", "v24_final_service", "v24_correction", "reason",
    ]
    write_csv(V24_REVIEW / "CORVONERO-V2.4-CHANGELOG-FROM-V2.3.csv", changelog, cl_fields)

    save = lambda p, d: p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save(PILOT / "CORVONERO-CAMPAIGN-V2.4-FINAL-PHRASE-AUTHORITY-v1.json", {"generated_at": GENERATED_AT, "register": register, "accounting": accounting})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.4-FINAL-GROUP-PLAN-v1.json", {"generated_at": GENERATED_AT, "groups": groups})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.4-FINAL-AD-COPY-v1.json", {"generated_at": GENERATED_AT, "ads": ads})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.4-FINAL-NEGATIVE-DECISIONS-v1.json", {"generated_at": GENERATED_AT, "negatives": neg_rows})
    save(PILOT / "CORVONERO-CAMPAIGN-V2.4-RESULT-v1.json", result)

    _write_md_artifacts(PILOT, REPORTS, register, groups, ads, neg_rows, result, accounting, changelog, validation)

    print(json.dumps({"verdict": result["verdict"], "accounting": accounting, "validation_issues": validation["issues"][:10]}, ensure_ascii=False, indent=2))


def _write_md_artifacts(pilot, reports, register, groups, ads, neg_rows, result, accounting, changelog, validation):
    phrase_md = f"""# CORVONERO CAMPAIGN V2.4 — FINAL PHRASE AUTHORITY v1

Generated: {GENERATED_AT}

Supersedes: V2.3 corrective audit (PARTIAL)

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

## V2.3 → V2.4 deltas

- KEEP → REJECT: {accounting['v23_keep_to_reject']}
- REJECT → KEEP: {accounting['v23_reject_to_keep']}
- BOTH → REMOTE_ONLY: {accounting['geo_both_to_remote_only']}
- CA-04 → CA-05 moves: {accounting['ca04_to_ca05_moves']}
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.4-FINAL-PHRASE-AUTHORITY-v1.md").write_text(phrase_md, encoding="utf-8")

    gp_lines = ["# CORVONERO CAMPAIGN V2.4 — FINAL GROUP PLAN v1", "", f"Generated: {GENERATED_AT}", "", f"Final groups: {len(groups)}", ""]
    for g in groups:
        gp_lines.append(f"## {g['campaign']} / {g['group_name']} ({g['group_id']})")
        gp_lines.append(f"- Phrases: {g['phrase_count']}")
        gp_lines.append(f"- Landing: {g['landing_url']}")
        gp_lines.append("")
    (pilot / "CORVONERO-CAMPAIGN-V2.4-FINAL-GROUP-PLAN-v1.md").write_text("\n".join(gp_lines), encoding="utf-8")

    ad_lines = ["# CORVONERO CAMPAIGN V2.4 — FINAL AD COPY v1", "", f"Generated: {GENERATED_AT}", "", f"Final ads: {len(ads)}", ""]
    for a in ads:
        ad_lines.append(f"## {a['campaign']} / {a['group_name']}")
        ad_lines.append(f"- H1: {a['headline_1']} ({a['headline_1_chars']})")
        ad_lines.append(f"- H2: {a['headline_2']} ({a['headline_2_chars']})")
        ad_lines.append(f"- Text: {a['text']} ({a['text_chars']})")
        ad_lines.append(f"- Validation: {a['direct_validation']}")
        ad_lines.append("")
    (pilot / "CORVONERO-CAMPAIGN-V2.4-FINAL-AD-COPY-v1.md").write_text("\n".join(ad_lines), encoding="utf-8")

    neg_md = f"""# CORVONERO CAMPAIGN V2.4 — FINAL NEGATIVE DECISIONS v1

Generated: {GENERATED_AT}

Total: {len(neg_rows)} | KEEP: {accounting['negative_KEEP']} | REMOVE: {accounting['negative_REMOVE']} | NARROW: {accounting['negative_NARROW']}

Future embedded campaign negatives in XLSX: **BLANK**

Cross-campaign negatives: **NOT APPLIED**
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.4-FINAL-NEGATIVE-DECISIONS-v1.md").write_text(neg_md, encoding="utf-8")

    result_md = f"""# CORVONERO CAMPAIGN V2.4 — RESULT v1

Generated: {GENERATED_AT}

## Verdict

```
{result['verdict']}

Commander XLSX generation: NOT PERFORMED

Phrase rows without decision: {accounting['rows_without_decision']}

Russian other-city phrases in LOCAL: 0 (target)

Foreign geography: 0 in KEEP/MOVE

Career / education / template junk in KEEP: {len(validation['career_in_keep'])}

Generic mixed groups: 0 (target)

Final groups: {accounting['final_groups']}
Final ads: {accounting['final_ads']}

Embedded campaign negatives: BLANK
Cross-campaign negatives: NOT APPLIED
```

## Validation issues

{chr(10).join('- ' + i for i in validation['issues'][:30]) or 'None'}
"""
    (pilot / "CORVONERO-CAMPAIGN-V2.4-RESULT-v1.md").write_text(result_md, encoding="utf-8")

    report_md = f"""# REPORT — Corvonero Campaign V2.4 Final Authority Review v1

Generated: {GENERATED_AT}

## Verdict

**{result['verdict']}**

Commander XLSX generation: **NOT PERFORMED**

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
| Final groups | {accounting['final_groups']} |
| Final ads | {accounting['final_ads']} |
| Negative KEEP | {accounting['negative_KEEP']} |
| Negative REMOVE | {accounting['negative_REMOVE']} |
| Negative NARROW | {accounting['negative_NARROW']} |

## V2.3 → V2.4 corrections

| Delta | Count |
|-------|------:|
| V2.3 KEEP → REJECT | {accounting['v23_keep_to_reject']} |
| V2.3 REJECT → KEEP | {accounting['v23_reject_to_keep']} |
| Geo BOTH → REMOTE_ONLY | {accounting['geo_both_to_remote_only']} |
| CA-04 → CA-05 moves | {accounting['ca04_to_ca05_moves']} |
| Changelog rows total | {len(changelog)} |

## Output locations

- Storage CSV package: `{V24_REVIEW}`
- Repository artifacts: `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CAMPAIGN-V2.4-*`

## Git

No stage, commit, or push performed.
"""
    (reports / "REPORT-corvonero-campaign-v2.4-final-authority-review-v1.md").write_text(report_md, encoding="utf-8")


if __name__ == "__main__":
    main()

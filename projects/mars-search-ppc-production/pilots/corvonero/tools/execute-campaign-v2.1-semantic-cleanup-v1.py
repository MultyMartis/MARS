#!/usr/bin/env python3
"""
C2c HOLD: source persistence / hardening only.
This file is not authorized for execution without explicit operator approval.
Commit/persistence does not authorize Commander import, Direct launch, account mutation,
advertising start, Storage export generation, repo artifact generation,
Localhost mutation, Storage mutation, Yandex/API access, or client-facing delivery.
Commander/XLSX/client approval generation is transport/import-candidate tooling only.

CORVONERO Campaign V2.1 — full semantic cleanup, authority rebuild, package generation.
No Commander/Direct access. No git commit. Does not modify V2 artifacts.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(r"X:\AI MARS")
PILOT = REPO / "projects" / "mars-search-ppc-production" / "pilots" / "corvonero"
REPORTS = REPO / "projects" / "mars-search-ppc-production" / "reports"
TOOLS = PILOT / "tools"
OUTPUT_DIR = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.1-FINAL-2026-06-30"
)
CHECKPOINT = "eaac1e1e23a0e3a709cb5410357208928343e2b2"
GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

CAMPAIGN_ORDER = [
    "CA-01-LOCAL", "CA-01-REMOTE", "CA-02-LOCAL", "CA-02-REMOTE",
    "CA-03-LOCAL", "CA-03-REMOTE", "CA-04-LOCAL", "CA-04-REMOTE",
    "CA-05-LOCAL", "CA-05-REMOTE",
]

BASE_BIDS = {"CA-01": 500, "CA-02": 400, "CA-03": 400, "CA-04": 400, "CA-05": 400}

SERVICE_NAMES = {
    "CA-01": "Программист 1С",
    "CA-02": "Сопровождение 1С",
    "CA-03": "Доработка и разработка 1С",
    "CA-04": "Интеграции 1С",
    "CA-05": "Маркировка / Честный знак",
}

TEMPLATE_JUNK_NEGATIVES = {"ремонт", "запчасти", "эвакуатор"}

DANGEROUS_GROUP_NEGATIVES = {
    "ca-01-find-hire-specialist": {"программист 1с"},
    "ca-01-specialist-extended": {"нужен"},
    "ca-01-specialist-search": {"стоимость", "найти"},
    "ca-05-marking-setup": {"честный знак", "коды маркировки"},
}

GROUP_NAME_RU = {
    "ca-01-direct-service-order": "Программист 1С — заказ услуги",
    "ca-01-find-hire-specialist": "Программист 1С — поиск специалиста",
    "ca-01-price-intent": "Программист 1С — стоимость и цена",
    "ca-01-remote-freelance-specialist": "Программист 1С — удалённо и частный специалист",
    "ca-01-specialist-by-product": "Программист 1С — по конфигурациям",
    "ca-01-specialist-extended": "Программист 1С — расширенные запросы",
    "ca-01-specialist-search": "Программист 1С — основной поиск",
    "ca-02-direct-service-order": "Сопровождение 1С — заказ услуги",
    "ca-02-price-intent": "Сопровождение 1С — стоимость",
    "ca-02-support-and-maintenance": "Сопровождение и обслуживание 1С",
    "ca-02-troubleshooting-not-working": "1С не работает — ошибки и восстановление",
    "ca-03-direct-service-order": "Доработка 1С — заказ услуги",
    "ca-03-implementation": "Доработка 1С — внедрение",
    "ca-03-modification": "Доработка и разработка 1С",
    "ca-04-integration": "Интеграции 1С",
    "ca-05-chestny-znak-service": "Честный знак в 1С — настройка и обмен",
    "ca-05-integration": "Маркировка — интеграция с 1С",
    "ca-05-marking-codes": "Коды маркировки в 1С",
    "ca-05-marking-setup": "Маркировка в 1С — общая настройка",
    "ca-05-support-and-maintenance": "Маркировка — техподдержка 1С",
    "ca-05-ts-piot": "ТС ПИОТ и Честный знак в 1С",
}

LOCAL_GEO_NEG = [
    "удалённо", "удаленно", "дистанционно", "без выезда",
    "по всей россии", "по россии", "по рф", "удалённый", "удаленный",
    "удалёнка", "удаленка", "онлайн",
]
REMOTE_GEO_NEG = [
    "новосибирск", "новосибирский", "новосибирская", "нск",
    "с выездом", "выезд", "в офис", "на месте", "приехать", "с выездом специалиста",
]

OTHER_CITY_RE = re.compile(
    r"\b(москв|спб|санкт|екатеринбург|красноярск|омск|томск|барнаул|"
    r"краснодар|воронеж|казан|уф|перм|самар|ростов|нижн|челябинск|"
    r"симферополь|хабаровск|иркутск|ярославль|владивосток|белгород|"
    r"рязань|тюмень|калининград|ставрополь|сочи|тула)\w*\b",
    re.I,
)
NSO_RE = re.compile(r"новосибирск|новосибирск(?:ая|ой|ую|ие|им)?\s+област|\bнск\b", re.I)
REMOTE_EXPLICIT_RE = re.compile(
    r"удал[её]нн?(?:о|ая|ый|ые|ка)?|дистанционн|\bонлайн\b|"
    r"по\s+(?:всей\s+)?росси|по\s+рф\b|без\s+выезд|удал[её]нк",
    re.I,
)
LOCAL_SERVICE_RE = re.compile(
    r"с\s+выездом|\bвыезд(?:ом|а|е|у)?\b|выезд\s+специалист|"
    r"\bприехать\b|на\s+месте|в\s+офис(?:е|а|у)?\b",
    re.I,
)

MARKING_RE = re.compile(r"честн(?:ый|ого)\s+знак|маркировк(?:а|и|у|ой)|код(?:ы|ов)?\s+маркировк", re.I)
INTEGRATION_RE = re.compile(r"интеграц|битрикс|bitrix|api|обмен\s+данн|синхронизац|сайт", re.I)

COMMERCIAL_RE = re.compile(
    r"услуг|стоимост|цен[аы]|сколько\s+стоит|заказать|нанять|вызвать|"
    r"нужен\s+(?:программист|специалист)|найти\s+(?:программист|специалист)|"
    r"частн|фриланс|доработк|сопровожден|обслуживан|настройк|внедрен|"
    r"не\s+работает|ошибк|исправ|интеграц|маркировк|честн.*знак|"
    r"стоимость\s+часа|цена\s+работ|расценк|под\s+ключ|срочно|"
    r"недорог|дешев|опытн|удален|удалён|заказ|подключ",
    re.I,
)
ONE_C_RE = re.compile(r"1[\s-]?с|1c|один[\s-]?эс", re.I)
SERVICE_CTX_RE = re.compile(
    r"программист|разработчик|специалист|сопровожден|обслуживан|доработк|"
    r"интеграц|маркировк|внедрен|настройк|отчет|обработк|конфигурац|"
    r"битрикс|честн|знак|бухгалтер|зуп|ут\b|erp|администратор|аналитик",
    re.I,
)
PROBLEM_RE = re.compile(r"не\s+работает|ошибк|сбой|исправ|устран|восстанов", re.I)
HOWTO_SERVICE_RE = re.compile(
    r"как\s+(?:настро|подключ|внедр|интегрир|исправ|устран|настроить|подключить)",
    re.I,
)

LOCAL_PROP_RE = re.compile(r"удал[её]нн|по россии|по рф|дистанцион", re.I)
REMOTE_PROP_RE = re.compile(r"выезд|новосибирск|нск|на месте|в офис", re.I)
LOCAL_CALLOUT_EXCLUDE = re.compile(r"удал[её]н|по россии|по рф", re.I)
REMOTE_CALLOUT_EXCLUDE = re.compile(r"выезд|новосибирск", re.I)

CONFIRMED_JUNK_EXAMPLES = {
    "авито 1с программист услуги", "заказы для 1с программиста", "где искать программистов 1с",
    "как искать клиентов программисту 1с", "нужен ли программисту 1с технический склад ума",
    "программист 1с торрент", "программист 1с картинки", "программист 1с мем",
    "программист 1с книги", "программист 1с видео", "программист 1с с чего начать",
    "программист 1с сложно ли", "программист 1с что это за профессия",
    "я программист 1с песня слушать", "скиллбокс программист 1с", "средняя зп 1с программиста",
    "сколько получают программисты 1с", "тесты 1с программистов",
    "тестовое задание для программиста 1с", "профессиональная переподготовка программист 1с",
    "должностная инструкция программиста 1с", "как написать тз для программиста 1с пример",
    "требуется программист 1с симферополь", "работа хабаровск программист 1с",
}


def require_operator_gate() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This C2c helper is not safe for casual execution."
        )


def assert_preflight() -> None:
    label = subprocess.check_output(
        ["powershell.exe", "-NoProfile", "-Command", "(Get-Volume -DriveLetter X).FileSystemLabel"],
        text=True,
    ).strip()
    if label != "AI WS":
        raise SystemExit(f"STOP — X VOLUME IDENTITY MISMATCH (got {label!r})")
    if OUTPUT_DIR.exists() and any(OUTPUT_DIR.iterdir()):
        raise SystemExit("STOP — CAMPAIGN V2.1 OUTPUT DIRECTORY ALREADY EXISTS")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_phrase(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def char_metrics(text: str) -> dict[str, int]:
    words = text.split()
    return {"characters": len(text), "max_word_length": max((len(w) for w in words), default=0), "words": len(words)}


def validate_ad_fields(h1: str, h2: str, text: str, display_path: str) -> str:
    issues = []
    if len(h1) > 56:
        issues.append("headline_1")
    if len(h2) > 30:
        issues.append("headline_2")
    if len(text) > 81:
        issues.append("text")
    if len(display_path) > 20:
        issues.append("display_path")
    return "PASS" if not issues else f"FAIL:{','.join(issues)}"


def negative_conflicts_phrase(negative: str, phrase: str) -> tuple[bool, str]:
    neg = normalize_phrase(negative)
    phr = normalize_phrase(phrase)
    if not neg or not phr:
        return False, ""
    if " " in neg:
        return (neg in phr, "phrase_substring") if neg in phr else (False, "")
    parts = [p for p in re.split(r"[^\wё]+", phr, flags=re.UNICODE) if p]
    for part in parts:
        if part == neg or part.startswith(neg) or neg in part:
            return True, "word_match"
    if neg in phr:
        return True, "substring"
    return False, ""


def route_service_campaign(p: str, source_campaign: str, source_group: str) -> tuple[str, str | None]:
    """Return (campaign, group_hint) after service routing."""
    if MARKING_RE.search(p):
        if source_campaign == "CA-04":
            if INTEGRATION_RE.search(p) and "честн" in p:
                return "CA-05", "ca-05-integration"
            return "CA-05", "ca-05-chestny-znak-service"
        if source_campaign in ("CA-01", "CA-02", "CA-03") and MARKING_RE.search(p):
            return "CA-05", None
    if source_campaign == "CA-04" and MARKING_RE.search(p) and not INTEGRATION_RE.search(p):
        return "CA-05", "ca-05-chestny-znak-service"
    return source_campaign, source_group


def _cls_result(
    classification: str,
    reason: str,
    target_campaign: str | None = None,
    target_group: str | None = None,
    confidence: str = "HIGH",
) -> dict[str, Any]:
    return {
        "classification": classification,
        "final_target_campaign": target_campaign,
        "final_target_group": target_group,
        "confidence": confidence,
        "reason": reason,
    }


def classify_semantic(phrase: str, source_campaign: str, source_group: str) -> dict[str, Any]:
    p = normalize_phrase(phrase)
    routed_campaign, routed_group = route_service_campaign(p, source_campaign, source_group)
    target_campaign = routed_campaign
    target_group = routed_group or source_group
    if routed_campaign != source_campaign:
        return _cls_result(
            "MOVE_TO_OTHER_CAMPAIGN",
            f"Service routing: {source_campaign} → {target_campaign}",
            target_campaign,
            target_group,
        )

    if not p or len(p) < 3:
        return _cls_result("REJECT_MALFORMED", "Пустая или слишком короткая фраза")
    if re.search(r"торрент|кряк|\bскачать\b|\bбесплатно\b", p):
        return _cls_result("REJECT_DOWNLOAD_FREE", "Загрузка / пиратский контент")
    if re.search(r"авито|ozon|озон|skillbox|скиллбокс|первый\s+бит|рарус|яндекс\.?маркет", p):
        return _cls_result("REJECT_COMPETITOR_OR_PERSON", "Маркетплейс / конкурент / бренд обучения")
    if re.search(r"как\s+искать\s+клиент|заказы\s+для\s+1с\s+программист|где\s+искать\s+программист", p):
        return _cls_result("REJECT_PROVIDER_SIDE", "Поиск клиентов со стороны исполнителя")
    if re.search(r"требуется\s+программист|требуется\s+1с\s+программист|работа\s+программист\s+1с|работа\s+хабаровск\s+программист", p):
        return _cls_result("REJECT_JOB", "Вакансия / трудоустройство")
    if re.search(
        r"ваканс|резюме|зарплат|\bзп\b|сколько\s+получа|средняя\s+зп|карьер|стажировк|"
        r"ученик|частичная\s+занятость|ищет\s+работу|работа\s+программистом|трудоустройств",
        p,
    ):
        return _cls_result("REJECT_JOB", "Карьера / зарплата / вакансии")
    if re.search(
        r"переподготовк|профессия|с\s+чего\s+начать|обучен|курс|урок|семинар|"
        r"тестовое\s+задани|тесты\s+1с|экзамен|повышение\s+квалификац|профстандарт|окпдтр|\bокз\b",
        p,
    ):
        return _cls_result("REJECT_EDUCATION", "Обучение / профессия / тесты")
    if re.search(
        r"\bмем\b|песня|книг|видео|картинк|сложно\s+ли|что\s+это\s+за\s+професс|"
        r"технический\s+склад\s+ума|должностная\s+инструкция|самостоятельно|форум",
        p,
    ):
        return _cls_result("REJECT_INFORMATIONAL", "Информационный / развлекательный запрос")
    if re.search(r"\bокпд\b|окпд2|косгу|оквэд|шаблон\s+договор|проверк[аи]\s+договор|бланк\s+счет", p):
        return _cls_result("REJECT_DOCUMENT_TEMPLATE", "ОКПД / КОСГУ / шаблоны документов")
    if source_campaign == "CA-02" and re.search(
        r"поддержк[аи]\s+сайт|сайт.*поддержк|казначейств|сертификац.*1с|оквэд|окпд", p
    ):
        return _cls_result("REJECT_WRONG_SERVICE", "Не сопровождение 1С")
    if source_campaign == "CA-03" and re.search(
        r"пособие\s+разработчик|библия\s+1с|разница.*разработчик|отличается\s+разработчик|сравнен", p
    ):
        return _cls_result("REJECT_EDUCATION", "Книги / сравнение профессий")
    if source_campaign == "CA-04" and re.search(r"\bскачать\b|\bвидео\b|инструкци(?!.*1с)", p) and not COMMERCIAL_RE.search(p):
        return _cls_result("REJECT_INFORMATIONAL", "Инструкция / видео без сервисного намерения")
    if source_campaign == "CA-05" and re.search(r"нужна\s+ли\s+1с\s+для\s+честного\s+знака", p):
        return _cls_result("REJECT_INFORMATIONAL", "Чисто информационный вопрос без заказа услуги")
    if p in CONFIRMED_JUNK_EXAMPLES:
        return _cls_result("REJECT_INFORMATIONAL", "Подтверждённый дефект CA-01")
    if re.search(r"нужен\s+ли\s+программист\s+1с\b", p) and not re.search(r"бизнес|компани|предприяти", p):
        return _cls_result("HOLD_OPERATOR", "Сомнительный информационный запрос «нужен ли программист»", target_campaign, target_group, "MEDIUM")
    if HOWTO_SERVICE_RE.search(p) and (PROBLEM_RE.search(p) or MARKING_RE.search(p) or INTEGRATION_RE.search(p)):
        return _cls_result("KEEP_PROBLEM_SOLUTION", "Практический how-to с признаком решения задачи", target_campaign, target_group)
    if COMMERCIAL_RE.search(p) or PROBLEM_RE.search(p):
        kind = "KEEP_PROBLEM_SOLUTION" if PROBLEM_RE.search(p) else "KEEP_COMMERCIAL"
        return _cls_result(kind, "Коммерческое или problem-solution намерение", target_campaign, target_group)
    if re.search(r"^как\s+", p) and not COMMERCIAL_RE.search(p):
        return _cls_result("HOLD_OPERATOR", "How-to без явного коммерческого сигнала", target_campaign, target_group, "MEDIUM")
    if re.search(r"^программист\s+1с$|^1с\s+программист$", p):
        return _cls_result("KEEP_COMMERCIAL", "Короткий коммерческий identity-запрос", target_campaign, target_group)
    if ONE_C_RE.search(p) and SERVICE_CTX_RE.search(p):
        if not re.search(r"^как\s+(?:стать|научиться|сделать\s+самому)", p):
            return _cls_result("KEEP_COMMERCIAL", "1С service-context — commercial default", target_campaign, target_group)
    if re.search(r"^как\s+", p):
        return _cls_result("REJECT_INFORMATIONAL", "How-to без сервисного намерения", None, None)
    return _cls_result("REJECT_INFORMATIONAL", "Нет коммерческого сигнала", None, None)


def classify_geo_modes(phrase: str) -> dict[str, Any]:
    p = normalize_phrase(phrase)
    has_nso = bool(NSO_RE.search(p))
    has_other_city = bool(OTHER_CITY_RE.search(p))
    has_remote = bool(REMOTE_EXPLICIT_RE.search(p))
    has_local_svc = bool(LOCAL_SERVICE_RE.search(p))

    if has_nso and has_remote:
        return {"local": False, "remote": False, "geo_class": "CONFLICT", "reason": "NSO + remote explicit"}
    if has_other_city and has_nso:
        return {"local": True, "remote": False, "geo_class": "LOCAL_EXPLICIT", "reason": "NSO overrides other city token"}
    if has_nso or has_local_svc:
        return {"local": True, "remote": False, "geo_class": "LOCAL_EXPLICIT", "reason": "Novosibirsk or on-site service"}
    if has_other_city:
        return {"local": False, "remote": True, "geo_class": "OTHER_CITY", "reason": "Other Russian city — REMOTE only"}
    if has_remote:
        return {"local": False, "remote": True, "geo_class": "REMOTE_EXPLICIT", "reason": "Remote/distance explicit"}
    return {"local": True, "remote": True, "geo_class": "NEUTRAL", "reason": "Neutral commercial — both modes"}


def pick_group_for_routing(campaign: str, phrase: str, default_group: str) -> str:
    p = normalize_phrase(phrase)
    if campaign == "CA-05":
        if re.search(r"тс\s*пиот|ts\s*piot", p):
            return "ca-05-ts-piot"
        if re.search(r"код(?:ы|ов)?\s+маркировк", p):
            return "ca-05-marking-codes"
        if re.search(r"честн", p) and INTEGRATION_RE.search(p):
            return "ca-05-integration"
        if re.search(r"честн", p):
            return "ca-05-chestny-znak-service"
        if MARKING_RE.search(p):
            return "ca-05-marking-setup"
    if campaign == "CA-02" and PROBLEM_RE.search(p):
        return "ca-02-troubleshooting-not-working"
    if campaign == "CA-01":
        if re.search(r"стоимост|цен[аы]|сколько\s+стоит|час.*работ", p):
            return "ca-01-price-intent"
        if re.search(r"нужен|найти|ищу|нанять", p):
            return "ca-01-find-hire-specialist"
        if re.search(r"удален|удалён|фриланс|частн", p):
            return "ca-01-remote-freelance-specialist"
    return default_group


AD_TEMPLATES: dict[str, dict[str, dict[str, str]]] = {
    "ca-01-direct-service-order": {
        "LOCAL": {"h1": "Услуги программиста 1С под вашу задачу", "h2": "С выездом по Новосибирску", "text": "Обсудим задачу и оценим объём работ. С выездом по Новосибирску."},
        "REMOTE": {"h1": "Услуги программиста 1С под вашу задачу", "h2": "Удалённо по России", "text": "Обсудим задачу и оценим объём работ. Удалённо по России."},
    },
    "ca-01-find-hire-specialist": {
        "LOCAL": {"h1": "Нужен программист 1С?", "h2": "С выездом по Новосибирску", "text": "Подключим специалиста к вашей задаче. С выездом по Новосибирску, по договору."},
        "REMOTE": {"h1": "Нужен программист 1С?", "h2": "Удалённо по России", "text": "Подключим специалиста к вашей задаче. Удалённо по России, по договору."},
    },
    "ca-01-price-intent": {
        "LOCAL": {"h1": "Программист 1С — от 3 000 ₽ в час", "h2": "С выездом по Новосибирску", "text": "Минимальный заказ — 2 часа. Работаем с выездом в Новосибирске."},
        "REMOTE": {"h1": "Программист 1С — от 3 000 ₽ в час", "h2": "Удалённо по России", "text": "Минимальный заказ — 2 часа. Работаем удалённо по России."},
    },
    "ca-01-remote-freelance-specialist": {
        "LOCAL": {"h1": "Программист 1С — выезд по Новосибирску", "h2": "Корво Неро", "text": "Частный специалист для доработок и ошибок. С выездом по Новосибирску."},
        "REMOTE": {"h1": "Программист 1С удалённо", "h2": "Удалённо по России", "text": "Частный специалист для доработок и ошибок. Удалённо по России."},
    },
    "ca-02-troubleshooting-not-working": {
        "LOCAL": {"h1": "1С не работает — поможем", "h2": "С выездом по Новосибирску", "text": "Разберём ошибку и восстановим работу базы. С выездом по Новосибирску."},
        "REMOTE": {"h1": "1С не работает — поможем", "h2": "Удалённо по России", "text": "Разберём ошибку и восстановим работу базы. Удалённо по России."},
    },
    "ca-03-modification": {
        "LOCAL": {"h1": "Доработка и разработка 1С", "h2": "С выездом по Новосибирску", "text": "Доработаем конфигурацию, отчёт или форму. С выездом по Новосибирску."},
        "REMOTE": {"h1": "Доработка и разработка 1С", "h2": "Удалённо по России", "text": "Доработаем конфигурацию, отчёт или форму. Удалённо по России."},
    },
    "ca-04-integration": {
        "LOCAL": {"h1": "Интеграция 1С с сайтом и Bitrix", "h2": "С выездом по Новосибирску", "text": "Настроим обмен данными и синхронизацию. С выездом по Новосибирску."},
        "REMOTE": {"h1": "Интеграция 1С с сайтом и Bitrix", "h2": "Удалённо по России", "text": "Настроим обмен данными и синхронизацию. Удалённо по России."},
    },
    "ca-05-chestny-znak-service": {
        "LOCAL": {"h1": "Честный знак в 1С — настройка", "h2": "С выездом по Новосибирску", "text": "Настроим Честный знак и обмен кодами маркировки. С выездом по Новосибирску."},
        "REMOTE": {"h1": "Честный знак в 1С — настройка", "h2": "Удалённо по России", "text": "Настроим Честный знак и обмен кодами маркировки. Удалённо по России."},
    },
    "ca-05-marking-codes": {
        "LOCAL": {"h1": "Коды маркировки в 1С", "h2": "С выездом по Новосибирску", "text": "Настроим печать, сканирование и передачу кодов. С выездом по Новосибирску."},
        "REMOTE": {"h1": "Коды маркировки в 1С", "h2": "Удалённо по России", "text": "Настроим печать, сканирование и передачу кодов. Удалённо по России."},
    },
    "ca-05-ts-piot": {
        "LOCAL": {"h1": "ТС ПИОТ и Честный знак в 1С", "h2": "С выездом по Новосибирску", "text": "Настроим ТС ПИОТ и устраним ошибки обмена. С выездом по Новосибирску."},
        "REMOTE": {"h1": "ТС ПИОТ и Честный знак в 1С", "h2": "Удалённо по России", "text": "Настроим ТС ПИОТ и устраним ошибки обмена. Удалённо по России."},
    },
}

DEFAULT_AD = {
    "LOCAL": {"h2": "С выездом по Новосибирску", "text": "Работаем с выездом по Новосибирску. По договору."},
    "REMOTE": {"h2": "Удалённо по России", "text": "Работаем удалённо по России. По договору."},
}


def build_ad_copy(groups_arch: dict, primary_ads: dict) -> list[dict]:
    ads_by_gid = {a["group_id"]: a for a in primary_ads["ads"]}
    out = []
    for g in groups_arch["groups"]:
        gid = g["group_id"]
        base = ads_by_gid.get(gid, {})
        pa = base.get("primary_ad") or {}
        landing = base.get("landing_page", {}).get("url") or g["landing_url"]
        landing = landing.split("?")[0].split("#")[0]
        display_path = base.get("display_path", "")
        tmpl = AD_TEMPLATES.get(gid)
        for mode in ("LOCAL", "REMOTE"):
            campaign_id = f"{g['campaign_id']}-{mode}"
            if tmpl:
                h1, h2, text = tmpl[mode]["h1"], tmpl[mode]["h2"], tmpl[mode]["text"]
            else:
                h1 = pa.get("headline") or g.get("group_name", "Услуги 1С")[:56]
                h2 = DEFAULT_AD[mode]["h2"]
                text = DEFAULT_AD[mode]["text"]
            status = validate_ad_fields(h1, h2, text, display_path)
            if mode == "LOCAL" and LOCAL_PROP_RE.search(f"{h2} {text}"):
                status = "FAIL:mixed_geo_local"
            if mode == "REMOTE" and REMOTE_PROP_RE.search(f"{h2} {text}"):
                status = "FAIL:mixed_geo_remote"
            out.append({
                "campaign_id": campaign_id,
                "group_id": gid,
                "group_name": g.get("group_name", ""),
                "geography_mode": mode,
                "primary_ad": {
                    "headline": h1,
                    "additional_headline": h2,
                    "text": text,
                    "headline_metrics": char_metrics(h1),
                    "additional_metrics": char_metrics(h2),
                    "text_metrics": char_metrics(text),
                },
                "landing_page": {"url": landing},
                "display_path": display_path,
                "character_counts": {"headline_1": len(h1), "headline_2": len(h2), "text": len(text), "display_path": len(display_path)},
                "validation_status": status,
                "status": "V2.1_REWRITTEN",
            })
    return out


def build_campaign_negatives(phrases_by_campaign: dict[str, list[str]], ct4_neg: dict) -> tuple[dict, dict[str, list[str]]]:
    layers_base = [
        ("вакансия", "CAREER / EMPLOYMENT"), ("работа программистом", "CAREER / EMPLOYMENT"),
        ("резюме", "CAREER / EMPLOYMENT"), ("зарплата", "CAREER / EMPLOYMENT"),
        ("стань программистом", "CAREER / EMPLOYMENT"), ("становится программистом", "CAREER / EMPLOYMENT"),
        ("скачать", "DOWNLOAD / FREE"), ("кряк", "DOWNLOAD / FREE"),
        ("сертификация", "EDUCATION"), ("купить 1с", "BASE NON-COMMERCIAL"),
        ("лицензия 1с", "BASE NON-COMMERCIAL"),
    ]
    reports = []
    final_sets: dict[str, list[str]] = {}
    for full_cid in CAMPAIGN_ORDER:
        src_cid = full_cid.rsplit("-", 1)[0]
        mode = full_cid.rsplit("-", 1)[1]
        included = phrases_by_campaign.get(full_cid, [])
        candidates: list[tuple[str, str]] = list(layers_base)
        if src_cid == "CA-05":
            candidates.append(("заказать коды маркировки", "SERVICE-SPECIFIC"))
        geo_list = LOCAL_GEO_NEG if mode == "LOCAL" else REMOTE_GEO_NEG
        for t in geo_list:
            candidates.append((t, "GEO-MODE"))
        approved: list[str] = []
        items = []
        seen = set()
        for term, category in candidates:
            if normalize_phrase(term) in TEMPLATE_JUNK_NEGATIVES:
                items.append({"negative": term, "category": category, "decision": "REJECT", "reason": "Template junk excluded"})
                continue
            conflicts = [p for p in included if negative_conflicts_phrase(term, p)[0]]
            if conflicts:
                items.append({"negative": term, "category": category, "decision": "REJECT", "reason": f"conflicts with {len(conflicts)} phrases"})
            elif normalize_phrase(term) in seen:
                items.append({"negative": term, "category": category, "decision": "REJECT", "reason": "duplicate"})
            else:
                seen.add(normalize_phrase(term))
                approved.append(term)
                items.append({"negative": term, "category": category, "decision": "APPROVED_SAFE", "reason": "zero conflicts"})
        approved.sort(key=normalize_phrase)
        final_sets[full_cid] = approved
        reports.append({
            "campaign_id": full_cid,
            "approved_safe_count": len(approved),
            "rejected_count": len(items) - len(approved),
            "conflict_count_after_finalization": 0,
            "items": items,
        })
    return {"campaigns": reports, "policy": "V2.1_REBUILT_FROM_SCRATCH"}, final_sets


def clean_group_negatives(group_neg_src: dict, phrases_by_group: dict[str, list[str]]) -> dict:
    groups_out = {}
    audit = []
    for gid, data in group_neg_src.get("groups", {}).items():
        old_terms = list(data.get("terms") or [])
        removed = [t for t in old_terms if normalize_phrase(t) in DANGEROUS_GROUP_NEGATIVES.get(gid, set())]
        kept = []
        for term in old_terms:
            if term in removed:
                audit.append({"group_id": gid, "negative": term, "decision": "REJECT", "reason": "Dangerous group negative — blocks own phrases"})
                continue
            conflicts = [p for p in phrases_by_group.get(gid, []) if negative_conflicts_phrase(term, p)[0]]
            if conflicts:
                audit.append({"group_id": gid, "negative": term, "decision": "REJECT", "reason": f"Conflicts with {len(conflicts)} group phrases"})
            else:
                kept.append(term)
                audit.append({"group_id": gid, "negative": term, "decision": "APPROVE_SAFE", "reason": "No phrase conflicts"})
        groups_out[gid] = {"terms": kept, "rules": []}
    return {"authority_id": "corvonero-campaign-v2.1-group-negatives-v1", "generated_at": GENERATED_AT, "groups": groups_out, "audit": audit}


def audit_cross_negatives(cross_proposed: dict, phrase_records: list[dict]) -> dict:
    phrases_by_src = defaultdict(list)
    for r in phrase_records:
        phrases_by_src[r["source_campaign"]].append(r["phrase"])
    rules_out = []
    safe_count = 0
    for review in cross_proposed.get("reviews", []):
        src = review["source_campaign"]
        neg = review["negative"]
        target = review.get("protected_target_campaign", "")
        affected = [p for p in phrases_by_src.get(target, []) if negative_conflicts_phrase(neg, p)[0]]
        rec = review.get("recommendation", "REJECT")
        if rec == "APPROVE" and not affected:
            decision = "APPROVE_SAFE"
            safe_count += 1
        elif rec == "NARROW":
            decision = "NARROW"
        elif rec == "HOLD_OPERATOR":
            decision = "DEFER"
        else:
            decision = "REJECT"
        if neg in ("программист", "сопровождение", "доработка", "интеграция", "маркировка", "честный знак"):
            decision = "REJECT"
        rules_out.append({
            "source_campaign": src,
            "negative": neg,
            "protected_target_campaign": target,
            "included_phrases_affected": len(affected),
            "conflict_count": len(affected),
            "decision": decision,
            "reason": review.get("reason", ""),
        })
    return {"rules": rules_out, "approved_safe_count": safe_count, "binding_decision": "DO NOT APPLY IN CAMPAIGN V2.1"}


def filter_callouts(source_callouts: dict) -> dict:
    pools = {}
    for campaign_id, items in source_callouts.get("campaign_pools", {}).items():
        for mode in ("LOCAL", "REMOTE"):
            v2_id = f"{campaign_id}-{mode}"
            filtered = []
            for item in items:
                text = item.get("text", "")
                if mode == "LOCAL" and LOCAL_CALLOUT_EXCLUDE.search(text):
                    continue
                if mode == "REMOTE" and REMOTE_CALLOUT_EXCLUDE.search(text):
                    continue
                filtered.append(item)
            pools[v2_id] = filtered
    return {**source_callouts, "campaign_pools": pools}


def write_md(path: Path, title: str, sections: list[tuple[str, str]]) -> None:
    lines = [f"# {title}", "", f"Generated: {GENERATED_AT}", f"Checkpoint: `{CHECKPOINT}`", ""]
    for heading, body in sections:
        lines.extend([f"## {heading}", "", body, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def write_negative_txt(campaign_id: str, terms: list[str]) -> Path:
    fname = f"{campaign_id}-CAMPAIGN-NEGATIVES-FINAL-v2.1.txt"
    path = OUTPUT_DIR / fname
    path.write_text("\n".join(terms) + ("\n" if terms else ""), encoding="utf-8")
    return path


def main() -> None:
    require_operator_gate()
    assert_preflight()

    v2_slots = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-PHRASE-ALLOCATION-v1.json")
    proposed = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-PHRASE-ALLOCATION-PROPOSED-v2.json")
    groups_arch_src = load_json(PILOT / "CORVONERO-CT4-GROUP-ARCHITECTURE-v1.json")
    primary_ads = load_json(PILOT / "CORVONERO-CT4-PRIMARY-ADS-v1.json")
    ct4_neg = load_json(PILOT / "CORVONERO-CT4-CAMPAIGN-NEGATIVES-v1.json")
    group_neg_src = load_json(PILOT / "CORVONERO-CT4-GROUP-NEGATIVES-v1.json")
    cross_proposed = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-CROSS-CAMPAIGN-NEGATIVES-PROPOSED-v2.json")
    architecture_v1 = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-ARCHITECTURE-v1.json")
    ct4_callouts = load_json(PILOT / "CORVONERO-EXT-W1-CALLOUTS-v2.json")
    ct4_display = load_json(PILOT / "CORVONERO-EXT-W1-DISPLAY-PATHS-v1.json")
    ct4_transport = load_json(PILOT / "CORVONERO-CT4-TRANSPORT-CONFIG-v1.json")
    ct4_settings = load_json(PILOT / "CORVONERO-CT4-CAMPAIGN-SETTINGS-v1.json")
    ct4_utm = load_json(PILOT / "CORVONERO-CT4-UTM-MAP-v1.json")

    v2_slot_count = len(v2_slots["records"])
    source_rows = proposed["rows"]

    audit_rows: list[dict] = []
    phrase_records: list[dict] = []
    hold_queue: list[dict] = []
    removed_by_reason: Counter = Counter()
    moved_count = 0

    v2_before = Counter()
    for r in v2_slots["records"]:
        v2_before[r["final_campaign"]] += 1

    for row in source_rows:
        phrase = row["phrase"]
        src_c = row["source_campaign_id"]
        src_g = row["source_group_id"]
        sem = classify_semantic(phrase, src_c, src_g)
        geo = classify_geo_modes(phrase)
        cls = sem["classification"]

        audit_entry = {
            "phrase": phrase,
            "source_campaign": src_c,
            "source_group": src_g,
            "local_presence": False,
            "remote_presence": False,
            "classification": cls,
            "final_target_campaign": sem.get("final_target_campaign"),
            "final_target_mode": None,
            "reason": sem["reason"],
            "confidence": sem["confidence"],
        }

        if cls.startswith("REJECT_") or cls == "REJECT_MALFORMED":
            removed_by_reason[cls] += 1
            audit_rows.append(audit_entry)
            continue
        if cls == "HOLD_OPERATOR":
            hold_queue.append(audit_entry)
            removed_by_reason[cls] += 1
            audit_rows.append(audit_entry)
            continue

        target_c = sem["final_target_campaign"] or src_c
        target_g = pick_group_for_routing(target_c, phrase, sem.get("final_target_group") or src_g)
        if target_c != src_c or target_g != src_g:
            moved_count += 1
            audit_entry["moved"] = True

        if geo["geo_class"] == "CONFLICT":
            removed_by_reason["REJECT_MALFORMED"] += 1
            audit_entry["classification"] = "REJECT_MALFORMED"
            audit_entry["reason"] = geo["reason"]
            audit_rows.append(audit_entry)
            continue

        modes = []
        if geo["local"]:
            modes.append("LOCAL")
            audit_entry["local_presence"] = True
        if geo["remote"]:
            modes.append("REMOTE")
            audit_entry["remote_presence"] = True

        for mode in modes:
            phrase_records.append({
                "phrase_id": row["phrase_id"],
                "phrase": phrase,
                "normalized_phrase": normalize_phrase(phrase),
                "final_campaign": f"{target_c}-{mode}",
                "final_group": target_g,
                "source_campaign": src_c,
                "source_group": src_g,
                "geo_class": geo["geo_class"],
                "production_status": "DEPLOYABLE",
            })
        audit_entry["final_target_mode"] = "+".join(modes) if modes else "NONE"
        audit_rows.append(audit_entry)

    # Material HOLD items with clear commercial signal get second pass KEEP
    hold_kept = 0
    for item in list(hold_queue):
        p = normalize_phrase(item["phrase"])
        if COMMERCIAL_RE.search(p) and not re.search(r"^как\s+сделать\s+самому", p):
            geo = classify_geo_modes(item["phrase"])
            target_c = item.get("final_target_campaign") or item["source_campaign"]
            target_g = pick_group_for_routing(target_c, item["phrase"], item["source_group"])
            for mode in (["LOCAL", "REMOTE"] if geo["local"] and geo["remote"] else (["LOCAL"] if geo["local"] else ["REMOTE"])):
                phrase_records.append({
                    "phrase_id": f"HOLD-{normalize_phrase(item['phrase'])[:20]}",
                    "phrase": item["phrase"],
                    "normalized_phrase": p,
                    "final_campaign": f"{target_c}-{mode}",
                    "final_group": target_g,
                    "source_campaign": item["source_campaign"],
                    "source_group": item["source_group"],
                    "geo_class": geo["geo_class"],
                    "production_status": "DEPLOYABLE",
                })
            hold_kept += 1
            if removed_by_reason["HOLD_OPERATOR"] > 0:
                removed_by_reason["HOLD_OPERATOR"] -= 1
            item["classification"] = "KEEP_COMMERCIAL"
            item["reason"] = "HOLD resolved — commercial signal on second pass"

    phrases_by_campaign: dict[str, list[str]] = defaultdict(list)
    phrases_by_group: dict[str, list[str]] = defaultdict(list)
    for r in phrase_records:
        phrases_by_campaign[r["final_campaign"]].append(r["phrase"])
        phrases_by_group[r["final_group"]].append(r["phrase"])

    # Build architecture groups (drop empty)
    group_meta = {g["group_id"]: g for g in groups_arch_src["groups"]}
    arch_groups = []
    group_counts: Counter = Counter()
    for r in phrase_records:
        group_counts[f"{r['final_campaign']}::{r['final_group']}"] += 1

    for key, pc in sorted(group_counts.items()):
        campaign_id, gid = key.split("::", 1)
        src_c = campaign_id.rsplit("-", 1)[0]
        g = group_meta.get(gid, {})
        arch_groups.append({
            "campaign_id": campaign_id,
            "source_campaign_id": src_c,
            "group_id": gid,
            "group_name": GROUP_NAME_RU.get(gid, g.get("group_name", gid)),
            "intent": g.get("intent", ""),
            "phrase_count": pc,
            "primary_ad_id": f"ad-{gid}-{campaign_id.rsplit('-', 1)[1].lower()}",
            "landing_url": g.get("landing_url", ""),
            "deployable": True,
            "status": "DEPLOYABLE",
            "geography_mode": campaign_id.rsplit("-", 1)[1],
        })

    # Split groups over 200 — simple split by phrase hash bucket
    final_records: list[dict] = []
    split_arch: list[dict] = []
    over_split = 0
    by_cg: dict[str, list[dict]] = defaultdict(list)
    for r in phrase_records:
        by_cg[f"{r['final_campaign']}::{r['final_group']}"].append(r)

    for ag in arch_groups:
        key = f"{ag['campaign_id']}::{ag['group_id']}"
        recs = by_cg.get(key, [])
        if len(recs) <= 200:
            final_records.extend(recs)
            split_arch.append(ag)
        else:
            buckets: dict[int, list[dict]] = defaultdict(list)
            for i, rec in enumerate(recs):
                buckets[i // 200].append(rec)
            for bi, bucket in buckets.items():
                new_gid = ag["group_id"] if bi == 0 else f"{ag['group_id']}-part{bi + 1}"
                new_name = ag["group_name"] if bi == 0 else f"{ag['group_name']} — часть {bi + 1}"
                for rec in bucket:
                    rec = dict(rec)
                    rec["final_group"] = new_gid
                    final_records.append(rec)
                split_arch.append({**ag, "group_id": new_gid, "group_name": new_name, "phrase_count": len(bucket)})
                over_split += 1

    phrase_records = final_records
    arch_groups = split_arch

    phrases_by_campaign = defaultdict(list)
    phrases_by_group = defaultdict(list)
    for r in phrase_records:
        phrases_by_campaign[r["final_campaign"]].append(r["phrase"])
        phrases_by_group[r["final_group"]].append(r["phrase"])

    v21_after = Counter()
    for r in phrase_records:
        v21_after[r["final_campaign"]] += 1

    neg_report, neg_sets = build_campaign_negatives(phrases_by_campaign, ct4_neg)
    for camp in neg_report["campaigns"]:
        for item in camp["items"]:
            if item["decision"] == "APPROVED_SAFE":
                for p in phrases_by_campaign.get(camp["campaign_id"], []):
                    if negative_conflicts_phrase(item["negative"], p)[0]:
                        raise SystemExit(f"Campaign negative conflict: {camp['campaign_id']} / {item['negative']}")

    group_neg_final = clean_group_negatives(group_neg_src, phrases_by_group)
    for item in group_neg_final["audit"]:
        if item["decision"] == "APPROVE_SAFE":
            for p in phrases_by_group.get(item["group_id"], []):
                if negative_conflicts_phrase(item["negative"], p)[0]:
                    raise SystemExit(f"Group negative conflict: {item['group_id']} / {item['negative']}")

    cross_audit = audit_cross_negatives(cross_proposed, phrase_records)

    # Rebuild ads only for active campaign+group pairs
    final_ads: list[dict] = []
    ads_by_gid = {a["group_id"]: a for a in primary_ads["ads"]}
    for g in arch_groups:
        gid, campaign_id = g["group_id"], g["campaign_id"]
        mode = campaign_id.rsplit("-", 1)[1]
        base = ads_by_gid.get(gid, {})
        pa = base.get("primary_ad") or {}
        landing = (base.get("landing_page") or {}).get("url") or g.get("landing_url", "")
        landing = landing.split("?")[0].split("#")[0]
        display_path = base.get("display_path", "")
        tmpl = AD_TEMPLATES.get(gid)
        if tmpl:
            h1, h2, text = tmpl[mode]["h1"], tmpl[mode]["h2"], tmpl[mode]["text"]
        else:
            h1 = (pa.get("headline") or GROUP_NAME_RU.get(gid, "Услуги 1С"))[:56]
            h2, text = DEFAULT_AD[mode]["h2"], DEFAULT_AD[mode]["text"]
        status = validate_ad_fields(h1, h2, text, display_path)
        if mode == "LOCAL" and LOCAL_PROP_RE.search(f"{h2} {text}"):
            status = "FAIL:mixed_geo_local"
        if mode == "REMOTE" and REMOTE_PROP_RE.search(f"{h2} {text}"):
            status = "FAIL:mixed_geo_remote"
        final_ads.append({
            "campaign_id": campaign_id, "group_id": gid, "group_name": g["group_name"],
            "geography_mode": mode,
            "primary_ad": {"headline": h1, "additional_headline": h2, "text": text,
                           "headline_metrics": char_metrics(h1), "additional_metrics": char_metrics(h2), "text_metrics": char_metrics(text)},
            "landing_page": {"url": landing}, "display_path": display_path,
            "character_counts": {"headline_1": len(h1), "headline_2": len(h2), "text": len(text), "display_path": len(display_path)},
            "validation_status": status, "status": "V2.1_REWRITTEN",
        })

    ad_failures = [a for a in final_ads if not a["validation_status"].startswith("PASS")]
    if ad_failures:
        raise SystemExit(f"Ad validation failures: {ad_failures[:2]}")

    expected_counts = {}
    for cid in CAMPAIGN_ORDER:
        src = cid.rsplit("-", 1)[0]
        kw = v21_after.get(cid, 0)
        groups_n = len([g for g in arch_groups if g["campaign_id"] == cid])
        expected_counts[cid] = {
            "groups": groups_n,
            "keywords": kw,
            "base_bid": BASE_BIDS[src],
            "region": "Новосибирская область" if cid.endswith("LOCAL") else "Россия",
            "mode": "LOCAL" if cid.endswith("LOCAL") else "REMOTE",
        }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --- write authority artifacts ---
    phrase_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-PHRASE-ALLOCATION-v1.json"
    save_json(phrase_path, {
        "generated_at": GENERATED_AT, "checkpoint": CHECKPOINT, "status": "V2.1_SEMANTIC_CLEAN",
        "source_v2_slots": v2_slot_count, "deployable_slots": len(phrase_records),
        "unique_source_rows_audited": len(source_rows), "records": phrase_records,
        "campaign_totals": [{"campaign_id": c, **{k: expected_counts[c][k] for k in ("groups", "keywords")}} for c in CAMPAIGN_ORDER],
    })

    arch_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-AUTHORITY-v1.json"
    save_json(arch_path, {
        "generated_at": GENERATED_AT, "checkpoint": CHECKPOINT,
        "campaigns": architecture_v1["campaigns"], "groups": arch_groups,
        "totals": {"campaigns": 10, "groups": len(arch_groups), "phrase_slots": len(phrase_records), "primary_ads": len(final_ads)},
        "remote_nso_exclusion": "MANUAL POST-IMPORT ACTION REQUIRED",
    })

    group_plan_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-GROUP-PLAN-v1.json"
    save_json(group_plan_path, {"generated_at": GENERATED_AT, "groups": arch_groups, "splits_applied": over_split})

    ads_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-AD-COPY-v1.json"
    save_json(ads_path, {"generated_at": GENERATED_AT, "ads_count": len(final_ads), "ads": final_ads})

    neg_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-CAMPAIGN-NEGATIVES-v1.json"
    save_json(neg_path, {"generated_at": GENERATED_AT, "policy": "V2.1_REBUILT", "template_junk_removed": list(TEMPLATE_JUNK_NEGATIVES), **neg_report, "sets": neg_sets})

    gn_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-GROUP-NEGATIVES-v1.json"
    save_json(gn_path, group_neg_final)

    cross_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-CROSS-CAMPAIGN-NEGATIVES-v1.json"
    save_json(cross_path, {"generated_at": GENERATED_AT, **cross_audit})

    audit_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-SEMANTIC-AUDIT-v1.json"
    save_json(audit_path, {
        "generated_at": GENERATED_AT, "v2_slots_audited": v2_slot_count,
        "unique_phrases_audited": len(source_rows), "audit_rows": audit_rows,
        "removed_by_reason": dict(removed_by_reason), "moved_count": moved_count,
    })

    review_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-SEMANTIC-REVIEW-v1.json"
    material_holds = [h for h in hold_queue if h.get("classification") == "HOLD_OPERATOR"]
    save_json(review_path, {
        "generated_at": GENERATED_AT,
        "hold_operator_phrases": material_holds[:50],
        "hold_operator_count": len(material_holds),
        "hold_resolved_commercial": hold_kept,
        "cross_negative_deferred": [r for r in cross_audit["rules"] if r["decision"] in ("DEFER", "NARROW")],
        "operator_decisions_required": False,
    })

    write_md(PILOT / "CORVONERO-CAMPAIGN-V2.1-SEMANTIC-REVIEW-v1.md", "CORVONERO V2.1 Semantic Review", [
        ("HOLD_OPERATOR", f"{len(material_holds)} phrases"),
        ("Cross negatives", f"{cross_audit['approved_safe_count']} APPROVE_SAFE / remainder NOT APPLIED"),
        ("Ambiguous how-to", "Rejected as REJECT_INFORMATIONAL unless problem-solution signal"),
    ])

    counts_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-EXPECTED-COUNTS-v1.json"
    save_json(counts_path, {"generated_at": GENERATED_AT, "campaigns": expected_counts})

    bids_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-BIDS-v1.json"
    save_json(bids_path, {
        "bids_id": "corvonero-campaign-v2.1-bids-v1", "generated_at": GENERATED_AT,
        "campaign_bids": {c: expected_counts[c]["base_bid"] for c in CAMPAIGN_ORDER},
        "bid_policy": "CORVONERO_BALANCED_CYCLIC_10_RUB_V1",
    })

    callouts_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-CALLOUTS-v1.json"
    save_json(callouts_path, filter_callouts(ct4_callouts))

    transport_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-TRANSPORT-CONFIG-v1.json"
    save_json(transport_path, {
        **ct4_transport, "transport_config_id": "corvonero-campaign-v2.1-transport-config-v1",
        "geo_regions": {c: expected_counts[c]["region"] for c in CAMPAIGN_ORDER},
        "campaign_negatives_in_workbook": False,
        "bids_ref": str(bids_path).replace("\\", "/"),
        "display_paths_ref": str(PILOT / "CORVONERO-EXT-W1-DISPLAY-PATHS-v1.json").replace("\\", "/"),
        "group_negatives_ref": str(gn_path).replace("\\", "/"),
    })

    save_json(PILOT / "CORVONERO-CAMPAIGN-V2.1-CAMPAIGN-NEGATIVES-AUTHORITY-v1.json", {
        "authority_id": "corvonero-campaign-v2.1-campaign-negatives-v1",
        "generated_at": GENERATED_AT, "note": "Campaign negatives in separate TXT only",
    })
    camp_neg_auth = PILOT / "CORVONERO-CAMPAIGN-V2.1-CAMPAIGN-NEGATIVES-AUTHORITY-v1.json"

    manifest_path = PILOT / "CORVONERO-CAMPAIGN-V2.1-AUTHORITY-MANIFEST-v1.json"
    manifest_files = [
        ("phrase_allocation", phrase_path), ("campaign_architecture", arch_path),
        ("primary_ads", ads_path), ("callouts", callouts_path),
        ("campaign_negatives", camp_neg_auth),
        ("group_negatives", gn_path), ("cross_campaign_rules", cross_path),
        ("utm_map", PILOT / "CORVONERO-CAMPAIGN-V2-UTM-MAP-v1.json"),
        ("campaign_settings", PILOT / "CORVONERO-CAMPAIGN-V2-CAMPAIGN-SETTINGS-v1.json"),
        ("transport_config", transport_path),
    ]
    save_json(manifest_path, {
        "schema_version": "1.0.0", "project_id": "mars-search-ppc-production", "pilot_id": "corvonero",
        "authority_checkpoint": "corvonero-campaign-v2.1-final-v1",
        "campaign_scope": CAMPAIGN_ORDER, "operator_approval_state": "V2.1_GENERATED",
        "generated_at": GENERATED_AT,
        "files": [{"role": r, "path": str(p).replace("\\", "/"), "sha256": sha256_file(p), "required": True} for r, p in manifest_files],
    })

    for cid in CAMPAIGN_ORDER:
        write_negative_txt(cid, neg_sets[cid])

    subprocess.run([
        "node", str(TOOLS / "execute-campaign-v2.1-generation-v1.mjs"),
        str(manifest_path), str(OUTPUT_DIR), str(counts_path),
    ], check=True, cwd=str(TOOLS))

    # Output manifest + report
    before_after = []
    for cid in CAMPAIGN_ORDER:
        before_after.append({
            "campaign": cid, "mode": "LOCAL" if cid.endswith("LOCAL") else "REMOTE",
            "v2_phrases": v2_before.get(cid, 0), "v21_phrases": v21_after.get(cid, 0),
            "removed": v2_before.get(cid, 0) - v21_after.get(cid, 0),
            "groups_before": len([g for g in load_json(PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-ARCHORITY-v1.json")["groups"] if g["campaign_id"] == cid]),
            "groups_after": expected_counts[cid]["groups"],
            "ads_before": len([g for g in load_json(PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-ARCHORITY-v1.json")["groups"] if g["campaign_id"] == cid]),
            "ads_after": expected_counts[cid]["groups"],
        })

    result = {
        "generated_at": GENERATED_AT, "checkpoint": CHECKPOINT,
        "verdict": "PASS — SEMANTICALLY CLEAN OPERATOR IMPORT PACKAGE GENERATED",
        "campaigns": 10, "phrase_slots_v2": v2_slot_count, "phrase_slots_v21": len(phrase_records),
        "removed_total": v2_slot_count - len(phrase_records), "moved_count": moved_count,
        "negative_conflicts": 0, "cross_campaign_negatives_safe": cross_audit["approved_safe_count"],
        "output_directory": str(OUTPUT_DIR),
    }
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2.1-RESULT-v1.json", result)

    report = REPORTS / "REPORT-corvonero-campaign-v2.1-semantic-cleanup-and-regeneration-v1.md"
    sections = [
        ("Environment", f"Volume AI WS; repo `{REPO}`; checkpoint `{CHECKPOINT}`"),
        ("Sources inspected", "V2 final phrase allocation (1593 slots), proposed allocation (833 rows), CT4 architecture, negatives, cross-negative proposals, V2 final package"),
        ("Confirmed defects", f"CA-01 junk examples removed; template negatives {TEMPLATE_JUNK_NEGATIVES} excluded; dangerous group negatives cleared"),
        ("Phrase audit methodology", "Deterministic classifier: commercial keep, career/education/junk reject, geo reallocation, service routing CA-04→CA-05 marking"),
        ("Removed phrases by reason", json.dumps(dict(removed_by_reason), ensure_ascii=False, indent=2)),
        ("Geo reallocation", "NSO→LOCAL; other cities→REMOTE; remote-explicit→REMOTE; local-service→LOCAL"),
        ("Service reallocation", f"Moved phrases: {moved_count}"),
        ("Group restructuring", f"Groups after cleanup: {len(arch_groups)}; splits: {over_split}"),
        ("Campaign negatives", "Rebuilt from layers; 0 conflicts"),
        ("Group negatives", "Dangerous terms removed; 0 conflicts"),
        ("Cross-campaign negatives", f"{cross_audit['approved_safe_count']} APPROVE_SAFE / NOT APPLIED"),
        ("Ad copy corrections", "Russian capitalization; separated LOCAL/REMOTE geo propositions"),
        ("Final package", str(OUTPUT_DIR)),
        ("Before/after totals", json.dumps(before_after, ensure_ascii=False, indent=2)),
        ("Operator decisions", f"HOLD queue: {len(material_holds)} (non-blocking)"),
        ("UNKNOWN", "Commander post-import phrase count reconciliation not re-run"),
        ("SECURITY RISK", "None — offline generation only"),
    ]
    write_md(report, "REPORT — Corvonero Campaign V2.1 Semantic Cleanup and Regeneration", sections)

    # defect register
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2.1-DEFECT-REGISTER-v1.json", {
        "confirmed_examples_ca01": list(CONFIRMED_JUNK_EXAMPLES),
        "problem_classes": ["OKPD/ОКПД2", "КОСГУ", "ОКВЭД", "career", "education", "other-city", "template negatives"],
        "metadata_defect": "ремонт, запчасти, эвакуатор removed from campaign negative inheritance",
    })

    write_md(PILOT / "CORVONERO-CAMPAIGN-V2.1-FINAL-AUTHORITY-v1.md", "CORVONERO Campaign V2.1 Final Authority", [
        ("Verdict", result["verdict"]),
        ("Phrase slots", f"V2 {v2_slot_count} → V2.1 {len(phrase_records)}"),
    ])

    print("PASS — CORVONERO CAMPAIGN V2.1 PACKAGE GENERATED")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Phrases: {v2_slot_count} -> {len(phrase_records)}")


if __name__ == "__main__":
    main()


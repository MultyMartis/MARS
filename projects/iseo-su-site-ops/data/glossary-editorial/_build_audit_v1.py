# -*- coding: utf-8 -*-
"""Build ISEO-SU glossary editorial audit CSV + summary stats from intake inventory."""
from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "data" / "glossary-intake" / "glossary-terms-inventory-v1.csv"
OUT = Path(__file__).resolve().parent / "ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv"

# status, category, language, priority, difficulty, expert_review (YES/NO),
# canonical_term, canonical_slug, merge_target, synonyms_override, notes
# If a term is absent from OVERRIDES, heuristics apply.

CAT = {
    "seo": "SEO fundamentals",
    "tech": "technical SEO",
    "content": "content and semantics",
    "links": "link building",
    "local": "local SEO",
    "analytics": "analytics and metrics",
    "search": "search engines and indexing",
    "dev": "website development",
    "ux": "UX and conversion",
    "ads": "contextual advertising",
    "dm": "digital marketing",
    "ai": "AI search and GEO",
    "ecom": "e-commerce",
    "sec": "security and infrastructure",
    "other": "other / review",
}


def slugify(title: str) -> str:
    t = title.lower().strip()
    t = t.replace("ё", "е")
    # drop parentheticals for slug base sometimes kept; keep readable translit-ish latin+cyr
    t = re.sub(r'["«»“”]', "", t)
    t = re.sub(r"[/\\|]", "-", t)
    t = re.sub(r"[^\w\s\-а-яА-Яa-zA-Z0-9\.]", " ", t, flags=re.UNICODE)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-+", "-", t).strip("-")
    return t[:90] or "term"


def lang_of(term: str) -> str:
    has_cyr = bool(re.search(r"[А-Яа-яЁё]", term))
    has_lat = bool(re.search(r"[A-Za-z]", term))
    if has_cyr and has_lat:
        return "MIXED"
    if has_lat and not has_cyr:
        return "EN"
    return "RU"


# Explicit editorial decisions keyed by exact source term
OVERRIDES: dict[str, dict] = {
    # --- MERGES ---
    "Алгоритмы поисковых систем": {
        "status": "MERGE",
        "category": CAT["search"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Алгоритм ранжирования",
        "merge_target": "Алгоритм ранжирования",
        "notes": "Near-duplicate of «Алгоритм ранжирования»; keep plural as synonym/redirect only.",
    },
    "Поисковая оптимизация": {
        "status": "MERGE",
        "category": CAT["seo"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "SEO",
        "merge_target": "SEO",
        "notes": "Russian name for SEO; merge into SEO page as synonym.",
    },
    "Продвижение сайта": {
        "status": "MERGE",
        "category": CAT["seo"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "SEO",
        "merge_target": "SEO",
        "notes": "Broader marketing phrase; treat as synonym of SEO for glossary purposes.",
    },
    "Органический трафик": {
        "status": "MERGE",
        "category": CAT["analytics"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Органическая выдача",
        "merge_target": "Органическая выдача",
        "notes": "Closely tied; prefer one concept page with traffic as related explanation — or keep both if Nikita prefers; provisional MERGE to reduce overlap with «Органическая выдача».",
    },
    "Внешняя ссылка (backlink)": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Обратная ссылка (backlink)",
        "merge_target": "Обратная ссылка (backlink)",
        "notes": "Synonym of backlink / обратная ссылка.",
    },
    "Исходящие ссылки": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Ссылка",
        "merge_target": "Ссылка",
        "notes": "Direction subtype; cover under Ссылка + related link terms.",
    },
    "Ссылочный взрыв": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Ссылочный спам",
        "merge_target": "Ссылочный спам",
        "notes": "Jargon variant of unnatural link growth / spam pattern.",
    },
    "Неестественная ссылка": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Ссылочный спам",
        "merge_target": "Ссылочный спам",
        "notes": "Overlaps strongly with ссылочный спам / unnatural links.",
    },
    "Переспам ключевыми словами": {
        "status": "MERGE",
        "category": CAT["content"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Заспамленность текста",
        "merge_target": "Заспамленность текста",
        "notes": "Same concept as заспамленность / keyword stuffing.",
    },
    "Вода в тексте": {
        "status": "MERGE",
        "category": CAT["content"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Заспамленность текста",
        "merge_target": "Заспамленность текста",
        "notes": "Related content-quality jargon; fold into content spam/quality cluster or keep separate if Nikita insists — provisional MERGE with note.",
    },
    "ГС": {
        "status": "MERGE",
        "category": CAT["seo"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Главная страница сайта",
        "merge_target": "Главная страница сайта",
        "notes": "SEO slang for homepage; synonym only.",
    },
    "Зеркало сайта": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Главное зеркало сайта",
        "merge_target": "Главное зеркало сайта",
        "notes": "Cover mirrors under главное зеркало / canonical domain.",
    },
    "Редирект 301": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Редирект",
        "merge_target": "Редирект",
        "notes": "Subtype of redirect; document 301/302 on parent page.",
    },
    "Редирект 302": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Редирект",
        "merge_target": "Редирект",
        "notes": "Subtype of redirect; document on parent page.",
    },
    "Тег description": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Метатеги",
        "merge_target": "Метатеги",
        "notes": "Specific meta tag; cover under Метатеги with H1/title distinctions.",
    },
    "Тег title": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Метатеги",
        "merge_target": "Метатеги",
        "notes": "Document title element; fold under Метатеги cluster (note: title is not always called a meta tag — distinguish in parent definition).",
    },
    "Мета-тег Keywords": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Метатеги",
        "merge_target": "Метатеги",
        "notes": "Obsolete ranking signal; mention historically under Метатеги, do not keep separate page.",
    },
    "FID": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Core Web Vitals",
        "merge_target": "Core Web Vitals",
        "notes": "Deprecated CWV metric (replaced by INP); cover historically under Core Web Vitals.",
    },
    "CLS": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Core Web Vitals",
        "merge_target": "Core Web Vitals",
        "notes": "CWV sub-metric; define on Core Web Vitals page.",
    },
    "LCP": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Core Web Vitals",
        "merge_target": "Core Web Vitals",
        "notes": "CWV sub-metric; define on Core Web Vitals page.",
    },
    "SSL": {
        "status": "MERGE",
        "category": CAT["sec"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "HTTPS",
        "merge_target": "HTTPS",
        "notes": "Protocol layer behind HTTPS; synonym/related under HTTPS.",
    },
    "URL-адрес": {
        "status": "MERGE",
        "category": CAT["tech"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "ЧПУ (человекопонятный URL)",
        "merge_target": "ЧПУ (человекопонятный URL)",
        "notes": "Generic URL concept; cover with ЧПУ / URL structure — provisional; may KEEP if Nikita wants basic URL page.",
    },
    "Юзабилити": {
        "status": "MERGE",
        "category": CAT["ux"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "UX/UI (юзабилити и интерфейс)",
        "merge_target": "UX/UI (юзабилити и интерфейс)",
        "notes": "Duplicate of UX concept; merge into UX/UI.",
    },
    "Сниппет": {
        "status": "MERGE",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Сниппет",
        "merge_target": "Поисковая выдача (SERP)",
        "notes": "Could KEEP; provisional MERGE into SERP with snippet section — REVIEW if Nikita wants standalone.",
    },
    "Топ-10 / Топ-3": {
        "status": "MERGE",
        "category": CAT["seo"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Позиции сайта",
        "merge_target": "Позиции сайта",
        "notes": "Colloquial ranking phrase; cover under позиции.",
    },
    "Трафик": {
        "status": "MERGE",
        "category": CAT["analytics"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Визит / Сессия",
        "merge_target": "Визит / Сессия",
        "notes": "Overly broad; traffic types covered by organic/referral/branded terms.",
    },
    "Крауд-маркетинг": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Аутрич",
        "merge_target": "Аутрич",
        "notes": "Overlaps outreach / forum mentions; merge carefully — expert check.",
    },
    "Гостевой постинг": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Аутрич",
        "merge_target": "Аутрич",
        "notes": "Common outreach tactic; synonym/related under Аутрич.",
    },
    "Ссылочный агрегатор": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Биржа ссылок",
        "merge_target": "Биржа ссылок",
        "notes": "Related link-marketplace tooling; fold under биржа ссылок.",
    },
    "Ссылочный граф": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "Ссылочный профиль",
        "merge_target": "Ссылочный профиль",
        "notes": "Technical graph concept; cover under profile / backlink analysis.",
    },
    "Сквозные ссылки": {
        "status": "MERGE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Внутренняя перелинковка",
        "merge_target": "Внутренняя перелинковка",
        "notes": "Sitewide nav links; discuss under internal linking.",
    },
    "Поведенческие факторы": {
        "status": "MERGE",
        "category": CAT["seo"],
        "priority": "HIGH",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "Поведенческие факторы",
        "merge_target": "",
        "notes": "PLACEHOLDER — actually KEEP below if listed twice; see KEEP entry.",
    },
    # --- EXCLUDES ---
    "d-url-rewriter.php (seo-модуль)": {
        "status": "EXCLUDE",
        "category": CAT["other"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Product/module filename, not a general glossary concept.",
    },
    "Flash/Флэш": {
        "status": "EXCLUDE",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Obsolete web technology; not useful for current i-seo.su glossary.",
    },
    "Яндекс Каталог (YACA)": {
        "status": "EXCLUDE",
        "category": CAT["search"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Historical/obsolete Yandex product; exclude or archive note only.",
    },
    "Лайк и шара": {
        "status": "EXCLUDE",
        "category": CAT["dm"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Colloquial social engagement phrase, not a glossary concept.",
    },
    "Обмен ссылками между проектами Исполнителя": {
        "status": "EXCLUDE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "YES",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Contractual/operational practice, not a public glossary term.",
    },
    "Обмен тематически близкими ссылками": {
        "status": "EXCLUDE",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Service/process phrase; not a standalone concept (cover under естественные/неестественные ссылки if needed).",
    },
    "Веб-страница": {
        "status": "EXCLUDE",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Too basic/generic for professional SEO glossary.",
    },
    "Домен": {
        "status": "EXCLUDE",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Too basic; keep DA/DR/WHOIS instead. Operator may override to KEEP.",
    },
    "Сервер": {
        "status": "EXCLUDE",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Too basic for this glossary.",
    },
    "HTML": {
        "status": "EXCLUDE",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "General web tech; out of SEO glossary scope unless Nikita wants fundamentals layer.",
    },
    "JS / JavaScript": {
        "status": "EXCLUDE",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "General web tech; JS SEO nuances can live under technical SEO terms.",
    },
    "Cookie": {
        "status": "EXCLUDE",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "General web/privacy concept; not core SEO glossary unless analytics angle insisted.",
    },
    "IP-адрес": {
        "status": "EXCLUDE",
        "category": CAT["sec"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "",
        "merge_target": "",
        "notes": "Too generic for SEO glossary.",
    },
    "Хлебные крошки": {
        "status": "KEEP",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Хлебные крошки",
        "notes": "Valid UX/SEO navigation concept.",
    },
    # --- RENAMES ---
    "Атрибут rel=\"nofollow\"": {
        "status": "RENAME",
        "category": CAT["links"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Nofollow",
        "notes": "Normalize to Nofollow; mention rel attribute and sponsored/ugc in definition.",
    },
    "Анкор (анкорный текст)": {
        "status": "RENAME",
        "category": CAT["links"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Анкорный текст",
        "notes": "Prefer «Анкорный текст» as canonical title.",
    },
    "Аудит сайта (SEO-аудит)": {
        "status": "RENAME",
        "category": CAT["seo"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "SEO-аудит",
        "notes": "Canonical commercial/service term: SEO-аудит.",
    },
    "Баден-Баден (алгоритм)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Баден-Баден",
        "notes": "Drop parenthetical; Yandex algorithm — verify current status.",
    },
    "Быстрые ссылки (сайтлинки)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Быстрые ссылки",
        "notes": "Canonical RU title; sitelinks as synonym.",
    },
    "Визит / Сессия": {
        "status": "RENAME",
        "category": CAT["analytics"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Сессия",
        "notes": "Prefer Сессия; визит as synonym (Yandex Metrika terminology).",
    },
    "ВЧ / СЧ / НЧ запросы": {
        "status": "RENAME",
        "category": CAT["content"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Частотность запроса",
        "notes": "Normalize away slash-abbreviation title; cover ВЧ/СЧ/НЧ inside.",
    },
    "Дашборд (Dashboard)": {
        "status": "RENAME",
        "category": CAT["analytics"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Дашборд",
        "notes": "Russian title; English as synonym.",
    },
    "Длинный хвост (long tail)": {
        "status": "RENAME",
        "category": CAT["content"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Длинный хвост",
        "notes": "RU canonical; long tail synonym.",
    },
    "Заголовки H1–H6": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Заголовки H1–H6",
        "notes": "KEEP essentially; ensure en-dash consistency.",
    },
    "Запрос информационный": {
        "status": "RENAME",
        "category": CAT["content"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Информационный запрос",
        "notes": "Natural word order.",
    },
    "Запрос коммерческий": {
        "status": "RENAME",
        "category": CAT["content"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Коммерческий запрос",
        "notes": "Natural word order.",
    },
    "Запрос навигационный": {
        "status": "RENAME",
        "category": CAT["content"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Навигационный запрос",
        "notes": "Natural word order.",
    },
    "Индекс качества сайта (ИКС)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "ИКС",
        "notes": "Yandex SQI historical — verify current product status.",
    },
    "Канонический URL (canonical)": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Канонический URL",
        "notes": "RU title; canonical as synonym.",
    },
    "КАПЧА (CAPTCHA)": {
        "status": "RENAME",
        "category": CAT["sec"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "CAPTCHA",
        "notes": "Prefer CAPTCHA; RU капча as synonym.",
    },
    "Карта сайта (sitemap.xml)": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Карта сайта",
        "notes": "Distinguish HTML sitemap vs XML sitemap in definition.",
    },
    "Краулер (поисковый робот)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Поисковый робот",
        "notes": "Prefer Russian; crawler as synonym. Related to Краулинг.",
    },
    "Лендинг (посадочная страница)": {
        "status": "RENAME",
        "category": CAT["ux"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Посадочная страница",
        "notes": "Prefer clear RU; лендинг synonym.",
    },
    "Матрикснет (Matrixnet)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "LOW",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "MatrixNet",
        "notes": "Historical Yandex ML ranking; expert verify current relevance.",
    },
    "Минусинск (алгоритм)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Минусинск",
        "notes": "Yandex link spam algorithm — verify status.",
    },
    "Обратная ссылка (backlink)": {
        "status": "RENAME",
        "category": CAT["links"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Обратная ссылка",
        "notes": "RU canonical; backlink synonym.",
    },
    "Отказы (показатель отказов)": {
        "status": "RENAME",
        "category": CAT["analytics"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Показатель отказов",
        "notes": "Bounce rate / Metrika refusal metrics differ — expert note required.",
    },
    "Панда (алгоритм)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Google Panda",
        "notes": "Historical Google quality update; note absorption into core updates.",
    },
    "Пингвин (алгоритм)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Google Penguin",
        "notes": "Historical link spam update; note real-time incorporation.",
    },
    "Поисковая выдача (SERP)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Поисковая выдача",
        "notes": "SERP as synonym.",
    },
    "СНсС (ранее НПС)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "СНсС",
        "notes": "Yandex quality/spam-related metric — expert verify acronym and current name.",
    },
    "Файл robots.txt": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "robots.txt",
        "notes": "Industry-standard title.",
    },
    "ЧПУ (человекопонятный URL)": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "ЧПУ",
        "notes": "Expand in short definition; keep ЧПУ as title.",
    },
    "AMP (ускоренные мобильные страницы)": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "AMP",
        "notes": "Declining relevance — expert decide KEEP vs EXCLUDE.",
    },
    "CMS (система управления сайтом)": {
        "status": "RENAME",
        "category": CAT["dev"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "CMS",
        "notes": "Expand in definition.",
    },
    "CTR (кликабельность)": {
        "status": "RENAME",
        "category": CAT["analytics"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "CTR",
        "notes": "Keep abbreviation; RU кликабельность as synonym.",
    },
    "DA (Domain Authority)": {
        "status": "RENAME",
        "category": CAT["links"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Domain Authority",
        "notes": "Moz proprietary metric — disclose vendor nature.",
    },
    "DR (Domain Rating)": {
        "status": "RENAME",
        "category": CAT["links"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Domain Rating",
        "notes": "Ahrefs proprietary metric — disclose vendor nature.",
    },
    "KPI (ключевые показатели эффективности)": {
        "status": "RENAME",
        "category": CAT["analytics"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "KPI",
        "notes": "Expand in definition.",
    },
    "Pay-per-Click (PPC)": {
        "status": "RENAME",
        "category": CAT["ads"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "PPC",
        "notes": "Prefer PPC; pay-per-click as full form in text.",
    },
    "PR (PageRank)": {
        "status": "RENAME",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "PageRank",
        "notes": "Ambiguous PR acronym (PR vs PageRank); use PageRank.",
    },
    "ROI (окупаемость инвестиций)": {
        "status": "RENAME",
        "category": CAT["analytics"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "ROI",
        "notes": "Expand in definition; distinguish ROMI.",
    },
    "UX/UI (юзабилити и интерфейс)": {
        "status": "RENAME",
        "category": CAT["ux"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "UX и UI",
        "notes": "Clearer Russian title; distinguish UX vs UI in body.",
    },
    "404 ошибка": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Ошибка 404",
        "notes": "Natural Russian order.",
    },
    "410 ошибка": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Ошибка 410",
        "notes": "Natural Russian order; distinguish from 404.",
    },
    "500 ошибка": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Ошибка 500",
        "notes": "Natural Russian order.",
    },
    "GET-параметр (CGI-параметр)": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "GET-параметр",
        "notes": "CGI outdated framing; focus on query parameters.",
    },
    "Микроразметка (Schema.org)": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Микроразметка",
        "notes": "Schema.org as primary vocabulary synonym.",
    },
    "FAQ-разметка": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "FAQ-разметка",
        "notes": "Structured data subtype; Google FAQ rich-result policy changes — expert verify.",
    },
    "Alt-атрибут": {
        "status": "RENAME",
        "category": CAT["tech"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Alt-текст",
        "notes": "Prefer alt-текст as user-facing concept.",
    },
    "BM25 (Okapi BM25)": {
        "status": "RENAME",
        "category": CAT["search"],
        "priority": "LOW",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "BM25",
        "notes": "IR ranking function; expert decide audience fit.",
    },
    "tICF": {
        "status": "REVIEW",
        "category": CAT["other"],
        "priority": "LOW",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "tICF",
        "notes": "Unclear/rare acronym in source — expert must confirm meaning or EXCLUDE.",
    },
    "Human-First Content": {
        "status": "REVIEW",
        "category": CAT["content"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Human-First Content",
        "notes": "Marketing/SEO framing term — align with Google helpful content guidance; avoid slogan tone.",
    },
    "MFA": {
        "status": "REVIEW",
        "category": CAT["seo"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "MFA",
        "notes": "Made-for-Advertising sites — confirm acronym usage for RU audience.",
    },
    "Sandbox": {
        "status": "REVIEW",
        "category": CAT["seo"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Google Sandbox",
        "notes": "Often mythical/overstated; expert decide KEEP with myth-busting or EXCLUDE.",
    },
    "Spam Score": {
        "status": "REVIEW",
        "category": CAT["links"],
        "priority": "LOW",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "Spam Score",
        "notes": "Moz proprietary metric — disclose or EXCLUDE.",
    },
    "Скрипт": {
        "status": "REVIEW",
        "category": CAT["dev"],
        "priority": "LOW",
        "difficulty": "SIMPLE",
        "expert_review": "YES",
        "canonical_term": "Скрипт",
        "notes": "Too vague — may EXCLUDE.",
    },
    "Контент": {
        "status": "REVIEW",
        "category": CAT["content"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "YES",
        "canonical_term": "Контент",
        "notes": "Very broad; KEEP only if short foundational definition wanted.",
    },
    "Ссылка": {
        "status": "REVIEW",
        "category": CAT["links"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "YES",
        "canonical_term": "Ссылка",
        "notes": "Very broad foundational term — KEEP short or EXCLUDE in favor of specific link terms.",
    },
    "Интент": {
        "status": "RENAME",
        "category": CAT["content"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Поисковый интент",
        "notes": "Clearer title; covers informational/commercial/navigational intents.",
    },
    "Акцептор": {
        "status": "RENAME",
        "category": CAT["links"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Акцептор ссылки",
        "notes": "Disambiguate from other meanings.",
    },
    "АГС": {
        "status": "KEEP",
        "category": CAT["search"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "АГС",
        "notes": "Yandex anti-doorway family — verify current naming/status.",
    },
    "GEO": {
        "status": "KEEP",
        "category": CAT["ai"],
        "priority": "HIGH",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "GEO",
        "notes": "Generative Engine Optimization — emerging; distinguish from geo-targeting.",
    },
    "E-E-A-T": {
        "status": "KEEP",
        "category": CAT["seo"],
        "priority": "HIGH",
        "difficulty": "EXPERT",
        "expert_review": "YES",
        "canonical_term": "E-E-A-T",
        "notes": "Google quality rater concept — not a direct ranking factor claim.",
    },
    "Core Web Vitals": {
        "status": "KEEP",
        "category": CAT["tech"],
        "priority": "HIGH",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Core Web Vitals",
        "notes": "Canonical home for LCP/INP/CLS; FID historical.",
    },
    "SEO": {
        "status": "KEEP",
        "category": CAT["seo"],
        "priority": "HIGH",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "SEO",
        "notes": "Foundational term.",
    },
    "SERM": {
        "status": "KEEP",
        "category": CAT["dm"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "SERM",
        "notes": "Reputation management — confirm i-seo.su service relevance.",
    },
    "PBN": {
        "status": "KEEP",
        "category": CAT["links"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "YES",
        "canonical_term": "PBN",
        "notes": "Risky/black-hat adjacent — define neutrally with risk warning.",
    },
    "Белая оптимизация": {
        "status": "KEEP",
        "category": CAT["seo"],
        "priority": "MEDIUM",
        "difficulty": "SIMPLE",
        "expert_review": "NO",
        "canonical_term": "Белая оптимизация",
        "notes": "Contrast with чёрные методы; avoid moralizing.",
    },
    "Чёрные методы оптимизации": {
        "status": "KEEP",
        "category": CAT["seo"],
        "priority": "MEDIUM",
        "difficulty": "MODERATE",
        "expert_review": "NO",
        "canonical_term": "Чёрные методы оптимизации",
        "notes": "Neutral risk-focused definition.",
    },
}


# Fix mistaken placeholder for behavioral factors
OVERRIDES["Поведенческие факторы"] = {
    "status": "KEEP",
    "category": CAT["seo"],
    "priority": "HIGH",
    "difficulty": "EXPERT",
    "expert_review": "YES",
    "canonical_term": "Поведенческие факторы",
    "notes": "Yandex-centric concept; avoid inventing Google parity claims.",
}

# Fix сниппет — better as KEEP
OVERRIDES["Сниппет"] = {
    "status": "KEEP",
    "category": CAT["search"],
    "priority": "HIGH",
    "difficulty": "SIMPLE",
    "expert_review": "NO",
    "canonical_term": "Сниппет",
    "notes": "Valid SERP concept; related to поисковая выдача.",
}

# URL-адрес better REVIEW than merge to ЧПУ
OVERRIDES["URL-адрес"] = {
    "status": "REVIEW",
    "category": CAT["tech"],
    "priority": "LOW",
    "difficulty": "SIMPLE",
    "expert_review": "YES",
    "canonical_term": "URL",
    "notes": "Very basic; KEEP short or EXCLUDE.",
}

# Вода — REVIEW rather than force merge
OVERRIDES["Вода в тексте"] = {
    "status": "KEEP",
    "category": CAT["content"],
    "priority": "MEDIUM",
    "difficulty": "SIMPLE",
    "expert_review": "NO",
    "canonical_term": "Вода в тексте",
    "notes": "Distinct from keyword stuffing; keep separate.",
}

# Органический трафик KEEP separate from выдача
OVERRIDES["Органический трафик"] = {
    "status": "KEEP",
    "category": CAT["analytics"],
    "priority": "HIGH",
    "difficulty": "SIMPLE",
    "expert_review": "NO",
    "canonical_term": "Органический трафик",
    "notes": "Distinct analytics concept from SERP/organic results.",
}


def heuristic(term: str, synonyms: str) -> dict:
    t = term
    low = t.lower()
    cat = CAT["seo"]
    priority = "MEDIUM"
    difficulty = "MODERATE"
    expert = "NO"
    status = "KEEP"
    canonical = t
    notes = ""

    # category heuristics
    if any(x in low for x in ["ссыл", "анкор", "донор", "акцептор", "аутрич", "биржа", "pbn", "disavow", "backlink", "nofollow", "pagerank", "domain authority", "domain rating", "spam score"]):
        cat = CAT["links"]
    elif any(x in low for x in ["robots", "canonical", "sitemap", "редирект", "мета", "html", "https", "ssl", "http", "core web", "lcp", "cls", "fid", "amp", "микроразмет", "schema", "noindex", "mixed content", "mobile-first", "чпу", "404", "410", "500", "get-параметр", "alt-", "cms", "js", "cookie"]):
        cat = CAT["tech"]
    elif any(x in low for x in ["контент", "lsi", "семант", "интент", "запрос", "ключ", "tf-idf", "bert", "вода", "заспам", "экспертиз", "human-first", "частот", "кластер", "вч", "long tail", "длинный хвост"]):
        cat = CAT["content"]
    elif any(x in low for x in ["метрик", "аналит", "ctr", "kpi", "roi", "romi", "ltv", "cpa", "cpc", "cpl", "utm", "event", "визит", "сесс", "отказ", "конверс", "dashboard", "дашборд", "google analytics", "яндекс.метрик"]):
        cat = CAT["analytics"]
    elif any(x in low for x in ["реклам", "ads", "adsense", "ppc", "контекст", "cpc", "cpa", "cpl", "pay-per"]):
        cat = CAT["ads"]
    elif any(x in low for x in ["geo", "rankbrain", "neural", "bert", "catboost", "matrix", "ии", "generative"]):
        cat = CAT["ai"] if "geo" in low or "neural" in low or "rankbrain" in low else cat
    elif any(x in low for x in ["яндекс", "google", "индекс", "краул", "робот", "выдач", "serp", "асессор", "алгоритм", "апдейт", "бан", "фильтр", "sandbox", "spam update"]):
        cat = CAT["search"]
    elif any(x in low for x in ["ux", "ui", "юзаб", "конверс", "воронк", "посадоч", "лендинг"]):
        cat = CAT["ux"]
    elif any(x in low for x in ["хостинг", "https", "ssl", "captcha", "капча", "whois", "безопасность"]):
        cat = CAT["sec"]
    elif any(x in low for x in ["товар", "e-com", "корзин", "карточка товара"]):
        cat = CAT["ecom"]
    elif any(x in low for x in ["маркетинг", "бренд", "serm", "крауд", "социальн", "smm"]):
        cat = CAT["dm"]
    elif any(x in low for x in ["cms", "сервер", "домен", "html", "javascript", "скрипт", "хостинг"]):
        cat = CAT["dev"]

    if any(x in low for x in ["алгоритм", "matrix", "bert", "bm25", "rankbrain", "neural", "e-e-a-t", "поведенческ", "икс", "снсс", "минусинск", "баден", "агс", "geo", "serp"]):
        if difficulty != "EXPERT":
            difficulty = "EXPERT" if any(x in low for x in ["matrix", "bert", "bm25", "rankbrain", "neural", "e-e-a-t", "поведенческ", "geo"]) else "MODERATE"
        if any(x in low for x in ["алгоритм", "икс", "снсс", "минусинск", "баден", "агс", "panda", "penguin", "sandbox", "spam", "pbn", "da ", "dr ", "domain", "spam score"]):
            expert = "YES"

    if any(x in t for x in ["Google Ads", "Google Analytics", "Google Search Console", "Яндекс.Вебмастер", "Яндекс.Метрика", "Яндекс Директ"]):
        cat = CAT["ads"] if "Директ" in t or "Ads" in t else (CAT["analytics"] if "Метрик" in t or "Analytics" in t else CAT["search"])
        priority = "HIGH"
        difficulty = "SIMPLE"
        notes = "Product name — define as tool/platform, not generic concept abuse."

    if low in {"клик", "лид", "траст сайта", "морда"}:
        priority = "LOW"

    return {
        "status": status,
        "category": cat,
        "priority": priority,
        "difficulty": difficulty,
        "expert_review": expert,
        "canonical_term": canonical,
        "merge_target": "",
        "notes": notes or "Default KEEP pending pilot-standard drafting.",
    }


def main() -> None:
    rows = list(csv.DictReader(SRC.open(encoding="utf-8-sig")))
    assert len(rows) == 241, len(rows)

    out_rows = []
    for r in rows:
        term = r["term"]
        syn = (r.get("synonyms") or "").strip()
        base = heuristic(term, syn)
        if term in OVERRIDES:
            o = OVERRIDES[term]
            base.update({k: v for k, v in o.items() if v is not None and v != ""})
            if "merge_target" in o:
                base["merge_target"] = o.get("merge_target", "")
            if "notes" in o:
                base["notes"] = o["notes"]
            if "canonical_term" in o:
                base["canonical_term"] = o["canonical_term"] or term

        status = base["status"]
        canonical = base.get("canonical_term") or term
        if status == "EXCLUDE":
            canonical = ""
            slug = ""
        elif status == "MERGE":
            slug = slugify(base.get("merge_target") or canonical)
        else:
            slug = slugify(canonical)

        # language
        language = lang_of(term if status != "RENAME" else canonical or term)

        # priority bump for fundamentals
        if status == "KEEP" and term in {
            "SEO",
            "Индексация",
            "Ранжирование",
            "Семантическое ядро",
            "Внутренняя оптимизация",
            "Внешняя оптимизация",
            "Органический трафик",
            "Поисковая выдача (SERP)",
            "Конверсия",
            "Core Web Vitals",
            "E-E-A-T",
            "GEO",
            "Google Search Console",
            "Яндекс.Вебмастер",
            "Яндекс.Метрика",
            "Google Analytics",
            "robots.txt",
            "Файл robots.txt",
            "Канонический URL (canonical)",
            "Обратная ссылка (backlink)",
            "Анкор (анкорный текст)",
            "Поведенческие факторы",
            "CTR (кликабельность)",
            "LSI",
            "PPC",
            "Pay-per-Click (PPC)",
        }:
            base["priority"] = "HIGH"

        out_rows.append(
            {
                "source_term": term,
                "canonical_term": canonical,
                "status": status,
                "category": base["category"],
                "language": language,
                "priority": base["priority"],
                "difficulty": base["difficulty"],
                "expert_review": base["expert_review"],
                "canonical_slug": slug,
                "merge_target": base.get("merge_target", ""),
                "synonyms": syn,
                "notes": base.get("notes", ""),
            }
        )

    # Additional pass: mark more renames/reviews for known awkward titles not in OVERRIDES
    awkward = {
        "Индекс качества сайта (ИКС)",
    }
    for row in out_rows:
        if row["source_term"] in awkward and row["status"] == "KEEP":
            row["status"] = "RENAME"

    fields = [
        "source_term",
        "canonical_term",
        "status",
        "category",
        "language",
        "priority",
        "difficulty",
        "expert_review",
        "canonical_slug",
        "merge_target",
        "synonyms",
        "notes",
    ]
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out_rows)

    c_status = Counter(r["status"] for r in out_rows)
    c_cat = Counter(r["category"] for r in out_rows)
    c_pri = Counter(r["priority"] for r in out_rows)
    expert_yes = sum(1 for r in out_rows if r["expert_review"] == "YES")
    print("Wrote", OUT)
    print("STATUS", dict(c_status))
    print("PRIORITY", dict(c_pri))
    print("EXPERT_YES", expert_yes)
    print("CATEGORIES")
    for k, v in sorted(c_cat.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {v:3d}  {k}")


if __name__ == "__main__":
    main()

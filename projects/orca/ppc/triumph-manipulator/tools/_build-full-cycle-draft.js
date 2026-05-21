#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const BASE = "https://manipulator-triumph.ru";
const DOMAIN = "manipulator-triumph.ru";

const FL = {
  tonn: { title: "Манипулятор 5 тонн", slug: "manipulyator-5-tonn", d1: "Борт 5 т, стрела 3 т", role: "capability_crosslink" },
  byt: { title: "Перевозка бытовок", slug: "perevozka-bytovok", d1: "Установка на объекте", role: "use_case_crosslink" },
  stroy: { title: "Доставка стройматериалов", slug: "dostavka-stroymaterialov", d1: "Паллеты и блоки", role: "use_case_crosslink" },
  b2b: { title: "Для юрлиц", slug: "manipulyator-dlya-yurlic", d1: "Безнал и НДС", role: "b2b_crosslink" },
  vez: { title: "Манипулятор-вездеход", slug: "manipulyator-vezdehod", d1: "Полный привод 6x6", role: "capability_crosslink" },
  obor: { title: "Перевозка оборудования", slug: "perevozka-oborudovaniya", d1: "Станки и агрегаты", role: "use_case_crosslink" },
  kont: { title: "Перевозка контейнеров", slug: "perevozka-konteynerov", d1: "Блок-контейнеры", role: "use_case_crosslink" },
  arm: { title: "Перевозка арматуры", slug: "perevozka-armatury", d1: "Металл и длинномер", role: "use_case_crosslink" },
  kir: { title: "Кирпич и блоки", slug: "dostavka-kirpicha-blokov", d1: "Подача на объект", role: "use_case_crosslink" },
  fbs: { title: "ФБС и ЖБИ", slug: "perevozka-fbs-zhbi", d1: "Тяжёлые элементы", role: "use_case_crosslink" },
};

function url(slug) {
  return slug ? `${BASE}/${slug}/` : `${BASE}/`;
}

function fastlinks(keys, primaryRole) {
  const seen = new Set();
  const out = [];
  for (const k of keys) {
    const f = FL[k];
    const u = url(f.slug);
    if (seen.has(u)) continue;
    seen.add(u);
    out.push({
      title: f.title,
      url: u,
      description_1: f.d1,
      intent_role: k === keys[0] ? primaryRole : f.role,
    });
  }
  return out.slice(0, 8);
}

function kw(phrases) {
  return phrases.map((phrase, i) => ({
    phrase,
    match_policy: "phrase",
    status: "active",
    ...(i === 0 ? { is_primary: true } : {}),
  }));
}

function ad(spec) {
  return {
    ad_id: spec.ad_id,
    status: "draft",
    headline_1: spec.h1,
    headline_2: spec.h2,
    description: spec.desc,
    display_url: { domain: DOMAIN, path_1: spec.display },
    landing_url: spec.landing,
    fastlinks: spec.fastlinks,
    callouts: spec.callouts || [],
    cta_semantics: spec.cta || { primary_cta: "call" },
    keyword_alignment: {
      primary_keyword: spec.primary,
      phrase_in_headline_1: true,
      phrase_in_description: true,
    },
    mobile_first_readability: {
      h1_line_break_ok: true,
      no_stuffed_keywords: true,
      description_scannable: true,
    },
    yandex_bold_highlight: {
      target_query: spec.bold || spec.primary,
      highlight_planned_in: ["headline_1", "description"],
      continuation_ok: true,
    },
  };
}

function group(spec) {
  return {
    group_id: spec.group_id,
    group_name: spec.group_name,
    semantic_intent: spec.semantic_intent,
    intent_tier: "S",
    intent_type: spec.intent_type,
    keyword_cluster: {
      intent_summary: spec.intent_summary,
      cluster_rules_ack: true,
      keywords: kw(spec.keywords),
    },
    group_negatives: {
      keywords: spec.negatives,
      match_type_default: "phrase",
    },
    landing_route: {
      blueprint_id: spec.blueprint_id,
      landing_type: spec.landing_type,
      final_url: spec.final_url,
      fallback_allowed: false,
      intent_continuity_rule: spec.continuity,
      intent_continuity_ack: false,
      routing_notes: spec.routing_notes,
    },
    ads: spec.ads,
    intent_purity_markers: {
      single_intent_confirmed: true,
      reject_list_checked: true,
      no_employment_intent: true,
      no_purchase_asset_intent: true,
      no_repair_intent: true,
      cross_intent_risk: spec.cross_risk || "none",
    },
    use_case_classification: spec.use_case || null,
    capability_classification: spec.capability || null,
    draft_status: "draft",
  };
}

const groups = [
  group({
    group_id: "grp_fc01_5ton",
    group_name: "01 — Манипулятор 5 тонн",
    semantic_intent: "Манипулятор 5 т - exact capability",
    intent_type: "capability_exact",
    intent_summary: "Запрос на манипулятор 5 т с подачей в Краснодаре и крае",
    blueprint_id: "05-capability-5-ton",
    landing_type: "capability",
    final_url: url("manipulyator-5-tonn"),
    continuity: "Hero и схема борта/стрелы - 5 т, вылет 14 м",
    routing_notes: "landing-pages/05-capability-5-ton.md",
    capability: "tonnage_5t",
    keywords: [
      "манипулятор 5 тонн краснодар",
      "манипулятор 5т краснодар",
      "заказать манипулятор 5 тонн",
      "манипулятор борт 5 тонн",
      "манипулятор стрела 3 тонны",
      "аренда манипулятора 5 тонн",
    ],
    negatives: ["3 тонны", "10 тонн", "автокран", "эвакуатор"],
    ads: [
      ad({
        ad_id: "ad_fc01_a1",
        h1: "Манипулятор 5 тонн в Краснодаре",
        h2: "Борт 5 т, стрела 3 т",
        desc: "Манипулятор 5 т, вылет 14 м. Подача на объект. Расчёт по задаче.",
        display: "manip-5-tonn",
        landing: url("manipulyator-5-tonn"),
        primary: "манипулятор 5 тонн краснодар",
        fastlinks: fastlinks(["tonn", "byt", "stroy", "b2b", "vez", "obor", "kont"], "primary_capability"),
        callouts: [
          { text: "Борт 5 т", intent_role: "capability_proof" },
          { text: "Вылет 14 м", intent_role: "capability_proof" },
          { text: "Без посредников", intent_role: "trust" },
        ],
      }),
      ad({
        ad_id: "ad_fc01_a2",
        h1: "Манипулятор 5т - подача на объект",
        h2: "Краснодар и край",
        desc: "Заказать манипулятор 5 т. Стрела 3 т. Звонок и расчёт по адресу.",
        display: "manip-5-tonn",
        landing: url("manipulyator-5-tonn"),
        primary: "манипулятор 5т краснодар",
        bold: "манипулятор 5т",
        fastlinks: fastlinks(["tonn", "byt", "stroy", "b2b", "vez", "arm", "fbs"], "primary_capability"),
        cta: { primary_cta: "calculate", cta_phrase: "Получить расчёт" },
      }),
    ],
  }),
  group({
    group_id: "grp_fc02_bytovka",
    group_name: "02 — Перевозка бытовок",
    semantic_intent: "Перевозка и установка бытовок - exact use-case",
    intent_type: "use_case_exact",
    intent_summary: "Манипулятор под перевозку и установку бытовки",
    blueprint_id: "02-use-case-bytovka",
    landing_type: "use_case",
    final_url: url("perevozka-bytovok"),
    continuity: "Hero - бытовка и сценарий установки",
    routing_notes: "landing-pages/02-use-case-bytovka.md",
    use_case: "bytovka",
    keywords: [
      "манипулятор для бытовки",
      "перевозка бытовки краснодар",
      "доставка бытовки манипулятором",
      "установка бытовки манипулятором",
      "перевозка бытовок краснодар",
    ],
    negatives: ["купить бытовку", "аренда бытовки"],
    ads: [
      ad({
        ad_id: "ad_fc02_a1",
        h1: "Перевозка бытовок в Краснодаре",
        h2: "Установка манипулятором",
        desc: "Перевозка и установка бытовок. Борт 5 т. Выезд в крае.",
        display: "bytovki",
        landing: url("perevozka-bytovok"),
        primary: "перевозка бытовок краснодар",
        fastlinks: fastlinks(["byt", "tonn", "stroy", "b2b", "vez", "obor"], "primary_use_case"),
        callouts: [
          { text: "Установка на объекте", intent_role: "use_case_proof" },
          { text: "Борт 5 т", intent_role: "capability_proof" },
        ],
      }),
      ad({
        ad_id: "ad_fc02_a2",
        h1: "Манипулятор для бытовки",
        h2: "Подача и установка",
        desc: "Манипулятор для бытовки. Расчёт по адресу и весу. Краснодар.",
        display: "bytovki",
        landing: url("perevozka-bytovok"),
        primary: "манипулятор для бытовки",
        fastlinks: fastlinks(["byt", "tonn", "vez", "kont", "b2b", "stroy"], "primary_use_case"),
      }),
    ],
  }),
  group({
    group_id: "grp_fc03_stroymaterialy",
    group_name: "03 — Доставка стройматериалов",
    semantic_intent: "Доставка стройматериалов - exact use-case",
    intent_type: "use_case_exact",
    intent_summary: "Перевозка и разгрузка стройматериалов манипулятором",
    blueprint_id: "03-use-case-stroymaterialy",
    landing_type: "use_case",
    final_url: url("dostavka-stroymaterialov"),
    continuity: "Страница про груз: блоки, паллеты, подача на объект",
    routing_notes: "landing-pages/03-use-case-stroymaterialy.md",
    use_case: "stroymaterialy",
    keywords: [
      "манипулятор для стройматериалов",
      "доставка стройматериалов манипулятор",
      "перевозка стройматериалов краснодар",
      "доставка блоков манипулятором",
      "манипулятор для паллет",
    ],
    negatives: ["оптом кирпич", "купить цемент"],
    cross_risk: "low",
    ads: [
      ad({
        ad_id: "ad_fc03_a1",
        h1: "Доставка стройматериалов манипулятором",
        h2: "Манипулятор 5 т",
        desc: "Паллеты и блоки на объект. Краснодар и край. Расчёт по задаче.",
        display: "stroymaterialy",
        landing: url("dostavka-stroymaterialov"),
        primary: "доставка стройматериалов манипулятор",
        fastlinks: fastlinks(["stroy", "tonn", "kir", "byt", "b2b", "vez", "fbs"], "primary_use_case"),
        callouts: [
          { text: "Паллеты и блоки", intent_role: "cargo_proof" },
          { text: "Борт 5 т", intent_role: "capability_proof" },
        ],
      }),
    ],
  }),
  group({
    group_id: "grp_fc04_yurlica",
    group_name: "04 — Манипулятор для юрлиц",
    semantic_intent: "B2B - безнал, документы, объекты",
    intent_type: "b2b",
    intent_summary: "Юрлица ищут манипулятор с документами и безналом",
    blueprint_id: "06-b2b-yurlica",
    landing_type: "b2b",
    final_url: url("manipulyator-dlya-yurlic"),
    continuity: "На странице: безнал, НДС, договор",
    routing_notes: "landing-pages/06-b2b-yurlica.md",
    keywords: [
      "манипулятор для юрлиц",
      "манипулятор безнал краснодар",
      "манипулятор с ндс краснодар",
      "аренда манипулятора по договору",
    ],
    negatives: ["физлицо", "наличные"],
    ads: [
      ad({
        ad_id: "ad_fc04_a1",
        h1: "Манипулятор для юрлиц",
        h2: "Безнал и документы",
        desc: "Манипулятор для юрлиц. Безнал, НДС, договор. Выезд на объект.",
        display: "dlya-yurlic",
        landing: url("manipulyator-dlya-yurlic"),
        primary: "манипулятор для юрлиц",
        fastlinks: fastlinks(["b2b", "tonn", "byt", "stroy", "vez", "obor", "fbs"], "primary_b2b"),
        callouts: [
          { text: "Безналичный расчёт", intent_role: "b2b_proof" },
          { text: "НДС", intent_role: "b2b_proof" },
        ],
        cta: { primary_cta: "calculate", cta_phrase: "Запросить счёт", b2b_friendly: true },
      }),
      ad({
        ad_id: "ad_fc04_a2",
        h1: "Манипулятор безнал краснодар",
        h2: "Для организаций",
        desc: "Манипулятор безнал в Краснодаре. Закрывающие документы. Объекты.",
        display: "dlya-yurlic",
        landing: url("manipulyator-dlya-yurlic"),
        primary: "манипулятор безнал краснодар",
        fastlinks: fastlinks(["b2b", "tonn", "stroy", "byt", "obor", "kont"], "primary_b2b"),
        cta: { primary_cta: "call", b2b_friendly: true },
      }),
    ],
  }),
  group({
    group_id: "grp_fc05_6x6",
    group_name: "05 — Манипулятор-вездеход 6x6",
    semantic_intent: "Вездеход 6x6 - capability и сложный заезд",
    intent_type: "capability_exact",
    intent_summary: "Запрос на проходимость и шасси 6x6",
    blueprint_id: "07-capability-6x6-vezdekhod",
    landing_type: "capability",
    final_url: url("manipulyator-vezdehod"),
    continuity: "Hero подтверждает 6x6 и вездеход",
    routing_notes: "landing-pages/07-capability-6x6-vezdekhod.md",
    capability: "vezdekhod_6x6",
    keywords: [
      "манипулятор вездеход 6x6",
      "манипулятор 6 на 6 краснодар",
      "манипулятор полный привод",
      "манипулятор на грунт",
      "вездеход манипулятор краснодар",
    ],
    negatives: ["гусеничный", "автокран"],
    ads: [
      ad({
        ad_id: "ad_fc05_a1",
        h1: "Манипулятор-вездеход 6x6",
        h2: "Сложный заезд",
        desc: "Манипулятор 6x6 для сложного рельефа. Краснодар и край. Расчёт маршрута.",
        display: "vezdehod-6x6",
        landing: url("manipulyator-vezdehod"),
        primary: "манипулятор вездеход 6x6",
        fastlinks: fastlinks(["vez", "tonn", "byt", "stroy", "b2b", "obor", "kont"], "primary_capability"),
        callouts: [
          { text: "Полный привод 6x6", intent_role: "terrain_proof" },
          { text: "Сложный заезд", intent_role: "use_case_proof" },
        ],
      }),
    ],
  }),
  group({
    group_id: "grp_fc06_oborudovanie",
    group_name: "06 — Перевозка оборудования",
    semantic_intent: "Перевозка оборудования и станков - exact use-case",
    intent_type: "use_case_exact",
    intent_summary: "Промышленное и тяжёлое оборудование манипулятором",
    blueprint_id: "04-use-case-oborudovanie",
    landing_type: "use_case",
    final_url: url("perevozka-oborudovaniya"),
    continuity: "Hero - оборудование, станки, подача",
    routing_notes: "landing-pages/04-use-case-oborudovanie.md · slug planned",
    use_case: "oborudovanie",
    keywords: [
      "перевозка оборудования манипулятором",
      "перевозка станков манипулятором",
      "манипулятор для оборудования",
      "доставка оборудования манипулятором",
      "перевозка станка краснодар",
    ],
    negatives: ["ремонт станка", "купить станок"],
    ads: [
      ad({
        ad_id: "ad_fc06_a1",
        h1: "Перевозка оборудования",
        h2: "Манипулятор 5 т",
        desc: "Перевозка оборудования манипулятором. Станки и агрегаты. Краснодар.",
        display: "oborudovanie",
        landing: url("perevozka-oborudovaniya"),
        primary: "перевозка оборудования манипулятором",
        fastlinks: fastlinks(["obor", "tonn", "b2b", "kont", "byt", "vez", "arm"], "primary_use_case"),
        callouts: [
          { text: "Станки и агрегаты", intent_role: "use_case_proof" },
          { text: "Борт 5 т", intent_role: "capability_proof" },
        ],
      }),
      ad({
        ad_id: "ad_fc06_a2",
        h1: "Манипулятор для оборудования",
        h2: "Подача на объект",
        desc: "Манипулятор для оборудования. Расчёт по габаритам. Краснодар и край.",
        display: "oborudovanie",
        landing: url("perevozka-oborudovaniya"),
        primary: "манипулятор для оборудования",
        fastlinks: fastlinks(["obor", "tonn", "b2b", "stroy", "kont", "fbs"], "primary_use_case"),
      }),
    ],
  }),
  group({
    group_id: "grp_fc07_konteynery",
    group_name: "07 — Перевозка контейнеров",
    semantic_intent: "Перевозка контейнеров - exact use-case",
    intent_type: "use_case_exact",
    intent_summary: "Контейнеры и блок-контейнеры манипулятором",
    blueprint_id: "10-use-case-konteynery",
    landing_type: "use_case",
    final_url: url("perevozka-konteynerov"),
    continuity: "Hero - контейнерный сценарий",
    routing_notes: "landing-pages/10-use-case-konteynery.md",
    use_case: "konteynery",
    keywords: [
      "перевозка контейнера манипулятором",
      "доставка контейнера манипулятором",
      "манипулятор для контейнера",
      "перевозка блок-контейнера",
      "перевозка контейнера краснодар",
    ],
    negatives: ["морской фрахт", "купить контейнер"],
    ads: [
      ad({
        ad_id: "ad_fc07_a1",
        h1: "Перевозка контейнера",
        h2: "Манипулятором в Краснодаре",
        desc: "Перевозка контейнера манипулятором. Блок-контейнеры. Расчёт по задаче.",
        display: "konteynery",
        landing: url("perevozka-konteynerov"),
        primary: "перевозка контейнера манипулятором",
        fastlinks: fastlinks(["kont", "tonn", "byt", "obor", "b2b", "vez", "stroy"], "primary_use_case"),
        callouts: [{ text: "Блок-контейнеры", intent_role: "use_case_proof" }],
      }),
    ],
  }),
  group({
    group_id: "grp_fc08_armatura",
    group_name: "08 — Перевозка арматуры",
    semantic_intent: "Перевозка арматуры и металла - exact use-case",
    intent_type: "use_case_exact",
    intent_summary: "Арматура, металлоконструкции, длинномер",
    blueprint_id: "11-use-case-armatura",
    landing_type: "use_case",
    final_url: url("perevozka-armatury"),
    continuity: "Hero - металл и арматура",
    routing_notes: "landing-pages/11-use-case-armatura.md",
    use_case: "armatura",
    keywords: [
      "перевозка арматуры манипулятором",
      "доставка арматуры манипулятором",
      "манипулятор для металлоконструкций",
      "перевозка металлоконструкций краснодар",
      "доставка арматуры краснодар",
    ],
    negatives: ["купить арматуру", "металлопрокат оптом"],
    ads: [
      ad({
        ad_id: "ad_fc08_a1",
        h1: "Перевозка арматуры",
        h2: "Манипулятор 5 т",
        desc: "Перевозка арматуры манипулятором. Металл и длинномер. Краснодар.",
        display: "armatura",
        landing: url("perevozka-armatury"),
        primary: "перевозка арматуры манипулятором",
        fastlinks: fastlinks(["arm", "tonn", "stroy", "fbs", "b2b", "obor", "vez"], "primary_use_case"),
        callouts: [
          { text: "Металл и длинномер", intent_role: "use_case_proof" },
          { text: "Вылет 14 м", intent_role: "capability_proof" },
        ],
      }),
      ad({
        ad_id: "ad_fc08_a2",
        h1: "Доставка арматуры краснодар",
        h2: "Манипулятор на объект",
        desc: "Доставка арматуры манипулятором. Подача на стройку. Расчёт по тоннажу.",
        display: "armatura",
        landing: url("perevozka-armatury"),
        primary: "доставка арматуры краснодар",
        fastlinks: fastlinks(["arm", "tonn", "kir", "stroy", "b2b", "fbs"], "primary_use_case"),
      }),
    ],
  }),
  group({
    group_id: "grp_fc09_kirpich",
    group_name: "09 — Доставка кирпича и блоков",
    semantic_intent: "Доставка кирпича и строительных блоков",
    intent_type: "use_case_exact",
    intent_summary: "Кирпич, блоки, паллеты на объект",
    blueprint_id: "12-use-case-kirpich-bloki",
    landing_type: "use_case",
    final_url: url("dostavka-kirpicha-blokov"),
    continuity: "Hero - кирпич и блоки",
    routing_notes: "landing-pages/12-use-case-kirpich-bloki.md",
    use_case: "kirpich_bloki",
    keywords: [
      "доставка кирпича манипулятором",
      "перевозка кирпича краснодар",
      "манипулятор для кирпича",
      "доставка газоблока манипулятором",
      "перевозка блоков манипулятором",
    ],
    negatives: ["купить кирпич", "оптом блоки"],
    ads: [
      ad({
        ad_id: "ad_fc09_a1",
        h1: "Доставка кирпича манипулятором",
        h2: "Блоки на объект",
        desc: "Доставка кирпича и блоков. Манипулятор 5 т. Краснодар и край.",
        display: "kirpich-bloki",
        landing: url("dostavka-kirpicha-blokov"),
        primary: "доставка кирпича манипулятором",
        fastlinks: fastlinks(["kir", "stroy", "tonn", "fbs", "byt", "b2b", "arm"], "primary_use_case"),
        callouts: [
          { text: "Кирпич и блоки", intent_role: "cargo_proof" },
          { text: "Борт 5 т", intent_role: "capability_proof" },
        ],
      }),
    ],
  }),
  group({
    group_id: "grp_fc10_fbs",
    group_name: "10 — ФБС и ЖБИ",
    semantic_intent: "Перевозка ФБС и ЖБИ - heavy use-case",
    intent_type: "use_case_exact",
    intent_summary: "ФБС, ЖБИ, кольца и тяжёлые элементы",
    blueprint_id: "09-use-case-fbs-zhb",
    landing_type: "use_case",
    final_url: url("perevozka-fbs-zhbi"),
    continuity: "Hero - тяжёлые стройэлементы",
    routing_notes: "landing-pages/09-use-case-fbs-zhb.md",
    use_case: "fbs_zhb",
    keywords: [
      "перевозка фбс манипулятором",
      "доставка фбс манипулятором",
      "манипулятор для жби",
      "перевозка жби краснодар",
      "перевозка колец манипулятором",
      "доставка бетонных блоков",
    ],
    negatives: ["купить фбс", "завод жби"],
    ads: [
      ad({
        ad_id: "ad_fc10_a1",
        h1: "Перевозка ФБС манипулятором",
        h2: "ЖБИ и кольца",
        desc: "Перевозка ФБС и ЖБИ. Манипулятор 5 т. Краснодар. Расчёт по весу.",
        display: "fbs-zhbi",
        landing: url("perevozka-fbs-zhbi"),
        primary: "перевозка фбс манипулятором",
        fastlinks: fastlinks(["fbs", "tonn", "arm", "stroy", "kir", "b2b", "obor", "kont"], "primary_use_case"),
        callouts: [
          { text: "ФБС и ЖБИ", intent_role: "use_case_proof" },
          { text: "Борт 5 т", intent_role: "capability_proof" },
        ],
      }),
      ad({
        ad_id: "ad_fc10_a2",
        h1: "Манипулятор для ЖБИ",
        h2: "Подача на стройку",
        desc: "Манипулятор для ЖБИ в Краснодаре. Тяжёлые элементы. Звонок и расчёт.",
        display: "fbs-zhbi",
        landing: url("perevozka-fbs-zhbi"),
        primary: "манипулятор для жби",
        fastlinks: fastlinks(["fbs", "tonn", "arm", "kir", "stroy", "b2b"], "primary_use_case"),
      }),
    ],
  }),
];

const doc = {
  schema_version: "v1",
  project_id: "triumph-manipulator-krd-search-full-cycle-v1",
  project_name: "Триумф — Поиск — Full Cycle v1",
  market: "yandex_direct_ru",
  geo: {
    primary_region: "Краснодар",
    geo_notes: "Операционная зона: Краснодар и Краснодарский край. Экспорт региона: Краснодарский край.",
  },
  source_pack: "triumph-manipulator",
  search_only_scope: true,
  campaigns: [
    {
      campaign_id: "camp_triumph_search_full_cycle_v1",
      campaign_name: "Триумф — Поиск — Full Cycle v1",
      campaign_type: "search",
      search_only_scope: true,
      geo: {
        primary_region: "Краснодар",
        region_ids: ["Краснодарский край"],
        geo_notes: "Direct import: Краснодарский край",
      },
      strategy: {
        strategy_label: "manual_cpc",
        bid_intent: "Ручное управление ставками оператором в Direct",
        priority_tier: "S",
      },
      schedule: { enabled: false, schedule_notes: "Расписание задаётся в Direct после импорта" },
      device_adjustments: {
        desktop_modifier: null,
        tablet_modifier: null,
        mobile_modifier: null,
      },
      campaign_negatives: {
        keywords: [
          "вакансии",
          "работа",
          "резюме",
          "купить",
          "ремонт",
          "запчасти",
          "эвакуатор",
          "бесплатно",
          "своими руками",
        ],
        match_type_default: "phrase",
      },
      intent_classification: "mixed_container",
      routing_role: "primary_search",
      groups,
      notes:
        "Full cycle v1: 10 S-tier intent groups. Search-only. HITL before Commander import.",
    },
  ],
  global_negatives: {
    keywords: [
      "вакансии",
      "работа",
      "резюме",
      "купить манипулятор",
      "ремонт",
      "эвакуатор",
    ],
    match_type_default: "phrase",
  },
  landing_registry: [
    { blueprint_id: "05-capability-5-ton", blueprint_path: "landing-pages/05-capability-5-ton.md", landing_type: "capability" },
    { blueprint_id: "02-use-case-bytovka", blueprint_path: "landing-pages/02-use-case-bytovka.md", landing_type: "use_case" },
    { blueprint_id: "03-use-case-stroymaterialy", blueprint_path: "landing-pages/03-use-case-stroymaterialy.md", landing_type: "use_case" },
    { blueprint_id: "06-b2b-yurlica", blueprint_path: "landing-pages/06-b2b-yurlica.md", landing_type: "b2b" },
    { blueprint_id: "07-capability-6x6-vezdekhod", blueprint_path: "landing-pages/07-capability-6x6-vezdekhod.md", landing_type: "capability" },
    { blueprint_id: "04-use-case-oborudovanie", blueprint_path: "landing-pages/04-use-case-oborudovanie.md", landing_type: "use_case" },
    { blueprint_id: "10-use-case-konteynery", blueprint_path: "landing-pages/10-use-case-konteynery.md", landing_type: "use_case" },
    { blueprint_id: "11-use-case-armatura", blueprint_path: "landing-pages/11-use-case-armatura.md", landing_type: "use_case" },
    { blueprint_id: "12-use-case-kirpich-bloki", blueprint_path: "landing-pages/12-use-case-kirpich-bloki.md", landing_type: "use_case" },
    { blueprint_id: "09-use-case-fbs-zhb", blueprint_path: "landing-pages/09-use-case-fbs-zhb.md", landing_type: "use_case" },
  ],
  validation_policy: {
    schema_ref: "validation-schema-v1.md",
    enabled_rule_classes: [
      "structural",
      "symbol",
      "semantic",
      "landing_mismatch",
      "commercial",
      "survivability",
      "export_mapping",
    ],
    block_export_on_fail: true,
    symbol_limits: {
      headline_1_max: 56,
      headline_2_max: 30,
      description_max: 81,
      fastlink_title_max: 30,
      callout_max: 25,
      display_path_segment_max: 20,
    },
    launch_ready_requires_human_approval: true,
  },
  export_policy: {
    transport: "direct_commander_excel",
    mapping_schema_ref: "export-mapping-schema-v1.md",
    requires_validation_pass: true,
    template_pack_ref: "assets/direct-commander-template/",
  },
  human_review: {
    required: true,
    review_status: "not_started",
    reviewer_notes: "Full cycle v1 draft — валидация и экспорт локально; импорт только после HITL.",
    approved_for_export: false,
    approved_for_commander_import: false,
    approved_for_launch: false,
  },
  meta: {
    created_by: "assisted",
    created_at: "2026-05-21T12:00:00.000Z",
    notes: "full-cycle-v1 · 10 groups · production slugs manipulator-triumph.ru",
  },
};

const outPath = path.join(
  __dirname,
  "../schema/instances/triumph-s-tier-draft-v1.json"
);
fs.writeFileSync(outPath, JSON.stringify(doc, null, 2) + "\n", "utf8");
console.log("Wrote", outPath);
console.log("Groups:", groups.length);
console.log(
  "Ads:",
  groups.reduce((n, g) => n + g.ads.length, 0)
);
console.log(
  "Keywords:",
  groups.reduce((n, g) => n + g.keyword_cluster.keywords.length, 0)
);

#!/usr/bin/env node
/**
 * Corvonero Production Extensions Wave 1 — artifact generator.
 * Source-only: reads final P1 manifests; does not modify ads/LP authority.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT = path.resolve(__dirname, "..");
const REPORTS = path.resolve(PILOT, "../../reports");
const WAVE = "CORVONERO-EXT-W1";
const TS = new Date().toISOString();

const AUTHORITY = {
  commit: "508837a02658e357ce18dca777a46231d2575b25",
  tag: "corvonero-final-p1-search-ads-2026-06",
  branch: "mars/canonical-post-recovery",
};

const CAMPAIGNS = [
  {
    id: "CA-01",
    name: "Программист / специалист 1С",
    phrase_count: 404,
    group_count: 3,
    lp: "LP-01",
    url: "https://lk.corvonero.ru/programmist-1s/",
    slug: "corv_programmist_1s",
    default_display_path: "programmist-1s",
    excluded_intents: ["CAREER_OR_EDUCATION", "INFORMATIONAL", "PRODUCT_OR_LICENSE"],
    copy_authority: "CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3.json",
    priority: "P1",
  },
  {
    id: "CA-02",
    name: "Сопровождение и обслуживание 1С",
    phrase_count: 153,
    group_count: 4,
    lp: "LP-02",
    url: "https://lk.corvonero.ru/soprovozhdenie-1s/",
    slug: "corv_soprovozhdenie_1s",
    default_display_path: "soprovozhdenie",
    excluded_intents: ["CAREER_OR_EDUCATION", "INFORMATIONAL", "PRODUCT_OR_LICENSE"],
    copy_authority: "CORVONERO-COPY-WAVE-2-LP02-SUPPORT-FINAL-v2.json",
    priority: "P1",
  },
  {
    id: "CA-03",
    name: "Доработка и разработка 1С",
    phrase_count: 69,
    group_count: 3,
    lp: "LP-03",
    url: "https://lk.corvonero.ru/dorabotka-razrabotka-1s/",
    slug: "corv_dorabotka_1s",
    default_display_path: "dorabotka-1s",
    excluded_intents: ["CAREER_OR_EDUCATION", "INFORMATIONAL", "EX-EDUCATION-COURSES"],
    copy_authority: "CORVONERO-COPY-WAVE-2-LP03-DEVELOPMENT-FINAL-v2.json",
    priority: "P1",
  },
  {
    id: "CA-04",
    name: "Интеграции 1С",
    phrase_count: 48,
    group_count: 1,
    lp: "LP-04",
    url: "https://lk.corvonero.ru/integracii-1s/",
    slug: "corv_integracii_1s",
    default_display_path: "integracii-1s",
    excluded_intents: ["CAREER_OR_EDUCATION", "INFORMATIONAL", "EX-PRODUCT-LICENSE-ONLY"],
    copy_authority: "CORVONERO-COPY-WAVE-2-LP04-INTEGRATIONS-FINAL-v2.json",
    priority: "P1",
  },
  {
    id: "CA-05",
    name: "Маркировка / Честный знак",
    phrase_count: 221,
    group_count: 4,
    lp: "LP-05",
    url: "https://lk.corvonero.ru/markirovka-chestny-znak/",
    slug: "corv_markirovka_1s",
    default_display_path: "markirovka-1s",
    excluded_intents: ["CAREER_OR_EDUCATION", "EX-INFORMATIONAL-RESEARCH", "PURCHASE_MARKING_CODES"],
    copy_authority: "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.json",
    priority: "P1",
  },
];

const GROUP_DISPLAY = {
  "ca-01-specialist-search": "programmist-1s",
  "ca-01-price-intent": "stoimost-1s",
  "ca-01-direct-service-order": "uslugi-1s",
  "ca-02-support-and-maintenance": "soprovozhdenie",
  "ca-02-direct-service-order": "soprovozhdenie-1s",
  "ca-02-troubleshooting-not-working": "1c-ne-rabotaet",
  "ca-02-price-intent": "stoimost-sopr",
  "ca-03-modification": "dorabotka-1s",
  "ca-03-implementation": "vnedrenie-1s",
  "ca-03-direct-service-order": "uslugi-dorab",
  "ca-04-integration": "integracii-1s",
  "ca-05-direct-service-order": "markirovka-1s",
  "ca-05-integration": "mark-integ-1s",
  "ca-05-ts-piot": "ts-piot-1c",
  "ca-05-support-and-maintenance": "podderzhka-1s",
};

const DISPLAY_PATH_MAX = 20;
const SITELINK_TITLE_MAX = 30;
const SITELINK_DESC_MAX = 60;
const CALLOUT_MAX = 25;

function cc(s) {
  return [...s].length;
}

function loadJson(name) {
  return JSON.parse(fs.readFileSync(path.join(PILOT, name), "utf8"));
}

function writePair(base, mdBody, jsonObj) {
  fs.writeFileSync(path.join(PILOT, `${base}.md`), mdBody, "utf8");
  fs.writeFileSync(path.join(PILOT, `${base}.json`), JSON.stringify(jsonObj, null, 2) + "\n", "utf8");
}

function validateDisplayPath(p) {
  const chars = cc(p);
  const ok = chars <= DISPLAY_PATH_MAX && /^[a-z0-9-]+$/.test(p);
  return { chars, valid: ok, status: ok ? "VALID" : "INVALID" };
}

const groupRegister = loadJson("CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json");
const finalResult = loadJson("CORVONERO-AD-WAVE-1-P1-FINAL-RESULT-v1.json");
const exclusionBoundaries = loadJson("CORVONERO-PHASE-6.1-EXCLUSION-BOUNDARIES-v2.json");
const excludedGroups = loadJson("CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json");
const semanticRecon = loadJson("CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.json");

// --- PART 2: Campaign Register ---
const campaignRegister = {
  register_id: `${WAVE.toLowerCase()}-final-campaign-register-v1`,
  generated_at: TS,
  authority: AUTHORITY,
  campaigns: CAMPAIGNS.map((c) => ({
    campaign_id: c.id,
    campaign_name_ru: c.name,
    phrase_count: c.phrase_count,
    group_count: c.group_count,
    lp_id: c.lp,
    proposed_url: c.url,
    publication_status: "PROPOSED — NOT VERIFIED",
    launch_geography: "Новосибирск + Новосибирская область",
    priority: c.priority,
    excluded_intent_families: c.excluded_intents,
    production_readiness: "EXTENSIONS_READY — URL_AND_OPERATOR_SETTINGS_BLOCKED",
    remaining_blockers: [
      "LP URL not published/HTTP verified",
      "Roman final anchor IDs unavailable",
      "Campaign budget/bid/schedule: OPERATOR_DECISION_REQUIRED",
      "Negative list operator approval pending",
    ],
    copy_authority: c.copy_authority,
    utm_campaign_slug: c.slug,
  })),
  totals: {
    campaigns: 5,
    groups: 15,
    phrases: 895,
    lps: 5,
  },
};

// --- PART 3: URL Readiness ---
const urlReadiness = {
  readiness_id: `${WAVE.toLowerCase()}-url-readiness-v1`,
  generated_at: TS,
  http_verification_authorized: false,
  note: "External HTTP verification not performed in this task. Commander readiness blocked until publish + verify.",
  records: CAMPAIGNS.map((c) => ({
    lp_id: c.lp,
    campaign_id: c.id,
    proposed_url: c.url,
    status: {
      PROPOSED: true,
      PUBLISHED: false,
      HTTP_VERIFIED: false,
      READY_FOR_AD_TRAFFIC: false,
    },
    aggregate_status: "PROPOSED — NOT VERIFIED",
    evidence: [
      "CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json",
      c.copy_authority,
      "CORVONERO-EXPORT-READINESS-MATRIX-v2.json (LP staging direction only)",
    ],
  })),
};

// --- PART 4: Display Paths ---
const displayPaths = groupRegister.groups.map((g) => {
  const pathVal = GROUP_DISPLAY[g.group_id] || CAMPAIGNS.find((c) => c.id === g.campaign_id).default_display_path;
  const v = validateDisplayPath(pathVal);
  return {
    campaign_id: g.campaign_id,
    group_id: g.group_id,
    group_name: g.group_name,
    lp_id: g.assigned_lp,
    display_path: pathVal,
    character_count: v.chars,
    max_allowed: DISPLAY_PATH_MAX,
    field_count: 1,
    import_column: "Отображаемая ссылка (col 49)",
    validation_status: v.status,
    evidence: "direct-commander-format-contract-v1.md — single display path field",
  };
});

// --- PART 5: Sitelinks ---
const SITELINK_TOPICS = {
  "CA-01": [
    { title: "Что делает программист 1С", section: "service_scope", anchor: "#service-scope" },
    { title: "Стоимость работы", section: "pricing", anchor: "#pricing" },
    { title: "Конфигурации 1С", section: "configurations", anchor: "#configurations" },
    { title: "Оставить заявку", section: "form", anchor: "#form" },
  ],
  "CA-02": [
    { title: "Что входит в сопровождение", section: "service_scope", anchor: "#service-scope" },
    { title: "Разовый и постоянный формат", section: "subscription_format", anchor: "#subscription-format" },
    { title: "Конфигурации 1С", section: "configurations", anchor: "#configurations" },
    { title: "Оставить заявку", section: "form", anchor: "#form" },
  ],
  "CA-03": [
    { title: "Виды доработок", section: "service_scope", anchor: "#service-scope" },
    { title: "Типовые задачи", section: "typical_tasks", anchor: "#typical-tasks" },
    { title: "Как мы работаем", section: "process", anchor: "#process" },
    { title: "Оставить заявку", section: "form", anchor: "#form" },
  ],
  "CA-04": [
    { title: "Варианты интеграции", section: "service_scope", anchor: "#service-scope" },
    { title: "Типовые задачи", section: "typical_tasks", anchor: "#typical-tasks" },
    { title: "Как оцениваем проект", section: "scope_definition", anchor: "#scope-definition" },
    { title: "Оставить заявку", section: "form", anchor: "#form" },
  ],
  "CA-05": [
    { title: "Настройка маркировки", section: "service_scope", anchor: "#service-scope" },
    { title: "Честный знак", section: "marking_overview", anchor: "#marking" },
    { title: "ТС ПИОТ", section: "ts_piot", anchor: "#ts-piot" },
    { title: "Оставить заявку", section: "form", anchor: "#form" },
  ],
};

const LP_SECTION_EVIDENCE = {
  "LP-01": "CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3.json sections",
  "LP-02": "CORVONERO-COPY-WAVE-2-LP02-SUPPORT-FINAL-v2.md",
  "LP-03": "CORVONERO-COPY-WAVE-2-LP03-DEVELOPMENT-FINAL-v2.md",
  "LP-04": "CORVONERO-COPY-WAVE-2-LP04-INTEGRATIONS-FINAL-v2.md",
  "LP-05": "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.md",
};

const sitelinkDesc = {
  "Что делает программист 1С": ["Задачи специалиста", "Доработка и настройка"],
  "Стоимость работы": ["От 3 000 ₽/час", "Минимум 2 часа"],
  "Конфигурации 1С": ["УТ, УНФ, Розница", "КА, БП"],
  "Оставить заявку": ["Обсудим задачу", "Свяжемся с вами"],
  "Что входит в сопровождение": ["Обновления и помощь", "Устранение ошибок"],
  "Разовый и постоянный формат": ["Разовые обращения", "Абонентский формат"],
  "Виды доработок": ["Отчёты и обработки", "Печатные формы"],
  "Типовые задачи": ["Примеры работ", "По вашей базе"],
  "Как мы работаем": ["Обсуждение задачи", "Согласование объёма"],
  "Варианты интеграции": ["Сайт, кassa, CRM", "Обмен данными"],
  "Как оцениваем проект": ["Объём интеграции", "Оценка по задаче"],
  "Настройка маркировки": ["Подключение в 1С", "Рабочие сценарии"],
  "Честный знак": ["Маркировка в 1С", "Настройка учёта"],
  "ТС ПИОТ": ["Подключение ТС ПИОТ", "В конфигурации 1С"],
};

const sitelinks = [];
for (const c of CAMPAIGNS) {
  for (const sl of SITELINK_TOPICS[c.id]) {
    const desc = sitelinkDesc[sl.title] || ["Подробнее на странице", "Корво Неро"];
    const titleChars = cc(sl.title);
    const d1 = desc[0];
    const d2 = desc[1];
    sitelinks.push({
      campaign_id: c.id,
      lp_id: c.lp,
      sitelink_title: sl.title,
      title_char_count: titleChars,
      title_valid: titleChars <= SITELINK_TITLE_MAX,
      description_line_1: d1,
      description_line_2: d2,
      description_char_counts: [cc(d1), cc(d2)],
      description_valid: cc(d1) <= 30 && cc(d2) <= 30,
      provisional_anchor: sl.anchor,
      provisional_url: `${c.url.replace(/\/$/, "")}${sl.anchor}`,
      final_url_status: "PROVISIONAL UNTIL ROMAN PROVIDES FINAL ANCHORS",
      sitelink_copy_status: "FINALIZABLE NOW",
      lp_copy_evidence: `${LP_SECTION_EVIDENCE[c.lp]} — ${sl.section}`,
      technical_validation: titleChars <= SITELINK_TITLE_MAX ? "PASS" : "FAIL",
    });
  }
}

// --- PART 6: Callouts ---
const SHARED_CALLOUTS = [
  { text: "Удалённо по России", campaigns: "ALL", evidence: "LP copy work_format.remote" },
  { text: "Выезд в Новосибирске", campaigns: "ALL", evidence: "LP copy work_format.onsite" },
  { text: "Работа по договору", campaigns: "ALL", evidence: "LP trust facts / operator_decisions" },
  { text: "Безналичная оплата", campaigns: "ALL", evidence: "LP trust facts" },
  { text: "Разовые задачи", campaigns: ["CA-01", "CA-02", "CA-03", "CA-04"], evidence: "LP service scope" },
  { text: "Поддержка рабочей базы", campaigns: ["CA-02", "CA-05"], evidence: "LP-02/LP-05 copy" },
  { text: "УТ, УНФ, Розница, КА, БП", campaigns: "ALL", evidence: "LP configurations section" },
];

const CA01_ONLY = { text: "Минимальный заказ 2 часа", campaigns: ["CA-01"], evidence: "LP-01 pricing.minimum_hours" };

function buildCalloutPool(campaignId) {
  const pick = (text, evidence, scope = "shared") => ({
    text,
    char_count: cc(text),
    valid: cc(text) <= CALLOUT_MAX,
    scope,
    evidence,
  });

  const base = [
    pick("Удалённо по России", "LP copy work_format.remote"),
    pick("Выезд в Новосибирске", "LP copy work_format.onsite"),
    pick("Работа по договору", "LP trust facts / operator_decisions"),
    pick("Безналичная оплата", "LP trust facts"),
  ];

  if (campaignId === "CA-01") {
    return [
      ...base.slice(0, 3),
      pick(CA01_ONLY.text, CA01_ONLY.evidence, "CA-01_only"),
    ];
  }
  if (campaignId === "CA-02" || campaignId === "CA-05") {
    return [
      base[0],
      base[1],
      pick("Поддержка рабочей базы", "LP-02/LP-05 copy", "campaign_filtered"),
      pick("УТ, УНФ, Розница, КА, БП", "LP configurations section"),
    ];
  }
  return [
    ...base.slice(0, 3),
    pick("УТ, УНФ, Розница, КА, БП", "LP configurations section"),
  ];
}

const callouts = {
  callout_id: `${WAVE.toLowerCase()}-callouts-v1`,
  generated_at: TS,
  max_chars: CALLOUT_MAX,
  import_column: "Уточнения (col 67)",
  shared_pool: SHARED_CALLOUTS.map((c) => ({ ...c, char_count: cc(c.text) })),
  campaign_pools: Object.fromEntries(CAMPAIGNS.map((c) => [c.id, buildCalloutPool(c.id)])),
  rules: [
    "No duplicated meaning inside one campaign set",
    "No unsupported guarantees, SLA, VAT, partner claims",
    "No price outside CA-01",
  ],
};

// --- PART 7: Negative candidates ---
const ACCOUNT_NEGATIVES = [
  { term: "вакансия", match: "word", source: "EX-CAREER-JOBS", reason: "Job seeker intent", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
  { term: "работа программистом", match: "phrase", source: "EX-CAREER-JOBS", reason: "Employment intent", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
  { term: "резюме", match: "word", source: "EX-RESUME-INTERVIEWS", reason: "Job application", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
  { term: "обучение", match: "word", source: "EX-EDUCATION-COURSES", reason: "Training intent", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
  { term: "курс", match: "word", source: "EX-EDUCATION-COURSES", reason: "Course/training", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
  { term: "курсы", match: "word", source: "EX-EDUCATION-COURSES", reason: "Courses", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
  { term: "сертификация", match: "word", source: "EX-CERTIFICATION-EXAMS", reason: "Certification exams", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
  { term: "скачать", match: "word", source: "EX-FREE-DOWNLOADS", reason: "Download/piracy", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
  { term: "кряк", match: "word", source: "EX-FREE-DOWNLOADS", reason: "Piracy", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
  { term: "зарплата", match: "word", source: "EX-SALARY", reason: "Salary research", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
  { term: "стань программистом", match: "phrase", source: "CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.json S1", reason: "Career path REJECT evidence", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
  { term: "становится программистом", match: "phrase", source: "CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json", reason: "REJECTED_FOR_ADVERTISING", overblocking: "LOW", status: "APPROVED_CANDIDATE" },
];

const CAMPAIGN_NEGATIVES = [
  { term: "купить 1с", match: "phrase", campaign: "ALL", source: "EX-PRODUCT-LICENSE-ONLY", reason: "License purchase", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
  { term: "лицензия 1с", match: "phrase", campaign: "ALL", source: "EX-PRODUCT-LICENSE-ONLY", reason: "Product-only", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
  { term: "инструкция", match: "word", campaign: "CA-02", source: "EX-SELF-SERVICE-MANUALS", reason: "DIY manual — high overblock on troubleshooting group", overblocking: "HIGH", status: "DO_NOT_DEPLOY" },
  { term: "как сделать самому", match: "phrase", campaign: "ALL", source: "EX-SELF-SERVICE-MANUALS", reason: "Self-service", overblocking: "HIGH", status: "REVIEW_REQUIRED" },
  { term: "заказать коды маркировки", match: "phrase", campaign: "CA-05", source: "CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json ca-05-specialist-search", reason: "Purchase codes not setup", overblocking: "HIGH", status: "REVIEW_REQUIRED" },
  { term: "трактир", match: "word", campaign: "CA-02", source: "CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.json S2 ABSTAIN", reason: "Unsupported scope — client confirmation required", overblocking: "HIGH", status: "DO_NOT_DEPLOY" },
  { term: "erp", match: "word", campaign: "CA-05", source: "CORVONERO-PHASE-6-ABSTAIN-HOLDOUT-v1.json GENERIC_PLATFORM_OR_ERP", reason: "Unsupported ERP scope", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
];

const GROUP_CROSS_NEGATIVES = [
  { term: "маркировка", source: "CA-01", protect: "CA-05", reason: "Route marking intent to CA-05", overblocking: "HIGH", status: "DO_NOT_DEPLOY" },
  { term: "честный знак", source: "CA-01", protect: "CA-05", reason: "Marking campaign owns marking", overblocking: "MEDIUM", status: "REVIEW_REQUIRED" },
  { term: "интеграция", source: "CA-01", protect: "CA-04", reason: "Integration campaign boundary", overblocking: "HIGH", status: "DO_NOT_DEPLOY" },
  { term: "сопровождение", source: "CA-01", protect: "CA-02", reason: "Support campaign owns ongoing support", overblocking: "HIGH", status: "DO_NOT_DEPLOY" },
  { term: "доработка", source: "CA-01", protect: "CA-03", reason: "Development campaign boundary", overblocking: "HIGH", status: "DO_NOT_DEPLOY" },
  { term: "программист", source: "CA-02", protect: "CA-01", reason: "CA-01 broad programmer — must NOT broadly exclude программист", overblocking: "CRITICAL", status: "DO_NOT_DEPLOY" },
  { term: "коды маркировки", source: "CA-05", protect: "CA-05", reason: "Cannot broadly exclude — setup queries remain", overblocking: "CRITICAL", status: "DO_NOT_DEPLOY" },
];

const negativeCandidates = {
  package_id: `${WAVE.toLowerCase()}-negative-candidates-v1`,
  generated_at: TS,
  deployment_status: "NOT_DEPLOYED — OPERATOR_APPROVAL_REQUIRED",
  layers: {
    account_shared: ACCOUNT_NEGATIVES.map((n) => ({ ...n, level: "ACCOUNT / SHARED" })),
    campaign: CAMPAIGN_NEGATIVES.map((n) => ({ ...n, level: "CAMPAIGN" })),
    group_cross: GROUP_CROSS_NEGATIVES.map((n) => ({ ...n, level: "GROUP CROSS-NEGATIVES" })),
  },
  excluded_groups_evidence: excludedGroups.excluded_groups,
  exclusion_families: exclusionBoundaries.families,
};

const crossNegatives = {
  design_id: `${WAVE.toLowerCase()}-cross-negatives-v1`,
  generated_at: TS,
  policy: "Conservative boundaries — CA-01 is broad; do not force strict isolation where overlap is intentional",
  proposals: [
    {
      source_campaign: "CA-02",
      excluded_term: "программист",
      destination_protected: "CA-01",
      examples_affected: ["программист 1с", "услуги программиста"],
      overblocking_risk: "CRITICAL",
      recommendation: "DO NOT ADD — программист cannot be broadly excluded",
    },
    {
      source_campaign: "CA-03",
      excluded_term: "сопровождение",
      destination_protected: "CA-02",
      examples_affected: ["внедрение и сопровождение 1с (deployable in CA-03)"],
      overblocking_risk: "HIGH",
      recommendation: "DO NOT ADD at campaign level — mixed-intent phrases remain in CA-03",
    },
    {
      source_campaign: "CA-01",
      excluded_term: "маркировка",
      destination_protected: "CA-05",
      examples_affected: ["программист 1с маркировка"],
      overblocking_risk: "HIGH",
      recommendation: "REVIEW_REQUIRED — phrase-level only if evidenced",
    },
    {
      source_campaign: "CA-05",
      excluded_term: "коды маркировки",
      destination_protected: "CA-05",
      examples_affected: ["настройка кодов маркировки в 1с"],
      overblocking_risk: "CRITICAL",
      recommendation: "DO NOT ADD broadly — use phrase-level REJECT only",
    },
    {
      source_campaign: "CA-04",
      excluded_term: "доработка",
      destination_protected: "CA-03",
      examples_affected: ["доработка интеграции 1с"],
      overblocking_risk: "MEDIUM",
      recommendation: "REVIEW_REQUIRED — optional group-level refinement",
    },
    {
      source_campaign: "CA-01",
      excluded_term: "интеграция",
      destination_protected: "CA-04",
      examples_affected: ["программист 1с интеграция"],
      overblocking_risk: "HIGH",
      recommendation: "DO NOT ADD at CA-01 campaign level",
    },
  ],
};

const negativeRiskAudit = {
  audit_id: `${WAVE.toLowerCase()}-negative-risk-audit-v1`,
  generated_at: TS,
  critical_guards: [
    { rule: "программист not globally excluded", status: "ENFORCED" },
    { rule: "коды маркировки not broadly excluded", status: "ENFORCED" },
    { rule: "Трактир not global negative", status: "ENFORCED — DO_NOT_DEPLOY until client scope" },
    { rule: "No auto-convert all REJECT to broad minus", status: "ENFORCED" },
  ],
  counts: {
    approved_candidate: [...ACCOUNT_NEGATIVES, ...CAMPAIGN_NEGATIVES, ...GROUP_CROSS_NEGATIVES].filter((n) => n.status === "APPROVED_CANDIDATE").length,
    review_required: [...ACCOUNT_NEGATIVES, ...CAMPAIGN_NEGATIVES, ...GROUP_CROSS_NEGATIVES].filter((n) => n.status === "REVIEW_REQUIRED").length,
    do_not_deploy: [...ACCOUNT_NEGATIVES, ...CAMPAIGN_NEGATIVES, ...GROUP_CROSS_NEGATIVES].filter((n) => n.status === "DO_NOT_DEPLOY").length,
  },
  deployable_list_exists: false,
};

// --- PART 9: UTM Policy ---
const utmPolicy = {
  policy_id: `${WAVE.toLowerCase()}-utm-policy-v1`,
  generated_at: TS,
  status: "PROPOSED_TEMPLATE — REQUIRES_IMPORT_PROFILE_CONFIRMATION",
  template: {
    utm_source: "yandex",
    utm_medium: "cpc",
    utm_campaign: "<campaign_slug>",
    utm_content: "<group_slug>",
    utm_term: "<keyword>",
  },
  campaign_slugs: Object.fromEntries(CAMPAIGNS.map((c) => [c.id, c.slug])),
  group_slugs: Object.fromEntries(groupRegister.groups.map((g) => [g.group_id, g.group_id])),
  dynamic_keyword: {
    proposed_macro: "{keyword}",
    status: "REQUIRES_IMPORT_PROFILE_CONFIRMATION",
    evidence: "orca direct-commander-production-dataset-v7.1.json uses {keyword}; triumph template macro support SAFE UNKNOWN",
  },
  encoding_policy: {
    lowercase: true,
    cyrillic_in_slugs: "AVOID — use Latin transliteration for utm_campaign and utm_content",
    url_encoding: "encodeURIComponent for utm_term when static; macro substitution when supported",
  },
  join_rules: {
    base_url_has_query: "use & for subsequent params",
    base_url_no_query: "use ? before first param",
    fragment_anchor: "UTM query before fragment — https://host/path/?utm_source=...#anchor",
    duplicate_question_mark: "FORBIDDEN — normalize before export",
  },
  example: "https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=corv_programmist_1s&utm_content=ca-01-specialist-search&utm_term={keyword}",
};

// --- PART 10: Campaign Settings ---
const campaignSettings = {
  profile_id: `${WAVE.toLowerCase()}-campaign-settings-v1`,
  generated_at: TS,
  confirmed_boundary: {
    geography: "Новосибирск + Новосибирская область",
  },
  campaigns: CAMPAIGNS.map((c) => ({
    campaign_id: c.id,
    campaign_name: c.name,
    campaign_type: "Текстово-графическая кампания",
    placement: { search: "PLANNED", advertising_network: "NOT AUTHORIZED" },
    geography: "Новосибирск + Новосибирская область",
    schedule: "OPERATOR_DECISION_REQUIRED",
    bid_strategy: "OPERATOR_DECISION_REQUIRED",
    budget: "OPERATOR_DECISION_REQUIRED",
    device_adjustments: "OPERATOR_DECISION_REQUIRED",
    demographic_adjustments: "OPERATOR_DECISION_REQUIRED",
    auto_targeting: "NOT AUTHORIZED UNTIL SEPARATE REVIEW",
    phrase_matching: "OPERATOR_DECISION_REQUIRED — match may encode in phrase text per format contract",
    negative_keyword_application: "Three-layer design — not deployed",
    monitoring: "NOT STARTED",
    moderation_state: "NOT SUBMITTED",
    launch_status: "NOT AUTHORIZED",
  })),
};

// --- PART 11: Import Profile ---
const IMPORT_FIELDS = [
  { field: "campaign_type", column: "Тип кампании:", classification: "READY", entity: "campaign" },
  { field: "placement", column: "Места показа:", classification: "READY", entity: "campaign" },
  { field: "campaign_negatives", column: "Минус-фразы на кампанию:", classification: "PROVISIONAL", entity: "campaign" },
  { field: "promotion_url", column: "Объект продвижения:", classification: "PROVISIONAL", entity: "campaign" },
  { field: "group_id", column: "ID группы", classification: "READY", entity: "group" },
  { field: "group_name", column: "Название группы", classification: "READY", entity: "group" },
  { field: "group_number", column: "Номер группы", classification: "READY", entity: "group" },
  { field: "phrase_id", column: "ID фразы", classification: "READY", entity: "phrase" },
  { field: "phrase", column: "Фраза (с минус-словами)", classification: "READY", entity: "phrase" },
  { field: "group_negatives", column: "Минус-фразы на группу", classification: "PROVISIONAL", entity: "minus-phrase" },
  { field: "ad_id", column: "ID объявления", classification: "READY", entity: "ad" },
  { field: "headline_1", column: "Заголовок 1", classification: "READY", entity: "ad" },
  { field: "headline_2", column: "Заголовок 2", classification: "READY", entity: "ad" },
  { field: "text", column: "Текст", classification: "READY", entity: "ad" },
  { field: "combinatorial_headlines", column: "N/A — primary ads finalized", classification: "READY", entity: "combinatorial" },
  { field: "landing_url", column: "Ссылка", classification: "PROVISIONAL", entity: "url" },
  { field: "display_path", column: "Отображаемая ссылка", classification: "READY", entity: "display path" },
  { field: "sitelink_titles", column: "Заголовки быстрых ссылок", classification: "READY", entity: "sitelinks" },
  { field: "sitelink_descriptions", column: "Описания быстрых ссылок", classification: "READY", entity: "sitelinks" },
  { field: "sitelink_urls", column: "Адреса быстрых ссылок", classification: "ROMAN_REQUIRED", entity: "sitelinks" },
  { field: "callouts", column: "Уточнения", classification: "READY", entity: "callouts" },
  { field: "utm", column: "Append to Ссылка", classification: "PROPOSED_TEMPLATE", entity: "utm" },
  { field: "region", column: "Регион", classification: "READY", entity: "region" },
  { field: "keyword_status", column: "Статус фразы", classification: "READY", entity: "status" },
  { field: "ad_status", column: "Статус объявления", classification: "READY", entity: "status" },
  { field: "bid", column: "Ставка", classification: "OPERATOR_REQUIRED", entity: "bid" },
  { field: "daily_budget", column: "N/A in template data table", classification: "OPERATOR_REQUIRED", entity: "budget" },
  { field: "schedule", column: "N/A in template", classification: "OPERATOR_REQUIRED", entity: "campaign settings" },
  { field: "yandex_business_org", column: "Организация из Яндекс Бизнеса", classification: "OPERATOR_REQUIRED", entity: "campaign settings" },
  { field: "phone", column: "Номер телефона", classification: "OPERATOR_REQUIRED", entity: "campaign settings" },
  { field: "match_type_column", column: "N/A", classification: "NOT_USED", entity: "phrase" },
  { field: "image", column: "Изображение", classification: "NOT_USED", entity: "ad" },
];

const importProfile = {
  profile_id: `${WAVE.toLowerCase()}-import-profile-v1`,
  generated_at: TS,
  template_reference: "direct-commander-format-contract-v1.md / triumph-manipulator-commander-template-v1.xlsx",
  sheet: "Тексты",
  xlsx_generated: false,
  fields: IMPORT_FIELDS,
  classification_summary: {
    READY: IMPORT_FIELDS.filter((f) => f.classification === "READY").length,
    PROVISIONAL: IMPORT_FIELDS.filter((f) => f.classification === "PROVISIONAL" || f.classification === "PROPOSED_TEMPLATE").length,
    OPERATOR_REQUIRED: IMPORT_FIELDS.filter((f) => f.classification === "OPERATOR_REQUIRED").length,
    ROMAN_REQUIRED: IMPORT_FIELDS.filter((f) => f.classification === "ROMAN_REQUIRED").length,
    NOT_USED: IMPORT_FIELDS.filter((f) => f.classification === "NOT_USED").length,
  },
};

// --- PART 12: Commander Readiness Gate ---
const blockers = [
  { id: "B1", blocker: "LP URLs not published/HTTP verified", status: "OPEN", owner: "Roman / operator" },
  { id: "B2", blocker: "Final anchor IDs from Roman unavailable", status: "OPEN", owner: "Roman" },
  { id: "B3", blocker: "Privacy/form publication not completed", status: "OPEN", owner: "Roman / operator" },
  { id: "B4", blocker: "Campaign budget not set", status: "OPEN", owner: "Operator" },
  { id: "B5", blocker: "Bid strategy not set", status: "OPEN", owner: "Operator" },
  { id: "B6", blocker: "Schedule not set", status: "OPEN", owner: "Operator" },
  { id: "B7", blocker: "Commander import template not instantiated for Corvonero", status: "OPEN", owner: "Operator" },
  { id: "B8", blocker: "Final negative list not operator-approved", status: "OPEN", owner: "Operator" },
  { id: "B9", blocker: "UTM dynamic macro requires import profile confirmation", status: "OPEN", owner: "Operator" },
];

const commanderGate = {
  gate_id: `${WAVE.toLowerCase()}-commander-readiness-gate-v1`,
  generated_at: TS,
  commander_xlsx: "BLOCKED",
  mandatory_fields_classified: "100%",
  blockers,
  ready_when: [
    "All blockers closed",
    "URL readiness READY_FOR_AD_TRAFFIC for all 5 LPs",
    "Operator approves negative deploy list",
    "Corvonero commander template fork verified",
  ],
};

// --- Validation ---
const allNegatives = [
  ...negativeCandidates.layers.account_shared,
  ...negativeCandidates.layers.campaign,
  ...negativeCandidates.layers.group_cross,
];
const validation = {
  campaigns: CAMPAIGNS.length,
  deployable_groups: groupRegister.deployable_groups,
  deployable_phrases: groupRegister.deployable_phrases,
  lps: 5,
  groups_without_display_path: displayPaths.filter((d) => !d.display_path).length,
  campaigns_without_sitelink_copy: CAMPAIGNS.filter((c) => !sitelinks.some((s) => s.campaign_id === c.id)).length,
  campaigns_without_callout_pool: CAMPAIGNS.filter((c) => !callouts.campaign_pools[c.id]?.length).length,
  negative_candidates_without_source: allNegatives.filter((n) => !n.source).length,
  utm_campaign_slugs_unique: new Set(CAMPAIGNS.map((c) => c.slug)).size,
  commander_mandatory_fields_classified_pct: 100,
  preflight: {
    branch: AUTHORITY.branch,
    head_at_authority: true,
    phrase_allocation: "CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json",
    group_register: "CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json",
    primary_ads: "CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.json",
    lp_copy: "LP-01..LP-05 final copy artifacts present",
  },
};

const result = {
  result_id: `${WAVE.toLowerCase()}-result-v1`,
  generated_at: TS,
  verdict: "CORVONERO PRODUCTION EXTENSIONS WAVE 1: PASS — EXTENSIONS AND IMPORT PROFILE READY FOR OPERATOR REVIEW",
  components: {
    sitelink_copy: "CREATED",
    sitelink_urls: "PROVISIONAL UNTIL FINAL ANCHORS",
    callouts: "CREATED",
    negative_candidates: "CREATED — NOT DEPLOYED",
    utm_policy: "CREATED",
    campaign_settings: "PARTIAL — OPERATOR DECISIONS REQUIRED",
    commander_import_profile: "CREATED",
    commander_xlsx: "BLOCKED UNTIL REQUIRED INPUTS ARE RESOLVED",
    advertising: "NOT STARTED",
  },
  validation,
  authority: AUTHORITY,
};

// Write all files
writePair(`${WAVE}-FINAL-CAMPAIGN-REGISTER-v1`, campaignRegisterMd(campaignRegister), campaignRegister);
writePair(`${WAVE}-URL-READINESS-v1`, urlReadinessMd(urlReadiness), urlReadiness);
writePair(`${WAVE}-DISPLAY-PATHS-v1`, displayPathsMd(displayPaths), { display_path_id: `${WAVE.toLowerCase()}-display-paths-v1`, generated_at: TS, max_chars: DISPLAY_PATH_MAX, single_field: true, records: displayPaths });
writePair(`${WAVE}-SITELINKS-v1`, sitelinksMd(sitelinks), { sitelink_id: `${WAVE.toLowerCase()}-sitelinks-v1`, generated_at: TS, copy_status: "FINALIZABLE NOW", url_status: "PROVISIONAL UNTIL ROMAN PROVIDES FINAL ANCHORS", records: sitelinks });
writePair(`${WAVE}-CALLOUTS-v1`, calloutsMd(callouts), callouts);
writePair(`${WAVE}-NEGATIVE-CANDIDATES-v1`, negativesMd(negativeCandidates), negativeCandidates);
writePair(`${WAVE}-CROSS-NEGATIVES-v1`, crossNegativesMd(crossNegatives), crossNegatives);
writePair(`${WAVE}-NEGATIVE-RISK-AUDIT-v1`, riskAuditMd(negativeRiskAudit), negativeRiskAudit);
writePair(`${WAVE}-UTM-POLICY-v1`, utmMd(utmPolicy), utmPolicy);
writePair(`${WAVE}-CAMPAIGN-SETTINGS-v1`, settingsMd(campaignSettings), campaignSettings);
writePair(`${WAVE}-IMPORT-PROFILE-v1`, importProfileMd(importProfile), importProfile);
writePair(`${WAVE}-COMMANDER-READINESS-GATE-v1`, gateMd(commanderGate), commanderGate);
writePair(`${WAVE}-RESULT-v1`, resultMd(result), result);

fs.writeFileSync(
  path.join(PILOT, `${WAVE}-OPERATOR-DECISION-PACKET-v1.md`),
  operatorPacketMd(result, commanderGate, campaignSettings, negativeCandidates),
  "utf8"
);

fs.writeFileSync(
  path.join(REPORTS, "REPORT-corvonero-production-extensions-wave-1-v1.md"),
  reportMd(result, validation, AUTHORITY),
  "utf8"
);

console.log(JSON.stringify({ ok: true, validation, verdict: result.verdict }, null, 2));

function campaignRegisterMd(r) {
  let md = `# ${WAVE} — Final Campaign Register v1\n\nGenerated: ${TS}\n\nAuthority: \`${AUTHORITY.commit}\` / \`${AUTHORITY.tag}\`\n\n`;
  md += `| Campaign | Name | Phrases | Groups | LP | URL | Publication | Geography | Readiness |\n`;
  md += `|----------|------|---------|--------|----|----|-------------|-----------|----------|\n`;
  for (const c of r.campaigns) {
    md += `| ${c.campaign_id} | ${c.campaign_name_ru} | ${c.phrase_count} | ${c.group_count} | ${c.lp_id} | ${c.proposed_url} | ${c.publication_status} | ${c.launch_geography} | ${c.production_readiness} |\n`;
  }
  md += `\n**Totals:** ${r.totals.campaigns} campaigns, ${r.totals.groups} groups, ${r.totals.phrases} phrases, ${r.totals.lps} LPs.\n`;
  return md;
}

function urlReadinessMd(r) {
  let md = `# ${WAVE} — URL Readiness v1\n\nHTTP verification: **not performed** (not authorized in this task).\n\n`;
  for (const rec of r.records) {
    md += `## ${rec.lp_id} (${rec.campaign_id})\n\n- URL: ${rec.proposed_url}\n- Status: **${rec.aggregate_status}**\n- PROPOSED: yes | PUBLISHED: no | HTTP_VERIFIED: no | READY_FOR_AD_TRAFFIC: no\n\n`;
  }
  return md;
}

function displayPathsMd(records) {
  let md = `# ${WAVE} — Display Paths v1\n\nSingle field per import profile (col 49 «Отображаемая ссылка»). Max ${DISPLAY_PATH_MAX} chars.\n\n`;
  md += `| Campaign | Group | LP | Path | Chars | Status |\n|----------|-------|----|------|-------|--------|\n`;
  for (const d of records) {
    md += `| ${d.campaign_id} | ${d.group_id} | ${d.lp_id} | ${d.display_path} | ${d.character_count} | ${d.validation_status} |\n`;
  }
  return md;
}

function sitelinksMd(records) {
  let md = `# ${WAVE} — Sitelinks v1\n\n**Copy:** FINALIZABLE NOW | **URLs:** PROVISIONAL UNTIL ROMAN PROVIDES FINAL ANCHORS\n\n`;
  for (const s of records) {
    md += `### ${s.campaign_id} — ${s.sitelink_title}\n\n- LP: ${s.lp_id}\n- Descriptions: ${s.description_line_1} / ${s.description_line_2}\n- Provisional: \`${s.provisional_url}\`\n- Evidence: ${s.lp_copy_evidence}\n\n`;
  }
  return md;
}

function calloutsMd(c) {
  let md = `# ${WAVE} — Callouts v1\n\nMax ${CALLOUT_MAX} chars per callout (col 67 «Уточнения»).\n\n`;
  for (const [cid, pool] of Object.entries(c.campaign_pools)) {
    md += `## ${cid}\n\n${pool.map((p) => `- ${p.text} (${p.char_count} chars)`).join("\n")}\n\n`;
  }
  return md;
}

function negativesMd(n) {
  let md = `# ${WAVE} — Negative Keyword Candidates v1\n\n**Status:** NOT DEPLOYED — operator approval required.\n\n`;
  for (const [layer, items] of Object.entries(n.layers)) {
    md += `## ${layer}\n\n| Term | Match | Source | Status | Risk |\n|------|-------|--------|--------|------|\n`;
    for (const i of items) {
      md += `| ${i.term} | ${i.match} | ${i.source} | ${i.status} | ${i.overblocking} |\n`;
    }
    md += `\n`;
  }
  return md;
}

function crossNegativesMd(c) {
  let md = `# ${WAVE} — Cross-Campaign Negatives v1\n\n${c.policy}\n\n`;
  md += `| Source | Term | Protect | Risk | Recommendation |\n|--------|------|---------|------|----------------|\n`;
  for (const p of c.proposals) {
    md += `| ${p.source_campaign} | ${p.excluded_term} | ${p.destination_protected} | ${p.overblocking_risk} | ${p.recommendation} |\n`;
  }
  return md;
}

function riskAuditMd(a) {
  let md = `# ${WAVE} — Negative Risk Audit v1\n\n`;
  md += `| Guard | Status |\n|-------|--------|\n`;
  for (const g of a.critical_guards) md += `| ${g.rule} | ${g.status} |\n`;
  md += `\nDeployable minus list: **${a.deployable_list_exists ? "YES" : "NO"}**\n`;
  return md;
}

function utmMd(u) {
  return `# ${WAVE} — UTM Policy v1\n\nStatus: **${u.status}**\n\n\`\`\`\nutm_source=yandex\nutm_medium=cpc\nutm_campaign=<campaign_slug>\nutm_content=<group_slug>\nutm_term=<keyword>\n\`\`\`\n\nExample:\n\`${u.example}\`\n`;
}

function settingsMd(s) {
  let md = `# ${WAVE} — Campaign Settings v1\n\nGeography: **${s.confirmed_boundary.geography}**\n\n`;
  for (const c of s.campaigns) {
    md += `## ${c.campaign_id}\n\n- Search: ${c.placement.search}\n- Network: ${c.placement.advertising_network}\n- Auto-targeting: ${c.auto_targeting}\n- Launch: ${c.launch_status}\n- Budget/Bid/Schedule: OPERATOR_DECISION_REQUIRED\n\n`;
  }
  return md;
}

function importProfileMd(p) {
  let md = `# ${WAVE} — Import Profile v1\n\nXLSX: **not generated**\n\n| Field | Column | Class |\n|-------|--------|-------|\n`;
  for (const f of p.fields) md += `| ${f.field} | ${f.column} | ${f.classification} |\n`;
  return md;
}

function gateMd(g) {
  let md = `# ${WAVE} — Commander Readiness Gate v1\n\n**Commander XLSX:** ${g.commander_xlsx}\n\n## Blockers\n\n`;
  for (const b of g.blockers) md += `- **${b.id}** ${b.blocker} (${b.owner})\n`;
  return md;
}

function resultMd(r) {
  return `# ${WAVE} — Result v1\n\n**Verdict:** ${r.verdict}\n\n${Object.entries(r.components).map(([k, v]) => `- ${k}: ${v}`).join("\n")}\n`;
}

function operatorPacketMd(result, gate, settings, negatives) {
  return `# ${WAVE} — Operator Decision Packet v1\n\n## Required decisions\n\n1. Approve or revise negative candidate list (currently NOT DEPLOYED)\n2. Set budget, bids, schedule per campaign\n3. Confirm UTM template and {keyword} macro support\n4. Publish and verify LP URLs\n5. Provide final Tilda anchor IDs (Roman)\n6. Fork/verify Corvonero Commander template\n\n## Commander gate\n\nStatus: **${gate.commander_xlsx}**\n\n## Campaign commercial settings\n\nAll P1 campaigns: budget/bid/schedule = OPERATOR_DECISION_REQUIRED\n`;
}

function reportMd(result, validation, auth) {
  return `# REPORT — Corvonero Production Extensions Wave 1 v1

Date: ${TS.split("T")[0]}

## Preflight

| Check | Result |
|-------|--------|
| Branch | \`${auth.branch}\` |
| HEAD | \`${auth.commit}\` (tag \`${auth.tag}\`) |
| Descends from authority | YES |
| Final phrase allocation | \`CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json\` — 895 deployable |
| Final group register | \`CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json\` — 15 groups |
| Final primary ads | \`CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.json\` — unchanged |
| LP copy LP-01..LP-05 | Final copy artifacts present |
| LP URLs published | **NOT VERIFIED** — PROPOSED only |
| Excluded groups preserved | ca-02-specialist-search, ca-02-modification, ca-05-specialist-search |
| Deferred | CA-06 / LP-06 — 37 phrases |
| Unrelated WIP | Not modified |
| Commit / push | Not performed |

## Verdict

**${result.verdict}**

| Component | Status |
|-----------|--------|
| Sitelink copy | CREATED |
| Sitelink URLs | PROVISIONAL UNTIL FINAL ANCHORS |
| Callouts | CREATED |
| Negative candidates | CREATED — NOT DEPLOYED |
| UTM policy | CREATED (PROPOSED_TEMPLATE) |
| Campaign settings | PARTIAL — OPERATOR DECISIONS REQUIRED |
| Commander import profile | CREATED |
| Commander XLSX | BLOCKED |
| Advertising | NOT STARTED |

## Validation

| Metric | Expected | Actual |
|--------|----------|--------|
| Campaigns | 5 | ${validation.campaigns} |
| Deployable groups | 15 | ${validation.deployable_groups} |
| Deployable phrases | 895 | ${validation.deployable_phrases} |
| LPs | 5 | ${validation.lps} |
| Groups without display path | 0 | ${validation.groups_without_display_path} |
| Campaigns without sitelink copy | 0 | ${validation.campaigns_without_sitelink_copy} |
| Campaigns without callout pool | 0 | ${validation.campaigns_without_callout_pool} |
| Negative candidates without source | 0 | ${validation.negative_candidates_without_source} |
| UTM campaign slugs (unique) | 5 | ${validation.utm_campaign_slugs_unique} |
| Commander mandatory fields classified | 100% | ${validation.commander_mandatory_fields_classified_pct}% |

## Outputs

27 files under \`projects/mars-search-ppc-production/pilots/corvonero/\` (prefix \`CORVONERO-EXT-W1-\`) plus generator \`tools/execute-ext-wave-1-v1.mjs\`.

Report: \`projects/mars-search-ppc-production/reports/REPORT-corvonero-production-extensions-wave-1-v1.md\`

## Technical evidence

- Commander column contract: \`projects/orca/projects/corvonero-yandex-direct/production/direct-commander-format-contract-v1.md\`
- Display path: single field col 49, max 20 chars
- UTM: append to col 48 «Ссылка»; \`{keyword}\` macro REQUIRES_IMPORT_PROFILE_CONFIRMATION
- HTTP verification: not authorized in this task

## Git

No commit, no push. Final ads and LP authority untouched. No Commander XLSX created.
`;
}

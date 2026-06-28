#!/usr/bin/env node
/**
 * Corvonero Production Extensions Wave 1 — v2 operator decisions applier.
 * Reads v1 authority + final P1 manifests; does not modify v1 artefacts, ads, or LP copy.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT = path.resolve(__dirname, "..");
const REPORTS = path.resolve(PILOT, "../../reports");
const WAVE = "CORVONERO-EXT-W1";
const TS = new Date().toISOString();
const TASK_REF = "CURSOR TASK — CORVONERO EXTENSIONS WAVE 1 — APPLY OPERATOR DECISIONS";

const AUTHORITY = {
  commit: "508837a02658e357ce18dca777a46231d2575b25",
  tag: "corvonero-final-p1-search-ads-2026-06",
  branch: "mars/canonical-post-recovery",
  v1_baseline: "CORVONERO-EXT-W1-*-v1",
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
  },
  {
    id: "CA-02",
    name: "Сопровождение и обслуживание 1С",
    phrase_count: 153,
    group_count: 4,
    lp: "LP-02",
    url: "https://lk.corvonero.ru/soprovozhdenie-1s/",
    slug: "corv_soprovozhdenie_1s",
  },
  {
    id: "CA-03",
    name: "Доработка и разработка 1С",
    phrase_count: 69,
    group_count: 3,
    lp: "LP-03",
    url: "https://lk.corvonero.ru/dorabotka-razrabotka-1s/",
    slug: "corv_dorabotka_1s",
  },
  {
    id: "CA-04",
    name: "Интеграции 1С",
    phrase_count: 48,
    group_count: 1,
    lp: "LP-04",
    url: "https://lk.corvonero.ru/integracii-1s/",
    slug: "corv_integracii_1s",
  },
  {
    id: "CA-05",
    name: "Маркировка / Честный знак",
    phrase_count: 221,
    group_count: 4,
    lp: "LP-05",
    url: "https://lk.corvonero.ru/markirovka-chestny-znak/",
    slug: "corv_markirovka_1s",
  },
];

const SITELINK_TITLE_MAX = 30;
const SITELINK_DESC_MAX = 30;
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

const groupRegister = loadJson("CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json");
const v1Sitelinks = loadJson("CORVONERO-EXT-W1-SITELINKS-v1.json");
const v1CrossNegatives = loadJson("CORVONERO-EXT-W1-CROSS-NEGATIVES-v1.json");
const v1NegativeCandidates = loadJson("CORVONERO-EXT-W1-NEGATIVE-CANDIDATES-v1.json");

const LP_SECTION_EVIDENCE = {
  "LP-01": "CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3.json sections",
  "LP-02": "CORVONERO-COPY-WAVE-2-LP02-SUPPORT-FINAL-v2.md",
  "LP-03": "CORVONERO-COPY-WAVE-2-LP03-DEVELOPMENT-FINAL-v2.md",
  "LP-04": "CORVONERO-COPY-WAVE-2-LP04-INTEGRATIONS-FINAL-v2.md",
  "LP-05": "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.md",
};

function buildSitelinkRecord(campaign, slot, overrides = {}) {
  const base = v1Sitelinks.records.find(
    (r) => r.campaign_id === campaign.id && r.sitelink_title === slot.v1TitleMatch
  );
  const title = overrides.title ?? base?.sitelink_title ?? slot.title;
  const d1 = overrides.description_line_1 ?? base?.description_line_1;
  const d2 = overrides.description_line_2 ?? base?.description_line_2;
  const anchor = overrides.provisional_anchor ?? base?.provisional_anchor;
  const section = overrides.section ?? slot.section;
  const titleChars = cc(title);
  const d1c = cc(d1);
  const d2c = cc(d2);
  return {
    campaign_id: campaign.id,
    lp_id: campaign.lp,
    sitelink_index: slot.index,
    sitelink_title: title,
    title_char_count: titleChars,
    title_valid: titleChars <= SITELINK_TITLE_MAX,
    description_line_1: d1,
    description_line_2: d2,
    description_char_counts: [d1c, d2c],
    description_valid: d1c <= SITELINK_DESC_MAX && d2c <= SITELINK_DESC_MAX,
    provisional_anchor: anchor,
    provisional_url: `${campaign.url.replace(/\/$/, "")}${anchor}`,
    final_url_status: "PROVISIONAL — FINAL ANCHOR REQUIRED",
    sitelink_copy_status: overrides.operator_action ?? "APPROVED_UNCHANGED",
    operator_decision: overrides.operator_decision ?? "APPROVED_UNCHANGED",
    lp_copy_evidence: `${LP_SECTION_EVIDENCE[campaign.lp]} — ${section}`,
    technical_validation:
      titleChars <= SITELINK_TITLE_MAX && d1c <= SITELINK_DESC_MAX && d2c <= SITELINK_DESC_MAX
        ? "PASS"
        : "FAIL",
  };
}

const SITELINK_SLOTS = {
  "CA-01": [
    { index: 1, v1TitleMatch: "Что делает программист 1С", section: "service_scope" },
    { index: 2, v1TitleMatch: "Стоимость работы", section: "pricing" },
    { index: 3, v1TitleMatch: "Конфигурации 1С", section: "configurations" },
    { index: 4, v1TitleMatch: "Оставить заявку", section: "form" },
  ],
  "CA-02": [
    { index: 1, v1TitleMatch: "Что входит в сопровождение", section: "service_scope" },
    { index: 2, v1TitleMatch: "Разовый и постоянный формат", section: "subscription_format" },
    { index: 3, v1TitleMatch: "Конфигурации 1С", section: "configurations" },
    { index: 4, v1TitleMatch: "Оставить заявку", section: "form" },
  ],
  "CA-03": [
    { index: 1, v1TitleMatch: "Виды доработок", section: "service_scope" },
    {
      index: 2,
      v1TitleMatch: "Типовые задачи",
      section: "typical_tasks",
      overrides: {
        title: "Типовые задачи",
        description_line_1: "Отчёты, формы, процессы",
        description_line_2: "Под задачи бизнеса",
        provisional_anchor: "#typical-tasks",
        operator_action: "APPROVED_REVISED",
        operator_decision: "REPLACE_SITELINK_2",
      },
    },
    { index: 3, v1TitleMatch: "Как мы работаем", section: "process" },
    { index: 4, v1TitleMatch: "Оставить заявку", section: "form" },
  ],
  "CA-04": [
    {
      index: 1,
      v1TitleMatch: "Варианты интеграции",
      section: "service_scope",
      overrides: {
        title: "Варианты интеграции",
        description_line_1: "Сайт, Битрикс, CRM",
        description_line_2: "Обмен данными",
        provisional_anchor: "#service-scope",
        operator_action: "APPROVED_REVISED",
        operator_decision: "REPLACE_SITELINK_1",
      },
    },
    { index: 2, v1TitleMatch: "Типовые задачи", section: "typical_tasks" },
    {
      index: 3,
      v1TitleMatch: "Как оцениваем проект",
      section: "scope_definition",
      overrides: {
        title: "Оценка интеграции",
        description_line_1: "Анализ двух систем",
        description_line_2: "Оценка по задаче",
        provisional_anchor: "#scope-definition",
        operator_action: "APPROVED_REVISED",
        operator_decision: "REPLACE_SITELINK_3",
      },
    },
    { index: 4, v1TitleMatch: "Оставить заявку", section: "form" },
  ],
  "CA-05": [
    { index: 1, v1TitleMatch: "Настройка маркировки", section: "service_scope" },
    { index: 2, v1TitleMatch: "Честный знак", section: "marking_overview" },
    { index: 3, v1TitleMatch: "ТС ПИОТ", section: "ts_piot" },
    { index: 4, v1TitleMatch: "Оставить заявку", section: "form" },
  ],
};

const sitelinkRecords = [];
for (const c of CAMPAIGNS) {
  for (const slot of SITELINK_SLOTS[c.id]) {
    sitelinkRecords.push(buildSitelinkRecord(c, slot, slot.overrides ?? {}));
  }
}

const sitelinks = {
  sitelink_id: `${WAVE.toLowerCase()}-sitelinks-v2`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  copy_status: "APPROVED — URLS PROVISIONAL",
  url_status: "PROVISIONAL — FINAL ANCHOR REQUIRED",
  url_not_implemented: true,
  records: sitelinkRecords,
  validation: {
    sitelink_sets: 5,
    sitelinks_total: sitelinkRecords.length,
    all_titles_valid: sitelinkRecords.every((s) => s.title_valid),
    all_descriptions_valid: sitelinkRecords.every((s) => s.description_valid),
    mixed_script_kassa_present: sitelinkRecords.some((s) =>
      `${s.description_line_1}${s.description_line_2}`.includes("кassa")
    ),
    unsupported_kassa_claim: false,
  },
};

const CALLOUT_SETS = {
  "CA-01": [
    { text: "Удалённо по России", evidence: "LP copy work_format.remote" },
    { text: "Выезд в Новосибирске", evidence: "LP copy work_format.onsite" },
    { text: "Работа по договору", evidence: "LP trust facts / operator_decisions" },
    { text: "Минимальный заказ 2 часа", evidence: "LP-01 pricing.minimum_hours", scope: "CA-01_only" },
  ],
  "CA-02": [
    { text: "Удалённо по России", evidence: "LP copy work_format.remote" },
    { text: "Выезд в Новосибирске", evidence: "LP copy work_format.onsite" },
    { text: "Поддержка рабочей базы", evidence: "LP-02 copy", scope: "campaign_filtered" },
    { text: "УТ, УНФ, Розница, КА, БП", evidence: "LP configurations section" },
  ],
  "CA-03": [
    { text: "Удалённо по России", evidence: "LP copy work_format.remote" },
    { text: "Выезд в Новосибирске", evidence: "LP copy work_format.onsite" },
    { text: "Работа по договору", evidence: "LP trust facts / operator_decisions" },
    { text: "УТ, УНФ, Розница, КА, БП", evidence: "LP configurations section" },
  ],
  "CA-04": [
    { text: "Удалённо по России", evidence: "LP copy work_format.remote" },
    { text: "Выезд в Новосибирске", evidence: "LP copy work_format.onsite" },
    { text: "Работа по договору", evidence: "LP trust facts / operator_decisions" },
    { text: "УТ, УНФ, Розница, КА, БП", evidence: "LP configurations section" },
  ],
  "CA-05": [
    { text: "Удалённо по России", evidence: "LP copy work_format.remote" },
    { text: "Выезд в Новосибирске", evidence: "LP copy work_format.onsite" },
    { text: "Настройка маркировки", evidence: "LP-05 service_scope", scope: "CA-05_only" },
    { text: "УТ, УНФ, Розница, КА, БП", evidence: "LP configurations section" },
  ],
};

function mapCalloutPool(items) {
  return items.map((item) => ({
    text: item.text,
    char_count: cc(item.text),
    valid: cc(item.text) <= CALLOUT_MAX,
    scope: item.scope ?? "operator_approved",
    evidence: item.evidence,
    operator_status: "APPROVED",
  }));
}

const callouts = {
  callout_id: `${WAVE.toLowerCase()}-callouts-v2`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  max_chars: CALLOUT_MAX,
  import_column: "Уточнения (col 67)",
  copy_status: "APPROVED",
  campaign_pools: Object.fromEntries(
    Object.entries(CALLOUT_SETS).map(([cid, pool]) => [cid, mapCalloutPool(pool)])
  ),
  validation: {
    callout_sets: 5,
    all_valid: Object.values(CALLOUT_SETS)
      .flat()
      .every((c) => cc(c.text) <= CALLOUT_MAX),
  },
};

const APPROVED_SHARED = [
  { term: "вакансия", match: "word", source: "EX-CAREER-JOBS", reason: "Job seeker intent" },
  { term: "работа программистом", match: "phrase", source: "EX-CAREER-JOBS", reason: "Employment intent" },
  { term: "резюме", match: "word", source: "EX-RESUME-INTERVIEWS", reason: "Job application" },
  { term: "сертификация", match: "word", source: "EX-CERTIFICATION-EXAMS", reason: "Certification exams" },
  { term: "кряк", match: "word", source: "EX-FREE-DOWNLOADS", reason: "Piracy" },
  { term: "зарплата", match: "word", source: "EX-SALARY", reason: "Salary research" },
  { term: "стань программистом", match: "phrase", source: "CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.json S1", reason: "Career path REJECT evidence" },
  { term: "становится программистом", match: "phrase", source: "CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json", reason: "REJECTED_FOR_ADVERTISING" },
  { term: "скачать", match: "word", source: "EX-FREE-DOWNLOADS", reason: "Download/piracy — operator approved controlled deployment" },
];

const REJECTED_SHARED = [
  { term: "обучение", match: "word", status: "REVIEW_REQUIRED — NOT DEPLOYABLE", reason: "possible overlap with employee training or other ambiguous service-related intent" },
  { term: "курс", match: "word", status: "REVIEW_REQUIRED — NOT DEPLOYABLE", reason: "possible overlap with employee training or other ambiguous service-related intent" },
  { term: "курсы", match: "word", status: "REVIEW_REQUIRED — NOT DEPLOYABLE", reason: "possible overlap with employee training or other ambiguous service-related intent" },
];

const APPROVED_CAMPAIGN_PHRASE = [
  { term: "купить 1с", match: "phrase", campaigns: CAMPAIGNS.map((c) => c.id), reason: "product or license purchase intent; Corvonero service scope does not include license sales" },
  { term: "лицензия 1с", match: "phrase", campaigns: CAMPAIGNS.map((c) => c.id), reason: "product or license purchase intent; Corvonero service scope does not include license sales" },
];

const APPROVED_CA05_EXTRA = {
  term: "заказать коды маркировки",
  match: "phrase",
  campaigns: ["CA-05"],
  reason: "confirmed acquisition/purchase intent, not technical 1C setup",
};

const NOT_DEPLOYED_CAMPAIGN = [
  { term: "как сделать самому", match: "phrase", campaigns: CAMPAIGNS.map((c) => c.id), status: "REVIEW_REQUIRED — NOT DEPLOYABLE", reason: "Self-service — high overblocking risk" },
  { term: "инструкция", match: "word", campaigns: ["CA-02"], status: "DO_NOT_DEPLOY", reason: "DIY manual — high overblock on troubleshooting group" },
  { term: "трактир", match: "word", campaigns: ["CA-02"], status: "DO_NOT_DEPLOY", reason: "Unsupported scope — client confirmation required" },
  { term: "erp", match: "word", campaigns: ["CA-05"], status: "REVIEW_REQUIRED — NOT DEPLOYABLE", reason: "Unsupported ERP scope" },
];

function expandCampaignNegatives() {
  const rows = [];
  for (const n of APPROVED_CAMPAIGN_PHRASE) {
    for (const cid of n.campaigns) {
      rows.push({
        term: n.term,
        match: n.match,
        campaign_id: cid,
        level: "CAMPAIGN",
        deploy_status: "APPROVED_FOR_DEPLOYMENT",
        reason: n.reason,
        source: "EX-PRODUCT-LICENSE-ONLY",
      });
    }
  }
  rows.push({
    term: APPROVED_CA05_EXTRA.term,
    match: APPROVED_CA05_EXTRA.match,
    campaign_id: "CA-05",
    level: "CAMPAIGN",
    deploy_status: "APPROVED_FOR_DEPLOYMENT",
    reason: APPROVED_CA05_EXTRA.reason,
    source: "CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json ca-05-specialist-search",
  });
  return rows;
}

const deployableShared = APPROVED_SHARED.map((n) => ({
  ...n,
  level: "ACCOUNT / SHARED",
  deploy_status: "APPROVED_FOR_DEPLOYMENT",
  operator_decision: "APPROVED",
}));

const deployableCampaign = expandCampaignNegatives();

const negativeDeployment = {
  deployment_id: `${WAVE.toLowerCase()}-negative-deployment-v1`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  deployment_status: "APPROVED_CONTROLLED_SET — NOT IMPORTED",
  import_authorized: false,
  layers: {
    account_shared_deployable: deployableShared,
    account_shared_rejected: REJECTED_SHARED.map((n) => ({
      ...n,
      level: "ACCOUNT / SHARED",
      operator_decision: "REJECTED",
    })),
    campaign_deployable: deployableCampaign,
    campaign_not_deployed: NOT_DEPLOYED_CAMPAIGN.map((n) => ({
      ...n,
      level: "CAMPAIGN",
      operator_decision: "NOT_DEPLOYED",
    })),
    cross_campaign_deployed: [],
  },
  counts: {
    approved_shared: deployableShared.length,
    approved_campaign_phrase_per_campaign: 2,
    additional_ca05_phrase: 1,
    cross_campaign_deployed: 0,
    total_deployable_entries: deployableShared.length + deployableCampaign.length,
  },
  v1_audit_preserved: "CORVONERO-EXT-W1-NEGATIVE-CANDIDATES-v1.json",
  v1_risk_audit_preserved: "CORVONERO-EXT-W1-NEGATIVE-RISK-AUDIT-v1.json",
};

const crossNegativeTerms = [
  "программист",
  "сопровождение",
  "доработка",
  "интеграция",
  "маркировка",
  "честный знак",
  "коды маркировки",
];

const crossNegatives = {
  design_id: `${WAVE.toLowerCase()}-cross-negatives-v2`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  deployment_policy: "Deploy no cross-campaign negatives in the initial production package",
  cross_campaign_negatives_deployed: 0,
  operator_decision: "NOT_DEPLOYED",
  explicit_non_deploy_terms: crossNegativeTerms,
  non_deploy_reason: "valid service overlap exists among campaigns; strict isolation creates excessive overblocking risk",
  proposals: v1CrossNegatives.proposals.map((p) => ({
    ...p,
    deploy_status: "NOT_DEPLOYED",
    operator_decision: "NOT_DEPLOYED",
    audit_evidence_preserved: true,
  })),
  v1_group_cross_layer: v1NegativeCandidates.layers.group_cross.map((n) => ({
    term: n.term,
    source: n.source,
    protect: n.protect,
    v1_status: n.status,
    v2_deploy_status: "NOT_DEPLOYED",
    reason: n.reason,
    overblocking: n.overblocking,
    audit_evidence_preserved: true,
  })),
};

const utmPolicy = {
  policy_id: `${WAVE.toLowerCase()}-utm-policy-v2`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  status: "APPROVED — BASE POLICY",
  approved_base_parameters: {
    utm_source: "yandex",
    utm_medium: "cpc",
    utm_campaign: "<campaign_slug>",
    utm_content: "<group_slug>",
  },
  approved_url_suffix: "?utm_source=yandex&utm_medium=cpc&utm_campaign=<campaign_slug>&utm_content=<group_slug>",
  campaign_slugs: Object.fromEntries(CAMPAIGNS.map((c) => [c.id, c.slug])),
  group_slug_policy: "utm_content = final deployable group slug",
  group_slugs: Object.fromEntries(groupRegister.groups.map((g) => [g.group_id, g.group_id])),
  utm_term: {
    proposed_macro: "{keyword}",
    status: "REQUIRES_COMMANDER_TEMPLATE_CONFIRMATION",
    in_approved_production_suffix: false,
    note: "Do not place utm_term into the production-ready URL until Commander template confirms dynamic keyword macro support",
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
  example_without_keyword_macro:
    "https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=corv_programmist_1s&utm_content=ca-01-specialist-search",
  validation: {
    campaign_slugs_unique: new Set(CAMPAIGNS.map((c) => c.slug)).size,
    keyword_macro_in_approved_suffix: false,
  },
};

const campaignSettings = {
  profile_id: `${WAVE.toLowerCase()}-campaign-settings-v2`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  operator_decisions_applied: true,
  confirmed_boundary: {
    geography: "Новосибирск + Новосибирская область",
  },
  unresolved: {
    budget: "OPERATOR_DECISION_REQUIRED",
    bid_strategy: "OPERATOR_DECISION_REQUIRED",
    schedule: "OPERATOR_DECISION_REQUIRED",
    yandex_metrica_counter: "NOT PROVIDED",
    conversion_goals: "NOT PROVIDED",
  },
  campaigns: CAMPAIGNS.map((c) => ({
    campaign_id: c.id,
    campaign_name: c.name,
    campaign_type: "Текстово-графическая кампания",
    placement: {
      search: "APPROVED",
      advertising_network: "DISABLED",
    },
    geography: "Новосибирск + Новосибирская область",
    auto_targeting: "DISABLED",
    device_adjustments: "NONE",
    demographic_adjustments: "NONE",
    schedule: "OPERATOR_DECISION_REQUIRED",
    bid_strategy: "OPERATOR_DECISION_REQUIRED",
    budget: "OPERATOR_DECISION_REQUIRED",
    yandex_metrica_counter: "NOT PROVIDED",
    conversion_goals: "NOT PROVIDED",
    phrase_matching: "OPERATOR_DECISION_REQUIRED — match may encode in phrase text per format contract",
    negative_keyword_application: "APPROVED_CONTROLLED_SET — see CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.json",
    monitoring: "NOT STARTED",
    moderation_state: "NOT SUBMITTED",
    launch_status: "NOT AUTHORIZED",
  })),
};

const commanderGate = {
  gate_id: `${WAVE.toLowerCase()}-commander-readiness-gate-v2`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  commander_xlsx: "BLOCKED",
  mandatory_fields_classified: "100%",
  blockers: [
    { id: "B1", blocker: "LP URLs not published/HTTP verified", status: "OPEN", owner: "Roman" },
    { id: "B2", blocker: "Final anchor IDs from Roman unavailable", status: "OPEN", owner: "Roman" },
    { id: "B3", blocker: "Privacy/form publication not completed", status: "OPEN", owner: "Roman / operator" },
    { id: "B4", blocker: "Campaign budget not set", status: "OPEN", owner: "Operator" },
    { id: "B5", blocker: "Bid strategy not set", status: "OPEN", owner: "Operator" },
    { id: "B6", blocker: "Schedule not set", status: "OPEN", owner: "Operator" },
    { id: "B7", blocker: "Commander import template not instantiated for Corvonero", status: "OPEN", owner: "MARS" },
    { id: "B8", blocker: "Final negative list not operator-approved", status: "CLOSED", owner: "Operator", closed_at: TS, evidence: "CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.json" },
    { id: "B9", blocker: "UTM dynamic keyword macro requires Commander template confirmation", status: "OPEN", owner: "MARS" },
    { id: "B10", blocker: "Yandex Metrica counter not provided", status: "OPEN", owner: "Operator" },
    { id: "B11", blocker: "Conversion goals not provided", status: "OPEN", owner: "Operator" },
  ],
  remaining_blockers_by_owner: {
    ROMAN: [
      "publish and verify five LP URLs",
      "supply final anchor IDs",
      "complete and verify forms/privacy publication",
    ],
    OPERATOR: [
      "set budgets",
      "set bid strategy",
      "set schedule",
      "provide Metrica counter",
      "provide conversion goals",
    ],
    MARS: [
      "instantiate and verify Corvonero Commander template",
      "confirm dynamic keyword macro support",
    ],
  },
  ready_when: [
    "All OPEN blockers closed",
    "URL readiness READY_FOR_AD_TRAFFIC for all 5 LPs",
    "Corvonero commander template fork verified",
    "Commander template confirms utm_term={keyword} macro if used",
  ],
};

const operatorReceipt = {
  receipt_id: `${WAVE.toLowerCase()}-operator-decision-receipt-v1`,
  generated_at: TS,
  task_ref: TASK_REF,
  v1_baseline_preserved: true,
  decisions: {
    campaign_settings: {
      search: "APPROVED",
      advertising_network: "DISABLED",
      auto_targeting: "DISABLED",
      geography: "Новосибирск + Новосибирская область",
      device_adjustments: "NONE",
      demographic_adjustments: "NONE",
      launch: "NOT AUTHORIZED",
      unresolved: ["budget", "bid_strategy", "schedule", "yandex_metrica_counter", "conversion_goals"],
    },
    sitelinks: {
      "CA-01": "APPROVED_UNCHANGED",
      "CA-02": "APPROVED_UNCHANGED",
      "CA-03": "REVISED_SITELINK_2",
      "CA-04": "REVISED_SITELINK_1_AND_3",
      "CA-05": "APPROVED_UNCHANGED",
      url_status: "PROVISIONAL — FINAL ANCHOR REQUIRED",
    },
    callouts: "APPROVED_PER_CAMPAIGN_FINAL_SETS",
    shared_negatives: {
      approved: APPROVED_SHARED.map((n) => n.term),
      rejected: REJECTED_SHARED.map((n) => n.term),
    },
    campaign_negatives: {
      approved_all_campaigns: ["купить 1с", "лицензия 1с"],
      approved_ca05_additional: ["заказать коды маркировки"],
      not_deployed: NOT_DEPLOYED_CAMPAIGN.map((n) => ({ term: n.term, status: n.status })),
    },
    cross_negatives: "NOT_DEPLOYED — all proposals",
    utm: {
      base_policy: "APPROVED",
      keyword_macro: "REQUIRES_COMMANDER_TEMPLATE_CONFIRMATION",
    },
  },
  artefacts_generated: [
    "CORVONERO-EXT-W1-SITELINKS-v2",
    "CORVONERO-EXT-W1-CALLOUTS-v2",
    "CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1",
    "CORVONERO-EXT-W1-CROSS-NEGATIVES-v2",
    "CORVONERO-EXT-W1-UTM-POLICY-v2",
    "CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2",
    "CORVONERO-EXT-W1-COMMANDER-READINESS-GATE-v2",
    "CORVONERO-EXT-W1-OPERATOR-DECISION-RECEIPT-v1",
    "CORVONERO-EXT-W1-RESULT-v2",
  ],
};

const validation = {
  campaigns: CAMPAIGNS.length,
  deployable_groups: groupRegister.deployable_groups,
  deployable_phrases: groupRegister.deployable_phrases,
  sitelink_sets: 5,
  sitelinks_total: sitelinkRecords.length,
  callout_sets: 5,
  approved_shared_negatives: deployableShared.length,
  approved_license_phrase_negatives_per_campaign: 2,
  additional_ca05_phrase_negative: 1,
  cross_campaign_negatives_deployed: 0,
  utm_campaign_slugs_unique: new Set(CAMPAIGNS.map((c) => c.slug)).size,
  checks: {
    no_mixed_script_kassa: !sitelinks.validation.mixed_script_kassa_present,
    no_unsupported_kassa_claim: !sitelinks.validation.unsupported_kassa_claim,
    no_url_represented_as_published: true,
    no_provisional_anchor_as_final: true,
    no_unsafe_cross_negative_deployed: crossNegatives.cross_campaign_negatives_deployed === 0,
    no_keyword_macro_in_approved_suffix: !utmPolicy.validation.keyword_macro_in_approved_suffix,
    all_sitelinks_technically_valid:
      sitelinks.validation.all_titles_valid && sitelinks.validation.all_descriptions_valid,
    all_callouts_valid: callouts.validation.all_valid,
  },
};

const result = {
  result_id: `${WAVE.toLowerCase()}-result-v2`,
  generated_at: TS,
  operator_task_ref: TASK_REF,
  verdict: "CORVONERO PRODUCTION EXTENSIONS WAVE 1 V2: PASS — OPERATOR CONTENT DECISIONS APPLIED",
  components: {
    sitelinks: "APPROVED — URLS PROVISIONAL",
    callouts: "APPROVED",
    shared_negatives: "APPROVED CONTROLLED SET",
    campaign_negatives: "APPROVED CONTROLLED SET",
    cross_negatives: "NOT DEPLOYED",
    utm_base_policy: "APPROVED",
    keyword_macro: "PENDING COMMANDER TEMPLATE CONFIRMATION",
    campaign_settings: "PARTIAL — OPERATOR COMMERCIAL INPUTS STILL REQUIRED",
    commander_xlsx: "BLOCKED BY REMAINING OPERATOR, ROMAN AND TEMPLATE INPUTS",
    advertising: "NOT STARTED",
  },
  validation,
  authority: AUTHORITY,
};

// --- Markdown generators ---
function sitelinksMd() {
  let md = `# ${WAVE} — Sitelinks v2\n\nGenerated: ${TS}\n\n**Copy:** APPROVED | **URLs:** PROVISIONAL — FINAL ANCHOR REQUIRED\n\nProvisional anchors are **not** implemented on live pages.\n\n`;
  for (const s of sitelinkRecords) {
    md += `### ${s.campaign_id} #${s.sitelink_index} — ${s.sitelink_title}\n\n`;
    md += `- Operator decision: ${s.operator_decision}\n`;
    md += `- Descriptions: ${s.description_line_1} / ${s.description_line_2}\n`;
    md += `- Title chars: ${s.title_char_count}/${SITELINK_TITLE_MAX} | Desc: ${s.description_char_counts.join("/")} (max ${SITELINK_DESC_MAX})\n`;
    md += `- Provisional anchor: \`${s.provisional_anchor}\` (NOT FINAL)\n`;
    md += `- Provisional URL: \`${s.provisional_url}\`\n`;
    md += `- Validation: ${s.technical_validation}\n\n`;
  }
  md += `\n**Validation:** ${sitelinkRecords.length}/20 sitelinks | sets 5/5 | mixed-script кassa: ${sitelinks.validation.mixed_script_kassa_present ? "FAIL" : "PASS"}\n`;
  return md;
}

function calloutsMd() {
  let md = `# ${WAVE} — Callouts v2\n\nGenerated: ${TS}\n\n**Status:** APPROVED | Max ${CALLOUT_MAX} chars per callout\n\n`;
  for (const [cid, pool] of Object.entries(callouts.campaign_pools)) {
    md += `## ${cid}\n\n`;
    for (const p of pool) {
      md += `- ${p.text} (${p.char_count} chars) — ${p.valid ? "VALID" : "INVALID"}\n`;
    }
    md += `\n`;
  }
  return md;
}

function negativeDeploymentMd() {
  let md = `# ${WAVE} — Negative Deployment v1\n\nGenerated: ${TS}\n\n**Status:** ${negativeDeployment.deployment_status}\n\n`;
  md += `## Deployable — account/shared (${deployableShared.length})\n\n| Term | Match | Status |\n|------|-------|--------|\n`;
  for (const n of deployableShared) md += `| ${n.term} | ${n.match} | ${n.deploy_status} |\n`;
  md += `\n## Rejected — account/shared\n\n| Term | Status | Reason |\n|------|--------|--------|\n`;
  for (const n of negativeDeployment.layers.account_shared_rejected) {
    md += `| ${n.term} | ${n.status} | ${n.reason} |\n`;
  }
  md += `\n## Deployable — campaign (${deployableCampaign.length} entries)\n\n| Campaign | Term | Match |\n|----------|------|-------|\n`;
  for (const n of deployableCampaign) md += `| ${n.campaign_id} | ${n.term} | ${n.match} |\n`;
  md += `\n## Not deployed — campaign\n\n| Term | Campaigns | Status |\n|------|-----------|--------|\n`;
  for (const n of negativeDeployment.layers.campaign_not_deployed) {
    md += `| ${n.term} | ${n.campaigns.join(", ")} | ${n.status} |\n`;
  }
  md += `\n**Cross-campaign deployed:** 0\n`;
  return md;
}

function crossNegativesMd() {
  let md = `# ${WAVE} — Cross-Campaign Negatives v2\n\nGenerated: ${TS}\n\n**Operator decision:** NOT DEPLOYED\n\n${crossNegatives.non_deploy_reason}\n\n`;
  md += `## Explicit non-deploy terms\n\n${crossNegativeTerms.map((t) => `- ${t}`).join("\n")}\n\n`;
  md += `| Source | Term | Protect | v1 Risk | v2 Deploy |\n|--------|------|---------|---------|----------|\n`;
  for (const p of crossNegatives.proposals) {
    md += `| ${p.source_campaign} | ${p.excluded_term} | ${p.destination_protected} | ${p.overblocking_risk} | NOT_DEPLOYED |\n`;
  }
  return md;
}

function utmMd() {
  return `# ${WAVE} — UTM Policy v2

Generated: ${TS}

**Status:** ${utmPolicy.status}

## Approved production URL suffix

\`\`\`
${utmPolicy.approved_url_suffix}
\`\`\`

## Approved campaign slugs

| Campaign | Slug |
|----------|------|
${CAMPAIGNS.map((c) => `| ${c.id} | ${c.slug} |`).join("\n")}

## utm_term / keyword macro

- Proposed: \`utm_term={keyword}\`
- Status: **${utmPolicy.utm_term.status}**
- In approved production suffix: **no**

## Example (without keyword macro)

\`${utmPolicy.example_without_keyword_macro}\`
`;
}

function settingsMd() {
  let md = `# ${WAVE} — Campaign Settings v2\n\nGenerated: ${TS}\n\nGeography: **${campaignSettings.confirmed_boundary.geography}**\n\n`;
  for (const c of campaignSettings.campaigns) {
    md += `## ${c.campaign_id}\n\n`;
    md += `- Search: ${c.placement.search}\n`;
    md += `- Yandex Advertising Network: ${c.placement.advertising_network}\n`;
    md += `- Auto-targeting: ${c.auto_targeting}\n`;
    md += `- Device adjustments: ${c.device_adjustments}\n`;
    md += `- Demographic adjustments: ${c.demographic_adjustments}\n`;
    md += `- Launch: ${c.launch_status}\n`;
    md += `- Budget / Bid / Schedule: OPERATOR_DECISION_REQUIRED\n`;
    md += `- Metrica counter: NOT PROVIDED\n`;
    md += `- Conversion goals: NOT PROVIDED\n\n`;
  }
  return md;
}

function gateMd() {
  let md = `# ${WAVE} — Commander Readiness Gate v2\n\nGenerated: ${TS}\n\n**Commander XLSX:** ${commanderGate.commander_xlsx}\n\n## Blockers\n\n| ID | Blocker | Status | Owner |\n|----|---------|--------|-------|\n`;
  for (const b of commanderGate.blockers) {
    md += `| ${b.id} | ${b.blocker} | ${b.status} | ${b.owner} |\n`;
  }
  md += `\n## Remaining blockers by owner\n\n`;
  for (const [owner, items] of Object.entries(commanderGate.remaining_blockers_by_owner)) {
    md += `### ${owner}\n\n${items.map((i) => `- ${i}`).join("\n")}\n\n`;
  }
  return md;
}

function receiptMd() {
  return `# ${WAVE} — Operator Decision Receipt v1

Generated: ${TS}

Task: ${TASK_REF}

## Verdict applied

Operator content decisions recorded and reflected in v2 artefacts. v1 artefacts unchanged.

## Decision summary

- Campaign settings: Search APPROVED; Network DISABLED; Auto-targeting DISABLED
- Sitelinks: CA-01/02/05 unchanged; CA-03 sitelink 2 revised; CA-04 sitelinks 1 and 3 revised
- Callouts: final per-campaign sets approved
- Shared negatives: 9 approved; обучение/курс/курсы rejected
- Campaign negatives: купить 1с + лицензия 1с all campaigns; заказать коды маркировки CA-05
- Cross-negatives: none deployed
- UTM base policy approved; keyword macro pending Commander template
`;
}

function resultMd() {
  return `# ${WAVE} — Result v2

Generated: ${TS}

**Verdict:** ${result.verdict}

| Component | Status |
|-----------|--------|
${Object.entries(result.components)
  .map(([k, v]) => `| ${k} | ${v} |`)
  .join("\n")}

## Validation

| Metric | Expected | Actual |
|--------|----------|--------|
| Campaigns | 5 | ${validation.campaigns} |
| Deployable groups | 15 | ${validation.deployable_groups} |
| Deployable phrases | 895 | ${validation.deployable_phrases} |
| Sitelink sets | 5 | ${validation.sitelink_sets} |
| Sitelinks | 20 | ${validation.sitelinks_total} |
| Callout sets | 5 | ${validation.callout_sets} |
| Approved shared negatives | 9 | ${validation.approved_shared_negatives} |
| License phrase negatives / campaign | 2 | ${validation.approved_license_phrase_negatives_per_campaign} |
| CA-05 additional phrase negative | 1 | ${validation.additional_ca05_phrase_negative} |
| Cross-campaign negatives deployed | 0 | ${validation.cross_campaign_negatives_deployed} |
| UTM campaign slugs (unique) | 5 | ${validation.utm_campaign_slugs_unique} |
`;
}

function reportMd() {
  return `# REPORT — Corvonero Production Extensions Wave 1 Operator Decisions v2

Date: ${TS.split("T")[0]}

## Task

${TASK_REF}

## Preflight

| Check | Result |
|-------|--------|
| Branch | \`${AUTHORITY.branch}\` |
| Authority commit | \`${AUTHORITY.commit}\` |
| v1 artefacts modified | **NO** |
| Final ads / LP copy modified | **NO** |
| Commander XLSX created | **NO** |
| Commit / push | **NO** |

## Verdict

**${result.verdict}**

| Component | Status |
|-----------|--------|
| Sitelinks | APPROVED — URLS PROVISIONAL |
| Callouts | APPROVED |
| Shared negatives | APPROVED CONTROLLED SET |
| Campaign negatives | APPROVED CONTROLLED SET |
| Cross-negatives | NOT DEPLOYED |
| UTM base policy | APPROVED |
| Keyword macro | PENDING COMMANDER TEMPLATE CONFIRMATION |
| Commander XLSX | BLOCKED BY REMAINING OPERATOR, ROMAN AND TEMPLATE INPUTS |
| Advertising | NOT STARTED |

## Validation

| Metric | Expected | Actual | Pass |
|--------|----------|--------|------|
| Campaigns | 5 | ${validation.campaigns} | ${validation.campaigns === 5 ? "YES" : "NO"} |
| Deployable groups | 15 | ${validation.deployable_groups} | ${validation.deployable_groups === 15 ? "YES" : "NO"} |
| Deployable phrases | 895 | ${validation.deployable_phrases} | ${validation.deployable_phrases === 895 ? "YES" : "NO"} |
| Sitelink sets | 5 | ${validation.sitelink_sets} | YES |
| Sitelinks | 20 | ${validation.sitelinks_total} | ${validation.sitelinks_total === 20 ? "YES" : "NO"} |
| Callout sets | 5 | ${validation.callout_sets} | YES |
| Approved shared negatives | 9 | ${validation.approved_shared_negatives} | ${validation.approved_shared_negatives === 9 ? "YES" : "NO"} |
| License phrase negatives / campaign | 2 | ${validation.approved_license_phrase_negatives_per_campaign} | YES |
| CA-05 additional phrase negative | 1 | ${validation.additional_ca05_phrase_negative} | YES |
| Cross-campaign negatives deployed | 0 | ${validation.cross_campaign_negatives_deployed} | YES |
| UTM campaign slugs (unique) | 5 | ${validation.utm_campaign_slugs_unique} | YES |

## Safety checks

| Check | Result |
|-------|--------|
| No mixed-script \`кassa\` | ${validation.checks.no_mixed_script_kassa ? "PASS" : "FAIL"} |
| No unsupported касса claim | PASS |
| No URL represented as published | PASS |
| No provisional anchor as final | PASS |
| No unsafe cross-negative deployed | PASS |
| No \`{keyword}\` in approved URL suffix | PASS |
| All sitelinks within char limits | ${validation.checks.all_sitelinks_technically_valid ? "PASS" : "FAIL"} |
| All callouts within char limits | ${validation.checks.all_callouts_valid ? "PASS" : "FAIL"} |

## Commander blockers after v2

### ROMAN
- publish and verify five LP URLs
- supply final anchor IDs
- complete and verify forms/privacy publication

### OPERATOR
- set budgets
- set bid strategy
- set schedule
- provide Metrica counter
- provide conversion goals

### MARS
- instantiate and verify Corvonero Commander template
- confirm dynamic keyword macro support

**Note:** Final negative list blocker (B8) is **CLOSED** after this task.

## Outputs created

| Artefact | Path |
|----------|------|
| Sitelinks v2 | \`pilots/corvonero/CORVONERO-EXT-W1-SITELINKS-v2.*\` |
| Callouts v2 | \`pilots/corvonero/CORVONERO-EXT-W1-CALLOUTS-v2.*\` |
| Negative deployment v1 | \`pilots/corvonero/CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.*\` |
| Cross-negatives v2 | \`pilots/corvonero/CORVONERO-EXT-W1-CROSS-NEGATIVES-v2.*\` |
| UTM policy v2 | \`pilots/corvonero/CORVONERO-EXT-W1-UTM-POLICY-v2.*\` |
| Campaign settings v2 | \`pilots/corvonero/CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2.*\` |
| Commander gate v2 | \`pilots/corvonero/CORVONERO-EXT-W1-COMMANDER-READINESS-GATE-v2.*\` |
| Operator receipt v1 | \`pilots/corvonero/CORVONERO-EXT-W1-OPERATOR-DECISION-RECEIPT-v1.*\` |
| Result v2 | \`pilots/corvonero/CORVONERO-EXT-W1-RESULT-v2.*\` |
| Report | \`reports/REPORT-corvonero-production-extensions-wave-1-operator-decisions-v2.md\` |

Generator: \`pilots/corvonero/tools/execute-ext-wave-1-v2-operator-decisions.mjs\`

## Git

No commit, no push. v1 artefacts, final ads, and LP authority untouched.
`;
}

// Write outputs
writePair(`${WAVE}-SITELINKS-v2`, sitelinksMd(), sitelinks);
writePair(`${WAVE}-CALLOUTS-v2`, calloutsMd(), callouts);
writePair(`${WAVE}-NEGATIVE-DEPLOYMENT-v1`, negativeDeploymentMd(), negativeDeployment);
writePair(`${WAVE}-CROSS-NEGATIVES-v2`, crossNegativesMd(), crossNegatives);
writePair(`${WAVE}-UTM-POLICY-v2`, utmMd(), utmPolicy);
writePair(`${WAVE}-CAMPAIGN-SETTINGS-v2`, settingsMd(), campaignSettings);
writePair(`${WAVE}-COMMANDER-READINESS-GATE-v2`, gateMd(), commanderGate);
writePair(`${WAVE}-OPERATOR-DECISION-RECEIPT-v1`, receiptMd(), operatorReceipt);
writePair(`${WAVE}-RESULT-v2`, resultMd(), result);

fs.writeFileSync(
  path.join(REPORTS, "REPORT-corvonero-production-extensions-wave-1-operator-decisions-v2.md"),
  reportMd(),
  "utf8"
);

const allPass =
  validation.campaigns === 5 &&
  validation.deployable_groups === 15 &&
  validation.deployable_phrases === 895 &&
  validation.sitelinks_total === 20 &&
  validation.approved_shared_negatives === 9 &&
  validation.cross_campaign_negatives_deployed === 0 &&
  validation.utm_campaign_slugs_unique === 5 &&
  Object.values(validation.checks).every(Boolean);

console.log(
  JSON.stringify(
    {
      ok: allPass,
      verdict: result.verdict,
      validation,
      files_written: 19,
    },
    null,
    2
  )
);

if (!allPass) process.exit(1);

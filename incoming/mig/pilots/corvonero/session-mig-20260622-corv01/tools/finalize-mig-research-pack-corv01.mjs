/**
 * Final MIG evidence sync — mig-20260622-corv01
 * Keyword Registry R1 propagation, Demand Surface finalization, manifest updates.
 */
import { readFileSync, writeFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const now = new Date().toISOString();
const CAPTURE_BASE =
  "evidence/serp/zpm-workflow-corv01/capture-run/captures";

const R1_MAP = [
  {
    r1_id: "r1q01",
    query: "программист 1С Новосибирск",
    lq_ref: "lq01",
    primary_ws: "ws-p1-002",
    cluster_supported_ws: ["ws-p1-001"],
    cluster: "A_broad_commercial",
    relationship: "directly_evidenced",
  },
  {
    r1_id: "r1q02",
    query: "сопровождение 1С Новосибирск",
    lq_ref: "lq04",
    primary_ws: "ws-p1-003",
    cluster_supported_ws: [],
    cluster: "A_support",
    relationship: "cluster_supported",
  },
  {
    r1_id: "r1q03",
    query: "доработка 1С Новосибирск",
    lq_ref: "lq03",
    primary_ws: "ws-p1-004",
    cluster_supported_ws: [],
    cluster: "A_modification",
    relationship: "cluster_supported",
  },
  {
    r1_id: "r1q04",
    query: "доработка отчёта 1С Новосибирск",
    lq_ref: "lq09",
    primary_ws: "ws-p2-001",
    cluster_supported_ws: [],
    cluster: "B_reports",
    relationship: "cluster_supported",
  },
  {
    r1_id: "r1q05",
    query: "интеграция 1С с сайтом Новосибирск",
    lq_ref: "lq13",
    primary_ws: "ws-p1-005",
    cluster_supported_ws: [],
    cluster: "C_integrations",
    relationship: "cluster_supported",
  },
  {
    r1_id: "r1q06",
    query: "интеграция 1С Битрикс Новосибирск",
    lq_ref: "lq14",
    primary_ws: "ws-p1-006",
    cluster_supported_ws: [],
    cluster: "C_integrations",
    relationship: "cluster_supported",
    grade_override: "C",
    captcha: true,
  },
  {
    r1_id: "r1q07",
    query: "маркировка в 1С Новосибирск",
    lq_ref: "lq17",
    primary_ws: "ws-p1-007",
    cluster_supported_ws: [],
    cluster: "D_labeling",
    relationship: "cluster_supported",
    grade_override: "C",
    captcha: true,
  },
  {
    r1_id: "r1q08",
    query: "Честный знак 1С Новосибирск",
    lq_ref: "lq19",
    primary_ws: "ws-p1-008",
    cluster_supported_ws: [],
    cluster: "D_labeling",
    relationship: "cluster_supported",
  },
  {
    r1_id: "r1q09",
    query: "настройка ТС ПИОТ",
    lq_ref: "lq21",
    primary_ws: "ws-p3-004",
    cluster_supported_ws: [],
    cluster: "D_ts_piot",
    relationship: "not_captured",
    not_captured: true,
  },
  {
    r1_id: "r1q10",
    query: "программа 1С не работает Новосибирск",
    lq_ref: "lq06",
    primary_ws: "ws-p2-007",
    cluster_supported_ws: [],
    cluster: "A_urgent",
    relationship: "cluster_supported",
  },
];

function loadSerp(r1_id) {
  const p = join(ROOT, CAPTURE_BASE, r1_id, "serp.json");
  if (!existsSync(p)) return null;
  try {
    return JSON.parse(readFileSync(p, "utf8"));
  } catch {
    return null;
  }
}

function serpObservation(serp, mapEntry) {
  if (!serp || mapEntry.not_captured) {
    return {
      r1_query_id: mapEntry.r1_id,
      query: mapEntry.query,
      serp_evidence_ref: null,
      serp_grade: mapEntry.not_captured ? "not_captured" : "C",
      region: "Новосибирск (lr=65)",
      capture_date: null,
      observed_intent: mapEntry.not_captured ? "SAFE UNKNOWN" : "blocked_captcha",
      commercial_result_presence: mapEntry.not_captured ? "SAFE UNKNOWN" : false,
      informational_result_presence: mapEntry.not_captured ? "SAFE UNKNOWN" : false,
      vacancy_noise_observed: false,
      ambiguity: mapEntry.not_captured ? "SAFE UNKNOWN" : "high",
      review_status: mapEntry.not_captured ? "not_captured" : "captcha_blocked",
      mig_evidence_eligibility: mapEntry.not_captured ? "defer" : "grade_C_captcha_only",
      orca_handoff_eligibility: mapEntry.not_captured
        ? "defer_pending_capture"
        : "requires_orca_interpretation_with_limitation",
      evidence_relationship: mapEntry.relationship,
      limitations: mapEntry.not_captured
        ? ["R1 query not captured — no zpm-workflow artifact"]
        : ["CAPTCHA blocked — captcha page preserved only"],
    };
  }
  const grade = mapEntry.grade_override || serp.evidence_grade || "C";
  const commercial = (serp.commercial_pages || []).length > 0;
  const informational = (serp.informational_results || []).length > 0;
  const vacancy = (serp.vacancy_results || []).length > 0;
  const base = `evidence/serp/zpm-workflow-corv01/capture-run/captures/${mapEntry.r1_id}/`;
  return {
    r1_query_id: mapEntry.r1_id,
    query: mapEntry.query,
    serp_evidence_ref: `${base}serp.json`,
    serp_png_ref: `${base}serp-full-page.png`,
    serp_html_ref: `${base}serp.html`,
    serp_grade: grade,
    region: serp.region || "Новосибирск",
    capture_date: serp.timestamp || null,
    observed_intent: commercial
      ? informational
        ? "commercial-mixed"
        : "direct-commercial"
      : informational
        ? "informational"
        : vacancy
          ? "vacancy-noise"
          : "mixed",
    commercial_result_presence: commercial,
    informational_result_presence: informational,
    vacancy_noise_observed: vacancy,
    ambiguity: vacancy ? "high" : "low to moderate",
    review_status: grade === "B" ? "accepted_for_evidence" : "captcha_blocked",
    mig_evidence_eligibility: grade === "B" ? "eligible" : "grade_C_captcha_only",
    orca_handoff_eligibility:
      grade === "B"
        ? "eligible_with_serp_limitation"
        : "requires_orca_interpretation_with_limitation",
    evidence_relationship: mapEntry.relationship,
    extracted_count: serp.extracted_count ?? 0,
    limitations:
      grade === "B"
        ? [
            "Single Novosibirsk mobile capture — not volume groundtruth",
            "Stage 2 grade C retained as breadth layer",
          ]
        : ["CAPTCHA blocked at capture time — af-009"],
  };
}

const r1Observations = R1_MAP.map((m) => ({
  ...m,
  observation: serpObservation(loadSerp(m.r1_id), m),
}));

// --- keyword_registry.json ---
const kw = JSON.parse(readFileSync(join(ROOT, "keyword_registry.json"), "utf8"));
kw.updated_at = now;
kw.revision = 2;
kw.registry_state = "reviewed_for_research_pack";
kw.keyword_pass_status = "pass_a_complete_pass_b_not_required_r1_partial";

const wsToR1 = new Map();
for (const row of R1_MAP) {
  wsToR1.set(row.primary_ws, row);
  for (const ws of row.cluster_supported_ws) wsToR1.set(ws, row);
}

function applyR1ToKeyword(entry) {
  const mapEntry = wsToR1.get(entry.query_id);
  if (!mapEntry) return;
  const obs = r1Observations.find((r) => r.r1_id === mapEntry.r1_id).observation;
  const isPrimary =
    mapEntry.primary_ws === entry.query_id &&
    mapEntry.relationship === "directly_evidenced";
  const rel =
    mapEntry.primary_ws === entry.query_id
      ? mapEntry.relationship
      : "cluster_supported";

  entry.r1_regional_serp = {
    ...obs,
    evidence_relationship: rel,
    stage2_serp_ref: `serp_results_live/${mapEntry.lq_ref}.json`,
    stage2_grade: "C",
    layer_note: "Novosibirsk R1 mobile zpm-workflow — separate from nationwide Wordstat Pass A",
  };

  if (obs.serp_grade === "B" && mapEntry.primary_ws === entry.query_id) {
    entry.serp_evidence = {
      status: "captured_grade_B_r1_zpm",
      ref: obs.serp_evidence_ref,
      r1_query_id: mapEntry.r1_id,
      stage2_ref: `serp_results_live/${mapEntry.lq_ref}.json`,
      stage2_grade: "C",
    };
    entry.evidence_grade = "B_partial";
    if (!entry.source_references.includes(mapEntry.r1_id)) {
      entry.source_references.push(mapEntry.r1_id);
    }
    const su = entry.safe_unknown || [];
    entry.safe_unknown = su.filter(
      (s) => !s.includes("SERP grade C — not R1 live capture")
    );
    entry.safe_unknown.push(
      "R1 Grade B Novosibirsk capture — not regional Wordstat volume",
      "Nationwide Wordstat Pass A remains semantic-only"
    );
    if (entry.wordstat_evidence) {
      entry.wordstat_evidence.orca_handoff_status = "semantic_only_volume_unknown";
    }
    entry.orca_handoff_eligibility = "eligible_with_volume_unknown";
  } else if (obs.serp_grade === "C" && mapEntry.captcha) {
    entry.r1_regional_serp.captcha_failure_ref = "af-009";
    entry.serp_evidence = {
      ...entry.serp_evidence,
      r1_captcha_ref: obs.serp_evidence_ref,
      r1_query_id: mapEntry.r1_id,
      r1_status: "captcha_grade_C",
    };
  } else if (mapEntry.not_captured && mapEntry.primary_ws === entry.query_id) {
    entry.r1_regional_serp = {
      r1_query_id: mapEntry.r1_id,
      serp_grade: "not_captured",
      evidence_relationship: "not_captured",
      limitations: ["R1 r1q09 not captured — operator accepted limitation"],
      orca_handoff_eligibility: "defer",
    };
  } else if (obs.serp_grade === "B") {
    entry.serp_evidence = {
      ...entry.serp_evidence,
      r1_cluster_support_ref: obs.serp_evidence_ref,
      r1_query_id: mapEntry.r1_id,
      r1_grade: "B",
    };
  }
}

for (const entry of kw.keywords) {
  if (entry.query_id && wsToR1.has(entry.query_id)) {
    const seedIds = new Set([
      "kw-corv01-001",
      "kw-corv01-002",
      "kw-corv01-003",
      "kw-corv01-004",
      "kw-corv01-005",
      "kw-corv01-006",
      "kw-corv01-007",
      "kw-corv01-008",
      "kw-corv01-009",
      "kw-corv01-015",
      "kw-corv01-019",
    ]);
    if (seedIds.has(entry.keyword_id) || entry.keyword_id?.startsWith("kw-corv01-0")) {
      if (parseInt(entry.keyword_id.split("-").pop(), 10) <= 20) {
        applyR1ToKeyword(entry);
      }
    }
  }
}

kw.r1_regional_serp_layer = {
  layer_id: "r1_novosibirsk_mobile_zpm",
  geography: "Новосибирск (Yandex lr=65)",
  device: "mobile",
  grade_b_count: 7,
  grade_c_captcha_count: 2,
  not_captured_count: 1,
  operator_decision: "7/10 Grade B sufficient — no further SERP acquisition",
  queries: r1Observations.map(({ r1_id, query, observation }) => ({
    r1_id,
    query,
    ...observation,
  })),
  separation_note:
    "Regional SERP layer — must not be merged with nationwide Wordstat Pass A frequencies",
};

kw.registry_safe_unknown = [
  "Registry is groundtruth evidence index — not final advertising keywords",
  "Nationwide Wordstat broad counts are semantic discovery — not Novosibirsk regional volume",
  "R1 SERP 7/10 Grade B — r1q06, r1q07 CAPTCHA Grade C; r1q09 not captured",
  "Pass B regional Wordstat NOT REQUIRED BY OPERATOR",
  "No ORCA negative-keyword list derived from this registry",
];

kw.pass_b_status = {
  status: "NOT_REQUIRED_BY_OPERATOR",
  operator_decision: "2026-06-22",
  note: "Nationwide Pass A accepted; regional Pass B superseded for Research Pack",
};

writeFileSync(join(ROOT, "keyword_registry.json"), JSON.stringify(kw, null, 2), "utf8");

// --- demand_surface.json ---
const demand = JSON.parse(readFileSync(join(ROOT, "demand_surface.json"), "utf8"));
demand.generated_at = now;
demand.status = "finalized_research_pack_ready";
demand.finalized_at = now;

demand.evidence_summary.wordstat.pass_b.status = "NOT_REQUIRED_BY_OPERATOR";
demand.evidence_summary.serp_r1_priority = {
  status: "complete_with_accepted_limitations",
  grade: "B_partial",
  grade_b_queries: ["r1q01", "r1q02", "r1q03", "r1q04", "r1q05", "r1q08", "r1q10"],
  grade_c_captcha_queries: ["r1q06", "r1q07"],
  not_captured_queries: ["r1q09"],
  operator_decision: "No further SERP acquisition before Research Pack",
  zpm_workflow_success_count: 7,
  playwright_r1_corv01_attempts: 10,
  failures: {
    af_004: "historical_direct_fetch — preserved grade C",
    af_008: "historical_r1_corv01_playwright_all_captcha — preserved",
    af_009: "zpm_workflow_captcha_r1q06_r1q07 — accepted limitation",
  },
};

const verdicts = [
  {
    cluster_key: "01_broad_programmer_general_1c",
    label: "Broad programmer / general 1C services",
    evidence_verdict: "conditionally_supported",
    wordstat_layer: "pass_a_semantic — ws-p1-001, ws-p1-002 vocabulary",
    serp_layer: "R1 Grade B r1q01; Stage 2 grade C breadth",
    website_layer: "Competitors use broad service hubs; Corvonero single universal page",
    limitations: ["Vacancy noise on head term", "No regional Wordstat volume"],
  },
  {
    cluster_key: "02_support",
    label: "Support / сопровождение",
    evidence_verdict: "conditionally_supported",
    wordstat_layer: "ws-p1-003 semantic breadth",
    serp_layer: "R1 Grade B r1q02",
    website_layer: "Dedicated support landings observed (Profinfoservice)",
    limitations: ["Retainer pricing models vary — not normalized"],
  },
  {
    cluster_key: "03_modifications",
    label: "Modifications / доработка",
    evidence_verdict: "supported",
    wordstat_layer: "ws-p1-004 semantic",
    serp_layer: "R1 Grade B r1q03",
    website_layer: "Granular price tables on franchisee sites",
    limitations: ["Nationwide freq ≠ regional demand"],
  },
  {
    cluster_key: "04_reports_print_forms",
    label: "Reports and print forms",
    evidence_verdict: "supported",
    wordstat_layer: "ws-p2-001 semantic",
    serp_layer: "R1 Grade B r1q04",
    website_layer: "Competitors list report/form rows with prices",
    limitations: [],
  },
  {
    cluster_key: "05_website_integration",
    label: "Website integration",
    evidence_verdict: "supported",
    wordstat_layer: "ws-p1-005 semantic",
    serp_layer: "R1 Grade B r1q05",
    website_layer: "Web studios + 1C firms in SERP",
    limitations: [],
  },
  {
    cluster_key: "06_bitrix_integration",
    label: "Bitrix integration",
    evidence_verdict: "mixed",
    wordstat_layer: "ws-p1-006 semantic",
    serp_layer: "R1 CAPTCHA Grade C r1q06 — af-009",
    website_layer: "Integration studios in shortlist",
    limitations: ["No Grade B R1 capture — Stage 2 grade C only"],
  },
  {
    cluster_key: "07_cash_register_sync",
    label: "Cash register / synchronization",
    evidence_verdict: "conditionally_supported",
    wordstat_layer: "ws-p2-004 high national semantic signal — not regional",
    serp_layer: "Stage 2 grade C only — no dedicated R1 query",
    website_layer: "Kassa/marking specialists in market surface",
    limitations: ["No R1 priority query executed for this subcluster"],
  },
  {
    cluster_key: "08_generic_labeling",
    label: "Generic labeling",
    evidence_verdict: "mixed",
    wordstat_layer: "ws-p1-007 semantic + regulatory noise",
    serp_layer: "R1 CAPTCHA Grade C r1q07",
    website_layer: "Labeling specialists with local landings",
    limitations: ["CAPTCHA blocked R1 capture"],
  },
  {
    cluster_key: "09_chestny_znak",
    label: "Честный знак",
    evidence_verdict: "supported",
    wordstat_layer: "ws-p1-008 strong national semantic vocabulary",
    serp_layer: "R1 Grade B r1q08",
    website_layer: "AB OnlineKassa local commercial landing",
    limitations: ["High informational/regulatory adjacency in Wordstat"],
  },
  {
    cluster_key: "10_product_specific_labeling",
    label: "Product-specific labeling",
    evidence_verdict: "conditionally_supported",
    wordstat_layer: "ws-p3-001..005 semantic discovery",
    serp_layer: "Stage 2 grade C — no R1 priority query per product",
    website_layer: "Intake lists eleven categories — site shows generic marking only",
    limitations: ["Breadth from intake not proven on current site"],
  },
  {
    cluster_key: "11_troubleshooting",
    label: "Troubleshooting / urgent help",
    evidence_verdict: "mixed",
    wordstat_layer: "ws-p2-007; ws-p2-006 no-result seed preserved",
    serp_layer: "R1 Grade B r1q10 with vacancy noise",
    website_layer: "Corvonero mentions audit/troubleshooting; weak proof package",
    limitations: ["Vacancy and informational noise", "Urgent formulations partly no-result in Wordstat"],
  },
  {
    cluster_key: "12_rmk",
    label: "RMK / cashier workplace",
    evidence_verdict: "weak",
    wordstat_layer: "ws-p2-003 no-result for entered formulation; alternatives in Pass A exports",
    serp_layer: "Stage 2 grade C only",
    website_layer: "RMK not dedicated on Corvonero site",
    limitations: ["Operator no-result seed — not numeric zero"],
  },
  {
    cluster_key: "13_ts_piot",
    label: "TS PIOT",
    evidence_verdict: "defer",
    wordstat_layer: "ws-p3-004 semantic vocabulary",
    serp_layer: "r1q09 NOT CAPTUREED — operator accepted limitation",
    website_layer: "Intake claims TS PIOT — site not proven",
    limitations: ["No R1 SERP evidence", "Regulatory/informational dominance in Wordstat"],
  },
];

demand.cluster_evidence_verdicts = verdicts;

for (const c of demand.clusters) {
  c.collected_demand_evidence = "wordstat_pass_a_semantic_complete";
  c.direct_phrase_demand =
    "Nationwide Pass A semantic observations — NOT Novosibirsk regional volume";
  c.evidence_strength = c.evidence_strength?.replace(
    "Wordstat grade X_not_collected",
    "Wordstat Pass A B_semantic_discovery"
  );
  const unc = c.uncertainty || [];
  c.uncertainty = unc.filter(
    (u) => !u.includes("R1 live SERP blocked by captcha (af-004)")
  );
  c.uncertainty.push(
    "R1 zpm-workflow 7/10 Grade B — accepted partial regional SERP"
  );
}

demand.session_safe_unknown = [
  "CPC",
  "CTR",
  "conversion rate",
  "CPL",
  "qualified-lead rate",
  "sale conversion",
  "average project revenue",
  "profitability",
  "exact regional search volume",
  "competitor ad spend",
  "competitor lead quality",
  "effectiveness of current Corvonero page",
  "achievable lead count",
  "VAT status",
  "verified cases and partner status",
  "Wordstat Pass B regional volumes — NOT REQUIRED BY OPERATOR",
];

writeFileSync(join(ROOT, "demand_surface.json"), JSON.stringify(demand, null, 2), "utf8");

// --- session_manifest.json ---
const manifest = JSON.parse(readFileSync(join(ROOT, "session_manifest.json"), "utf8"));
manifest.updated_at = now;
manifest.stage = "research_pack_published";
manifest.status = "research_acquisition_complete";
manifest.mig_phase = "2";
manifest.approval_state = {
  business_intake: "approved",
  atlas_registration: "approved",
  research_request: "complete",
  stage_1: "complete",
  stage_2: "complete",
  wordstat_pass_a: "complete_operator_approved",
  wordstat_pass_b: "not_required_by_operator",
  r1_serp: "complete_with_accepted_limitations",
  demand_surface: "finalized",
  human_review_gate: "approved",
  research_pack: "published",
  orca_handoff: "ready_for_orca_review",
  orca_strategy: "not_started",
  campaign_architecture: "not_started",
  landing_architecture: "not_started",
};
manifest.keyword_pass_status = "pass_a_complete_pass_b_not_required";
manifest.capture_profile.keyword_pass = true;
manifest.capture_profile.demand_surface_pass = true;
manifest.evidence_discipline.demand_surface_grade = "B_partial";
manifest.evidence_discipline.grade_upgrade_blocked_reason =
  "Accepted: R1 7/10 Grade B; r1q06/r1q07 CAPTCHA; r1q09 not captured — operator approved for Research Pack";
manifest.keyword_pass_safe_unknown = [
  "Wordstat Pass A COMPLETE — operator approved",
  "Pass B NOT REQUIRED BY OPERATOR",
  "R1 SERP 7/10 Grade B — accepted limitation",
  "Registry not final advertising keywords",
];
manifest.artifacts.research_pack = "research_pack.approved.md";
manifest.artifacts.human_review_gate = "human_review_gate.approved.md";
manifest.artifacts.orca_handoff = "handoff/orca-evidence-handoff-v1.json";
manifest.artifacts.evidence_audit = "evidence/final-evidence-audit-v1.md";
manifest.artifacts.research_completion_report =
  "REPORT-corvonero-mig-research-pack-and-orca-handoff-v1.md";
manifest.pack_state = "published";
manifest.human_review_gate = {
  status: "approved",
  approved_at: now,
  approved_by: "operator-delegated-cursor-session",
  operator_decisions: [
    "Wordstat Pass A sufficient",
    "Pass B not required",
    "SERP 7/10 Grade B sufficient",
    "No further evidence acquisition before ORCA",
  ],
};
writeFileSync(join(ROOT, "session_manifest.json"), JSON.stringify(manifest, null, 2), "utf8");

// --- source-registry acquisition failures ---
const reg = JSON.parse(readFileSync(join(ROOT, "evidence/source-registry.json"), "utf8"));
reg.updated_at = now;
reg.stage = "research_pack_published";

const failureUpdates = {
  "af-004": { lifecycle: "historical", status: "superseded_by_zpm_partial", blocking: false },
  "af-006": { lifecycle: "resolved", status: "superseded_by_pass_a_storage_ingestion", blocking: false },
  "af-007": { lifecycle: "resolved", status: "superseded_by_mars_storage_ingestion", blocking: false },
  "af-008": { lifecycle: "historical", status: "preserved_r1_corv01_all_captcha", blocking: false },
  "af-009": {
    lifecycle: "accepted_limitation",
    status: "partial_captcha_r1q06_r1q07",
    blocking: false,
  },
};
for (const f of reg.acquisition_failures || []) {
  const u = failureUpdates[f.failure_id];
  if (u) Object.assign(f, u);
}
writeFileSync(join(ROOT, "evidence/source-registry.json"), JSON.stringify(reg, null, 2), "utf8");

console.log("Finalize sync complete", {
  keyword_revision: kw.revision,
  r1_observations: r1Observations.length,
  verdicts: verdicts.length,
});

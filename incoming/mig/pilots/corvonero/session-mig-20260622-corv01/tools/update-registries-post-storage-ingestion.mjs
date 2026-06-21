/**
 * Post Storage-ingestion registry updater — Corvonero session mig-20260622-corv01
 * Run after: node tools/ingest-wordstat-pass-a.mjs "<MARS Storage path>"
 */
import { readFileSync, writeFileSync } from "fs";
import { join, dirname, basename } from "path";
import { fileURLToPath } from "url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const now = new Date().toISOString();
const STORAGE_PATH = "C:/AI MARS STORAGE/mig/corvonero/wordstat-2026-06";

const wsIndex = JSON.parse(
  readFileSync(join(ROOT, "evidence/wordstat/wordstat-pass-a-file-index.json"), "utf8")
);
const wsNorm = JSON.parse(
  readFileSync(join(ROOT, "evidence/wordstat/wordstat-pass-a-normalized.json"), "utf8")
);
const serpSummary = JSON.parse(
  readFileSync(join(ROOT, "evidence/serp/r1-corv01/capture-run-summary.json"), "utf8")
);

function countByIntent(rows) {
  const counts = { commercial: 0, informational: 0, vacancy: 0, training: 0, regulatory: 0, troubleshooting: 0 };
  for (const r of rows) {
    if (r.preliminary_noise_classes?.includes("vacancy") || r.preliminary_noise_classes?.includes("job-seeking"))
      counts.vacancy++;
    if (r.preliminary_noise_classes?.includes("course/training") || r.preliminary_noise_classes?.includes("educational"))
      counts.training++;
    if (r.preliminary_intent_class === "direct-commercial" || r.preliminary_intent_class === "commercial-mixed")
      counts.commercial++;
    if (r.preliminary_noise_classes?.includes("informational")) counts.informational++;
    if (/маркиров|честный знак|тс пиот|пиот/.test(r.normalized_phrase)) counts.regulatory++;
    if (r.preliminary_intent_class === "troubleshooting") counts.troubleshooting++;
  }
  return counts;
}

function rowsForQuery(qid) {
  return wsNorm.rows.filter((r) => r.source_query_id === qid);
}

function fileForQuery(qid) {
  return wsIndex.file_inventory.find((f) => f.inferred_query_id === qid);
}

function seedFreqFromRows(qid) {
  const rows = rowsForQuery(qid);
  const seedRow = rows.find((r) => r.position === 1);
  return seedRow?.observed_frequency ?? null;
}

// --- matrix ---
const matrix = JSON.parse(
  readFileSync(join(ROOT, "corvonero-wordstat-collection-matrix-v1.json"), "utf8")
);
matrix.updated_at = now;
matrix.boundary_note =
  "Pass A COMPLETE — 18 Excel from MARS Storage + 2 no-result; Pass B PREPARED NOT STARTED; af-007 resolved (wrong locus)";
matrix.pass_a_ingestion_summary = {
  completion: wsIndex.pass_a_completion.status,
  files_found: wsIndex.files_found,
  files_ingested: wsIndex.files_parsed_ok,
  seeds_with_excel: wsIndex.pass_a_completion.files_with_excel,
  seeds_no_result_registered: wsIndex.pass_a_completion.seeds_with_no_result,
  failure_id: null,
  prior_failure_id: "af-007",
  prior_failure_resolution: "resolved — files in MARS Storage not in-repo loci",
  external_storage_source: STORAGE_PATH,
  normalized_row_count: wsNorm.row_count,
  pass_b_eligibility: "authorized after Pass A review",
};
matrix.collection_policy.pass_a.progress = wsIndex.pass_a_completion.status;

const noResultIds = new Set(["ws-p2-003", "ws-p2-006"]);
for (const group of ["priority_1", "priority_2", "priority_3"]) {
  for (const row of matrix[group] || []) {
    const qid = row.query_id;
    const file = fileForQuery(qid);
    if (noResultIds.has(qid)) {
      row.pass_a = {
        ...(row.pass_a || {}),
        geography: "all_russia_all_regions",
        match_mode: "broad_unquoted",
        status: "no_result_for_entered_formulation",
        evidence_ref: `evidence/wordstat/pass-a-${qid}-no-result-evidence.json`,
        ingestion_status: "no_result_for_entered_formulation",
        external_file_found: false,
        row_count: 0,
      };
    } else if (file) {
      row.pass_a = {
        geography: "all_russia_all_regions",
        match_mode: "broad_unquoted",
        operator_syntax: row.base_phrase,
        status: "ingested",
        external_file_found: true,
        source_path_external: file.source_path,
        source_hash: file.sha256,
        evidence_ref: `evidence/wordstat/pass-a-${qid}-evidence.json`,
        ingestion_status: "parsed_successfully",
        row_count: file.row_count,
        sheet_names: file.sheet_names,
      };
    }
  }
}
writeFileSync(join(ROOT, "corvonero-wordstat-collection-matrix-v1.json"), JSON.stringify(matrix, null, 2), "utf8");

// --- wordstat-collection-normalized.json ---
const wcn = JSON.parse(readFileSync(join(ROOT, "wordstat-collection-normalized.json"), "utf8"));
wcn.generated_at = now;
wcn.status = "pass_a_complete";
wcn.collection_policy = { pass_a: "COMPLETE", pass_b: "NOT_STARTED" };
wcn.pass_a_collected_semantic_evidence = wsIndex.files_parsed_ok;
wcn.pass_a_frequencies_recorded = wsNorm.row_count;
wcn.external_storage_source = STORAGE_PATH;

for (const rec of wcn.records) {
  const qid = rec.query_id;
  if (noResultIds.has(qid)) {
    rec.pass_a = {
      ...(rec.pass_a || {}),
      status: "no_result_for_entered_formulation",
      evidence_ref: `evidence/wordstat/pass-a-${qid}-no-result-evidence.json`,
      row_count: 0,
    };
    rec.primary_frequency = null;
    rec.primary_frequency_status = "no_result_not_zero";
    rec.evidence_grade = "B_operator_report";
    continue;
  }
  const file = fileForQuery(qid);
  const rows = rowsForQuery(qid);
  if (file && rows.length) {
    rec.pass_a = {
      operator_syntax: rec.exact_phrase || rec.operator_syntax,
      match_mode: "broad_unquoted",
      region: "все регионы / all Russia",
      status: "ingested",
      evidence_ref: `evidence/wordstat/pass-a-${qid}-evidence.json`,
      source_path_external: file.source_path,
      source_hash: file.sha256,
      row_count: file.row_count,
    };
    rec.related_queries = rows.slice(0, 50).map((r) => ({
      phrase: r.raw_phrase,
      observed_frequency: r.observed_frequency,
      source_row: r.source_row,
    }));
    rec.relevant_variants = rows
      .filter((r) => r.preliminary_intent_class === "direct-commercial")
      .slice(0, 20)
      .map((r) => r.raw_phrase);
    rec.irrelevant_variants = rows
      .filter((r) => r.preliminary_noise_classes?.length > 0)
      .slice(0, 20)
      .map((r) => r.raw_phrase);
    rec.primary_frequency = seedFreqFromRows(qid);
    rec.primary_frequency_status = "observed_broad_national_not_regional";
    rec.evidence_grade = "B_semantic_discovery";
    rec.acquisition_limitations = [
      "Nationwide broad — not regional Novosibirsk demand",
      "Not exact phrase frequency",
      "Not traffic forecast",
    ];
  }
}
writeFileSync(join(ROOT, "wordstat-collection-normalized.json"), JSON.stringify(wcn, null, 2), "utf8");

// --- wordstat_snapshot ---
const snap = JSON.parse(readFileSync(join(ROOT, "wordstat_snapshot.cap-20260622-corv01.json"), "utf8"));
snap.pass_a_status = "COMPLETE";
snap.status = "pass_a_complete";
snap.evidence_grade = "B_semantic_discovery";
snap.external_storage_source = STORAGE_PATH;
snap.source_file_ref = "evidence/wordstat/wordstat-pass-a-file-index.json";
snap.session_safe_unknown = [
  "Pass A nationwide broad rows ingested — not regional demand",
  "Pass B regional validation not started",
  "Individual row frequencies are semantic discovery only",
];
for (const row of snap.rows) {
  const qid = row.query_id;
  if (noResultIds.has(qid)) {
    row.frequency_status = "no_result_for_entered_formulation";
    row.evidence_grade = "B_operator_report";
    row.pass_a_evidence_ref = `evidence/wordstat/pass-a-${qid}-no-result-evidence.json`;
    continue;
  }
  const file = fileForQuery(qid);
  const rows = rowsForQuery(qid);
  if (file) {
    row.frequency_status = "observed_broad_national_semantic_discovery";
    row.evidence_grade = "B_semantic_discovery";
    row.pass_a_evidence_ref = `evidence/wordstat/pass-a-${qid}-evidence.json`;
    row.related_row_count = rows.length;
    row.source_path_external = file.source_path;
    const top = rows.find((r) => r.position === 1);
    if (top?.observed_frequency != null) {
      row.operator_observed_ui_total = {
        value: top.observed_frequency,
        status: "observed_from_excel_row_1",
        interpretation: "nationwide_broad_semantic_only_not_regional_demand",
        source_row: top.source_row,
      };
    }
  }
}
writeFileSync(join(ROOT, "wordstat_snapshot.cap-20260622-corv01.json"), JSON.stringify(snap, null, 2), "utf8");

// --- demand_surface ---
const intentCounts = countByIntent(wsNorm.rows);
const ds = JSON.parse(readFileSync(join(ROOT, "demand_surface.json"), "utf8"));
ds.generated_at = now;
ds.status = "partial_wordstat_complete_pass_a_serp_captcha";
ds.evidence_summary.wordstat = {
  status: "pass_a_complete",
  grade: "B_semantic_discovery",
  pass_a: {
    status: "COMPLETE",
    excel_files_ingested: wsIndex.files_parsed_ok,
    normalized_row_count: wsNorm.row_count,
    no_result_seeds: wsIndex.no_result_seeds.map((n) => n.entered_phrase),
    semantic_evidence_count: wsIndex.files_parsed_ok,
    frequencies_recorded: wsNorm.row_count,
    failure: null,
    prior_failure: "af-007 resolved",
    external_storage_source: STORAGE_PATH,
  },
  pass_b: { status: "NOT_STARTED" },
};
ds.wordstat_pass_a_national_semantic_discovery = {
  layer_id: "wordstat_pass_a_national_semantic_discovery",
  geography: "all_russia",
  interpretation:
    "observed broad Wordstat frequency for semantic discovery — not Novosibirsk regional demand",
  pass_a_status: "COMPLETE",
  evidence_supported_phrase_count: wsNorm.row_count,
  seed_count: 20,
  excel_file_count: wsIndex.files_parsed_ok,
  broad_national_frequency_signals: "2399 row-level observations from 18 operator exports",
  commercial_vocabulary: intentCounts.commercial,
  informational_vocabulary: intentCounts.informational,
  vacancy_employment_noise: intentCounts.vacancy,
  training_course_noise: intentCounts.training,
  regulatory_noise: intentCounts.regulatory,
  troubleshooting_adjacent: intentCounts.troubleshooting,
  major_adjacent_intents: [
    "vacancy/job-seeking in broad programmer cluster",
    "training/course noise in head terms",
    "regulatory labeling vocabulary in P1/P3 clusters",
    "troubleshooting formulations in ws-p2-007 and related exports",
  ],
  no_result_seed_formulations: wsIndex.no_result_seeds,
  alternative_formulations: wsNorm.alternative_formulations,
  evidence_strength: "moderate — full Pass A Excel ingestion from MARS Storage; 2 operator no-result records preserved",
  limitations: [
    "National broad totals must not be used as Novosibirsk demand",
    "Not exact phrase frequency — broad unquoted semantic discovery",
    "Not traffic forecast or commercial click expectation",
    "Pass B not started",
    "ws-p3-004/ws-p3-005 filename slugs may not match matrix base_phrase — mapped by query_id in filename only",
  ],
  evidence_refs: [
    "evidence/wordstat/wordstat-pass-a-file-index.json",
    "evidence/wordstat/wordstat-pass-a-normalized.json",
    "C:/AI MARS STORAGE/mig/corvonero/wordstat-2026-06/",
  ],
  separation_note:
    "Layer 1 nationwide Wordstat semantic discovery — separate from Novosibirsk SERP (grade C) and future Pass B regional Wordstat",
};
writeFileSync(join(ROOT, "demand_surface.json"), JSON.stringify(ds, null, 2), "utf8");

// --- keyword_registry ---
const kr = JSON.parse(readFileSync(join(ROOT, "keyword_registry.json"), "utf8"));
kr.generated_at = now;
kr.keyword_pass_status = "pass_a_semantic_complete_pass_b_pending";
const existingNorms = new Set(kr.keywords.map((k) => k.normalized_phrase));

for (const kw of kr.keywords) {
  const qid = kw.query_id;
  if (noResultIds.has(qid)) {
    kw.wordstat_evidence = {
      status: "no_result_for_entered_formulation",
      ref: `evidence/wordstat/pass-a-${qid}-no-result-evidence.json`,
      entered_phrase: qid === "ws-p2-003" ? "доработка РМК" : "срочно программист 1С",
      numeric_frequency: "not_available",
      regional_volume_status: "UNKNOWN",
      semantic_discovery_status: "no_result_operator_report",
      orca_handoff_status: "blocked_volume_unknown",
    };
    continue;
  }
  const rows = rowsForQuery(qid);
  const file = fileForQuery(qid);
  if (rows.length && file) {
    const seedRow = rows.find((r) => r.position === 1);
    kw.wordstat_evidence = {
      status: "pass_a_semantic_ingested",
      ref: `evidence/wordstat/pass-a-${qid}-evidence.json`,
      national_broad_observed_count: seedRow?.observed_frequency ?? null,
      related_phrase_count: rows.length,
      source_path_external: file.source_path,
      source_hash: file.sha256,
      regional_volume_status: "UNKNOWN",
      semantic_discovery_status: "ingested_from_storage",
      orca_handoff_status: "candidate_pending_pass_b",
      evidence_limitations: [
        "Nationwide broad — not regional demand",
        "Not traffic forecast",
      ],
    };
    if (seedRow?.observed_frequency != null) {
      kw.numeric_slots = kw.numeric_slots || {};
      kw.numeric_slots.freq = {
        status: "observed_broad_national_semantic_only",
        value: seedRow.observed_frequency,
        source_row: seedRow.source_row,
        safe_unknown: ["Pass B regional validation not started", "Broad unquoted — not exact frequency"],
      };
    }
  }
}

let nextId = kr.keywords.length + 1;
for (const row of wsNorm.rows) {
  if (existingNorms.has(row.normalized_phrase)) continue;
  existingNorms.add(row.normalized_phrase);
  kr.keywords.push({
    keyword_id: `kw-corv01-disc-${String(nextId++).padStart(3, "0")}`,
    query_id: row.source_query_id,
    source_phrase: row.raw_phrase,
    normalized_phrase: row.normalized_phrase,
    cluster: matrix.priority_1?.find((s) => s.query_id === row.source_query_id)?.cluster ||
      matrix.priority_2?.find((s) => s.query_id === row.source_query_id)?.cluster ||
      matrix.priority_3?.find((s) => s.query_id === row.source_query_id)?.cluster ||
      "discovered",
    seed_cluster: row.seed_phrase,
    geography: "Pass A: all Russia (semantic); Pass B: pending",
    wordstat_evidence: {
      status: "pass_a_discovered_phrase",
      national_broad_observed_count: row.observed_frequency,
      source_file: basename(row.source_path_external || row.source_file || ""),
      source_hash: row.source_hash,
      source_row: row.source_row,
      regional_volume_status: "UNKNOWN",
      candidate_status: "semantic_discovery_candidate",
      orca_handoff_eligibility: "pending_pass_b_and_review",
    },
    intent_class: row.preliminary_intent_class,
    noise_classes: row.preliminary_noise_classes,
    ambiguity: row.preliminary_intent_class === "ambiguous" ? "moderate" : "low",
    review_status: "candidate_not_final_keyword",
    orca_handoff_eligibility: "pending_pass_b_and_review",
  });
}
kr.discovered_phrase_count = kr.keywords.length - 20;
writeFileSync(join(ROOT, "keyword_registry.json"), JSON.stringify(kr, null, 2), "utf8");

// --- serp_r1_index (preserve af-008) ---
const serpIndex = JSON.parse(readFileSync(join(ROOT, "serp_r1_index.json"), "utf8"));
serpIndex.generated_at = now;
writeFileSync(join(ROOT, "serp_r1_index.json"), JSON.stringify(serpIndex, null, 2), "utf8");

// --- source-registry ---
const sr = JSON.parse(readFileSync(join(ROOT, "evidence/source-registry.json"), "utf8"));
sr.generated_at = now;
for (const e of sr.entries) {
  if (e.ref_id === "ev-020") {
    e.grade = "B_semantic_discovery";
    e.collected = wsIndex.files_parsed_ok;
    e.source = "mars_storage_external";
    e.external_path = STORAGE_PATH;
  }
  if (e.ref_id === "ev-021") {
    e.grade = "B_semantic_discovery";
    e.source = "pass_a_complete";
  }
  if (e.ref_id === "ev-022") {
    e.grade = "B_semantic_discovery";
    e.source = "pass_a_ingested";
  }
  if (e.ref_id === "ev-033") {
    e.grade = "B_semantic_discovery";
    e.files_found = wsIndex.files_found;
    e.files_ingested = wsIndex.files_parsed_ok;
    e.external_storage = STORAGE_PATH;
  }
  if (e.ref_id === "ev-034") {
    e.grade = "B_semantic_discovery";
    e.row_count = wsNorm.row_count;
  }
  if (e.ref_id === "ev-030") {
    e.grade = "B_semantic_discovery";
    e.ingestion_status = "ingested";
  }
}
const af007 = sr.acquisition_failures.find((f) => f.failure_id === "af-007");
if (af007) {
  af007.status = "resolved_superseded";
  af007.resolution_date = "2026-06-22";
  af007.resolution =
    "Root cause: ingestion scanned in-repo loci only. Operator files were in MARS Storage at approved path.";
  af007.corrected_source = STORAGE_PATH;
  af007.ingestion_result = {
    files_found: wsIndex.files_found,
    files_parsed: wsIndex.files_parsed_ok,
    normalized_rows: wsNorm.row_count,
    pass_a_status: "COMPLETE",
  };
  af007.prior_false_claim = "zero Excel/CSV at approved loci — superseded";
}
const af006 = sr.acquisition_failures.find((f) => f.failure_id === "af-006");
if (af006) af006.manual_ingestion_status = "pass_a_complete";
writeFileSync(join(ROOT, "evidence/source-registry.json"), JSON.stringify(sr, null, 2), "utf8");

// --- session_manifest ---
const sm = JSON.parse(readFileSync(join(ROOT, "session_manifest.json"), "utf8"));
sm.updated_at = now;
sm.queries.wordstat_excel_files_ingested = wsIndex.files_parsed_ok;
sm.queries.wordstat_queries_collected = wsIndex.pass_a_completion.accounted;
sm.queries.wordstat_pass_a_semantic_evidence = wsIndex.files_parsed_ok;
sm.capture_profile.wordstat_pass_a_in_progress = false;
sm.capture_profile.wordstat_pass_a_partial = false;
sm.capture_profile.wordstat_pass_a_complete = true;
sm.keyword_pass_status = "pass_a_semantic_complete";
sm.keyword_pass_safe_unknown = [
  "Wordstat Pass A COMPLETE — 18 Excel from MARS Storage + 2 no-result",
  "Wordstat Pass B not started",
  "R1 Playwright SERP attempted — af-008 CAPTCHA all queries",
  "keyword_pass remains false until Pass B complete and Human Review Gate",
];
sm.evidence_discipline.wordstat_grade = "B_semantic_discovery";
sm.evidence_discipline.wordstat_pass_a_grade = "B_semantic_discovery_complete";
sm.evidence_discipline.grade_upgrade_blocked_reason =
  "SERP af-008 Playwright CAPTCHA all queries; Pass B not started; legacy af-004 direct-fetch grade C preserved";
sm.artifacts.wordstat_storage_correction_report =
  "REPORT-mig-wordstat-storage-ingestion-correction-v1.md";
writeFileSync(join(ROOT, "session_manifest.json"), JSON.stringify(sm, null, 2), "utf8");

console.log("Registries updated:", {
  pass_a: wsIndex.pass_a_completion.status,
  files: wsIndex.files_parsed_ok,
  rows: wsNorm.row_count,
  keywords: kr.keywords.length,
});

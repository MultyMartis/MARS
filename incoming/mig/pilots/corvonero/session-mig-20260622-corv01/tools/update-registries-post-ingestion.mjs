/**
 * Post-ingestion registry updater — Corvonero session mig-20260622-corv01
 */
import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const now = new Date().toISOString();

const serpSummary = JSON.parse(
  readFileSync(join(ROOT, "evidence/serp/r1-corv01/capture-run-summary.json"), "utf8")
);
const wsIndex = JSON.parse(
  readFileSync(join(ROOT, "evidence/wordstat/wordstat-pass-a-file-index.json"), "utf8")
);

// --- serp_r1_index.json ---
const serpIndex = JSON.parse(readFileSync(join(ROOT, "serp_r1_index.json"), "utf8"));
serpIndex.generated_at = now;
serpIndex.capture_method = "playwright_mobile_yandex_lr65";
serpIndex.playwright_adapter = "tools/capture-serp-r1.mjs";
serpIndex.triumph_pattern_ref =
  "incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/capture-serp-multi.mjs";
serpIndex.r1_success_count = serpSummary.results.filter((r) => r.ok).length;
serpIndex.r1_playwright_attempt_count = serpSummary.results.length;
serpIndex.acquisition_failure = serpIndex.r1_success_count === 0 ? "af-008" : null;
serpIndex.acquisition_failure_note =
  "Playwright mobile capture attempted — CAPTCHA on all queries; no bypass";
serpIndex.legacy_grade_c_fallback = "serp_results_r1/ — direct-fetch af-004 preserved";

for (const q of serpIndex.queries) {
  const cap = serpSummary.results.find((r) => r.r1_id === q.r1_id);
  q.playwright_capture = {
    artifact_dir: `evidence/serp/r1-corv01/captures/${q.r1_id}/`,
    serp_json: `evidence/serp/r1-corv01/captures/${q.r1_id}/serp.json`,
    png: `evidence/serp/r1-corv01/captures/${q.r1_id}/serp-full-page.png`,
    html: `evidence/serp/r1-corv01/captures/${q.r1_id}/serp.html`,
    captcha_status: cap?.captcha ?? "unknown",
    extracted_count: cap?.extracted_count ?? 0,
    evidence_grade: cap?.grade ?? "C",
  };
  q.r1_status = cap?.captcha === "blocked" ? "failed_captcha_playwright" : cap?.ok ? "captured" : "partial";
  q.evidence_grade = cap?.grade ?? "C";
  q.artifact_playwright = q.playwright_capture.serp_json;
  q.artifact_legacy_fallback = q.artifact;
}
writeFileSync(join(ROOT, "serp_r1_index.json"), JSON.stringify(serpIndex, null, 2), "utf8");

// --- demand_surface.json ---
const ds = JSON.parse(readFileSync(join(ROOT, "demand_surface.json"), "utf8"));
ds.generated_at = now;
ds.status = "partial_wordstat_and_serp";
ds.evidence_summary.wordstat = {
  status: "pass_a_partial",
  grade: "X_not_collected",
  pass_a: {
    status: "PARTIAL",
    excel_files_ingested: wsIndex.files_parsed_ok,
    no_result_seeds: wsIndex.no_result_seeds,
    semantic_evidence_count: 1,
    frequencies_recorded: 0,
    failure: "af-007",
  },
  pass_b: { status: "NOT_STARTED" },
};
ds.evidence_summary.serp_r1_priority = {
  status: serpIndex.r1_success_count > 0 ? "partial_captured" : "failed_captcha_playwright",
  grade: serpIndex.r1_success_count > 0 ? "B_partial" : "C",
  playwright_attempts: 10,
  success_count: serpIndex.r1_success_count,
  failure: serpIndex.r1_success_count === 0 ? "af-008" : null,
  legacy_af004_fallback_preserved: true,
};
ds.wordstat_pass_a_national_semantic_discovery = {
  layer_id: "wordstat_pass_a_national_semantic_discovery",
  geography: "all_russia",
  interpretation:
    "observed broad Wordstat frequency for semantic discovery — not Novosibirsk regional demand",
  pass_a_status: "PARTIAL",
  broad_national_vocabulary_size: wsIndex.files_parsed_ok > 0 ? "from_excel_rows" : 0,
  observed_phrase_diversity: wsIndex.files_parsed_ok > 0 ? "pending_excel" : 0,
  commercial_phrase_presence: "SAFE UNKNOWN — no Excel ingested",
  noise_density: "SAFE UNKNOWN — no Excel ingested",
  major_adjacent_intents: wsIndex.files_parsed_ok > 0 ? [] : ["SAFE UNKNOWN"],
  no_result_seeds: [
    {
      phrase: "доработка РМК",
      query_id: "ws-p2-003",
      status: "no_result_for_entered_formulation",
    },
    {
      phrase: "срочно программист 1С",
      query_id: "ws-p2-006",
      status: "no_result_for_entered_formulation",
    },
  ],
  evidence_strength: "weak — Excel exports not on disk; 2 no-result operator reports; ws-p1-001 partial",
  limitations: [
    "af-007 — zero Excel files at approved loci",
    "National broad totals must not be used as Novosibirsk demand",
    "Pass B not started",
  ],
  evidence_refs: [
    "evidence/wordstat/wordstat-pass-a-file-index.json",
    "evidence/wordstat/pass-a-ws-p1-001-evidence.json",
    "evidence/wordstat/pass-a-ws-p2-003-no-result-evidence.json",
    "evidence/wordstat/pass-a-ws-p2-006-no-result-evidence.json",
  ],
};
writeFileSync(join(ROOT, "demand_surface.json"), JSON.stringify(ds, null, 2), "utf8");

// --- keyword_registry partial updates ---
const kr = JSON.parse(readFileSync(join(ROOT, "keyword_registry.json"), "utf8"));
kr.generated_at = now;
for (const kw of kr.keywords) {
  if (kw.query_id === "ws-p2-003") {
    kw.wordstat_evidence = {
      status: "no_result_for_entered_formulation",
      ref: "evidence/wordstat/pass-a-ws-p2-003-no-result-evidence.json",
      entered_phrase: "доработка РМК",
      numeric_frequency: "not_available",
      regional_volume_status: "UNKNOWN",
      semantic_discovery_status: "no_result_operator_report",
      orca_handoff_status: "blocked_volume_unknown",
    };
  }
  if (kw.query_id === "ws-p2-006") {
    kw.wordstat_evidence = {
      status: "no_result_for_entered_formulation",
      ref: "evidence/wordstat/pass-a-ws-p2-006-no-result-evidence.json",
      entered_phrase: "срочно программист 1С",
      numeric_frequency: "not_available",
      regional_volume_status: "UNKNOWN",
      semantic_discovery_status: "no_result_operator_report",
      orca_handoff_status: "blocked_volume_unknown",
    };
  }
  if (!kw.wordstat_evidence?.national_broad_evidence && kw.query_id !== "ws-p2-003" && kw.query_id !== "ws-p2-006") {
    kw.wordstat_evidence = {
      ...(kw.wordstat_evidence || {}),
      national_broad_evidence: wsIndex.files_parsed_ok > 0 ? "pending" : "missing_export_file",
      regional_volume_status: "UNKNOWN",
      semantic_discovery_status: "awaiting_excel_ingestion",
      orca_handoff_status: "blocked_volume_unknown",
    };
  }
}
writeFileSync(join(ROOT, "keyword_registry.json"), JSON.stringify(kr, null, 2), "utf8");

console.log("Registries updated");

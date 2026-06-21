/**
 * Post ZPM-workflow SERP capture registry updater — mig-20260622-corv01
 */
import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const now = new Date().toISOString();

const summary = JSON.parse(
  readFileSync(
    join(ROOT, "evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json"),
    "utf8"
  )
);

const ZPM_BASE = "evidence/serp/zpm-workflow-corv01/capture-run/captures";

function zpmCapture(r1_id) {
  return {
    artifact_dir: `${ZPM_BASE}/${r1_id}/`,
    serp_json: `${ZPM_BASE}/${r1_id}/serp.json`,
    png: `${ZPM_BASE}/${r1_id}/serp-full-page.png`,
    html: `${ZPM_BASE}/${r1_id}/serp.html`,
  };
}

// --- serp_r1_index.json ---
const serpIndex = JSON.parse(readFileSync(join(ROOT, "serp_r1_index.json"), "utf8"));
serpIndex.generated_at = now;
serpIndex.zpm_workflow_run = {
  label: "zpm-workflow-corv01",
  adapter: "tools/capture-serp-zpm-workflow.mjs",
  triumph_ref: summary.triumph_ref,
  captured_at: summary.captured_at,
  browser_mode: summary.browser_mode,
  delay_ms_base: summary.delay_ms_base,
  summary_artifact: "evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json",
  workflow_audit: "evidence/serp/zpm-workflow-corv01/workflow-audit/zpm-serp-workflow-recovery-audit-v1.md",
  grade_b_count: summary.grade_b_count,
  grade_c_count: summary.grade_c_count,
  validation_batch_complete: summary.meta.validation_complete,
  remaining_batch_run: false,
  stopped_on_captcha: summary.meta.stopped_on_captcha,
  stopped_after: summary.meta.stopped_after ?? null,
};
serpIndex.r1_zpm_workflow_success_count = summary.grade_b_count;
serpIndex.r1_best_available_grade = summary.grade_b_count > 0 ? "B_partial" : "C";

for (const row of summary.results) {
  const q = serpIndex.queries.find((x) => x.r1_id === row.r1_id);
  if (!q) continue;
  const cap = zpmCapture(row.r1_id);
  q.zpm_workflow_capture = {
    ...cap,
    captcha_status: row.captcha,
    extracted_count: row.extracted_count,
    evidence_grade: row.grade,
    captured_at: summary.captured_at,
  };
  if (row.grade === "B") {
    q.evidence_grade = "B";
    q.r1_status = "captured_zpm_workflow";
    q.artifact_zpm_workflow = cap.serp_json;
  } else if (row.captcha === "blocked") {
    q.zpm_workflow_captcha = {
      ...cap,
      stopped_batch: true,
    };
  }
}

writeFileSync(join(ROOT, "serp_r1_index.json"), JSON.stringify(serpIndex, null, 2), "utf8");

// --- demand_surface.json ---
const demand = JSON.parse(readFileSync(join(ROOT, "demand_surface.json"), "utf8"));
demand.generated_at = now;
demand.status = "partial_wordstat_complete_pass_a_serp_partial_b";
demand.evidence_summary.wordstat.pass_b = {
  status: "NOT_REQUIRED_BY_OPERATOR",
  operator_decision_date: "2026-06-22",
  superseded_preparation_refs: [
    "corvonero-wordstat-collection-matrix-v1.json Pass B section",
    "wordstat-export-manual-20260622-corv01.md Pass B procedure"
  ],
  note: "Regional Wordstat Pass B not required; nationwide Pass A vocabulary accepted for semantic discovery",
};
demand.evidence_summary.serp_r1_priority = {
  status: "partial_captured_zpm_workflow",
  grade: "B_partial",
  playwright_r1_corv01_attempts: 10,
  r1_corv01_success_count: 0,
  zpm_workflow_attempts: summary.results.length,
  zpm_workflow_success_count: summary.grade_b_count,
  failures: {
    af_004: "historical_direct_fetch",
    af_008: "historical_r1_corv01_playwright_all_captcha",
    af_009: summary.meta.stopped_on_captcha
      ? `zpm_workflow_captcha_after_${summary.meta.stopped_after}`
      : null,
  },
  legacy_af004_fallback_preserved: true,
  r1_corv01_playwright_preserved: true,
};
writeFileSync(join(ROOT, "demand_surface.json"), JSON.stringify(demand, null, 2), "utf8");

// --- keyword_registry.json ---
const kw = JSON.parse(readFileSync(join(ROOT, "keyword_registry.json"), "utf8"));
kw.updated_at = now;
kw.keyword_pass_status = "pass_a_semantic_complete_pass_b_not_required";
kw.pass_b_status = {
  status: "NOT_REQUIRED_BY_OPERATOR",
  operator_decision: "2026-06-22",
  prior_status: "pending",
  note: "Nationwide Wordstat Pass A accepted for vocabulary; regional Pass B superseded",
};
writeFileSync(join(ROOT, "keyword_registry.json"), JSON.stringify(kw, null, 2), "utf8");

// --- source-registry.json ---
const reg = JSON.parse(readFileSync(join(ROOT, "evidence/source-registry.json"), "utf8"));
reg.updated_at = now;
reg.entries.push({
  ref_id: "ev-039",
  type: "serp_zpm_workflow_capture",
  artifact: "evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json",
  date: "2026-06-22",
  grade: "B_partial",
  source: "playwright_mobile_yandex_lr65_zpm_workflow",
  stage: "demand_surface",
  query_count: summary.results.length,
  success_count: summary.grade_b_count,
  browser_mode: "headful",
});
reg.entries.push({
  ref_id: "ev-040",
  type: "zpm_workflow_audit",
  artifact:
    "evidence/serp/zpm-workflow-corv01/workflow-audit/zpm-serp-workflow-recovery-audit-v1.md",
  date: "2026-06-22",
  grade: "A",
  source: "workflow_recovery",
  stage: "demand_surface",
});

const af008 = reg.acquisition_failures.find((f) => f.failure_id === "af-008");
if (af008) {
  af008.status = "historical_route_failed";
  af008.note =
    "Historical r1-corv01 adapter (reused browser context, headless) — all 10 CAPTCHA; superseded by zpm-workflow-corv01 partial success";
  af008.zpm_workflow_partial_success = {
    grade_b_queries: summary.results.filter((r) => r.grade === "B").map((r) => r.r1_id),
    date: "2026-06-22",
  };
}

reg.acquisition_failures.push({
  failure_id: "af-009",
  topic: "ZPM-workflow validation batch — CAPTCHA on third query",
  reason: `Headful fresh-browser Triumph-pattern capture; CAPTCHA on ${summary.meta.stopped_after} after 2 Grade B captures`,
  impact: "Remaining 7 R1 queries not executed; partial regional SERP evidence available",
  grade_cap: "B_partial",
  status: "open_partial",
  collection_date: "2026-06-22",
  remediation: "Resume remaining batch after cooldown with same pacing; or operator manual CAPTCHA solve",
  does_not_supersede_af_008: true,
});

writeFileSync(join(ROOT, "evidence/source-registry.json"), JSON.stringify(reg, null, 2), "utf8");

// --- session_manifest.json ---
const manifest = JSON.parse(readFileSync(join(ROOT, "session_manifest.json"), "utf8"));
manifest.updated_at = now;
manifest.capture_profile.wordstat_pass_b_prepared = true;
manifest.capture_profile.wordstat_pass_b_not_required = true;
manifest.capture_profile.serp_zpm_workflow_attempt = true;
manifest.queries.wordstat_pass_b_collected = 0;
manifest.queries.wordstat_pass_b_status = "NOT_REQUIRED_BY_OPERATOR";
manifest.queries.r1_zpm_workflow_captured = summary.grade_b_count;
manifest.queries.r1_zpm_workflow_attempted = summary.results.length;
manifest.artifacts.serp_zpm_workflow_captures =
  "evidence/serp/zpm-workflow-corv01/capture-run/captures/";
manifest.artifacts.serp_zpm_workflow_report =
  "REPORT-mig-zpm-serp-workflow-recovery-and-corvonero-execution-v1.md";
manifest.artifacts.zpm_workflow_audit =
  "evidence/serp/zpm-workflow-corv01/workflow-audit/zpm-serp-workflow-recovery-audit-v1.md";
manifest.evidence_discipline.r1_priority_serp_grade = "B_partial";
manifest.evidence_discipline.r1_zpm_workflow_attempt =
  "2026-06-22 — 2/3 validation Grade B; CAPTCHA r1q07; remaining batch not run";
manifest.evidence_discipline.r1_playwright_attempt =
  "2026-06-22 — af-008 historical r1-corv01 all CAPTCHA preserved";
manifest.evidence_discipline.grade_upgrade_blocked_reason =
  "Partial R1 SERP (2/10 Grade B); 7 queries not captured; af-009 captcha on r1q07";
manifest.keyword_pass_safe_unknown = manifest.keyword_pass_safe_unknown.filter(
  (s) => !s.includes("Pass B not started")
);
manifest.keyword_pass_safe_unknown.push(
  "Wordstat Pass B NOT REQUIRED BY OPERATOR — nationwide Pass A accepted",
  "R1 SERP partial — zpm-workflow 2 Grade B; 7 queries pending after af-009"
);
writeFileSync(join(ROOT, "session_manifest.json"), JSON.stringify(manifest, null, 2), "utf8");

// --- evidence/review.md ---
const review = `# MIG Human Review — Demand Surface pass

**Session:** \`mig-20260622-corv01\`  
**Project:** PRJ-0013 — Корво Неро  
**Stage:** MIG Demand Surface  
**Date:** 2026-06-22  
**Updated:** 2026-06-22 — ZPM-workflow SERP partial capture + Pass B operator decision

## Review status

| Field | Value |
|-------|-------|
| Business Intake | **APPROVED** |
| ATLAS Registration | **APPROVED** |
| MIG Research Request | **APPROVED FOR EXECUTION** |
| Stage 1 | **COMPLETE** |
| Stage 2 | **COMPLETE** |
| Demand Surface pass | **DEPOSITED — PENDING OPERATOR REVIEW** |
| Wordstat Pass A | **COMPLETE** — 18 Excel + 2 no-result; 2399 rows |
| Wordstat Pass B | **NOT REQUIRED BY OPERATOR** — superseded |
| R1 af-004 (direct fetch) | **Historical failure preserved** — grade C |
| R1 af-008 (r1-corv01 Playwright) | **Historical failure preserved** — all CAPTCHA |
| R1 zpm-workflow | **PARTIAL** — 2 Grade B (r1q01, r1q05); CAPTCHA r1q07 (af-009) |
| Keyword Registry | **DRAFT** — Pass A semantic ingested |
| Research Pack approval | **NOT APPROVED** — pending SERP review |
| ORCA handoff | **BLOCKED** |

## Evidence summary

| Layer | Grade | Notes |
|-------|-------|-------|
| Stage 1 SERP | **C** | Preserved |
| Stage 2 live SERP | **C** | Preserved |
| R1 r1-corv01 Playwright | **C** | af-008 — preserved |
| R1 zpm-workflow | **B_partial** | r1q01, r1q05 Grade B |
| R1 legacy fallback | **C** | af-004 preserved |
| Wordstat Pass A | **B_semantic_discovery** | Complete |
| Wordstat Pass B | **N/A** | Not required by operator |
| Demand Surface | **C_partial → B_partial SERP layer** | Partial regional SERP |
| Competitor shortlist | **B** | Unchanged |

## Operator actions required

1. Review 2 Grade B SERP captures (r1q01, r1q05) under \`evidence/serp/zpm-workflow-corv01/\`
2. Decide: resume remaining 7 queries after cooldown, or accept partial SERP for Research Pack scoping
3. Research Pack — **not blocked by Pass B**; blocked until SERP run reviewed or accepted with limitations

## SAFE UNKNOWN preserved

- CPC, CTR, conversion, CPL, ad density
- 7 uncaptured R1 queries
- Research Pack assembly — pending operator SERP review

---

*Scaffold only — not signed.*
`;
writeFileSync(join(ROOT, "evidence/review.md"), review, "utf8");

console.log("Registries updated.", {
  grade_b: summary.grade_b_count,
  stopped_after: summary.meta.stopped_after,
});

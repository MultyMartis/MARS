/**
 * Throttled SERP resume registry updater — mig-20260622-corv01
 * Merges cumulative capture evidence; idempotent source-registry updates.
 */
import { readFileSync, writeFileSync, readdirSync, existsSync, appendFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const CAPTURE_ROOT = join(
  ROOT,
  "evidence/serp/zpm-workflow-corv01/capture-run/captures"
);
const SUMMARY_PATH = join(
  ROOT,
  "evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json"
);
const now = new Date().toISOString();
const batchLabel = process.argv[2] || "unknown";

function zpmCapture(r1_id) {
  const base = `evidence/serp/zpm-workflow-corv01/capture-run/captures/${r1_id}/`;
  return {
    artifact_dir: base,
    serp_json: `${base}serp.json`,
    png: `${base}serp-full-page.png`,
    html: `${base}serp.html`,
  };
}

function loadSummary() {
  if (!existsSync(SUMMARY_PATH)) {
    return {
      results: [],
      grade_b_count: 0,
      grade_c_count: 0,
      meta: {},
    };
  }
  return JSON.parse(readFileSync(SUMMARY_PATH, "utf8"));
}

function scanCaptures() {
  if (!existsSync(CAPTURE_ROOT)) return [];
  const rows = [];
  for (const dir of readdirSync(CAPTURE_ROOT)) {
    const serpPath = join(CAPTURE_ROOT, dir, "serp.json");
    if (!existsSync(serpPath)) continue;
    try {
      const j = JSON.parse(readFileSync(serpPath, "utf8"));
      rows.push({
        r1_id: j.query_id || dir,
        query: j.query,
        ok: j.evidence_grade === "B",
        grade: j.evidence_grade,
        captcha: j.captcha_status,
        extracted_count: j.extracted_count ?? 0,
        page_title: j.page_title ?? null,
        timestamp: j.timestamp,
      });
    } catch {
      /* skip malformed */
    }
  }
  rows.sort((a, b) => (a.r1_id || "").localeCompare(b.r1_id || ""));
  return rows;
}

const summary = loadSummary();
const scanned = scanCaptures();
const byId = new Map((summary.results || []).map((r) => [r.r1_id, r]));
for (const row of scanned) byId.set(row.r1_id, { ...byId.get(row.r1_id), ...row });
const allResults = [...byId.values()];
const gradeB = allResults.filter((r) => r.grade === "B");
const gradeC = allResults.filter((r) => r.grade === "C");
const captchaRows = allResults.filter((r) => r.captcha === "blocked");

const mergedSummary = {
  ...summary,
  captured_at: now,
  workflow_label: "zpm-workflow-corv01",
  source_script: "tools/capture-serp-zpm-workflow.mjs",
  triumph_ref:
    "incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/capture-serp-multi.mjs",
  browser_mode: "headful",
  delay_ms_base: 90000,
  delay_ms_jitter: 30000,
  region_lr: "65",
  throttled_resume: true,
  last_registry_batch: batchLabel,
  results: allResults,
  grade_b_count: gradeB.length,
  grade_c_count: gradeC.length,
  meta: {
    ...(summary.meta || {}),
    throttled_resume_active: true,
    last_batch: batchLabel,
    stopped_on_captcha: summary.meta?.stopped_on_captcha ?? false,
    stopped_after: summary.meta?.stopped_after ?? null,
  },
};
writeFileSync(SUMMARY_PATH, JSON.stringify(mergedSummary, null, 2), "utf8");

// --- serp_r1_index.json ---
const serpIndex = JSON.parse(readFileSync(join(ROOT, "serp_r1_index.json"), "utf8"));
serpIndex.generated_at = now;
serpIndex.zpm_workflow_run = {
  label: "zpm-workflow-corv01",
  adapter: "tools/capture-serp-zpm-workflow.mjs",
  triumph_ref: mergedSummary.triumph_ref,
  captured_at: now,
  browser_mode: "headful",
  delay_ms_base: 90000,
  delay_ms_jitter: 30000,
  summary_artifact: "evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json",
  workflow_audit:
    "evidence/serp/zpm-workflow-corv01/workflow-audit/zpm-serp-workflow-recovery-audit-v1.md",
  grade_b_count: gradeB.length,
  grade_c_count: gradeC.length,
  throttled_resume: true,
  last_batch: batchLabel,
  stopped_on_captcha: mergedSummary.meta.stopped_on_captcha,
  stopped_after: mergedSummary.meta.stopped_after,
};
serpIndex.r1_zpm_workflow_success_count = gradeB.length;
serpIndex.r1_best_available_grade =
  gradeB.length >= 8 ? "B" : gradeB.length >= 4 ? "B_partial" : gradeB.length > 0 ? "B_partial" : "C";

for (const row of allResults) {
  const q = serpIndex.queries.find((x) => x.r1_id === row.r1_id);
  if (!q) continue;
  const cap = zpmCapture(row.r1_id);
  q.zpm_workflow_capture = {
    ...cap,
    captcha_status: row.captcha,
    extracted_count: row.extracted_count,
    evidence_grade: row.grade,
    captured_at: row.timestamp || now,
  };
  if (row.grade === "B") {
    q.evidence_grade = "B";
    q.r1_status = "captured_zpm_workflow";
    q.artifact_zpm_workflow = cap.serp_json;
  } else if (row.captcha === "blocked") {
    q.zpm_workflow_captcha = { ...cap, stopped_batch: true };
  }
}
writeFileSync(join(ROOT, "serp_r1_index.json"), JSON.stringify(serpIndex, null, 2), "utf8");

// --- demand_surface.json ---
const demand = JSON.parse(readFileSync(join(ROOT, "demand_surface.json"), "utf8"));
demand.generated_at = now;
demand.status = "partial_wordstat_complete_pass_a_serp_partial_b";
demand.evidence_summary.serp_r1_priority = {
  status: gradeB.length >= 8 ? "captured_zpm_workflow" : "partial_captured_zpm_workflow",
  grade: gradeB.length >= 8 ? "B" : "B_partial",
  playwright_r1_corv01_attempts: 10,
  r1_corv01_success_count: 0,
  zpm_workflow_attempts: allResults.length,
  zpm_workflow_success_count: gradeB.length,
  throttled_resume_last_batch: batchLabel,
  failures: {
    af_004: "historical_direct_fetch",
    af_008: "historical_r1_corv01_playwright_all_captcha",
    af_009: captchaRows.length
      ? `zpm_workflow_captcha_${captchaRows.map((r) => r.r1_id).join("_")}`
      : null,
  },
  legacy_af004_fallback_preserved: true,
  r1_corv01_playwright_preserved: true,
};
writeFileSync(join(ROOT, "demand_surface.json"), JSON.stringify(demand, null, 2), "utf8");

// --- keyword_registry.json ---
const kw = JSON.parse(readFileSync(join(ROOT, "keyword_registry.json"), "utf8"));
kw.updated_at = now;
writeFileSync(join(ROOT, "keyword_registry.json"), JSON.stringify(kw, null, 2), "utf8");

// --- source-registry.json ---
const reg = JSON.parse(readFileSync(join(ROOT, "evidence/source-registry.json"), "utf8"));
reg.updated_at = now;

const evThrottled = reg.entries.find((e) => e.ref_id === "ev-041");
const throttledEntry = {
  ref_id: "ev-041",
  type: "serp_zpm_workflow_throttled_resume",
  artifact: "evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json",
  date: "2026-06-22",
  grade: gradeB.length >= 8 ? "B" : "B_partial",
  source: "playwright_mobile_yandex_lr65_zpm_workflow_throttled",
  stage: "demand_surface",
  last_batch: batchLabel,
  grade_b_count: gradeB.length,
  grade_c_count: gradeC.length,
  captcha_queries: captchaRows.map((r) => r.r1_id),
};
if (evThrottled) Object.assign(evThrottled, throttledEntry);
else reg.entries.push(throttledEntry);

const af009 = reg.acquisition_failures.find((f) => f.failure_id === "af-009");
if (af009) {
  af009.status = captchaRows.length ? "open_partial" : "resolved_or_superseded";
  af009.grade_b_queries = gradeB.map((r) => r.r1_id);
  af009.captcha_queries = captchaRows.map((r) => r.r1_id);
  af009.last_throttled_batch = batchLabel;
  af009.note = captchaRows.length
    ? `Throttled resume; CAPTCHA on ${captchaRows.map((r) => r.r1_id).join(", ")}; ${gradeB.length} Grade B`
    : `Throttled resume complete; ${gradeB.length} Grade B captures`;
}

writeFileSync(join(ROOT, "evidence/source-registry.json"), JSON.stringify(reg, null, 2), "utf8");

// --- session_manifest.json ---
const manifest = JSON.parse(readFileSync(join(ROOT, "session_manifest.json"), "utf8"));
manifest.updated_at = now;
manifest.queries.r1_zpm_workflow_captured = gradeB.length;
manifest.queries.r1_zpm_workflow_attempted = allResults.length;
manifest.evidence_discipline.r1_priority_serp_grade =
  gradeB.length >= 8 ? "B" : "B_partial";
manifest.evidence_discipline.r1_zpm_workflow_attempt = `2026-06-22 — throttled resume; ${gradeB.length}/10 Grade B; last batch ${batchLabel}`;
manifest.evidence_discipline.grade_upgrade_blocked_reason =
  gradeB.length >= 8
    ? null
    : `Partial R1 SERP (${gradeB.length}/10 Grade B); captcha: ${captchaRows.map((r) => r.r1_id).join(", ") || "none"}`;
writeFileSync(join(ROOT, "session_manifest.json"), JSON.stringify(manifest, null, 2), "utf8");

// --- execution-log.md append ---
const logPath = join(ROOT, "evidence/serp/zpm-workflow-corv01/capture-run/execution-log.md");
const logLine = `- ${now} — REGISTRY throttled batch \`${batchLabel}\`: Grade B=${gradeB.length}, Grade C=${gradeC.length}, captcha=${captchaRows.map((r) => r.r1_id).join(",") || "none"}\n`;
if (existsSync(logPath)) {
  appendFileSync(logPath, logLine, "utf8");
}

// --- evidence/review.md ---
const gradeBIds = gradeB.map((r) => r.r1_id).join(", ");
const captchaIds = captchaRows.map((r) => r.r1_id).join(", ") || "none";
const pending = 10 - gradeB.length;
const review = `# MIG Human Review — Demand Surface pass

**Session:** \`mig-20260622-corv01\`  
**Project:** PRJ-0013 — Корво Неро  
**Stage:** MIG Demand Surface  
**Date:** 2026-06-22  
**Updated:** ${now.slice(0, 10)} — throttled ZPM-workflow SERP resume (batch \`${batchLabel}\`)

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
| R1 zpm-workflow | **${gradeB.length >= 8 ? "COMPLETE" : "PARTIAL"}** — ${gradeB.length} Grade B (${gradeBIds || "none"}) |
| CAPTCHA queries | **${captchaIds}** |
| Keyword Registry | **DRAFT** — Pass A semantic ingested |
| Research Pack approval | **NOT APPROVED** — pending SERP review |
| ORCA handoff | **BLOCKED** |

## Evidence summary

| Layer | Grade | Notes |
|-------|-------|-------|
| Stage 1 SERP | **C** | Preserved |
| Stage 2 live SERP | **C** | Preserved |
| R1 r1-corv01 Playwright | **C** | af-008 — preserved |
| R1 zpm-workflow | **${gradeB.length >= 8 ? "B" : "B_partial"}** | ${gradeBIds || "none"} |
| R1 legacy fallback | **C** | af-004 preserved |
| Wordstat Pass A | **B_semantic_discovery** | Complete |
| Wordstat Pass B | **N/A** | Not required by operator |
| Demand Surface | **C_partial → ${gradeB.length >= 8 ? "B" : "B_partial"} SERP layer** | Throttled resume |
| Competitor shortlist | **B** | Unchanged |

## Operator actions required

1. Review Grade B SERP captures under \`evidence/serp/zpm-workflow-corv01/\`
2. ${pending > 0 ? `${pending} queries uncaptured or CAPTCHA-blocked` : "All 10 R1 queries captured Grade B"}
3. Research Pack — pending operator SERP review or acceptance with limitations

## SAFE UNKNOWN preserved

- CPC, CTR, conversion, CPL, ad density
- ${pending > 0 ? `${pending} uncaptured or CAPTCHA R1 queries` : "None — full R1 coverage"}
- Research Pack assembly — pending operator SERP review

---

*Scaffold only — not signed.*
`;
writeFileSync(join(ROOT, "evidence/review.md"), review, "utf8");

console.log("Throttled registries updated.", {
  batch: batchLabel,
  grade_b: gradeB.length,
  grade_c: gradeC.length,
  captcha: captchaRows.map((r) => r.r1_id),
});

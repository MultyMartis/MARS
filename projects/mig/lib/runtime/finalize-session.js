"use strict";

const { mergeSafeUnknown } = require("./update-session-manifest");

const GRADE_ORDER = { A: 0, B: 1, C: 2, D: 3, X: 4 };

function worstGrade(grades) {
  let worst = "A";
  for (const g of grades) {
    if (GRADE_ORDER[g] > GRADE_ORDER[worst]) {
      worst = g;
    }
  }
  return worst;
}

function computeSessionGrade(manifest) {
  const grades = [];
  if (manifest.serp?.mode === "fallback") {
    grades.push("D");
  } else if (manifest.serp?.mode) {
    grades.push("C");
  }
  const cd = manifest.competitor_discovery?.status;
  if (cd === "complete") {
    grades.push("B");
  } else if (cd === "empty") {
    grades.push("D");
  }
  const wa = manifest.website_acquisition?.status;
  if (wa === "complete") {
    grades.push("B");
  } else if (wa === "partial") {
    grades.push("C");
  } else if (wa === "failed") {
    grades.push("D");
  }
  const la = manifest.landing_analysis?.status;
  if (la === "complete") {
    grades.push("B");
  } else if (la === "skipped") {
    grades.push("D");
  }
  if (!grades.length) {
    return "X";
  }
  return worstGrade(grades);
}

function buildCoverage(manifest) {
  const completed = ["intake"];
  const skipped = [];
  const failed = [];

  const passMap = [
    ["search", manifest.pass_status?.search],
    ["competitors", manifest.pass_status?.competitors],
    ["websites", manifest.pass_status?.websites],
    ["landings", manifest.pass_status?.landings],
    ["keywords", manifest.pass_status?.keywords],
    ["deep_research", manifest.pass_status?.deep_research],
    ["pack", manifest.pass_status?.pack],
  ];

  for (const [phase, state] of passMap) {
    if (state === "complete" || state === "empty") {
      if (!completed.includes(phase)) {
        completed.push(phase);
      }
    } else if (state === "skipped") {
      skipped.push(phase);
    } else if (state === "failed") {
      failed.push(phase);
    }
  }

  const partial =
    failed.length > 0 ||
    manifest.website_acquisition?.status === "partial" ||
    manifest.competitor_discovery?.status === "empty" ||
    (manifest.serp?.mode === "fallback" && manifest.competitor_discovery?.competitor_count === 0);

  return {
    session_grade: computeSessionGrade(manifest),
    phases_completed: completed,
    phases_skipped: skipped,
    phases_failed: failed,
    partial,
  };
}

/**
 * Terminal manifest state after P6 pack assembly.
 */
function finalizeSession(manifest, { packWritten = true, fatal = false } = {}) {
  const coverage = buildCoverage(manifest);
  let stage = "draft_complete";
  let status = "complete";
  let packState = "draft";

  if (fatal || manifest.pass_status?.search === "failed") {
    stage = "failed";
    status = "failed";
    packState = "failed";
  } else if (coverage.partial) {
    stage = "partial_complete";
    status = "partial";
    packState = packWritten ? "draft" : "failed";
  }

  const migPhase = manifest.pack?.mig_phase || manifest.mig_phase || "1";

  return {
    ...manifest,
    updated_at: new Date().toISOString(),
    status,
    stage,
    coverage,
    pack: {
      ...manifest.pack,
      pack_state: packState,
      mig_phase: migPhase,
    },
    approval: {
      ...manifest.approval,
      pack_state: packState,
    },
    pass_status: {
      ...manifest.pass_status,
      pack: packWritten ? "complete" : "failed",
    },
    runtime_metadata: {
      ...manifest.runtime_metadata,
      last_pass: "pack",
    },
  };
}

function mergeSerpSafeUnknown(manifest, serpResult) {
  return {
    ...manifest,
    safe_unknown: mergeSafeUnknown(manifest, serpResult.safe_unknown || []),
  };
}

module.exports = {
  finalizeSession,
  buildCoverage,
  computeSessionGrade,
  mergeSerpSafeUnknown,
};

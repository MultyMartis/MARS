"use strict";

const fs = require("fs");
const path = require("path");

const INDEX_FILENAME = "website_snapshots.json";
const GRADE_ORDER = { A: 0, B: 1, C: 2, D: 3, X: 4 };

function worstGrade(grades) {
  if (!grades.length) {
    return "X";
  }
  return grades.reduce((worst, grade) =>
    GRADE_ORDER[grade] > GRADE_ORDER[worst] ? grade : worst
  );
}

function deriveSessionCoverage(snapshots) {
  const successes = snapshots.filter((s) => s.status === "success");
  if (!snapshots.length) {
    return "unknown";
  }
  if (successes.length === snapshots.length) {
    return "complete";
  }
  if (successes.length > 0) {
    return "partial";
  }
  return "minimal";
}

function snapshotArtifactRefs(snapshotId) {
  const base = `snapshots/sites/${snapshotId}`;
  return {
    website_snapshot: `${base}/website_snapshot.json`,
    page_html: `${base}/page.html`,
    headers: `${base}/headers.json`,
  };
}

function buildSnapshotRecord(planEntry, fetchResult, facts, sessionId, captureTime) {
  const snapshotId = planEntry.snapshot_id;
  const acquisitionMethod = fetchResult.acquisition_method || "http_get";
  let status = fetchResult.status || "failed";
  const safeUnknown = [];

  if (status === "success" && facts.acquisition_status === "render_required") {
    status = "render_required";
    safeUnknown.push("JavaScript-rendered page — static capture insufficient");
  } else if (status === "success" && facts.acquisition_status === "empty") {
    status = "empty";
    safeUnknown.push("Empty response body");
  } else if (status === "success") {
    status = facts.acquisition_status === "success" ? "success" : status;
  }

  if (fetchResult.error && status !== "success") {
    safeUnknown.push(`Fetch error: ${fetchResult.error}`);
  }

  let evidenceGrade = "X";
  if (status === "success") {
    evidenceGrade = acquisitionMethod === "fixture" ? "B" : "B";
    if (!fetchResult.body) {
      evidenceGrade = "C";
    }
  } else if (status === "render_required" || status === "empty") {
    evidenceGrade = "D";
  }

  const finalDomain = planEntry.domain || "unknown";

  return {
    snapshot_id: snapshotId,
    session_id: sessionId,
    competitor_id: planEntry.competitor_id || null,
    domain: finalDomain,
    requested_url: planEntry.requested_url,
    final_url: fetchResult.final_url || planEntry.requested_url,
    page_role: planEntry.page_role || "homepage",
    capture_time: captureTime,
    status,
    acquisition_method: acquisitionMethod === "fixture" ? "http_get_dom" : "http_get_dom",
    http_status: fetchResult.http_status ?? null,
    redirect_chain: fetchResult.redirect_chain || [],
    content_type: fetchResult.content_type || null,
    charset: null,
    render_status: facts.render_status || "unknown",
    fetch_duration_ms: fetchResult.duration_ms ?? null,
    title: facts.title ?? null,
    meta_description: facts.meta_description ?? null,
    canonical_url: facts.canonical_url ?? null,
    lang: facts.lang ?? null,
    headings: facts.headings || [],
    contacts: facts.contacts || { phones: [], emails: [], addresses: [], messengers: [] },
    offers: facts.offers || [],
    pricing_signals: facts.pricing_signals || [],
    cta_elements: facts.cta_elements || [],
    forms: facts.forms || [],
    links: facts.links || { internal: [], external: [] },
    trust_signals_visible: facts.trust_signals_visible || [],
    visible_text_excerpt: facts.visible_text_excerpt ?? null,
    artifact_refs: snapshotArtifactRefs(snapshotId),
    evidence_grade: evidenceGrade,
    safe_unknown: safeUnknown,
  };
}

function writeSnapshotArtifacts(sessionDir, snapshot, fetchResult) {
  const snapshotDir = path.join(sessionDir, "snapshots", "sites", snapshot.snapshot_id);
  fs.mkdirSync(snapshotDir, { recursive: true });

  const htmlPath = path.join(snapshotDir, "page.html");
  const headersPath = path.join(snapshotDir, "headers.json");
  const snapshotPath = path.join(snapshotDir, "website_snapshot.json");

  fs.writeFileSync(htmlPath, fetchResult.body || "", "utf8");
  fs.writeFileSync(
    headersPath,
    `${JSON.stringify(
      {
        http_status: fetchResult.http_status,
        final_url: fetchResult.final_url,
        redirect_chain: fetchResult.redirect_chain || [],
        headers: fetchResult.headers || {},
        fetch_duration_ms: fetchResult.duration_ms ?? null,
        captured_at: snapshot.capture_time,
      },
      null,
      2
    )}\n`,
    "utf8"
  );
  fs.writeFileSync(snapshotPath, `${JSON.stringify(snapshot, null, 2)}\n`, "utf8");

  return {
    snapshot_dir: snapshotDir,
    website_snapshot: snapshotPath,
    page_html: htmlPath,
    headers: headersPath,
  };
}

function buildWebsiteSnapshotsIndex(sessionId, urlPlan, snapshots, options = {}) {
  const generatedAt = options.generated_at || new Date().toISOString();
  const grades = snapshots.map((s) => s.evidence_grade);
  const sessionSafeUnknown = options.safe_unknown || [];

  if (urlPlan.skipped?.length) {
    sessionSafeUnknown.push(
      `Website capture partial: ${urlPlan.skipped.length} competitor(s) skipped (see url_plan)`
    );
  }

  return {
    schema_version: "0.1",
    session_id: sessionId,
    generated_at: generatedAt,
    acquisition_phase: 3,
    url_plan: urlPlan.entries.map((entry) => ({
      snapshot_id: entry.snapshot_id,
      competitor_id: entry.competitor_id,
      requested_url: entry.requested_url,
      page_role: entry.page_role,
    })),
    snapshots,
    session_coverage: deriveSessionCoverage(snapshots),
    section_evidence_grade: worstGrade(grades),
    safe_unknown: sessionSafeUnknown,
  };
}

function writeWebsiteSnapshots(sessionDir, index) {
  const indexPath = path.join(sessionDir, INDEX_FILENAME);
  fs.writeFileSync(indexPath, `${JSON.stringify(index, null, 2)}\n`, "utf8");
  return { path: indexPath, filename: INDEX_FILENAME };
}

function deriveWebsiteManifestMeta(index) {
  const successCount = index.snapshots.filter((s) => s.status === "success").length;
  return {
    status: successCount > 0 ? "complete" : index.snapshots.length ? "partial" : "empty",
    snapshot_count: index.snapshots.length,
    success_count: successCount,
    generated_at: index.generated_at,
    artifact_file: INDEX_FILENAME,
    section_evidence_grade: index.section_evidence_grade,
    session_coverage: index.session_coverage,
  };
}

module.exports = {
  INDEX_FILENAME,
  buildSnapshotRecord,
  buildWebsiteSnapshotsIndex,
  writeSnapshotArtifacts,
  writeWebsiteSnapshots,
  deriveWebsiteManifestMeta,
  snapshotArtifactRefs,
};

"use strict";

const fs = require("fs");
const path = require("path");

const DEFAULT_REGISTRY_PATH = path.join(
  __dirname,
  "..",
  "..",
  "config",
  "landing-block-registry-v0.json"
);

const GRADE_ORDER = { A: 0, B: 1, C: 2, D: 3, X: 4 };

function loadBlockRegistry(registryPath) {
  const filePath = registryPath || DEFAULT_REGISTRY_PATH;
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function worstGrade(grades) {
  if (!grades.length) {
    return "X";
  }
  return grades.reduce((worst, grade) =>
    GRADE_ORDER[grade] > GRADE_ORDER[worst] ? grade : worst
  );
}

function makeEvidence(snapshot, options = {}) {
  const source = options.source || "website_snapshot";
  return {
    source,
    snapshot_id: options.snapshot_id || snapshot.snapshot_id || null,
    snapshot_field: options.snapshot_field || null,
    html_anchor: options.html_anchor || null,
    verbatim_text: options.verbatim_text || null,
    capture_time: snapshot.capture_time,
    ambiguity: options.ambiguity || "none",
  };
}

function padSeq(n, width = 3) {
  return String(n).padStart(width, "0");
}

function landingIdFor(sessionId, seq) {
  return `${sessionId}-la${padSeq(seq)}`;
}

function blockIdFor(landingId, seq) {
  return `${landingId}-b${padSeq(seq)}`;
}

function offerIdFor(landingId, seq) {
  return `${landingId}-of${padSeq(seq)}`;
}

function ctaIdFor(landingId, seq) {
  return `${landingId}-cta${padSeq(seq)}`;
}

function trustIdFor(landingId, seq) {
  return `${landingId}-tr${padSeq(seq)}`;
}

function pricingIdFor(landingId, seq) {
  return `${landingId}-pr${padSeq(seq)}`;
}

function contactIdFor(landingId, seq) {
  return `${landingId}-co${padSeq(seq)}`;
}

function formIdFor(landingId, seq) {
  return `${landingId}-fm${padSeq(seq)}`;
}

function readPageHtml(sessionDir, snapshot) {
  const ref = snapshot.artifact_refs?.page_html;
  if (!ref) {
    return null;
  }
  const htmlPath = path.join(sessionDir, ref);
  if (!fs.existsSync(htmlPath)) {
    return null;
  }
  return fs.readFileSync(htmlPath, "utf8");
}

function readWebsiteSnapshotsIndex(sessionDir) {
  const indexPath = path.join(sessionDir, "website_snapshots.json");
  if (!fs.existsSync(indexPath)) {
    throw new Error(`website_snapshots.json not found in ${sessionDir}`);
  }
  return JSON.parse(fs.readFileSync(indexPath, "utf8"));
}

function headingMatchesPatterns(text, patterns) {
  if (!text) {
    return false;
  }
  const lower = text.toLowerCase();
  return patterns.some((p) => lower.includes(p.toLowerCase()));
}

function uniqueByKey(items, keyFn) {
  const seen = new Set();
  const out = [];
  for (const item of items) {
    const key = keyFn(item);
    if (seen.has(key)) {
      continue;
    }
    seen.add(key);
    out.push(item);
  }
  return out;
}

module.exports = {
  loadBlockRegistry,
  worstGrade,
  makeEvidence,
  landingIdFor,
  blockIdFor,
  offerIdFor,
  ctaIdFor,
  trustIdFor,
  pricingIdFor,
  contactIdFor,
  formIdFor,
  readPageHtml,
  readWebsiteSnapshotsIndex,
  headingMatchesPatterns,
  uniqueByKey,
  DEFAULT_REGISTRY_PATH,
};

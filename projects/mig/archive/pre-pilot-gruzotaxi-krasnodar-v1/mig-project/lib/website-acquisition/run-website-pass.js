"use strict";

const fs = require("fs");
const path = require("path");

const { buildUrlPlan, loadRules } = require("./build-url-plan");
const { fetchPage } = require("./fetch-page");
const { extractPageFacts } = require("./extract-page-facts");
const {
  buildSnapshotRecord,
  buildWebsiteSnapshotsIndex,
  writeSnapshotArtifacts,
  writeWebsiteSnapshots,
} = require("./write-website-snapshot");

function readCompetitorsArtifact(sessionDir) {
  const filePath = path.join(sessionDir, "competitors.json");
  if (!fs.existsSync(filePath)) {
    throw new Error(`competitors.json not found in ${sessionDir}`);
  }
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Run website acquisition pass for a session directory.
 * @param {string} sessionDir
 * @param {{ signals?: object, url_cap?: number, fixtureRoot?: string, fixtureMap?: Record<string,string>, rules?: object, rulesPath?: string }} [options]
 */
async function runWebsitePass(sessionDir, options = {}) {
  const rules = options.rules || loadRules(options.rulesPath);
  const competitorsArtifact = options.competitorsArtifact || readCompetitorsArtifact(sessionDir);
  const sessionId = competitorsArtifact.session_id;
  const urlPlan = buildUrlPlan(competitorsArtifact, {
    signals: options.signals,
    url_cap: options.url_cap,
    rules,
  });

  const snapshots = [];
  const captureTime = new Date().toISOString();

  for (let i = 0; i < urlPlan.entries.length; i += 1) {
    const entry = urlPlan.entries[i];
    if (i > 0 && rules.inter_request_delay_ms > 0) {
      await delay(rules.inter_request_delay_ms);
    }

    const fetchResult = await fetchPage(entry.requested_url, {
      timeoutMs: rules.fetch_timeout_ms,
      maxRedirects: rules.max_redirects,
      fixtureRoot: options.fixtureRoot,
      fixtureMap: options.fixtureMap,
    });

    const facts =
      fetchResult.body && fetchResult.ok
        ? extractPageFacts(fetchResult.body, fetchResult.final_url || entry.requested_url, { rules })
        : {
            headings: [],
            contacts: { phones: [], emails: [], addresses: [], messengers: [] },
            offers: [],
            pricing_signals: [],
            cta_elements: [],
            forms: [],
            links: { internal: [], external: [] },
            trust_signals_visible: [],
            render_status: "unknown",
            acquisition_status: fetchResult.status === "timeout" ? "timeout" : "failed",
          };

    const snapshot = buildSnapshotRecord(entry, fetchResult, facts, sessionId, captureTime);
    writeSnapshotArtifacts(sessionDir, snapshot, fetchResult);
    snapshots.push(snapshot);
  }

  const index = buildWebsiteSnapshotsIndex(sessionId, urlPlan, snapshots, {
    generated_at: captureTime,
    safe_unknown: [],
  });
  const written = writeWebsiteSnapshots(sessionDir, index);

  return {
    session_id: sessionId,
    session_dir: sessionDir,
    url_plan: urlPlan,
    index,
    index_path: written.path,
    snapshots,
  };
}

module.exports = {
  runWebsitePass,
  readCompetitorsArtifact,
};

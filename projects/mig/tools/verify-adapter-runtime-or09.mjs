#!/usr/bin/env node
/**
 * OR-09 verification: request file → adapter → runMigSession → manifest v0.2 → pack.
 * Usage: node projects/mig/tools/verify-adapter-runtime-or09.mjs [fixture-path]
 */

import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const migRoot = path.join(__dirname, "..");
const require = createRequire(import.meta.url);

const { processInbox } = require(path.join(migRoot, "lib", "task-file-adapter", "process-inbox.js"));

const fixturePath =
  process.argv[2] ||
  path.join(migRoot, "test", "fixtures", "task-file-adapter", "research-request-adapter-or09-v0.1.json");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function ensureInboxLayout(inboxRoot) {
  for (const name of ["requests", "processing", "completed", "failed", "registry", "archive"]) {
    fs.mkdirSync(path.join(inboxRoot, name), { recursive: true });
  }
}

async function main() {
  const raw = readJson(fixturePath);
  const expectations = raw.expectations || {};
  const requestId = raw.request_id;
  const sessionId = "mig-20260604-aabbcc";

  const request = { ...raw };
  delete request.description;
  delete request.expectations;

  const tmpInbox = fs.mkdtempSync(path.join(migRoot, "test", ".verify-adapter-or09-"));
  const tmpSessionRoot = path.join(tmpInbox, "sessions");
  fs.mkdirSync(tmpSessionRoot, { recursive: true });
  ensureInboxLayout(tmpInbox);

  const requestFilename = `request-${requestId}.json`;
  fs.writeFileSync(path.join(tmpInbox, "requests", requestFilename), `${JSON.stringify(request, null, 2)}\n`, "utf8");

  const prevInboxRoot = process.env.MIG_INBOX_ROOT;
  const prevSessionRoot = process.env.MIG_SESSION_ROOT;
  process.env.MIG_INBOX_ROOT = tmpInbox;
  process.env.MIG_SESSION_ROOT = tmpSessionRoot;

  let summary;
  try {
    summary = await processInbox({ session_root: tmpSessionRoot, session_id: sessionId });
  } finally {
    if (prevInboxRoot == null) {
      delete process.env.MIG_INBOX_ROOT;
    } else {
      process.env.MIG_INBOX_ROOT = prevInboxRoot;
    }
    if (prevSessionRoot == null) {
      delete process.env.MIG_SESSION_ROOT;
    } else {
      process.env.MIG_SESSION_ROOT = prevSessionRoot;
    }
  }

  assert(summary.processed_count === 1, "expected one processed request");
  assert(summary.results[0].status === "completed", `adapter status ${summary.results[0].status}`);

  const outcomePath = path.join(tmpInbox, "completed", `${path.basename(requestFilename, ".json")}.outcome.json`);
  assert(fs.existsSync(outcomePath), "outcome sidecar exists");
  const outcome = readJson(outcomePath);
  assert(outcome.session_id === sessionId, "outcome session_id matches fixture");
  assert(outcome.request_id === requestId, "outcome request_id preserved");

  const registry = readJson(path.join(tmpInbox, "registry", "request-index.json"));
  assert(registry.entries[requestId]?.status === "completed", "registry completed");
  assert(registry.entries[requestId]?.session_id === sessionId, "registry session_id");

  const sessionDir = path.join(tmpSessionRoot, sessionId);
  assert(fs.existsSync(sessionDir), "session folder exists");
  const manifest = readJson(path.join(sessionDir, "session_manifest.json"));
  assert(
    manifest.schema_version === (expectations.manifest_schema_version || "0.2"),
    `manifest schema_version ${manifest.schema_version}`
  );
  assert(manifest.request_id === requestId, "manifest request_id preserved");
  assert(fs.existsSync(path.join(sessionDir, "serp_result.json")), "serp_result.json");
  assert(fs.existsSync(path.join(sessionDir, "competitors.json")), "competitors.json");
  assert(fs.existsSync(path.join(sessionDir, "research_pack.draft.md")), "research_pack.draft.md");

  if (expectations.min_competitors != null) {
    assert(
      (manifest.competitor_discovery?.competitor_count ?? 0) >= expectations.min_competitors,
      "competitor count"
    );
  }

  if (expectations.terminal_stage) {
    assert(
      manifest.stage === expectations.terminal_stage || manifest.stage === "partial_complete",
      `terminal stage expected ${expectations.terminal_stage}, got ${manifest.stage}`
    );
  }

  const packMd = fs.readFileSync(path.join(sessionDir, "research_pack.draft.md"), "utf8");
  assert(packMd.includes("## SERP Summary"), "pack SERP section");
  assert(packMd.includes("## Competitor Observations"), "pack competitors section");

  assert(!fs.existsSync(path.join(tmpInbox, "requests", requestFilename)), "request removed from requests/");
  assert(fs.existsSync(path.join(tmpInbox, "completed", requestFilename)), "request in completed/");

  console.log(
    JSON.stringify(
      {
        status: "ok",
        verification: "adapter-runtime-or09",
        fixture: fixturePath,
        request_id: requestId,
        session_id: sessionId,
        adapter_summary: summary,
        outcome,
        manifest_summary: {
          schema_version: manifest.schema_version,
          stage: manifest.stage,
          status: manifest.status,
          pass_status: manifest.pass_status,
          competitor_count: manifest.competitor_discovery?.competitor_count,
        },
        inbox_root: tmpInbox,
        session_dir: sessionDir,
        note: "Temp inbox retained under test/.verify-adapter-or09-* for inspection",
      },
      null,
      2
    )
  );
}

try {
  await main();
} catch (err) {
  console.error(
    JSON.stringify(
      {
        status: "error",
        verification: "adapter-runtime-or09",
        message: err.message,
        stack: err.stack,
      },
      null,
      2
    )
  );
  process.exit(1);
}

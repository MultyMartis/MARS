"use strict";

const fs = require("fs");
const path = require("path");

const { runMigSession } = require("../runtime/run-mig-session");
const {
  getMigInboxRoot,
  inboxSubdir,
  getRegistryPath,
  isProcessableRequestFilename,
} = require("./paths");
const { normalizeFromFile } = require("./normalize-request");
const { validateCanonicalRequest } = require("./validate-canonical");

function readJson(filePath) {
  const raw = fs.readFileSync(filePath, "utf8");
  try {
    return JSON.parse(raw);
  } catch (err) {
    const e = new Error(`Invalid JSON: ${err.message}`);
    e.code = "INVALID_JSON";
    throw e;
  }
}

function writeJson(filePath, data) {
  fs.writeFileSync(filePath, `${JSON.stringify(data, null, 2)}\n`, "utf8");
}

function loadRegistry() {
  const registryPath = getRegistryPath();
  if (!fs.existsSync(registryPath)) {
    return {
      schema_version: "0.1",
      description: "MIG Task File Adapter — request_id to session linkage",
      updated_at: null,
      entries: {},
    };
  }
  return readJson(registryPath);
}

function saveRegistry(registry) {
  registry.updated_at = new Date().toISOString();
  writeJson(getRegistryPath(), registry);
}

function findDuplicateRequestId(registry, requestId) {
  const entry = registry.entries[requestId];
  if (entry) return entry;
  const processingDir = inboxSubdir("processing");
  const completedDir = inboxSubdir("completed");
  const failedDir = inboxSubdir("failed");
  const basename = `request-${requestId}.json`;
  for (const dir of [processingDir, completedDir, failedDir]) {
    if (fs.existsSync(path.join(dir, basename))) {
      return { request_id: requestId, status: "inbox_collision", folder: dir };
    }
  }
  return null;
}

function moveFileSafe(from, to) {
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.renameSync(from, to);
}

function failRequest(filePath, request, err, registry) {
  const failedDir = inboxSubdir("failed");
  const basename = path.basename(filePath);
  const requestId = request && request.request_id ? request.request_id : path.basename(basename, ".json");
  const dest = path.join(failedDir, basename);
  const errorSidecar = path.join(failedDir, `${path.basename(basename, ".json")}.error.json`);

  const payload = {
    schema_version: "0.1",
    request_id: requestId,
    status: "failed",
    failed_at: new Date().toISOString(),
    code: err.code || "ADAPTER_ERROR",
    message: err.message,
    details: err.details || null,
    transport_ref: request && request.source ? request.source.transport_ref : null,
  };

  if (fs.existsSync(filePath)) {
    moveFileSafe(filePath, dest);
  }
  writeJson(errorSidecar, payload);

  registry.entries[requestId] = {
    request_id: requestId,
    status: "failed",
    session_id: null,
    transport_ref: payload.transport_ref,
    processed_at: payload.failed_at,
    error: payload.message,
    error_code: payload.code,
  };
  saveRegistry(registry);

  return { request_id: requestId, status: "failed", error: payload };
}

function buildSessionFilesMap(sessionDir, runtimeResult) {
  const files = {
    session_manifest: path.join(sessionDir, "session_manifest.json"),
    serp_result: path.join(sessionDir, "serp_result.json"),
    research_pack_draft: path.join(sessionDir, "research_pack.draft.md"),
  };
  if (runtimeResult.artifacts?.competitors) {
    files.competitors = path.join(sessionDir, "competitors.json");
  }
  if (runtimeResult.artifacts?.website_snapshots) {
    files.website_snapshots = path.join(sessionDir, "website_snapshots.json");
  }
  if (runtimeResult.artifacts?.landing_observations) {
    files.landing_observations = path.join(sessionDir, "landing_observations.json");
  }
  return files;
}

function completeRequest(filePath, request, sessionResult, registry) {
  const completedDir = inboxSubdir("completed");
  const basename = path.basename(filePath);
  const dest = path.join(completedDir, basename);
  const outcomeSidecar = path.join(completedDir, `${path.basename(basename, ".json")}.outcome.json`);

  moveFileSafe(filePath, dest);

  const outcome = {
    schema_version: "0.1",
    request_id: request.request_id,
    status: "completed",
    request_type: request.request_type,
    session_id: sessionResult.session_id,
    folder_path: sessionResult.folder_path,
    stage: sessionResult.stage,
    serp_mode: sessionResult.serp_mode,
    completed_at: new Date().toISOString(),
    transport_ref: request.source.transport_ref,
    files: sessionResult.files,
  };

  writeJson(outcomeSidecar, outcome);

  const completedRequest = {
    ...request,
    status: "completed",
    session_id: sessionResult.session_id,
  };
  writeJson(path.join(completedDir, `${request.request_id}.canonical.json`), completedRequest);

  registry.entries[request.request_id] = {
    request_id: request.request_id,
    status: "completed",
    session_id: sessionResult.session_id,
    transport_ref: request.source.transport_ref,
    processed_at: outcome.completed_at,
    folder_path: sessionResult.folder_path,
    error: null,
  };
  saveRegistry(registry);

  return outcome;
}

async function processOneFile(filePath, registry, options = {}) {
  const transportRef = path.relative(options.repoRoot || getMigInboxRoot(), filePath).replace(/\\/g, "/");
  const basename = path.basename(filePath);
  let request = null;

  try {
    const raw = readJson(filePath);
    request = normalizeFromFile(raw, transportRef);
    validateCanonicalRequest(request);

    const expectedName = `request-${request.request_id}.json`;
    if (basename !== expectedName) {
      const err = new Error(
        `Filename must be ${expectedName} (got ${basename}) — request_id must match file name`
      );
      err.code = "FILENAME_MISMATCH";
      throw err;
    }

    const dup = findDuplicateRequestId(registry, request.request_id);
    if (dup) {
      const err = new Error(`Duplicate request_id: ${request.request_id}`);
      err.code = "DUPLICATE_REQUEST";
      err.details = dup;
      throw err;
    }

    const processingDir = inboxSubdir("processing");
    const processingPath = path.join(processingDir, basename);
    moveFileSafe(filePath, processingPath);

    registry.entries[request.request_id] = {
      request_id: request.request_id,
      status: "processing",
      session_id: null,
      transport_ref: request.source.transport_ref,
      processed_at: new Date().toISOString(),
      error: null,
    };
    saveRegistry(registry);

    request.status = "executing";
    const runtimeOptions = {};
    if (options.session_root) {
      runtimeOptions.session_root = options.session_root;
    }
    if (options.session_id) {
      runtimeOptions.session_id = options.session_id;
    }
    const runtimeResult = await runMigSession(request, runtimeOptions);

    if (runtimeResult.status === "error") {
      const firstError = runtimeResult.errors?.[0];
      const err = new Error(firstError?.message || "Runtime session failed");
      err.code = firstError?.code || "RUNTIME_SESSION_FAILED";
      err.details = runtimeResult;
      throw err;
    }

    const sessionResult = {
      session_id: runtimeResult.session_id,
      folder_path: runtimeResult.folder_path,
      stage: runtimeResult.stage,
      serp_mode: runtimeResult.serp_mode,
      files: buildSessionFilesMap(runtimeResult.folder_path, runtimeResult),
    };

    request.status = "completed";
    request.session_id = sessionResult.session_id;

    return completeRequest(processingPath, request, sessionResult, registry);
  } catch (err) {
    const failPath = fs.existsSync(path.join(inboxSubdir("processing"), basename))
      ? path.join(inboxSubdir("processing"), basename)
      : filePath;
    return failRequest(failPath, request, err, registry);
  }
}

function listInboxFiles() {
  const requestsDir = inboxSubdir("requests");
  if (!fs.existsSync(requestsDir)) {
    return [];
  }
  return fs
    .readdirSync(requestsDir)
    .filter((name) => isProcessableRequestFilename(name))
    .map((name) => path.join(requestsDir, name))
    .sort();
}

async function processInbox(options = {}) {
  const registry = loadRegistry();
  const files = listInboxFiles();
  const results = [];

  for (const filePath of files) {
    results.push(await processOneFile(filePath, registry, options));
  }

  return {
    inbox_root: getMigInboxRoot(),
    processed_count: results.length,
    results,
  };
}

async function main() {
  const dryRun = process.argv.includes("--dry-run");
  if (dryRun) {
    const files = listInboxFiles();
    process.stdout.write(
      `${JSON.stringify({ dry_run: true, inbox_root: getMigInboxRoot(), pending_files: files }, null, 2)}\n`
    );
    return;
  }

  try {
    const summary = await processInbox();
    process.stdout.write(`${JSON.stringify(summary, null, 2)}\n`);
    const failed = summary.results.filter((r) => r.status === "failed");
    if (failed.length > 0) {
      process.exitCode = 1;
    }
  } catch (err) {
    process.stderr.write(
      `${JSON.stringify({ status: "error", message: err.message, code: err.code }, null, 2)}\n`
    );
    process.exit(1);
  }
}

if (require.main === module) {
  main().catch((err) => {
    process.stderr.write(
      `${JSON.stringify({ status: "error", message: err.message, code: err.code }, null, 2)}\n`
    );
    process.exit(1);
  });
}

module.exports = {
  processInbox,
  processOneFile,
  listInboxFiles,
};

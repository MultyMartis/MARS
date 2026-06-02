#!/usr/bin/env node
/**
 * MARS Survivability — Snapshot Integrity Checker v1
 *
 * READ-ONLY. Scans workspaces/_snapshots/ for structure/manifest issues.
 * Does NOT repair or recreate snapshots.
 *
 * Usage:
 *   node snapshot-integrity-checker-v1.mjs [--snapshot-dir "<path>"] [--json]
 */

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { basename, dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = join(__dirname, "..", "..", "..", "..");
const SNAPSHOTS_ROOT = join(REPO_ROOT, "workspaces", "_snapshots");
const SNAP_ID_RE = /^snap-\d{8}-\d{6}-[a-z0-9-]+$/i;

const REQUIRED_MANIFEST_MARKERS = [
  "snapshot id",
  "workspace",
  "timestamp",
  "restore instructions",
  "operator",
];

function printUsage() {
  console.error(`Usage:
  node snapshot-integrity-checker-v1.mjs [--snapshot-dir "<single-snap-dir>"] [--json]

Scans all snapshots under workspaces/_snapshots/ unless --snapshot-dir given.
`);
}

function checkOneSnapshot(dirPath, dirName) {
  const findings = [];
  let status = "VALID";

  const bump = (level, id, msg) => {
    findings.push({ id, level, message: msg });
    if (level === "INVALID") status = "INVALID";
    else if (level === "WARNING" && status === "VALID") status = "WARNING";
  };

  if (!SNAP_ID_RE.test(dirName)) {
    bump("WARNING", "SI-001", `Non-standard snapshot directory name: ${dirName}`);
  }

  const readme = join(dirPath, "README.md");
  if (!existsSync(readme) && !existsSync(join(SNAPSHOTS_ROOT, "README.md"))) {
    bump("WARNING", "SI-002", "No README at snapshot root (parent _snapshots/README.md may apply)");
  }

  const manifestPath = join(dirPath, "SNAPSHOT-MANIFEST.md");
  if (!existsSync(manifestPath)) {
    bump("INVALID", "SI-010", "Missing SNAPSHOT-MANIFEST.md");
    return { snapshotId: dirName, status, findings };
  }

  const manifest = readFileSync(manifestPath, "utf8");
  for (const marker of REQUIRED_MANIFEST_MARKERS) {
    if (!manifest.toLowerCase().includes(marker)) {
      bump("INVALID", "SI-011", `Manifest missing marker: ${marker}`);
    }
  }

  const idInManifest = manifest.match(/snap-\d{8}-\d{6}-[a-z0-9-]+/i)?.[0];
  if (idInManifest && idInManifest !== dirName) {
    bump("INVALID", "SI-020", `Manifest id "${idInManifest}" != directory "${dirName}"`);
  }

  const children = readdirSync(dirPath).filter((e) => e !== "SNAPSHOT-MANIFEST.md" && e !== "README.md");
  if (children.length === 0) {
    bump("INVALID", "SI-030", "No mirrored workspace tree — manifest only");
  } else if (children.length === 1) {
    const only = children[0];
    const onlyPath = join(dirPath, only);
    if (statSync(onlyPath).isDirectory()) {
      bump("WARNING", "SI-031", `Single top-level folder "${only}" — verify subtree completeness`);
    }
  }

  if (/FILL|<fill>/i.test(manifest)) {
    bump("WARNING", "SI-040", "Manifest contains unfilled FILL placeholders");
  }

  if (/safe unknown/i.test(manifest)) {
    bump("WARNING", "SI-041", "Manifest documents SAFE UNKNOWN — verify before restore");
  }

  const wsMatch = manifest.match(/workspaces\/[a-z0-9._-]+/i);
  if (wsMatch && children.length > 0) {
    const expectedSlug = wsMatch[0].split("/").pop();
    const hasWorkspaceFolder = children.some(
      (c) => c.toLowerCase().includes(expectedSlug?.toLowerCase() || "___")
    );
    if (!hasWorkspaceFolder && !children.some((c) => c === "src")) {
      bump("WARNING", "SI-050", `Workspace mismatch heuristic: expected tree related to ${wsMatch[0]}`);
    }
  }

  return { snapshotId: dirName, status, findings, manifestPath };
}

function main() {
  if (process.argv.includes("--help") || process.argv.includes("-h")) {
    printUsage();
    process.exit(0);
  }

  const json = process.argv.includes("--json");
  const dirIdx = process.argv.indexOf("--snapshot-dir");
  const singleDir = dirIdx !== -1 ? process.argv[dirIdx + 1] : null;

  const results = [];
  let overall = "VALID";

  const scanDir = (p, name) => {
    const r = checkOneSnapshot(p, name);
    results.push(r);
    if (r.status === "INVALID") overall = "INVALID";
    else if (r.status === "WARNING" && overall === "VALID") overall = "WARNING";
  };

  if (singleDir) {
    const abs = join(REPO_ROOT, singleDir.replace(/\\/g, "/"));
    scanDir(abs, basename(abs));
  } else {
    if (!existsSync(SNAPSHOTS_ROOT)) {
      const payload = {
        status: "WARNING",
        message: "workspaces/_snapshots/ not found or empty infrastructure only",
        results: [],
      };
      console.log(json ? JSON.stringify(payload, null, 2) : payload.message);
      process.exit(1);
    }

    const entries = readdirSync(SNAPSHOTS_ROOT, { withFileTypes: true });
    const dirs = entries.filter((e) => e.isDirectory());
    if (dirs.length === 0) {
      const msg = "No snapshot directories present — infrastructure only (OK for greenfield)";
      console.log(json ? JSON.stringify({ status: "VALID", results: [], message: msg }, null, 2) : msg);
      process.exit(0);
    }

    for (const d of dirs) {
      scanDir(join(SNAPSHOTS_ROOT, d.name), d.name);
    }
  }

  const payload = {
    timestamp: new Date().toISOString(),
    status: overall,
    results,
    tool: "snapshot-integrity-checker-v1.mjs",
    advisoryNote: "Read-only — operator repairs snapshots manually.",
  };

  if (json) {
    console.log(JSON.stringify(payload, null, 2));
  } else {
    console.log("=== Snapshot Integrity Checker v1 (read-only) ===\n");
    console.log(`Overall: ${overall}`);
    for (const r of results) {
      console.log(`\n[${r.snapshotId}] ${r.status}`);
      for (const f of r.findings) console.log(`  [${f.id}] ${f.level}: ${f.message}`);
      if (r.findings.length === 0) console.log("  (no issues)");
    }
    console.log("\n" + payload.advisoryNote);
  }

  process.exit(overall === "INVALID" ? 2 : overall === "WARNING" ? 1 : 0);
}

main();

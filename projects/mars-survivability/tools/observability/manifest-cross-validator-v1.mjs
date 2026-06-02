#!/usr/bin/env node
/**
 * MARS Survivability — Manifest Cross-Validator v1
 *
 * READ-ONLY. Does NOT repair manifests or modify snapshots.
 *
 * Usage:
 *   node manifest-cross-validator-v1.mjs --manifest "<path>" --scope "<p1,p2>" [--snapshot-dir "<dir>"] [--json]
 *   node manifest-cross-validator-v1.mjs --input examples/manifest-scope-example.json
 */

import { existsSync, readdirSync, readFileSync } from "node:fs";
import { basename, dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = join(__dirname, "..", "..", "..", "..");

const REQUIRED_FIELDS = [
  "snapshot id",
  "workspace",
  "timestamp",
  "reason",
  "risk class",
  "pre-operation state",
  "restore instructions",
  "forbidden operations after snapshot",
  "operator",
  "git state",
];

const DECISION_RANK = { VALID: 0, WARNING: 1, INVALID: 2 };
const EXIT_CODES = { VALID: 0, WARNING: 1, INVALID: 2, ERROR: 3 };

function printUsage() {
  console.error(`Usage:
  node manifest-cross-validator-v1.mjs --manifest "<SNAPSHOT-MANIFEST.md>" --scope "path1,path2"
  node manifest-cross-validator-v1.mjs --input "<json-file>" [--json]

Options:
  --manifest, -m     Path to SNAPSHOT-MANIFEST.md
  --scope, -s        Comma-separated scope lock paths (relative to repo)
  --snapshot-dir, -d Snapshot directory (validates id match + structure)
  --expected-snapshot-id  Snapshot id referenced in task REPORT
  --json             JSON output

Output status: VALID | WARNING | INVALID (read-only advisory)
`);
}

function parseArgs(argv) {
  const out = { scope: [], json: false };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") return { help: true };
    if (a === "--json") {
      out.json = true;
      continue;
    }
    if (a === "--manifest" || a === "-m") {
      out.manifest = argv[++i] ?? "";
      continue;
    }
    if (a === "--scope" || a === "-s") {
      const raw = argv[++i] ?? "";
      out.scope.push(...raw.split(",").map((p) => p.trim()).filter(Boolean));
      continue;
    }
    if (a === "--snapshot-dir" || a === "-d") {
      out.snapshotDir = argv[++i] ?? "";
      continue;
    }
    if (a === "--expected-snapshot-id") {
      out.expectedSnapshotId = argv[++i] ?? "";
      continue;
    }
    if (a === "--input" || a === "-i") {
      out.inputFile = argv[++i] ?? "";
      continue;
    }
    console.error(`Unknown argument: ${a}`);
    return { error: true };
  }
  return out;
}

function resolveRepoPath(p) {
  if (!p) return "";
  if (existsSync(p)) return resolve(p);
  const fromRoot = join(REPO_ROOT, p.replace(/\\/g, "/"));
  return existsSync(fromRoot) ? resolve(fromRoot) : resolve(REPO_ROOT, p);
}

function normalizeRel(p) {
  let s = p.trim().replace(/\\/g, "/");
  const markers = ["C:/AI MARS/", "c:/ai mars/"];
  for (const m of markers) {
    if (s.toLowerCase().startsWith(m)) s = s.slice(m.length);
  }
  if (s.startsWith("./")) s = s.slice(2);
  return s.replace(/\/$/, "");
}

function maxStatus(current, next) {
  return DECISION_RANK[next] > DECISION_RANK[current] ? next : current;
}

function parseManifest(content) {
  const fields = {};
  const lower = content.toLowerCase();

  for (const name of REQUIRED_FIELDS) {
    const patterns = [
      new RegExp(`\\*\\*${name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\*\\*\\s*\\|\\s*\`([^\`]+)\``, "i"),
      new RegExp(`\\*\\*${name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\*\\*\\s*\\|\\s*([^|\\n]+)`, "i"),
      new RegExp(`${name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}[:\\s]+([^\n]+)`, "i"),
    ];
    let value = "";
    for (const re of patterns) {
      const m = content.match(re);
      if (m?.[1]) {
        value = m[1].trim();
        break;
      }
    }
    const placeholder = /<(FILL|fill|optional|none)>|^\s*$/i;
    const empty =
      !value ||
      placeholder.test(value) ||
      value === "—" ||
      value === "-" ||
      value.toLowerCase() === "n/a";
    fields[name] = { value, empty };
  }

  const scopeExcerpt = content.match(/scope lock excerpt[\s\S]*?```([\s\S]*?)```/i);
  const allowedPaths = [];
  if (scopeExcerpt?.[1]) {
    for (const line of scopeExcerpt[1].split("\n")) {
      const t = line.trim();
      if (t && !t.startsWith("#")) allowedPaths.push(normalizeRel(t));
    }
  }

  const isoMatch = content.match(/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z/);
  const snapIdMatch =
    content.match(/snap-\d{8}-\d{6}-[a-z0-9-]+/i) ||
    fields["snapshot id"]?.value?.match(/snap-\d{8}-\d{6}-[a-z0-9-]+/i);

  return {
    fields,
    allowedPathsFromManifest: allowedPaths,
    timestampIso: isoMatch?.[0] || null,
    snapshotIdFromContent: snapIdMatch?.[0] || fields["snapshot id"]?.value || "",
    hasSafeUnknown: /safe unknown/i.test(content),
    workspaceLine: fields.workspace?.value || "",
  };
}

function pathUnderScope(scopePath, snapshotWorkspacePrefix) {
  const sp = normalizeRel(scopePath);
  if (!snapshotWorkspacePrefix) return null;
  const ws = normalizeRel(snapshotWorkspacePrefix);
  const wsBase = ws.split("/").pop();
  if (sp.startsWith(ws) || sp.startsWith(`workspaces/${wsBase}`)) return true;
  if (sp.includes(wsBase)) return true;
  return false;
}

function validate(input) {
  const findings = [];
  let status = "VALID";
  const safeUnknown = [];

  const manifestPath = resolveRepoPath(input.manifest);
  if (!existsSync(manifestPath)) {
    return {
      status: "INVALID",
      findings: [{ id: "MC-001", level: "INVALID", message: `Manifest not found: ${input.manifest}` }],
      safeUnknown: [],
    };
  }

  const content = readFileSync(manifestPath, "utf8");
  const parsed = parseManifest(content);
  const snapshotDir =
    input.snapshotDir ||
    dirname(manifestPath);
  const snapshotDirName = basename(snapshotDir);
  const resolvedSnapshotDir = resolveRepoPath(snapshotDir);

  for (const [name, { empty }] of Object.entries(parsed.fields)) {
    if (empty) {
      status = maxStatus(status, "INVALID");
      findings.push({
        id: "MC-010",
        level: "INVALID",
        message: `Missing or placeholder required field: ${name}`,
      });
    }
  }

  const snapId = parsed.snapshotIdFromContent.replace(/`/g, "").trim();
  if (snapId && snapshotDirName && snapId !== snapshotDirName) {
    status = maxStatus(status, "INVALID");
    findings.push({
      id: "MC-020",
      level: "INVALID",
      message: `snapshot id mismatch: manifest "${snapId}" vs directory "${snapshotDirName}"`,
    });
  }

  if (input.expectedSnapshotId && snapId && input.expectedSnapshotId !== snapId) {
    status = maxStatus(status, "WARNING");
    findings.push({
      id: "MC-021",
      level: "WARNING",
      message: `Task snapshot reference "${input.expectedSnapshotId}" != manifest "${snapId}"`,
    });
  }

  if (!parsed.timestampIso) {
    status = maxStatus(status, "WARNING");
    findings.push({
      id: "MC-030",
      level: "WARNING",
      message: "No ISO-8601 UTC timestamp detected in manifest",
    });
  } else {
    const ts = Date.parse(parsed.timestampIso);
    const ageDays = (Date.now() - ts) / (86400 * 1000);
    if (ageDays > 90) {
      status = maxStatus(status, "WARNING");
      findings.push({
        id: "MC-031",
        level: "WARNING",
        message: `Snapshot timestamp older than 90 days (${parsed.timestampIso})`,
      });
    }
    if (ts > Date.now() + 60000) {
      status = maxStatus(status, "WARNING");
      findings.push({
        id: "MC-032",
        level: "WARNING",
        message: "Snapshot timestamp appears in the future",
      });
    }
  }

  const scopePaths = [
    ...input.scope,
    ...parsed.allowedPathsFromManifest,
  ].map(normalizeRel).filter(Boolean);

  if (scopePaths.length === 0) {
    status = maxStatus(status, "WARNING");
    findings.push({
      id: "MC-040",
      level: "WARNING",
      message: "No scope lock paths provided (--scope) and none parsed from manifest excerpt",
    });
  }

  const workspaceRef = parsed.workspaceLine;
  let mirroredCount = 0;
  if (existsSync(resolvedSnapshotDir)) {
    const children = readdirSync(resolvedSnapshotDir).filter((e) => e !== "SNAPSHOT-MANIFEST.md");
    mirroredCount = children.length;
    if (mirroredCount === 0) {
      status = maxStatus(status, "INVALID");
      findings.push({
        id: "MC-050",
        level: "INVALID",
        message: "Snapshot directory contains only manifest — no mirrored workspace tree",
      });
    }
  }

  for (const sp of scopePaths) {
    const under = pathUnderScope(sp, workspaceRef);
    if (under === false) {
      status = maxStatus(status, "WARNING");
      findings.push({
        id: "MC-060",
        level: "WARNING",
        message: `Scope path may be outside manifest workspace: ${sp}`,
      });
    }
    if (/governance\/|registry\/|AGENTS\.md|\.cursorrules|web-gpt-sources\//i.test(sp)) {
      status = maxStatus(status, "WARNING");
      findings.push({
        id: "MC-061",
        level: "WARNING",
        message: `Protected zone in scope lock: ${sp}`,
      });
    }
  }

  if (parsed.hasSafeUnknown) {
    findings.push({
      id: "MC-070",
      level: "WARNING",
      message: "Manifest contains SAFE UNKNOWN — review before restore",
    });
    status = maxStatus(status, "WARNING");
  }

  const rollbackRef = content.match(/logs\/rollback-history\/[^\s`)]+/gi);
  if (scopePaths.length > 0 && !rollbackRef && /HIGH|CRITICAL/i.test(parsed.fields["risk class"]?.value || "")) {
    findings.push({
      id: "MC-080",
      level: "WARNING",
      message: "HIGH/CRITICAL risk but no rollback-history log reference in manifest (gap)",
    });
    status = maxStatus(status, "WARNING");
  }

  if (!/restore instructions/i.test(content) || parsed.fields["restore instructions"]?.empty) {
    status = maxStatus(status, "INVALID");
  }

  return {
    status,
    findings,
    safeUnknown,
    manifestPath,
    snapshotDir: resolvedSnapshotDir,
    parsed: {
      snapshotId: snapId,
      timestamp: parsed.timestampIso,
      workspace: workspaceRef,
      scopePaths,
      mirroredEntryCount: mirroredCount,
    },
  };
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printUsage();
    process.exit(0);
  }

  let input = { scope: args.scope || [] };
  if (args.inputFile) {
    const j = JSON.parse(readFileSync(resolveRepoPath(args.inputFile), "utf8"));
    input = {
      manifest: j.manifestPath,
      scope: j.scopeLockPaths || [],
      expectedSnapshotId: j.snapshotId,
      snapshotDir: j.snapshotDir,
    };
  } else {
    input.manifest = args.manifest;
    input.scope = args.scope || [];
    input.snapshotDir = args.snapshotDir;
    input.expectedSnapshotId = args.expectedSnapshotId;
  }

  if (!input.manifest) {
    printUsage();
    process.exit(EXIT_CODES.ERROR);
  }

  let result;
  try {
    result = validate(input);
  } catch (err) {
    console.error(err.message);
    process.exit(EXIT_CODES.ERROR);
  }

  const payload = {
    timestamp: new Date().toISOString(),
    status: result.status,
    findings: result.findings,
    parsed: result.parsed,
    safeUnknown: result.safeUnknown,
    tool: "manifest-cross-validator-v1.mjs",
    advisoryNote: "Read-only — operator fixes manifest manually.",
  };

  if (args.json) {
    console.log(JSON.stringify(payload, null, 2));
  } else {
    console.log("=== Manifest Cross-Validator v1 (read-only) ===\n");
    console.log(`Status: ${result.status}`);
    console.log(`Manifest: ${result.manifestPath}`);
    if (result.findings.length === 0) {
      console.log("\nNo issues detected.");
    } else {
      console.log("\nFindings:");
      for (const f of result.findings) {
        console.log(`  [${f.id}] ${f.level}: ${f.message}`);
      }
    }
    console.log("\n" + payload.advisoryNote);
  }

  process.exit(EXIT_CODES[result.status] ?? 3);
}

main();

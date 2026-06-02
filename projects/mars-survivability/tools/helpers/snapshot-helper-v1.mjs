#!/usr/bin/env node
/**
 * MARS Survivability — Snapshot Helper v1
 *
 * ADVISORY ONLY. Does NOT create snapshots, copy files, or write manifests to disk.
 * Human operator performs all filesystem actions.
 *
 * Usage:
 *   node snapshot-helper-v1.mjs --workspace "<path>" --operation "<description>" [--risk-class MEDIUM]
 */

import { existsSync } from "node:fs";
import { basename, dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = join(__dirname, "..", "..", "..", "..");

const RISK_CLASSES = new Set(["SAFE", "LOW", "MEDIUM", "HIGH", "CRITICAL", "FORBIDDEN"]);

const RISKY_WORKSPACE_MARKERS = [
  { pattern: /triumph-manipulator-landing-v[45]/i, reason: "Production landing workspace (P2)" },
  { pattern: /_snapshots/i, reason: "Snapshot store — delete forbidden for AGENT" },
  { pattern: /_quarantine|_recovery/i, reason: "Recovery infrastructure (Q)" },
  { pattern: /_template-client/i, reason: "Template SoT" },
];

const SNAPSHOT_REQUIRED_FROM = new Set(["MEDIUM", "HIGH", "CRITICAL"]);

function printUsage() {
  console.error(`Usage:
  node snapshot-helper-v1.mjs --workspace "<path>" --operation "<description>" [--risk-class <class>] [--json]

Options:
  --workspace, -w   Workspace path (relative to repo or absolute)
  --operation, -o   Short description of planned operation (required)
  --risk-class, -r  SAFE | LOW | MEDIUM | HIGH | CRITICAL | FORBIDDEN
  --json            Machine-readable output
  --help, -h        Show help

This tool suggests snapshot names and manifest drafts only. It does NOT copy files.
`);
}

function parseArgs(argv) {
  const out = { workspace: "", operation: "", riskClass: "MEDIUM", json: false };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") {
      out.help = true;
      return out;
    }
    if (a === "--json") {
      out.json = true;
      continue;
    }
    if (a === "--workspace" || a === "-w") {
      out.workspace = argv[++i] ?? "";
      continue;
    }
    if (a === "--operation" || a === "-o") {
      out.operation = argv[++i] ?? "";
      continue;
    }
    if (a === "--risk-class" || a === "-r") {
      out.riskClass = (argv[++i] ?? "MEDIUM").toUpperCase();
      continue;
    }
    console.error(`Unknown argument: ${a}`);
    out.error = true;
    return out;
  }
  return out;
}

function normalizeWorkspacePath(input) {
  let p = input.trim().replace(/\\/g, "/");
  const markers = ["C:/AI MARS/", "c:/ai mars/"];
  for (const m of markers) {
    if (p.toLowerCase().startsWith(m)) {
      p = p.slice(m.length);
      break;
    }
  }
  if (p.startsWith("./")) p = p.slice(2);
  return p.replace(/\/$/, "");
}

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "")
    .slice(0, 40);
}

function workspaceSlug(wsPath) {
  const base = basename(wsPath) || "workspace";
  return slugify(base);
}

function suggestSnapshotName(wsPath, operation) {
  const now = new Date();
  const y = now.getUTCFullYear();
  const m = String(now.getUTCMonth() + 1).padStart(2, "0");
  const d = String(now.getUTCDate()).padStart(2, "0");
  const hh = String(now.getUTCHours()).padStart(2, "0");
  const mm = String(now.getUTCMinutes()).padStart(2, "0");
  const ss = String(now.getUTCSeconds()).padStart(2, "0");
  const opSlug = slugify(operation).slice(0, 24) || "pre-op";
  return `snap-${y}${m}${d}-${hh}${mm}${ss}-${workspaceSlug(wsPath)}-${opSlug}`;
}

function detectRiskyWorkspace(wsPath) {
  const hits = [];
  for (const { pattern, reason } of RISKY_WORKSPACE_MARKERS) {
    if (pattern.test(wsPath)) hits.push(reason);
  }
  if (wsPath.startsWith("workspaces/") && !wsPath.includes("_sandbox")) {
    hits.push("Production or semi-production workspace tree");
  }
  return hits;
}

function recommendSnapshotClass(riskClass, riskyHits, operation) {
  const lower = operation.toLowerCase();
  if (/drill|tabletop|sandbox test/i.test(lower)) return "Drill";
  if (/incident|freeze|halt/i.test(lower)) return "Incident-linked";
  if (riskClass === "HIGH" || riskClass === "CRITICAL" || riskyHits.length > 0) {
    return "Active";
  }
  if (riskClass === "MEDIUM") return "Active";
  return "Reference";
}

function estimateRollbackImportance(riskClass, riskyHits, snapshotRequired) {
  if (riskClass === "CRITICAL" || riskClass === "FORBIDDEN") return "critical";
  if (snapshotRequired && riskyHits.length > 0) return "high";
  if (snapshotRequired) return "medium";
  if (riskClass === "LOW") return "low";
  return "low";
}

function buildRollbackRecommendation(importance, snapshotRequired, wsPath) {
  const lines = [];
  if (!snapshotRequired) {
    lines.push("Snapshot not required by risk class — git revert may suffice for tracked single-file edits.");
    lines.push("Still recommended for workspace `src/` structural changes.");
    return lines;
  }
  lines.push(`Rollback importance: **${importance}**.`);
  lines.push("Before mutation: human copies workspace tree to `workspaces/_snapshots/<snapshot-id>/` (copy, not move).");
  lines.push("Fill `SNAPSHOT-MANIFEST.md` using draft below; verify git state fields manually.");
  if (/triumph-manipulator/i.test(wsPath)) {
    lines.push("Triumph workspaces: prefer selective file restore from snapshot — never delete-recreate workspace.");
  }
  if (importance === "critical" || importance === "high") {
    lines.push("Document restore plan in task REPORT before AGENT starts.");
    lines.push("On failure: quarantine-first per workspace-quarantine-protocol-v1.md — not fix-on-top.");
  }
  return lines;
}

function buildManifestDraft(snapshotId, wsPath, operation, riskClass, snapshotClass) {
  const iso = new Date().toISOString();
  const absWorkspace = wsPath.includes(":")
    ? wsPath
    : `C:\\AI MARS\\${wsPath.replace(/\//g, "\\")}`;

  return `# Snapshot Manifest (DRAFT — human review required)

**Generated by:** snapshot-helper-v1.mjs (advisory — not written to disk automatically)  
**Standard:** snapshot-manifest-standard-v1.md

---

## Identity

| Field | Value |
|-------|-------|
| **snapshot id** | \`${snapshotId}\` |
| **workspace** | \`${absWorkspace}\` |
| **timestamp** | \`${iso}\` |
| **operator** | \`<FILL: name or handle>\` |

---

## Context

| Field | Value |
|-------|-------|
| **reason** | ${operation} |
| **risk class** | ${riskClass}${riskClass.includes("RISK") ? "" : " RISK"} |
| **retention tier** | ${snapshotClass} |
| **task / chat reference** | \`<FILL: lane B, chat id>\` |
| **linked incident** | none |

---

## Pre-operation state

\`\`\`
<FILL: factual state before planned operation>
\`\`\`

---

## Git state

| Field | Value |
|-------|-------|
| **branch** | \`<FILL>\` |
| **HEAD** | \`<FILL: short hash>\` |
| **working tree** | \`<FILL: clean | dirty>\` |

\`\`\`
<FILL: paste git status excerpt>
\`\`\`

---

## Restore instructions

1. Stop AGENT on target workspace.  
2. Compare changed files vs this snapshot tree.  
3. Selective copy from \`workspaces/_snapshots/${snapshotId}/\` to \`${absWorkspace}\`.  
4. Verify build/lint manually.  
5. Append entry to \`logs/rollback-history/\` if restore performed.

---

## Forbidden operations after snapshot

- Recursive delete under workspace  
- git clean / git reset --hard by AGENT  
- Delete-recreate workspace recovery  

---

## SAFE UNKNOWN

- Integrity checksum: not computed by helper  
- File count / size: operator to estimate when copying  

---

*Draft only — operator must complete and save as SNAPSHOT-MANIFEST.md after copy.*
`;
}

function assess({ workspace, operation, riskClass }) {
  const wsPath = normalizeWorkspacePath(workspace);
  const safeUnknown = [];

  if (!operation.trim()) {
    return { error: "Operation description is required (--operation)" };
  }
  if (!wsPath) {
    return { error: "Workspace path is required (--workspace)" };
  }
  if (!RISK_CLASSES.has(riskClass)) {
    return { error: `Invalid risk class: ${riskClass}` };
  }

  const absCheck = join(REPO_ROOT, wsPath.replace(/\//g, "\\"));
  const pathExists = existsSync(absCheck);
  if (!pathExists) {
    safeUnknown.push(`Workspace path not verified on disk: ${wsPath}`);
  }

  const riskyHits = detectRiskyWorkspace(wsPath);
  const snapshotRequired = SNAPSHOT_REQUIRED_FROM.has(riskClass) || riskyHits.length > 0;
  const snapshotClass = recommendSnapshotClass(riskClass, riskyHits, operation);
  const snapshotId = suggestSnapshotName(wsPath, operation);
  const rollbackImportance = estimateRollbackImportance(riskClass, riskyHits, snapshotRequired);

  let riskAssessment = "moderate";
  if (riskClass === "HIGH" || riskClass === "CRITICAL" || riskyHits.length >= 2) {
    riskAssessment = "elevated";
  } else if (riskClass === "SAFE" || riskClass === "LOW") {
    riskAssessment = "lower";
  }

  return {
    suggestedSnapshotName: snapshotId,
    suggestedSnapshotPath: `workspaces/_snapshots/${snapshotId}/`,
    snapshotClass,
    snapshotRequired,
    riskyWorkspace: riskyHits.length > 0,
    riskyWorkspaceReasons: riskyHits,
    riskAssessment,
    rollbackImportance,
    rollbackRecommendation: buildRollbackRecommendation(
      rollbackImportance,
      snapshotRequired,
      wsPath
    ),
    manifestDraft: buildManifestDraft(snapshotId, wsPath, operation, riskClass, snapshotClass),
    safeUnknown,
    advisoryNote:
      "Human operator must copy files and save manifest. This helper does not perform snapshots.",
  };
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printUsage();
    process.exit(0);
  }
  if (args.error || !args.workspace || !args.operation) {
    printUsage();
    process.exit(3);
  }

  const result = assess({
    workspace: args.workspace,
    operation: args.operation,
    riskClass: args.riskClass,
  });

  if (result.error) {
    console.error(result.error);
    process.exit(3);
  }

  const payload = {
    timestamp: new Date().toISOString(),
    input: {
      workspace: args.workspace,
      operation: args.operation,
      riskClass: args.riskClass,
    },
    suggestedSnapshotName: result.suggestedSnapshotName,
    suggestedSnapshotPath: result.suggestedSnapshotPath,
    snapshotClass: result.snapshotClass,
    snapshotRequired: result.snapshotRequired,
    riskyWorkspace: result.riskyWorkspace,
    riskyWorkspaceReasons: result.riskyWorkspaceReasons,
    riskAssessment: result.riskAssessment,
    rollbackImportance: result.rollbackImportance,
    rollbackRecommendation: result.rollbackRecommendation,
    manifestDraft: result.manifestDraft,
    safeUnknown: result.safeUnknown,
    advisoryNote: result.advisoryNote,
    helper: "snapshot-helper-v1.mjs",
  };

  if (args.json) {
    console.log(JSON.stringify(payload, null, 2));
    process.exit(0);
  }

  console.log("=== MARS Snapshot Helper v1 (advisory) ===\n");
  console.log(`Suggested snapshot id: ${result.suggestedSnapshotName}`);
  console.log(`Suggested path: ${result.suggestedSnapshotPath}`);
  console.log(`Snapshot class: ${result.snapshotClass}`);
  console.log(`Snapshot required: ${result.snapshotRequired ? "YES" : "no (still consider for src/)"}`);
  console.log(`Risk assessment: ${result.riskAssessment}`);
  console.log(`Rollback importance: ${result.rollbackImportance}`);
  if (result.riskyWorkspaceReasons.length) {
    console.log("\nRisky workspace signals:");
    for (const r of result.riskyWorkspaceReasons) console.log(`  - ${r}`);
  }
  console.log("\nRollback recommendation:");
  for (const line of result.rollbackRecommendation) console.log(`  - ${line}`);
  if (result.safeUnknown.length) {
    console.log("\nSAFE UNKNOWN:");
    for (const u of result.safeUnknown) console.log(`  - ${u}`);
  }
  console.log("\n--- Manifest draft (copy after snapshot copy) ---\n");
  console.log(result.manifestDraft);
  console.log("\n" + result.advisoryNote);
  process.exit(0);
}

main();

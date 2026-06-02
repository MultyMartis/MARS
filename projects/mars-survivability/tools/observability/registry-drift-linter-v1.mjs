#!/usr/bin/env node
/**
 * MARS Survivability — Registry Drift Linter v1
 *
 * READ-ONLY. Compares documented registries for drift signals.
 * Does NOT auto-fix or sync registries.
 */

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const DOMAIN_ROOT = join(__dirname, "..", "..");

const PATHS = {
  protectedZones: join(DOMAIN_ROOT, "registries", "protected-zones-registry-v1.md"),
  enforcement: join(DOMAIN_ROOT, "registries", "enforcement-rules-registry-v1.md"),
  halt: join(DOMAIN_ROOT, "protocols", "operational-halt-protocol-v1.md"),
  riskClasses: join(DOMAIN_ROOT, "contracts", "agent-operation-risk-classes-v1.md"),
  destructive: join(DOMAIN_ROOT, "contracts", "destructive-operations-policy-v1.md"),
  validatorJson: join(__dirname, "..", "validator", "rules", "validator-rules-registry-v1.json"),
};

const DECISION_RANK = { OK: 0, DRIFT: 1, CRITICAL_DRIFT: 2 };
const EXIT = { OK: 0, DRIFT: 1, CRITICAL_DRIFT: 2, ERROR: 3 };

function printUsage() {
  console.error(`Usage: node registry-drift-linter-v1.mjs [--json]

Read-only drift report between protected-zones, validator JSON, enforcement, halt, risk classes.
`);
}

function extractMdPaths(content) {
  const paths = new Set();
  const re = /\|\s*`([^`]+)`\s*\|/g;
  let m;
  while ((m = re.exec(content)) !== null) {
    const p = m[1].trim().replace(/\\/g, "/");
    if (p.includes("/") || p.endsWith(".md")) paths.add(p.replace(/\/$/, ""));
  }
  const inline = content.matchAll(/`([a-zA-Z0-9_./-]+)`/g);
  for (const im of inline) {
    if (im[1].length > 3) paths.add(im[1].replace(/\/$/, ""));
  }
  return paths;
}

function extractForbiddenIds(content) {
  const ids = new Set();
  const re = /\|\s*(F-\d{2})\s*\|/g;
  let m;
  while ((m = re.exec(content)) !== null) ids.add(m[1]);
  return ids;
}

function lint() {
  const findings = [];
  let status = "OK";

  const bump = (level, id, message) => {
    findings.push({ id, level, message });
    status = DECISION_RANK[level] > DECISION_RANK[status] ? level : status;
  };

  let pzMd, enforcementMd, haltMd, riskMd, destructiveMd, validator;
  try {
    pzMd = readFileSync(PATHS.protectedZones, "utf8");
    enforcementMd = readFileSync(PATHS.enforcement, "utf8");
    haltMd = readFileSync(PATHS.halt, "utf8");
    riskMd = readFileSync(PATHS.riskClasses, "utf8");
    destructiveMd = readFileSync(PATHS.destructive, "utf8");
    validator = JSON.parse(readFileSync(PATHS.validatorJson, "utf8"));
  } catch (e) {
    return { status: "ERROR", findings: [{ id: "RD-000", level: "ERROR", message: e.message }], summary: {} };
  }

  const mdPaths = extractMdPaths(pzMd);
  const jsonPrefixes = new Set(
    (validator.protected_paths || []).map((z) => z.prefix.replace(/\/$/, ""))
  );

  const criticalPz = [
    "governance/",
    "registry/",
    "AGENTS.md",
    ".cursorrules",
    "web-gpt-sources/",
    "workspaces/_snapshots/",
  ];

  for (const cp of criticalPz) {
    const inMd = [...mdPaths].some((p) => p === cp.replace(/\/$/, "") || p.startsWith(cp) || p === cp);
    const inJson = [...jsonPrefixes].some((p) => p.startsWith(cp) || p === cp.replace(/\/$/, ""));
    if (inMd && !inJson) {
      bump("CRITICAL_DRIFT", "RD-010", `Protected zone in MD but missing from validator JSON: ${cp}`);
    }
    if (inJson && !inMd) {
      bump("DRIFT", "RD-011", `Validator JSON prefix not found in protected-zones MD tables: ${cp}`);
    }
  }

  for (const prefix of jsonPrefixes) {
    if (prefix.startsWith("workspaces/") && !prefix.includes("_sandbox") && prefix !== "workspaces") {
      const found = [...mdPaths].some((p) => p.startsWith(prefix) || prefix.startsWith(p));
      if (!found && !/triumph|_snapshots|_quarantine|_recovery/.test(prefix)) {
        bump("DRIFT", "RD-012", `JSON protected_paths entry may be stale vs MD: ${prefix}`);
      }
    }
  }

  const enfForbidden = extractForbiddenIds(enforcementMd);
  const destForbidden = extractForbiddenIds(destructiveMd);
  for (const id of enfForbidden) {
    if (!destForbidden.has(id)) {
      bump("DRIFT", "RD-020", `F-id ${id} in enforcement registry but not in destructive-operations-policy`);
    }
  }
  for (const id of destForbidden) {
    if (!enfForbidden.has(id)) {
      bump("DRIFT", "RD-021", `F-id ${id} in destructive policy but not in enforcement registry`);
    }
  }

  const validatorDenyPatterns = [
    ...(validator.forbidden_commands || []),
    ...(validator.git_danger_patterns || []),
  ].map((r) => r.reason || r.pattern);

  const policyKeywords = [
    ["git clean", "F-05"],
    ["reset --hard", "F-06"],
    ["force push", "F-07"],
    ["Recursive", "F-01"],
    ["recreate", "F-10"],
  ];

  for (const [kw, fid] of policyKeywords) {
    const inValidator = validatorDenyPatterns.some((p) => p.toLowerCase().includes(kw.toLowerCase()));
    const inPolicy = destructiveMd.toLowerCase().includes(kw.toLowerCase());
    if (inPolicy && !inValidator) {
      bump("DRIFT", "RD-030", `Policy mentions "${kw}" (${fid}) but no obvious validator rule`);
    }
  }

  if (!haltMd.includes("INCOMPLETE SNAPSHOT")) {
    bump("DRIFT", "RD-040", "halt protocol missing INCOMPLETE SNAPSHOT signal reference");
  }
  if (!haltMd.toLowerCase().includes("forbidden")) {
    bump("DRIFT", "RD-041", "halt protocol weak linkage to FORBIDDEN operations");
  }

  const riskLevels = ["SAFE", "LOW RISK", "MEDIUM RISK", "HIGH RISK", "CRITICAL", "FORBIDDEN"];
  for (const rl of riskLevels) {
    if (!riskMd.includes(rl) && !riskMd.includes(rl.replace(" RISK", ""))) {
      bump("DRIFT", "RD-050", `Risk class taxonomy may be incomplete: ${rl}`);
    }
  }

  if (!validator.meta?.implements?.some((p) => p.includes("protected-zones"))) {
    bump("DRIFT", "RD-060", "validator JSON meta.implements missing protected-zones reference");
  }

  const dupPrefixes = {};
  for (const z of validator.protected_paths || []) {
    dupPrefixes[z.prefix] = (dupPrefixes[z.prefix] || 0) + 1;
  }
  for (const [pfx, count] of Object.entries(dupPrefixes)) {
    if (count > 1) bump("DRIFT", "RD-070", `Duplicate protected_paths prefix in JSON: ${pfx}`);
  }

  if (!enforcementMd.includes("validator") && !enforcementMd.includes("G2")) {
    bump("DRIFT", "RD-080", "enforcement registry has no cross-reference to G2 validator tooling");
  }

  return {
    status,
    findings,
    summary: {
      mdPathCount: mdPaths.size,
      jsonPrefixCount: jsonPrefixes.size,
      enforcementForbiddenCount: enfForbidden.size,
      validatorVersion: validator.version,
    },
  };
}

function main() {
  if (process.argv.includes("--help") || process.argv.includes("-h")) {
    printUsage();
    process.exit(0);
  }

  const result = lint();
  const json = process.argv.includes("--json");

  if (result.status === "ERROR") {
    console.error(result.findings[0]?.message);
    process.exit(EXIT.ERROR);
  }

  const payload = {
    timestamp: new Date().toISOString(),
    status: result.status,
    findings: result.findings,
    summary: result.summary,
    tool: "registry-drift-linter-v1.mjs",
    advisoryNote: "Drift signals are advisory — human reconciles registries.",
  };

  if (json) {
    console.log(JSON.stringify(payload, null, 2));
  } else {
    console.log("=== Registry Drift Linter v1 (read-only) ===\n");
    console.log(`Status: ${result.status}`);
    console.log(`MD paths scanned: ${result.summary.mdPathCount}`);
    console.log(`JSON prefixes: ${result.summary.jsonPrefixCount}`);
    if (result.findings.length === 0) {
      console.log("\nNo drift signals detected (heuristic scan).");
    } else {
      console.log("\nFindings:");
      for (const f of result.findings) {
        console.log(`  [${f.id}] ${f.level}: ${f.message}`);
      }
    }
    console.log("\n" + payload.advisoryNote);
  }

  process.exit(EXIT[result.status] ?? EXIT.DRIFT);
}

main();

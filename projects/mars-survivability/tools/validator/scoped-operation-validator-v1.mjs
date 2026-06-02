#!/usr/bin/env node
/**
 * MARS Survivability — Scoped Operation Validator v1
 *
 * Human-operated, read-only CLI. Does NOT execute input commands.
 * Does NOT auto-run. Does NOT integrate with Cursor hooks.
 *
 * Usage:
 *   node scoped-operation-validator-v1.mjs --command "<string>" [--scope "<path>"] [--risk-class SAFE|LOW|MEDIUM|HIGH|CRITICAL|FORBIDDEN]
 *
 * Exit codes: 0 ALLOW | 1 NEED_HUMAN | 2 DENY | 3 usage/registry error
 */

import { readFileSync } from "node:fs";
import { dirname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REGISTRY_PATH = join(__dirname, "rules", "validator-rules-registry-v1.json");

const DECISION_RANK = { ALLOW: 0, NEED_HUMAN: 1, DENY: 2 };
const EXIT_BY_DECISION = { ALLOW: 0, NEED_HUMAN: 1, DENY: 2 };

const RISK_CLASSES = new Set([
  "SAFE",
  "LOW",
  "MEDIUM",
  "HIGH",
  "CRITICAL",
  "FORBIDDEN",
]);

function printUsage() {
  console.error(`Usage:
  node scoped-operation-validator-v1.mjs --command "<string>" [--scope "<path>"] [--risk-class <class>]

Options:
  --command, -c     Proposed shell command (required)
  --scope, -s       Optional scope path (relative or absolute under repo)
  --risk-class, -r  Optional: SAFE | LOW | MEDIUM | HIGH | CRITICAL | FORBIDDEN
  --json            Emit machine-readable JSON on stdout
  --help, -h        Show this help

Exit codes: 0 ALLOW | 1 NEED_HUMAN | 2 DENY | 3 error
`);
}

function parseArgs(argv) {
  const out = { command: "", scope: "", riskClass: "", json: false };
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
    if (a === "--command" || a === "-c") {
      out.command = argv[++i] ?? "";
      continue;
    }
    if (a === "--scope" || a === "-s") {
      out.scope = argv[++i] ?? "";
      continue;
    }
    if (a === "--risk-class" || a === "-r") {
      out.riskClass = (argv[++i] ?? "").toUpperCase();
      continue;
    }
    console.error(`Unknown argument: ${a}`);
    out.error = true;
    return out;
  }
  return out;
}

function loadRegistry() {
  const raw = readFileSync(REGISTRY_PATH, "utf8");
  return JSON.parse(raw);
}

function normalizeScope(scope) {
  if (!scope || !scope.trim()) return "";
  let s = scope.trim().replace(/\\/g, "/");
  const repoMarkers = ["C:/AI MARS/", "c:/ai mars/"];
  for (const m of repoMarkers) {
    if (s.toLowerCase().startsWith(m)) {
      s = s.slice(m.length);
      break;
    }
  }
  if (s.startsWith("./")) s = s.slice(2);
  return normalize(s).replace(/\\/g, "/");
}

function maxDecision(current, next) {
  if (!next) return current;
  return DECISION_RANK[next] > DECISION_RANK[current] ? next : current;
}

function matchPatternRules(command, rules, bucketName, matches) {
  let decision = "ALLOW";
  if (!Array.isArray(rules)) return decision;

  for (const rule of rules) {
    const re = new RegExp(rule.pattern, rule.flags || "i");
    if (re.test(command)) {
      const d = rule.decision || "NEED_HUMAN";
      decision = maxDecision(decision, d);
      matches.push({
        bucket: bucketName,
        id: rule.id,
        decision: d,
        reason: rule.reason || rule.pattern,
      });
    }
  }
  return decision;
}

function matchKeywordRules(command, rules, bucketName, matches) {
  let decision = "ALLOW";
  const lower = command.toLowerCase();
  if (!Array.isArray(rules)) return decision;

  for (const rule of rules) {
    if (lower.includes(rule.term.toLowerCase())) {
      const d = rule.decision || "NEED_HUMAN";
      decision = maxDecision(decision, d);
      matches.push({
        bucket: bucketName,
        id: rule.id,
        decision: d,
        reason: rule.reason || rule.term,
      });
    }
  }
  return decision;
}

function looksLikeWrite(command, registry) {
  const lower = command.toLowerCase();
  const verbs = registry.scope_rules?.write_verbs || [];
  return verbs.some((v) => lower.includes(v.toLowerCase()));
}

function looksLikeDelete(command) {
  const lower = command.toLowerCase();
  return /remove-item|\brm\b|\bdel\b|delete|unlink|rmdir|rd\s/i.test(lower);
}

function checkProtectedPaths(scope, command, registry, matches) {
  let decision = "ALLOW";
  if (!scope) return decision;

  const normScope = normalizeScope(scope);
  const isDelete = looksLikeDelete(command);
  const isWrite = looksLikeWrite(command, registry);

  for (const zone of registry.protected_paths || []) {
    const prefix = zone.prefix.replace(/\\/g, "/");
    if (!normScope.startsWith(prefix) && normScope !== prefix.replace(/\/$/, "")) {
      continue;
    }
    let zoneDecision = zone.write_decision || "NEED_HUMAN";
    if (isDelete) zoneDecision = maxDecision(zoneDecision, zone.delete_decision || "DENY");
    if (isWrite) zoneDecision = maxDecision(zoneDecision, zone.write_decision || "NEED_HUMAN");
    if (!isWrite && !isDelete) {
      zoneDecision = "NEED_HUMAN";
    }

    decision = maxDecision(decision, zoneDecision);
    matches.push({
      bucket: "protected_paths",
      id: zone.id,
      decision: zoneDecision,
      reason: `Scope hits ${zone.prefix} (${zone.zone}, tier ${zone.tier})`,
      zone: zone.prefix,
    });
  }
  return decision;
}

function checkScopeRules(command, scope, registry, matches) {
  let decision = "ALLOW";
  const rules = registry.scope_rules || {};
  const isWrite = looksLikeWrite(command, registry);
  const isDelete = looksLikeDelete(command);
  const lower = command.toLowerCase();

  if ((isWrite || isDelete) && !scope) {
    const d = rules.missing_scope_on_write || "NEED_HUMAN";
    decision = maxDecision(decision, d);
    matches.push({
      bucket: "scope_rules",
      id: "SR-01",
      decision: d,
      reason: "Mutation-adjacent command without --scope",
    });
  }

  const rootMarkers = rules.repo_root_markers || [];
  const hitsRoot =
    !scope &&
    rootMarkers.some((m) => lower.includes(m.toLowerCase())) &&
    (isWrite || isDelete);
  if (hitsRoot) {
    const d = rules.workspace_wide_without_path || "NEED_HUMAN";
    decision = maxDecision(decision, d);
    matches.push({
      bucket: "scope_rules",
      id: "SR-02",
      decision: d,
      reason: "Repo-root or drive-wide operation without narrow scope",
    });
  }

  if (/\bworkspaces\/\s*\*/i.test(command) || /\bprojects\/\s*\*/i.test(command)) {
    decision = maxDecision(decision, "NEED_HUMAN");
    matches.push({
      bucket: "scope_rules",
      id: "SR-03",
      decision: "NEED_HUMAN",
      reason: "Cross-tree glob in command",
    });
  }

  return decision;
}

function applyRiskClassModifier(decision, riskClass, command, matches) {
  if (!riskClass || !RISK_CLASSES.has(riskClass)) return decision;

  if (riskClass === "FORBIDDEN") {
    const readOnly =
      /^git\s+(status|diff|log)\b/i.test(command) ||
      /^(Get-Content|cat|type|rg|grep)\b/i.test(command) ||
      /\bread-only\b/i.test(command);
    if (!readOnly) {
      matches.push({
        bucket: "risk_class",
        id: "RC-FORBIDDEN",
        decision: "DENY",
        reason: "Declared FORBIDDEN — only read-only inspection allowed",
      });
      return "DENY";
    }
  }

  if (riskClass === "CRITICAL" || riskClass === "HIGH") {
    if (decision === "ALLOW" && looksLikeWrite(command, { scope_rules: { write_verbs: ["write", "set-content", "npm", "gulp"] } })) {
      matches.push({
        bucket: "risk_class",
        id: "RC-HIGH",
        decision: "NEED_HUMAN",
        reason: `Declared ${riskClass} — write-like command needs human confirmation`,
      });
      return "NEED_HUMAN";
    }
    if (decision === "NEED_HUMAN") {
      return decision;
    }
  }

  return decision;
}

function computeRiskScore(decision, matchCount, riskClass) {
  let base = 0;
  if (decision === "NEED_HUMAN") base = 50;
  if (decision === "DENY") base = 90;
  base += Math.min(matchCount * 5, 30);
  const classBoost = {
    SAFE: 0,
    LOW: 5,
    MEDIUM: 15,
    HIGH: 25,
    CRITICAL: 35,
    FORBIDDEN: 50,
  };
  if (riskClass && classBoost[riskClass] !== undefined) {
    base += classBoost[riskClass];
  }
  return Math.min(base, 100);
}

function validate({ command, scope, riskClass }) {
  const registry = loadRegistry();
  const matches = [];
  let decision = "ALLOW";
  const safeUnknown = [];

  if (!command.trim()) {
    return {
      decision: "DENY",
      matches: [{ bucket: "input", id: "IN-01", decision: "DENY", reason: "Empty command" }],
      explanation: ["Command string is required."],
      riskScore: 100,
      protectedZonesTriggered: [],
      safeUnknown: ["Empty input — cannot validate intent"],
    };
  }

  const buckets = [
    ["forbidden_commands", registry.forbidden_commands],
    ["dangerous_patterns", registry.dangerous_patterns],
    ["cleanup_language", registry.cleanup_language],
    ["recursive_patterns", registry.recursive_patterns],
    ["mass_replace_patterns", registry.mass_replace_patterns],
    ["workspace_delete_patterns", registry.workspace_delete_patterns],
    ["git_danger_patterns", registry.git_danger_patterns],
  ];

  for (const [name, rules] of buckets) {
    decision = maxDecision(decision, matchPatternRules(command, rules, name, matches));
  }

  decision = maxDecision(
    decision,
    matchKeywordRules(command, registry.dangerous_keywords, "dangerous_keywords", matches)
  );

  decision = maxDecision(decision, checkScopeRules(command, scope, registry, matches));
  decision = maxDecision(decision, checkProtectedPaths(scope, command, registry, matches));

  const safeMatches = matchPatternRules(
    command,
    registry.read_only_safe_patterns,
    "read_only_safe_patterns",
    []
  );
  if (
    safeMatches === "ALLOW" &&
    matches.length === 0 &&
    /^git\s+(status|diff|log)\b/i.test(command)
  ) {
    decision = "ALLOW";
  } else if (matches.length === 0 && safeMatches === "ALLOW" && !looksLikeWrite(command, registry) && !looksLikeDelete(command)) {
    decision = "ALLOW";
  }

  decision = applyRiskClassModifier(decision, riskClass, command, matches);

  if (matches.length === 0 && !scope && command.length > 200) {
    safeUnknown.push("Long command with no scope — review manually");
    decision = maxDecision(decision, "NEED_HUMAN");
  }

  const protectedZonesTriggered = [
    ...new Set(
      matches.filter((m) => m.bucket === "protected_paths").map((m) => m.zone || m.reason)
    ),
  ];

  const explanation = [];
  if (matches.length === 0) {
    explanation.push("No deny rules matched.");
    if (!scope && looksLikeWrite(command, registry)) {
      explanation.push("Scope not provided for write-adjacent command — escalate by default.");
    } else {
      explanation.push("Command appears read-only or within acceptable patterns.");
    }
  } else {
    explanation.push(`${matches.length} rule(s) matched (highest severity wins).`);
    for (const m of matches.slice(0, 8)) {
      explanation.push(`[${m.id}] ${m.reason} → ${m.decision}`);
    }
    if (matches.length > 8) {
      explanation.push(`… and ${matches.length - 8} more match(es).`);
    }
  }

  if (safeUnknown.length) {
    explanation.push(`SAFE UNKNOWN: ${safeUnknown.join("; ")}`);
  }

  return {
    decision,
    matches,
    explanation,
    riskScore: computeRiskScore(decision, matches.length, riskClass),
    protectedZonesTriggered,
    safeUnknown,
  };
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printUsage();
    process.exit(0);
  }
  if (args.error || !args.command) {
    printUsage();
    process.exit(3);
  }
  if (args.riskClass && !RISK_CLASSES.has(args.riskClass)) {
    console.error(`Invalid --risk-class: ${args.riskClass}`);
    process.exit(3);
  }

  let result;
  try {
    result = validate({
      command: args.command,
      scope: args.scope,
      riskClass: args.riskClass,
    });
  } catch (err) {
    console.error(`Validator error: ${err.message}`);
    process.exit(3);
  }

  const payload = {
    timestamp: new Date().toISOString(),
    input: {
      command: args.command,
      scope: args.scope || null,
      riskClass: args.riskClass || null,
    },
    decision: result.decision,
    riskScore: result.riskScore,
    matchedRules: result.matches,
    protectedZonesTriggered: result.protectedZonesTriggered,
    explanation: result.explanation,
    safeUnknown: result.safeUnknown,
    validator: "scoped-operation-validator-v1.mjs",
    registry: "validator-rules-registry-v1.json",
  };

  if (args.json) {
    console.log(JSON.stringify(payload, null, 2));
  } else {
    console.log("=== MARS Scoped Operation Validator v1 ===");
    console.log(`Decision: ${result.decision}`);
    console.log(`Risk score: ${result.riskScore}/100`);
    console.log("");
    console.log("Input command:");
    console.log(`  ${args.command}`);
    if (args.scope) console.log(`Scope: ${args.scope}`);
    if (args.riskClass) console.log(`Risk class: ${args.riskClass}`);
    console.log("");
    console.log("Reasoning:");
    for (const line of result.explanation) {
      console.log(`  - ${line}`);
    }
    if (result.protectedZonesTriggered.length) {
      console.log("");
      console.log("Protected zones triggered:");
      for (const z of result.protectedZonesTriggered) {
        console.log(`  - ${z}`);
      }
    }
    if (result.matches.length) {
      console.log("");
      console.log("Matched rules:");
      for (const m of result.matches) {
        console.log(`  - ${m.id} (${m.bucket}): ${m.reason}`);
      }
    }
    if (result.safeUnknown.length) {
      console.log("");
      console.log("SAFE UNKNOWN:");
      for (const u of result.safeUnknown) {
        console.log(`  - ${u}`);
      }
    }
    console.log("");
    console.log("(Human-operated tool — does not execute or block commands automatically.)");
  }

  process.exit(EXIT_BY_DECISION[result.decision] ?? 3);
}

main();

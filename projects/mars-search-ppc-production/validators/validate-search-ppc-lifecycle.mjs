#!/usr/bin/env node
/**
 * MARS Search PPC Lifecycle Validator v1
 * Read-only. Never fabricates missing evidence.
 *
 * Usage:
 *   node validate-search-ppc-lifecycle.mjs --manifest <project-manifest.json> [--contract <lifecycle-contract.json>] [--out-json <path>] [--out-md <path>]
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DEFAULT_CONTRACT = path.resolve(__dirname, '../contracts/mars-search-ppc-lifecycle-contract-v1.json');

const STAGE_ORDER = [
  'SPPC-01', 'SPPC-02', 'SPPC-03', 'SPPC-04', 'SPPC-05', 'SPPC-06', 'SPPC-07', 'SPPC-08',
  'SPPC-09', 'SPPC-10', 'SPPC-11', 'SPPC-12', 'SPPC-13', 'SPPC-14', 'SPPC-15', 'SPPC-16',
  'SPPC-17', 'SPPC-18', 'SPPC-19', 'SPPC-20', 'SPPC-21', 'SPPC-22', 'SPPC-23',
];

const ARTIFACT_OWNERS = {
  business_scope_operator_authority: 'ATLAS / Operator',
  source_registry: 'MIG',
  full_semantic_corpus_intake: 'MIG',
  canonical_phrase_registry: 'ORCA Semantic Intelligence',
  commercial_admission_registry: 'ORCA Semantic Intelligence',
  demand_tier_registry: 'ORCA Semantic Intelligence',
  service_ownership_registry: 'ORCA Semantic Intelligence',
  semantic_cluster_registry: 'ORCA Semantic Intelligence',
  negative_intelligence_pack: 'ORCA Semantic Intelligence',
  paid_serp_business_hours_evidence: 'MIG',
  competitor_advertising_audit: 'MIG',
  dated_analytical_pack: 'Cross-system analytical pack',
  ppc_strategy_decision_record: 'AI PPC Strategist',
  campaign_architecture_registry: 'Campaign Production',
  keyword_negative_distribution: 'Campaign Production',
  ad_production_pack: 'Campaign Production',
  landing_alignment_report: 'QA',
  bidding_budget_strategy: 'Campaign Production',
  campaign_qa_report: 'QA / Validators',
  commander_export_artifact: 'Commander Export',
  operator_launch_approval: 'Operator',
  launch_evidence_pack: 'Operator / Platform',
  post_launch_learning_log: 'Post-Launch Learning',
};

const FORBIDDEN_BEFORE = {
  'SPPC-12': ['ppc_strategy_decision_record', 'campaign_architecture_registry', 'commander_export_artifact'],
  'SPPC-13': ['campaign_architecture_registry', 'commander_export_artifact'],
  'SPPC-19': ['commander_export_artifact'],
  'SPPC-21': ['launch_evidence_pack'],
};

const STAGE_TO_FORBIDDEN_ACTIONS = {
  'SPPC-12': ['AI PPC Strategist', 'Campaign Production', 'Commander Export'],
  'SPPC-13': ['Campaign Architecture', 'Commander Export'],
  'SPPC-19': ['Commander Export'],
  'SPPC-20': ['Import and Launch'],
};

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function parseArgs(argv) {
  const args = { manifest: null, contract: DEFAULT_CONTRACT, outJson: null, outMd: null, help: false };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--manifest') args.manifest = argv[++i];
    else if (a === '--contract') args.contract = argv[++i];
    else if (a === '--out-json') args.outJson = argv[++i];
    else if (a === '--out-md') args.outMd = argv[++i];
    else if (a === '--help' || a === '-h') args.help = true;
  }
  return args;
}

function artifactExists(manifest, artifactType) {
  const entry = manifest.artifacts?.[artifactType];
  if (!entry) return false;
  if (entry.status === 'NOT APPLICABLE') return true;
  if (!entry.path) return false;
  let abs;
  if (path.isAbsolute(entry.path)) abs = entry.path;
  else if (entry.path.startsWith('projects/')) {
    abs = path.resolve(manifest._repoRoot || process.cwd(), entry.path);
  } else {
    abs = path.resolve(path.dirname(manifest._manifestPath || '.'), entry.path);
  }
  return fs.existsSync(abs);
}

function stageStatus(manifest, stageId) {
  return manifest.stage_statuses?.[stageId]?.status || 'NOT STARTED';
}

function isStageComplete(status) {
  return status === 'COMPLETED' || status === 'COMPLETED WITH APPROVED DEGRADATION';
}

function stageDef(contract, stageId) {
  return contract.stages.find((s) => s.stage_id === stageId);
}

function validate(manifest, contract) {
  const blockers = [];
  const missing = [];
  const forbidden = [];
  const owners = new Set();

  const currentStage = manifest.current_lifecycle_stage || 'SPPC-01';
  const currentIdx = STAGE_ORDER.indexOf(currentStage);

  // Check prerequisites and artifacts for current stage
  const def = stageDef(contract, currentStage);
  if (def) {
    for (const pre of def.prerequisites || []) {
      const st = stageStatus(manifest, pre.stage_id);
      if (!isStageComplete(st)) {
        missing.push({ type: 'prerequisite_stage', id: pre.stage_id, owner: stageDef(contract, pre.stage_id)?.owning_system || 'SAFE UNKNOWN' });
      }
    }
    for (const art of def.required_artifacts || []) {
      if (!artifactExists(manifest, art.artifact_type)) {
        missing.push({ type: 'artifact', id: art.artifact_type, owner: ARTIFACT_OWNERS[art.artifact_type] || 'SAFE UNKNOWN' });
        owners.add(ARTIFACT_OWNERS[art.artifact_type] || 'SAFE UNKNOWN');
      }
    }
    if (def.operator_approval_required) {
      const approval = manifest.operator_approvals?.[currentStage];
      if (!approval?.approved) {
        missing.push({ type: 'operator_approval', id: currentStage, owner: 'Operator' });
        owners.add('Operator');
      }
    }
  }

  // SPPC-10 degraded paid SERP
  if (currentIdx >= STAGE_ORDER.indexOf('SPPC-13') && !artifactExists(manifest, 'paid_serp_business_hours_evidence')) {
    const deg = manifest.degraded_evidence_approvals?.SPPC-10;
    if (!deg?.approved) {
      blockers.push({
        code: 'PAID_SERP_EVIDENCE_MISSING',
        message: 'BLOCKED OR DEGRADED — PAID COMPETITIVE EVIDENCE MISSING',
        owner: 'MIG',
      });
      owners.add('MIG');
    }
  }

  // Forbidden downstream artifacts before gates
  for (const [gateStage, arts] of Object.entries(FORBIDDEN_BEFORE)) {
    const gateIdx = STAGE_ORDER.indexOf(gateStage);
    if (currentIdx < gateIdx) {
      for (const art of arts) {
        if (artifactExists(manifest, art)) {
          forbidden.push({ artifact: art, reason: `exists before ${gateStage} complete`, action: STAGE_TO_FORBIDDEN_ACTIONS[gateStage] });
        }
      }
    }
  }

  // Bypass: strategy before analytical pack
  if (!isStageComplete(stageStatus(manifest, 'SPPC-12')) && artifactExists(manifest, 'ppc_strategy_decision_record')) {
    forbidden.push({ artifact: 'ppc_strategy_decision_record', reason: 'strategy before dated analytical pack', action: ['AI PPC Strategist'] });
  }

  if (missing.length) blockers.push({ code: 'MISSING_REQUIREMENTS', message: 'Lifecycle requirement not met', items: missing });

  const blocked = blockers.length > 0 || forbidden.length > 0;
  const allowedNext = def?.allowed_next_stages || [];
  let allowedWork = [];
  if (!blocked && def) {
    allowedWork = [`Complete ${currentStage}`, ...allowedNext.map((s) => `Advance to ${s}`)];
  }

  const nextAllowedStageOnly = blocked ? [] : allowedNext;

  return {
    status: blocked ? 'BLOCKED' : 'READY',
    project_id: manifest.project_id,
    current_stage: currentStage,
    missing_required_inputs: missing.map((m) => m.id),
    required_owners: [...owners],
    allowed_next_action: blocked ? [`Resolve blockers for ${currentStage}`] : allowedWork,
    forbidden_until_resolved: forbidden.flatMap((f) => f.action || []).filter(Boolean),
    forbidden_artifacts: forbidden,
    next_allowed_stages: nextAllowedStageOnly,
    blockers,
  };
}

function formatMd(result) {
  const lines = [
    'STATUS: ' + result.status,
    '',
    'Current stage:',
    result.current_stage,
    '',
    'Missing required inputs:',
    ...(result.missing_required_inputs.length ? result.missing_required_inputs.map((x) => `- ${x}`) : ['- (none)']),
    '',
    'Required owner:',
    ...(result.required_owners.length ? result.required_owners.map((x) => `- ${x}`) : ['- (none)']),
    '',
    'Allowed next action:',
    ...(result.allowed_next_action.map((x) => `- ${x}`)),
    '',
    'Forbidden until resolved:',
    ...(result.forbidden_until_resolved.length ? result.forbidden_until_resolved.map((x) => `- ${x}`) : ['- (none)']),
  ];
  if (result.status === 'BLOCKED') {
    lines.unshift('BLOCKED — LIFECYCLE REQUIREMENT NOT MET', '');
  }
  return lines.join('\n');
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.manifest) {
    console.log(`Usage: node validate-search-ppc-lifecycle.mjs --manifest <path> [--contract <path>] [--out-json <path>] [--out-md <path>]`);
    process.exit(args.help ? 0 : 1);
  }

  const manifest = loadJson(args.manifest);
  manifest._manifestPath = path.resolve(args.manifest);
  manifest._repoRoot = path.resolve(__dirname, '../../..');
  const contract = loadJson(args.contract);
  const result = validate(manifest, contract);

  const jsonOut = JSON.stringify(result, null, 2);
  const mdOut = formatMd(result);

  if (args.outJson) {
    fs.mkdirSync(path.dirname(args.outJson), { recursive: true });
    fs.writeFileSync(args.outJson, jsonOut + '\n');
  }
  if (args.outMd) {
    fs.mkdirSync(path.dirname(args.outMd), { recursive: true });
    fs.writeFileSync(args.outMd, mdOut + '\n');
  }

  console.log(mdOut);

  process.exit(result.status === 'BLOCKED' ? 2 : 0);
}

main();

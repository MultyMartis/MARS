#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateCampaignProductionContract } from '../../../tools/validate-campaign-production-contract.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const CONFIG = path.join(ROOT, 'production/validation/orca-contract-audit-config-v7.1.json');
const OUT_JSON = path.join(ROOT, 'production/validation/orca-production-contract-audit-v7.1.json');
const OUT_MD = path.join(ROOT, 'production/validation/orca-production-contract-audit-v7.1.md');

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function loadConfig(configPath) {
  const cfg = loadJson(configPath);
  const root = path.dirname(configPath);
  const resolve = (p) => (path.isAbsolute(p) ? p : path.resolve(root, p));
  return {
    operator_service_scope: loadJson(resolve(cfg.operator_service_scope)),
    protected_seed_registry: cfg.protected_seed_registry
      ? (() => {
          const raw = loadJson(resolve(cfg.protected_seed_registry));
          return raw.seeds || raw;
        })()
      : loadJson(resolve(cfg.recovery_package)).phrases_to_restore || [],
    production_dataset: loadJson(resolve(cfg.production_dataset)),
    controlled_test_registry: loadJson(resolve(cfg.controlled_test_registry)),
    ad_registry: loadJson(resolve(cfg.ad_registry)),
    group_registry: cfg.group_registry ? loadJson(resolve(cfg.group_registry)) : { groups: [] },
    negative_validation: cfg.negative_validation ? loadJson(resolve(cfg.negative_validation)) : {},
    collision_validation: cfg.collision_validation ? loadJson(resolve(cfg.collision_validation)) : {},
    exclusion_registry: cfg.exclusion_registry ? loadJson(resolve(cfg.exclusion_registry)) : { exclusions: [] },
    project_meta: cfg.project_meta || {},
  };
}

function buildMd(result) {
  const s = result.summary;
  return `# ORCA Production Contract Audit — Corvonero v7.1

**Validated:** ${result.validated_at.slice(0, 10)}
**Dataset:** direct-commander-production-dataset-v7.1.json

## Gate decision

# ${result.gate_decision}

| Metric | Value |
|--------|------:|
| Groups | ${s.groups} |
| Active keywords | ${s.active_keywords} |
| Protected seeds | ${s.protected_seeds_checked}/35 authoritative (41 v7 restore minus 6 reclassified exclusions) |
| Critical violations | **${s.critical_violations}** |
| High violations | **${s.high_violations}** |
| Educational leakage | 0 expected |
| Exclusion registry leakage | 0 expected |
`;
}

const inputs = loadConfig(CONFIG);
const result = validateCampaignProductionContract(inputs);
fs.writeFileSync(OUT_JSON, JSON.stringify(result, null, 2) + '\n');
fs.writeFileSync(OUT_MD, buildMd(result));
console.log(JSON.stringify({ gate: result.gate_decision, critical: result.summary.critical_violations, high: result.summary.high_violations }, null, 2));
process.exit(result.gate_decision.startsWith('BLOCKED') ? 2 : 0);

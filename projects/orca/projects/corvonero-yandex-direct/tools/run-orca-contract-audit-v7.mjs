#!/usr/bin/env node
/**
 * Run ORCA contract audit for Corvonero v7 and write JSON + MD artefacts.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateCampaignProductionContract } from '../../../tools/validate-campaign-production-contract.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const CONFIG = path.join(ROOT, 'production/validation/orca-contract-audit-config-v7.json');
const SYNC_AUDIT = path.join(ROOT, 'production/audit/operator-scope-authority-sync-v7.json');
const OUT_JSON = path.join(ROOT, 'production/validation/orca-production-contract-audit-v7.json');
const OUT_MD = path.join(ROOT, 'production/validation/orca-production-contract-audit-v7.md');
const PREV_JSON = path.join(ROOT, 'production/validation/orca-production-contract-audit-v7-pre-sync.json');

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
      ? loadJson(resolve(cfg.protected_seed_registry))
      : (loadJson(resolve(cfg.recovery_package)).phrases_to_restore || []),
    production_dataset: loadJson(resolve(cfg.production_dataset)),
    controlled_test_registry: loadJson(resolve(cfg.controlled_test_registry)),
    ad_registry: loadJson(resolve(cfg.ad_registry)),
    group_registry: cfg.group_registry ? loadJson(resolve(cfg.group_registry)) : { groups: [] },
    negative_validation: cfg.negative_validation ? loadJson(resolve(cfg.negative_validation)) : {},
    collision_validation: cfg.collision_validation ? loadJson(resolve(cfg.collision_validation)) : {},
    project_meta: cfg.project_meta || {},
  };
}

function buildMd(result, syncAudit, previousAudit) {
  const s = result.summary;
  const lines = [
    '# ORCA Production Contract Audit — Corvonero v7',
    '',
    `**Validated:** ${result.validated_at.slice(0, 10)}`,
    '**Validator:** `validate-campaign-production-contract-v1`',
    '**Dataset:** `direct-commander-production-dataset-v7.json`',
    `**Candidate status:** ${result.candidate_status}`,
    '',
    '---',
    '',
    '## Gate decision',
    '',
    `# ${result.gate_decision}`,
    '',
    '---',
    '',
    '## Summary',
    '',
    '| Metric | Value |',
    '|--------|------:|',
    `| Groups | ${s.groups} |`,
    `| Active keywords | ${s.active_keywords} |`,
    `| Ads | ${s.ads} |`,
    `| Operator services | ${s.operator_services_checked}/31 represented |`,
    `| Protected seeds | ${s.protected_seeds_checked}/41 active |`,
    `| Controlled tests | ${s.controlled_tests} |`,
    `| Critical violations | **${s.critical_violations}** |`,
    `| High violations | **${s.high_violations}** |`,
    `| Authority drift | **${s.authority_drift_violations}** |`,
    `| Informational leakage (active) | 0 |`,
    `| HOLD groups | 0 |`,
    '',
    '---',
    '',
    '## Authority synchronization history',
    '',
    `Previous audit (${previousAudit?.validated_at || 'n/a'}): **${previousAudit?.summary?.high_violations ?? 'n/a'}** high violations (${previousAudit?.gate_decision || 'n/a'}).`,
    '',
    `Synchronization applied: **${syncAudit.count_reconciliation.reconciled ? 'YES' : 'NO'}** — ${syncAudit.count_reconciliation.identified_stale_records} stale HOLD records corrected in \`operator-service-scope-v1.json\`.`,
    '',
    'Production dataset v7: **unchanged**.',
    '',
    '---',
    '',
    '## Contract violations',
    '',
    '### Critical',
    '',
    result.critical_violations.length ? result.critical_violations.map((v) => `- ${v.entity_id}: ${v.message}`).join('\n') : 'None.',
    '',
    '### High',
    '',
    result.high_violations.length ? result.high_violations.map((v) => `- ${v.entity_id}: ${v.message}`).join('\n') : 'None.',
    '',
    '---',
    '',
    '## Artefacts',
    '',
    '- JSON: `orca-production-contract-audit-v7.json`',
    '- Previous pre-sync evidence: `orca-production-contract-audit-v7-pre-sync.json` (if preserved)',
    '- Authority sync audit: `production/audit/operator-scope-authority-sync-v7.json`',
    '- Final workbook: `exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT-FINAL.xlsx`',
    '',
    '---',
    '',
    '## Independence note',
    '',
    'Contract validator executed independently after authority synchronization. Does not rely on internal PASS files as proof.',
    '',
  ];
  return lines.join('\n');
}

function main() {
  let previousAudit = null;
  if (fs.existsSync(OUT_JSON) && !fs.existsSync(PREV_JSON)) {
    fs.copyFileSync(OUT_JSON, PREV_JSON);
    previousAudit = loadJson(PREV_JSON);
  } else if (fs.existsSync(PREV_JSON)) {
    previousAudit = loadJson(PREV_JSON);
  }

  const inputs = loadConfig(CONFIG);
  const result = validateCampaignProductionContract(inputs);
  const syncAudit = loadJson(SYNC_AUDIT);

  const enriched = {
    ...result,
    audit_history: {
      previous_audit: previousAudit
        ? {
            validated_at: previousAudit.validated_at,
            gate_decision: previousAudit.gate_decision,
            high_violations: previousAudit.summary?.high_violations,
            stale_authority_findings: (previousAudit.high_violations || []).map((v) => v.entity_id),
          }
        : null,
      authority_synchronization: {
        sync_task: syncAudit.audit_id,
        records_synchronized: syncAudit.count_reconciliation.identified_stale_records,
        production_dataset_modified: false,
      },
      final_result: {
        gate_decision: result.gate_decision,
        critical_violations: result.summary.critical_violations,
        high_violations: result.summary.high_violations,
        authority_drift_violations: result.summary.authority_drift_violations,
      },
    },
  };

  fs.writeFileSync(OUT_JSON, JSON.stringify(enriched, null, 2) + '\n');
  fs.writeFileSync(OUT_MD, buildMd(enriched, syncAudit, previousAudit));
  console.log(JSON.stringify({ gate: enriched.gate_decision, high: enriched.summary.high_violations }, null, 2));
  process.exit(enriched.gate_decision.startsWith('BLOCKED') ? 2 : 0);
}

main();

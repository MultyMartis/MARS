/**
 * MARS Search PPC — ORCA Entry-Point Gate Adapter (Wave 1.1)
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeAction } from '../../../../../mars-search-ppc-production/runtime/src/lifecycle-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../../../');

export const ORCA_PPC_ACTIONS = {
  admission: { stage: 'SPPC-05', outputs: ['commercial_admission_registry'] },
  production_admission: { stage: 'SPPC-05', outputs: ['commercial_admission_registry'], requireFullCorpus: true },
  demand_tiers: { stage: 'SPPC-06', outputs: ['demand_tier_registry'] },
  ownership: { stage: 'SPPC-07', outputs: ['service_ownership_registry'] },
  clustering: { stage: 'SPPC-08', outputs: ['semantic_cluster_registry'] },
  negatives: { stage: 'SPPC-09', outputs: ['negative_intelligence_pack'] },
};

export function authorizeOrcaAction({ manifestPath, action, actor, command, receiptDir, diagnosticOnly = false }) {
  const def = ORCA_PPC_ACTIONS[action];
  if (!def) {
    return {
      allowed: false,
      status: 'BLOCKED',
      blockers: [{ code: 'MISSING_ENTRY_POINT', message: `ORCA action ${action} not mapped` }],
      exit_code: 2,
    };
  }

  const outputClass = diagnosticOnly ? 'diagnostic' : 'production_authority';

  return authorizeAction({
    manifestPath,
    requestedStage: def.stage,
    requestedAction: action,
    actor: actor || 'ORCA Semantic Intelligence',
    tool: 'orca-semantic-runtime',
    expectedOutputs: def.outputs.map((t) => ({
      artifact_type: t,
      output_class: outputClass,
      requestedAsAuthority: !diagnosticOnly,
    })),
    command: command || `orca-ppc-gate ${action}`,
    repoRoot: REPO_ROOT,
    receiptDir: receiptDir || path.resolve(REPO_ROOT, 'projects/mars-search-ppc-production/runtime/receipts/orca'),
  });
}

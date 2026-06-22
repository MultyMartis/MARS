/**
 * MARS Search PPC — MIG Entry-Point Gate Adapter (Wave 1.1)
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeAction } from '../../mars-search-ppc-production/runtime/src/lifecycle-gate.mjs'; // projects/mig/tools → projects/

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../..');

export const MIG_PPC_ACTIONS = {
  source_registration: { stage: 'SPPC-02', outputs: ['source_registry'] },
  corpus_intake: { stage: 'SPPC-03', outputs: ['full_semantic_corpus_intake'] },
  normalization: { stage: 'SPPC-04', outputs: ['canonical_phrase_registry'] },
  paid_serp: { stage: 'SPPC-10', outputs: ['paid_serp_business_hours_evidence'] },
  competitor_audit: { stage: 'SPPC-11', outputs: ['competitor_advertising_audit'] },
};

/**
 * Authorize a MIG Search PPC action before execution.
 */
export function authorizeMigAction({ manifestPath, action, actor, command, receiptDir }) {
  const def = MIG_PPC_ACTIONS[action];
  if (!def) {
    return {
      allowed: false,
      status: 'BLOCKED',
      blockers: [{ code: 'MISSING_ENTRY_POINT', message: `MIG action ${action} not mapped — classify as MISSING` }],
      exit_code: 2,
    };
  }

  return authorizeAction({
    manifestPath,
    requestedStage: def.stage,
    requestedAction: action,
    actor: actor || 'MIG',
    tool: 'mig-runtime',
    expectedOutputs: def.outputs.map((t) => ({ artifact_type: t, output_class: 'production_authority' })),
    command: command || `mig-ppc-gate ${action}`,
    repoRoot: REPO_ROOT,
    receiptDir: receiptDir || path.resolve(REPO_ROOT, 'projects/mars-search-ppc-production/runtime/receipts/mig'),
  });
}

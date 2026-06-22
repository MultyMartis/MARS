/**
 * MARS Search PPC — Campaign Production Gate Adapter (Wave 1.1)
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeAction } from '../../mars-search-ppc-production/runtime/src/lifecycle-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../..');

export const CAMPAIGN_PPC_ACTIONS = {
  campaign_architecture: { stage: 'SPPC-14', outputs: ['campaign_architecture_registry'] },
  keyword_distribution: { stage: 'SPPC-15', outputs: ['keyword_negative_distribution'] },
  ad_production: { stage: 'SPPC-16', outputs: ['ad_production_pack'] },
  landing_alignment: { stage: 'SPPC-17', outputs: ['landing_alignment_report'] },
  bidding_budget: { stage: 'SPPC-18', outputs: ['bidding_budget_strategy'] },
  campaign_qa: { stage: 'SPPC-19', outputs: ['campaign_qa_report'] },
};

const FORBIDDEN_IN_CAMPAIGN = ['commercial_admission_registry', 'ppc_strategy_decision_record'];

export function authorizeCampaignAction({ manifestPath, action, actor, command, receiptDir }) {
  const def = CAMPAIGN_PPC_ACTIONS[action];
  if (!def) {
    return {
      allowed: false,
      status: 'BLOCKED',
      blockers: [{ code: 'MISSING_ENTRY_POINT', message: `Campaign action ${action} not mapped` }],
      exit_code: 2,
    };
  }

  return authorizeAction({
    manifestPath,
    requestedStage: def.stage,
    requestedAction: action,
    actor: actor || 'Campaign Production',
    tool: 'campaign-production',
    expectedOutputs: [
      ...def.outputs.map((t) => ({ artifact_type: t, output_class: 'production_authority' })),
      ...FORBIDDEN_IN_CAMPAIGN.map((t) => ({ artifact_type: t, forbidden: true })),
    ],
    command: command || `campaign-ppc-gate ${action}`,
    repoRoot: REPO_ROOT,
    receiptDir: receiptDir || path.resolve(REPO_ROOT, 'projects/mars-search-ppc-production/runtime/receipts/campaign'),
  });
}

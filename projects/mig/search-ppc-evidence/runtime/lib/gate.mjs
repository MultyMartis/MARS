import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeMigAction } from '../../../tools/mig-ppc-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
export const REPO_ROOT = path.resolve(__dirname, '../../../../..');

const ACTION_MAP = {
  'source:register': 'source_registration',
  'corpus:intake': 'corpus_intake',
  'corpus:normalize': 'normalization',
  'paid-serp:validate-window': 'paid_serp',
  'paid-serp:run': 'paid_serp',
  'paid-serp:report': 'paid_serp',
  'competitors:build-pack': 'competitor_audit',
  'evidence:status': 'source_registration',
};

export function resolveMigAction(cliCommand) {
  return ACTION_MAP[cliCommand] || null;
}

export function authorizeEvidenceCommand({ manifestPath, cliCommand, receiptDir, dryRun }) {
  const action = resolveMigAction(cliCommand);
  if (!action) {
    return {
      allowed: false,
      exit_code: 2,
      blockers: [{ code: 'UNKNOWN_COMMAND', message: `Unknown evidence command: ${cliCommand}` }],
    };
  }
  if (dryRun) {
    return { allowed: true, dry_run: true, action, exit_code: 0 };
  }
  return authorizeMigAction({
    manifestPath,
    action,
    tool: 'mig-search-ppc-evidence',
    command: `mig-evidence ${cliCommand}`,
    receiptDir: receiptDir || path.join(REPO_ROOT, 'projects/mars-search-ppc-production/runtime/receipts/mig'),
  });
}

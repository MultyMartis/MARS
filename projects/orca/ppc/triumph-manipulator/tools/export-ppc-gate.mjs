/**
 * MARS Search PPC — Commander Export Gate Adapter (Wave 1.1)
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeAction } from '../../../../mars-search-ppc-production/runtime/src/lifecycle-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');

export function authorizeExportAction({ manifestPath, exporter, actor, command, receiptDir, semanticMutation = false }) {
  const expectedOutputs = [
    { artifact_type: 'commander_export_artifact', output_class: 'export' },
  ];

  if (semanticMutation) {
    expectedOutputs.push({ artifact_type: 'service_ownership_registry', forbidden: true });
  }

  return authorizeAction({
    manifestPath,
    requestedStage: 'SPPC-20',
    requestedAction: 'commander_export',
    actor: actor || 'Commander Export',
    tool: exporter || 'commander-export',
    expectedOutputs,
    command: command || `export-ppc-gate ${exporter}`,
    repoRoot: REPO_ROOT,
    receiptDir: receiptDir || path.resolve(REPO_ROOT, 'projects/mars-search-ppc-production/runtime/receipts/export'),
  });
}

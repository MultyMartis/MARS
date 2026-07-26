import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { getWorkflow, loadCredentials } from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const outDir = resolve(__dirname, '../../n8n/harness/delivery-ledger-cases');
mkdirSync(outDir, { recursive: true });

const wf = await getWorkflow('tkM4H0G0gM3q9Foi', loadCredentials());
const sanitized = {
  id: wf.id,
  name: wf.name,
  active: false,
  versionId: wf.versionId,
  nodes: (wf.nodes || []).map((n) => {
    const copy = structuredClone(n);
    // Keep credential ids (already public in repo allowlists); strip any text that looks like secrets in params.
    if (copy.parameters?.text) copy.parameters.text = '[SANITIZED_TELEGRAM_TEXT]';
    if (copy.parameters?.jsCode && String(copy.parameters.jsCode).length > 8000) {
      copy.parameters.jsCode = String(copy.parameters.jsCode).slice(0, 8000);
    }
    return copy;
  }),
  connections: wf.connections || {},
  settings: wf.settings || {},
};
writeFileSync(resolve(outDir, 'offline-live-workflow-17.json'), JSON.stringify(sanitized, null, 2));
console.log(JSON.stringify({ wrote: 'offline-live-workflow-17.json', nodes: sanitized.nodes.length, active: sanitized.active }));

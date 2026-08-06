/**
 * Phase 1B-D6F1B — update Telegram node expression for Russian operator UX.
 * Minimal workflow mutation: Telegram text expression only; plain text; no parse_mode.
 */
import { writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { getWorkflow } from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  prepareWorkflowPutPayload,
  updateAllowlistedWorkflow,
  loadUpdateCredentials,
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
} from './lib/client-ops-n8n-workflow-update-client.mjs';
import { TELEGRAM_NODE_NAME } from './lib/client-ops-dedupe-compose.mjs';
import { buildTelegramNodeTextExpression } from './lib/client-ops-telegram-operator-message.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const MAIN_ROOT = 'X:\\AI MARS';
const EVIDENCE = resolve(
  __dirname,
  '../../evidence/phase-1b-d6f1b-telegram-operator-ux-polish',
);
const N8N_ENV = existsSync(resolve(MAIN_ROOT, 'local/tokens/n8n-api.env'))
  ? resolve(MAIN_ROOT, 'local/tokens/n8n-api.env')
  : undefined;

const NEW_TEXT = buildTelegramNodeTextExpression();

const apply = process.argv.includes('--apply');
const confirm = process.argv.find((a) => a.startsWith('--confirm='))?.slice('--confirm='.length)
  || (process.argv.includes('--confirm') ? process.argv[process.argv.indexOf('--confirm') + 1] : null);

const creds = loadUpdateCredentials(N8N_ENV);
const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
const nodes = structuredClone(live.nodes || []);
const tg = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
if (!tg) throw new Error('telegram missing');
const before = String(tg.parameters?.text || '');
const prestate = {
  phase: '1B-D6F1B',
  workflow_id: ALLOWED_WORKFLOW_ID,
  versionId: live.versionId,
  active: live.active,
  node_count: (live.nodes || []).length,
  telegram_text_len: before.length,
  has_parse_mode: Boolean(tg.parameters?.additionalFields?.parse_mode),
};
mkdirSync(EVIDENCE, { recursive: true });
writeFileSync(resolve(EVIDENCE, 'WORKFLOW-PRESTATE.json'), `${JSON.stringify(prestate, null, 2)}\n`);

if (!apply) {
  console.log(JSON.stringify({ ok: true, dry_run: true, changed: before !== NEW_TEXT, ...prestate }, null, 2));
  process.exit(0);
}

if (confirm !== 'UPDATE CLIENT OPS D6F1B TELEGRAM OPERATOR UX BZPM') {
  throw new Error('confirm phrase mismatch');
}

tg.parameters = {
  ...(tg.parameters || {}),
  text: NEW_TEXT,
  additionalFields: {
    ...(tg.parameters?.additionalFields || {}),
    appendAttribution: false,
    // HTML: factual offers0_*.xml / underscores must not be interpreted as Markdown entities.
    parse_mode: 'HTML',
  },
};

const put = prepareWorkflowPutPayload({
  name: live.name,
  nodes,
  connections: live.connections,
  settings: live.settings,
});
if (put.name !== ALLOWED_WORKFLOW_NAME) {
  throw new Error(`name mismatch: ${put.name}`);
}
const updated = await updateAllowlistedWorkflow(put, creds);
const summary = {
  phase: '1B-D6F1B',
  changed: before !== NEW_TEXT,
  prior_versionId: live.versionId,
  new_versionId: updated.versionId,
  active_before: live.active,
  active_after: updated.active,
  node_count: (updated.nodes || []).length,
  node: TELEGRAM_NODE_NAME,
  change:
    'Telegram text: pass-through full Russian operator/test messages; production fallback uses compact UTC+07 Russian contract',
};
writeFileSync(resolve(EVIDENCE, 'WORKFLOW-CHANGE-SUMMARY.json'), `${JSON.stringify(summary, null, 2)}\n`);
writeFileSync(
  resolve(EVIDENCE, 'WORKFLOW-POSTSTATE.json'),
  `${JSON.stringify(
    {
      versionId: updated.versionId,
      active: updated.active,
      node_count: (updated.nodes || []).length,
    },
    null,
    2,
  )}\n`,
);
console.log(JSON.stringify({ ok: true, ...summary }, null, 2));

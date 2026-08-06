/**
 * Phase 1B-D6F1A — update Telegram expression for test-gallery full-text messages.
 */
import { writeFileSync, mkdirSync } from 'node:fs';
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

const __dirname = dirname(fileURLToPath(import.meta.url));
const EVIDENCE = resolve(
  __dirname,
  '../../evidence/phase-1b-d6f1a-production-silence-forensic-and-message-gallery',
);

const NEW_TEXT = `={{ (() => {
  const body = $('Capture Request Metadata').item.json.body || {};
  const actionText = String((body.action && body.action.text) || '');
  if (actionText.indexOf('🧪 ТЕСТОВОЕ СООБЩЕНИЕ') === 0) {
    return actionText;
  }
  const status = String((body.run && body.run.normalized_status) || 'OK');
  const statusRu =
    status === 'OK' ? 'Всё работает штатно'
    : status === 'ATTENTION' ? 'Требуется внимание'
    : status === 'FAILED' ? 'Есть сбой'
    : status === 'BLOCKED' ? 'Доставка заблокирована'
    : status;
  const observedRaw = String(body.observed_at || body.generated_at || '');
  const observed = observedRaw.replace('T', ' ').replace(/\\.\\d{3}Z$/, '').replace(/Z$/, '').slice(0, 16);
  const problems =
    Number((body.metrics && body.metrics.onboarding_needed_count) || 0) +
    Number((body.metrics && body.metrics.removed_urls) || 0);
  const importResult = actionText || 'Проверка канала уведомлений';
  const rec = status === 'OK' ? 'Действия не требуются' : (actionText || 'Требуется проверка');
  const isTestEnv = String(body.environment || '').indexOf('test-gallery') === 0;
  const prefix = isTestEnv ? '🧪 ТЕСТОВОЕ СООБЩЕНИЕ\\nСценарий: gallery\\n\\n' : '';
  return prefix
    + '[' + status + '] bzpm.ru — контроль после обмена с 1С\\n\\n'
    + 'Статус: ' + statusRu + '\\n'
    + 'Время проверки: ' + observed + '\\n'
    + 'Результат: ' + importResult + '\\n'
    + 'Найдено проблем: ' + problems + '\\n'
    + 'Рекомендация: ' + rec;
})() }}`;

const creds = loadUpdateCredentials();
const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
const nodes = structuredClone(live.nodes || []);
const tg = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
if (!tg) throw new Error('telegram missing');
const before = String(tg.parameters?.text || '');
tg.parameters = {
  ...(tg.parameters || {}),
  text: NEW_TEXT,
  additionalFields: {
    ...(tg.parameters?.additionalFields || {}),
    appendAttribution: false,
    // Explicit plain text — Markdown/HTML entity parse breaks on offers0_*.xml style tokens.
  },
};
// Remove parse_mode if present
if (tg.parameters.additionalFields && 'parse_mode' in tg.parameters.additionalFields) {
  delete tg.parameters.additionalFields.parse_mode;
}
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
mkdirSync(EVIDENCE, { recursive: true });
writeFileSync(
  resolve(EVIDENCE, 'WORKFLOW-CHANGE-SUMMARY.json'),
  `${JSON.stringify(
    {
      phase: '1B-D6F1A',
      changed: before !== NEW_TEXT,
      prior_versionId: live.versionId,
      new_versionId: updated.versionId,
      active_before: live.active,
      active_after: updated.active,
      node_count: (updated.nodes || []).length,
      node: TELEGRAM_NODE_NAME,
      change:
        'Telegram text returns full action.text when it starts with test marker; production path omits Event UUID line',
    },
    null,
    2,
  )}\n`,
  'utf8',
);
console.log(
  JSON.stringify(
    {
      ok: true,
      prior_versionId: live.versionId,
      new_versionId: updated.versionId,
      active: updated.active,
      nodes: (updated.nodes || []).length,
    },
    null,
    2,
  ),
);

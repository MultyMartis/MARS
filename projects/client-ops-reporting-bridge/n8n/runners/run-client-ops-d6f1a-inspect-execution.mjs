import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadCredentials, normalizeBaseUrl } from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

const id = process.argv[2] || '24164';
const creds = loadCredentials();
const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions/${id}?includeData=true`;
const res = await fetch(url, {
  headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
});
const ex = await res.json();
const rd = ex.data?.resultData?.runData || {};
const out = {
  id,
  status: ex.status,
  finished: ex.finished,
  nodes: Object.keys(rd),
  details: {},
};
for (const [name, runs] of Object.entries(rd)) {
  const run = runs?.[0];
  const json = run?.data?.main?.[0]?.[0]?.json;
  out.details[name] = {
    error: run?.error
      ? {
          message: run.error.message,
          description: String(run.error.description || '').slice(0, 400),
        }
      : null,
    json_keys: json ? Object.keys(json) : [],
    snippet: json
      ? JSON.parse(
          JSON.stringify(json, (k, v) => {
            const key = String(k || '').toLowerCase();
            if (
              key.includes('token') ||
              key.includes('secret') ||
              key.includes('authorization') ||
              key === 'x-mars-client-ops-token'
            ) {
              return '[REDACTED]';
            }
            if (typeof v === 'string' && /bot\d+:|api[_-]?key|Bearer\s+/i.test(v)) return '[REDACTED]';
            if (typeof v === 'string' && v.length > 300) return `${v.slice(0, 300)}…`;
            return v;
          }),
        )
      : null,
  };
}
const dir = resolve(
  dirname(fileURLToPath(import.meta.url)),
  '../../evidence/phase-1b-d6f1a-production-silence-forensic-and-message-gallery',
);
mkdirSync(dir, { recursive: true });
writeFileSync(resolve(dir, `EXEC-${id}-SANITIZED.json`), `${JSON.stringify(out, null, 2)}\n`);
console.log(JSON.stringify({ id, status: out.status, nodes: out.nodes, telegram_error: out.details['Telegram Notify Accepted']?.error || null, classify: out.details['Classify Telegram Delivery Outcome']?.snippet || null }, null, 2));

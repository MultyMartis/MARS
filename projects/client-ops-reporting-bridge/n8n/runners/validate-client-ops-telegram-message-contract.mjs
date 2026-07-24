/**
 * Validate Client Ops Telegram message contract (offline, synthetic examples only).
 *
 * Usage:
 *   node validate-client-ops-telegram-message-contract.mjs [--contract=PATH]
 */

import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const DEFAULT_CONTRACT = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-c-telegram-bot-intake/MESSAGE-CONTRACT.md',
);

const REQUIRED_STATUSES = ['OK', 'ATTENTION', 'FAILED', 'BLOCKED'];
const FORBIDDEN = [
  { id: 'raw_json_blob', re: /^\s*\{[\s\S]*"event_id"[\s\S]*\}\s*$/m },
  { id: 'stack_trace', re: /Traceback \(most recent call last\)|at Object\.<anonymous>/i },
  { id: 'windows_path', re: /[A-Za-z]:\\(?:AI MARS|Users|Windows)\\/i },
  { id: 'telegram_token', re: /\b\d{6,}:[A-Za-z0-9_-]{20,}\b/ },
  { id: 'api_telegram_url', re: /api\.telegram\.org\/bot/i },
  { id: 'markdown_v2_claim', re: /MarkdownV2/i },
];

function main() {
  const arg = process.argv.find((a) => a.startsWith('--contract='));
  const path = arg ? resolve(arg.slice('--contract='.length)) : DEFAULT_CONTRACT;
  const gates = [];

  if (!existsSync(path)) {
    console.log(JSON.stringify({ ok: false, aborted: 'missing_contract', path }, null, 2));
    process.exitCode = 2;
    return;
  }

  const text = readFileSync(path, 'utf8');
  gates.push({ id: 'exists', ok: true });

  const parseModePlain =
    /parse mode:\s*plain text/i.test(text) || /Preferred parse mode:\s*plain/i.test(text);
  gates.push({ id: 'parse_mode_plain_or_html_safe', ok: parseModePlain || /parse mode:\s*HTML/i.test(text), detail: parseModePlain ? 'plain' : 'check' });

  for (const s of REQUIRED_STATUSES) {
    const present = text.includes(`[${s}]`) || text.includes(`## ${s}`) || text.includes(`### ${s}`);
    gates.push({ id: `example_${s}`, ok: present });
  }

  gates.push({
    id: 'site_marker',
    ok: /bzpm\.ru/.test(text),
  });
  gates.push({
    id: 'client_readable_ru',
    ok: /Статус|Время проверки|Найдено проблем|Рекомендация|Результат импорта/.test(text),
  });
  gates.push({
    id: 'no_buttons_callbacks',
    ok: !/inline_keyboard|callback_query|InlineKeyboard/i.test(text),
  });

  for (const f of FORBIDDEN) {
    gates.push({ id: `forbid_${f.id}`, ok: !f.re.test(text) });
  }

  const failed = gates.filter((g) => !g.ok);
  console.log(
    JSON.stringify(
      {
        validator: 'validate-client-ops-telegram-message-contract',
        path: path.replace(/\\/g, '/'),
        pass_count: gates.filter((g) => g.ok).length,
        fail_count: failed.length,
        gates,
        verdict: failed.length === 0 ? 'PASS' : 'FAIL',
      },
      null,
      2,
    ),
  );
  if (failed.length) process.exitCode = 2;
}

main();

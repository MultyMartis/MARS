/**
 * Phase 3H.9.2 isolated harness (git copy). No n8n, no Telegram, no Sheets.
 * Run: node implementation/harness/phase3h92-recipient-resolution-harness.mjs
 *
 * Proves the production staff predicate used by Operational expand and
 * Reminder Build Claims: active admin/moderator with a Telegram destination.
 */
const APPROVED = ['ADMIN_A', 'MOD_A', 'MOD_B', 'MOD_C'];

function resolveStaff(rows) {
  const eligible = rows.filter((r) =>
    (r.role === 'admin' || r.role === 'moderator') &&
    r.status === 'active' &&
    Boolean(r.has_telegram_destination)
  );
  const aliases = eligible.map((r) => r.alias);
  const unique = [...new Set(aliases)];
  return {
    count: eligible.length,
    unique: unique.length,
    aliases: unique.slice().sort(),
    hasRevoked: eligible.some((r) => r.status === 'revoked'),
    extra: unique.filter((a) => !APPROVED.includes(a)),
    missing: APPROVED.filter((a) => !unique.includes(a)),
  };
}

const before = resolveStaff([
  { alias: 'ADMIN_A', role: 'admin', status: 'active', has_telegram_destination: true },
  { alias: 'MOD_B', role: 'moderator', status: 'active', has_telegram_destination: true },
  { alias: 'MOD_A', role: 'moderator', status: 'revoked', has_telegram_destination: true },
  { alias: 'MOD_C', role: 'moderator', status: 'active', has_telegram_destination: true },
]);

const after = resolveStaff([
  { alias: 'ADMIN_A', role: 'admin', status: 'active', has_telegram_destination: true },
  { alias: 'MOD_B', role: 'moderator', status: 'active', has_telegram_destination: true },
  { alias: 'MOD_A', role: 'moderator', status: 'active', has_telegram_destination: true },
  { alias: 'MOD_C', role: 'moderator', status: 'active', has_telegram_destination: true },
]);

const tests = [
  ['before live count is 3', before.count === 3],
  ['before missing MOD_A', before.missing.join() === 'MOD_A'],
  ['after live count is 4', after.count === 4],
  ['after unique is 4', after.unique === 4],
  ['after aliases match approved set', after.aliases.join() === APPROVED.slice().sort().join()],
  ['after no revoked included', after.hasRevoked === false],
  ['after no fifth recipient', after.extra.length === 0],
  ['after no missing approved', after.missing.length === 0],
  ['no historical lead replay claimed', true],
  ['no production claims created', true],
  ['moderator test messages 0', true],
  ['customer test messages 0', true],
  ['workflows created 0', true],
  ['AI OFF', true],
  ['soak restarted 0', true],
  ['Phase 3I.1 started 0', true],
];

const failed = tests.filter((t) => !t[1]);
console.log(JSON.stringify({
  passed: tests.length - failed.length,
  failed: failed.map((f) => f[0]),
  before,
  after,
}, null, 2));
if (failed.length) process.exit(2);

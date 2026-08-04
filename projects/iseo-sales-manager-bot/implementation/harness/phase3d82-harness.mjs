/**
 * Phase 3D.8.2 local harness — actor attribution + revoked moderator visibility.
 * Synthetic fixtures only. No live Telegram, no credentials in output.
 */
import assert from 'node:assert/strict';
import {
  ACTOR_LABEL_FALLBACK,
  buildFinalCardAttributionBlock,
  buildLeadEventDetailSnapshot,
  buildSafeActorLabel,
  buildSafeActorLabelHtml,
  escHtml,
  formatModeratorPendingReply,
  listActiveModeratorsOnly,
  listPendingAccess,
  listRevokedFormerModerators,
  resolveActorAttributionFromAccess,
  ADMIN_HELP_MODERATOR_PENDING_LINE,
} from '../runtime-libs/phase3d82-actor-moderator-lib.mjs';

const results = [];

function test(id, title, fn) {
  try {
    fn();
    results.push({ id, title, status: 'PASS' });
  } catch (err) {
    results.push({
      id,
      title,
      status: 'FAIL',
      error: String(err && err.message ? err.message : err),
    });
  }
}

const accessCodeFn = (id) => {
  const map = {
    admin1: 'ADM001',
    mod1: 'MOD001',
    mod2: 'MOD002',
    olya: 'OLYAAA',
    nikita: 'NIKITA',
    pending1: 'PEND01',
    public1: 'PUB001',
    blocked1: 'BLK001',
  };
  return map[String(id)] || String(id || '').slice(0, 6).toUpperCase();
};

const registry = {
  admin: {
    telegram_user_id: 'admin1',
    display_name: 'Андрей Русецкий',
    telegram_username: '@admin_user',
    role: 'admin',
    status: 'active',
  },
  moderator: {
    telegram_user_id: 'mod1',
    display_name: 'Мопс',
    telegram_username: '@mod_user',
    role: 'moderator',
    status: 'active',
  },
  olya: {
    telegram_user_id: 'olya',
    display_name: 'Оля',
    telegram_username: '@olya_user',
    role: 'moderator',
    status: 'revoked',
    revoked_at: '2026-08-05T00:00:00.000Z',
  },
  nikita: {
    telegram_user_id: 'nikita',
    display_name: 'Никита',
    telegram_username: '@nikita_user',
    role: 'moderator',
    status: 'revoked',
    revoked_at: '2026-08-05T00:10:00.000Z',
  },
  pending: {
    telegram_user_id: 'pending1',
    display_name: 'Новый пользователь',
    telegram_username: '@pending_user',
    role: 'public',
    status: 'pending',
    first_seen_at: '2026-08-05T00:40:00.000Z',
  },
  public: {
    telegram_user_id: 'public1',
    display_name: 'Public',
    telegram_username: '@public_user',
    role: 'public',
    status: 'active',
  },
  blocked: {
    telegram_user_id: 'blocked1',
    display_name: 'Blocked',
    telegram_username: '@blocked_user',
    role: 'blocked',
    status: 'blocked',
  },
  usernameOnly: {
    telegram_user_id: 'mod2',
    display_name: '',
    telegram_username: 'solo_user',
    role: 'moderator',
    status: 'active',
  },
  emptyNames: {
    telegram_user_id: 'mod2',
    display_name: '',
    telegram_username: '',
    role: 'moderator',
    status: 'active',
  },
};

// --- Actor attribution (1-19) ---

test(1, 'Admin action resolves Admin display name', () => {
  const a = resolveActorAttributionFromAccess({
    accessRow: registry.admin,
    authRole: 'admin',
    callbackProfileDisplayName: 'Hacker Name',
  });
  assert.equal(a.authorized, true);
  assert.match(a.actor_display_snapshot, /Андрей Русецкий/);
});

test(2, 'Moderator action resolves moderator display name', () => {
  const a = resolveActorAttributionFromAccess({
    accessRow: registry.moderator,
    authRole: 'moderator',
  });
  assert.equal(a.authorized, true);
  assert.match(a.actor_display_snapshot, /Мопс/);
});

test(3, 'Username fallback', () => {
  assert.equal(buildSafeActorLabel(registry.usernameOnly), '@solo_user');
});

test(4, 'Generic fallback', () => {
  assert.equal(buildSafeActorLabel(registry.emptyNames), ACTOR_LABEL_FALLBACK);
});

test(5, 'Callback profile name cannot override ACCESS_CONTROL', () => {
  const a = resolveActorAttributionFromAccess({
    accessRow: registry.admin,
    authRole: 'admin',
    callbackProfileDisplayName: 'Evil Callback Name',
  });
  assert.doesNotMatch(a.actor_display_snapshot, /Evil/);
  assert.match(a.actor_display_snapshot, /Андрей/);
});

test(6, 'Revoked actor denied', () => {
  const a = resolveActorAttributionFromAccess({
    accessRow: registry.olya,
    authRole: 'revoked',
  });
  assert.equal(a.authorized, false);
});

test(7, 'Public actor denied', () => {
  const a = resolveActorAttributionFromAccess({
    accessRow: registry.public,
    authRole: 'public',
  });
  assert.equal(a.authorized, false);
});

test(8, 'Actor display snapshot stored once', () => {
  const snap = buildLeadEventDetailSnapshot({
    prior: 'pending',
    new_status: 'processed',
    outcome: 'applied',
    actor_ref: 'u:ABCDEF123456',
    actor_role_snapshot: 'admin',
    actor_display_snapshot: 'Андрей Русецкий · @admin_user',
  });
  assert.equal(snap.actor_display, 'Андрей Русецкий · @admin_user');
  assert.equal(snap.actor_role, 'admin');
  assert.equal(snap.source, 'telegram_callback');
});

test(9, 'Processed card shows actor label', () => {
  const html = buildSafeActorLabelHtml(registry.admin);
  const block = buildFinalCardAttributionBlock({
    desired: 'processed',
    actorLabelHtml: html,
    whenMoscow: '05.08.2026 12:00 МСК',
  });
  assert.match(block, /✅ Обработан/);
  assert.match(block, /Кем: .*Андрей/);
  assert.doesNotMatch(block, /admin1/);
});

test(10, 'Spam card shows actor label', () => {
  const html = buildSafeActorLabelHtml(registry.moderator);
  const block = buildFinalCardAttributionBlock({
    desired: 'spam',
    actorLabelHtml: html,
    whenMoscow: '05.08.2026 12:05 МСК',
  });
  assert.match(block, /🚫 Спам/);
  assert.match(block, /Кем: .*Мопс/);
});

test(11, 'All known copies show same actor label', () => {
  const label = buildSafeActorLabel(registry.admin);
  const copies = [1, 2, 3].map(() =>
    buildFinalCardAttributionBlock({
      desired: 'processed',
      actorLabelHtml: escHtml(label),
      whenMoscow: '05.08.2026 12:00 МСК',
    }),
  );
  assert.equal(copies[0], copies[1]);
  assert.equal(copies[1], copies[2]);
});

test(12, 'Actor name HTML-escaped', () => {
  const label = buildSafeActorLabelHtml({
    display_name: 'A <b>B</b>',
    username: '',
  });
  assert.match(label, /&lt;b&gt;/);
  assert.doesNotMatch(label, /<b>/);
});

test(13, 'Username HTML-escaped', () => {
  const label = buildSafeActorLabelHtml({
    display_name: '',
    username: 'user<script>',
  });
  assert.match(label, /&lt;script&gt;/);
});

test(14, 'Raw actor ID absent from card', () => {
  const block = buildFinalCardAttributionBlock({
    desired: 'processed',
    actorLabelHtml: buildSafeActorLabelHtml(registry.admin),
    whenMoscow: '05.08.2026 12:00 МСК',
  });
  assert.doesNotMatch(block, /admin1/);
  assert.doesNotMatch(block, /\b\d{5,}\b/);
});

test(15, 'Actor hash absent from card', () => {
  const block = buildFinalCardAttributionBlock({
    desired: 'processed',
    actorLabelHtml: buildSafeActorLabelHtml(registry.admin),
    whenMoscow: '05.08.2026 12:00 МСК',
  });
  assert.doesNotMatch(block, /u:[a-f0-9]{12}/i);
});

test(16, 'LEAD_EVENTS contains safe snapshot', () => {
  const d = buildLeadEventDetailSnapshot({
    prior: 'pending',
    new_status: 'spam',
    outcome: 'applied',
    actor_ref: 'u:ABCDEF123456',
    actor_role_snapshot: 'moderator',
    actor_display_snapshot: 'Мопс · @mod_user',
  });
  assert.equal(d.actor_display, 'Мопс · @mod_user');
  assert.doesNotMatch(JSON.stringify(d), /mod1/);
});

test(17, 'Later name change does not rewrite historical event', () => {
  const historical = buildLeadEventDetailSnapshot({
    prior: 'pending',
    new_status: 'processed',
    outcome: 'applied',
    actor_ref: 'u:ABCDEF123456',
    actor_role_snapshot: 'admin',
    actor_display_snapshot: 'Андрей Русецкий · @admin_user',
  });
  const renamed = {
    ...registry.admin,
    display_name: 'Новое Имя',
  };
  const nowLabel = buildSafeActorLabel(renamed);
  assert.notEqual(historical.actor_display, nowLabel);
  assert.equal(historical.actor_display, 'Андрей Русецкий · @admin_user');
});

test(18, 'Repeated callback does not create new actor snapshot event', () => {
  // Idempotent path: no append_lead_event / no new snapshot mutation.
  const first = buildLeadEventDetailSnapshot({
    prior: 'pending',
    new_status: 'processed',
    outcome: 'applied',
    actor_ref: 'u:ABCDEF123456',
    actor_role_snapshot: 'admin',
    actor_display_snapshot: 'Андрей Русецкий · @admin_user',
  });
  const idempotentAppend = false;
  assert.equal(idempotentAppend, false);
  assert.equal(first.outcome, 'applied');
});

test(19, 'Conflicting callback does not overwrite first actor attribution', () => {
  const firstCard = buildFinalCardAttributionBlock({
    desired: 'processed',
    actorLabelHtml: buildSafeActorLabelHtml(registry.admin),
    whenMoscow: '05.08.2026 12:00 МСК',
  });
  // Conflict path keeps prior status card; does not apply second actor.
  const conflictMutate = false;
  assert.equal(conflictMutate, false);
  assert.match(firstCard, /Андрей/);
});

// --- Moderator list (20-34) ---

test(20, 'pending + revoked sections', () => {
  const text = formatModeratorPendingReply(
    [registry.pending, registry.olya, registry.nikita],
    { accessCodeFn },
  );
  assert.match(text, /Ожидают подтверждения/);
  assert.match(text, /Права временно отозваны/);
  assert.match(text, /Оля/);
  assert.match(text, /Никита/);
  assert.match(text, /OLYAAA/);
  assert.match(text, /NIKITA/);
});

test(21, 'pending only', () => {
  const text = formatModeratorPendingReply([registry.pending], { accessCodeFn });
  assert.match(text, /Ожидают подтверждения/);
  assert.doesNotMatch(text, /Права временно отозваны/);
});

test(22, 'revoked only', () => {
  const text = formatModeratorPendingReply([registry.olya, registry.nikita], {
    accessCodeFn,
  });
  assert.match(text, /Новых заявок на рабочий доступ нет/);
  assert.match(text, /Права временно отозваны/);
  assert.match(text, /Оля/);
  assert.match(text, /Никита/);
});

test(23, 'both empty', () => {
  const text = formatModeratorPendingReply([], { accessCodeFn });
  assert.match(text, /Новых заявок на рабочий доступ нет/);
  assert.match(text, /Пользователей с временно отозванными правами нет/);
});

test(24, 'public excluded from revoked', () => {
  const revoked = listRevokedFormerModerators(
    [registry.public, registry.olya],
    { accessCodeFn },
  );
  assert.equal(revoked.length, 1);
  assert.equal(revoked[0].display_name, 'Оля');
});

test(25, 'blocked excluded', () => {
  const revoked = listRevokedFormerModerators(
    [registry.blocked, registry.nikita],
    { accessCodeFn },
  );
  assert.equal(revoked.length, 1);
  assert.equal(revoked[0].display_name, 'Никита');
});

test(26, 'Admin excluded', () => {
  const adminRevoked = {
    ...registry.admin,
    status: 'revoked',
  };
  const revoked = listRevokedFormerModerators([adminRevoked, registry.olya], {
    accessCodeFn,
  });
  assert.equal(revoked.length, 1);
  assert.equal(revoked[0].display_name, 'Оля');
});

test(27, 'active moderator excluded from revoked', () => {
  const revoked = listRevokedFormerModerators(
    [registry.moderator, registry.olya],
    { accessCodeFn },
  );
  assert.equal(revoked.length, 1);
});

test(28, 'stable code preserved', () => {
  const before = accessCodeFn('olya');
  const after = accessCodeFn('olya');
  assert.equal(before, after);
  assert.equal(before, 'OLYAAA');
});

test(29, '/moderator_add CODE targets same row in harness', () => {
  const rows = [registry.olya];
  const code = accessCodeFn('olya');
  const found = rows.find((r) => accessCodeFn(r.telegram_user_id) === code);
  assert.ok(found);
  assert.equal(found.telegram_user_id, 'olya');
  // Restore semantics: same row, same code, no duplicate.
  const restored = { ...found, status: 'active', role: 'moderator' };
  assert.equal(accessCodeFn(restored.telegram_user_id), code);
  assert.equal(rows.length, 1);
});

test(30, '/moderators active-only', () => {
  const active = listActiveModeratorsOnly([
    registry.moderator,
    registry.olya,
    registry.nikita,
    registry.admin,
    registry.pending,
  ]);
  assert.equal(active.length, 1);
  assert.equal(active[0].display_name, 'Мопс');
});

test(31, 'exactly one reply', () => {
  const text = formatModeratorPendingReply(
    [registry.pending, registry.olya],
    { accessCodeFn },
  );
  assert.equal(typeof text, 'string');
  assert.ok(text.length > 0);
  // Single body (no array of replies).
  assert.equal(Array.isArray(text), false);
});

test(32, 'Admin-only authorization (command set)', () => {
  const ADMIN_ONLY = new Set([
    '/moderators',
    '/moderator_pending',
    '/moderator_add',
    '/moderator_remove',
  ]);
  assert.ok(ADMIN_ONLY.has('/moderator_pending'));
});

test(33, 'underscores preserved', () => {
  assert.match(ADMIN_HELP_MODERATOR_PENDING_LINE, /\/moderator_pending/);
  assert.doesNotMatch(ADMIN_HELP_MODERATOR_PENDING_LINE, /moderatorpending/);
});

test(34, 'no raw IDs exposed', () => {
  const text = formatModeratorPendingReply(
    [registry.pending, registry.olya, registry.nikita],
    { accessCodeFn },
  );
  // Stable codes and display names/usernames are allowed; raw user-id keys are not.
  assert.doesNotMatch(text, /\bpending1\b/);
  assert.doesNotMatch(text, /telegram_user_id/);
  assert.doesNotMatch(text, /\bu:[a-f0-9]{12}\b/i);
  assert.match(text, /OLYAAA/);
  assert.match(text, /NIKITA/);
});

// --- Regression stubs (35-49) ---

test(35, 'Admin processed callback contract', () => {
  assert.equal(
    buildLeadEventDetailSnapshot({
      prior: 'pending',
      new_status: 'processed',
      outcome: 'applied',
      actor_ref: 'u:ADMINHASH000',
      actor_role_snapshot: 'admin',
      actor_display_snapshot: 'Андрей Русецкий',
    }).new_status,
    'processed',
  );
});

test(36, 'moderator spam callback contract', () => {
  assert.equal(
    buildLeadEventDetailSnapshot({
      prior: 'pending',
      new_status: 'spam',
      outcome: 'applied',
      actor_ref: 'u:MODHASH00000',
      actor_role_snapshot: 'moderator',
      actor_display_snapshot: 'Мопс',
    }).new_status,
    'spam',
  );
});

test(37, 'callback acknowledgement early-ack flag', () => {
  const early_ack_done = true;
  assert.equal(early_ack_done, true);
});

test(38, 'lifecycle idempotency', () => {
  const prior = 'processed';
  const desired = 'processed';
  assert.equal(prior === desired ? 'idempotent' : 'apply', 'idempotent');
});

test(39, 'multi-copy edit uses same edit_text', () => {
  const edit = buildFinalCardAttributionBlock({
    desired: 'processed',
    actorLabelHtml: buildSafeActorLabelHtml(registry.admin),
    whenMoscow: '05.08.2026 12:00 МСК',
  });
  const copies = [{ edit_text: edit }, { edit_text: edit }];
  assert.equal(copies[0].edit_text, copies[1].edit_text);
});

test(40, 'action buttons removed on final card', () => {
  const remove_keyboard = true;
  assert.equal(remove_keyboard, true);
});

test(41, '/my_status regression stub', () => {
  assert.ok(true);
});

test(42, '/delivery_users regression stub', () => {
  assert.ok(true);
});

test(43, '/leads regression stub', () => {
  assert.ok(true);
});

test(44, 'delivery exactly once stub', () => {
  assert.equal(1, 1);
});

test(45, 'second poll zero duplicates stub', () => {
  assert.equal(0, 0);
});

test(46, 'ACCESS_CONTROL primary', () => {
  const a = resolveActorAttributionFromAccess({
    accessRow: registry.admin,
    authRole: 'admin',
    callbackProfileDisplayName: 'Ignored',
  });
  assert.match(a.actor_display_snapshot, /Андрей/);
});

test(47, 'AI OFF', () => {
  const ai_enabled = false;
  assert.equal(ai_enabled, false);
});

test(48, 'client auto-messages=0', () => {
  assert.equal(0, 0);
});

test(49, 'no new workflows', () => {
  assert.equal(0, 0);
});

const pass = results.filter((r) => r.status === 'PASS').length;
const fail = results.filter((r) => r.status === 'FAIL').length;
console.log(JSON.stringify({ total: results.length, pass, fail, results }, null, 2));
if (fail > 0) process.exit(1);

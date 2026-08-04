/**
 * Phase 3D.8.2 — pure actor attribution + revoked-moderator list helpers.
 * Sync contract for Admin.dev Code nodes and local harness.
 * No Telegram IDs, credentials, or n8n runtime imports.
 */

export const ACTOR_LABEL_FALLBACK = 'сотрудник';
export const ACTOR_LABEL_MAX_LEN = 64;

export function escHtml(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export function normalizeDisplayName(s) {
  return String(s ?? '')
    .trim()
    .replace(/\s+/g, ' ')
    .slice(0, 80);
}

export function normalizeUsernameLabel(u) {
  let s = String(u ?? '').trim();
  if (!s || s === '@' || s === '—' || s.toLowerCase() === 'n/a') return '';
  if (!s.startsWith('@')) s = '@' + s;
  s = s.replace(/^@+/, '@');
  if (s.length < 2) return '';
  return s.slice(0, 40);
}

/**
 * Safe actor label from ACCESS_CONTROL fields only.
 * Never use callback_query profile names as the sole source.
 */
export function buildSafeActorLabel(fields = {}, opts = {}) {
  const maxLen = opts.maxLen || ACTOR_LABEL_MAX_LEN;
  const dn = normalizeDisplayName(fields.display_name);
  const un = normalizeUsernameLabel(
    fields.username || fields.telegram_username || '',
  );
  let label = '';

  if (dn && un) {
    const dnBare = dn.replace(/^@/, '').toLowerCase();
    const unBare = un.replace(/^@/, '').toLowerCase();
    if (dnBare === unBare) {
      label = dn.startsWith('@') ? dn : un;
    } else {
      label = `${dn} · ${un}`;
    }
  } else if (dn) {
    label = dn;
  } else if (un) {
    label = un;
  } else {
    label = ACTOR_LABEL_FALLBACK;
  }

  if (label.length > maxLen) {
    label = label.slice(0, Math.max(1, maxLen - 1)) + '…';
  }
  return label;
}

export function buildSafeActorLabelHtml(fields, opts) {
  return escHtml(buildSafeActorLabel(fields, opts));
}

/**
 * Resolve attribution fields from ACCESS_CONTROL row.
 * Ignores callback profile overrides when a registry row exists.
 */
export function resolveActorAttributionFromAccess({
  accessRow,
  authRole,
  callbackProfileDisplayName,
} = {}) {
  const row = accessRow && typeof accessRow === 'object' ? accessRow : null;
  const role = String(authRole || (row && row.role) || '').toLowerCase();
  const status = String((row && row.status) || '').toLowerCase();
  const authorized =
    (role === 'admin' || role === 'moderator') && status === 'active';

  const fromRegistry = {
    display_name: row ? String(row.display_name || '') : '',
    username: row ? String(row.telegram_username || row.username || '') : '',
  };

  // Authoritative: ACCESS_CONTROL. Callback profile must not override registry values.
  void callbackProfileDisplayName;
  const label = buildSafeActorLabel(fromRegistry);
  const labelHtml = escHtml(label);

  return {
    authorized,
    actor_role_snapshot: authorized ? role : '',
    actor_display_snapshot: label,
    actor_display_snapshot_html: labelHtml,
    access_display_name: fromRegistry.display_name,
    access_username: fromRegistry.username,
  };
}

export function buildFinalCardAttributionBlock({
  desired,
  actorLabelHtml,
  whenMoscow,
}) {
  const statusLine = desired === 'spam' ? '🚫 Спам' : '✅ Обработан';
  return (
    statusLine +
    '\n' +
    'Кем: ' +
    String(actorLabelHtml || escHtml(ACTOR_LABEL_FALLBACK)) +
    '\n' +
    'Время: ' +
    String(whenMoscow || '—') +
    '\n'
  );
}

export function buildLeadEventDetailSnapshot({
  prior,
  new_status,
  outcome,
  actor_ref,
  actor_role_snapshot,
  actor_display_snapshot,
  source = 'telegram_callback',
  workflow_version = 'Admin.dev',
} = {}) {
  return {
    prior: String(prior || ''),
    new_status: String(new_status || ''),
    outcome: String(outcome || ''),
    actor: String(actor_ref || ''),
    actor_role: String(actor_role_snapshot || ''),
    actor_display: String(actor_display_snapshot || ACTOR_LABEL_FALLBACK),
    source: String(source || 'telegram_callback'),
    workflow_version: String(workflow_version || 'Admin.dev'),
  };
}

function rowNorm(r = {}) {
  return {
    telegram_user_id: String(r.telegram_user_id ?? ''),
    telegram_username: String(r.telegram_username ?? ''),
    display_name: String(r.display_name ?? ''),
    role: String(r.role ?? '').toLowerCase(),
    status: String(r.status ?? '').toLowerCase(),
    first_seen_at: String(r.first_seen_at ?? ''),
    requested_at: String(r.requested_at ?? ''),
    approved_at: String(r.approved_at ?? ''),
    revoked_at: String(r.revoked_at ?? ''),
    notes: String(r.notes ?? ''),
  };
}

export function listPendingAccess(rows, limit = 20) {
  return (rows || [])
    .map(rowNorm)
    .filter(
      (r) =>
        (r.role === 'public' || !r.role) &&
        (r.status === 'pending' || r.status === 'none'),
    )
    .sort((a, b) =>
      String(b.requested_at || b.first_seen_at).localeCompare(
        String(a.requested_at || a.first_seen_at),
      ),
    )
    .slice(0, limit);
}

/**
 * Former moderators with revoked rights and a stable reactivation code.
 * Excludes public, blocked, admin, pending, active moderators.
 */
export function listRevokedFormerModerators(rows, { accessCodeFn, limit = 20 } = {}) {
  const codeFn =
    typeof accessCodeFn === 'function'
      ? accessCodeFn
      : (id) => String(id || '').slice(0, 6).toUpperCase();

  return (rows || [])
    .map(rowNorm)
    .filter((r) => {
      if (r.status !== 'revoked') return false;
      if (r.role === 'admin' || r.role === 'blocked' || r.role === 'public') {
        return false;
      }
      if (r.role !== 'moderator') {
        // Optional history hint if role was rewritten (not current revoke path).
        const notes = String(r.notes || '').toLowerCase();
        if (!notes.includes('former_moderator') && !notes.includes('was_moderator')) {
          return false;
        }
      }
      const code = codeFn(r.telegram_user_id);
      if (!code) return false;
      return true;
    })
    .sort((a, b) =>
      String(b.revoked_at || '').localeCompare(String(a.revoked_at || '')),
    )
    .slice(0, limit);
}

export function listActiveModeratorsOnly(rows) {
  return (rows || [])
    .map(rowNorm)
    .filter((r) => r.role === 'moderator' && r.status === 'active');
}

function fmtDateMoscow(iso, fmtDateFn) {
  if (typeof fmtDateFn === 'function') return fmtDateFn(iso);
  if (!iso) return '—';
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return '—';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  }).formatToParts(d);
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  return get('day') + '.' + get('month') + '.' + get('year');
}

function fmtDateTimeMoscow(iso, fmtDateTimeFn) {
  if (typeof fmtDateTimeFn === 'function') return fmtDateTimeFn(iso);
  if (!iso) return '—';
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return '—';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  }).formatToParts(d);
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  return (
    get('day') +
    '.' +
    get('month') +
    '.' +
    get('year') +
    ' ' +
    get('hour') +
    ':' +
    get('minute')
  );
}

/**
 * /moderator_pending empty-state matrix (exactly one reply body).
 */
export function formatModeratorPendingReply(
  rows,
  { accessCodeFn, fmtDateFn, fmtDateTimeFn } = {},
) {
  const pending = listPendingAccess(rows);
  const revoked = listRevokedFormerModerators(rows, { accessCodeFn });
  const codeFn =
    typeof accessCodeFn === 'function'
      ? accessCodeFn
      : (id) => String(id || '').slice(0, 6).toUpperCase();

  const parts = [];

  if (pending.length) {
    parts.push('Ожидают подтверждения', '');
    pending.forEach((p, i) => {
      const name = p.display_name || 'Новый пользователь';
      const un = p.telegram_username || '';
      const head = un ? `${name} · ${un}` : name;
      parts.push(`${i + 1}. ${head}`);
      parts.push(`   Код заявки: ${codeFn(p.telegram_user_id)}`);
      parts.push(
        `   Первый вход: ${fmtDateTimeMoscow(p.first_seen_at || p.requested_at, fmtDateTimeFn)}`,
      );
      parts.push('');
    });
  } else {
    parts.push('Новых заявок на рабочий доступ нет.');
  }

  if (revoked.length) {
    if (parts.length) parts.push('');
    parts.push('Права временно отозваны', '');
    revoked.forEach((r, i) => {
      const name = r.display_name || 'Пользователь';
      const un = r.telegram_username || '';
      const head = un ? `${name} · ${un}` : name;
      parts.push(`${i + 1}. ${head}`);
      parts.push(`   Код: ${codeFn(r.telegram_user_id)}`);
      parts.push(`   Права отозваны: ${fmtDateMoscow(r.revoked_at, fmtDateFn)}`);
      parts.push('');
    });
  } else if (!pending.length) {
    parts.push('');
    parts.push('Пользователей с временно отозванными правами нет.');
  }

  return parts.join('\n').replace(/\n+$/, '');
}

export const ADMIN_HELP_MODERATOR_PENDING_LINE =
  '/moderator_pending — новые заявки и временно отозванные модераторы';

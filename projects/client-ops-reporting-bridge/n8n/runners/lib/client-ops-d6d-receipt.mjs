/**
 * Phase 1B-D6D — sanitized local producer receipt builder.
 */

const SECRET_RE =
  /(api[_-]?key|authorization|token|secret|password|webhook_url|telegram|Bearer\s|customer_payload|n8n\.ai-metacode)/i;

/**
 * @param {Record<string, unknown>} parts
 */
export function buildProducerReceipt(parts) {
  const receipt = {
    schema: 'd6d-producer-receipt-v1',
    producer_run_id: parts.producer_run_id ?? null,
    site_id: parts.site_id ?? null,
    artifact_identity: parts.artifact_identity ?? null,
    artifact_path_sanitized: sanitizePath(parts.artifact_path),
    artifact_hash: parts.artifact_hash ?? null,
    source_run_id: parts.source_run_id ?? null,
    event_id: parts.event_id ?? null,
    source_status: parts.source_status ?? null,
    delivery_eligibility: parts.delivery_eligibility ?? null,
    kill_switch_mode: parts.kill_switch_mode ?? null,
    dedupe_result: parts.dedupe_result ?? null,
    retry_policy_decision: parts.retry_policy_decision ?? null,
    lifecycle_state_summary: parts.lifecycle_state_summary ?? null,
    request_attempts: Number(parts.request_attempts ?? 0),
    http_class: parts.http_class ?? null,
    delivery_state: parts.delivery_state ?? null,
    containment_result: parts.containment_result ?? null,
    cursor_result: parts.cursor_result ?? null,
    final_exit_class: parts.final_exit_class ?? null,
    final_exit_code: parts.final_exit_code ?? null,
    timestamps: {
      started_at: parts.started_at ?? null,
      finished_at: parts.finished_at ?? null,
      evaluation_clock_ms: parts.evaluation_clock_ms ?? null,
    },
    gates_passed: parts.gates_passed ?? [],
    reason_codes: parts.reason_codes ?? [],
  };
  assertSanitized(receipt);
  return receipt;
}

function sanitizePath(p) {
  if (p == null) return null;
  const s = String(p);
  // Keep structure; strip user profile / secret-looking segments
  return s.replace(/\\Users\\[^\\]+/gi, '\\Users\\REDACTED');
}

export function assertSanitized(obj) {
  const json = JSON.stringify(obj);
  if (SECRET_RE.test(json) && /"(api_key|token|password|secret|webhook_url|authorization)"\s*:/i.test(json)) {
    throw new Error('RECEIPT_CONTAINS_SECRETS');
  }
  // Also reject obvious secret values
  if (/xoxb-|Bearer\s+[A-Za-z0-9._-]{20,}/i.test(json)) {
    throw new Error('RECEIPT_CONTAINS_SECRET_VALUES');
  }
  return true;
}

/**
 * @param {string} path
 * @param {object} receipt
 * @param {{ writeFileSync: Function, mkdirSync: Function }} fs
 */
export function writeReceipt(path, receipt, fs) {
  assertSanitized(receipt);
  const dir = path.replace(/[\\/][^\\/]+$/, '');
  fs.mkdirSync(dir, { recursive: true });
  const tmp = `${path}.tmp`;
  fs.writeFileSync(tmp, `${JSON.stringify(receipt, null, 2)}\n`, 'utf8');
  fs.renameSync(tmp, path);
  return path;
}

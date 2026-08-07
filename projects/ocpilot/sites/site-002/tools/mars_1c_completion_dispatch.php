<?php
/**
 * MARS SITE-002 server-side Client Ops completion dispatcher (Phase 1B-D6G1).
 * Invoked by the canonical import wrapper immediately after terminal.json is written.
 * Secrets come only from mars_1c_wrapper.local.php (non-Git).
 */
declare(strict_types=1);

const MARS_1C_DISPATCH_SCHEMA = '1b-d6g1a.1';
const MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID = '8f3c2a91-6b4e-4d7a-9c1f-2e5a8b0d4f67';
const MARS_1C_DISPATCH_PENDING = 'PENDING';
const MARS_1C_DISPATCH_SENDING = 'SENDING';
const MARS_1C_DISPATCH_SENT = 'SENT';
const MARS_1C_DISPATCH_FAILED_RETRYABLE = 'FAILED_RETRYABLE';
const MARS_1C_DISPATCH_FAILED_FINAL = 'FAILED_FINAL';
const MARS_1C_DISPATCH_ALREADY = 'ALREADY_DISPATCHED';
const MARS_1C_DISPATCH_BLOCKED_KILL_SWITCH = 'BLOCKED_BY_KILL_SWITCH';

/**
 * Authoritative server-side outbound Client Ops kill switch (Phase 1B-D6G1A).
 * Preferred key: CLIENT_OPS_DISPATCH_ENABLED
 * Established equivalent (D6G1): server_dispatch_enabled
 * Default: true (dispatch allowed).
 */
function mars_1c_client_ops_dispatch_enabled(array $cfg): bool
{
    foreach (['CLIENT_OPS_DISPATCH_ENABLED', 'client_ops_dispatch_enabled', 'server_dispatch_enabled'] as $key) {
        if (!array_key_exists($key, $cfg)) {
            continue;
        }
        $v = $cfg[$key];
        if (is_bool($v)) {
            return $v;
        }
        if (is_int($v) || is_float($v)) {
            return ((int) $v) !== 0;
        }
        if (is_string($v)) {
            $normalized = strtolower(trim($v));
            if (in_array($normalized, ['1', 'true', 'yes', 'on', 'enabled'], true)) {
                return true;
            }
            if (in_array($normalized, ['0', 'false', 'no', 'off', 'disabled'], true)) {
                return false;
            }
        }
    }
    return true;
}

function mars_1c_dispatch_dir(array $paths): string
{
    return $paths['storage'] . '/mars-tools/cron/dispatch-state';
}

function mars_1c_dispatch_status_path(array $paths, string $runId): string
{
    return mars_1c_run_dir($paths, $runId) . '/dispatch-status.json';
}

function mars_1c_dispatch_delivered_path(array $paths, string $runId): string
{
    return mars_1c_dispatch_dir($paths) . '/' . preg_replace('/[^a-zA-Z0-9._-]/', '_', $runId) . '.delivered.json';
}

function mars_1c_uuid_v5(string $namespaceUuid, string $name): string
{
    $nhex = str_replace('-', '', $namespaceUuid);
    $ns = hex2bin($nhex);
    if ($ns === false || strlen($ns) !== 16) {
        throw new RuntimeException('Invalid namespace UUID');
    }
    $hash = sha1($ns . $name, true);
    $hash[6] = chr((ord($hash[6]) & 0x0f) | 0x50);
    $hash[8] = chr((ord($hash[8]) & 0x3f) | 0x80);
    $h = bin2hex($hash);
    return substr($h, 0, 8) . '-' . substr($h, 8, 4) . '-' . substr($h, 12, 4)
        . '-' . substr($h, 16, 4) . '-' . substr($h, 20, 12);
}

/** @param mixed $value */
function mars_1c_sort_keys_deep($value)
{
    if (is_array($value)) {
        $isList = array_keys($value) === range(0, count($value) - 1);
        if ($isList) {
            $out = [];
            foreach ($value as $item) {
                $out[] = mars_1c_sort_keys_deep($item);
            }
            return $out;
        }
        ksort($value);
        $out = [];
        foreach ($value as $k => $v) {
            $out[$k] = mars_1c_sort_keys_deep($v);
        }
        return $out;
    }
    return $value;
}

function mars_1c_compute_event_id(array $parts): string
{
    $identity = [
        'action_code' => $parts['action_code'] ?? 'NONE',
        'event_type' => $parts['event_type'] ?? 'site.post_1c_monitor',
        'metrics' => [
            'added_urls' => (int) ($parts['metrics']['added_urls'] ?? 0),
            'baseline_count' => (int) ($parts['metrics']['baseline_count'] ?? 0),
            'current_count' => (int) ($parts['metrics']['current_count'] ?? 0),
            'onboarding_needed_count' => (int) ($parts['metrics']['onboarding_needed_count'] ?? 0),
            'removed_urls' => (int) ($parts['metrics']['removed_urls'] ?? 0),
        ],
        'normalized_status' => $parts['normalized_status'] ?? 'ATTENTION',
        'observed_at' => $parts['observed_at'] ?? '',
        'reason_codes' => array_values($parts['reason_codes'] ?? []),
        'run_id' => $parts['run_id'] ?? '',
        'schema_major' => (int) ($parts['schema_major'] ?? 1),
        'site_id' => $parts['site_id'] ?? MARS_1C_SITE_ID,
        'summary_code' => $parts['summary_code'] ?? '',
    ];
    sort($identity['reason_codes']);
    $canonical = mars_1c_sort_keys_deep($identity);
    $json = json_encode($canonical, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    if ($json === false) {
        throw new RuntimeException('event identity encode failed');
    }
    return mars_1c_uuid_v5(MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID, hash('sha256', $json));
}

function mars_1c_format_site002_local_time(?string $iso): string
{
    if ($iso === null || $iso === '') {
        return '';
    }
    try {
        $dt = new DateTimeImmutable($iso);
        $dt = $dt->setTimezone(new DateTimeZone('Asia/Barnaul'));
        return $dt->format('d.m.Y, H:i');
    } catch (Throwable $e) {
        return '';
    }
}

function mars_1c_telegram_text_from_terminal(array $terminal): string
{
    $summary = (string) ($terminal['summary_code'] ?? '');
    $final = (string) ($terminal['final_status'] ?? '');
    $observed = mars_1c_format_site002_local_time($terminal['completed_at'] ?? $terminal['started_at'] ?? null);
    $domain = 'bzpm.ru';

    if ($final === MARS_1C_STATUS_SUCCESS || $summary === 'FULL_IMPORT_SUCCESS') {
        $title = '✅ Импорт 1С завершён успешно';
        $body = "Каталог обновлён.\nЦены и остатки обработаны.\nКритических ошибок не обнаружено.";
    } elseif ($final === MARS_1C_STATUS_FAILED || $summary === 'IMPORT_ERROR') {
        $title = '❌ Импорт 1С завершился с ошибкой';
        $err = trim((string) ($terminal['sanitized_error_summary'] ?? 'Импорт завершился с ошибкой'));
        $body = $err !== '' ? $err : 'Импорт завершился с ошибкой.';
    } elseif ($final === MARS_1C_STATUS_ATTENTION_COMPLETED_WITH_WARNINGS || $summary === 'IMPORT_COMPLETED_WITH_WARNINGS') {
        $title = '⚠️ Импорт 1С завершён с предупреждениями';
        $body = trim((string) ($terminal['sanitized_error_summary'] ?? 'Импорт завершён с предупреждениями'));
    } else {
        // Default / offers missing
        $title = '⚠️ Импорт 1С выполнен не полностью';
        $body = "Каталог обработан успешно.\nФайл с ценами и остатками от 1С не получен.\n\nЦены и остатки товаров могли не обновиться.\n\nЧто проверить:\nвыгрузку предложений из 1С и наличие файла offers0_*.xml.";
    }

    $lines = [$title, '', 'Сайт: ' . $domain];
    if ($observed !== '') {
        $lines[] = 'Время: ' . $observed;
    }
    $lines[] = '';
    $lines[] = $body;
    return implode("\n", $lines);
}

function mars_1c_build_completion_envelope(array $terminal): array
{
    $runId = (string) ($terminal['run_id'] ?? '');
    $final = (string) ($terminal['final_status'] ?? '');
    $summary = (string) ($terminal['summary_code'] ?? 'IMPORT_COMPLETION');
    $reportClass = (string) ($terminal['report_class'] ?? '');
    $observedAt = (string) ($terminal['completed_at'] ?? $terminal['started_at'] ?? date('c'));

    if ($final === MARS_1C_STATUS_SUCCESS) {
        $severity = 'OK';
        $normalized = 'OK';
        $sourceStatus = 'CLEAN';
        $reason = ['D6G_IMPORT_COMPLETION', 'FULL_IMPORT_SUCCESS'];
        $actionCode = 'NONE';
    } elseif ($final === MARS_1C_STATUS_FAILED) {
        $severity = 'FAILED';
        $normalized = 'FAILED';
        $sourceStatus = 'FAILURE_REVIEW_REQUIRED';
        $reason = ['D6G_IMPORT_COMPLETION', 'IMPORT_ERROR'];
        $actionCode = 'REVIEW_IMPORT_FAILURE';
    } elseif ($final === MARS_1C_STATUS_ATTENTION_COMPLETED_WITH_WARNINGS) {
        $severity = 'ATTENTION';
        $normalized = 'ATTENTION';
        $sourceStatus = 'ATTENTION_REQUIRED';
        $reason = ['D6G_IMPORT_COMPLETION', 'IMPORT_COMPLETED_WITH_WARNINGS'];
        $actionCode = 'REVIEW_IMPORT_WARNINGS';
    } else {
        $severity = 'ATTENTION';
        $normalized = 'ATTENTION';
        $sourceStatus = 'ATTENTION_REQUIRED';
        $reason = ['D6G_IMPORT_COMPLETION', 'OFFERS0_XML_ABSENT'];
        $actionCode = 'CHECK_1C_OFFERS_EXPORT';
        if ($summary === '' || $summary === 'IMPORT_COMPLETION') {
            $summary = 'OFFERS_INPUT_MISSING';
        }
        if ($reportClass === '') {
            $reportClass = 'CATALOG_SUCCESS_OFFERS_INPUT_MISSING';
        }
    }

    $telegram = mars_1c_telegram_text_from_terminal($terminal);
    $eventId = mars_1c_compute_event_id([
        'action_code' => $actionCode,
        'event_type' => 'site.post_1c_monitor',
        'metrics' => [
            'added_urls' => 0,
            'baseline_count' => 0,
            'current_count' => 0,
            'onboarding_needed_count' => 0,
            'removed_urls' => 0,
        ],
        'normalized_status' => $normalized,
        'observed_at' => $observedAt,
        'reason_codes' => $reason,
        'run_id' => $runId,
        'schema_major' => 1,
        'site_id' => MARS_1C_SITE_ID,
        'summary_code' => $summary,
    ]);

    return [
        'schema_name' => 'mars.client_ops.report',
        'schema_version' => '1.0',
        'event_id' => $eventId,
        'event_type' => 'site.post_1c_monitor',
        'generated_at' => date('c'),
        'observed_at' => $observedAt,
        'environment' => 'production',
        'site' => [
            'site_id' => MARS_1C_SITE_ID,
            'site_name' => 'BZPM',
            'domain' => 'bzpm.ru',
        ],
        'producer' => [
            'name' => 'mars.client-ops.site-002.server-completion-dispatcher',
            'version' => MARS_1C_DISPATCH_SCHEMA,
        ],
        'run' => [
            'run_id' => $runId,
            'source_status' => $sourceStatus,
            'normalized_status' => $normalized,
            'summary_code' => $summary,
            'reason_codes' => $reason,
        ],
        'action' => [
            'required' => $severity !== 'OK',
            'code' => $actionCode,
            'text' => $telegram,
        ],
        'metrics' => [
            'baseline_count' => 0,
            'current_count' => 0,
            'added_urls' => 0,
            'removed_urls' => 0,
            'onboarding_needed_count' => 0,
        ],
        'freshness' => ['age_seconds' => 30, 'stale' => false],
        'security' => [
            'classification' => 'internal',
            'contains_secrets' => false,
            'redacted' => true,
        ],
        'report_class' => $reportClass !== '' ? $reportClass : $summary,
        'import_final_status' => $final,
        'trigger_source' => $terminal['trigger_source'] ?? null,
        'telegram_text' => $telegram,
    ];
}

/**
 * Persist dispatch attempt without secrets.
 *
 * @return array{status:string,http_status:?int,event_id:?string,attempted_at:string,reason:?string,intake_state:?string,delivery_state:?string}
 */
function mars_1c_write_dispatch_status(array $paths, string $runId, array $status): bool
{
    $status['schema_version'] = MARS_1C_DISPATCH_SCHEMA;
    $status['run_id'] = $runId;
    $status['updated_at'] = date('c');
    // Never persist secret-bearing fields
    unset($status['webhook_url'], $status['token'], $status['authorization'], $status['secret']);
    return mars_1c_atomic_write_json(mars_1c_dispatch_status_path($paths, $runId), $status);
}

function mars_1c_dispatch_ui_label(?string $status): string
{
    switch ((string) $status) {
        case MARS_1C_DISPATCH_SENT:
        case MARS_1C_DISPATCH_ALREADY:
        case 'DELIVERED':
            return 'Отправлен';
        case MARS_1C_DISPATCH_SENDING:
            return 'Отправляется';
        case MARS_1C_DISPATCH_FAILED_RETRYABLE:
        case MARS_1C_DISPATCH_FAILED_FINAL:
            return 'Ошибка отправки';
        case MARS_1C_DISPATCH_PENDING:
        case 'QUEUED':
            return 'Ожидает отправки';
        case MARS_1C_DISPATCH_BLOCKED_KILL_SWITCH:
        case 'SERVER_DISPATCH_DISABLED':
            return 'Отключено (kill switch)';
        default:
            return $status !== null && $status !== '' ? (string) $status : 'Не запрошен';
    }
}

/**
 * One immediate authenticated POST to n8n webhook. No retry loop.
 *
 * @return array{ok:bool,status:string,http_status:?int,event_id:?string,reason:?string,intake_state:?string,delivery_state:?string,duplicate?:bool}
 */
function mars_1c_server_dispatch_completion(array $paths, array $cfg, string $runId, ?array $terminal = null): array
{
    $runId = preg_replace('/[^a-zA-Z0-9._-]/', '_', $runId) ?? $runId;
    $deliveredPath = mars_1c_dispatch_delivered_path($paths, $runId);
    if (is_file($deliveredPath)) {
        $prev = mars_1c_read_json($deliveredPath) ?: [];
        return [
            'ok' => true,
            'status' => MARS_1C_DISPATCH_ALREADY,
            'http_status' => isset($prev['http_status']) ? (int) $prev['http_status'] : null,
            'event_id' => $prev['event_id'] ?? null,
            'reason' => 'ALREADY_DISPATCHED',
            'intake_state' => $prev['intake_state'] ?? null,
            'delivery_state' => $prev['delivery_state'] ?? null,
            'duplicate' => true,
        ];
    }

    if (!mars_1c_client_ops_dispatch_enabled($cfg)) {
        $blocked = [
            'status' => MARS_1C_DISPATCH_BLOCKED_KILL_SWITCH,
            'http_status' => null,
            'event_id' => null,
            'attempted_at' => date('c'),
            'reason' => 'BLOCKED_BY_KILL_SWITCH',
            'intake_state' => null,
            'delivery_state' => null,
        ];
        mars_1c_write_dispatch_status($paths, $runId, $blocked);
        return ['ok' => true, 'blocked' => true] + $blocked;
    }

    if ($terminal === null) {
        $terminal = mars_1c_read_json(mars_1c_run_dir($paths, $runId) . '/terminal.json');
    }
    if (!is_array($terminal) || empty($terminal['run_id'])) {
        $fail = [
            'status' => MARS_1C_DISPATCH_FAILED_FINAL,
            'http_status' => null,
            'event_id' => null,
            'attempted_at' => date('c'),
            'reason' => 'TERMINAL_MISSING',
            'intake_state' => null,
            'delivery_state' => null,
        ];
        mars_1c_write_dispatch_status($paths, $runId, $fail);
        return ['ok' => false] + $fail;
    }

    $webhookUrl = trim((string) ($cfg['client_ops_webhook_url'] ?? ''));
    $token = (string) ($cfg['client_ops_webhook_auth_secret'] ?? $cfg['client_ops_webhook_token'] ?? '');
    if ($webhookUrl === '' || $token === '') {
        $fail = [
            'status' => MARS_1C_DISPATCH_FAILED_RETRYABLE,
            'http_status' => null,
            'event_id' => null,
            'attempted_at' => date('c'),
            'reason' => 'WEBHOOK_CREDS_MISSING',
            'intake_state' => null,
            'delivery_state' => null,
        ];
        mars_1c_write_dispatch_status($paths, $runId, $fail);
        return ['ok' => false] + $fail;
    }

    $envelope = mars_1c_build_completion_envelope($terminal);
    $sending = [
        'status' => MARS_1C_DISPATCH_SENDING,
        'http_status' => null,
        'event_id' => $envelope['event_id'],
        'attempted_at' => date('c'),
        'reason' => null,
        'intake_state' => null,
        'delivery_state' => null,
    ];
    mars_1c_write_dispatch_status($paths, $runId, $sending);

    $payload = json_encode($envelope, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    if ($payload === false) {
        $fail = [
            'status' => MARS_1C_DISPATCH_FAILED_FINAL,
            'http_status' => null,
            'event_id' => $envelope['event_id'],
            'attempted_at' => date('c'),
            'reason' => 'ENVELOPE_ENCODE_FAILED',
            'intake_state' => null,
            'delivery_state' => null,
        ];
        mars_1c_write_dispatch_status($paths, $runId, $fail);
        return ['ok' => false] + $fail;
    }

    $httpStatus = null;
    $body = '';
    $transportError = null;
    if (function_exists('curl_init')) {
        $ch = curl_init($webhookUrl);
        curl_setopt_array($ch, [
            CURLOPT_POST => true,
            CURLOPT_HTTPHEADER => [
                'Accept: application/json',
                'Content-Type: application/json',
                'x-mars-client-ops-token: ' . $token,
            ],
            CURLOPT_POSTFIELDS => $payload,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CONNECTTIMEOUT => 15,
            CURLOPT_TIMEOUT => 45,
        ]);
        $body = (string) curl_exec($ch);
        if ($body === '' && curl_errno($ch)) {
            $transportError = 'CURL_' . curl_errno($ch);
        }
        $httpStatus = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
    } else {
        $ctx = stream_context_create([
            'http' => [
                'method' => 'POST',
                'header' => "Accept: application/json\r\nContent-Type: application/json\r\nx-mars-client-ops-token: {$token}\r\n",
                'content' => $payload,
                'timeout' => 45,
                'ignore_errors' => true,
            ],
        ]);
        $body = (string) @file_get_contents($webhookUrl, false, $ctx);
        if (isset($http_response_header[0]) && preg_match('/\s(\d{3})\s/', $http_response_header[0], $m)) {
            $httpStatus = (int) $m[1];
        }
    }

    $decoded = null;
    if ($body !== '') {
        $decoded = json_decode($body, true);
    }
    $intake = is_array($decoded) ? ($decoded['intake_state'] ?? ($decoded['data']['intake_state'] ?? null)) : null;
    $delivery = is_array($decoded) ? ($decoded['delivery_state'] ?? ($decoded['data']['delivery_state'] ?? null)) : null;
    $ok = ($httpStatus === 200 || $httpStatus === 202);

    if ($ok) {
        $receipt = [
            'status' => MARS_1C_DISPATCH_SENT,
            'http_status' => $httpStatus,
            'event_id' => $envelope['event_id'],
            'attempted_at' => date('c'),
            'reason' => null,
            'intake_state' => is_string($intake) ? $intake : null,
            'delivery_state' => is_string($delivery) ? $delivery : null,
            'producer' => 'server-completion-dispatcher',
        ];
        mars_1c_write_dispatch_status($paths, $runId, $receipt);
        mars_1c_atomic_write_json($deliveredPath, $receipt);
        // Clear inbox marker if present (best-effort)
        $inbox = mars_1c_dispatch_inbox_dir($paths) . '/' . $runId . '.json';
        if (is_file($inbox)) {
            @unlink($inbox);
        }
        return ['ok' => true] + $receipt;
    }

    $reason = $transportError ?: ('HTTP_' . (string) ($httpStatus ?? '0'));
    $failStatus = ($httpStatus === 400 || $httpStatus === 401 || $httpStatus === 403)
        ? MARS_1C_DISPATCH_FAILED_FINAL
        : MARS_1C_DISPATCH_FAILED_RETRYABLE;
    $fail = [
        'status' => $failStatus,
        'http_status' => $httpStatus,
        'event_id' => $envelope['event_id'],
        'attempted_at' => date('c'),
        'reason' => $reason,
        'intake_state' => is_string($intake) ? $intake : null,
        'delivery_state' => is_string($delivery) ? $delivery : null,
    ];
    mars_1c_write_dispatch_status($paths, $runId, $fail);
    return ['ok' => false] + $fail;
}

/**
 * Bounded recovery sweep: only PENDING / FAILED_RETRYABLE terminals.
 * Max one attempt per run per invocation. No uncontrolled loops.
 *
 * @return array{scanned:int,attempted:int,sent:int,already:int,failed:int,results:array<int,array>}
 */
function mars_1c_dispatch_recovery_sweep(array $paths, array $cfg, int $limit = 20): array
{
    $runsDir = mars_1c_runs_dir($paths);
    $out = ['scanned' => 0, 'attempted' => 0, 'sent' => 0, 'already' => 0, 'failed' => 0, 'results' => []];
    if (!is_dir($runsDir)) {
        return $out;
    }
    $names = scandir($runsDir) ?: [];
    foreach ($names as $name) {
        if ($name === '.' || $name === '..') {
            continue;
        }
        if (!is_dir($runsDir . '/' . $name)) {
            continue;
        }
        if (!preg_match('/^mars-\d{8}-/', $name)) {
            continue;
        }
        $out['scanned']++;
        if ($out['attempted'] >= $limit) {
            break;
        }
        $termPath = $runsDir . '/' . $name . '/terminal.json';
        if (!is_file($termPath)) {
            continue;
        }
        $st = mars_1c_read_json(mars_1c_dispatch_status_path($paths, $name));
        $status = is_array($st) ? (string) ($st['status'] ?? '') : '';
        if ($status === MARS_1C_DISPATCH_SENT || $status === MARS_1C_DISPATCH_ALREADY) {
            continue;
        }
        if (is_file(mars_1c_dispatch_delivered_path($paths, $name))) {
            continue;
        }
        // Prefer inbox-marked or explicitly retryable/pending
        $inbox = mars_1c_dispatch_inbox_dir($paths) . '/' . $name . '.json';
        $eligible = is_file($inbox)
            || $status === ''
            || $status === MARS_1C_DISPATCH_PENDING
            || $status === 'QUEUED'
            || $status === MARS_1C_DISPATCH_FAILED_RETRYABLE
            || $status === MARS_1C_DISPATCH_BLOCKED_KILL_SWITCH
            || $status === 'SERVER_DISPATCH_DISABLED';
        if (!$eligible) {
            continue;
        }
        $out['attempted']++;
        $result = mars_1c_server_dispatch_completion($paths, $cfg, $name);
        $out['results'][] = [
            'run_id' => $name,
            'ok' => !empty($result['ok']),
            'status' => $result['status'] ?? null,
            'reason' => $result['reason'] ?? null,
            'http_status' => $result['http_status'] ?? null,
        ];
        if (!empty($result['duplicate']) || (($result['status'] ?? '') === MARS_1C_DISPATCH_ALREADY)) {
            $out['already']++;
        } elseif (!empty($result['ok'])) {
            $out['sent']++;
        } else {
            $out['failed']++;
        }
    }
    return $out;
}

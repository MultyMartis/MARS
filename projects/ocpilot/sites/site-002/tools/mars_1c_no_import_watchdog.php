<?php
/**
 * MARS SITE-002 server-side no-import watchdog (Phase 1B-D6G1).
 * Emits at most one NO_FRESH_IMPORT Client Ops event per reporting date
 * when no completed scheduled terminal exists for the expected window.
 *
 * CLI: php mars_1c_no_import_watchdog.php
 * Cron (Moscow): 0 9 * * *  (= 13:00 Asia/Barnaul)
 */
declare(strict_types=1);

require_once __DIR__ . '/mars_1c_import_run_contract.php';
require_once __DIR__ . '/mars_1c_completion_dispatch.php';

const MARS_WATCHDOG_VERSION = '1b-d6g1.1';
const MARS_WATCHDOG_DEADLINE_HOUR_BARNAUL = 13;

function mars_watchdog_paths(): array
{
    $here = __DIR__;
    if (strpos($here, DIRECTORY_SEPARATOR . 'storage' . DIRECTORY_SEPARATOR . 'mars-tools') !== false) {
        $resolved = realpath($here . '/../../..');
        $root = $resolved ? $resolved : $here . '/../../..';
    } else {
        $resolved = realpath($here . '/../..');
        $root = $resolved ? $resolved : $here . '/../..';
    }
    return [
        'app_root' => $root,
        'storage' => $root . '/storage',
        'local_config' => $root . '/storage/mars-tools/cron/mars_1c_wrapper.local.php',
        'runs_dir' => $root . '/storage/mars-tools/cron/runs',
        'current_run' => $root . '/storage/mars-tools/cron/current-run.json',
        'watchdog_state' => $root . '/storage/mars-tools/cron/watchdog-state',
        'log_dir' => $root . '/storage/mars-tools/cron/logs',
    ];
}

function mars_watchdog_load_cfg(array $paths): array
{
    $cfg = [
        'client_ops_webhook_url' => '',
        'client_ops_webhook_auth_secret' => '',
        'client_ops_webhook_token' => '',
        'server_dispatch_enabled' => true,
        'watchdog_enabled' => true,
    ];
    if (is_file($paths['local_config'])) {
        /** @noinspection PhpIncludeInspection */
        $local = include $paths['local_config'];
        if (is_array($local)) {
            $cfg = array_merge($cfg, $local);
        }
    }
    return $cfg;
}

function mars_watchdog_barnaul_now(): DateTimeImmutable
{
    return new DateTimeImmutable('now', new DateTimeZone('Asia/Barnaul'));
}

function mars_watchdog_log(array $paths, string $msg): void
{
    if (!is_dir($paths['log_dir'])) {
        @mkdir($paths['log_dir'], 0755, true);
    }
    $line = sprintf("[%s] [WATCHDOG] %s\n", date('c'), $msg);
    @file_put_contents($paths['log_dir'] . '/mars_1c_watchdog_' . date('Ymd') . '.log', $line, FILE_APPEND | LOCK_EX);
}

function mars_watchdog_find_today_scheduled_terminal(array $paths, string $ymdCompact, string $ymdDash): ?array
{
    $runsDir = $paths['runs_dir'];
    if (!is_dir($runsDir)) {
        return null;
    }
    $names = scandir($runsDir) ?: [];
    $best = null;
    foreach ($names as $name) {
        if ($name === '.' || $name === '..') {
            continue;
        }
        if (strpos($name, 'mars-' . $ymdCompact) !== 0) {
            continue;
        }
        $term = mars_1c_read_json($runsDir . '/' . $name . '/terminal.json');
        if (!is_array($term) || empty($term['final_status'])) {
            continue;
        }
        $trigger = (string) ($term['trigger_source'] ?? '');
        // Any completed terminal for the reporting date satisfies freshness
        // (manual import accepted as daily freshness per D6G1 policy).
        $completed = (string) ($term['completed_at'] ?? $term['started_at'] ?? '');
        if ($completed !== '' && strpos($completed, $ymdDash) === false && strpos($name, $ymdCompact) === false) {
            continue;
        }
        if ($best === null) {
            $best = $term;
        }
        if ($trigger === MARS_1C_TRIGGER_SCHEDULED) {
            return $term;
        }
    }
    // Also inspect current-run if same date
    $cur = mars_1c_read_json($paths['current_run']);
    if (is_array($cur) && !empty($cur['final_status'])) {
        $rid = (string) ($cur['run_id'] ?? '');
        $completed = (string) ($cur['completed_at'] ?? $cur['started_at'] ?? '');
        if (strpos($rid, $ymdCompact) !== false || strpos($completed, $ymdDash) !== false) {
            return $cur;
        }
    }
    return $best;
}

function mars_watchdog_build_no_fresh_envelope(string $eventDate, string $observedAt): array
{
    $eventId = 'site002-no-fresh-import-' . $eventDate;
    $telegram = "⚠️ Нет свежего импорта 1С\n\nСайт: bzpm.ru\nВремя проверки: "
        . mars_1c_format_site002_local_time($observedAt)
        . "\n\nОжидаемый импорт 1С за сегодня не найден.\nПроверьте выгрузку из 1С и расписание Beget cron.";
    return [
        'schema_name' => 'mars.client_ops.report',
        'schema_version' => '1.0',
        'event_id' => $eventId,
        'event_type' => 'site.post_1c_monitor',
        'generated_at' => $observedAt,
        'observed_at' => $observedAt,
        'environment' => 'production',
        'site' => [
            'site_id' => MARS_1C_SITE_ID,
            'site_name' => 'BZPM',
            'domain' => 'bzpm.ru',
        ],
        'producer' => [
            'name' => 'mars.client-ops.site-002.server-no-import-watchdog',
            'version' => MARS_WATCHDOG_VERSION,
        ],
        'run' => [
            'run_id' => 'watchdog-' . $eventDate,
            'source_status' => 'ATTENTION_REQUIRED',
            'normalized_status' => 'ATTENTION',
            'summary_code' => 'NO_FRESH_1C_IMPORT',
            'reason_codes' => ['NO_FRESH_IMPORT_IN_EXPECTED_WINDOW', 'D6G1_SERVER_WATCHDOG'],
        ],
        'action' => [
            'required' => true,
            'code' => 'CHECK_1C_SCHEDULED_IMPORT',
            'text' => $telegram,
        ],
        'metrics' => [
            'baseline_count' => 0,
            'current_count' => 0,
            'added_urls' => 0,
            'removed_urls' => 0,
            'onboarding_needed_count' => 0,
        ],
        'freshness' => ['age_seconds' => 0, 'stale' => false],
        'security' => [
            'classification' => 'internal',
            'contains_secrets' => false,
            'redacted' => true,
        ],
        'report_class' => 'NO_FRESH_IMPORT',
        'telegram_text' => $telegram,
    ];
}

function mars_watchdog_post(array $cfg, array $envelope): array
{
    $webhookUrl = trim((string) ($cfg['client_ops_webhook_url'] ?? ''));
    $token = (string) ($cfg['client_ops_webhook_auth_secret'] ?? $cfg['client_ops_webhook_token'] ?? '');
    if ($webhookUrl === '' || $token === '') {
        return ['ok' => false, 'http_status' => null, 'reason' => 'WEBHOOK_CREDS_MISSING'];
    }
    $payload = json_encode($envelope, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    if ($payload === false) {
        return ['ok' => false, 'http_status' => null, 'reason' => 'ENCODE_FAILED'];
    }
    $httpStatus = null;
    $body = '';
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
    $ok = ($httpStatus === 200 || $httpStatus === 202);
    return [
        'ok' => $ok,
        'http_status' => $httpStatus,
        'reason' => $ok ? null : ('HTTP_' . (string) ($httpStatus ?? '0')),
        'body_len' => strlen($body),
    ];
}

function mars_watchdog_main(): void
{
    $paths = mars_watchdog_paths();
    $cfg = mars_watchdog_load_cfg($paths);
    $now = mars_watchdog_barnaul_now();
    $eventDate = $now->format('Y-m-d');
    $ymdCompact = $now->format('Ymd');
    $observedAt = $now->format('c');
    $marker = $paths['watchdog_state'] . '/' . $eventDate . '.sent.json';

    $out = [
        'ok' => true,
        'watchdog_version' => MARS_WATCHDOG_VERSION,
        'event_date' => $eventDate,
        'local_hour' => (int) $now->format('G'),
        'skipped' => false,
        'reason' => null,
    ];

    if (empty($cfg['watchdog_enabled'])) {
        $out['skipped'] = true;
        $out['reason'] = 'WATCHDOG_DISABLED';
        echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
        return;
    }
    if (is_file($marker)) {
        $out['skipped'] = true;
        $out['reason'] = 'ALREADY_SENT_TODAY';
        echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
        return;
    }
    if ((int) $now->format('G') < MARS_WATCHDOG_DEADLINE_HOUR_BARNAUL) {
        $out['skipped'] = true;
        $out['reason'] = 'BEFORE_DEADLINE';
        echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
        return;
    }

    // Import still running?
    $cur = mars_1c_read_json($paths['current_run']);
    if (is_array($cur) && empty($cur['final_status'])) {
        $phase = (string) ($cur['current_phase'] ?? '');
        if ($phase !== '' && !in_array($phase, [MARS_1C_PHASE_DONE, MARS_1C_PHASE_QUEUED], true)) {
            $out['skipped'] = true;
            $out['reason'] = 'IMPORT_STILL_RUNNING';
            $out['run_id'] = $cur['run_id'] ?? null;
            echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
            return;
        }
    }

    $terminal = mars_watchdog_find_today_scheduled_terminal($paths, $ymdCompact, $eventDate);
    if (is_array($terminal) && !empty($terminal['final_status'])) {
        $out['skipped'] = true;
        $out['reason'] = 'TERMINAL_EXISTS';
        $out['run_id'] = $terminal['run_id'] ?? null;
        $out['trigger_source'] = $terminal['trigger_source'] ?? null;
        echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
        return;
    }

    $envelope = mars_watchdog_build_no_fresh_envelope($eventDate, $observedAt);
    $post = mars_watchdog_post($cfg, $envelope);
    $receipt = [
        'event_id' => $envelope['event_id'],
        'ok' => !empty($post['ok']),
        'http_status' => $post['http_status'] ?? null,
        'reason' => $post['reason'] ?? null,
        'finished_at' => date('c'),
    ];
    if (!is_dir($paths['watchdog_state'])) {
        @mkdir($paths['watchdog_state'], 0755, true);
    }
    mars_1c_atomic_write_json($paths['watchdog_state'] . '/' . $eventDate . '.last-attempt.json', $receipt);
    if (!empty($post['ok'])) {
        mars_1c_atomic_write_json($marker, $receipt);
    }
    mars_watchdog_log($paths, 'result ok=' . (!empty($post['ok']) ? '1' : '0') . ' http=' . (string) ($post['http_status'] ?? ''));
    $out['ok'] = !empty($post['ok']);
    $out['receipt'] = $receipt;
    $out['watchdog_only'] = true;
    echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
    if (empty($post['ok'])) {
        exit(1);
    }
}

mars_watchdog_main();

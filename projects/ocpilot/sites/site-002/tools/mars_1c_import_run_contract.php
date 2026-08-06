<?php
/**
 * MARS SITE-002 canonical 1C import run contract (Phase 1B-D6G).
 * Shared by scheduled Beget cron and OpenCart admin manual launch.
 */
declare(strict_types=1);

const MARS_1C_RUN_SCHEMA_VERSION = '1b-d6g.1';
const MARS_1C_SITE_ID = 'SITE-002';
const MARS_1C_TRIGGER_SCHEDULED = 'SCHEDULED';
const MARS_1C_TRIGGER_ADMIN_MANUAL = 'ADMIN_MANUAL';

const MARS_1C_STATUS_SUCCESS = 'SUCCESS';
const MARS_1C_STATUS_ATTENTION_OFFERS_INPUT_MISSING = 'ATTENTION_OFFERS_INPUT_MISSING';
const MARS_1C_STATUS_ATTENTION_COMPLETED_WITH_WARNINGS = 'ATTENTION_COMPLETED_WITH_WARNINGS';
const MARS_1C_STATUS_FAILED = 'FAILED';

const MARS_1C_PHASE_QUEUED = 'QUEUED';
const MARS_1C_PHASE_STARTING = 'STARTING';
const MARS_1C_PHASE_CATALOG = 'CATALOG';
const MARS_1C_PHASE_OFFERS = 'OFFERS';
const MARS_1C_PHASE_TERMINAL = 'TERMINAL';
const MARS_1C_PHASE_DISPATCH = 'DISPATCH';
const MARS_1C_PHASE_DONE = 'DONE';

function mars_1c_runs_dir(array $paths): string
{
    return $paths['storage'] . '/mars-tools/cron/runs';
}

function mars_1c_current_path(array $paths): string
{
    return $paths['storage'] . '/mars-tools/cron/current-run.json';
}

function mars_1c_dispatch_inbox_dir(array $paths): string
{
    return $paths['storage'] . '/mars-tools/cron/dispatch-inbox';
}

function mars_1c_run_dir(array $paths, string $runId): string
{
    return mars_1c_runs_dir($paths) . '/' . preg_replace('/[^a-zA-Z0-9._-]/', '_', $runId);
}

function mars_1c_atomic_write_json(string $path, array $data): bool
{
    $dir = dirname($path);
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }
    $tmp = $path . '.tmp.' . getmypid();
    $json = json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    if ($json === false) {
        return false;
    }
    if (file_put_contents($tmp, $json . "\n", LOCK_EX) === false) {
        return false;
    }
    if (!@rename($tmp, $path)) {
        $ok = file_put_contents($path, $json . "\n", LOCK_EX) !== false;
        @unlink($tmp);
        return $ok;
    }
    return true;
}

function mars_1c_read_json(string $path): ?array
{
    if (!is_file($path)) {
        return null;
    }
    $raw = file_get_contents($path);
    if ($raw === false || $raw === '') {
        return null;
    }
    $data = json_decode($raw, true);
    return is_array($data) ? $data : null;
}

function mars_1c_new_run_state(string $runId, string $trigger, string $requestedAt): array
{
    return [
        'schema_version' => MARS_1C_RUN_SCHEMA_VERSION,
        'site_id' => MARS_1C_SITE_ID,
        'run_id' => $runId,
        'trigger_source' => $trigger,
        'requested_at' => $requestedAt,
        'started_at' => null,
        'completed_at' => null,
        'current_phase' => MARS_1C_PHASE_QUEUED,
        'final_status' => null,
        'ui_status' => 'Ожидает запуска',
        'catalog_input_inventory' => [],
        'offers_input_inventory' => [],
        'catalog_phase_result' => null,
        'offers_phase_result' => null,
        'authoritative_counts' => new stdClass(),
        'sanitized_error_summary' => null,
        'log_reference' => null,
        'terminal_result_path' => null,
        'txt_report_path' => null,
        'report_dispatch_status' => 'NOT_REQUESTED',
        'report_dispatch_at' => null,
        'pid' => null,
    ];
}

function mars_1c_ui_status_from_state(array $state): string
{
    $final = $state['final_status'] ?? null;
    $phase = $state['current_phase'] ?? '';
    if ($final === MARS_1C_STATUS_SUCCESS) {
        return 'Завершён';
    }
    if ($final === MARS_1C_STATUS_ATTENTION_OFFERS_INPUT_MISSING || $final === MARS_1C_STATUS_ATTENTION_COMPLETED_WITH_WARNINGS) {
        return 'Требует внимания';
    }
    if ($final === MARS_1C_STATUS_FAILED) {
        return 'Ошибка';
    }
    if (in_array($phase, [MARS_1C_PHASE_STARTING, MARS_1C_PHASE_CATALOG, MARS_1C_PHASE_OFFERS, MARS_1C_PHASE_TERMINAL, MARS_1C_PHASE_DISPATCH], true)) {
        return 'Выполняется';
    }
    if ($phase === MARS_1C_PHASE_QUEUED) {
        return 'Ожидает запуска';
    }
    return 'Не запущен';
}

function mars_1c_classify_terminal(array $stepCatalog, array $stepOffers, array $xmlSummary, bool $hardFail, ?string $error): array
{
    $catalogOk = (($stepCatalog['status'] ?? '') === 'PASS');
    $offersStatus = (string) ($stepOffers['status'] ?? '');
    $offersOk = ($offersStatus === 'PASS');
    $offersCount = (int) ($xmlSummary['offers0_count'] ?? 0);
    $offersInputs = [];
    if (!empty($stepOffers['input_files']) && is_array($stepOffers['input_files'])) {
        foreach ($stepOffers['input_files'] as $f) {
            if (is_string($f) && preg_match('/offers0_.*\\.xml/i', $f)) {
                $offersInputs[] = $f;
            }
        }
    }
    $hasOffersFile = $offersCount > 0 || count($offersInputs) > 0;

    if ($hardFail || !$catalogOk || ($offersStatus === 'FAIL')) {
        return [
            'final_status' => MARS_1C_STATUS_FAILED,
            'report_class' => 'IMPORT_ERROR',
            'summary_code' => 'IMPORT_ERROR',
            'sanitized_error_summary' => mars_1c_sanitize_error($error ?: 'Импорт завершился с ошибкой'),
        ];
    }

    // Catalog PASS + offers phase PASS/empty with no offers0_*.xml => ATTENTION (not full success).
    if ($catalogOk && !$hasOffersFile) {
        return [
            'final_status' => MARS_1C_STATUS_ATTENTION_OFFERS_INPUT_MISSING,
            'report_class' => 'CATALOG_SUCCESS_OFFERS_INPUT_MISSING',
            'summary_code' => 'OFFERS_INPUT_MISSING',
            'sanitized_error_summary' => 'Файл с ценами и остатками от 1С не получен',
        ];
    }

    if ($catalogOk && $offersOk && $hasOffersFile) {
        return [
            'final_status' => MARS_1C_STATUS_SUCCESS,
            'report_class' => 'FULL_SUCCESS',
            'summary_code' => 'FULL_IMPORT_SUCCESS',
            'sanitized_error_summary' => null,
        ];
    }

    return [
        'final_status' => MARS_1C_STATUS_ATTENTION_COMPLETED_WITH_WARNINGS,
        'report_class' => 'COMPLETED_WITH_WARNINGS',
        'summary_code' => 'IMPORT_COMPLETED_WITH_WARNINGS',
        'sanitized_error_summary' => mars_1c_sanitize_error($error ?: 'Импорт завершён с предупреждениями'),
    ];
}

function mars_1c_sanitize_error(?string $msg): ?string
{
    if ($msg === null) {
        return null;
    }
    $s = trim(preg_replace('/\\s+/', ' ', $msg) ?? '');
    if ($s === '') {
        return null;
    }
    $s = preg_replace('/[A-Za-z]:\\\\[^\\s]+/', '[path]', $s) ?? $s;
    $s = preg_replace('/\\/(?:home|var|storage|tmp)[^\\s]*/', '[path]', $s) ?? $s;
    $s = preg_replace('/\\b(token|password|secret|authorization)=\\S+/i', '$1=[REDACTED]', $s) ?? $s;
    return mb_substr($s, 0, 200);
}

function mars_1c_write_run_state(array $paths, array $state): bool
{
    $state['ui_status'] = mars_1c_ui_status_from_state($state);
    $runDir = mars_1c_run_dir($paths, (string) $state['run_id']);
    $ok1 = mars_1c_atomic_write_json($runDir . '/run-state.json', $state);
    $ok2 = mars_1c_atomic_write_json(mars_1c_current_path($paths), $state);
    return $ok1 && $ok2;
}

function mars_1c_write_terminal(array $paths, array $state, array $terminal): bool
{
    $runDir = mars_1c_run_dir($paths, (string) $state['run_id']);
    $path = $runDir . '/terminal.json';
    $ok = mars_1c_atomic_write_json($path, $terminal);
    $state['terminal_result_path'] = 'runs/' . $state['run_id'] . '/terminal.json';
    $state['current_phase'] = MARS_1C_PHASE_TERMINAL;
    $state['completed_at'] = $terminal['completed_at'] ?? date('c');
    $state['final_status'] = $terminal['final_status'] ?? null;
    mars_1c_write_run_state($paths, $state);
    return $ok;
}

function mars_1c_enqueue_dispatch(array $paths, string $runId): bool
{
    $dir = mars_1c_dispatch_inbox_dir($paths);
    return mars_1c_atomic_write_json($dir . '/' . $runId . '.json', [
        'schema_version' => MARS_1C_RUN_SCHEMA_VERSION,
        'site_id' => MARS_1C_SITE_ID,
        'run_id' => $runId,
        'queued_at' => date('c'),
        'dispatch_status' => 'PENDING',
    ]);
}

function mars_1c_lock_payload(array $paths, string $runId, string $phase, string $trigger): string
{
    return json_encode([
        'pid' => getmypid(),
        'run_id' => $runId,
        'phase' => $phase,
        'trigger_source' => $trigger,
        'started_at' => time(),
        'site_id' => MARS_1C_SITE_ID,
    ], JSON_UNESCAPED_UNICODE);
}

function mars_1c_parse_lock(array $paths): array
{
    $lock = $paths['lock_file'];
    if (!is_file($lock)) {
        return ['locked' => false];
    }
    $raw = trim((string) file_get_contents($lock));
    $json = json_decode($raw, true);
    if (is_array($json)) {
        $started = (int) ($json['started_at'] ?? 0);
        $age = $started > 0 ? time() - $started : null;
        return [
            'locked' => true,
            'pid' => isset($json['pid']) ? (int) $json['pid'] : null,
            'run_id' => $json['run_id'] ?? null,
            'phase' => $json['phase'] ?? null,
            'trigger_source' => $json['trigger_source'] ?? null,
            'started_at' => $started ?: null,
            'age_seconds' => $age,
            'stale' => $age !== null && $age > MARS_STALE_LOCK_SECONDS,
            'format' => 'json',
        ];
    }
    // Legacy pid|timestamp
    $parts = explode('|', $raw);
    $started = isset($parts[1]) ? (int) $parts[1] : 0;
    $age = $started > 0 ? time() - $started : null;
    return [
        'locked' => true,
        'pid' => isset($parts[0]) ? (int) $parts[0] : null,
        'run_id' => null,
        'phase' => null,
        'trigger_source' => null,
        'started_at' => $started ?: null,
        'age_seconds' => $age,
        'stale' => $age !== null && $age > MARS_STALE_LOCK_SECONDS,
        'format' => 'legacy',
    ];
}

function mars_1c_process_alive(?int $pid): bool
{
    if ($pid === null || $pid <= 0) {
        return false;
    }
    if (strncasecmp(PHP_OS, 'WIN', 3) === 0) {
        return false; // production lock lives on Linux Beget
    }
    // POSIX: signal 0 checks existence without killing.
    return @posix_kill($pid, 0);
}

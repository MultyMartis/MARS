<?php
/**
 * MARS SITE-002 parallel 1C cron wrapper.
 * Does not replace Sergey legacy import.
 * Run mode is disabled until operator enables cron and configures token/local config.
 *
 * Legacy entry preserved: index.php?route=common/cronjob
 * Sergey files: cronjob.php, import_1C.php, import_1C_offers.php — READ ONLY / untouched.
 *
 * Modes: --dry-run | --status | --run  (CLI)
 *        ?mode=dry-run|status|run&token=...  (HTTP via gateway only)
 *
 * TXT reports: /storage/mars-tools/cron/reports/
 */
declare(strict_types=1);

require_once __DIR__ . '/mars_1c_import_run_contract.php';

const MARS_WRAPPER_OPERATION = 'SITE-002-PROD-D6G-EVENT-DRIVEN-1C-IMPORT-01';
const MARS_WRAPPER_VERSION = '1.2.0';
const MARS_CMD_CATALOG = '1c';
const MARS_CMD_OFFERS = '1c_offers';
const MARS_MAX_RUNTIME_SECONDS = 2700;
const MARS_STALE_LOCK_SECONDS = 3600;
const MARS_BARNAUL_SCHEDULE = '12:00 Barnaul UTC+7';

function mars_str_contains($haystack, $needle)
{
    return $needle === '' || strpos($haystack, $needle) !== false;
}

/** Resolve application root (parent of storage/ and public_html/). */
function mars_app_root()
{
    $here = __DIR__;
    if (mars_str_contains($here, DIRECTORY_SEPARATOR . 'storage' . DIRECTORY_SEPARATOR . 'mars-tools')) {
        $resolved = realpath($here . '/../../..');
        return $resolved ? $resolved : $here . '/../../..';
    }
    if (mars_str_contains($here, DIRECTORY_SEPARATOR . 'public_html' . DIRECTORY_SEPARATOR . 'mars-tools')) {
        $resolved = realpath($here . '/../../..');
        return $resolved ? $resolved : $here . '/../../..';
    }
    $resolved = realpath($here . '/../..');
    return $resolved ? $resolved : $here . '/../..';
}

function mars_paths(): array
{
    $root = mars_app_root();
    return [
        'app_root' => $root,
        'public_html' => $root . '/public_html',
        'storage' => $root . '/storage',
        'xml_dir' => is_dir($root . '/1c_incoming/webdata')
            ? $root . '/1c_incoming/webdata'
            : $root . '/public_html/1c_incoming/webdata',
        'lock_file' => $root . '/storage/mars-tools/cron/mars_1c_import.lock',
        'log_dir' => $root . '/storage/mars-tools/cron/logs',
        'reports_dir' => $root . '/storage/mars-tools/cron/reports',
        'local_config' => $root . '/storage/mars-tools/cron/mars_1c_wrapper.local.php',
        'config_php' => $root . '/public_html/config.php',
        'cronjob_route' => 'index.php?route=common/cronjob',
        'wrapper_path' => $root . '/storage/mars-tools/cron/mars_1c_import_wrapper.php',
        'runs_dir' => $root . '/storage/mars-tools/cron/runs',
        'current_run' => $root . '/storage/mars-tools/cron/current-run.json',
        'dispatch_inbox' => $root . '/storage/mars-tools/cron/dispatch-inbox',
        'contract_path' => $root . '/storage/mars-tools/cron/mars_1c_import_run_contract.php',
    ];
}

function mars_load_local_config(array $paths): array
{
    $cfg = [
        'run_token' => '',
        'site_base_url' => 'https://bzpm.ru/',
        'allow_http_run' => false,
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

function mars_ensure_dir(string $dir): void
{
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }
}

function mars_log_path(array $paths): string
{
    mars_ensure_dir($paths['log_dir']);
    return $paths['log_dir'] . '/mars_1c_import_' . date('Ymd') . '.log';
}

function mars_log(array $paths, string $level, string $message): void
{
    $line = sprintf("[%s] [%s] %s\n", date('c'), strtoupper($level), $message);
    file_put_contents(mars_log_path($paths), $line, FILE_APPEND | LOCK_EX);
}

function mars_server_timezone_label(): string
{
    $tz = @date_default_timezone_get();
    if (!is_string($tz) || $tz === '') {
        return 'SAFE UNKNOWN';
    }
    return $tz;
}

function mars_generate_run_id(): string
{
    return 'mars-' . date('Ymd-His') . '-' . substr(bin2hex(random_bytes(4)), 0, 8);
}

function mars_report_filename(string $mode): string
{
    $stamp = date('Y-m-d_His');
    if ($mode === 'dry-run') {
        return 'mars_1c_import_dry_run_' . $stamp . '.txt';
    }
    if ($mode === 'status') {
        return 'mars_1c_import_status_' . $stamp . '.txt';
    }
    return 'mars_1c_import_' . $stamp . '.txt';
}

/** @return array{collector: callable, finalize: callable, path: string|null} */
function mars_report_begin(array $paths, string $mode, string $runId, ?float $wallStartedAt = null): array
{
    $lines = [];
    $startedAt = $wallStartedAt ?? microtime(true);
    $startedIso = $wallStartedAt !== null ? date('c', (int) $startedAt) : date('c');

    $lines[] = 'SITE-002 MARS 1C IMPORT REPORT';
    $lines[] = '';
    $lines[] = 'Run ID:';
    $lines[] = $runId;
    $lines[] = '';
    $lines[] = 'Operation:';
    $lines[] = 'MARS parallel 1C import wrapper';
    $lines[] = '';
    $lines[] = 'Mode:';
    $lines[] = $mode;
    $lines[] = '';
    $lines[] = 'Environment:';
    $lines[] = 'PRODUCTION';
    $lines[] = '';
    $lines[] = 'Production:';
    $lines[] = 'https://bzpm.ru/';
    $lines[] = '';
    $lines[] = 'Started:';
    $lines[] = $startedIso;
    $lines[] = '';
    $lines[] = 'Server timezone:';
    $lines[] = mars_server_timezone_label();
    $lines[] = '';
    $lines[] = 'Barnaul target schedule:';
    $lines[] = MARS_BARNAUL_SCHEDULE;
    $lines[] = '';
    $lines[] = 'Legacy policy:';
    $lines[] = 'Sergey legacy import preserved; wrapper is parallel.';
    $lines[] = '';
    $lines[] = 'Wrapper path:';
    $lines[] = $paths['wrapper_path'];
    $lines[] = '';

    $reportPath = null;
    $writeError = null;

    $collector = function (string $block) use (&$lines): void {
        $lines[] = $block;
    };

    $finalize = function (
        string $finalStatus,
        array $extra = []
    ) use (
        &$lines,
        &$reportPath,
        &$writeError,
        $paths,
        $mode,
        $startedAt,
        $startedIso
    ): ?string {
        if (isset($extra['lock_before'])) {
            $lockBefore = $extra['lock_before'];
            $lines[] = 'Lock:';
            $lines[] = 'status before: ' . (!empty($lockBefore['locked']) ? 'held' : 'free');
            $lines[] = 'created: ' . (isset($extra['lock_created']) && $extra['lock_created'] ? 'yes' : 'no');
            $lines[] = 'removed: ' . (isset($extra['lock_removed']) && $extra['lock_removed'] ? 'yes' : 'no');
            $lines[] = 'stale lock: ' . (!empty($lockBefore['stale']) ? 'yes' : 'no');
            $lines[] = '';
        }

        if (isset($extra['step_catalog'])) {
            $step = $extra['step_catalog'];
            $lines[] = 'Step 1 — catalog/products:';
            $lines[] = 'command:';
            $lines[] = MARS_CMD_CATALOG;
            $lines[] = 'status:';
            $lines[] = isset($step['status']) ? (string) $step['status'] : 'NOT RUN';
            $lines[] = 'input files:';
            if (!empty($step['input_files']) && is_array($step['input_files'])) {
                foreach ($step['input_files'] as $file) {
                    $lines[] = '- ' . $file;
                }
            } else {
                $lines[] = '- (none listed)';
            }
            $lines[] = 'duration:';
            $lines[] = isset($step['duration']) ? (string) $step['duration'] : 'n/a';
            $lines[] = 'errors:';
            $lines[] = isset($step['errors']) ? (string) $step['errors'] : '';
            $lines[] = '';
        }

        if (isset($extra['step_offers'])) {
            $step = $extra['step_offers'];
            $lines[] = 'Step 2 — offers/prices/stocks:';
            $lines[] = 'command:';
            $lines[] = MARS_CMD_OFFERS;
            $lines[] = 'status:';
            $lines[] = isset($step['status']) ? (string) $step['status'] : 'NOT RUN';
            $lines[] = 'input files:';
            if (!empty($step['input_files']) && is_array($step['input_files'])) {
                foreach ($step['input_files'] as $file) {
                    $lines[] = '- ' . $file;
                }
            } else {
                $lines[] = '- (none listed)';
            }
            $lines[] = 'duration:';
            $lines[] = isset($step['duration']) ? (string) $step['duration'] : 'n/a';
            $lines[] = 'errors:';
            $lines[] = isset($step['errors']) ? (string) $step['errors'] : '';
            $lines[] = '';
        }

        if (isset($extra['db_flags'])) {
            $db = $extra['db_flags'];
            $lines[] = 'DB flags:';
            $lines[] = '1c active before: ' . ($db['1c_before'] ?? 'NOT READ');
            $lines[] = '1c active after: ' . ($db['1c_after'] ?? 'NOT READ');
            $lines[] = '1c_offers active before: ' . ($db['1c_offers_before'] ?? 'NOT READ');
            $lines[] = '1c_offers active after: ' . ($db['1c_offers_after'] ?? 'NOT READ');
            $lines[] = 'Note:';
            $lines[] = 'Do not print DB credentials.';
            $lines[] = '';
        } else {
            $lines[] = 'DB flags:';
            $lines[] = '1c active before: NOT READ';
            $lines[] = '1c active after: NOT READ';
            $lines[] = '1c_offers active before: NOT READ';
            $lines[] = '1c_offers active after: NOT READ';
            $lines[] = 'Note:';
            $lines[] = 'Do not print DB credentials.';
            $lines[] = '';
        }

        $invocation = PHP_SAPI === 'cli' ? 'CLI' : 'HTTP gateway';
        $lines[] = 'HTTP/CLI invocation:';
        $lines[] = $invocation;
        $lines[] = '';
        $lines[] = 'Final status:';
        $lines[] = $finalStatus;
        $lines[] = '';
        $lines[] = 'Finished:';
        $lines[] = date('c');
        $lines[] = '';
        $lines[] = 'Duration:';
        $durationSeconds = round(microtime(true) - $startedAt, 2);
        if ($durationSeconds < 0.01 && isset($extra['duration_seconds'])) {
            $durationSeconds = round((float) $extra['duration_seconds'], 2);
        }
        $lines[] = (string) $durationSeconds . ' seconds';

        try {
            mars_ensure_dir($paths['reports_dir']);
            $filename = mars_report_filename($mode);
            $finalPath = $paths['reports_dir'] . '/' . $filename;
            $tmpPath = $finalPath . '.tmp';
            $content = implode("\n", $lines) . "\n";
            if (file_put_contents($tmpPath, $content, LOCK_EX) === false) {
                throw new RuntimeException('Failed to write report temp file');
            }
            if (!@rename($tmpPath, $finalPath)) {
                if (file_put_contents($finalPath, $content, LOCK_EX) === false) {
                    throw new RuntimeException('Failed to finalize report file');
                }
                @unlink($tmpPath);
            }
            $reportPath = $finalPath;
            mars_log($paths, 'info', 'TXT report written: ' . $filename);
        } catch (Throwable $e) {
            $writeError = $e->getMessage();
            mars_log($paths, 'warn', 'TXT report write failed: ' . $writeError);
        }

        return $reportPath;
    };

    return [
        'collector' => $collector,
        'finalize' => $finalize,
        'path' => $reportPath,
        'write_error' => &$writeError,
    ];
}

function mars_xml_input_summary(array $paths): array
{
    $xml = mars_check_xml($paths);
    $importSummary = [];
    foreach ($xml['import0_sample'] as $name) {
        $importSummary[] = $name . ' (import0_*.xml)';
    }
    if ($xml['import0_count'] > count($xml['import0_sample'])) {
        $importSummary[] = '... total import0 files: ' . $xml['import0_count'];
    }
    $offersSummary = [];
    foreach ($xml['offers0_sample'] as $name) {
        $offersSummary[] = $name . ' (offers0_*.xml)';
    }
    if ($xml['offers0_count'] > count($xml['offers0_sample'])) {
        $offersSummary[] = '... total offers0 files: ' . $xml['offers0_count'];
    }
    return [
        'catalog' => $importSummary,
        'offers' => $offersSummary,
        'import0_count' => $xml['import0_count'],
        'offers0_count' => $xml['offers0_count'],
    ];
}

function mars_output(array $payload, $exitCode = 0)
{
    if (PHP_SAPI === 'cli') {
        echo json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . PHP_EOL;
        exit((int) $exitCode);
    }
    header('Content-Type: application/json; charset=utf-8');
    $httpCode = 200;
    if ((int) $exitCode === 0) {
        $httpCode = 200;
    } elseif ((int) $exitCode >= 400 && (int) $exitCode <= 599) {
        $httpCode = (int) $exitCode;
    } elseif ((int) $exitCode === 2) {
        $httpCode = 409;
    } else {
        $httpCode = 400;
    }
    http_response_code($httpCode);
    echo json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

function mars_parse_mode(): string
{
    if (PHP_SAPI === 'cli') {
        global $argv;
        $args = $argv ?? [];
        if (in_array('--dry-run', $args, true)) {
            return 'dry-run';
        }
        if (in_array('--status', $args, true)) {
            return 'status';
        }
        if (in_array('--run', $args, true)) {
            return 'run';
        }
        if (in_array('--enqueue', $args, true)) {
            return 'enqueue';
        }
        return 'dry-run';
    }
    $mode = isset($_GET['mode']) ? (string) $_GET['mode'] : 'dry-run';
    return in_array($mode, ['dry-run', 'status', 'run', 'enqueue'], true) ? $mode : 'dry-run';
}

function mars_lock_status(array $paths): array
{
    $parsed = mars_1c_parse_lock($paths);
    if (empty($parsed['locked'])) {
        return ['locked' => false, 'pid' => null, 'started_at' => null, 'age_seconds' => null, 'run_id' => null, 'phase' => null];
    }
    return $parsed;
}

function mars_acquire_lock(array $paths, string $runId = '', string $trigger = MARS_1C_TRIGGER_SCHEDULED, string $phase = MARS_1C_PHASE_STARTING): bool
{
    $status = mars_lock_status($paths);
    if (!empty($status['locked']) && empty($status['stale'])) {
        // Active lock — reject overlap (do not kill active import).
        return false;
    }
    if (!empty($status['locked']) && !empty($status['stale'])) {
        $alive = mars_1c_process_alive(isset($status['pid']) ? (int) $status['pid'] : null);
        if ($alive) {
            return false; // age exceeded but process still alive — do not steal
        }
        @unlink($paths['lock_file']);
        mars_log($paths, 'warn', 'Removed stale lock after proven inactive process');
    }
    mars_ensure_dir(dirname($paths['lock_file']));
    $payload = mars_1c_lock_payload($paths, $runId !== '' ? $runId : mars_generate_run_id(), $phase, $trigger);
    $fh = fopen($paths['lock_file'], 'c+');
    if ($fh === false) {
        return false;
    }
    if (!flock($fh, LOCK_EX | LOCK_NB)) {
        fclose($fh);
        return false;
    }
    ftruncate($fh, 0);
    fwrite($fh, $payload);
    fflush($fh);
    // Keep lock file; flock released on process end. Also rewrite without holding FH permanently:
    fclose($fh);
    file_put_contents($paths['lock_file'], $payload, LOCK_EX);
    return true;
}

function mars_release_lock(array $paths): void
{
    if (is_file($paths['lock_file'])) {
        @unlink($paths['lock_file']);
    }
}

function mars_tail_log(array $paths, int $lines = 40): array
{
    $file = mars_log_path($paths);
    if (!is_file($file)) {
        return [];
    }
    $content = file($file, FILE_IGNORE_NEW_LINES);
    if ($content === false) {
        return [];
    }
    return array_slice($content, -$lines);
}

function mars_check_legacy_files(array $paths): array
{
    $public = $paths['public_html'];
    $files = [
        'cronjob.php' => $public . '/catalog/controller/common/cronjob.php',
        'cronjob_model.php' => $public . '/catalog/model/catalog/cronjob.php',
        'import_1C.php' => $public . '/catalog/controller/common/import_1C.php',
        'import_1C_offers.php' => $public . '/catalog/controller/common/import_1C_offers.php',
        'import_1C_process.php' => $public . '/catalog/controller/common/import_1C_process.php',
    ];
    $out = [];
    foreach ($files as $name => $path) {
        $out[$name] = ['path' => $path, 'exists' => is_file($path), 'classification' => 'LEGACY SERGEY — READ ONLY'];
    }
    return $out;
}

function mars_check_xml(array $paths): array
{
    $dir = $paths['xml_dir'];
    $import = glob($dir . '/import0_*.xml') ?: [];
    $offers = glob($dir . '/offers0_*.xml') ?: [];
    return [
        'directory' => $dir,
        'exists' => is_dir($dir),
        'import0_count' => count($import),
        'offers0_count' => count($offers),
        'import0_sample' => array_slice(array_map('basename', $import), 0, 5),
        'offers0_sample' => array_slice(array_map('basename', $offers), 0, 5),
    ];
}


function mars_parse_trigger(): string
{
    if (PHP_SAPI === 'cli') {
        global $argv;
        $args = $argv ?? [];
        foreach ($args as $a) {
            if (strpos($a, '--trigger=') === 0) {
                $v = substr($a, strlen('--trigger='));
                if ($v === MARS_1C_TRIGGER_ADMIN_MANUAL) {
                    return MARS_1C_TRIGGER_ADMIN_MANUAL;
                }
            }
        }
        return MARS_1C_TRIGGER_SCHEDULED;
    }
    $t = isset($_REQUEST['trigger']) ? (string) $_REQUEST['trigger'] : MARS_1C_TRIGGER_SCHEDULED;
    return $t === MARS_1C_TRIGGER_ADMIN_MANUAL ? MARS_1C_TRIGGER_ADMIN_MANUAL : MARS_1C_TRIGGER_SCHEDULED;
}

function mars_spawn_background_run(array $paths, string $runId, string $trigger): array
{
    $php = PHP_BINARY ?: 'php';
    $script = $paths['wrapper_path'];
    if (!is_file($script) && is_file(__FILE__)) {
        $script = __FILE__;
    }
    $cmd = escapeshellarg($php) . ' ' . escapeshellarg($script)
        . ' --run --trigger=' . escapeshellarg($trigger)
        . ' --resume-run-id=' . escapeshellarg($runId);
    $log = $paths['log_dir'] . '/background_' . preg_replace('/[^a-zA-Z0-9._-]/', '_', $runId) . '.log';
    mars_ensure_dir($paths['log_dir']);
    if (strncasecmp(PHP_OS, 'WIN', 3) === 0) {
        $full = 'start /B "" ' . $cmd . ' > ' . escapeshellarg($log) . ' 2>&1';
        pclose(popen($full, 'r'));
        return ['ok' => true, 'method' => 'windows_start', 'log' => basename($log)];
    }
    $full = 'nohup ' . $cmd . ' > ' . escapeshellarg($log) . ' 2>&1 & echo $!';
    $pidOut = [];
    $code = 0;
    @exec($full, $pidOut, $code);
    return [
        'ok' => $code === 0,
        'method' => 'nohup',
        'spawn_pid' => isset($pidOut[0]) ? (int) $pidOut[0] : null,
        'log' => basename($log),
    ];
}

function mars_mode_enqueue(array $paths, array $localCfg)
{
    $isCli = PHP_SAPI === 'cli';
    $token = isset($_REQUEST['token']) ? (string) $_REQUEST['token'] : '';
    $tokenOk = $localCfg['run_token'] !== '' && hash_equals($localCfg['run_token'], $token);
    if (!$isCli && (!$localCfg['allow_http_run'] || !$tokenOk)) {
        // Admin path uses OpenCart session — gateway may pass admin_enqueue flag via local include only.
        if (empty($localCfg['allow_admin_enqueue']) || empty($GLOBALS['MARS_1C_ADMIN_ENQUEUE_AUTHORIZED'])) {
            mars_output([
                'operation' => MARS_WRAPPER_OPERATION,
                'mode' => 'enqueue',
                'error' => 'Enqueue denied',
                'mutation' => false,
            ], 403);
        }
    }

    $trigger = mars_parse_trigger();
    if ($trigger !== MARS_1C_TRIGGER_ADMIN_MANUAL) {
        $trigger = MARS_1C_TRIGGER_ADMIN_MANUAL;
    }

    $lock = mars_lock_status($paths);
    if (!empty($lock['locked']) && empty($lock['stale'])) {
        mars_output([
            'operation' => MARS_WRAPPER_OPERATION,
            'mode' => 'enqueue',
            'accepted' => false,
            'error' => 'Импорт уже выполняется',
            'lock' => $lock,
            'current_run' => mars_1c_read_json(mars_1c_current_path($paths)),
            'mutation' => false,
        ], 409);
    }

    $runId = mars_generate_run_id();
    $requestedAt = date('c');
    $state = mars_1c_new_run_state($runId, $trigger, $requestedAt);
    $state['current_phase'] = MARS_1C_PHASE_QUEUED;
    mars_1c_write_run_state($paths, $state);

    if (!mars_acquire_lock($paths, $runId, $trigger, MARS_1C_PHASE_QUEUED)) {
        // Race
        mars_output([
            'operation' => MARS_WRAPPER_OPERATION,
            'mode' => 'enqueue',
            'accepted' => false,
            'error' => 'Импорт уже выполняется',
            'lock' => mars_lock_status($paths),
            'mutation' => false,
        ], 409);
    }

    $spawn = mars_spawn_background_run($paths, $runId, $trigger);
    $state['current_phase'] = MARS_1C_PHASE_STARTING;
    $state['pid'] = $spawn['spawn_pid'] ?? getmypid();
    mars_1c_write_run_state($paths, $state);

    mars_output([
        'operation' => MARS_WRAPPER_OPERATION,
        'mode' => 'enqueue',
        'accepted' => true,
        'run_id' => $runId,
        'trigger_source' => $trigger,
        'ui_status' => 'Ожидает запуска',
        'spawn' => ['ok' => $spawn['ok'], 'method' => $spawn['method']],
        'mutation' => true,
        'note' => 'Background canonical runner started; HTTP returns immediately.',
    ], 0);
}


function mars_mode_dry_run(array $paths, array $localCfg)
{
    $runId = mars_generate_run_id();
    $lockBefore = mars_lock_status($paths);
    $xmlSummary = mars_xml_input_summary($paths);
    $report = mars_report_begin($paths, 'dry-run', $runId);

    $reportPath = $report['finalize']('DRY-RUN ONLY', [
        'lock_before' => $lockBefore,
        'lock_created' => false,
        'lock_removed' => false,
        'step_catalog' => [
            'status' => 'SKIPPED',
            'input_files' => $xmlSummary['catalog'],
            'duration' => '0',
            'errors' => '',
        ],
        'step_offers' => [
            'status' => 'SKIPPED',
            'input_files' => $xmlSummary['offers'],
            'duration' => '0',
            'errors' => '',
        ],
    ]);

    $payload = [
        'operation' => MARS_WRAPPER_OPERATION,
        'version' => MARS_WRAPPER_VERSION,
        'mode' => 'dry-run',
        'mutation' => false,
        'run_id' => $runId,
        'report_file' => $reportPath,
        'legacy_preserved' => true,
        'intended_sequence' => [
            ['step' => 1, 'command' => MARS_CMD_CATALOG, 'legacy' => 'import_1C.php via common/cronjob'],
            ['step' => 2, 'command' => MARS_CMD_OFFERS, 'legacy' => 'import_1C_offers.php via common/cronjob', 'after' => 'catalog success'],
        ],
        'paths' => [
            'lock_file' => $paths['lock_file'],
            'log_dir' => $paths['log_dir'],
            'reports_dir' => $paths['reports_dir'],
            'config_php' => ['path' => $paths['config_php'], 'exists' => is_file($paths['config_php'])],
        ],
        'legacy_files' => mars_check_legacy_files($paths),
        'xml' => mars_check_xml($paths),
        'lock' => mars_lock_status($paths),
        'run_token_configured' => $localCfg['run_token'] !== '',
        'http_run_allowed' => (bool) $localCfg['allow_http_run'],
        'note' => 'Dry-run only — no DB changes, no cronjob route call, no import execution.',
    ];
    mars_output($payload, 0);
}

function mars_mode_status(array $paths)
{
    $runId = mars_generate_run_id();
    $lockBefore = mars_lock_status($paths);
    $report = mars_report_begin($paths, 'status', $runId);

    $reportPath = $report['finalize']('STATUS ONLY', [
        'lock_before' => $lockBefore,
        'lock_created' => false,
        'lock_removed' => false,
        'step_catalog' => [
            'status' => 'NOT RUN',
            'input_files' => [],
            'duration' => 'n/a',
            'errors' => '',
        ],
        'step_offers' => [
            'status' => 'NOT RUN',
            'input_files' => [],
            'duration' => 'n/a',
            'errors' => '',
        ],
    ]);

    $current = mars_1c_read_json(mars_1c_current_path($paths));
    $payload = [
        'operation' => MARS_WRAPPER_OPERATION,
        'mode' => 'status',
        'mutation' => false,
        'run_id' => $runId,
        'report_file' => $reportPath,
        'lock' => mars_lock_status($paths),
        'current_run' => $current,
        'last_log_lines' => mars_tail_log($paths),
        'log_file' => is_file(mars_log_path($paths)) ? mars_log_path($paths) : null,
        'reports_dir' => $paths['reports_dir'],
    ];
    mars_output($payload, 0);
}

function mars_bootstrap_db(array $paths)
{
    if (!is_file($paths['config_php'])) {
        throw new RuntimeException('config.php not found — cannot bootstrap DB');
    }
    require_once $paths['config_php'];
    require_once DIR_SYSTEM . 'startup.php';
    $registry = new Registry();
    $db = new DB(DB_DRIVER, DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_PORT);
    $registry->set('db', $db);
    return $db;
}

function mars_read_cron_active($db, string $command): string
{
    $command = $db->escape($command);
    $query = $db->query("SELECT `active` FROM `cron` WHERE `command` = '" . $command . "' LIMIT 1");
    if (!$query->num_rows) {
        return 'NOT FOUND';
    }
    return (int) $query->row['active'] === 1 ? '1' : '0';
}

function mars_set_cron_active($db, string $command, int $active): void
{
    $command = $db->escape($command);
    if ($active === 1) {
        $db->query("UPDATE `cron` SET `active` = 0");
        $db->query("UPDATE `cron` SET `active` = 1 WHERE `command` = '" . $command . "'");
    } else {
        $db->query("UPDATE `cron` SET `active` = 0 WHERE `command` = '" . $command . "'");
    }
}

function mars_invoke_cronjob_http(string $baseUrl): array
{
    $url = rtrim($baseUrl, '/') . '/index.php?route=common/cronjob';
    $ctx = stream_context_create([
        'http' => [
            'timeout' => MARS_MAX_RUNTIME_SECONDS,
            'ignore_errors' => true,
            'header' => "User-Agent: MARS-1C-Wrapper/" . MARS_WRAPPER_VERSION . "\r\n",
        ],
    ]);
    $body = @file_get_contents($url, false, $ctx);
    $status = 0;
    if (isset($http_response_header[0]) && preg_match('/\s(\d{3})\s/', $http_response_header[0], $m)) {
        $status = (int) $m[1];
    }
    return [
        'url' => $url,
        'http_status' => $status,
        'body_preview' => is_string($body) ? mb_substr(strip_tags($body), 0, 500) : '',
        'ok' => is_string($body) && $body !== '',
    ];
}

function mars_mode_run(array $paths, array $localCfg)
{
    $isCli = PHP_SAPI === 'cli';
    $token = isset($_GET['token']) ? (string) $_GET['token'] : '';
    $tokenOk = $localCfg['run_token'] !== '' && hash_equals($localCfg['run_token'], $token);

    if (!$isCli && (!$localCfg['allow_http_run'] || !$tokenOk)) {
        mars_output([
            'operation' => MARS_WRAPPER_OPERATION,
            'mode' => 'run',
            'error' => 'HTTP run denied — configure mars_1c_wrapper.local.php (run_token, allow_http_run) or use CLI.',
            'mutation' => false,
        ], 403);
    }

    if ($isCli && $localCfg['run_token'] === '' && getenv('MARS_1C_WRAPPER_ALLOW_CLI_RUN') !== '1') {
        mars_output([
            'operation' => MARS_WRAPPER_OPERATION,
            'mode' => 'run',
            'error' => 'CLI run blocked — set run_token in local config or export MARS_1C_WRAPPER_ALLOW_CLI_RUN=1 after operator approval.',
            'mutation' => false,
        ], 403);
    }

    $trigger = mars_parse_trigger();
    $resumeId = null;
    if (PHP_SAPI === 'cli') {
        global $argv;
        foreach (($argv ?? []) as $a) {
            if (strpos($a, '--resume-run-id=') === 0) {
                $resumeId = substr($a, strlen('--resume-run-id='));
            }
        }
    } elseif (isset($_REQUEST['resume_run_id'])) {
        $resumeId = (string) $_REQUEST['resume_run_id'];
    }

    $existingLock = mars_lock_status($paths);
    $runId = $resumeId ?: mars_generate_run_id();
    // If enqueue already holds lock for this run_id, continue; else acquire.
    $needAcquire = true;
    if (!empty($existingLock['locked']) && empty($existingLock['stale']) && ($existingLock['run_id'] ?? null) === $runId) {
        $needAcquire = false;
    }
    if ($needAcquire && !mars_acquire_lock($paths, $runId, $trigger, MARS_1C_PHASE_STARTING)) {
        mars_output([
            'operation' => MARS_WRAPPER_OPERATION,
            'mode' => 'run',
            'error' => 'Импорт уже выполняетсяИмпорт уже выполняется => mars_lock_status($paths),
            'current_run' => mars_1c_read_json(mars_1c_current_path($paths)),
            'mutation' => false,
        ], 409);
    }

    $lockBefore = mars_lock_status($paths);
    $xmlSummary = mars_xml_input_summary($paths);
    $started = microtime(true);
    $requestedAt = date('c');
    $state = mars_1c_read_json(mars_1c_run_dir($paths, $runId) . '/run-state.json');
    if (!$state) {
        $state = mars_1c_new_run_state($runId, $trigger, $requestedAt);
    }
    $state['started_at'] = date('c');
    $state['current_phase'] = MARS_1C_PHASE_STARTING;
    $state['pid'] = getmypid();
    $state['log_reference'] = 'logs/mars_1c_import_' . date('Ymd') . '.log';
    $state['catalog_input_inventory'] = $xmlSummary['catalog'];
    $state['offers_input_inventory'] = $xmlSummary['offers'];
    mars_1c_write_run_state($paths, $state);
    mars_log($paths, 'info', 'Run mode started run_id=' . $runId . ' trigger=' . $trigger);
    $steps = [];
    $dbFlags = [
        '1c_before' => 'NOT READ',
        '1c_after' => 'NOT READ',
        '1c_offers_before' => 'NOT READ',
        '1c_offers_after' => 'NOT READ',
    ];
    $stepCatalog = [
        'status' => 'NOT RUN',
        'input_files' => $xmlSummary['catalog'],
        'duration' => '0',
        'errors' => '',
    ];
    $stepOffers = [
        'status' => 'SKIPPED',
        'input_files' => $xmlSummary['offers'],
        'duration' => '0',
        'errors' => '',
    ];
    $finalStatus = 'FAILED';
    $reportPath = null;

    try {
        $db = mars_bootstrap_db($paths);
        $dbFlags['1c_before'] = mars_read_cron_active($db, MARS_CMD_CATALOG);
        $dbFlags['1c_offers_before'] = mars_read_cron_active($db, MARS_CMD_OFFERS);

        $state['current_phase'] = MARS_1C_PHASE_CATALOG;
        mars_1c_write_run_state($paths, $state);
        mars_log($paths, 'info', 'Step 1 — activate command ' . MARS_CMD_CATALOG);
        $step1Start = microtime(true);
        mars_set_cron_active($db, MARS_CMD_CATALOG, 1);
        $step1 = mars_invoke_cronjob_http($localCfg['site_base_url']);
        mars_set_cron_active($db, MARS_CMD_CATALOG, 0);
        $dbFlags['1c_after'] = mars_read_cron_active($db, MARS_CMD_CATALOG);
        $steps['catalog'] = $step1;
        $stepCatalog = [
            'status' => $step1['ok'] ? 'PASS' : 'FAIL',
            'input_files' => $xmlSummary['catalog'],
            'duration' => (string) round(microtime(true) - $step1Start, 2) . ' seconds',
            'errors' => $step1['ok'] ? '' : 'HTTP ' . ($step1['http_status'] ?? 0),
        ];
        mars_log($paths, 'info', 'Step 1 complete — HTTP ' . ($step1['http_status'] ?? 0));

        if (!$step1['ok']) {
            throw new RuntimeException('Catalog import step failed or returned empty response');
        }

        $state['current_phase'] = MARS_1C_PHASE_OFFERS;
        mars_1c_write_run_state($paths, $state);
        mars_log($paths, 'info', 'Step 2 — activate command ' . MARS_CMD_OFFERS);
        $step2Start = microtime(true);
        mars_set_cron_active($db, MARS_CMD_OFFERS, 1);
        $step2 = mars_invoke_cronjob_http($localCfg['site_base_url']);
        mars_set_cron_active($db, MARS_CMD_OFFERS, 0);
        $dbFlags['1c_offers_after'] = mars_read_cron_active($db, MARS_CMD_OFFERS);
        $steps['offers'] = $step2;
        $stepOffers = [
            'status' => $step2['ok'] ? 'PASS' : 'FAIL',
            'input_files' => $xmlSummary['offers'],
            'duration' => (string) round(microtime(true) - $step2Start, 2) . ' seconds',
            'errors' => $step2['ok'] ? '' : 'HTTP ' . ($step2['http_status'] ?? 0),
        ];
        mars_log($paths, 'info', 'Step 2 complete — HTTP ' . ($step2['http_status'] ?? 0));

        if (!$step2['ok']) {
            throw new RuntimeException('Offers import step failed or returned empty response');
        }

        $class = mars_1c_classify_terminal($stepCatalog, $stepOffers, $xmlSummary, false, null);
        $finalStatus = $class['final_status'];
        mars_log($paths, 'info', 'Run mode finished classification=' . $finalStatus);
        $runDurationSeconds = round(microtime(true) - $started, 2);
        $completedAt = date('c');

        $state['catalog_phase_result'] = $stepCatalog;
        $state['offers_phase_result'] = $stepOffers;
        $state['sanitized_error_summary'] = $class['sanitized_error_summary'];
        $state['final_status'] = $finalStatus;
        $state['completed_at'] = $completedAt;
        $state['current_phase'] = MARS_1C_PHASE_TERMINAL;

        $terminal = [
            'schema_version' => MARS_1C_RUN_SCHEMA_VERSION,
            'site_id' => MARS_1C_SITE_ID,
            'run_id' => $runId,
            'trigger_source' => $trigger,
            'started_at' => $state['started_at'],
            'completed_at' => $completedAt,
            'duration_seconds' => $runDurationSeconds,
            'final_status' => $finalStatus,
            'report_class' => $class['report_class'],
            'summary_code' => $class['summary_code'],
            'catalog_phase_result' => $stepCatalog,
            'offers_phase_result' => $stepOffers,
            'catalog_input_inventory' => $xmlSummary['catalog'],
            'offers_input_inventory' => $xmlSummary['offers'],
            'sanitized_error_summary' => $class['sanitized_error_summary'],
            'log_reference' => $state['log_reference'],
        ];
        mars_1c_write_terminal($paths, $state, $terminal);

        $report = mars_report_begin($paths, 'run', $runId, $started);
        $reportPath = $report['finalize']($finalStatus, [
            'lock_before' => $lockBefore,
            'lock_created' => true,
            'lock_removed' => true,
            'step_catalog' => $stepCatalog,
            'step_offers' => $stepOffers,
            'db_flags' => $dbFlags,
            'duration_seconds' => $runDurationSeconds,
        ]);
        $state['txt_report_path'] = $reportPath ? basename((string) $reportPath) : null;

        $state['current_phase'] = MARS_1C_PHASE_DISPATCH;
        $state['report_dispatch_status'] = 'PENDING';
        mars_1c_write_run_state($paths, $state);
        mars_1c_enqueue_dispatch($paths, $runId);
        $state['report_dispatch_status'] = 'QUEUED';
        $state['report_dispatch_at'] = date('c');
        $state['current_phase'] = MARS_1C_PHASE_DONE;
        mars_1c_write_run_state($paths, $state);

        mars_release_lock($paths);

        mars_output([
            'operation' => MARS_WRAPPER_OPERATION,
            'mode' => 'run',
            'mutation' => true,
            'run_id' => $runId,
            'trigger_source' => $trigger,
            'final_status' => $finalStatus,
            'report_class' => $class['report_class'],
            'report_file' => $reportPath,
            'duration_seconds' => $runDurationSeconds,
            'steps' => $steps,
            'dispatch' => 'QUEUED',
            'legacy_preserved' => true,
            'note' => 'Canonical runner terminal result written; completion dispatch queued.',
        ], 0);
    } catch (Throwable $e) {
        mars_log($paths, 'error', $e->getMessage());
        try {
            if (isset($db)) {
                $db->query('UPDATE `cron` SET `active` = 0');
                $dbFlags['1c_after'] = mars_read_cron_active($db, MARS_CMD_CATALOG);
                $dbFlags['1c_offers_after'] = mars_read_cron_active($db, MARS_CMD_OFFERS);
            }
        } catch (Throwable $ignored) {
        }
        if ($stepCatalog['status'] === 'NOT RUN') {
            $stepCatalog['status'] = 'FAIL';
            $stepCatalog['errors'] = $e->getMessage();
        }
        if ($stepOffers['status'] === 'SKIPPED' && !empty($steps['catalog']) && $steps['catalog']['ok']) {
            $stepOffers['status'] = 'NOT RUN';
        } elseif ($stepOffers['status'] === 'SKIPPED') {
            $stepOffers['status'] = 'SKIPPED';
        }
        $class = mars_1c_classify_terminal($stepCatalog, $stepOffers, $xmlSummary, true, $e->getMessage());
        $finalStatus = $class['final_status'];
        $runDurationSeconds = round(microtime(true) - $started, 2);
        $completedAt = date('c');
        if (!isset($state) || !is_array($state)) {
            $state = mars_1c_new_run_state($runId, $trigger ?? MARS_1C_TRIGGER_SCHEDULED, date('c'));
        }
        $state['catalog_phase_result'] = $stepCatalog;
        $state['offers_phase_result'] = $stepOffers;
        $state['sanitized_error_summary'] = $class['sanitized_error_summary'];
        $state['final_status'] = $finalStatus;
        $state['completed_at'] = $completedAt;
        $terminal = [
            'schema_version' => MARS_1C_RUN_SCHEMA_VERSION,
            'site_id' => MARS_1C_SITE_ID,
            'run_id' => $runId,
            'trigger_source' => $trigger ?? MARS_1C_TRIGGER_SCHEDULED,
            'started_at' => $state['started_at'] ?? null,
            'completed_at' => $completedAt,
            'duration_seconds' => $runDurationSeconds,
            'final_status' => $finalStatus,
            'report_class' => $class['report_class'],
            'summary_code' => $class['summary_code'],
            'catalog_phase_result' => $stepCatalog,
            'offers_phase_result' => $stepOffers,
            'catalog_input_inventory' => $xmlSummary['catalog'] ?? [],
            'offers_input_inventory' => $xmlSummary['offers'] ?? [],
            'sanitized_error_summary' => $class['sanitized_error_summary'],
            'log_reference' => $state['log_reference'] ?? null,
        ];
        mars_1c_write_terminal($paths, $state, $terminal);

        $report = mars_report_begin($paths, 'run', $runId, $started);
        $reportPath = $report['finalize']($finalStatus, [
            'lock_before' => $lockBefore,
            'lock_created' => true,
            'lock_removed' => true,
            'step_catalog' => $stepCatalog,
            'step_offers' => $stepOffers,
            'db_flags' => $dbFlags,
            'duration_seconds' => $runDurationSeconds,
        ]);
        $state['txt_report_path'] = $reportPath ? basename((string) $reportPath) : null;
        $state['report_dispatch_status'] = 'PENDING';
        mars_1c_write_run_state($paths, $state);
        mars_1c_enqueue_dispatch($paths, $runId);
        $state['report_dispatch_status'] = 'QUEUED';
        $state['report_dispatch_at'] = date('c');
        $state['current_phase'] = MARS_1C_PHASE_DONE;
        mars_1c_write_run_state($paths, $state);
        mars_release_lock($paths);

        mars_output([
            'operation' => MARS_WRAPPER_OPERATION,
            'mode' => 'run',
            'mutation' => true,
            'run_id' => $runId,
            'final_status' => $finalStatus,
            'report_file' => $reportPath,
            'error' => mars_1c_sanitize_error($e->getMessage()),
            'steps' => $steps,
            'duration_seconds' => $runDurationSeconds,
            'dispatch' => 'QUEUED',
        ], 1);
    }
}

// --- entry ---
$paths = mars_paths();
$localCfg = mars_load_local_config($paths);
$mode = mars_parse_mode();

switch ($mode) {
    case 'status':
        mars_mode_status($paths);
        break;
    case 'enqueue':
        mars_mode_enqueue($paths, $localCfg);
        break;
    case 'run':
        mars_mode_run($paths, $localCfg);
        break;
    case 'dry-run':
    default:
        mars_mode_dry_run($paths, $localCfg);
        break;
}

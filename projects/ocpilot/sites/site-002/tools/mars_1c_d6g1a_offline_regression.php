<?php
/**
 * Phase 1B-D6G1A offline/sandbox regression (no production webhook).
 * Usage: php mars_1c_d6g1a_offline_regression.php
 */
declare(strict_types=1);

require_once __DIR__ . '/mars_1c_import_run_contract.php';
require_once __DIR__ . '/mars_1c_completion_dispatch.php';

$results = [];
$pass = static function (string $id, bool $ok, array $detail = []) use (&$results): void {
    $results[] = ['id' => $id, 'pass' => $ok, 'detail' => $detail];
};

$pass('R_kill_true_enabled', mars_1c_client_ops_dispatch_enabled(['CLIENT_OPS_DISPATCH_ENABLED' => true]) === true);
$pass('R_kill_false_blocks', mars_1c_client_ops_dispatch_enabled(['CLIENT_OPS_DISPATCH_ENABLED' => false]) === false);
$pass('R_kill_alias_server_dispatch', mars_1c_client_ops_dispatch_enabled(['server_dispatch_enabled' => false]) === false);
$pass('R_kill_default_true', mars_1c_client_ops_dispatch_enabled([]) === true);
$pass(
    'R_ui_blocked_label',
    mars_1c_dispatch_ui_label(MARS_1C_DISPATCH_BLOCKED_KILL_SWITCH) === 'Отключено (kill switch)'
);

$sandbox = sys_get_temp_dir() . '/mars-d6g1a-' . bin2hex(random_bytes(4));
$runId = 'mars-20990101-sandbox-deadbeef';
@mkdir($sandbox . '/mars-tools/cron/runs/' . $runId, 0777, true);
@mkdir($sandbox . '/mars-tools/cron/dispatch-state', 0777, true);
@mkdir($sandbox . '/mars-tools/cron/watchdog-state', 0777, true);

$paths = [
    'storage' => $sandbox,
    'runs_dir' => $sandbox . '/mars-tools/cron/runs',
    'current_run' => $sandbox . '/mars-tools/cron/current-run.json',
    'watchdog_state' => $sandbox . '/mars-tools/cron/watchdog-state',
    'log_dir' => $sandbox . '/mars-tools/cron/logs',
    'local_config' => $sandbox . '/mars-tools/cron/local.php',
];

$terminal = [
    'run_id' => $runId,
    'final_status' => 'ATTENTION_OFFERS_INPUT_MISSING',
    'summary_code' => 'OFFERS_INPUT_MISSING',
    'completed_at' => '2099-01-01T12:00:00+07:00',
    'started_at' => '2099-01-01T11:59:00+07:00',
    'trigger_source' => 'SCHEDULED',
];
mars_1c_atomic_write_json(mars_1c_run_dir($paths, $runId) . '/terminal.json', $terminal);

$cfgOff = [
    'CLIENT_OPS_DISPATCH_ENABLED' => false,
    'client_ops_webhook_url' => 'https://example.invalid/webhook',
    'client_ops_webhook_auth_secret' => 'test-secret-not-real',
];
$blocked = mars_1c_server_dispatch_completion($paths, $cfgOff, $runId, $terminal);
$pass('R12_kill_false_blocks_webhook', ($blocked['status'] ?? '') === MARS_1C_DISPATCH_BLOCKED_KILL_SWITCH
    && ($blocked['reason'] ?? '') === 'BLOCKED_BY_KILL_SWITCH'
    && empty($blocked['http_status']));
$pass('R13_terminal_still_present', is_file(mars_1c_run_dir($paths, $runId) . '/terminal.json'));

$cfgOn = $cfgOff;
$cfgOn['CLIENT_OPS_DISPATCH_ENABLED'] = true;
// Without real webhook this becomes FAILED_RETRYABLE / transport — but must NOT be kill-switch blocked.
$attempt = mars_1c_server_dispatch_completion($paths, $cfgOn, $runId, $terminal);
$pass(
    'R11_kill_true_eligible_not_blocked',
    ($attempt['status'] ?? '') !== MARS_1C_DISPATCH_BLOCKED_KILL_SWITCH
    && ($attempt['reason'] ?? '') !== 'BLOCKED_BY_KILL_SWITCH'
);

// Simulate delivered marker then re-dispatch => ALREADY
mars_1c_atomic_write_json(mars_1c_dispatch_delivered_path($paths, $runId), [
    'status' => MARS_1C_DISPATCH_SENT,
    'event_id' => 'sandbox-event',
    'http_status' => 202,
]);
$again = mars_1c_server_dispatch_completion($paths, $cfgOn, $runId, $terminal);
$pass('R15_recovery_idempotent_already', !empty($again['duplicate']) || ($again['status'] ?? '') === MARS_1C_DISPATCH_ALREADY);

// Watchdog missing-run fixture (inline logic mirror, no HTTP)
$eventDates = ['2099-02-01', '2099-02-01', '2099-02-02'];
$events = [];
foreach ($eventDates as $d) {
    $marker = $paths['watchdog_state'] . '/' . $d . '.sent.json';
    $eventId = 'site002-no-fresh-import-' . $d;
    if (is_file($marker)) {
        $events[] = ['date' => $d, 'action' => 'DEDUPED', 'event_id' => $eventId];
        continue;
    }
    mars_1c_atomic_write_json($marker, ['event_id' => $eventId, 'ok' => true]);
    $events[] = ['date' => $d, 'action' => 'CREATED', 'event_id' => $eventId];
}
$pass('R5_missing_creates_one', $events[0]['action'] === 'CREATED');
$pass('R6_same_date_dedupes', $events[1]['action'] === 'DEDUPED' && $events[0]['event_id'] === $events[1]['event_id']);
$pass('R7_next_day_new_event', $events[2]['action'] === 'CREATED' && $events[2]['event_id'] !== $events[0]['event_id']);

$allPass = true;
foreach ($results as $r) {
    if (empty($r['pass'])) {
        $allPass = false;
        break;
    }
}

echo json_encode([
    'phase' => '1B-D6G1A',
    'check' => 'offline-regression',
    'pass' => $allPass,
    'results' => $results,
    'sandbox' => $sandbox,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";

exit($allPass ? 0 : 1);

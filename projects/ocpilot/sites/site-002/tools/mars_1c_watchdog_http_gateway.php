<?php
/**
 * MARS SITE-002 — HTTP gateway for server-side no-import watchdog.
 * Requires token matching mars_1c_wrapper.local.php run_token.
 */
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

$local = realpath(__DIR__ . '/../../../storage/mars-tools/cron/mars_1c_wrapper.local.php');
$watchdog = realpath(__DIR__ . '/../../../storage/mars-tools/cron/mars_1c_no_import_watchdog.php');
if ($local === false || $watchdog === false) {
    http_response_code(503);
    echo json_encode(['ok' => false, 'error' => 'watchdog not deployed'], JSON_UNESCAPED_UNICODE);
    exit;
}

/** @noinspection PhpIncludeInspection */
$cfg = include $local;
$tokenCfg = is_array($cfg) ? (string) ($cfg['run_token'] ?? '') : '';
$token = isset($_REQUEST['token']) ? (string) $_REQUEST['token'] : '';
if ($tokenCfg === '' || $token === '' || !hash_equals($tokenCfg, $token)) {
    http_response_code(403);
    echo json_encode(['ok' => false, 'error' => 'denied'], JSON_UNESCAPED_UNICODE);
    exit;
}

ob_start();
/** @noinspection PhpIncludeInspection */
require $watchdog;
$out = ob_get_clean();
echo $out !== '' ? $out : json_encode(['ok' => false, 'error' => 'empty watchdog output'], JSON_UNESCAPED_UNICODE);

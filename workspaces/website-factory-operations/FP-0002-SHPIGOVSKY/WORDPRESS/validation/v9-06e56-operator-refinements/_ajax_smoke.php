<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.test';
$_SERVER['REQUEST_METHOD'] = 'POST';
$_SERVER['REMOTE_ADDR'] = '127.0.0.1';
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$nonce = wp_create_nonce('fp02_lead_submit');
$started = time() - 5;
$token = wp_generate_password(32, false, false);

$_POST = array(
  'action' => 'fp02_lead_submit',
  'fp02_lead_nonce' => $nonce,
  'name' => 'Тест Локальный',
  'phone' => '+7 925 183-64-64',
  'message' => 'Проверка локального обработчика форм E56',
  'consent' => '1',
  'company_url' => '',
  'form_started_at' => (string) $started,
  'timestamp' => (string) time(),
  'request_token' => $token,
  'form_context' => 'final',
  'lead_source' => 'e56-smoke',
  'page_url' => home_url('/'),
  'page_title' => 'Smoke',
);

ob_start();
try {
  do_action('wp_ajax_nopriv_fp02_lead_submit');
  $buf = ob_get_clean();
} catch (Throwable $e) {
  $buf = ob_get_clean();
  $buf .= ' EXCEPTION: ' . $e->getMessage();
}

$uploads = wp_upload_dir();
$logDir = trailingslashit($uploads['basedir']) . 'fp02-leads-local';
$files = is_dir($logDir) ? glob($logDir . '/receipt-*.json') : array();
$latest = $files ? max($files) : '';

$result = array(
  'raw' => $buf,
  'json' => json_decode($buf, true),
  'module_enabled' => \Shpigovsky\Core\ModuleRegistry::is_enabled('forms.consultation'),
  'receipt_dir' => $logDir,
  'latest_receipt' => $latest ? basename($latest) : null,
  'htaccess' => is_file($logDir . '/.htaccess'),
);

file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e56-operator-refinements/lead-ajax-smoke.json', json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT));
echo json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT), PHP_EOL;

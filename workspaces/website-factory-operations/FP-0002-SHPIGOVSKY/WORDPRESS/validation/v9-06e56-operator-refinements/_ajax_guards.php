<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.test';
$_SERVER['REQUEST_METHOD'] = 'POST';
$_SERVER['REMOTE_ADDR'] = '127.0.0.1';
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

function fp02_run_lead($post) {
  $_POST = $post;
  ob_start();
  try { do_action('wp_ajax_nopriv_fp02_lead_submit'); } catch (Throwable $e) {}
  $buf = ob_get_clean();
  return json_decode($buf, true) ?: array('raw'=>$buf);
}

$nonce = wp_create_nonce('fp02_lead_submit');
$token = 'dup' . wp_generate_password(28, false, false);
$base = array(
  'action' => 'fp02_lead_submit',
  'fp02_lead_nonce' => $nonce,
  'name' => 'Дубль',
  'phone' => '+7 925 111-22-33',
  'message' => 'Проверка дубликата',
  'consent' => '1',
  'company_url' => '',
  'form_started_at' => (string) (time() - 5),
  'timestamp' => (string) time(),
  'request_token' => $token,
  'form_context' => 'modal',
  'lead_source' => 'e56-dup',
);

$first = fp02_run_lead($base);
$second = fp02_run_lead($base);

$honey = $base;
$honey['request_token'] = 'hp' . wp_generate_password(28, false, false);
$honey['company_url'] = 'http://spam.example';
$honeypot = fp02_run_lead($honey);

$out = compact('first','second','honeypot');
file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e56-operator-refinements/lead-ajax-guards.json', json_encode($out, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT));
echo json_encode($out, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT), PHP_EOL;

// Confirm recipient constant not in public theme markup paths
$theme = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky';
$hits = array();
foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator($theme)) as $f) {
  if (!$f->isFile()) continue;
  $ext = strtolower($f->getExtension());
  if (!in_array($ext, array('php','js','css','html'), true)) continue;
  $c = @file_get_contents($f->getPathname());
  if ($c !== false && strpos($c, 'client.leads@polygon-ws.ru') !== false) {
    $hits[] = $f->getPathname();
  }
}
echo 'public_recipient_hits=' . count($hits) . PHP_EOL;

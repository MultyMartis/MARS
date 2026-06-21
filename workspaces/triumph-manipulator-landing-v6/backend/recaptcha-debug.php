<?php
/**
 * Temporary reCAPTCHA config diagnostic (no secrets).
 * Remove from production after troubleshooting.
 */

require_once __DIR__ . '/lib/config-loader.php';

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');

$localPath = __DIR__ . '/config.local.php';
$configLocalExists = is_file($localPath);

$config = [];
$siteConfigLoaderOk = 'no';

try {
    $config = triumph_load_config();
    $siteConfigLoaderOk = 'yes';
} catch (Throwable $e) {
    $siteConfigLoaderOk = 'no';
}

$siteKey = trim((string) ($config['recaptcha_site_key'] ?? ''));
$secretKey = trim((string) ($config['recaptcha_secret_key'] ?? ''));

echo json_encode(
    [
        'config_local_file_exists' => $configLocalExists ? 'yes' : 'no',
        'site_key_present' => ($siteKey !== '' && $siteKey !== 'PASTE_SITE_KEY_HERE') ? 'yes' : 'no',
        'secret_key_present' => ($secretKey !== '' && $secretKey !== 'PASTE_SECRET_KEY_HERE') ? 'yes' : 'no',
        'site_config_loader_ok' => $siteConfigLoaderOk,
        'recaptcha_lib_exists' => is_file(__DIR__ . '/lib/recaptcha.php') ? 'yes' : 'no',
        'host' => (string) ($_SERVER['HTTP_HOST'] ?? $_SERVER['SERVER_NAME'] ?? ''),
        'php_version' => PHP_VERSION,
        'note' => 'Temporary diagnostic only. Remove after troubleshooting.',
    ],
    JSON_UNESCAPED_UNICODE
);

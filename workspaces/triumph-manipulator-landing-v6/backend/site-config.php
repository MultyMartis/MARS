<?php

declare(strict_types=1);

/**
 * Public site config for frontend (no secrets).
 */

require_once __DIR__ . '/lib/config-loader.php';

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');

$config = triumph_load_config();
$siteKey = trim((string) ($config['recaptcha_site_key'] ?? ''));

echo json_encode(
    [
        'recaptchaSiteKey' => $siteKey,
    ],
    JSON_UNESCAPED_UNICODE
);

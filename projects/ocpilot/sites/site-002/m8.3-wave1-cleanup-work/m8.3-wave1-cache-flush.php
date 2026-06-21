<?php
// BZPM M8.3 Wave 1 — one-shot file cache flush (TEST only).
$token = 'm8.3-wave1-cache-flush-20260615';
if (!isset($_GET['token']) || $_GET['token'] !== $token) {
    http_response_code(403);
    exit('forbidden');
}

require_once __DIR__ . '/config.php';

$cleared = [];
$errors = [];
$dirs = [];
if (defined('DIR_CACHE')) {
    $dirs[] = rtrim(DIR_CACHE, '/\\') . '/';
}
$dirs[] = __DIR__ . '/system/storage/cache/';

foreach (array_unique($dirs) as $cacheDir) {
    if (!is_dir($cacheDir)) {
        continue;
    }
    foreach (glob($cacheDir . 'cache.*') as $file) {
        if (is_file($file)) {
            if (@unlink($file)) {
                $cleared[] = $file;
            } else {
                $errors[] = $file;
            }
        }
    }
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode([
    'ok' => true,
    'dirs' => $dirs,
    'cleared_count' => count($cleared),
    'cleared_sample' => array_slice($cleared, 0, 30),
    'errors' => $errors,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

@unlink(__FILE__);

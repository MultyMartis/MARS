<?php
declare(strict_types=1);

/**
 * i-SEO Report Hub — Phase 1A front controller.
 * No DB. No .env required. Source-only skeleton.
 */

// When used as PHP built-in server router, serve existing public files as-is.
if (PHP_SAPI === 'cli-server') {
    $reqPath = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);
    if (is_string($reqPath) && $reqPath !== '/' && $reqPath !== '') {
        $candidate = __DIR__ . str_replace('/', DIRECTORY_SEPARATOR, $reqPath);
        if (is_file($candidate)) {
            return false;
        }
    }
}

try {
    /** @var array<string, mixed> $app */
    $app = require dirname(__DIR__) . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . 'bootstrap.php';
    require $app['app_path'] . DIRECTORY_SEPARATOR . 'routes.php';

    /** @var \Iseo\Support\Router $router */
    $router = $app['router'];
    $router->dispatch(request_method(), request_path());
} catch (Throwable $e) {
    $debug = true;
    if (isset($app) && is_array($app) && isset($app['config']) && $app['config'] instanceof \Iseo\Services\ConfigService) {
        $debug = $app['config']->debug();
    }

    http_response_code(500);
    header('Content-Type: text/html; charset=UTF-8');

    if ($debug) {
        $message = htmlspecialchars($e->getMessage(), ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
        $file = htmlspecialchars($e->getFile(), ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
        $line = (int) $e->getLine();
        echo '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Error</title></head><body>';
        echo '<h1>Application error</h1>';
        echo '<p>Phase 1A debug view — no secrets intentionally shown.</p>';
        echo '<p><strong>Message:</strong> ' . $message . '</p>';
        echo '<p><strong>File:</strong> ' . $file . ' <strong>Line:</strong> ' . $line . '</p>';
        echo '</body></html>';
        return;
    }

    echo '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Error</title></head><body>';
    echo '<h1>Something went wrong</h1>';
    echo '<p>Safe error page. Details hidden because APP_DEBUG is false.</p>';
    echo '</body></html>';
}

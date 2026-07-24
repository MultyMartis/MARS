<?php
declare(strict_types=1);

/**
 * i-SEO Report Hub — Phase 1A health entrypoint.
 * Uses bootstrap. No DB connection.
 */

try {
    /** @var array<string, mixed> $app */
    $app = require dirname(__DIR__) . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . 'bootstrap.php';

    $health = new \Iseo\Controllers\HealthController(
        $app,
        $app['view'],
        $app['config'],
        $app['auth'],
        $app['csrf']
    );
    $health->index();
} catch (Throwable $e) {
    http_response_code(500);
    header('Content-Type: text/plain; charset=UTF-8');
    echo "Health bootstrap failed.\n";
    echo 'PHP ' . PHP_VERSION . "\n";
    echo 'DB not configured / not tested in Phase 1A' . "\n";
    if (getenv('APP_DEBUG') === 'true' || getenv('APP_DEBUG') === '1') {
        echo $e->getMessage() . "\n";
    }
}

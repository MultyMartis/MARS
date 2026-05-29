<?php

declare(strict_types=1);

/**
 * Load merged mailer / site config (config.php + optional config.local.php).
 *
 * @return array<string, mixed>
 */
function triumph_load_config(): array
{
    $baseDir = dirname(__DIR__);
    $configPath = $baseDir . '/config.php';
    $localPath = $baseDir . '/config.local.php';

    if (!is_file($configPath)) {
        return [];
    }

    /** @var array<string, mixed> $config */
    $config = require $configPath;

    if (is_file($localPath)) {
        /** @var array<string, mixed> $local */
        $local = require $localPath;
        $config = array_merge($config, $local);
    }

    return $config;
}

function triumph_is_production_host(): bool
{
    $host = strtolower((string) ($_SERVER['HTTP_HOST'] ?? $_SERVER['SERVER_NAME'] ?? ''));

    return $host !== '' && str_contains($host, 'manipulator-triumph.ru');
}

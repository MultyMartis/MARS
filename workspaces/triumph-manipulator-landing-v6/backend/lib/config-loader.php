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
        $config = triumph_merge_config($config, $local);
    }

    return $config;
}

/**
 * @param array<string, mixed> $base
 * @param array<string, mixed> $override
 * @return array<string, mixed>
 */
function triumph_merge_config(array $base, array $override): array
{
    foreach ($override as $key => $value) {
        if (
            is_array($value)
            && isset($base[$key])
            && is_array($base[$key])
            && triumph_is_assoc_array($base[$key])
            && triumph_is_assoc_array($value)
        ) {
            /** @var array<string, mixed> $baseChild */
            $baseChild = $base[$key];
            /** @var array<string, mixed> $overrideChild */
            $overrideChild = $value;
            $base[$key] = triumph_merge_config($baseChild, $overrideChild);
            continue;
        }

        $base[$key] = $value;
    }

    return $base;
}

/**
 * @param array<mixed> $array
 */
function triumph_is_assoc_array(array $array): bool
{
    if ($array === []) {
        return true;
    }

    return array_keys($array) !== range(0, count($array) - 1);
}

function triumph_is_production_host(): bool
{
    $host = strtolower((string) ($_SERVER['HTTP_HOST'] ?? $_SERVER['SERVER_NAME'] ?? ''));

    return $host !== '' && str_contains($host, 'manipulator-triumph.ru');
}

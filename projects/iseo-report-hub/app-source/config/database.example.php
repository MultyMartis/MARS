<?php
declare(strict_types=1);

/**
 * Example database config — placeholders / env lookup examples only.
 * Not loaded by Phase 0 pages. No real credentials. No connection attempted.
 *
 * Future Phase 1+ may read getenv() / a local .env loader.
 */
return [
    'driver' => 'mysql',
    'host' => getenv('DB_HOST') ?: '127.0.0.1',
    'port' => (int) (getenv('DB_PORT') ?: 3306),
    'database' => getenv('DB_DATABASE') ?: 'iseo_report_hub_dev',
    'username' => getenv('DB_USERNAME') ?: 'CHANGE_ME',
    'password' => getenv('DB_PASSWORD') ?: 'CHANGE_ME',
    'charset' => 'utf8mb4',
];

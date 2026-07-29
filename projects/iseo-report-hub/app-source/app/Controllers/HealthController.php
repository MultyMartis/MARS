<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\DatabaseService;

final class HealthController extends BaseController
{
    /** @var list<string> */
    private const EXPECTED_TABLES = [
        'schema_migrations',
        'users',
        'roles',
        'user_roles',
        'audit_log',
        'clients',
        'projects',
        'sites',
        'project_type_profiles',
    ];

    /**
     * @return array<string, mixed>
     */
    public function collectStatus(): array
    {
        $required = [
            'pdo',
            'pdo_mysql',
            'mbstring',
            'json',
            'openssl',
            'fileinfo',
            'session',
        ];

        $optional = [
            'gd',
            'curl',
            'intl',
            'mysqli',
            'imagick',
        ];

        $loaded = get_loaded_extensions();
        $loadedLower = array_map('strtolower', $loaded);

        $check = static function (array $names) use ($loadedLower): array {
            $out = [];
            foreach ($names as $name) {
                $out[$name] = in_array(strtolower($name), $loadedLower, true);
            }
            return $out;
        };

        $requiredStatus = $check($required);
        $optionalStatus = $check($optional);

        /** @var DatabaseService|null $db */
        $db = $this->app['db'] ?? null;
        $dbBlock = $this->collectDbStatus($db instanceof DatabaseService ? $db : null);

        $appOk = !in_array(false, $requiredStatus, true);
        $overall = 'ok';
        if (!$appOk) {
            $overall = 'fail';
        } elseif ($dbBlock['configured'] && !$dbBlock['connection_ok']) {
            $overall = 'degraded';
        } elseif (!$dbBlock['configured']) {
            $overall = 'degraded';
        }

        return [
            'overall' => $overall,
            'php_version' => PHP_VERSION,
            'sapi' => PHP_SAPI,
            'required' => $requiredStatus,
            'optional' => $optionalStatus,
            'all_required_ok' => $appOk,
            'app_skeleton' => 'Auth persistence bootstrap',
            'env_local_present' => $this->config->envLocalPresent(),
            'env_required' => false,
            'wordpress' => 'not used',
            'db' => $dbBlock,
        ];
    }

    /**
     * @return array<string, mixed>
     */
    private function collectDbStatus(?DatabaseService $db): array
    {
        $fallback = [
            'configured' => false,
            'connection_ok' => false,
            'connection_label' => 'fail',
            'database' => null,
            'migration_count' => null,
            'latest_migration' => null,
            'tables_expected' => count(self::EXPECTED_TABLES),
            'tables_present' => null,
            'users_count' => null,
            'roles_count' => null,
            'status' => 'not_configured',
        ];

        if ($db === null) {
            return $fallback;
        }

        $probe = $db->testConnection();
        $configured = !empty($probe['configured']);
        $connected = !empty($probe['connected']);

        $out = [
            'configured' => $configured,
            'connection_ok' => $connected,
            'connection_label' => $connected ? 'pass' : ($configured ? 'fail' : 'n/a'),
            'database' => $probe['database'] ?? $db->getDatabaseName(),
            'migration_count' => null,
            'latest_migration' => null,
            'tables_expected' => count(self::EXPECTED_TABLES),
            'tables_present' => null,
            'users_count' => null,
            'roles_count' => null,
            'status' => $connected ? 'ok' : ($configured ? 'degraded' : 'not_configured'),
        ];

        if (!$connected) {
            return $out;
        }

        $migrations = $db->getMigrationSummary();
        $tables = $db->getTablePresence(self::EXPECTED_TABLES);

        $out['migration_count'] = $migrations['count'];
        $out['latest_migration'] = $migrations['latest'];
        $out['tables_present'] = $tables['present'];
        $out['users_count'] = $db->countTable('users');
        $out['roles_count'] = $db->countTable('roles');

        return $out;
    }

    public function index(): void
    {
        $status = $this->collectStatus();
        $this->render('health', [
            'pageTitle' => 'Состояние системы',
            'status' => $status,
        ]);
    }

    public function notFound(): void
    {
        $this->render('not-found', [
            'pageTitle' => 'Not Found',
            'path' => request_path(),
        ], 404);
    }
}

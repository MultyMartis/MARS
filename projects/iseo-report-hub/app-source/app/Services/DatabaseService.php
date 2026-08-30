<?php
declare(strict_types=1);

namespace Iseo\Services;

use PDO;
use PDOException;
use Throwable;

/**
 * PDO MySQL connection helper — no Composer, no credential output.
 */
final class DatabaseService
{
    public const REQUIRED_LOCAL_DB = 'iseo_report_hub_dev';

    private ?PDO $pdo = null;

    /** CLI local-mutation tools only; never enable in normal web runtime. */
    private bool $localDevGuardEnabled = false;

    public function __construct(
        private ConfigService $config
    ) {
    }

    public function isConfigured(): bool
    {
        return (bool) $this->config->get('database.configured', false);
    }

    public function getDatabaseName(): ?string
    {
        $name = (string) $this->config->get('database.database', '');
        return $name !== '' ? $name : null;
    }

    /**
     * Opt-in for local CLI mutation tools (seed/fixture/admin bootstrap).
     * Normal web/runtime must leave this disabled so production DB names work.
     */
    public function enableLocalDevDatabaseGuard(): void
    {
        $this->localDevGuardEnabled = true;
    }

    /**
     * Local mutation tooling guard.
     * No-op unless explicitly enabled AND APP_ENV=local.
     * Never blocks configured production / non-local DB names in normal web runtime.
     */
    public function assertLocalDevDatabase(): void
    {
        if (!$this->localDevGuardEnabled) {
            return;
        }

        $env = strtolower((string) $this->config->get('app.env', ''));
        if ($env !== 'local') {
            throw new \RuntimeException(
                'REFUSED: local DB guard requires APP_ENV=local.'
            );
        }

        $name = $this->getDatabaseName();
        if ($name !== self::REQUIRED_LOCAL_DB) {
            throw new \RuntimeException(
                'REFUSED: target DB must be exactly "' . self::REQUIRED_LOCAL_DB . '".'
            );
        }
    }

    /**
     * @throws \RuntimeException
     */
    public function connect(): PDO
    {
        if ($this->pdo instanceof PDO) {
            return $this->pdo;
        }

        if (!$this->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }

        $host = (string) $this->config->get('database.host', '127.0.0.1');
        $port = (int) $this->config->get('database.port', 3306);
        $database = (string) $this->config->get('database.database', '');
        $username = (string) $this->config->get('database.username', '');
        $password = (string) $this->config->get('database.password', '');
        $charset = (string) $this->config->get('database.charset', 'utf8mb4');

        if ($database === '' || $username === '') {
            throw new \RuntimeException('Database configuration incomplete.');
        }

        $dsn = sprintf(
            'mysql:host=%s;port=%d;dbname=%s;charset=%s',
            $host,
            $port,
            $database,
            $charset
        );

        try {
            $this->pdo = new PDO($dsn, $username, $password, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false,
            ]);
        } catch (PDOException $e) {
            throw new \RuntimeException('Database connection failed.', 0, $e);
        }

        return $this->pdo;
    }

    /**
     * Safe connection probe — never includes credentials or full DSN.
     *
     * @return array{
     *   configured:bool,
     *   connected:bool,
     *   database:?string,
     *   error:?string
     * }
     */
    public function testConnection(): array
    {
        if (!$this->isConfigured()) {
            return [
                'configured' => false,
                'connected' => false,
                'database' => $this->getDatabaseName(),
                'error' => 'not_configured',
            ];
        }

        try {
            $pdo = $this->connect();
            $actual = (string) $pdo->query('SELECT DATABASE()')->fetchColumn();

            return [
                'configured' => true,
                'connected' => true,
                'database' => $actual !== '' ? $actual : $this->getDatabaseName(),
                'error' => null,
            ];
        } catch (Throwable $e) {
            return [
                'configured' => true,
                'connected' => false,
                'database' => $this->getDatabaseName(),
                'error' => 'connection_failed',
            ];
        }
    }

    /**
     * @return array{
     *   count:int,
     *   latest:?string,
     *   latest_executed_at:?string,
     *   available:bool
     * }
     */
    public function getMigrationSummary(): array
    {
        $empty = [
            'count' => 0,
            'latest' => null,
            'latest_executed_at' => null,
            'available' => false,
        ];

        try {
            $pdo = $this->connect();
            $exists = (int) $pdo->query(
                "SELECT COUNT(*) FROM information_schema.TABLES
                 WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'schema_migrations'"
            )->fetchColumn();

            if ($exists === 0) {
                return $empty;
            }

            $count = (int) $pdo->query('SELECT COUNT(*) FROM schema_migrations')->fetchColumn();
            $latest = $pdo->query(
                'SELECT migration, executed_at FROM schema_migrations ORDER BY id DESC LIMIT 1'
            )->fetch();

            return [
                'count' => $count,
                'latest' => is_array($latest) ? (string) ($latest['migration'] ?? '') : null,
                'latest_executed_at' => is_array($latest) ? (string) ($latest['executed_at'] ?? '') : null,
                'available' => true,
            ];
        } catch (Throwable) {
            return $empty;
        }
    }

    /**
     * @param list<string> $expectedTables
     * @return array{expected:int, present:int, missing:list<string>, available:bool}
     */
    public function getTablePresence(array $expectedTables): array
    {
        $result = [
            'expected' => count($expectedTables),
            'present' => 0,
            'missing' => [],
            'available' => false,
        ];

        try {
            $pdo = $this->connect();
            $stmt = $pdo->prepare(
                'SELECT COUNT(*) FROM information_schema.TABLES
                 WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = :table'
            );

            $missing = [];
            $present = 0;
            foreach ($expectedTables as $table) {
                $stmt->execute([':table' => $table]);
                if ((int) $stmt->fetchColumn() > 0) {
                    $present++;
                } else {
                    $missing[] = $table;
                }
            }

            $result['present'] = $present;
            $result['missing'] = $missing;
            $result['available'] = true;
        } catch (Throwable) {
            $result['missing'] = $expectedTables;
        }

        return $result;
    }

    /**
     * Safe count helper — returns null when unavailable.
     */
    public function countTable(string $table): ?int
    {
        if (!preg_match('/^[a-z_][a-z0-9_]*$/i', $table)) {
            return null;
        }

        try {
            $pdo = $this->connect();
            return (int) $pdo->query('SELECT COUNT(*) FROM `' . $table . '`')->fetchColumn();
        } catch (Throwable) {
            return null;
        }
    }
}

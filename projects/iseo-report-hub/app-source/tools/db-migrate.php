<?php
declare(strict_types=1);

/**
 * Minimal no-dependency DB migration CLI for i-SEO Report Hub (local only).
 *
 * Usage:
 *   php tools/db-migrate.php status
 *   php tools/db-migrate.php apply
 *
 * Safety:
 * - refuses any DB name other than iseo_report_hub_dev
 * - never prints DB password
 * - no DROP DATABASE / truncate / destructive reset
 */

const REQUIRED_DB = 'iseo_report_hub_dev';

function usage(): void
{
    fwrite(STDOUT, "Usage: php tools/db-migrate.php <status|apply>\n");
}

function projectRoot(): string
{
    return dirname(__DIR__);
}

function loadEnvLocal(string $root): void
{
    $candidates = [
        $root . DIRECTORY_SEPARATOR . '.env.local',
        dirname($root) . DIRECTORY_SEPARATOR . '.env.local',
    ];

    foreach ($candidates as $path) {
        if (!is_file($path)) {
            continue;
        }
        $lines = file($path, FILE_IGNORE_NEW_LINES);
        if ($lines === false) {
            continue;
        }
        foreach ($lines as $line) {
            $line = trim($line);
            if ($line === '' || str_starts_with($line, '#')) {
                continue;
            }
            if (!str_contains($line, '=')) {
                continue;
            }
            [$key, $value] = explode('=', $line, 2);
            $key = trim($key);
            $value = trim($value);
            if ($key === '') {
                continue;
            }
            if (
                (str_starts_with($value, '"') && str_ends_with($value, '"'))
                || (str_starts_with($value, "'") && str_ends_with($value, "'"))
            ) {
                $value = substr($value, 1, -1);
            }
            if (getenv($key) === false) {
                putenv($key . '=' . $value);
                $_ENV[$key] = $value;
            }
        }
        return;
    }
}

/**
 * @return array{host:string,port:int,database:string,username:string,password:string,charset:string}
 */
function dbConfig(): array
{
    return [
        'host' => (string) (getenv('DB_HOST') ?: '127.0.0.1'),
        'port' => (int) (getenv('DB_PORT') ?: 3306),
        'database' => (string) (getenv('DB_DATABASE') ?: ''),
        'username' => (string) (getenv('DB_USERNAME') ?: ''),
        'password' => (string) (getenv('DB_PASSWORD') ?: ''),
        'charset' => 'utf8mb4',
    ];
}

function assertTargetDb(string $database): void
{
    if ($database !== REQUIRED_DB) {
        fwrite(STDERR, 'REFUSED: target DB must be exactly "' . REQUIRED_DB . '"; got "' . $database . "\".\n");
        exit(2);
    }
}

function pdoConnect(array $cfg): PDO
{
    assertTargetDb($cfg['database']);
    $dsn = sprintf(
        'mysql:host=%s;port=%d;dbname=%s;charset=%s',
        $cfg['host'],
        $cfg['port'],
        $cfg['database'],
        $cfg['charset']
    );
    $pdo = new PDO($dsn, $cfg['username'], $cfg['password'], [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    $actual = (string) $pdo->query('SELECT DATABASE()')->fetchColumn();
    assertTargetDb($actual);
    return $pdo;
}

function migrationsDir(string $root): string
{
    return $root . DIRECTORY_SEPARATOR . 'database' . DIRECTORY_SEPARATOR . 'migrations';
}

/**
 * @return list<string>
 */
function listMigrationFiles(string $dir): array
{
    if (!is_dir($dir)) {
        return [];
    }
    $files = glob($dir . DIRECTORY_SEPARATOR . '*.sql') ?: [];
    sort($files, SORT_STRING);
    return $files;
}

function schemaMigrationsExists(PDO $pdo): bool
{
    $stmt = $pdo->query(
        "SELECT COUNT(*) FROM information_schema.TABLES
         WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'schema_migrations'"
    );
    return ((int) $stmt->fetchColumn()) > 0;
}

/**
 * @return array<string, array{checksum:string,batch:int,executed_at:string}>
 */
function loadApplied(PDO $pdo): array
{
    if (!schemaMigrationsExists($pdo)) {
        return [];
    }
    $rows = $pdo->query(
        'SELECT migration, checksum, batch, executed_at FROM schema_migrations ORDER BY id ASC'
    )->fetchAll();
    $map = [];
    foreach ($rows as $row) {
        $map[$row['migration']] = [
            'checksum' => (string) $row['checksum'],
            'batch' => (int) $row['batch'],
            'executed_at' => (string) $row['executed_at'],
        ];
    }
    return $map;
}

function nextBatch(PDO $pdo): int
{
    if (!schemaMigrationsExists($pdo)) {
        return 1;
    }
    $max = (int) $pdo->query('SELECT COALESCE(MAX(batch), 0) FROM schema_migrations')->fetchColumn();
    return $max + 1;
}

function checksumFile(string $path): string
{
    $hash = hash_file('sha256', $path);
    if ($hash === false) {
        throw new RuntimeException('Unable to hash migration file: ' . basename($path));
    }
    return $hash;
}

function splitSqlStatements(string $sql): array
{
    $statements = [];
    $buffer = '';
    $lines = preg_split("/\r\n|\n|\r/", $sql) ?: [];
    foreach ($lines as $line) {
        $trim = ltrim($line);
        if ($trim === '' || str_starts_with($trim, '--')) {
            continue;
        }
        $buffer .= $line . "\n";
        if (str_ends_with(rtrim($line), ';')) {
            $stmt = trim($buffer);
            if ($stmt !== '') {
                $statements[] = $stmt;
            }
            $buffer = '';
        }
    }
    $tail = trim($buffer);
    if ($tail !== '') {
        $statements[] = $tail;
    }
    return $statements;
}

function applyMigrationFile(PDO $pdo, string $path, int $batch): string
{
    $name = basename($path);
    $checksum = checksumFile($path);
    $sql = file_get_contents($path);
    if ($sql === false) {
        throw new RuntimeException('Unable to read migration: ' . $name);
    }

    // MySQL DDL implicitly commits; do not wrap CREATE/ALTER in a PDO transaction.
    foreach (splitSqlStatements($sql) as $statement) {
        $pdo->exec($statement);
    }

    if (!schemaMigrationsExists($pdo)) {
        throw new RuntimeException('schema_migrations missing after applying ' . $name);
    }

    $ins = $pdo->prepare(
        'INSERT INTO schema_migrations (migration, checksum, batch) VALUES (:migration, :checksum, :batch)'
    );
    $ins->execute([
        ':migration' => $name,
        ':checksum' => $checksum,
        ':batch' => $batch,
    ]);

    return $checksum;
}

function cmdStatus(PDO $pdo, string $root): int
{
    $db = (string) $pdo->query('SELECT DATABASE()')->fetchColumn();
    fwrite(STDOUT, "DB: {$db}\n");
    $ledgerExists = schemaMigrationsExists($pdo);
    fwrite(STDOUT, 'schema_migrations: ' . ($ledgerExists ? 'present' : 'absent') . "\n");

    $applied = loadApplied($pdo);
    $files = listMigrationFiles(migrationsDir($root));
    if ($files === []) {
        fwrite(STDOUT, "No migration files found.\n");
        return 0;
    }

    fwrite(STDOUT, "Migrations:\n");
    foreach ($files as $path) {
        $name = basename($path);
        $fileChecksum = checksumFile($path);
        if (!isset($applied[$name])) {
            fwrite(STDOUT, "  [pending] {$name}\n");
            continue;
        }
        $match = hash_equals($applied[$name]['checksum'], $fileChecksum) ? 'checksum_ok' : 'checksum_mismatch';
        fwrite(
            STDOUT,
            sprintf(
                "  [applied] %s batch=%d executed_at=%s %s\n",
                $name,
                $applied[$name]['batch'],
                $applied[$name]['executed_at'],
                $match
            )
        );
    }
    return 0;
}

function cmdApply(PDO $pdo, string $root): int
{
    $applied = loadApplied($pdo);
    $files = listMigrationFiles(migrationsDir($root));
    if ($files === []) {
        fwrite(STDOUT, "No migration files found.\n");
        return 0;
    }

    $pending = [];
    foreach ($files as $path) {
        $name = basename($path);
        if (!isset($applied[$name])) {
            $pending[] = $path;
            continue;
        }
        $fileChecksum = checksumFile($path);
        if (!hash_equals($applied[$name]['checksum'], $fileChecksum)) {
            fwrite(STDERR, "REFUSED: checksum mismatch for already-applied migration {$name}\n");
            return 3;
        }
    }

    if ($pending === []) {
        fwrite(STDOUT, "Nothing to apply. All migrations already applied.\n");
        return 0;
    }

    fwrite(STDOUT, 'Pending: ' . count($pending) . "\n");
    $batch = nextBatch($pdo);
    $count = 0;
    foreach ($pending as $path) {
        $name = basename($path);
        fwrite(STDOUT, "Applying {$name} ... ");
        $checksum = applyMigrationFile($pdo, $path, $batch);
        fwrite(STDOUT, "OK checksum={$checksum}\n");
        $count++;
    }
    fwrite(STDOUT, "Applied count: {$count}\n");
    return 0;
}

$root = projectRoot();
loadEnvLocal($root);

$argvCommand = $argv[1] ?? '';
if ($argvCommand !== 'status' && $argvCommand !== 'apply') {
    usage();
    exit(1);
}

$cfg = dbConfig();
if ($cfg['database'] === '' || $cfg['username'] === '') {
    fwrite(STDERR, "Missing DB_DATABASE or DB_USERNAME (set in .env.local or environment).\n");
    exit(2);
}
assertTargetDb($cfg['database']);

try {
    $pdo = pdoConnect($cfg);
} catch (Throwable $e) {
    fwrite(STDERR, 'DB connection failed: ' . $e->getMessage() . "\n");
    exit(4);
}

$code = $argvCommand === 'status' ? cmdStatus($pdo, $root) : cmdApply($pdo, $root);
exit($code);

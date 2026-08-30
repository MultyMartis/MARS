<?php
declare(strict_types=1);

/**
 * Create exactly one local admin_owner for iseo_report_hub_dev.
 *
 * Usage:
 *   php tools/create-local-admin.php [--name="Local Admin"] [--email=admin@iseo-report-hub.test]
 *
 * Password:
 *   - Prefer interactive prompt (hidden when possible)
 *   - Or set process-only env ISEO_ADMIN_PASSWORD (never argv; never commit)
 *
 * Safety:
 * - CLI only
 * - refuses DB name other than iseo_report_hub_dev
 * - refuses if admin_owner already exists (unless --allow-existing)
 * - refuses if email already exists
 * - never prints password or hash
 */

if (PHP_SAPI !== 'cli') {
    fwrite(STDERR, "REFUSED: CLI only.\n");
    exit(1);
}

const REQUIRED_DB = 'iseo_report_hub_dev';
const ADMIN_ROLE = 'admin_owner';
const DEFAULT_NAME = 'Local Admin';
const DEFAULT_EMAIL = 'admin@iseo-report-hub.test';

/**
 * @return array{name:string,email:string,allow_existing:bool}
 */
function parseArgs(array $argv): array
{
    $name = DEFAULT_NAME;
    $email = DEFAULT_EMAIL;
    $allowExisting = false;

    foreach (array_slice($argv, 1) as $arg) {
        if ($arg === '--allow-existing') {
            $allowExisting = true;
            continue;
        }
        if (str_starts_with($arg, '--name=')) {
            $name = trim(substr($arg, 7));
            continue;
        }
        if (str_starts_with($arg, '--email=')) {
            $email = strtolower(trim(substr($arg, 8)));
            continue;
        }
        if ($arg === '--help' || $arg === '-h') {
            fwrite(STDOUT, "Usage: php tools/create-local-admin.php [--name=...] [--email=...] [--allow-existing]\n");
            fwrite(STDOUT, "Password via hidden prompt or ISEO_ADMIN_PASSWORD env (local-only).\n");
            exit(0);
        }
        fwrite(STDERR, "Unknown argument: {$arg}\n");
        exit(1);
    }

    if ($name === '' || $email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        fwrite(STDERR, "Invalid name or email.\n");
        exit(1);
    }

    return [
        'name' => $name,
        'email' => $email,
        'allow_existing' => $allowExisting,
    ];
}

function readPassword(): string
{
    $fromEnv = getenv('ISEO_ADMIN_PASSWORD');
    if (is_string($fromEnv) && $fromEnv !== '') {
        return $fromEnv;
    }

    fwrite(STDOUT, "Enter local admin password (min 12 chars; input may be visible on some Windows consoles): ");
    $line = fgets(STDIN);
    if ($line === false) {
        fwrite(STDERR, "STOP — password input unavailable.\n");
        exit(2);
    }
    $password = rtrim($line, "\r\n");
    if ($password === '') {
        fwrite(STDERR, "STOP — empty password refused.\n");
        exit(2);
    }

    return $password;
}

$args = parseArgs($argv);
$root = dirname(__DIR__);

/** @var array<string, mixed> $app */
$app = require $root . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . 'bootstrap.php';

/** @var \Iseo\Services\DatabaseService $db */
$db = $app['db'];
/** @var \Iseo\Services\ConfigService $config */
$config = $app['config'];

if (!$db->isConfigured()) {
    fwrite(STDERR, "REFUSED: database not configured (.env.local / DB_* missing).\n");
    exit(2);
}

try {
    $db->enableLocalDevDatabaseGuard();
    $db->assertLocalDevDatabase();
    $pdo = $db->connect();
    $actual = (string) $pdo->query('SELECT DATABASE()')->fetchColumn();
    if ($actual !== REQUIRED_DB) {
        fwrite(STDERR, 'REFUSED: connected DB is not ' . REQUIRED_DB . ".\n");
        exit(2);
    }
} catch (Throwable $e) {
    fwrite(STDERR, "DB connection failed (details redacted).\n");
    exit(4);
}

$roleStmt = $pdo->prepare('SELECT id FROM roles WHERE code = :code LIMIT 1');
$roleStmt->execute([':code' => ADMIN_ROLE]);
$roleId = $roleStmt->fetchColumn();
if ($roleId === false) {
    fwrite(STDERR, "REFUSED: role admin_owner not found.\n");
    exit(3);
}
$roleId = (int) $roleId;

$adminCount = (int) $pdo->query(
    "SELECT COUNT(*)
     FROM user_roles ur
     INNER JOIN roles r ON r.id = ur.role_id
     WHERE r.code = 'admin_owner'"
)->fetchColumn();

if ($adminCount > 0 && !$args['allow_existing']) {
    fwrite(STDERR, "REFUSED: admin_owner already exists (users with role). Use --allow-existing only with explicit operator intent.\n");
    exit(5);
}

$emailCheck = $pdo->prepare('SELECT id FROM users WHERE email = :email LIMIT 1');
$emailCheck->execute([':email' => $args['email']]);
if ($emailCheck->fetchColumn() !== false) {
    fwrite(STDERR, "REFUSED: email already exists.\n");
    exit(6);
}

$password = readPassword();
if (strlen($password) < 12) {
    fwrite(STDERR, "REFUSED: password must be at least 12 characters.\n");
    // Clear local variable best-effort.
    $password = '';
    exit(7);
}

$hash = password_hash($password, PASSWORD_DEFAULT);
$password = ''; // clear plaintext ASAP
unset($password);

if (!is_string($hash) || $hash === '') {
    fwrite(STDERR, "REFUSED: password_hash failed.\n");
    exit(8);
}

try {
    $pdo->beginTransaction();

    $ins = $pdo->prepare(
        'INSERT INTO users (name, email, password_hash, status)
         VALUES (:name, :email, :password_hash, :status)'
    );
    $ins->execute([
        ':name' => $args['name'],
        ':email' => $args['email'],
        ':password_hash' => $hash,
        ':status' => 'active',
    ]);
    $userId = (int) $pdo->lastInsertId();
    $hash = ''; // clear hash from local var after insert

    $assign = $pdo->prepare(
        'INSERT INTO user_roles (user_id, role_id) VALUES (:user_id, :role_id)'
    );
    $assign->execute([
        ':user_id' => $userId,
        ':role_id' => $roleId,
    ]);

    $meta = json_encode(
        ['role' => ADMIN_ROLE, 'local_bootstrap' => true],
        JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR
    );
    $audit = $pdo->prepare(
        'INSERT INTO audit_log (actor_user_id, event_type, entity_type, entity_id, metadata_json)
         VALUES (:actor_user_id, :event_type, :entity_type, :entity_id, :metadata_json)'
    );
    $audit->execute([
        ':actor_user_id' => $userId,
        ':event_type' => 'auth.bootstrap.admin_created',
        ':entity_type' => 'user',
        ':entity_id' => $userId,
        ':metadata_json' => $meta,
    ]);

    $pdo->commit();
} catch (Throwable $e) {
    if ($pdo->inTransaction()) {
        $pdo->rollBack();
    }
    fwrite(STDERR, "CREATE FAILED (details redacted).\n");
    exit(9);
}

fwrite(STDOUT, "created=yes\n");
fwrite(STDOUT, 'user_id=' . $userId . "\n");
fwrite(STDOUT, 'email=' . $args['email'] . "\n");
fwrite(STDOUT, 'role=' . ADMIN_ROLE . "\n");
fwrite(STDOUT, "password=REDACTED\n");
fwrite(STDOUT, "hash=REDACTED\n");
exit(0);

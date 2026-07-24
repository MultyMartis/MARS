<?php
declare(strict_types=1);

/**
 * Create local-only demo fixture rows for iseo_report_hub_dev.
 *
 * Creates exactly:
 *   - 1 demo client (slug: demo-client)
 *   - 1 demo project (slug: demo-seo-project)
 *   - 1 demo site (url: https://demo.example.test)
 *   - 1 demo reporting_period (period_key: 2026-07)
 * Optional:
 *   - 1 audit_log event (local_fixture.created)
 *
 * Usage:
 *   php tools/create-local-fixture.php
 *
 * Safety:
 * - CLI only
 * - refuses DB name other than iseo_report_hub_dev
 * - refuses DB host other than 127.0.0.1
 * - idempotent (already-present → exit 0)
 * - refuses partial/inconsistent fixture state
 * - no DELETE/DROP/TRUNCATE
 * - never prints credentials / passwords / hashes
 * - no real client data
 */

if (PHP_SAPI !== 'cli') {
    fwrite(STDERR, "REFUSED: CLI only.\n");
    exit(1);
}

const REQUIRED_DB = 'iseo_report_hub_dev';
const REQUIRED_HOST = '127.0.0.1';
const ADMIN_EMAIL = 'admin@iseo-report-hub.test';
const MARKER = 'LOCAL_FIXTURE_ONLY';

const CLIENT_NAME = 'Demo Client';
const CLIENT_SLUG = 'demo-client';
const PROJECT_NAME = 'Demo SEO Project';
const PROJECT_SLUG = 'demo-seo-project';
const PROJECT_TYPE = 'service_corporate';
const SITE_URL = 'https://demo.example.test';
const PERIOD_KEY = '2026-07';
const PERIOD_START = '2026-07-01';
const PERIOD_END = '2026-07-31';
const PERIOD_STATUS = 'draft';
const PERIOD_TITLE = 'Demo July 2026';
const AUDIT_EVENT = 'local_fixture.created';

/**
 * @return list<string>
 */
function requiredTables(): array
{
    return [
        'clients',
        'projects',
        'sites',
        'reporting_periods',
        'users',
        'project_type_profiles',
        'audit_log',
    ];
}

/**
 * @return array<string, bool>
 */
function tableColumns(PDO $pdo, string $table): array
{
    $stmt = $pdo->prepare(
        'SELECT COLUMN_NAME FROM information_schema.COLUMNS
         WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = :table'
    );
    $stmt->execute([':table' => $table]);
    $cols = [];
    foreach ($stmt->fetchAll(PDO::FETCH_COLUMN) as $name) {
        $cols[(string) $name] = true;
    }
    return $cols;
}

function tableExists(PDO $pdo, string $table): bool
{
    $stmt = $pdo->prepare(
        'SELECT COUNT(*) FROM information_schema.TABLES
         WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = :table'
    );
    $stmt->execute([':table' => $table]);
    return (int) $stmt->fetchColumn() > 0;
}

function countTable(PDO $pdo, string $table): int
{
    return (int) $pdo->query('SELECT COUNT(*) FROM `' . $table . '`')->fetchColumn();
}

/**
 * @param array<string, bool> $cols
 */
function hasColumn(array $cols, string $name): bool
{
    return isset($cols[$name]);
}

/**
 * @return array{id:int,name:string,slug:string,status:string,notes:?string}|null
 */
function findDemoClient(PDO $pdo): ?array
{
    $stmt = $pdo->prepare('SELECT id, name, slug, status, notes FROM clients WHERE slug = :slug LIMIT 1');
    $stmt->execute([':slug' => CLIENT_SLUG]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    return is_array($row) ? [
        'id' => (int) $row['id'],
        'name' => (string) $row['name'],
        'slug' => (string) $row['slug'],
        'status' => (string) $row['status'],
        'notes' => $row['notes'] !== null ? (string) $row['notes'] : null,
    ] : null;
}

/**
 * @return array{id:int,client_id:int,name:string,slug:string,project_type:string,status:string}|null
 */
function findDemoProject(PDO $pdo, int $clientId): ?array
{
    $stmt = $pdo->prepare(
        'SELECT id, client_id, name, slug, project_type, status
         FROM projects WHERE client_id = :client_id AND slug = :slug LIMIT 1'
    );
    $stmt->execute([':client_id' => $clientId, ':slug' => PROJECT_SLUG]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    return is_array($row) ? [
        'id' => (int) $row['id'],
        'client_id' => (int) $row['client_id'],
        'name' => (string) $row['name'],
        'slug' => (string) $row['slug'],
        'project_type' => (string) $row['project_type'],
        'status' => (string) $row['status'],
    ] : null;
}

/**
 * @return array{id:int,project_id:int,url:string,label:?string,is_primary:int}|null
 */
function findDemoSite(PDO $pdo, int $projectId): ?array
{
    $stmt = $pdo->prepare(
        'SELECT id, project_id, url, label, is_primary
         FROM sites
         WHERE project_id = :project_id AND (url = :url OR is_primary = 1)
         ORDER BY (url = :url2) DESC, is_primary DESC, id ASC
         LIMIT 1'
    );
    $stmt->execute([
        ':project_id' => $projectId,
        ':url' => SITE_URL,
        ':url2' => SITE_URL,
    ]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    return is_array($row) ? [
        'id' => (int) $row['id'],
        'project_id' => (int) $row['project_id'],
        'url' => (string) $row['url'],
        'label' => $row['label'] !== null ? (string) $row['label'] : null,
        'is_primary' => (int) $row['is_primary'],
    ] : null;
}

/**
 * @return array{id:int,project_id:int,period_key:string,status:string,title:?string,summary:?string}|null
 */
function findDemoPeriod(PDO $pdo, int $projectId): ?array
{
    $stmt = $pdo->prepare(
        'SELECT id, project_id, period_key, status, title, summary
         FROM reporting_periods
         WHERE project_id = :project_id AND period_key = :period_key
         LIMIT 1'
    );
    $stmt->execute([':project_id' => $projectId, ':period_key' => PERIOD_KEY]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    return is_array($row) ? [
        'id' => (int) $row['id'],
        'project_id' => (int) $row['project_id'],
        'period_key' => (string) $row['period_key'],
        'status' => (string) $row['status'],
        'title' => $row['title'] !== null ? (string) $row['title'] : null,
        'summary' => $row['summary'] !== null ? (string) $row['summary'] : null,
    ] : null;
}

function resolveAdminUserId(PDO $pdo): ?int
{
    $stmt = $pdo->prepare('SELECT id FROM users WHERE email = :email LIMIT 1');
    $stmt->execute([':email' => ADMIN_EMAIL]);
    $id = $stmt->fetchColumn();
    return $id === false ? null : (int) $id;
}

/**
 * @param array{id:int,name:string,slug:string,status:string,notes:?string} $client
 */
function clientMatchesExpected(array $client): bool
{
    return $client['name'] === CLIENT_NAME
        && $client['slug'] === CLIENT_SLUG
        && $client['status'] === 'active'
        && $client['notes'] === MARKER;
}

/**
 * @param array{id:int,client_id:int,name:string,slug:string,project_type:string,status:string} $project
 */
function projectMatchesExpected(array $project, int $clientId): bool
{
    return $project['client_id'] === $clientId
        && $project['name'] === PROJECT_NAME
        && $project['slug'] === PROJECT_SLUG
        && $project['project_type'] === PROJECT_TYPE
        && $project['status'] === 'active';
}

/**
 * @param array{id:int,project_id:int,url:string,label:?string,is_primary:int} $site
 */
function siteMatchesExpected(array $site, int $projectId): bool
{
    return $site['project_id'] === $projectId
        && $site['url'] === SITE_URL
        && $site['label'] === MARKER
        && $site['is_primary'] === 1;
}

/**
 * @param array{id:int,project_id:int,period_key:string,status:string,title:?string,summary:?string} $period
 */
function periodMatchesExpected(array $period, int $projectId): bool
{
    return $period['project_id'] === $projectId
        && $period['period_key'] === PERIOD_KEY
        && $period['status'] === PERIOD_STATUS
        && $period['title'] === PERIOD_TITLE
        && $period['summary'] === MARKER;
}

function stopInconsistent(string $reason): never
{
    fwrite(STDERR, "STOP — inconsistent fixture state: {$reason}\n");
    exit(3);
}

foreach (array_slice($argv, 1) as $arg) {
    if ($arg === '--help' || $arg === '-h') {
        fwrite(STDOUT, "Usage: php tools/create-local-fixture.php\n");
        fwrite(STDOUT, "Creates local-only demo client/project/site/reporting_period (idempotent).\n");
        exit(0);
    }
    fwrite(STDERR, "Unknown argument: {$arg}\n");
    exit(1);
}

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

$host = (string) $config->get('database.host', '');
$name = (string) $config->get('database.database', '');

if ($host !== REQUIRED_HOST) {
    fwrite(STDERR, 'REFUSED: DB host must be exactly ' . REQUIRED_HOST . ".\n");
    exit(2);
}
if ($name !== REQUIRED_DB) {
    fwrite(STDERR, 'REFUSED: target DB must be exactly ' . REQUIRED_DB . ".\n");
    exit(2);
}

try {
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

foreach (requiredTables() as $table) {
    if (!tableExists($pdo, $table)) {
        fwrite(STDERR, "REFUSED: required table missing: {$table}\n");
        exit(5);
    }
}

$before = [
    'clients' => countTable($pdo, 'clients'),
    'projects' => countTable($pdo, 'projects'),
    'sites' => countTable($pdo, 'sites'),
    'reporting_periods' => countTable($pdo, 'reporting_periods'),
];

$clientCols = tableColumns($pdo, 'clients');
$projectCols = tableColumns($pdo, 'projects');
$siteCols = tableColumns($pdo, 'sites');
$periodCols = tableColumns($pdo, 'reporting_periods');
$auditCols = tableColumns($pdo, 'audit_log');

foreach (['name', 'slug', 'status', 'notes'] as $col) {
    if (!hasColumn($clientCols, $col)) {
        fwrite(STDERR, "REFUSED: clients.{$col} missing.\n");
        exit(5);
    }
}
foreach (['client_id', 'name', 'slug', 'project_type', 'status'] as $col) {
    if (!hasColumn($projectCols, $col)) {
        fwrite(STDERR, "REFUSED: projects.{$col} missing.\n");
        exit(5);
    }
}
foreach (['project_id', 'url', 'label', 'is_primary'] as $col) {
    if (!hasColumn($siteCols, $col)) {
        fwrite(STDERR, "REFUSED: sites.{$col} missing.\n");
        exit(5);
    }
}
foreach (['project_id', 'period_key', 'period_start', 'period_end', 'status', 'title', 'summary'] as $col) {
    if (!hasColumn($periodCols, $col)) {
        fwrite(STDERR, "REFUSED: reporting_periods.{$col} missing.\n");
        exit(5);
    }
}

$existingClient = findDemoClient($pdo);
$existingProject = null;
$existingSite = null;
$existingPeriod = null;

if ($existingClient !== null) {
    if (!clientMatchesExpected($existingClient)) {
        stopInconsistent('demo-client exists but fields do not match LOCAL_FIXTURE_ONLY expectations');
    }
    $existingProject = findDemoProject($pdo, $existingClient['id']);
    if ($existingProject !== null) {
        if (!projectMatchesExpected($existingProject, $existingClient['id'])) {
            stopInconsistent('demo-seo-project exists but fields do not match expectations');
        }
        $existingSite = findDemoSite($pdo, $existingProject['id']);
        if ($existingSite !== null && !siteMatchesExpected($existingSite, $existingProject['id'])) {
            stopInconsistent('demo site exists but fields do not match expectations');
        }
        $existingPeriod = findDemoPeriod($pdo, $existingProject['id']);
        if ($existingPeriod !== null && !periodMatchesExpected($existingPeriod, $existingProject['id'])) {
            stopInconsistent('demo reporting_period exists but fields do not match expectations');
        }
    }
}

$presentFlags = [
    'client' => $existingClient !== null,
    'project' => $existingProject !== null,
    'site' => $existingSite !== null,
    'period' => $existingPeriod !== null,
];
$presentCount = count(array_filter($presentFlags));

if ($presentCount > 0 && $presentCount < 4) {
    $parts = [];
    foreach ($presentFlags as $k => $v) {
        $parts[] = $k . '=' . ($v ? 'yes' : 'no');
    }
    stopInconsistent('partial fixture present (' . implode(', ', $parts) . ')');
}

if ($presentCount === 4) {
    fwrite(STDOUT, "result=already-present\n");
    fwrite(STDOUT, 'client_id=' . $existingClient['id'] . "\n");
    fwrite(STDOUT, 'project_id=' . $existingProject['id'] . "\n");
    fwrite(STDOUT, 'site_id=' . $existingSite['id'] . "\n");
    fwrite(STDOUT, 'reporting_period_id=' . $existingPeriod['id'] . "\n");
    fwrite(STDOUT, 'clients_before=' . $before['clients'] . "\n");
    fwrite(STDOUT, 'projects_before=' . $before['projects'] . "\n");
    fwrite(STDOUT, 'sites_before=' . $before['sites'] . "\n");
    fwrite(STDOUT, 'reporting_periods_before=' . $before['reporting_periods'] . "\n");
    fwrite(STDOUT, 'clients_after=' . $before['clients'] . "\n");
    fwrite(STDOUT, 'projects_after=' . $before['projects'] . "\n");
    fwrite(STDOUT, 'sites_after=' . $before['sites'] . "\n");
    fwrite(STDOUT, 'reporting_periods_after=' . $before['reporting_periods'] . "\n");
    fwrite(STDOUT, "validation=idempotent_match\n");
    fwrite(STDOUT, "audit_event=skipped_already_present\n");
    exit(0);
}

$adminUserId = resolveAdminUserId($pdo);

try {
    $pdo->beginTransaction();

    $insClient = $pdo->prepare(
        'INSERT INTO clients (name, slug, status, notes)
         VALUES (:name, :slug, :status, :notes)'
    );
    $insClient->execute([
        ':name' => CLIENT_NAME,
        ':slug' => CLIENT_SLUG,
        ':status' => 'active',
        ':notes' => MARKER,
    ]);
    $clientId = (int) $pdo->lastInsertId();

    $insProject = $pdo->prepare(
        'INSERT INTO projects (client_id, name, slug, project_type, status)
         VALUES (:client_id, :name, :slug, :project_type, :status)'
    );
    $insProject->execute([
        ':client_id' => $clientId,
        ':name' => PROJECT_NAME,
        ':slug' => PROJECT_SLUG,
        ':project_type' => PROJECT_TYPE,
        ':status' => 'active',
    ]);
    $projectId = (int) $pdo->lastInsertId();

    $insSite = $pdo->prepare(
        'INSERT INTO sites (project_id, url, label, is_primary)
         VALUES (:project_id, :url, :label, :is_primary)'
    );
    $insSite->execute([
        ':project_id' => $projectId,
        ':url' => SITE_URL,
        ':label' => MARKER,
        ':is_primary' => 1,
    ]);
    $siteId = (int) $pdo->lastInsertId();

    $periodFields = [
        'project_id',
        'period_key',
        'period_start',
        'period_end',
        'status',
        'title',
        'summary',
    ];
    $periodParams = [
        ':project_id' => $projectId,
        ':period_key' => PERIOD_KEY,
        ':period_start' => PERIOD_START,
        ':period_end' => PERIOD_END,
        ':status' => PERIOD_STATUS,
        ':title' => PERIOD_TITLE,
        ':summary' => MARKER,
    ];

    if ($adminUserId !== null) {
        if (hasColumn($periodCols, 'owner_user_id')) {
            $periodFields[] = 'owner_user_id';
            $periodParams[':owner_user_id'] = $adminUserId;
        }
        if (hasColumn($periodCols, 'created_by')) {
            $periodFields[] = 'created_by';
            $periodParams[':created_by'] = $adminUserId;
        }
    }

    $placeholders = array_map(static fn (string $f): string => ':' . $f, $periodFields);
    $insPeriod = $pdo->prepare(
        'INSERT INTO reporting_periods (`' . implode('`, `', $periodFields) . '`)
         VALUES (' . implode(', ', $placeholders) . ')'
    );
    $insPeriod->execute($periodParams);
    $periodId = (int) $pdo->lastInsertId();

    $auditWritten = false;
    $auditSkipReason = '';
    $auditReady = hasColumn($auditCols, 'event_type')
        && hasColumn($auditCols, 'entity_type')
        && hasColumn($auditCols, 'entity_id')
        && hasColumn($auditCols, 'metadata_json')
        && hasColumn($auditCols, 'actor_user_id');

    if ($auditReady) {
        $meta = json_encode(
            [
                'marker' => MARKER,
                'client_slug' => CLIENT_SLUG,
                'project_slug' => PROJECT_SLUG,
                'period_key' => PERIOD_KEY,
                'local_fixture' => true,
            ],
            JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR
        );
        $insAudit = $pdo->prepare(
            'INSERT INTO audit_log (actor_user_id, event_type, entity_type, entity_id, metadata_json)
             VALUES (:actor_user_id, :event_type, :entity_type, :entity_id, :metadata_json)'
        );
        $insAudit->execute([
            ':actor_user_id' => $adminUserId,
            ':event_type' => AUDIT_EVENT,
            ':entity_type' => 'reporting_period',
            ':entity_id' => $periodId,
            ':metadata_json' => $meta,
        ]);
        $auditWritten = true;
    } else {
        $auditSkipReason = 'audit_log schema incomplete for safe generic event';
    }

    $pdo->commit();
} catch (Throwable $e) {
    if ($pdo->inTransaction()) {
        $pdo->rollBack();
    }
    fwrite(STDERR, "CREATE FAILED (details redacted).\n");
    exit(9);
}

$after = [
    'clients' => countTable($pdo, 'clients'),
    'projects' => countTable($pdo, 'projects'),
    'sites' => countTable($pdo, 'sites'),
    'reporting_periods' => countTable($pdo, 'reporting_periods'),
];

fwrite(STDOUT, "result=created\n");
fwrite(STDOUT, 'client_id=' . $clientId . "\n");
fwrite(STDOUT, 'project_id=' . $projectId . "\n");
fwrite(STDOUT, 'site_id=' . $siteId . "\n");
fwrite(STDOUT, 'reporting_period_id=' . $periodId . "\n");
fwrite(STDOUT, 'clients_before=' . $before['clients'] . "\n");
fwrite(STDOUT, 'projects_before=' . $before['projects'] . "\n");
fwrite(STDOUT, 'sites_before=' . $before['sites'] . "\n");
fwrite(STDOUT, 'reporting_periods_before=' . $before['reporting_periods'] . "\n");
fwrite(STDOUT, 'clients_after=' . $after['clients'] . "\n");
fwrite(STDOUT, 'projects_after=' . $after['projects'] . "\n");
fwrite(STDOUT, 'sites_after=' . $after['sites'] . "\n");
fwrite(STDOUT, 'reporting_periods_after=' . $after['reporting_periods'] . "\n");
fwrite(STDOUT, "validation=insert_ok\n");
if ($auditWritten) {
    fwrite(STDOUT, 'audit_event=' . AUDIT_EVENT . "\n");
} else {
    fwrite(STDOUT, 'audit_event=skipped:' . $auditSkipReason . "\n");
}
exit(0);

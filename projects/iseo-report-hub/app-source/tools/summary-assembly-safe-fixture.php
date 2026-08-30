<?php
declare(strict_types=1);

/**
 * Guarded local-only fixture for Summary Assembly Apply write-proof.
 *
 * Usage:
 *   php tools/summary-assembly-safe-fixture.php --create --confirm-local-fixture
 *   php tools/summary-assembly-safe-fixture.php --cleanup --ids=<path> --confirm-local-fixture
 *
 * Safety:
 * - CLI only
 * - requires --confirm-local-fixture
 * - APP_ENV must be local
 * - DB name exactly iseo_report_hub_dev
 * - DB host exactly 127.0.0.1
 * - APP_URL host must be local
 * - never mutates monthly ids 1 or 5
 * - cleanup deletes exact JSON ids only after marker match
 * - never prints credentials / passwords / hashes / tokens
 */

if (PHP_SAPI !== 'cli') {
    fwrite(STDERR, "REFUSED: CLI only.\n");
    exit(1);
}

const REQUIRED_DB = 'iseo_report_hub_dev';
const REQUIRED_HOST = '127.0.0.1';
const REQUIRED_APP_ENV = 'local';
const LOCAL_MARKER = 'LOCAL_FIXTURE_ONLY';
const MARKER_PREFIX = 'MARS_FIXTURE_SUMMARY_APPLY_';
const PROTECTED_MONTHLY_IDS = [1, 5];
const DEFAULT_PERIOD_KEY = '2099-01';
const DEFAULT_CLIENT_ID = 1;
const DEFAULT_PROJECT_ID = 1;
const DEFAULT_SITE_ID = 1;
const DEFAULT_CREATED_BY = 1;
const DEFAULT_OWNER_ID = 2;
const DEFAULT_IDS_PATH = 'X:\\AI MARS STORAGE\\incoming\\iseo-report-hub\\summary-assembly-safe-fixture-implementation-01\\fixture-ids.json';
const TITLE_PREFIX = 'MARS SAFE APPLY FIXTURE';
const PLAN_PLACEHOLDER = "Черновой план до применения сборки. LOCAL_FIXTURE_ONLY";
const PLAN_SUMMARY = 'Устаревшее краткое описание до apply.';

/**
 * @return array{
 *   mode:?string,
 *   confirm:bool,
 *   ids:?string,
 *   dump_file:?string,
 *   help:bool
 * }
 */
function parseArgs(array $argv): array
{
    $out = [
        'mode' => null,
        'confirm' => false,
        'ids' => null,
        'dump_file' => null,
        'help' => false,
    ];
    foreach (array_slice($argv, 1) as $arg) {
        if ($arg === '--help' || $arg === '-h') {
            $out['help'] = true;
            continue;
        }
        if ($arg === '--create') {
            $out['mode'] = 'create';
            continue;
        }
        if ($arg === '--cleanup') {
            $out['mode'] = 'cleanup';
            continue;
        }
        if ($arg === '--confirm-local-fixture') {
            $out['confirm'] = true;
            continue;
        }
        if (str_starts_with($arg, '--ids=')) {
            $out['ids'] = substr($arg, 6);
            continue;
        }
        if (str_starts_with($arg, '--dump-file=')) {
            $out['dump_file'] = substr($arg, 12);
            continue;
        }
        fwrite(STDERR, "Unknown argument: {$arg}\n");
        exit(1);
    }
    return $out;
}

function printHelp(): void
{
    fwrite(STDOUT, "Usage:\n");
    fwrite(STDOUT, "  php tools/summary-assembly-safe-fixture.php --create --confirm-local-fixture\n");
    fwrite(STDOUT, "  php tools/summary-assembly-safe-fixture.php --cleanup --ids=<path> --confirm-local-fixture\n");
    fwrite(STDOUT, "Local iseo_report_hub_dev only. Never prints secrets.\n");
}

function refuse(string $message, int $code = 2): never
{
    fwrite(STDERR, 'REFUSED: ' . $message . "\n");
    exit($code);
}

function stop(string $message, int $code = 3): never
{
    fwrite(STDERR, 'STOP: ' . $message . "\n");
    exit($code);
}

/**
 * @param array<string, mixed> $payload
 */
function emitJson(array $payload): void
{
    echo json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . "\n";
}

function isLocalAppUrl(string $url): bool
{
    $host = strtolower((string) (parse_url($url, PHP_URL_HOST) ?: ''));
    if ($host === '') {
        $host = strtolower(preg_replace('#^https?://#i', '', $url) ?? '');
        $host = explode('/', $host)[0];
        $host = explode(':', $host)[0];
    }
    return in_array($host, ['iseo-report-hub.test', 'localhost', '127.0.0.1'], true);
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

function countWhere(PDO $pdo, string $sql, array $params = []): int
{
    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    return (int) $stmt->fetchColumn();
}

/**
 * @return array<string, int|string>
 */
function captureBaseline(PDO $pdo): array
{
    $export4 = (string) $pdo->query(
        'SELECT COALESCE(LEFT(checksum_sha256, 20), "") FROM report_exports WHERE id = 4'
    )->fetchColumn();
    $share7 = (string) $pdo->query(
        'SELECT COALESCE(status, "") FROM report_export_shares WHERE id = 7'
    )->fetchColumn();
    $r1Updated = (string) $pdo->query(
        'SELECT COALESCE(MAX(updated_at), "") FROM report_blocks WHERE monthly_report_content_id = 1'
    )->fetchColumn();
    $r1Sha = (string) $pdo->query(
        'SELECT SHA2(GROUP_CONCAT(id, ":", IFNULL(body, "") ORDER BY id SEPARATOR "|"), 256)
         FROM report_blocks WHERE monthly_report_content_id = 1'
    )->fetchColumn();

    return [
        'clients' => countTable($pdo, 'clients'),
        'projects' => countTable($pdo, 'projects'),
        'sites' => countTable($pdo, 'sites'),
        'reporting_periods' => countTable($pdo, 'reporting_periods'),
        'monthly_report_contents' => countTable($pdo, 'monthly_report_contents'),
        'report_blocks' => countTable($pdo, 'report_blocks'),
        'monthly_report_work_entries' => countTable($pdo, 'monthly_report_work_entries'),
        'weekly_checkpoints' => countTable($pdo, 'weekly_checkpoints'),
        'report_snapshots' => countTable($pdo, 'report_snapshots'),
        'report_exports' => countTable($pdo, 'report_exports'),
        'report_export_shares' => countTable($pdo, 'report_export_shares'),
        'shares_active' => countWhere($pdo, "SELECT COUNT(*) FROM report_export_shares WHERE status = 'active'"),
        'shares_revoked' => countWhere($pdo, "SELECT COUNT(*) FROM report_export_shares WHERE status = 'revoked'"),
        'seo_work_categories' => countTable($pdo, 'seo_work_categories'),
        'seo_work_items' => countTable($pdo, 'seo_work_items'),
        'users' => countTable($pdo, 'users'),
        'audit_log' => countTable($pdo, 'audit_log'),
        'blocks_r1' => countWhere($pdo, 'SELECT COUNT(*) FROM report_blocks WHERE monthly_report_content_id = 1'),
        'entries_r1' => countWhere($pdo, 'SELECT COUNT(*) FROM monthly_report_work_entries WHERE monthly_report_id = 1'),
        'blocks_r5' => countWhere($pdo, 'SELECT COUNT(*) FROM report_blocks WHERE monthly_report_content_id = 5'),
        'entries_r5' => countWhere($pdo, 'SELECT COUNT(*) FROM monthly_report_work_entries WHERE monthly_report_id = 5'),
        'r1_status' => (string) $pdo->query('SELECT COALESCE(status, "") FROM monthly_report_contents WHERE id = 1')->fetchColumn(),
        'r5_status' => (string) $pdo->query('SELECT COALESCE(status, "") FROM monthly_report_contents WHERE id = 5')->fetchColumn(),
        'export4_checksum_prefix' => $export4,
        'share7_status' => $share7,
        'r1_block_updated_max' => $r1Updated,
        'r1_block_body_sha' => $r1Sha,
    ];
}

/**
 * @return array{snapshots:int,exports:int,shares:int}
 */
function publicationCounts(PDO $pdo, int $monthlyId): array
{
    return [
        'snapshots' => countWhere(
            $pdo,
            'SELECT COUNT(*) FROM report_snapshots WHERE monthly_report_content_id = :id',
            [':id' => $monthlyId]
        ),
        'exports' => countWhere(
            $pdo,
            'SELECT COUNT(*) FROM report_exports WHERE monthly_report_content_id = :id',
            [':id' => $monthlyId]
        ),
        'shares' => countWhere(
            $pdo,
            'SELECT COUNT(*)
             FROM report_export_shares s
             INNER JOIN report_exports e ON e.id = s.report_export_id
             WHERE e.monthly_report_content_id = :id',
            [':id' => $monthlyId]
        ),
    ];
}

function choosePeriodKey(PDO $pdo, int $projectId): string
{
    $year = 2099;
    $month = 1;
    while ($year <= 2105) {
        $key = sprintf('%04d-%02d', $year, $month);
        $stmt = $pdo->prepare(
            'SELECT id FROM reporting_periods WHERE project_id = :pid AND period_key = :pkey LIMIT 1'
        );
        $stmt->execute([':pid' => $projectId, ':pkey' => $key]);
        if ($stmt->fetchColumn() === false) {
            return $key;
        }
        $month++;
        if ($month > 12) {
            $month = 1;
            $year++;
        }
    }
    stop('No unused synthetic period_key available in 2099-2105.');
}

function periodDates(string $periodKey): array
{
    $dt = DateTimeImmutable::createFromFormat('!Y-m', $periodKey);
    if ($dt === false) {
        stop('Invalid period_key.');
    }
    return [
        'start' => $dt->format('Y-m-01'),
        'end' => $dt->format('Y-m-t'),
    ];
}

function generateMarker(): string
{
    return MARKER_PREFIX . gmdate('Ymd_His');
}

function displayTitle(string $marker): string
{
    return TITLE_PREFIX . ' — ' . $marker . ' — ' . LOCAL_MARKER;
}

/**
 * @return list<array{block_key:string,title:string,sort_order:int,body:string,summary:string,writable:bool}>
 */
function blockSpecs(string $marker): array
{
    $manual = 'Ручной блок фикстуры. Не применяется автосборкой. ' . LOCAL_MARKER . "\n" . $marker;
    $auto = 'Автоблок-заглушка. ' . LOCAL_MARKER . "\n" . $marker;
    return [
        ['block_key' => 'executive_summary', 'title' => 'Краткое резюме', 'sort_order' => 10, 'body' => $manual, 'summary' => LOCAL_MARKER, 'writable' => false],
        ['block_key' => 'work_completed', 'title' => 'Что сделали', 'sort_order' => 20, 'body' => $auto, 'summary' => LOCAL_MARKER, 'writable' => true],
        ['block_key' => 'results_summary', 'title' => 'Результаты', 'sort_order' => 30, 'body' => $manual, 'summary' => LOCAL_MARKER, 'writable' => false],
        ['block_key' => 'risks_and_blockers', 'title' => 'Риски и блокеры', 'sort_order' => 40, 'body' => $auto, 'summary' => LOCAL_MARKER, 'writable' => true],
        ['block_key' => 'key_findings', 'title' => 'Ключевые выводы', 'sort_order' => 50, 'body' => $manual, 'summary' => LOCAL_MARKER, 'writable' => false],
        [
            'block_key' => 'next_month_plan',
            'title' => 'План на следующий месяц',
            'sort_order' => 60,
            'body' => PLAN_PLACEHOLDER . "\n\n" . $marker,
            'summary' => PLAN_SUMMARY,
            'writable' => true,
        ],
    ];
}

/**
 * @return list<array<string, mixed>>
 */
function entrySpecs(string $marker): array
{
    return [
        [
            'title' => 'Проведен технический мониторинг сайта',
            'description' => 'Выполнен плановый технический мониторинг демо-проекта.',
            'status' => 'done',
            'period_role' => 'done',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Выполнен технический мониторинг сайта.',
            'internal_note' => $marker,
            'work_item_slug' => 'tech-site-monitoring',
            'category_slug' => 'technical_monitoring',
            'sort_order' => 10,
        ],
        [
            'title' => 'Проверена индексация ключевых страниц',
            'description' => 'Проверена индексация ключевых страниц демо-проекта.',
            'status' => 'done',
            'period_role' => 'done',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Проверена индексация ключевых страниц.',
            'internal_note' => $marker,
            'work_item_slug' => 'tech-indexation-check',
            'category_slug' => 'technical_monitoring',
            'sort_order' => 20,
        ],
        [
            'title' => 'Актуализирована семантика по приоритетным группам',
            'description' => 'Выполнена актуализация семантики по приоритетным группам.',
            'status' => 'done',
            'period_role' => 'done',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Актуализирована семантика по приоритетным группам.',
            'internal_note' => $marker,
            'work_item_slug' => 'semantics-refresh',
            'category_slug' => 'semantic_core',
            'sort_order' => 30,
        ],
        [
            'title' => 'Подготовлены рекомендации по коммерческим факторам',
            'description' => 'Подготовлен набор рекомендаций по коммерческим факторам.',
            'status' => 'done',
            'period_role' => 'done',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Подготовлены рекомендации по коммерческим факторам.',
            'internal_note' => $marker,
            'work_item_slug' => 'commercial-page-recommendations',
            'category_slug' => 'commercial_factors',
            'sort_order' => 40,
        ],
        [
            'title' => 'Запланирована доработка мета-тегов',
            'description' => 'В план следующего периода включена доработка мета-тегов.',
            'status' => 'planned',
            'period_role' => 'planned_next',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Запланирована доработка мета-тегов.',
            'internal_note' => $marker,
            'work_item_slug' => 'onpage-meta-optimization',
            'category_slug' => 'onpage',
            'sort_order' => 50,
        ],
        [
            'title' => 'Запланирована подготовка новых текстов',
            'description' => 'В план следующего периода включена подготовка новых текстов.',
            'status' => 'planned',
            'period_role' => 'planned_next',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Запланирована подготовка новых текстов.',
            'internal_note' => $marker,
            'work_item_slug' => 'content-tz-prep',
            'category_slug' => 'content',
            'sort_order' => 60,
        ],
        [
            'title' => 'Требуется согласование приоритетных страниц',
            'description' => 'Нужно согласовать список приоритетных страниц для следующих работ.',
            'status' => 'blocked',
            'period_role' => 'risk',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Требуется согласование приоритетных страниц.',
            'internal_note' => $marker,
            'work_item_slug' => null,
            'category_slug' => 'reporting',
            'sort_order' => 70,
        ],
    ];
}

function resolveId(PDO $pdo, string $sql, array $params, string $label): int
{
    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    $id = $stmt->fetchColumn();
    if ($id === false) {
        stop('Required ' . $label . ' is missing.');
    }
    return (int) $id;
}

function existingMarkedIds(PDO $pdo): array
{
    $periods = $pdo->query(
        "SELECT id, period_key, title FROM reporting_periods
         WHERE title LIKE '%MARS_FIXTURE_SUMMARY_APPLY_%'
            OR summary LIKE '%MARS_FIXTURE_SUMMARY_APPLY_%'"
    )->fetchAll(PDO::FETCH_ASSOC) ?: [];
    $monthlies = $pdo->query(
        "SELECT id, title FROM monthly_report_contents
         WHERE title LIKE '%MARS_FIXTURE_SUMMARY_APPLY_%'
            OR internal_notes LIKE '%MARS_FIXTURE_SUMMARY_APPLY_%'"
    )->fetchAll(PDO::FETCH_ASSOC) ?: [];
    return ['periods' => $periods, 'monthlies' => $monthlies];
}

function loadIdsJson(string $path): array
{
    if (!is_file($path)) {
        stop('fixture-ids JSON not found: path omitted from output for safety. Provide --ids=.');
    }
    $raw = file_get_contents($path);
    if ($raw === false || trim($raw) === '') {
        stop('fixture-ids JSON is empty.');
    }
    $data = json_decode($raw, true);
    if (!is_array($data)) {
        stop('fixture-ids JSON is invalid.');
    }
    return $data;
}

function writeIdsJson(string $path, array $data): void
{
    $dir = dirname($path);
    if (!is_dir($dir) && !mkdir($dir, 0775, true) && !is_dir($dir)) {
        stop('Cannot create fixture-ids directory.');
    }
    $json = json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
    if ($json === false) {
        stop('Cannot encode fixture-ids JSON.');
    }
    if (file_put_contents($path, $json . "\n") === false) {
        stop('Cannot write fixture-ids JSON.');
    }
}

function markerRowsRemaining(PDO $pdo, string $marker): array
{
    return [
        'periods' => countWhere(
            $pdo,
            'SELECT COUNT(*) FROM reporting_periods WHERE summary = :m OR title LIKE :like',
            [':m' => $marker, ':like' => '%' . $marker . '%']
        ),
        'monthlies' => countWhere(
            $pdo,
            'SELECT COUNT(*) FROM monthly_report_contents WHERE internal_notes = :m OR title LIKE :like',
            [':m' => $marker, ':like' => '%' . $marker . '%']
        ),
        'blocks' => countWhere(
            $pdo,
            "SELECT COUNT(*) FROM report_blocks
             WHERE JSON_UNQUOTE(JSON_EXTRACT(data_json, '$.mars_fixture_marker')) = :m",
            [':m' => $marker]
        ),
        'entries' => countWhere(
            $pdo,
            'SELECT COUNT(*) FROM monthly_report_work_entries WHERE internal_note = :m',
            [':m' => $marker]
        ),
    ];
}

function runCreate(PDO $pdo, string $idsPath, ?string $dumpFile): void
{
    if (is_file($idsPath)) {
        $existing = json_decode((string) file_get_contents($idsPath), true);
        if (is_array($existing)) {
            $monthlyId = (int) ($existing['created']['monthly_id'] ?? 0);
            $marker = (string) ($existing['marker'] ?? '');
            if ($monthlyId > 0 && $marker !== '') {
                $still = countWhere(
                    $pdo,
                    'SELECT COUNT(*) FROM monthly_report_contents WHERE id = :id AND internal_notes = :m',
                    [':id' => $monthlyId, ':m' => $marker]
                );
                if ($still > 0) {
                    stop('Previous fixture still present. Run --cleanup first. monthly_id=' . $monthlyId);
                }
            }
        }
    }

    $marked = existingMarkedIds($pdo);
    if ($marked['periods'] !== [] || $marked['monthlies'] !== []) {
        $ids = [];
        foreach ($marked['monthlies'] as $row) {
            $ids[] = 'monthly:' . (int) $row['id'];
        }
        foreach ($marked['periods'] as $row) {
            $ids[] = 'period:' . (int) $row['id'];
        }
        stop('Marked fixture rows already exist. Do not guess cleanup. ids=' . implode(',', $ids));
    }

    $clientId = resolveId($pdo, 'SELECT id FROM clients WHERE id = :id LIMIT 1', [':id' => DEFAULT_CLIENT_ID], 'client id 1');
    $projectId = resolveId(
        $pdo,
        'SELECT id FROM projects WHERE id = :id AND client_id = :cid LIMIT 1',
        [':id' => DEFAULT_PROJECT_ID, ':cid' => $clientId],
        'project id 1'
    );
    $siteId = resolveId(
        $pdo,
        'SELECT id FROM sites WHERE id = :id AND project_id = :pid LIMIT 1',
        [':id' => DEFAULT_SITE_ID, ':pid' => $projectId],
        'site id 1'
    );
    $createdBy = resolveId($pdo, 'SELECT id FROM users WHERE id = :id LIMIT 1', [':id' => DEFAULT_CREATED_BY], 'user id 1');
    $ownerId = resolveId($pdo, 'SELECT id FROM users WHERE id = :id LIMIT 1', [':id' => DEFAULT_OWNER_ID], 'user id 2');

    $marker = generateMarker();
    $title = displayTitle($marker);
    $periodKey = choosePeriodKey($pdo, $projectId);
    $dates = periodDates($periodKey);
    $baseline = captureBaseline($pdo);
    $dataJson = json_encode(['mars_fixture_marker' => $marker], JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);

    $entrySpecs = entrySpecs($marker);
    $resolvedEntries = [];
    foreach ($entrySpecs as $spec) {
        $categoryId = resolveId(
            $pdo,
            'SELECT id FROM seo_work_categories WHERE slug = :slug LIMIT 1',
            [':slug' => (string) $spec['category_slug']],
            'category slug ' . $spec['category_slug']
        );
        $workItemId = null;
        if ($spec['work_item_slug'] !== null) {
            $workItemId = resolveId(
                $pdo,
                'SELECT id FROM seo_work_items WHERE slug = :slug LIMIT 1',
                [':slug' => (string) $spec['work_item_slug']],
                'work item slug ' . $spec['work_item_slug']
            );
        }
        $spec['category_id'] = $categoryId;
        $spec['work_item_id'] = $workItemId;
        $resolvedEntries[] = $spec;
    }

    $periodId = 0;
    $monthlyId = 0;
    $blockIds = [];
    $entryIds = [];

    try {
        $pdo->beginTransaction();

        $insPeriod = $pdo->prepare(
            'INSERT INTO reporting_periods
             (project_id, period_key, period_start, period_end, status, title, summary,
              owner_user_id, created_by, updated_by, finalized_at)
             VALUES
             (:project_id, :period_key, :period_start, :period_end, :status, :title, :summary,
              :owner_user_id, :created_by, :updated_by, NULL)'
        );
        $insPeriod->execute([
            ':project_id' => $projectId,
            ':period_key' => $periodKey,
            ':period_start' => $dates['start'],
            ':period_end' => $dates['end'],
            ':status' => 'active',
            ':title' => $title,
            ':summary' => $marker,
            ':owner_user_id' => $ownerId,
            ':created_by' => $createdBy,
            ':updated_by' => $createdBy,
        ]);
        $periodId = (int) $pdo->lastInsertId();

        $insMonthly = $pdo->prepare(
            'INSERT INTO monthly_report_contents
             (reporting_period_id, status, title, executive_summary, work_completed, results_summary,
              key_findings, risks_and_blockers, next_month_plan, client_notes, internal_notes,
              source_weekly_checkpoint_ids, owner_user_id, created_by, updated_by, finalized_at)
             VALUES
             (:reporting_period_id, :status, :title, NULL, NULL, NULL,
              NULL, NULL, NULL, NULL, :internal_notes,
              :source_weekly, :owner_user_id, :created_by, :updated_by, NULL)'
        );
        $insMonthly->execute([
            ':reporting_period_id' => $periodId,
            ':status' => 'in_progress',
            ':title' => $title,
            ':internal_notes' => $marker,
            ':source_weekly' => '[]',
            ':owner_user_id' => $ownerId,
            ':created_by' => $createdBy,
            ':updated_by' => $createdBy,
        ]);
        $monthlyId = (int) $pdo->lastInsertId();

        if (in_array($monthlyId, PROTECTED_MONTHLY_IDS, true)) {
            $pdo->rollBack();
            stop('Created monthly id collided with protected id ' . $monthlyId);
        }

        $insBlock = $pdo->prepare(
            'INSERT INTO report_blocks
             (monthly_report_content_id, block_key, block_type, sort_order, status, title, body, summary,
              data_json, source_weekly_checkpoint_ids, owner_user_id, created_by, updated_by)
             VALUES
             (:monthly_id, :block_key, :block_type, :sort_order, :status, :title, :body, :summary,
              :data_json, :source_weekly, :owner_user_id, :created_by, :updated_by)'
        );
        foreach (blockSpecs($marker) as $block) {
            $insBlock->execute([
                ':monthly_id' => $monthlyId,
                ':block_key' => $block['block_key'],
                ':block_type' => $block['block_key'],
                ':sort_order' => $block['sort_order'],
                ':status' => 'draft',
                ':title' => $block['title'],
                ':body' => $block['body'],
                ':summary' => $block['summary'],
                ':data_json' => $dataJson,
                ':source_weekly' => '[]',
                ':owner_user_id' => $ownerId,
                ':created_by' => $createdBy,
                ':updated_by' => $createdBy,
            ]);
            $blockIds[$block['block_key']] = (int) $pdo->lastInsertId();
        }

        $insEntry = $pdo->prepare(
            'INSERT INTO monthly_report_work_entries
             (monthly_report_id, work_item_id, category_id, title, description, status, period_role,
              client_visibility, client_summary, internal_note, evidence_note, sort_order,
              created_by_user_id, updated_by_user_id)
             VALUES
             (:monthly_report_id, :work_item_id, :category_id, :title, :description, :status, :period_role,
              :client_visibility, :client_summary, :internal_note, :evidence_note, :sort_order,
              :created_by_user_id, :updated_by_user_id)'
        );
        foreach ($resolvedEntries as $entry) {
            $insEntry->execute([
                ':monthly_report_id' => $monthlyId,
                ':work_item_id' => $entry['work_item_id'],
                ':category_id' => $entry['category_id'],
                ':title' => $entry['title'],
                ':description' => $entry['description'],
                ':status' => $entry['status'],
                ':period_role' => $entry['period_role'],
                ':client_visibility' => $entry['client_visibility'],
                ':client_summary' => $entry['client_summary'],
                ':internal_note' => $entry['internal_note'],
                ':evidence_note' => $marker,
                ':sort_order' => $entry['sort_order'],
                ':created_by_user_id' => $createdBy,
                ':updated_by_user_id' => $createdBy,
            ]);
            $entryIds[] = (int) $pdo->lastInsertId();
        }

        $pub = publicationCounts($pdo, $monthlyId);
        if ($pub['snapshots'] !== 0 || $pub['exports'] !== 0 || $pub['shares'] !== 0) {
            $pdo->rollBack();
            stop('Fixture monthly unexpectedly has publication rows.');
        }

        $afterR1 = (string) $pdo->query(
            'SELECT COALESCE(MAX(updated_at), "") FROM report_blocks WHERE monthly_report_content_id = 1'
        )->fetchColumn();
        if ($afterR1 !== (string) $baseline['r1_block_updated_max']) {
            $pdo->rollBack();
            stop('Report id 1 block timestamps changed during fixture create.');
        }

        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) {
            $pdo->rollBack();
        }
        fwrite(STDERR, "CREATE FAILED (details redacted).\n");
        exit(9);
    }

    $payload = [
        'ok' => true,
        'mode' => 'create',
        'marker' => $marker,
        'local_fixture_only' => true,
        'created_at' => gmdate('c'),
        'report_id_1_protected' => true,
        'report_id_5_protected' => true,
        'reused' => [
            'client_id' => $clientId,
            'project_id' => $projectId,
            'site_id' => $siteId,
            'user_ids' => [$createdBy, $ownerId],
            'created_by_user_id' => $createdBy,
            'owner_user_id' => $ownerId,
        ],
        'created' => [
            'period_id' => $periodId,
            'period_key' => $periodKey,
            'period_created_by_fixture' => true,
            'monthly_id' => $monthlyId,
            'monthly_status' => 'in_progress',
            'block_ids' => $blockIds,
            'entry_ids' => $entryIds,
        ],
        'publication' => publicationCounts($pdo, $monthlyId),
        'baseline_counts' => $baseline,
        'dump_filename' => $dumpFile,
        'ids_path' => $idsPath,
    ];
    writeIdsJson($idsPath, $payload);
    emitJson($payload);
}

function assertMarkerOnPeriod(PDO $pdo, int $id, string $marker): void
{
    $stmt = $pdo->prepare('SELECT id, summary, title FROM reporting_periods WHERE id = :id LIMIT 1');
    $stmt->execute([':id' => $id]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!is_array($row)) {
        stop('Fixture period id not found: ' . $id);
    }
    if ((string) $row['summary'] !== $marker && !str_contains((string) $row['title'], $marker)) {
        stop('Period marker mismatch for id ' . $id);
    }
}

function assertMarkerOnMonthly(PDO $pdo, int $id, string $marker): void
{
    if (in_array($id, PROTECTED_MONTHLY_IDS, true)) {
        stop('Cleanup refused: protected monthly id ' . $id);
    }
    $stmt = $pdo->prepare('SELECT id, internal_notes, title FROM monthly_report_contents WHERE id = :id LIMIT 1');
    $stmt->execute([':id' => $id]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!is_array($row)) {
        stop('Fixture monthly id not found: ' . $id);
    }
    if ((string) $row['internal_notes'] !== $marker && !str_contains((string) $row['title'], $marker)) {
        stop('Monthly marker mismatch for id ' . $id);
    }
}

function assertMarkerOnBlock(PDO $pdo, int $id, string $marker): void
{
    $stmt = $pdo->prepare(
        "SELECT id, monthly_report_content_id,
                JSON_UNQUOTE(JSON_EXTRACT(data_json, '$.mars_fixture_marker')) AS marker
         FROM report_blocks WHERE id = :id LIMIT 1"
    );
    $stmt->execute([':id' => $id]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!is_array($row)) {
        stop('Fixture block id not found: ' . $id);
    }
    $parent = (int) $row['monthly_report_content_id'];
    if (in_array($parent, PROTECTED_MONTHLY_IDS, true)) {
        stop('Cleanup refused: block belongs to protected monthly ' . $parent);
    }
    if ((string) $row['marker'] !== $marker) {
        stop('Block marker mismatch for id ' . $id);
    }
}

function assertMarkerOnEntry(PDO $pdo, int $id, string $marker): void
{
    $stmt = $pdo->prepare(
        'SELECT id, monthly_report_id, internal_note FROM monthly_report_work_entries WHERE id = :id LIMIT 1'
    );
    $stmt->execute([':id' => $id]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!is_array($row)) {
        stop('Fixture entry id not found: ' . $id);
    }
    $parent = (int) $row['monthly_report_id'];
    if (in_array($parent, PROTECTED_MONTHLY_IDS, true)) {
        stop('Cleanup refused: entry belongs to protected monthly ' . $parent);
    }
    if ((string) $row['internal_note'] !== $marker) {
        stop('Entry marker mismatch for id ' . $id);
    }
}

function deleteByIds(PDO $pdo, string $table, string $idColumn, array $ids): int
{
    $ids = array_values(array_filter(array_map('intval', $ids), static fn (int $id): bool => $id > 0));
    if ($ids === []) {
        return 0;
    }
    $placeholders = implode(',', array_fill(0, count($ids), '?'));
    $stmt = $pdo->prepare('DELETE FROM `' . $table . '` WHERE `' . $idColumn . '` IN (' . $placeholders . ')');
    $stmt->execute($ids);
    return $stmt->rowCount();
}

function countsMatchBaseline(array $before, array $after): array
{
    $keys = [
        'clients', 'projects', 'sites', 'reporting_periods', 'monthly_report_contents',
        'report_blocks', 'monthly_report_work_entries', 'weekly_checkpoints',
        'report_snapshots', 'report_exports', 'report_export_shares',
        'shares_active', 'shares_revoked', 'seo_work_categories', 'seo_work_items', 'users',
        'blocks_r1', 'entries_r1', 'blocks_r5', 'entries_r5',
        'r1_status', 'r5_status', 'export4_checksum_prefix', 'share7_status',
        'r1_block_updated_max', 'r1_block_body_sha',
    ];
    $mismatches = [];
    foreach ($keys as $key) {
        if ((string) ($before[$key] ?? '') !== (string) ($after[$key] ?? '')) {
            $mismatches[$key] = [
                'before' => $before[$key] ?? null,
                'after' => $after[$key] ?? null,
            ];
        }
    }
    return $mismatches;
}

function runCleanup(PDO $pdo, string $idsPath): void
{
    $data = loadIdsJson($idsPath);
    $marker = (string) ($data['marker'] ?? '');
    if ($marker === '' || !str_starts_with($marker, MARKER_PREFIX)) {
        stop('fixture-ids marker missing or invalid.');
    }

    $created = is_array($data['created'] ?? null) ? $data['created'] : [];
    $periodId = (int) ($created['period_id'] ?? 0);
    $monthlyId = (int) ($created['monthly_id'] ?? 0);
    $blockIds = is_array($created['block_ids'] ?? null) ? array_values($created['block_ids']) : [];
    $entryIds = is_array($created['entry_ids'] ?? null) ? array_values($created['entry_ids']) : [];
    $periodOwned = !empty($created['period_created_by_fixture']);

    if ($monthlyId <= 0 || $periodId <= 0) {
        stop('fixture-ids missing monthly/period id.');
    }
    if (in_array($monthlyId, PROTECTED_MONTHLY_IDS, true)) {
        stop('Cleanup refused: protected monthly id ' . $monthlyId);
    }
    if (in_array($periodId, [1, 3], true)) {
        stop('Cleanup refused: protected period id ' . $periodId);
    }

    assertMarkerOnMonthly($pdo, $monthlyId, $marker);
    assertMarkerOnPeriod($pdo, $periodId, $marker);
    foreach ($blockIds as $blockId) {
        assertMarkerOnBlock($pdo, (int) $blockId, $marker);
    }
    foreach ($entryIds as $entryId) {
        assertMarkerOnEntry($pdo, (int) $entryId, $marker);
    }

    $pub = publicationCounts($pdo, $monthlyId);
    if ($pub['snapshots'] !== 0 || $pub['exports'] !== 0 || $pub['shares'] !== 0) {
        stop(
            'Fixture monthly has snapshot/export/share rows. Cleanup refused. '
            . 'snapshots=' . $pub['snapshots']
            . ' exports=' . $pub['exports']
            . ' shares=' . $pub['shares']
        );
    }

    $deleted = [
        'report_blocks' => 0,
        'monthly_report_work_entries' => 0,
        'monthly_report_contents' => 0,
        'reporting_periods' => 0,
    ];

    try {
        $pdo->beginTransaction();
        $deleted['report_blocks'] = deleteByIds($pdo, 'report_blocks', 'id', $blockIds);
        $deleted['monthly_report_work_entries'] = deleteByIds($pdo, 'monthly_report_work_entries', 'id', $entryIds);
        $deleted['monthly_report_contents'] = deleteByIds($pdo, 'monthly_report_contents', 'id', [$monthlyId]);
        if ($periodOwned) {
            $deleted['reporting_periods'] = deleteByIds($pdo, 'reporting_periods', 'id', [$periodId]);
        }
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) {
            $pdo->rollBack();
        }
        fwrite(STDERR, "CLEANUP FAILED (details redacted). Keep backup and fixture rows.\n");
        exit(9);
    }

    $remaining = markerRowsRemaining($pdo, $marker);
    $after = captureBaseline($pdo);
    $baseline = is_array($data['baseline_counts'] ?? null) ? $data['baseline_counts'] : [];
    $mismatches = $baseline !== [] ? countsMatchBaseline($baseline, $after) : ['baseline_missing' => true];

    $coreMismatches = $mismatches;
    unset($coreMismatches['baseline_missing']);

    $payload = [
        'ok' => array_sum($remaining) === 0 && $coreMismatches === [],
        'mode' => 'cleanup',
        'marker' => $marker,
        'deleted' => $deleted,
        'remaining_marker_rows' => $remaining,
        'publication_at_stop_check' => $pub,
        'baseline_mismatches' => $coreMismatches,
        'audit_log_before' => $baseline['audit_log'] ?? null,
        'audit_log_after' => $after['audit_log'],
        'after_counts' => $after,
    ];

    $cleanedPath = preg_replace('/\.json$/', '.cleaned.json', $idsPath) ?? ($idsPath . '.cleaned.json');
    writeIdsJson($cleanedPath, $payload + ['source_ids_path' => $idsPath]);

    if (array_sum($remaining) !== 0) {
        emitJson($payload);
        stop('Marker rows remain after exact-id cleanup.');
    }
    if ($coreMismatches !== []) {
        emitJson($payload);
        stop('Baseline counts not restored after cleanup.');
    }

    emitJson($payload);
}

$args = parseArgs($argv);
if ($args['help']) {
    printHelp();
    exit(0);
}
if ($args['mode'] === null) {
    printHelp();
    refuse('Specify --create or --cleanup.');
}
if (!$args['confirm']) {
    refuse('--confirm-local-fixture is required.');
}

$root = dirname(__DIR__);
$app = require $root . DIRECTORY_SEPARATOR . 'app' . DIRECTORY_SEPARATOR . 'bootstrap.php';

/** @var \Iseo\Services\DatabaseService $db */
$db = $app['db'];
/** @var \Iseo\Services\ConfigService $config */
$config = $app['config'];

$appEnv = strtolower((string) $config->get('app.env', ''));
$appUrl = (string) $config->get('app.url', '');
$host = (string) $config->get('database.host', '');
$name = (string) $config->get('database.database', '');

if ($appEnv !== REQUIRED_APP_ENV) {
    refuse('APP_ENV must be exactly local.');
}
if (!isLocalAppUrl($appUrl)) {
    refuse('APP_URL host is not local.');
}
if (!$db->isConfigured()) {
    refuse('database not configured (.env.local / DB_* missing).');
}
if ($host !== REQUIRED_HOST) {
    refuse('DB host must be exactly ' . REQUIRED_HOST . '.');
}
if ($name !== REQUIRED_DB) {
    refuse('target DB must be exactly ' . REQUIRED_DB . '.');
}

try {
    $db->enableLocalDevDatabaseGuard();
    $db->assertLocalDevDatabase();
    $pdo = $db->connect();
    $actual = (string) $pdo->query('SELECT DATABASE()')->fetchColumn();
    if ($actual !== REQUIRED_DB) {
        refuse('connected DB is not ' . REQUIRED_DB . '.');
    }
} catch (Throwable $e) {
    fwrite(STDERR, "DB connection failed (details redacted).\n");
    exit(4);
}

$requiredTables = [
    'clients', 'projects', 'sites', 'users', 'reporting_periods', 'monthly_report_contents',
    'report_blocks', 'monthly_report_work_entries', 'seo_work_categories', 'seo_work_items',
    'weekly_checkpoints', 'report_snapshots', 'report_exports', 'report_export_shares', 'audit_log',
];
foreach ($requiredTables as $table) {
    if (!tableExists($pdo, $table)) {
        refuse('required table missing: ' . $table);
    }
}

$idsPath = $args['ids'] !== null && $args['ids'] !== '' ? $args['ids'] : DEFAULT_IDS_PATH;

if ($args['mode'] === 'create') {
    runCreate($pdo, $idsPath, $args['dump_file']);
    exit(0);
}

if ($args['mode'] === 'cleanup') {
    runCleanup($pdo, $idsPath);
    exit(0);
}

refuse('Unknown mode.');

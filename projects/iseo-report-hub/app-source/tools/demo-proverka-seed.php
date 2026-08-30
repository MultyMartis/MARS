<?php
declare(strict_types=1);

/**
 * Guarded local-only seed for demo user + ПРОВЕРКА.рф scenario.
 *
 * Usage:
 *   php tools/demo-proverka-seed.php --status
 *   php tools/demo-proverka-seed.php --create --confirm-local-demo-seed [--ids=path] [--evidence-dir=path]
 *   php tools/demo-proverka-seed.php --cleanup --confirm-local-demo-seed [--ids=path]
 *
 * Safety:
 * - CLI only
 * - APP_ENV=local, DB iseo_report_hub_dev @ 127.0.0.1, local APP_URL
 * - mutations require --confirm-local-demo-seed
 * - never mutates monthly report ids 1 or 5
 * - never creates export/share/snapshot/PDF
 * - never prints password hashes / tokens / cookies
 */

if (PHP_SAPI !== 'cli') {
    fwrite(STDERR, "REFUSED: CLI only.\n");
    exit(1);
}

const REQUIRED_DB = 'iseo_report_hub_dev';
const REQUIRED_HOST = '127.0.0.1';
const REQUIRED_APP_ENV = 'local';
const MARKER = 'MARS_DEMO_PROVERKA_20260821';
const CLIENT_SLUG = 'proverka-demo';
const PROJECT_SLUG = 'proverka-demo';
const CLIENT_NAME = "ПРОВЕРКА.рф";
const PROJECT_NAME = "SEO-продвижение ПРОВЕРКА.рф";
const SITE_LABEL = "ПРОВЕРКА.рф";
const SITE_URL = 'https://proverka.example';
const USER_NAME = 'Тест Проверочнов';
const USER_EMAIL = 'test@mail.ru';
const USER_ROLE = 'seo_specialist';
const PROTECTED_MONTHLY_IDS = [1, 5];
const DEFAULT_EVIDENCE_ROOT = 'X:\\AI MARS STORAGE\\incoming\\iseo-report-hub\\demo-user-scenario-seed-implementation-01';

/**
 * @return array{
 *   mode:?string,
 *   confirm:bool,
 *   ids:?string,
 *   evidence_dir:?string,
 *   help:bool
 * }
 */
function parseArgs(array $argv): array
{
    $out = [
        'mode' => null,
        'confirm' => false,
        'ids' => null,
        'evidence_dir' => null,
        'help' => false,
    ];
    foreach (array_slice($argv, 1) as $arg) {
        if ($arg === '--help' || $arg === '-h') {
            $out['help'] = true;
            continue;
        }
        if ($arg === '--status') {
            $out['mode'] = 'status';
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
        if ($arg === '--confirm-local-demo-seed') {
            $out['confirm'] = true;
            continue;
        }
        if (str_starts_with($arg, '--ids=')) {
            $out['ids'] = substr($arg, 6);
            continue;
        }
        if (str_starts_with($arg, '--evidence-dir=')) {
            $out['evidence_dir'] = substr($arg, 15);
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
    fwrite(STDOUT, "  php tools/demo-proverka-seed.php --status\n");
    fwrite(STDOUT, "  php tools/demo-proverka-seed.php --create --confirm-local-demo-seed [--ids=...] [--evidence-dir=...]\n");
    fwrite(STDOUT, "  php tools/demo-proverka-seed.php --cleanup --confirm-local-demo-seed [--ids=...]\n");
    fwrite(STDOUT, "Local iseo_report_hub_dev only. Never prints secrets/hashes.\n");
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
    $host = parse_url($url, PHP_URL_HOST);
    if (!is_string($host) || $host === '') {
        return false;
    }
    $host = strtolower($host);
    return in_array($host, ['localhost', '127.0.0.1', 'iseo-report-hub.test'], true)
        || str_ends_with($host, '.test')
        || str_ends_with($host, '.local');
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
 * @param array<string, int|string> $params
 */
function countWhere(PDO $pdo, string $sql, array $params = []): int
{
    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    return (int) $stmt->fetchColumn();
}

/**
 * @return array<string, mixed>
 */
function collectCounts(PDO $pdo): array
{
    $export4 = null;
    $stmt = $pdo->query(
        'SELECT id, monthly_report_content_id, format, status, file_size_bytes,
                LEFT(COALESCE(checksum_sha256, ""), 16) AS checksum_prefix
         FROM report_exports WHERE id = 4 LIMIT 1'
    );
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (is_array($row)) {
        $export4 = [
            'id' => (int) $row['id'],
            'monthly_report_content_id' => (int) $row['monthly_report_content_id'],
            'format' => (string) $row['format'],
            'status' => (string) $row['status'],
            'file_size_bytes' => $row['file_size_bytes'] !== null ? (int) $row['file_size_bytes'] : null,
            'checksum_prefix' => (string) $row['checksum_prefix'],
        ];
    }

    return [
        'users' => countTable($pdo, 'users'),
        'clients' => countTable($pdo, 'clients'),
        'projects' => countTable($pdo, 'projects'),
        'sites' => countTable($pdo, 'sites'),
        'reporting_periods' => countTable($pdo, 'reporting_periods'),
        'monthly_report_contents' => countTable($pdo, 'monthly_report_contents'),
        'report_blocks' => countTable($pdo, 'report_blocks'),
        'monthly_report_work_entries' => countTable($pdo, 'monthly_report_work_entries'),
        'report_exports' => countTable($pdo, 'report_exports'),
        'report_export_shares' => countTable($pdo, 'report_export_shares'),
        'report_snapshots' => countTable($pdo, 'report_snapshots'),
        'active_shares' => countWhere($pdo, 'SELECT COUNT(*) FROM report_export_shares WHERE revoked_at IS NULL'),
        'revoked_shares' => countWhere($pdo, 'SELECT COUNT(*) FROM report_export_shares WHERE revoked_at IS NOT NULL'),
        'blocks_r1' => countWhere($pdo, 'SELECT COUNT(*) FROM report_blocks WHERE monthly_report_content_id = 1'),
        'entries_r1' => countWhere($pdo, 'SELECT COUNT(*) FROM monthly_report_work_entries WHERE monthly_report_id = 1'),
        'blocks_r5' => countWhere($pdo, 'SELECT COUNT(*) FROM report_blocks WHERE monthly_report_content_id = 5'),
        'entries_r5' => countWhere($pdo, 'SELECT COUNT(*) FROM monthly_report_work_entries WHERE monthly_report_id = 5'),
        'export_4' => $export4,
        'marker_clients' => countWhere(
            $pdo,
            'SELECT COUNT(*) FROM clients WHERE slug = :slug OR notes LIKE :marker',
            [':slug' => CLIENT_SLUG, ':marker' => '%' . MARKER . '%']
        ),
        'user_test_mail_exists' => countWhere(
            $pdo,
            'SELECT COUNT(*) FROM users WHERE email = :email',
            [':email' => USER_EMAIL]
        ) > 0,
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

/**
 * @return array<string, mixed>|null
 */
function findDemoClient(PDO $pdo): ?array
{
    $stmt = $pdo->prepare(
        'SELECT id, name, slug, status, notes FROM clients
         WHERE slug = :slug OR notes LIKE :marker
         ORDER BY (slug = :slug2) DESC, id ASC LIMIT 1'
    );
    $stmt->execute([
        ':slug' => CLIENT_SLUG,
        ':slug2' => CLIENT_SLUG,
        ':marker' => '%' . MARKER . '%',
    ]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    return is_array($row) ? $row : null;
}

/**
 * @return array<string, mixed>|null
 */
function findDemoUser(PDO $pdo): ?array
{
    $stmt = $pdo->prepare(
        'SELECT u.id, u.name, u.email, u.status,
                GROUP_CONCAT(r.code ORDER BY r.code) AS roles
         FROM users u
         LEFT JOIN user_roles ur ON ur.user_id = u.id
         LEFT JOIN roles r ON r.id = ur.role_id
         WHERE u.email = :email
         GROUP BY u.id, u.name, u.email, u.status
         LIMIT 1'
    );
    $stmt->execute([':email' => USER_EMAIL]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!is_array($row)) {
        return null;
    }
    return [
        'id' => (int) $row['id'],
        'name' => (string) $row['name'],
        'email' => (string) $row['email'],
        'status' => (string) $row['status'],
        'roles' => $row['roles'] !== null ? (string) $row['roles'] : '',
    ];
}

/**
 * @return array<string, mixed>
 */
function discoverScenario(PDO $pdo): array
{
    $user = findDemoUser($pdo);
    $client = findDemoClient($pdo);
    $project = null;
    $site = null;
    $periodJuly = null;
    $periodAugust = null;
    $monthlyJuly = null;
    $monthlyAugust = null;
    $blockIdsJuly = [];
    $blockIdsAugust = [];
    $entryIdsJuly = [];
    $entryIdsAugust = [];
    $pubJuly = ['snapshots' => 0, 'exports' => 0, 'shares' => 0];
    $pubAugust = ['snapshots' => 0, 'exports' => 0, 'shares' => 0];

    if ($client !== null) {
        $clientId = (int) $client['id'];
        $stmt = $pdo->prepare(
            'SELECT id, client_id, name, slug, project_type, status
             FROM projects WHERE client_id = :cid AND slug = :slug LIMIT 1'
        );
        $stmt->execute([':cid' => $clientId, ':slug' => PROJECT_SLUG]);
        $project = $stmt->fetch(PDO::FETCH_ASSOC) ?: null;

        if (is_array($project)) {
            $projectId = (int) $project['id'];
            $stmt = $pdo->prepare(
                'SELECT id, project_id, url, label, is_primary
                 FROM sites WHERE project_id = :pid
                 ORDER BY is_primary DESC, id ASC LIMIT 1'
            );
            $stmt->execute([':pid' => $projectId]);
            $site = $stmt->fetch(PDO::FETCH_ASSOC) ?: null;

            foreach (['2026-07' => 'july', '2026-08' => 'august'] as $pkey => $label) {
                $stmt = $pdo->prepare(
                    'SELECT id, project_id, period_key, status, title
                     FROM reporting_periods
                     WHERE project_id = :pid AND period_key = :pkey LIMIT 1'
                );
                $stmt->execute([':pid' => $projectId, ':pkey' => $pkey]);
                $period = $stmt->fetch(PDO::FETCH_ASSOC) ?: null;
                if ($label === 'july') {
                    $periodJuly = $period;
                } else {
                    $periodAugust = $period;
                }
                if (!is_array($period)) {
                    continue;
                }
                $stmt = $pdo->prepare(
                    'SELECT id, reporting_period_id, status, title, finalized_at
                     FROM monthly_report_contents
                     WHERE reporting_period_id = :pid LIMIT 1'
                );
                $stmt->execute([':pid' => (int) $period['id']]);
                $monthly = $stmt->fetch(PDO::FETCH_ASSOC) ?: null;
                if ($label === 'july') {
                    $monthlyJuly = $monthly;
                } else {
                    $monthlyAugust = $monthly;
                }
                if (!is_array($monthly)) {
                    continue;
                }
                $mid = (int) $monthly['id'];
                if (in_array($mid, PROTECTED_MONTHLY_IDS, true)) {
                    stop('Discovered monthly id collides with protected report 1/5.');
                }
                $pub = publicationCounts($pdo, $mid);
                if ($label === 'july') {
                    $pubJuly = $pub;
                } else {
                    $pubAugust = $pub;
                }
                $stmt = $pdo->prepare(
                    'SELECT id FROM report_blocks WHERE monthly_report_content_id = :id ORDER BY sort_order, id'
                );
                $stmt->execute([':id' => $mid]);
                $ids = array_map('intval', $stmt->fetchAll(PDO::FETCH_COLUMN));
                $stmt = $pdo->prepare(
                    'SELECT id FROM monthly_report_work_entries WHERE monthly_report_id = :id ORDER BY sort_order, id'
                );
                $stmt->execute([':id' => $mid]);
                $eids = array_map('intval', $stmt->fetchAll(PDO::FETCH_COLUMN));
                if ($label === 'july') {
                    $blockIdsJuly = $ids;
                    $entryIdsJuly = $eids;
                } else {
                    $blockIdsAugust = $ids;
                    $entryIdsAugust = $eids;
                }
            }
        }
    }

    $complete = $user !== null
        && is_array($client)
        && is_array($project)
        && is_array($site)
        && is_array($periodJuly)
        && is_array($periodAugust)
        && is_array($monthlyJuly)
        && is_array($monthlyAugust)
        && count($blockIdsJuly) >= 6
        && count($blockIdsAugust) >= 6
        && count($entryIdsJuly) >= 10
        && count($entryIdsAugust) >= 8;

    $partial = ($client !== null || $user !== null)
        && !$complete;

    return [
        'marker' => MARKER,
        'user' => $user,
        'client' => $client,
        'project' => $project,
        'site' => $site,
        'period_july' => $periodJuly,
        'period_august' => $periodAugust,
        'monthly_july' => $monthlyJuly,
        'monthly_august' => $monthlyAugust,
        'block_ids_july' => $blockIdsJuly,
        'block_ids_august' => $blockIdsAugust,
        'work_entry_ids_july' => $entryIdsJuly,
        'work_entry_ids_august' => $entryIdsAugust,
        'publication_july' => $pubJuly,
        'publication_august' => $pubAugust,
        'complete' => $complete,
        'partial' => $partial,
        'counts' => collectCounts($pdo),
    ];
}

function ensureEvidenceDir(?string $requested): string
{
    if ($requested !== null && $requested !== '') {
        $dir = $requested;
    } else {
        $dir = DEFAULT_EVIDENCE_ROOT . DIRECTORY_SEPARATOR . date('Ymd-His');
    }
    if (!is_dir($dir) && !mkdir($dir, 0777, true) && !is_dir($dir)) {
        stop('Cannot create evidence directory.');
    }
    return $dir;
}

/**
 * @param array<string, mixed> $data
 */
function writeJsonFile(string $path, array $data): void
{
    $json = json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
    if ($json === false) {
        stop('JSON encode failed.');
    }
    if (file_put_contents($path, $json . "\n") === false) {
        stop('Failed writing ' . $path);
    }
}

function demoPassword(): string
{
    $fromEnv = getenv('ISEO_DEMO_SEED_PASSWORD');
    if (is_string($fromEnv) && $fromEnv !== '') {
        return $fromEnv;
    }
    // Operator-approved local demo password for this wave only.
    return 'test';
}

/**
 * @return array{executive_summary:string,results_summary:string,work_completed:string,key_findings:string,risks_and_blockers:string,next_month_plan:string,client_notes:string,internal_notes:string}
 */
function julyTexts(): array
{
    return [
        'executive_summary' =>
            'В июле выполнен первый полноценный этап SEO-подготовки проекта ПРОВЕРКА.рф: проведен технический аудит, собрана базовая семантика, проверена индексация ключевых страниц и подготовлен план доработок. Основной фокус месяца — убрать технические препятствия, привести структуру к понятному виду и подготовить основу для роста видимости в августе.',
        'results_summary' =>
            "Результаты июля 2026 (демо-данные для обучения):\n"
            . "- Органические визиты: 1 240 → 1 480\n"
            . "- Показы в поиске: 18 500 → 22 300\n"
            . "- Приоритетные URL в индексе: 42 → 47\n"
            . "- Технические ошибки (критичные/высокие): 18 → 7\n"
            . "- Лиды с органики (оценка): 9 → 12\n"
            . "- Запросов в топ-10 (мониторинговый набор): 14 → 19",
        'work_completed' =>
            "Что сделали в июле:\n"
            . "- Технический мониторинг и полный аудит (crawl ~1 100 URL)\n"
            . "- Проверка индексации приоритетных страниц\n"
            . "- Группировка семантики услуг (3 кластера)\n"
            . "- Обзор коммерческих факторов на ключевых URL\n"
            . "- Рекомендации по meta tags для 24 страниц\n"
            . "- Контент-план на август\n"
            . "- Список приоритетных страниц для роста\n"
            . "- Проверка целей аналитики",
        'key_findings' =>
            "Ключевые выводы:\n"
            . "- Техническая база заметно улучшилась после исправлений\n"
            . "- Приоритетным страницам нужно расширение коммерческих факторов\n"
            . "- Точки роста — низко- и среднечастотные запросы\n"
            . "- Контентное производство нужно продолжать в августе\n"
            . "- Требуется согласование приоритетов страниц с клиентом",
        'risks_and_blockers' =>
            "Риски и блокеры:\n"
            . "- Нужно согласование списка приоритетных страниц\n"
            . "- Части страниц нужны контентные и коммерческие доработки\n"
            . "- Критичных блокеров после технических правок нет",
        'next_month_plan' =>
            "План на август:\n"
            . "- Внедрить meta tags по сервисным кластерам\n"
            . "- Подготовить новые тексты\n"
            . "- Расширить коммерческие факторы\n"
            . "- Продолжить мониторинг индексации\n"
            . "- Сравнить динамику августа с июлем",
        'client_notes' =>
            'Просим подтвердить доступы редактора и согласованные формулировки оффера. Без этого часть коммерческих правок уйдёт на вторую половину августа.',
        'internal_notes' =>
            MARKER . ' — июль закрыт для демо. Метрики вымышленные. PDF/export/share не создавать.',
    ];
}

/**
 * @return array{executive_summary:string,results_summary:string,work_completed:string,key_findings:string,risks_and_blockers:string,next_month_plan:string,client_notes:string,internal_notes:string}
 */
function augustTexts(): array
{
    return [
        'executive_summary' =>
            'На 21 августа 2026 проект ПРОВЕРКА.рф во втором месяце SEO. Месяц ещё не закрыт: часть мета-правок выполнена, топ-10 запросов расширен до 21 в демо-наборе. Органический трафик MTD ~1 120 визитов при ~17 900 показах. Итоговые цифры будут сверены после окончания месяца.',
        'results_summary' =>
            "Предварительные результаты на 2026-08-21 (MTD, демо):\n"
            . "- Органические визиты MTD: ~1 120\n"
            . "- Показы MTD: ~17 900\n"
            . "- Запросов в топ-10: 21\n"
            . "- Лиды MTD (оценка): 10\n"
            . "- Технические ошибки сейчас: 5\n"
            . "- Новых/обновлённых страниц: 6\n"
            . "Финальные числа будут проверены после закрытия месяца.",
        'work_completed' =>
            "Сделано к 21 августа:\n"
            . "- Мета и H1 на 2 из 3 сервисных кластеров\n"
            . "- Повторная проверка индексации приоритетных URL\n"
            . "- 2 контент-брифа опубликованы / отданы в прод\n"
            . "- Черновой проход коммерческого чек-листа на 3 URL\n"
            . "Часть работ ещё в процессе или запланирована до конца месяца.",
        'key_findings' =>
            "Черновые выводы на 21.08:\n"
            . "- Рост топ-10 опережает контентный план — нужно догнать тексты\n"
            . "- Коммерческие страницы остаются главным риском конверсии\n"
            . "- Без согласования юр. формулировок часть URL «заморожена»",
        'risks_and_blockers' =>
            "Риски на 21.08:\n"
            . "- Юр. тексты всё ещё не согласованы (перенос с июля)\n"
            . "- Редактор клиента отвечает с задержкой 1–2 дня\n"
            . "- Риск не успеть 4 текста до конца месяца",
        'next_month_plan' =>
            "План до конца августа и задел на сентябрь:\n"
            . "- Добить мета кластера №3\n"
            . "- Опубликовать ≥2 согласованных текста\n"
            . "- Закрыть коммерческий чек-лист на оставшихся URL\n"
            . "- Собрать итоговый отчёт после 21.08\n"
            . "- Сентябрь (черновик): внутренняя перелинковка и расширение информационного спроса",
        'client_notes' =>
            'На 21.08 нужны ответы по формулировкам «Услуги/Цены» и слотам публикации текстов на неделе 25–29 августа.',
        'internal_notes' =>
            MARKER . ' — август намеренно незавершён на дату оператора 2026-08-21. Не финализировать. Не экспортировать.',
    ];
}

/**
 * @return list<array{block_key:string,block_type:string,title:string,sort_order:int,status:string,body:string,summary:string,data_json:?string}>
 */
function julyBlocks(array $texts): array
{
    $metricJson = json_encode([
        'demo' => true,
        'marker' => MARKER,
        'period' => '2026-07',
        'metrics' => [
            'organic_visits' => ['from' => 1240, 'to' => 1480],
            'impressions' => ['from' => 18500, 'to' => 22300],
            'indexed_priority_pages' => ['from' => 42, 'to' => 47],
            'tech_errors_high' => ['from' => 18, 'to' => 7],
            'leads_organic_est' => ['from' => 9, 'to' => 12],
            'top10_queries' => ['from' => 14, 'to' => 19],
        ],
    ], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

    return [
        [
            'block_key' => 'executive_summary',
            'block_type' => 'executive_summary',
            'title' => 'Краткое резюме',
            'sort_order' => 10,
            'status' => 'approved',
            'body' => $texts['executive_summary'],
            'summary' => 'Июль: технический фундамент, семантика и подготовка к росту в августе.',
            'data_json' => null,
        ],
        [
            'block_key' => 'results_summary',
            'block_type' => 'results_summary',
            'title' => 'Результаты',
            'sort_order' => 20,
            'status' => 'approved',
            'body' => $texts['results_summary'],
            'summary' => 'Умеренный рост трафика и снижение технических ошибок.',
            'data_json' => is_string($metricJson) ? $metricJson : null,
        ],
        [
            'block_key' => 'work_completed',
            'block_type' => 'work_completed',
            'title' => 'Что сделали',
            'sort_order' => 30,
            'status' => 'approved',
            'body' => $texts['work_completed'],
            'summary' => 'Аудит, индексация, семантика, мета-рекомендации и контент-план.',
            'data_json' => null,
        ],
        [
            'block_key' => 'key_findings',
            'block_type' => 'key_findings',
            'title' => 'Ключевые выводы',
            'sort_order' => 40,
            'status' => 'reviewed',
            'body' => $texts['key_findings'],
            'summary' => 'Техбаза укреплена; дальше — коммерция и контент.',
            'data_json' => null,
        ],
        [
            'block_key' => 'risks_and_blockers',
            'block_type' => 'risks_and_blockers',
            'title' => 'Риски и блокеры',
            'sort_order' => 50,
            'status' => 'reviewed',
            'body' => $texts['risks_and_blockers'],
            'summary' => 'Критичных блокеров нет; нужны согласования приоритетов.',
            'data_json' => null,
        ],
        [
            'block_key' => 'next_month_plan',
            'block_type' => 'next_month_plan',
            'title' => 'План на следующий месяц',
            'sort_order' => 60,
            'status' => 'approved',
            'body' => $texts['next_month_plan'],
            'summary' => 'Мета, тексты, коммерческие факторы и мониторинг индексации.',
            'data_json' => null,
        ],
    ];
}

/**
 * @return list<array{block_key:string,block_type:string,title:string,sort_order:int,status:string,body:string,summary:string,data_json:?string}>
 */
function augustBlocks(array $texts): array
{
    return [
        [
            'block_key' => 'executive_summary',
            'block_type' => 'executive_summary',
            'title' => 'Краткое резюме',
            'sort_order' => 10,
            'status' => 'in_progress',
            'body' => $texts['executive_summary'],
            'summary' => 'Август незавершён на 21.08; динамика сопоставима с июлем.',
            'data_json' => null,
        ],
        [
            'block_key' => 'results_summary',
            'block_type' => 'results_summary',
            'title' => 'Результаты',
            'sort_order' => 20,
            'status' => 'draft',
            'body' => $texts['results_summary'],
            'summary' => 'Предварительные MTD-метрики; финал после конца месяца.',
            'data_json' => null,
        ],
        [
            'block_key' => 'work_completed',
            'block_type' => 'work_completed',
            'title' => 'Что сделали',
            'sort_order' => 30,
            'status' => 'in_progress',
            'body' => $texts['work_completed'],
            'summary' => 'Часть мета и контента закрыта; остальное в работе.',
            'data_json' => null,
        ],
        [
            'block_key' => 'key_findings',
            'block_type' => 'key_findings',
            'title' => 'Ключевые выводы',
            'sort_order' => 40,
            'status' => 'in_progress',
            'body' => $texts['key_findings'],
            'summary' => 'Черновые выводы по топ-10 и коммерции.',
            'data_json' => null,
        ],
        [
            'block_key' => 'risks_and_blockers',
            'block_type' => 'risks_and_blockers',
            'title' => 'Риски и блокеры',
            'sort_order' => 50,
            'status' => 'in_progress',
            'body' => $texts['risks_and_blockers'],
            'summary' => 'Юр. согласование и сроки публикации остаются рисками.',
            'data_json' => null,
        ],
        [
            'block_key' => 'next_month_plan',
            'block_type' => 'next_month_plan',
            'title' => 'План на следующий месяц',
            'sort_order' => 60,
            'status' => 'draft',
            'body' => $texts['next_month_plan'],
            'summary' => 'Добить август и заложить сентябрьский контур.',
            'data_json' => null,
        ],
    ];
}

/**
 * @return list<array{title:string,description:string,status:string,period_role:string,client_visibility:string,client_summary:string,internal_note:string,evidence_note:string,sort_order:int}>
 */
function julyEntries(): array
{
    $rows = [
        ['Технический crawl и карта ошибок', 'Проверили структуру сайта и собрали список технических замечаний.', 'done', 'done', 'client_facing', 'Проверили структуру сайта и собрали список технических замечаний.', 'July seed entry', 'crawl summary 2026-07-05', 10],
        ['Исправление 404 и редиректов на приоритетных URL', 'Убрали битые ссылки и выстроили корректные переадресации.', 'done', 'done', 'client_facing', 'Убрали битые ссылки и выстроили корректные переадресации.', '11 URL fixed', '', 20],
        ['Обновление sitemap + переобход', 'Обновили карту сайта и запросили переобход важных страниц.', 'done', 'done', 'client_safe', 'Обновили карту сайта и запросили переобход важных страниц.', '', '', 30],
        ['Title/description для 24 страниц', 'Обновили заголовки и описания для приоритетных страниц.', 'done', 'done', 'client_facing', 'Обновили заголовки и описания для приоритетных страниц.', '', 'sheet meta-july', 40],
        ['Сбор семантики услуг (3 кластера)', 'Собрали и сгруппировали поисковые запросы по услугам.', 'done', 'done', 'client_facing', 'Собрали и сгруппировали поисковые запросы по услугам.', '', '', 50],
        ['Чек-лист коммерческих факторов (черновик)', 'Проверили контакты, доверие и призывы к действию.', 'done', 'done', 'client_safe', 'Проверили контакты, доверие и призывы к действию.', '', '', 60],
        ['Контент-план на август', 'Согласовали план текстов на следующий месяц.', 'done', 'done', 'client_facing', 'Согласовали план текстов на следующий месяц.', '', '', 70],
        ['Правки robots / noindex на служебных', 'Служебные разделы закрыты от индексации.', 'done', 'done', 'internal', 'Служебные разделы закрыты от индексации.', 'internal-only', '', 80],
        ['CWV spot-check мобильных шаблонов', 'Проверили скорость ключевых шаблонов на мобильных.', 'done', 'done', 'client_safe', 'Проверили скорость ключевых шаблонов на мобильных.', '', 'PSI notes demo', 90],
        ['Еженедельные статусы W1–W4', 'Внутренние checkpoint-заметки июля.', 'done', 'note', 'internal', 'Внутренние checkpoint-заметки июля.', 'internal checkpoints', '', 100],
        ['Ожидание доступа к CMS (W3)', 'Была пауза из‑за доступа к системе управления сайтом.', 'done', 'risk', 'client_safe', 'Была пауза из‑за доступа к системе управления сайтом.', 'blocked 2 days then resolved', '', 110],
        ['Согласование юр. формулировок «Услуги»', 'Нужно согласование текстов по услугам и ценам.', 'deferred', 'risk', 'client_facing', 'Нужно согласование текстов по услугам и ценам.', 'carries to August', '', 120],
    ];
    $out = [];
    foreach ($rows as $r) {
        $out[] = [
            'title' => $r[0],
            'description' => $r[1],
            'status' => $r[2],
            'period_role' => $r[3],
            'client_visibility' => $r[4],
            'client_summary' => $r[5],
            'internal_note' => $r[6],
            'evidence_note' => $r[7],
            'sort_order' => $r[8],
        ];
    }
    return $out;
}

/**
 * @return list<array{title:string,description:string,status:string,period_role:string,client_visibility:string,client_summary:string,internal_note:string,evidence_note:string,sort_order:int}>
 */
function augustEntries(): array
{
    $rows = [
        ['Мета/H1 кластер «Основные услуги»', 'Закрыто к 12.08.', 'done', 'done', 'client_facing', 'Обновили мета и H1 для основных услуг.', 'closed 2026-08-12', '', 10],
        ['Мета/H1 кластер «Доп. услуги»', 'Закрыто к 18.08.', 'done', 'done', 'client_facing', 'Обновили мета и H1 для дополнительных услуг.', 'closed 2026-08-18', '', 20],
        ['Мета/H1 кластер «Регион / выезд»', 'Около 60% к 21.08.', 'in_progress', 'done', 'client_facing', 'В работе мета и H1 для регионального кластера.', '~60% as of 2026-08-21', '', 30],
        ['Публикация текста «Услуга A»', 'Текст опубликован.', 'done', 'done', 'client_facing', 'Опубликован текст по услуге A.', '', '', 40],
        ['Публикация текста «Услуга B»', 'Текст опубликован.', 'done', 'done', 'client_safe', 'Опубликован текст по услуге B.', '', '', 50],
        ['Коммерческий чек-лист (3 URL)', 'Черновой проход на 3 URL.', 'in_progress', 'done', 'client_facing', 'Проверяем коммерческие факторы на первых трёх URL.', 'partial as of 2026-08-21', '', 60],
        ['Коммерческий чек-лист (оставшиеся 3 URL)', 'Запланировано до конца месяца.', 'planned', 'planned_next', 'client_safe', 'Осталось проверить ещё три URL.', 'planned to 2026-08-31', '', 70],
        ['Внутренняя перелинковка кластеров', 'Запланировано до конца месяца.', 'planned', 'planned_next', 'client_safe', 'Запланирована перелинковка кластеров.', '', '', 80],
        ['Согласование юр. формулировок', 'Блокер на стороне клиента.', 'blocked', 'risk', 'client_facing', 'Ждём согласование формулировок «Услуги/Цены».', 'client blocker', '', 90],
        ['Черновик итогового отчёта августа', 'Сборка после 25.08.', 'in_progress', 'note', 'internal', 'Черновик итогового отчёта в работе.', 'assembly after 2026-08-25', '', 100],
    ];
    $out = [];
    foreach ($rows as $r) {
        $out[] = [
            'title' => $r[0],
            'description' => $r[1],
            'status' => $r[2],
            'period_role' => $r[3],
            'client_visibility' => $r[4],
            'client_summary' => $r[5],
            'internal_note' => $r[6],
            'evidence_note' => $r[7],
            'sort_order' => $r[8],
        ];
    }
    return $out;
}

/**
 * @param list<array{block_key:string,block_type:string,title:string,sort_order:int,status:string,body:string,summary:string,data_json:?string}> $blocks
 * @return list<int>
 */
function insertBlocks(PDO $pdo, int $monthlyId, int $userId, array $blocks): array
{
    $ids = [];
    $ins = $pdo->prepare(
        'INSERT INTO report_blocks
         (monthly_report_content_id, block_key, block_type, sort_order, status, title, body, summary, data_json,
          owner_user_id, created_by, updated_by)
         VALUES
         (:mid, :block_key, :block_type, :sort_order, :status, :title, :body, :summary, :data_json,
          :owner_user_id, :created_by, :updated_by)'
    );
    foreach ($blocks as $b) {
        $ins->execute([
            ':mid' => $monthlyId,
            ':block_key' => $b['block_key'],
            ':block_type' => $b['block_type'],
            ':sort_order' => $b['sort_order'],
            ':status' => $b['status'],
            ':title' => $b['title'],
            ':body' => $b['body'],
            ':summary' => $b['summary'],
            ':data_json' => $b['data_json'],
            ':owner_user_id' => $userId,
            ':created_by' => $userId,
            ':updated_by' => $userId,
        ]);
        $ids[] = (int) $pdo->lastInsertId();
    }
    return $ids;
}

/**
 * @param list<array{title:string,description:string,status:string,period_role:string,client_visibility:string,client_summary:string,internal_note:string,evidence_note:string,sort_order:int}> $entries
 * @return list<int>
 */
function insertEntries(PDO $pdo, int $monthlyId, int $userId, array $entries): array
{
    $ids = [];
    $ins = $pdo->prepare(
        'INSERT INTO monthly_report_work_entries
         (monthly_report_id, work_item_id, category_id, title, description, status, period_role,
          client_visibility, client_summary, internal_note, evidence_note, sort_order,
          created_by_user_id, updated_by_user_id)
         VALUES
         (:monthly_report_id, NULL, NULL, :title, :description, :status, :period_role,
          :client_visibility, :client_summary, :internal_note, :evidence_note, :sort_order,
          :created_by_user_id, :updated_by_user_id)'
    );
    foreach ($entries as $e) {
        $ins->execute([
            ':monthly_report_id' => $monthlyId,
            ':title' => $e['title'],
            ':description' => $e['description'],
            ':status' => $e['status'],
            ':period_role' => $e['period_role'],
            ':client_visibility' => $e['client_visibility'],
            ':client_summary' => $e['client_summary'],
            ':internal_note' => $e['internal_note'],
            ':evidence_note' => $e['evidence_note'],
            ':sort_order' => $e['sort_order'],
            ':created_by_user_id' => $userId,
            ':updated_by_user_id' => $userId,
        ]);
        $ids[] = (int) $pdo->lastInsertId();
    }
    return $ids;
}

/**
 * @return array<string, mixed>
 */
function runCreate(PDO $pdo, string $idsPath, string $evidenceDir): array
{
    $before = discoverScenario($pdo);
    writeJsonFile($evidenceDir . DIRECTORY_SEPARATOR . 'seed-status-before.json', $before);
    writeJsonFile($evidenceDir . DIRECTORY_SEPARATOR . 'db-counts-before.json', $before['counts']);

    if ($before['complete'] === true) {
        $ids = buildIdsPayload($before, 'already_complete');
        writeJsonFile($idsPath, $ids);
        writeJsonFile($evidenceDir . DIRECTORY_SEPARATOR . 'seed-status-after.json', $before);
        writeJsonFile($evidenceDir . DIRECTORY_SEPARATOR . 'db-counts-after.json', $before['counts']);
        return [
            'ok' => true,
            'mode' => 'create',
            'action' => 'already_complete',
            'ids_path' => $idsPath,
            'ids' => $ids,
        ];
    }
    if ($before['partial'] === true) {
        stop('Partial demo marker state detected. Run --status and decide cleanup/restore; refusing duplicate create.');
    }

    $roleStmt = $pdo->prepare('SELECT id FROM roles WHERE code = :code LIMIT 1');
    $roleStmt->execute([':code' => USER_ROLE]);
    $roleId = $roleStmt->fetchColumn();
    if ($roleId === false) {
        stop('Role seo_specialist missing.');
    }
    $roleId = (int) $roleId;

    $password = demoPassword();
    $hash = password_hash($password, PASSWORD_DEFAULT);
    $password = '';
    unset($password);
    if (!is_string($hash) || $hash === '') {
        stop('password_hash failed.');
    }

    $julyTexts = julyTexts();
    $augustTexts = augustTexts();

    try {
        $pdo->beginTransaction();

        $userIns = $pdo->prepare(
            'INSERT INTO users (name, email, password_hash, status)
             VALUES (:name, :email, :password_hash, :status)'
        );
        $userIns->execute([
            ':name' => USER_NAME,
            ':email' => USER_EMAIL,
            ':password_hash' => $hash,
            ':status' => 'active',
        ]);
        $userId = (int) $pdo->lastInsertId();
        $hash = '';

        $pdo->prepare('INSERT INTO user_roles (user_id, role_id) VALUES (:uid, :rid)')
            ->execute([':uid' => $userId, ':rid' => $roleId]);

        $clientIns = $pdo->prepare(
            'INSERT INTO clients (name, slug, status, notes)
             VALUES (:name, :slug, :status, :notes)'
        );
        $clientIns->execute([
            ':name' => CLIENT_NAME,
            ':slug' => CLIENT_SLUG,
            ':status' => 'active',
            ':notes' => MARKER . ' — local demo client for team training. Not a real client.',
        ]);
        $clientId = (int) $pdo->lastInsertId();

        $projectIns = $pdo->prepare(
            'INSERT INTO projects (client_id, name, slug, project_type, status)
             VALUES (:client_id, :name, :slug, :project_type, :status)'
        );
        $projectIns->execute([
            ':client_id' => $clientId,
            ':name' => PROJECT_NAME,
            ':slug' => PROJECT_SLUG,
            ':project_type' => 'service_corporate',
            ':status' => 'active',
        ]);
        $projectId = (int) $pdo->lastInsertId();

        $siteIns = $pdo->prepare(
            'INSERT INTO sites (project_id, url, label, is_primary)
             VALUES (:project_id, :url, :label, 1)'
        );
        $siteIns->execute([
            ':project_id' => $projectId,
            ':url' => SITE_URL,
            ':label' => SITE_LABEL,
        ]);
        $siteId = (int) $pdo->lastInsertId();

        $periodIns = $pdo->prepare(
            'INSERT INTO reporting_periods
             (project_id, period_key, period_start, period_end, status, title, summary,
              owner_user_id, created_by, updated_by, finalized_at)
             VALUES
             (:project_id, :period_key, :period_start, :period_end, :status, :title, :summary,
              :owner_user_id, :created_by, :updated_by, :finalized_at)'
        );

        $periodIns->execute([
            ':project_id' => $projectId,
            ':period_key' => '2026-07',
            ':period_start' => '2026-07-01',
            ':period_end' => '2026-07-31',
            ':status' => 'finalized',
            ':title' => 'Июль 2026 — ПРОВЕРКА.рф',
            ':summary' => 'Первый полный месяц SEO по ПРОВЕРКА.рф.',
            ':owner_user_id' => $userId,
            ':created_by' => $userId,
            ':updated_by' => $userId,
            ':finalized_at' => '2026-08-01 10:00:00',
        ]);
        $periodJulyId = (int) $pdo->lastInsertId();

        $periodIns->execute([
            ':project_id' => $projectId,
            ':period_key' => '2026-08',
            ':period_start' => '2026-08-01',
            ':period_end' => '2026-08-31',
            ':status' => 'active',
            ':title' => 'Август 2026 — ПРОВЕРКА.рф',
            ':summary' => 'Второй месяц; незавершён на 2026-08-21.',
            ':owner_user_id' => $userId,
            ':created_by' => $userId,
            ':updated_by' => $userId,
            ':finalized_at' => null,
        ]);
        $periodAugustId = (int) $pdo->lastInsertId();

        $monthlyIns = $pdo->prepare(
            'INSERT INTO monthly_report_contents
             (reporting_period_id, status, title, executive_summary, work_completed, results_summary,
              key_findings, risks_and_blockers, next_month_plan, client_notes, internal_notes,
              owner_user_id, created_by, updated_by, finalized_at)
             VALUES
             (:reporting_period_id, :status, :title, :executive_summary, :work_completed, :results_summary,
              :key_findings, :risks_and_blockers, :next_month_plan, :client_notes, :internal_notes,
              :owner_user_id, :created_by, :updated_by, :finalized_at)'
        );

        $monthlyIns->execute([
            ':reporting_period_id' => $periodJulyId,
            ':status' => 'finalized',
            ':title' => 'Ежемесячный отчёт SEO — июль 2026 — ПРОВЕРКА.рф',
            ':executive_summary' => $julyTexts['executive_summary'],
            ':work_completed' => $julyTexts['work_completed'],
            ':results_summary' => $julyTexts['results_summary'],
            ':key_findings' => $julyTexts['key_findings'],
            ':risks_and_blockers' => $julyTexts['risks_and_blockers'],
            ':next_month_plan' => $julyTexts['next_month_plan'],
            ':client_notes' => $julyTexts['client_notes'],
            ':internal_notes' => $julyTexts['internal_notes'],
            ':owner_user_id' => $userId,
            ':created_by' => $userId,
            ':updated_by' => $userId,
            ':finalized_at' => '2026-08-01 10:00:00',
        ]);
        $monthlyJulyId = (int) $pdo->lastInsertId();

        $monthlyIns->execute([
            ':reporting_period_id' => $periodAugustId,
            ':status' => 'in_progress',
            ':title' => 'Ежемесячный отчёт SEO — август 2026 — ПРОВЕРКА.рф',
            ':executive_summary' => $augustTexts['executive_summary'],
            ':work_completed' => $augustTexts['work_completed'],
            ':results_summary' => $augustTexts['results_summary'],
            ':key_findings' => $augustTexts['key_findings'],
            ':risks_and_blockers' => $augustTexts['risks_and_blockers'],
            ':next_month_plan' => $augustTexts['next_month_plan'],
            ':client_notes' => $augustTexts['client_notes'],
            ':internal_notes' => $augustTexts['internal_notes'],
            ':owner_user_id' => $userId,
            ':created_by' => $userId,
            ':updated_by' => $userId,
            ':finalized_at' => null,
        ]);
        $monthlyAugustId = (int) $pdo->lastInsertId();

        if (in_array($monthlyJulyId, PROTECTED_MONTHLY_IDS, true)
            || in_array($monthlyAugustId, PROTECTED_MONTHLY_IDS, true)
        ) {
            throw new RuntimeException('Protected monthly id collision.');
        }

        $blockIdsJuly = insertBlocks($pdo, $monthlyJulyId, $userId, julyBlocks($julyTexts));
        $blockIdsAugust = insertBlocks($pdo, $monthlyAugustId, $userId, augustBlocks($augustTexts));
        $entryIdsJuly = insertEntries($pdo, $monthlyJulyId, $userId, julyEntries());
        $entryIdsAugust = insertEntries($pdo, $monthlyAugustId, $userId, augustEntries());

        $meta = json_encode(
            [
                'marker' => MARKER,
                'slug' => CLIENT_SLUG,
                'user_email' => USER_EMAIL,
                'monthly_july_id' => $monthlyJulyId,
                'monthly_august_id' => $monthlyAugustId,
                'no_export_share_snapshot' => true,
            ],
            JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR
        );
        $pdo->prepare(
            'INSERT INTO audit_log (actor_user_id, event_type, entity_type, entity_id, metadata_json)
             VALUES (:actor_user_id, :event_type, :entity_type, :entity_id, :metadata_json)'
        )->execute([
            ':actor_user_id' => $userId,
            ':event_type' => 'demo_proverka.seeded',
            ':entity_type' => 'client',
            ':entity_id' => $clientId,
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

    $after = discoverScenario($pdo);
    if ($after['complete'] !== true) {
        stop('Create finished but scenario is not complete.');
    }
    foreach ([$monthlyJulyId, $monthlyAugustId] as $mid) {
        $pub = publicationCounts($pdo, $mid);
        if ($pub['snapshots'] !== 0 || $pub['exports'] !== 0 || $pub['shares'] !== 0) {
            stop('Unexpected publication rows for demo monthly ' . $mid);
        }
    }

    $ids = [
        'marker' => MARKER,
        'created_at' => gmdate('c'),
        'action' => 'created',
        'user_id' => $userId,
        'user_email' => USER_EMAIL,
        'user_name' => USER_NAME,
        'user_role' => USER_ROLE,
        'client_id' => $clientId,
        'project_id' => $projectId,
        'site_id' => $siteId,
        'period_july_id' => $periodJulyId,
        'period_august_id' => $periodAugustId,
        'monthly_july_id' => $monthlyJulyId,
        'monthly_august_id' => $monthlyAugustId,
        'block_ids' => array_merge($blockIdsJuly, $blockIdsAugust),
        'block_ids_july' => $blockIdsJuly,
        'block_ids_august' => $blockIdsAugust,
        'work_entry_ids' => array_merge($entryIdsJuly, $entryIdsAugust),
        'work_entry_ids_july' => $entryIdsJuly,
        'work_entry_ids_august' => $entryIdsAugust,
        'weekly_checkpoint_ids' => [],
        'notes' => 'no password/hash/tokens; no export/share/snapshot',
        'urls' => [
            'july_report' => '/monthly-reports/' . $monthlyJulyId,
            'july_preview' => '/monthly-reports/' . $monthlyJulyId . '/preview',
            'august_report' => '/monthly-reports/' . $monthlyAugustId,
            'august_preview' => '/monthly-reports/' . $monthlyAugustId . '/preview',
            'august_work_create' => '/monthly-reports/' . $monthlyAugustId . '/work-entries/create',
            'sample_work_edit' => '/monthly-report-work-entries/' . ($entryIdsAugust[0] ?? 0) . '/edit',
            'period_july' => '/reporting-periods/' . $periodJulyId,
            'period_august' => '/reporting-periods/' . $periodAugustId,
        ],
        'baseline_counts' => $before['counts'],
    ];

    writeJsonFile($idsPath, $ids);
    writeJsonFile($evidenceDir . DIRECTORY_SEPARATOR . 'demo-proverka-ids.json', $ids);
    writeJsonFile($evidenceDir . DIRECTORY_SEPARATOR . 'seed-status-after.json', $after);
    writeJsonFile($evidenceDir . DIRECTORY_SEPARATOR . 'db-counts-after.json', $after['counts']);

    return [
        'ok' => true,
        'mode' => 'create',
        'action' => 'created',
        'ids_path' => $idsPath,
        'evidence_dir' => $evidenceDir,
        'ids' => $ids,
        'counts_after' => $after['counts'],
    ];
}

/**
 * @param array<string, mixed> $scenario
 * @return array<string, mixed>
 */
function buildIdsPayload(array $scenario, string $action): array
{
    $user = is_array($scenario['user'] ?? null) ? $scenario['user'] : null;
    $client = is_array($scenario['client'] ?? null) ? $scenario['client'] : null;
    $project = is_array($scenario['project'] ?? null) ? $scenario['project'] : null;
    $site = is_array($scenario['site'] ?? null) ? $scenario['site'] : null;
    $periodJuly = is_array($scenario['period_july'] ?? null) ? $scenario['period_july'] : null;
    $periodAugust = is_array($scenario['period_august'] ?? null) ? $scenario['period_august'] : null;
    $monthlyJuly = is_array($scenario['monthly_july'] ?? null) ? $scenario['monthly_july'] : null;
    $monthlyAugust = is_array($scenario['monthly_august'] ?? null) ? $scenario['monthly_august'] : null;
    $blockJuly = is_array($scenario['block_ids_july'] ?? null) ? $scenario['block_ids_july'] : [];
    $blockAugust = is_array($scenario['block_ids_august'] ?? null) ? $scenario['block_ids_august'] : [];
    $entryJuly = is_array($scenario['work_entry_ids_july'] ?? null) ? $scenario['work_entry_ids_july'] : [];
    $entryAugust = is_array($scenario['work_entry_ids_august'] ?? null) ? $scenario['work_entry_ids_august'] : [];

    $monthlyJulyId = is_array($monthlyJuly) ? (int) $monthlyJuly['id'] : null;
    $monthlyAugustId = is_array($monthlyAugust) ? (int) $monthlyAugust['id'] : null;
    $periodJulyId = is_array($periodJuly) ? (int) $periodJuly['id'] : null;
    $periodAugustId = is_array($periodAugust) ? (int) $periodAugust['id'] : null;
    $entrySample = $entryAugust[0] ?? ($entryJuly[0] ?? null);

    return [
        'marker' => MARKER,
        'created_at' => gmdate('c'),
        'action' => $action,
        'user_id' => $user !== null ? (int) $user['id'] : null,
        'user_email' => USER_EMAIL,
        'user_name' => USER_NAME,
        'user_role' => USER_ROLE,
        'client_id' => $client !== null ? (int) $client['id'] : null,
        'project_id' => $project !== null ? (int) $project['id'] : null,
        'site_id' => $site !== null ? (int) $site['id'] : null,
        'period_july_id' => $periodJulyId,
        'period_august_id' => $periodAugustId,
        'monthly_july_id' => $monthlyJulyId,
        'monthly_august_id' => $monthlyAugustId,
        'block_ids' => array_merge($blockJuly, $blockAugust),
        'block_ids_july' => $blockJuly,
        'block_ids_august' => $blockAugust,
        'work_entry_ids' => array_merge($entryJuly, $entryAugust),
        'work_entry_ids_july' => $entryJuly,
        'work_entry_ids_august' => $entryAugust,
        'weekly_checkpoint_ids' => [],
        'notes' => 'no password/hash/tokens',
        'urls' => [
            'july_report' => $monthlyJulyId ? '/monthly-reports/' . $monthlyJulyId : null,
            'july_preview' => $monthlyJulyId ? '/monthly-reports/' . $monthlyJulyId . '/preview' : null,
            'august_report' => $monthlyAugustId ? '/monthly-reports/' . $monthlyAugustId : null,
            'august_preview' => $monthlyAugustId ? '/monthly-reports/' . $monthlyAugustId . '/preview' : null,
            'august_work_create' => $monthlyAugustId ? '/monthly-reports/' . $monthlyAugustId . '/work-entries/create' : null,
            'sample_work_edit' => $entrySample ? '/monthly-report-work-entries/' . $entrySample . '/edit' : null,
            'period_july' => $periodJulyId ? '/reporting-periods/' . $periodJulyId : null,
            'period_august' => $periodAugustId ? '/reporting-periods/' . $periodAugustId : null,
        ],
    ];
}

/**
 * @param list<int> $ids
 */
function deleteByIds(PDO $pdo, string $table, string $column, array $ids): int
{
    $ids = array_values(array_unique(array_filter(array_map('intval', $ids), static fn (int $id): bool => $id > 0)));
    if ($ids === []) {
        return 0;
    }
    $placeholders = implode(',', array_fill(0, count($ids), '?'));
    $stmt = $pdo->prepare("DELETE FROM `{$table}` WHERE `{$column}` IN ({$placeholders})");
    $stmt->execute($ids);
    return $stmt->rowCount();
}

/**
 * @return array<string, mixed>
 */
function loadIdsJson(string $path): array
{
    if (!is_file($path)) {
        stop('IDs JSON not found: ' . $path);
    }
    $raw = file_get_contents($path);
    if ($raw === false) {
        stop('Cannot read IDs JSON.');
    }
    $data = json_decode($raw, true);
    if (!is_array($data)) {
        stop('Invalid IDs JSON.');
    }
    if (($data['marker'] ?? null) !== MARKER) {
        stop('IDs JSON marker mismatch.');
    }
    return $data;
}

/**
 * @return array<string, mixed>
 */
function runCleanup(PDO $pdo, string $idsPath): array
{
    $ids = loadIdsJson($idsPath);
    $monthlyIds = array_values(array_filter([
        (int) ($ids['monthly_july_id'] ?? 0),
        (int) ($ids['monthly_august_id'] ?? 0),
    ]));
    foreach ($monthlyIds as $mid) {
        if (in_array($mid, PROTECTED_MONTHLY_IDS, true)) {
            stop('Cleanup refused: protected monthly id in JSON.');
        }
        $pub = publicationCounts($pdo, $mid);
        if ($pub['snapshots'] > 0 || $pub['exports'] > 0 || $pub['shares'] > 0) {
            stop('Cleanup refused: demo monthly has export/share/snapshot rows. Restore backup instead.');
        }
    }

    $blockIds = array_map('intval', is_array($ids['block_ids'] ?? null) ? $ids['block_ids'] : []);
    $entryIds = array_map('intval', is_array($ids['work_entry_ids'] ?? null) ? $ids['work_entry_ids'] : []);
    $periodIds = array_values(array_filter([
        (int) ($ids['period_july_id'] ?? 0),
        (int) ($ids['period_august_id'] ?? 0),
    ]));
    $siteId = (int) ($ids['site_id'] ?? 0);
    $projectId = (int) ($ids['project_id'] ?? 0);
    $clientId = (int) ($ids['client_id'] ?? 0);
    $userId = (int) ($ids['user_id'] ?? 0);

    if ($clientId === 1 || $projectId === 1 || $siteId === 1) {
        stop('Cleanup refused: Demo Client entity id collision.');
    }

    $deleted = [
        'monthly_report_work_entries' => 0,
        'report_blocks' => 0,
        'monthly_report_contents' => 0,
        'reporting_periods' => 0,
        'sites' => 0,
        'projects' => 0,
        'clients' => 0,
        'user_roles' => 0,
        'users' => 0,
    ];

    try {
        $pdo->beginTransaction();
        $deleted['monthly_report_work_entries'] = deleteByIds($pdo, 'monthly_report_work_entries', 'id', $entryIds);
        $deleted['report_blocks'] = deleteByIds($pdo, 'report_blocks', 'id', $blockIds);
        $deleted['monthly_report_contents'] = deleteByIds($pdo, 'monthly_report_contents', 'id', $monthlyIds);
        $deleted['reporting_periods'] = deleteByIds($pdo, 'reporting_periods', 'id', $periodIds);
        if ($siteId > 0) {
            $deleted['sites'] = deleteByIds($pdo, 'sites', 'id', [$siteId]);
        }
        if ($projectId > 0) {
            $deleted['projects'] = deleteByIds($pdo, 'projects', 'id', [$projectId]);
        }
        if ($clientId > 0) {
            $deleted['clients'] = deleteByIds($pdo, 'clients', 'id', [$clientId]);
        }
        if ($userId > 0) {
            $stmt = $pdo->prepare('DELETE FROM user_roles WHERE user_id = :uid');
            $stmt->execute([':uid' => $userId]);
            $deleted['user_roles'] = $stmt->rowCount();
            $emailCheck = $pdo->prepare('SELECT email FROM users WHERE id = :id LIMIT 1');
            $emailCheck->execute([':id' => $userId]);
            $email = $emailCheck->fetchColumn();
            if ($email === USER_EMAIL) {
                $deleted['users'] = deleteByIds($pdo, 'users', 'id', [$userId]);
            }
        }
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) {
            $pdo->rollBack();
        }
        fwrite(STDERR, "CLEANUP FAILED (details redacted).\n");
        exit(9);
    }

    $after = discoverScenario($pdo);
    return [
        'ok' => $after['complete'] !== true && $after['partial'] !== true,
        'mode' => 'cleanup',
        'deleted' => $deleted,
        'after' => $after,
    ];
}

// --- main ---
$args = parseArgs($argv);
if ($args['help']) {
    printHelp();
    exit(0);
}
if ($args['mode'] === null) {
    printHelp();
    refuse('Specify --status, --create, or --cleanup.');
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
    'clients', 'projects', 'sites', 'users', 'roles', 'user_roles', 'reporting_periods',
    'monthly_report_contents', 'report_blocks', 'monthly_report_work_entries',
    'report_snapshots', 'report_exports', 'report_export_shares', 'audit_log',
];
foreach ($requiredTables as $table) {
    if (!tableExists($pdo, $table)) {
        refuse('required table missing: ' . $table);
    }
}

if ($args['mode'] === 'status') {
    $status = discoverScenario($pdo);
    emitJson([
        'ok' => true,
        'mode' => 'status',
        'marker' => MARKER,
        'user_email' => USER_EMAIL,
        'complete' => $status['complete'],
        'partial' => $status['partial'],
        'user' => $status['user'],
        'client_id' => is_array($status['client']) ? (int) $status['client']['id'] : null,
        'project_id' => is_array($status['project']) ? (int) $status['project']['id'] : null,
        'site_id' => is_array($status['site']) ? (int) $status['site']['id'] : null,
        'period_july_id' => is_array($status['period_july']) ? (int) $status['period_july']['id'] : null,
        'period_august_id' => is_array($status['period_august']) ? (int) $status['period_august']['id'] : null,
        'monthly_july_id' => is_array($status['monthly_july']) ? (int) $status['monthly_july']['id'] : null,
        'monthly_august_id' => is_array($status['monthly_august']) ? (int) $status['monthly_august']['id'] : null,
        'blocks_july' => count($status['block_ids_july']),
        'blocks_august' => count($status['block_ids_august']),
        'entries_july' => count($status['work_entry_ids_july']),
        'entries_august' => count($status['work_entry_ids_august']),
        'publication_july' => $status['publication_july'],
        'publication_august' => $status['publication_august'],
        'counts' => $status['counts'],
    ]);
    exit(0);
}

if (!$args['confirm']) {
    refuse('--confirm-local-demo-seed is required for --create/--cleanup.');
}

$evidenceDir = ensureEvidenceDir($args['evidence_dir']);
$idsPath = $args['ids'] !== null && $args['ids'] !== ''
    ? $args['ids']
    : ($evidenceDir . DIRECTORY_SEPARATOR . 'demo-proverka-ids.json');

if ($args['mode'] === 'create') {
    $result = runCreate($pdo, $idsPath, $evidenceDir);
    $log = $evidenceDir . DIRECTORY_SEPARATOR . 'seed-create-log.txt';
    file_put_contents(
        $log,
        "action={$result['action']}\nids_path={$idsPath}\nuser_email=" . USER_EMAIL . "\nmarker=" . MARKER . "\npassword=REDACTED\nhash=REDACTED\n"
    );
    emitJson($result);
    exit(0);
}

if ($args['mode'] === 'cleanup') {
    $result = runCleanup($pdo, $idsPath);
    emitJson($result);
    exit($result['ok'] ? 0 : 3);
}

refuse('Unknown mode.');

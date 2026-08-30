<?php
declare(strict_types=1);

/**
 * Seed Nikita SEO work catalogue + optional monthly work-entry fixtures.
 *
 * Local only: iseo_report_hub_dev @ 127.0.0.1
 *
 * Usage:
 *   php tools/seed-nikita-catalogue.php
 *   php tools/seed-nikita-catalogue.php --skip-monthly-fixtures
 *
 * Safety:
 * - CLI only
 * - refuses DB name other than iseo_report_hub_dev
 * - refuses DB host other than 127.0.0.1
 * - idempotent upsert by slug (categories/items) and by monthly_report_id+title (entries)
 * - no DELETE/DROP/TRUNCATE of existing MVP tables
 * - never prints credentials / passwords / hashes
 * - does not mutate report_exports / report_export_shares / report_blocks / monthly flat fields
 * - excludes access/credentials taxonomy
 *
 * Source attribution: nikita_catalogue_v1 (sanitized representative catalogue; not full proprietary dump)
 */

if (PHP_SAPI !== 'cli') {
    fwrite(STDERR, "REFUSED: CLI only.\n");
    exit(1);
}

const REQUIRED_DB = 'iseo_report_hub_dev';
const REQUIRED_HOST = '127.0.0.1';
const SOURCE_ATTR = 'nikita_catalogue_v1';
const FIXTURE_NOTE = 'LOCAL_FIXTURE_ONLY nikita_catalogue_v1';
const TARGET_MONTHLY_REPORT_ID = 1;

/**
 * @return array{host:string,port:int,database:string,username:string,password:string}
 */
function loadDbConfig(): array
{
    $root = dirname(__DIR__);
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
            if (
                (str_starts_with($value, '"') && str_ends_with($value, '"'))
                || (str_starts_with($value, "'") && str_ends_with($value, "'"))
            ) {
                $value = substr($value, 1, -1);
            }
            if ($key !== '' && getenv($key) === false) {
                putenv($key . '=' . $value);
                $_ENV[$key] = $value;
            }
        }
        break;
    }

    return [
        'host' => (string) (getenv('DB_HOST') ?: '127.0.0.1'),
        'port' => (int) (getenv('DB_PORT') ?: 3306),
        'database' => (string) (getenv('DB_DATABASE') ?: ''),
        'username' => (string) (getenv('DB_USERNAME') ?: ''),
        'password' => (string) (getenv('DB_PASSWORD') ?: ''),
    ];
}

function assertLocalDb(array $cfg): void
{
    if ($cfg['database'] !== REQUIRED_DB) {
        fwrite(STDERR, 'REFUSED: target DB must be exactly "' . REQUIRED_DB . "\".\n");
        exit(2);
    }
    if ($cfg['host'] !== REQUIRED_HOST) {
        fwrite(STDERR, 'REFUSED: DB host must be exactly "' . REQUIRED_HOST . "\".\n");
        exit(2);
    }
}

function connect(array $cfg): PDO
{
    assertLocalDb($cfg);
    $dsn = sprintf(
        'mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4',
        $cfg['host'],
        $cfg['port'],
        $cfg['database']
    );
    $pdo = new PDO($dsn, $cfg['username'], $cfg['password'], [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    $actualDb = (string) $pdo->query('SELECT DATABASE()')->fetchColumn();
    $actualHost = (string) $pdo->query("SELECT CASE WHEN @@hostname IS NOT NULL THEN 'connected' ELSE 'connected' END")->fetchColumn();
    unset($actualHost);
    if ($actualDb !== REQUIRED_DB) {
        fwrite(STDERR, "REFUSED: connected database mismatch.\n");
        exit(2);
    }
    return $pdo;
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

/**
 * @return list<array{slug:string,name:string,description:string,sort_order:int}>
 */
function categories(): array
{
    return [
        ['slug' => 'start', 'name' => 'Старт', 'description' => 'Стартовые работы и базовая настройка проекта.', 'sort_order' => 10],
        ['slug' => 'analytics', 'name' => 'Аналитика', 'description' => 'Аналитика состояния проекта, конкурентов и метрик.', 'sort_order' => 20],
        ['slug' => 'technical_monitoring', 'name' => 'Технический мониторинг', 'description' => 'Технический мониторинг, индексация и контроль ошибок.', 'sort_order' => 30],
        ['slug' => 'link_building', 'name' => 'Ссылочное', 'description' => 'Ссылочное продвижение и работа с площадками.', 'sort_order' => 40],
        ['slug' => 'semantic_core', 'name' => 'Семантика', 'description' => 'Сбор, кластеризация и актуализация семантики.', 'sort_order' => 50],
        ['slug' => 'commercial_factors', 'name' => 'Коммерческие факторы', 'description' => 'Коммерческие факторы карточек и страниц.', 'sort_order' => 60],
        ['slug' => 'content', 'name' => 'Тексты', 'description' => 'Текстовая оптимизация: ТЗ, написание и размещение.', 'sort_order' => 70],
        ['slug' => 'behavioral_factors_external', 'name' => 'Внешний ПФ', 'description' => 'Внешние поведенческие активности.', 'sort_order' => 80],
        ['slug' => 'behavioral_factors_internal', 'name' => 'Внутренний ПФ', 'description' => 'Улучшение внутренних поведенческих факторов.', 'sort_order' => 90],
        ['slug' => 'onpage', 'name' => 'OnPage', 'description' => 'OnPage-оптимизация страниц и структуры.', 'sort_order' => 100],
        ['slug' => 'serm', 'name' => 'SERM', 'description' => 'Мониторинг репутации и работа с упоминаниями.', 'sort_order' => 110],
        ['slug' => 'reporting', 'name' => 'Отчеты', 'description' => 'Ежемесячная отчетность и план работ.', 'sort_order' => 120],
        ['slug' => 'quantitative_plans', 'name' => 'Количественные планы', 'description' => 'Планирование объемов контента и ссылок.', 'sort_order' => 130],
    ];
}

/**
 * @return list<array{
 *   category_slug:string,
 *   slug:string,
 *   name:string,
 *   description:string,
 *   site_type:string,
 *   cadence:string,
 *   visibility:string,
 *   fill_mode:string,
 *   evidence_required:int,
 *   sort_order:int
 * }>
 */
function workItems(): array
{
    return [
        ['category_slug' => 'start', 'slug' => 'start-initial-audit', 'name' => 'Стартовый аудит', 'description' => 'Базовый стартовый аудит проекта.', 'site_type' => 'both', 'cadence' => 'one_time', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'start', 'slug' => 'start-base-tools-setup', 'name' => 'Настройка базовых инструментов', 'description' => 'Настройка базовых аналитических и технических инструментов.', 'site_type' => 'both', 'cadence' => 'one_time', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],

        ['category_slug' => 'analytics', 'slug' => 'analytics-project-state', 'name' => 'Анализ текущего состояния проекта', 'description' => 'Оценка текущего SEO-состояния проекта.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'analytics', 'slug' => 'analytics-competitors', 'name' => 'Анализ конкурентов', 'description' => 'Сравнительный анализ конкурентов по приоритетным направлениям.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],
        ['category_slug' => 'analytics', 'slug' => 'analytics-metrics-traffic', 'name' => 'Анализ метрики и трафика', 'description' => 'Анализ метрик и трафика за отчетный период.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 30],

        ['category_slug' => 'technical_monitoring', 'slug' => 'tech-site-monitoring', 'name' => 'Технический мониторинг сайта', 'description' => 'Регулярный технический мониторинг сайта.', 'site_type' => 'both', 'cadence' => 'recurring', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'technical_monitoring', 'slug' => 'tech-indexation-check', 'name' => 'Проверка индексации', 'description' => 'Проверка индексации ключевых страниц.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],
        ['category_slug' => 'technical_monitoring', 'slug' => 'tech-error-control', 'name' => 'Контроль ошибок', 'description' => 'Контроль технических ошибок и критичных сбоев.', 'site_type' => 'both', 'cadence' => 'recurring', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 30],

        ['category_slug' => 'semantic_core', 'slug' => 'semantics-core-collection', 'name' => 'Сбор семантического ядра', 'description' => 'Сбор и первичная подготовка семантического ядра.', 'site_type' => 'both', 'cadence' => 'one_time', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'semantic_core', 'slug' => 'semantics-clustering', 'name' => 'Кластеризация запросов', 'description' => 'Кластеризация запросов по группам и интентам.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],
        ['category_slug' => 'semantic_core', 'slug' => 'semantics-refresh', 'name' => 'Актуализация семантики', 'description' => 'Актуализация семантики по приоритетным группам.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 30],

        ['category_slug' => 'onpage', 'slug' => 'onpage-meta-optimization', 'name' => 'Оптимизация мета-тегов', 'description' => 'Оптимизация title/description и связанных мета-тегов.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'onpage', 'slug' => 'onpage-page-structure', 'name' => 'Оптимизация структуры страниц', 'description' => 'Оптимизация структуры и элементов страниц.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],
        ['category_slug' => 'onpage', 'slug' => 'onpage-internal-linking', 'name' => 'Внутренняя перелинковка', 'description' => 'Доработка внутренней перелинковки.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 30],

        ['category_slug' => 'content', 'slug' => 'content-tz-prep', 'name' => 'Подготовка технических заданий на тексты', 'description' => 'Подготовка ТЗ на тексты для приоритетных страниц.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'content', 'slug' => 'content-write-revise', 'name' => 'Написание и доработка текстов', 'description' => 'Написание или доработка текстов по согласованным ТЗ.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],
        ['category_slug' => 'content', 'slug' => 'content-publish', 'name' => 'Размещение текстов', 'description' => 'Размещение согласованных текстов на сайте.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 30],

        ['category_slug' => 'link_building', 'slug' => 'links-profile-analysis', 'name' => 'Анализ ссылочного профиля', 'description' => 'Анализ текущего ссылочного профиля.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'link_building', 'slug' => 'links-platform-selection', 'name' => 'Подбор площадок', 'description' => 'Подбор площадок для размещений.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],
        ['category_slug' => 'link_building', 'slug' => 'links-placement', 'name' => 'Размещение ссылок', 'description' => 'Размещение ссылок по согласованному плану.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 30],

        ['category_slug' => 'commercial_factors', 'slug' => 'commercial-analysis', 'name' => 'Анализ коммерческих факторов', 'description' => 'Анализ коммерческих факторов приоритетных страниц.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'commercial_factors', 'slug' => 'commercial-page-recommendations', 'name' => 'Рекомендации по карточкам и страницам', 'description' => 'Рекомендации по доработке карточек и коммерческих страниц.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],

        ['category_slug' => 'behavioral_factors_internal', 'slug' => 'bf-internal-improve', 'name' => 'Улучшение внутренних поведенческих факторов', 'description' => 'Работы по улучшению внутренних ПФ.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 0, 'sort_order' => 10],
        ['category_slug' => 'behavioral_factors_internal', 'slug' => 'bf-internal-user-scenarios', 'name' => 'Доработка пользовательских сценариев', 'description' => 'Доработка ключевых пользовательских сценариев.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 0, 'sort_order' => 20],

        ['category_slug' => 'behavioral_factors_external', 'slug' => 'bf-external-activities', 'name' => 'Внешние поведенческие активности', 'description' => 'Планирование и фиксация внешних ПФ-активностей.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 0, 'sort_order' => 10],

        ['category_slug' => 'serm', 'slug' => 'serm-reputation-monitoring', 'name' => 'Мониторинг репутации', 'description' => 'Мониторинг репутационных упоминаний.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 10],
        ['category_slug' => 'serm', 'slug' => 'serm-reviews-mentions', 'name' => 'Работа с отзывами и упоминаниями', 'description' => 'Работа с отзывами и публичными упоминаниями.', 'site_type' => 'both', 'cadence' => 'as_needed', 'visibility' => 'client_safe', 'fill_mode' => 'manual', 'evidence_required' => 1, 'sort_order' => 20],

        ['category_slug' => 'reporting', 'slug' => 'reporting-monthly-report', 'name' => 'Подготовка ежемесячного отчета', 'description' => 'Подготовка ежемесячного клиентского отчета.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_facing', 'fill_mode' => 'manual', 'evidence_required' => 0, 'sort_order' => 10],
        ['category_slug' => 'reporting', 'slug' => 'reporting-work-plan', 'name' => 'Подготовка плана работ', 'description' => 'Подготовка плана работ на следующий период.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'client_facing', 'fill_mode' => 'manual', 'evidence_required' => 0, 'sort_order' => 20],

        ['category_slug' => 'quantitative_plans', 'slug' => 'qty-content-volume-plan', 'name' => 'Планирование объема текстов', 'description' => 'Планирование объема текстовых работ.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 0, 'sort_order' => 10],
        ['category_slug' => 'quantitative_plans', 'slug' => 'qty-link-placement-plan', 'name' => 'Планирование ссылочных размещений', 'description' => 'Планирование объема ссылочных размещений.', 'site_type' => 'both', 'cadence' => 'monthly', 'visibility' => 'internal', 'fill_mode' => 'manual', 'evidence_required' => 0, 'sort_order' => 20],
    ];
}

/**
 * @return list<array{
 *   title:string,
 *   description:string,
 *   status:string,
 *   period_role:string,
 *   client_visibility:string,
 *   client_summary:?string,
 *   internal_note:string,
 *   work_item_slug:?string,
 *   category_slug:?string,
 *   sort_order:int
 * }>
 */
function monthlyFixtures(): array
{
    return [
        [
            'title' => 'Проведен технический мониторинг сайта',
            'description' => 'Выполнен плановый технический мониторинг демо-проекта.',
            'status' => 'done',
            'period_role' => 'done',
            'client_visibility' => 'client_safe',
            'client_summary' => 'Выполнен технический мониторинг сайта.',
            'internal_note' => FIXTURE_NOTE,
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
            'internal_note' => FIXTURE_NOTE,
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
            'internal_note' => FIXTURE_NOTE,
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
            'internal_note' => FIXTURE_NOTE,
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
            'internal_note' => FIXTURE_NOTE,
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
            'internal_note' => FIXTURE_NOTE,
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
            'internal_note' => FIXTURE_NOTE,
            'work_item_slug' => null,
            'category_slug' => 'reporting',
            'sort_order' => 70,
        ],
    ];
}

function upsertCategory(PDO $pdo, array $row): string
{
    $existing = $pdo->prepare('SELECT id FROM seo_work_categories WHERE slug = :slug LIMIT 1');
    $existing->execute([':slug' => $row['slug']]);
    $id = $existing->fetchColumn();
    if ($id !== false) {
        $upd = $pdo->prepare(
            'UPDATE seo_work_categories
             SET name = :name,
                 description = :description,
                 sort_order = :sort_order,
                 is_active = 1,
                 source = :source,
                 updated_at = CURRENT_TIMESTAMP
             WHERE id = :id'
        );
        $upd->execute([
            ':name' => $row['name'],
            ':description' => $row['description'],
            ':sort_order' => $row['sort_order'],
            ':source' => SOURCE_ATTR,
            ':id' => (int) $id,
        ]);
        return 'updated';
    }

    $ins = $pdo->prepare(
        'INSERT INTO seo_work_categories
         (slug, name, description, sort_order, is_active, source, created_at, updated_at)
         VALUES
         (:slug, :name, :description, :sort_order, 1, :source, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)'
    );
    $ins->execute([
        ':slug' => $row['slug'],
        ':name' => $row['name'],
        ':description' => $row['description'],
        ':sort_order' => $row['sort_order'],
        ':source' => SOURCE_ATTR,
    ]);
    return 'inserted';
}

/**
 * @param array<string,int> $categoryIds
 */
function upsertWorkItem(PDO $pdo, array $row, array $categoryIds): string
{
    $categoryId = $categoryIds[$row['category_slug']] ?? null;
    if ($categoryId === null) {
        throw new RuntimeException('Missing category for work item: ' . $row['slug']);
    }

    $existing = $pdo->prepare('SELECT id FROM seo_work_items WHERE slug = :slug LIMIT 1');
    $existing->execute([':slug' => $row['slug']]);
    $id = $existing->fetchColumn();
    if ($id !== false) {
        $upd = $pdo->prepare(
            'UPDATE seo_work_items
             SET category_id = :category_id,
                 name = :name,
                 description = :description,
                 site_type = :site_type,
                 cadence = :cadence,
                 visibility = :visibility,
                 fill_mode = :fill_mode,
                 evidence_required = :evidence_required,
                 sort_order = :sort_order,
                 is_active = 1,
                 source = :source,
                 updated_at = CURRENT_TIMESTAMP
             WHERE id = :id'
        );
        $upd->execute([
            ':category_id' => $categoryId,
            ':name' => $row['name'],
            ':description' => $row['description'],
            ':site_type' => $row['site_type'],
            ':cadence' => $row['cadence'],
            ':visibility' => $row['visibility'],
            ':fill_mode' => $row['fill_mode'],
            ':evidence_required' => $row['evidence_required'],
            ':sort_order' => $row['sort_order'],
            ':source' => SOURCE_ATTR,
            ':id' => (int) $id,
        ]);
        return 'updated';
    }

    $ins = $pdo->prepare(
        'INSERT INTO seo_work_items
         (category_id, slug, name, description, site_type, cadence, visibility, fill_mode,
          evidence_required, sort_order, is_active, source, created_at, updated_at)
         VALUES
         (:category_id, :slug, :name, :description, :site_type, :cadence, :visibility, :fill_mode,
          :evidence_required, :sort_order, 1, :source, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)'
    );
    $ins->execute([
        ':category_id' => $categoryId,
        ':slug' => $row['slug'],
        ':name' => $row['name'],
        ':description' => $row['description'],
        ':site_type' => $row['site_type'],
        ':cadence' => $row['cadence'],
        ':visibility' => $row['visibility'],
        ':fill_mode' => $row['fill_mode'],
        ':evidence_required' => $row['evidence_required'],
        ':sort_order' => $row['sort_order'],
        ':source' => SOURCE_ATTR,
    ]);
    return 'inserted';
}

/**
 * @return array<string,int>
 */
function loadCategoryIds(PDO $pdo): array
{
    $rows = $pdo->query('SELECT id, slug FROM seo_work_categories')->fetchAll();
    $map = [];
    foreach ($rows as $row) {
        $map[(string) $row['slug']] = (int) $row['id'];
    }
    return $map;
}

/**
 * @return array<string,int>
 */
function loadWorkItemIds(PDO $pdo): array
{
    $rows = $pdo->query('SELECT id, slug FROM seo_work_items')->fetchAll();
    $map = [];
    foreach ($rows as $row) {
        $map[(string) $row['slug']] = (int) $row['id'];
    }
    return $map;
}

/**
 * @param array<string,int> $categoryIds
 * @param array<string,int> $workItemIds
 */
function upsertMonthlyEntry(PDO $pdo, int $monthlyReportId, array $row, array $categoryIds, array $workItemIds): string
{
    $existing = $pdo->prepare(
        'SELECT id FROM monthly_report_work_entries
         WHERE monthly_report_id = :monthly_report_id AND title = :title
         LIMIT 1'
    );
    $existing->execute([
        ':monthly_report_id' => $monthlyReportId,
        ':title' => $row['title'],
    ]);
    $id = $existing->fetchColumn();

    $workItemId = null;
    if (!empty($row['work_item_slug'])) {
        $workItemId = $workItemIds[$row['work_item_slug']] ?? null;
    }
    $categoryId = null;
    if (!empty($row['category_slug'])) {
        $categoryId = $categoryIds[$row['category_slug']] ?? null;
    }

    $params = [
        ':monthly_report_id' => $monthlyReportId,
        ':work_item_id' => $workItemId,
        ':category_id' => $categoryId,
        ':title' => $row['title'],
        ':description' => $row['description'],
        ':status' => $row['status'],
        ':period_role' => $row['period_role'],
        ':client_visibility' => $row['client_visibility'],
        ':client_summary' => $row['client_summary'],
        ':internal_note' => $row['internal_note'],
        ':evidence_note' => FIXTURE_NOTE,
        ':sort_order' => $row['sort_order'],
    ];

    if ($id !== false) {
        $upd = $pdo->prepare(
            'UPDATE monthly_report_work_entries
             SET work_item_id = :work_item_id,
                 category_id = :category_id,
                 description = :description,
                 status = :status,
                 period_role = :period_role,
                 client_visibility = :client_visibility,
                 client_summary = :client_summary,
                 internal_note = :internal_note,
                 evidence_note = :evidence_note,
                 sort_order = :sort_order,
                 updated_at = CURRENT_TIMESTAMP
             WHERE id = :id'
        );
        $upd->execute([
            ':work_item_id' => $params[':work_item_id'],
            ':category_id' => $params[':category_id'],
            ':description' => $params[':description'],
            ':status' => $params[':status'],
            ':period_role' => $params[':period_role'],
            ':client_visibility' => $params[':client_visibility'],
            ':client_summary' => $params[':client_summary'],
            ':internal_note' => $params[':internal_note'],
            ':evidence_note' => $params[':evidence_note'],
            ':sort_order' => $params[':sort_order'],
            ':id' => (int) $id,
        ]);
        return 'updated';
    }

    $ins = $pdo->prepare(
        'INSERT INTO monthly_report_work_entries
         (monthly_report_id, work_item_id, category_id, title, description, status, period_role,
          client_visibility, client_summary, internal_note, evidence_note, sort_order,
          created_at, updated_at)
         VALUES
         (:monthly_report_id, :work_item_id, :category_id, :title, :description, :status, :period_role,
          :client_visibility, :client_summary, :internal_note, :evidence_note, :sort_order,
          CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)'
    );
    $ins->execute($params);
    return 'inserted';
}

$skipMonthly = in_array('--skip-monthly-fixtures', $argv, true);

$cfg = loadDbConfig();
if ($cfg['database'] === '' || $cfg['username'] === '') {
    fwrite(STDERR, "Missing DB_DATABASE or DB_USERNAME.\n");
    exit(2);
}
assertLocalDb($cfg);

try {
    $pdo = connect($cfg);
} catch (Throwable $e) {
    fwrite(STDERR, 'DB connection failed: ' . $e->getMessage() . "\n");
    exit(4);
}

foreach (['seo_work_categories', 'seo_work_items', 'monthly_report_work_entries'] as $table) {
    if (!tableExists($pdo, $table)) {
        fwrite(STDERR, "REFUSED: required table missing: {$table}. Apply DB-11 migration first.\n");
        exit(3);
    }
}

$catInserted = 0;
$catUpdated = 0;
foreach (categories() as $category) {
    $result = upsertCategory($pdo, $category);
    if ($result === 'inserted') {
        $catInserted++;
    } else {
        $catUpdated++;
    }
}
$categoryIds = loadCategoryIds($pdo);

$itemInserted = 0;
$itemUpdated = 0;
foreach (workItems() as $item) {
    $result = upsertWorkItem($pdo, $item, $categoryIds);
    if ($result === 'inserted') {
        $itemInserted++;
    } else {
        $itemUpdated++;
    }
}
$workItemIds = loadWorkItemIds($pdo);

$entryInserted = 0;
$entryUpdated = 0;
$entrySkipped = false;
if ($skipMonthly) {
    $entrySkipped = true;
    fwrite(STDOUT, "Monthly fixtures: skipped by flag.\n");
} else {
    $stmt = $pdo->prepare('SELECT id FROM monthly_report_contents WHERE id = :id LIMIT 1');
    $stmt->execute([':id' => TARGET_MONTHLY_REPORT_ID]);
    $monthlyExists = $stmt->fetchColumn() !== false;
    if (!$monthlyExists) {
        $entrySkipped = true;
        fwrite(STDOUT, "Monthly fixtures: skipped (monthly_report_contents id 1 not found).\n");
    } else {
        foreach (monthlyFixtures() as $entry) {
            $result = upsertMonthlyEntry($pdo, TARGET_MONTHLY_REPORT_ID, $entry, $categoryIds, $workItemIds);
            if ($result === 'inserted') {
                $entryInserted++;
            } else {
                $entryUpdated++;
            }
        }
    }
}

$categoryCount = (int) $pdo->query('SELECT COUNT(*) FROM seo_work_categories')->fetchColumn();
$itemCount = (int) $pdo->query('SELECT COUNT(*) FROM seo_work_items')->fetchColumn();
$entryCount = (int) $pdo->query(
    'SELECT COUNT(*) FROM monthly_report_work_entries WHERE monthly_report_id = ' . TARGET_MONTHLY_REPORT_ID
)->fetchColumn();

fwrite(STDOUT, "Seed source: " . SOURCE_ATTR . "\n");
fwrite(STDOUT, "Categories: inserted={$catInserted} updated={$catUpdated} total={$categoryCount}\n");
fwrite(STDOUT, "Work items: inserted={$itemInserted} updated={$itemUpdated} total={$itemCount}\n");
if ($entrySkipped) {
    fwrite(STDOUT, "Monthly entries: skipped total_for_report_1={$entryCount}\n");
} else {
    fwrite(STDOUT, "Monthly entries: inserted={$entryInserted} updated={$entryUpdated} total_for_report_1={$entryCount}\n");
}
fwrite(STDOUT, "OK\n");
exit(0);

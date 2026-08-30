<?php
declare(strict_types=1);
/** @var array<string, mixed> $status */
$db = is_array($status['db'] ?? null) ? $status['db'] : [];
$overall = (string) ($status['overall'] ?? 'unknown');
$overallRu = match ($overall) {
    'ok' => 'В порядке',
    'degraded' => 'Есть замечания',
    'fail', 'failed', 'error' => 'Ошибка',
    default => $overall,
};
$dbOk = !empty($db['connection_ok']);
$features = is_array($status['features'] ?? null) ? $status['features'] : [];
$deferred = is_array($status['deferred'] ?? null) ? $status['deferred'] : [];
$featureLabels = [
    'monthly_reports' => 'Месячные отчеты',
    'work_entries' => 'Работы за месяц',
    'summary_assembly' => 'Сборка черновика',
    'client_preview' => 'Клиентский preview',
];
$deferredLabels = [
    'pdf_regeneration' => 'Пересборка PDF',
    'export_html_alignment' => 'Выравнивание HTML export',
];
?>
<section class="mb-24">
    <div class="section-heading section-title">
        <span class="section-number">01</span>
        <div class="section-heading__text">
            <h2>Состояние системы</h2>
            <p>Локальная тестовая среда. Не продакшен. Секреты и токены здесь не показываются.</p>
        </div>
    </div>
    <div class="card panel health-status-card">
        <div class="card__body">
            <p>
                <span class="badge badge-<?= e($overall) ?>"><?= e($overallRu) ?></span>
                <span class="badge badge--draft">Локальная тестовая среда</span>
            </p>
            <ul class="facts health-facts">
                <li><strong>Приложение:</strong> <?= e((string) ($status['app'] ?? 'i-SEO Report Hub')) ?></li>
                <li><strong>Среда:</strong> локальная · не production</li>
                <li><strong>Статус runtime:</strong> <?= e($overallRu) ?></li>
                <li><strong>База данных:</strong>
                    <span class="<?= $dbOk ? 'ok' : 'warn' ?>"><?= $dbOk ? 'OK' : e((string) ($db['status'] ?? 'нет связи')) ?></span>
                </li>
                <li><strong>Этап продукта:</strong> <?= e((string) ($status['stage'] ?? 'Local MVP / UI polish')) ?></li>
                <li><strong>Проверено:</strong> <?= e((string) ($status['checked_at'] ?? '—')) ?></li>
            </ul>
        </div>
    </div>
</section>

<section class="mb-24 card-grid status-grid">
    <article class="card panel kpi-card health-mvp-card">
        <div class="card__body">
            <h2 class="kpi-card__label">Что уже работает в MVP</h2>
            <ul class="facts">
                <?php foreach ($features as $featureKey): ?>
                    <li><?= e($featureLabels[(string) $featureKey] ?? (string) $featureKey) ?></li>
                <?php endforeach; ?>
                <li>Exports / shares уже есть в локальной БД</li>
            </ul>
            <p class="note">Основной демо-путь: финализированный отчет (id 1). Пустой черновик (id 5) — намеренный empty draft.</p>
        </div>
    </article>

    <article class="card panel kpi-card health-deferred-card">
        <div class="card__body">
            <h2 class="kpi-card__label">Сейчас отложено</h2>
            <ul class="facts">
                <?php foreach ($deferred as $deferredKey): ?>
                    <li><?= e($deferredLabels[(string) $deferredKey] ?? (string) $deferredKey) ?></li>
                <?php endforeach; ?>
                <li><strong>Export 4:</strong> не менять (заморожен до финальной полировки PDF/export)</li>
            </ul>
            <p class="note">PDF/export regeneration отложена. Не считайте её завершённой.</p>
        </div>
    </article>
</section>

<section class="mb-24">
    <details class="card panel tech-details health-tech-details">
        <summary>Технические детали (для разработчика)</summary>
        <div class="card__body">
            <ul class="facts">
                <li><strong>PHP:</strong> <?= e((string) $status['php_version']) ?> · <?= e((string) $status['sapi']) ?></li>
                <li><strong>WordPress:</strong> <?= e((string) $status['wordpress']) ?></li>
                <li><strong>Локальный env-файл есть:</strong> <?= !empty($status['env_local_present']) ? 'да' : 'нет' ?> (содержимое не показывается)</li>
                <li><strong>Имя БД:</strong> <?= e((string) ($db['database'] ?? '—')) ?></li>
                <li><strong>Миграций:</strong> <?= e((string) ($db['migration_count'] ?? '—')) ?></li>
                <li><strong>Последняя миграция:</strong> <?= e((string) ($db['latest_migration'] ?? '—')) ?></li>
                <li><strong>Таблиц есть / ожидается:</strong>
                    <?= e((string) ($db['tables_present'] ?? '—')) ?> /
                    <?= e((string) ($db['tables_expected'] ?? '—')) ?>
                </li>
                <li><strong>Пользователей / ролей:</strong>
                    <?= e((string) ($db['users_count'] ?? '—')) ?> /
                    <?= e((string) ($db['roles_count'] ?? '—')) ?>
                </li>
                <li><strong>Нужные расширения:</strong>
                    <span class="<?= !empty($status['all_required_ok']) ? 'ok' : 'warn' ?>">
                        <?= !empty($status['all_required_ok']) ? 'все есть' : 'чего-то не хватает' ?>
                    </span>
                </li>
            </ul>
            <h3>Нужные расширения</h3>
            <ul class="ext-list">
                <?php foreach ($status['required'] as $name => $present): ?>
                    <li class="<?= $present ? 'ok' : 'missing' ?>">
                        <?= e((string) $name) ?> — <?= $present ? 'есть' : 'нет' ?>
                    </li>
                <?php endforeach; ?>
            </ul>
            <h3>Дополнительные расширения</h3>
            <ul class="ext-list">
                <?php foreach ($status['optional'] as $name => $present): ?>
                    <li class="<?= $present ? 'ok' : 'warn' ?>">
                        <?= e((string) $name) ?> — <?= $present ? 'есть' : 'нет' ?>
                    </li>
                <?php endforeach; ?>
            </ul>
            <p class="note">Пароли, токены, хеши и детали SQL-ошибок здесь не показываются.</p>
        </div>
    </details>
</section>

<section class="mb-24">
    <div class="card panel">
        <div class="card__body">
            <p class="action-row"><a class="btn btn-secondary" href="<?= e(url_path('/')) ?>">На главную</a></p>
        </div>
    </div>
</section>

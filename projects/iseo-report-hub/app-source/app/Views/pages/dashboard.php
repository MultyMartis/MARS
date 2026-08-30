<?php
declare(strict_types=1);
/** @var list<array{title:string,status:string,detail:string,status_label?:string}> $cards */
/** @var array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user */
/** @var string $authStatus */
/** @var int|null $periodCount */
/** @var int|null $checkpointCount */
/** @var int|null $monthlyCount */
/** @var int|null $blockCount */
/** @var int|null $activeShareCount */
/** @var array{
 *   available:bool,
 *   client_name:string,
 *   project_name:string,
 *   period_count:int,
 *   report_count:int,
 *   latest_monthly_id:?int,
 *   has_ready_pdf:bool,
 *   has_active_share:bool,
 *   export_href:?string,
 *   shares_href:?string
 * } $scenario
 */

$statusRu = static function (string $status): string {
    return match ($status) {
        'ready' => 'Готово',
        'pending' => 'В работе',
        'failed' => 'Ошибка',
        default => $status,
    };
};

$scenario = is_array($scenario ?? null) ? $scenario : [
    'available' => false,
    'client_name' => '',
    'project_name' => '',
    'period_count' => 0,
    'report_count' => 0,
    'latest_monthly_id' => null,
    'has_ready_pdf' => false,
    'has_active_share' => false,
    'export_href' => null,
    'shares_href' => null,
];

$scenarioTitle = 'Нет активного сценария';
if (!empty($scenario['available'])) {
    $client = trim((string) ($scenario['client_name'] ?? ''));
    $project = trim((string) ($scenario['project_name'] ?? ''));
    if ($client !== '' && $project !== '') {
        $scenarioTitle = $client . ' · ' . $project;
    } elseif ($client !== '') {
        $scenarioTitle = $client;
    } elseif ($project !== '') {
        $scenarioTitle = $project;
    }
}

$hasReadyPdf = !empty($scenario['has_ready_pdf']);
$hasActiveShare = !empty($scenario['has_active_share']);
$latestMonthlyId = isset($scenario['latest_monthly_id']) ? (int) $scenario['latest_monthly_id'] : 0;
$dashIsPrivileged = is_array($user)
    && (
        in_array('admin_owner', $user['roles'] ?? [], true)
        || in_array('seo_lead_reviewer', $user['roles'] ?? [], true)
    );

$roleLabels = [];
if (is_array($user) && !empty($user['roles']) && is_array($user['roles'])) {
    foreach ($user['roles'] as $role) {
        if (is_string($role) && $role !== '') {
            $roleLabels[] = ui_role_label($role);
        }
    }
}
?>
<section class="mb-24">
    <div class="section-heading section-title">
        <span class="section-number">01</span>
        <div class="section-heading__text">
            <h2>Рабочий контур</h2>
            <p>Локальная демка для SEO-специалиста: периоды, отчёты и статусы работ</p>
        </div>
    </div>

    <article class="card panel dashboard-hero primary-file-card">
        <div class="card__body">
            <div class="panel-head">
                <h3 class="card__title"><?= e($scenarioTitle) ?></h3>
                <p class="action-row">
                    <?php if ($hasReadyPdf): ?>
                        <span class="badge badge--completed status-badge status-ready">PDF готов</span>
                    <?php else: ?>
                        <span class="badge badge--draft status-badge">PDF ещё не создан</span>
                    <?php endif; ?>
                    <?php if ($hasActiveShare): ?>
                        <span class="badge badge--completed">Активная ссылка есть</span>
                    <?php else: ?>
                        <span class="badge badge--draft">Активной ссылки нет</span>
                    <?php endif; ?>
                </p>
            </div>
            <?php if (!empty($scenario['available'])): ?>
                <p class="note">
                    Отчётных периодов: <?= e((string) (int) ($scenario['period_count'] ?? 0)) ?>
                    · Месячных отчётов: <?= e((string) (int) ($scenario['report_count'] ?? 0)) ?>
                </p>
            <?php else: ?>
                <p class="note">В базе пока нет клиента/проекта для рабочего контура.</p>
            <?php endif; ?>
            <p class="note dashboard-auth-line">
                <strong><?= e($authStatus) ?></strong>
                · Локальная тестовая среда · <span class="fixture-badge"><?= e(\Iseo\Support\UiLabels::fixtureBadge()) ?></span>
            </p>
            <?php if (is_array($user)): ?>
                <ul class="facts manager-facts">
                    <li><strong>Имя:</strong> <?= e(ui_display_user_name($user['name'] ?? null, $user['email'] ?? null)) ?></li>
                    <li><strong>Email:</strong> <?= e($user['email']) ?></li>
                    <li><strong>Роли:</strong> <?= e($roleLabels !== [] ? implode(', ', $roleLabels) : '—') ?></li>
                </ul>
            <?php endif; ?>
            <p class="action-row quick-actions">
                <a class="btn btn-primary" href="<?= e(url_path('/reporting-periods')) ?>">Отчетные периоды</a>
                <?php if ($latestMonthlyId > 0): ?>
                    <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $latestMonthlyId)) ?>">Последний отчет</a>
                <?php else: ?>
                    <span class="btn btn-secondary" aria-disabled="true">Последний отчет</span>
                <?php endif; ?>
                <?php if ($hasReadyPdf && !empty($scenario['export_href'])): ?>
                    <a class="btn btn-secondary" href="<?= e(url_path((string) $scenario['export_href'])) ?>">Файлы отчета</a>
                <?php else: ?>
                    <span class="btn btn-secondary" aria-disabled="true" title="PDF ещё не создан">PDF ещё не создан</span>
                <?php endif; ?>
                <?php if ($dashIsPrivileged): ?>
                    <a class="btn btn-secondary" href="<?= e(url_path('/health')) ?>">Состояние системы</a>
                <?php endif; ?>
            </p>
        </div>
    </article>
</section>

<section class="mb-24">
    <div class="section-heading section-title">
        <span class="section-number">02</span>
        <div class="section-heading__text">
            <h2>Быстрые действия</h2>
            <p>Рабочий путь: периоды → отчет → предпросмотр → (позже) PDF / ссылка</p>
        </div>
    </div>

    <div class="card panel">
        <div class="card__body">
            <p class="action-row quick-actions">
                <a class="btn btn-primary" href="<?= e(url_path('/reporting-periods')) ?>">Отчетные периоды<?= isset($periodCount) && $periodCount !== null ? ' (' . e((string) $periodCount) . ')' : '' ?></a>
                <?php if ($latestMonthlyId > 0): ?>
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $latestMonthlyId)) ?>">Последний отчет</a>
                <?php endif; ?>
                <?php if ($hasReadyPdf && !empty($scenario['export_href'])): ?>
                    <a class="btn btn-secondary" href="<?= e(url_path((string) $scenario['export_href'])) ?>">Файлы отчета</a>
                <?php endif; ?>
                <?php if ($hasActiveShare && !empty($scenario['shares_href'])): ?>
                    <a class="btn btn-secondary" href="<?= e(url_path((string) $scenario['shares_href'])) ?>">Ссылки для клиента</a>
                <?php endif; ?>
                <?php if ($dashIsPrivileged): ?>
                    <a class="btn btn-secondary" href="<?= e(url_path('/health')) ?>">Состояние системы</a>
                <?php endif; ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/logout')) ?>">Выйти</a>
            </p>
        </div>
    </div>
</section>

<section class="mb-24">
    <div class="section-heading section-title">
        <span class="section-number">03</span>
        <div class="section-heading__text">
            <h2>Статус локальной системы</h2>
            <p>Технические модули — свёрнуты по умолчанию</p>
        </div>
    </div>

    <details class="card panel tech-details technical-details dashboard-status-details">
        <summary>Статус модулей</summary>
        <section class="status-grid card-grid">
            <?php foreach ($cards as $card): ?>
                <article class="kpi-card status-card status-<?= e($card['status']) ?>">
                    <p class="kpi-card__label"><?= e($card['title']) ?></p>
                    <p class="status-pill badge"><?= e((string) ($card['status_label'] ?? $statusRu($card['status']))) ?></p>
                    <p class="note"><?= e($card['detail']) ?></p>
                </article>
            <?php endforeach; ?>
        </section>
        <p class="note">
            Еженедельные заметки, месячные отчеты и блоки открываются через отчетный период.
            <?php if (isset($checkpointCount) && $checkpointCount !== null): ?>
                Заметок: <?= e((string) $checkpointCount) ?>.
            <?php endif; ?>
            <?php if (isset($monthlyCount) && $monthlyCount !== null): ?>
                Месячных отчетов: <?= e((string) $monthlyCount) ?>.
            <?php endif; ?>
            <?php if (isset($blockCount) && $blockCount !== null): ?>
                Блоков: <?= e((string) $blockCount) ?>.
            <?php endif; ?>
        </p>
    </details>
</section>

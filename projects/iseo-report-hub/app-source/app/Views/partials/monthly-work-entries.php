<?php
declare(strict_types=1);
/** @var int $reportId */
/** @var list<array<string, mixed>> $workEntries */
/** @var array<string, int> $workEntryCounters */
/** @var array{categories_active:int,items_active:int,source:string,available:bool} $catalogueSummary */
/** @var bool $canCreateWorkEntry */
/** @var bool $canEditWorkEntries */
/** @var bool $parentFinalized */
/** @var bool $isSpecialistFlow */
$workEntries = $workEntries ?? [];
$workEntryCounters = $workEntryCounters ?? [
    'total' => 0,
    'status_done' => 0,
    'period_planned_next' => 0,
    'period_risk_note' => 0,
    'visibility_client_facing' => 0,
    'visibility_client_safe' => 0,
    'visibility_internal' => 0,
];
$catalogueSummary = $catalogueSummary ?? [
    'categories_active' => 0,
    'items_active' => 0,
    'source' => 'nikita_catalogue_v1',
    'available' => false,
];
$canCreateWorkEntry = $canCreateWorkEntry ?? false;
$canEditWorkEntries = $canEditWorkEntries ?? $canCreateWorkEntry;
$parentFinalized = $parentFinalized ?? false;
$isSpecialistFlow = $isSpecialistFlow ?? false;
?>
<section class="panel work-entries-panel" id="work-entries">
    <div class="panel-head">
        <h2>Работы за месяц</h2>
        <p class="work-entries-actions">
            <?php if ($canCreateWorkEntry): ?>
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/work-entries/create')) ?>">Добавить работу</a>
            <?php endif; ?>
            <?php if (!$isSpecialistFlow): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/assembly-preview')) ?>">Собрать черновик</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">Блоки отчета</a>
            <?php endif; ?>
        </p>
    </div>

    <p class="work-entries-subtitle">
        Структурированный список SEO-работ. Можно посмотреть черновик для клиента — без PDF и публичной ссылки.
    </p>

    <?php if ($parentFinalized && $isSpecialistFlow): ?>
        <p class="note work-entries-notice work-entries-notice--finalized">
            Отчет финализирован. Для SEO-специалиста он открыт только для просмотра.
        </p>
    <?php elseif ($parentFinalized): ?>
        <p class="note work-entries-notice work-entries-notice--finalized">
            Месячный отчет уже финализирован. Изменения в работах не пересобирают PDF и снимки автоматически.
        </p>
    <?php else: ?>
        <p class="note work-entries-notice">
            Редактор работ доступен. Физическое удаление недоступно — убирайте работу из активной через статусы «Отменено» / «Отложено» или видимость «Внутреннее».
        </p>
    <?php endif; ?>

    <ul class="work-entry-counters">
        <li><strong>Всего:</strong> <?= e((string) $workEntryCounters['total']) ?></li>
        <li><strong>Выполнено:</strong> <?= e((string) $workEntryCounters['status_done']) ?></li>
        <li><strong>План на след. период:</strong> <?= e((string) $workEntryCounters['period_planned_next']) ?></li>
        <li><strong>Риск / заметка:</strong> <?= e((string) $workEntryCounters['period_risk_note']) ?></li>
        <li><strong>Клиенту:</strong> <?= e((string) $workEntryCounters['visibility_client_facing']) ?></li>
        <li><strong>Для отчета:</strong> <?= e((string) $workEntryCounters['visibility_client_safe']) ?></li>
        <li><strong>Внутренние:</strong> <?= e((string) $workEntryCounters['visibility_internal']) ?></li>
    </ul>

    <?php if (!empty($catalogueSummary['available'])): ?>
        <details class="tech-details catalogue-summary">
            <summary>Каталог SEO-работ подключен</summary>
            <ul class="facts">
                <li><strong>Активных категорий:</strong> <?= e((string) $catalogueSummary['categories_active']) ?></li>
                <li><strong>Активных работ:</strong> <?= e((string) $catalogueSummary['items_active']) ?></li>
                <li><strong>Источник:</strong> <code><?= e((string) $catalogueSummary['source']) ?></code></li>
            </ul>
        </details>
    <?php endif; ?>

    <?php if ($workEntries === []): ?>
        <p class="note work-entries-empty">
            <?php if ($canCreateWorkEntry): ?>
                Работы пока не добавлены. Нажмите «Добавить работу».
            <?php else: ?>
                Работы пока не добавлены.
            <?php endif; ?>
        </p>
    <?php else: ?>
        <div class="work-entry-list">
            <?php foreach ($workEntries as $entry): ?>
                <?php
                $status = (string) ($entry['status'] ?? '');
                $periodRole = (string) ($entry['period_role'] ?? '');
                $visibility = (string) ($entry['client_visibility'] ?? '');
                $categoryName = ui_display_label(trim((string) ($entry['category_name'] ?? '')), '');
                $clientSummary = ui_display_body(trim((string) ($entry['client_summary'] ?? '')), null, '');
                $internalNote = ui_display_body(trim((string) ($entry['internal_note'] ?? '')), null, '');
                $evidenceNote = ui_display_body(trim((string) ($entry['evidence_note'] ?? '')), null, '');
                $description = ui_display_body(trim((string) ($entry['description'] ?? '')), null, '');
                $isInactive = $status === 'cancelled' || $status === 'deferred';
                $cardClass = 'work-entry-card' . ($isInactive ? ' work-entry-card--inactive' : '');
                ?>
                <article class="<?= e($cardClass) ?>">
                    <div class="work-entry-card__head">
                        <h3 class="work-entry-card__title"><?= e(ui_display_label((string) ($entry['title'] ?? ''), '—')) ?></h3>
                        <div class="work-entry-card__badges">
                            <?php if ($categoryName !== ''): ?>
                                <span class="type-badge work-entry-badge work-entry-badge--category"><?= e($categoryName) ?></span>
                            <?php endif; ?>
                            <span class="status-badge status-<?= e($status) ?> work-entry-badge work-entry-badge--status">
                                <?= e(ui_work_entry_status_label($status)) ?>
                            </span>
                            <span class="work-entry-badge work-entry-badge--role work-entry-role-<?= e($periodRole) ?>">
                                <?= e(ui_work_entry_period_role_label($periodRole)) ?>
                            </span>
                            <span class="work-entry-badge work-entry-badge--visibility work-entry-visibility-<?= e($visibility) ?>">
                                <?= e(ui_work_entry_visibility_label($visibility)) ?>
                            </span>
                        </div>
                    </div>

                    <?php if ($clientSummary !== ''): ?>
                        <p class="work-entry-card__summary"><?= e($clientSummary) ?></p>
                    <?php endif; ?>

                    <?php if ($description !== ''): ?>
                        <p class="work-entry-card__description"><?= e($description) ?></p>
                    <?php endif; ?>

                    <?php if ($evidenceNote !== ''): ?>
                        <p class="work-entry-card__evidence"><strong>Доказательства:</strong> <?= e($evidenceNote) ?></p>
                    <?php endif; ?>

                    <?php if ($internalNote !== '' || ($entry['work_item_slug'] ?? null) || ($entry['category_slug'] ?? null)): ?>
                        <details class="tech-details">
                            <summary>Внутренняя заметка / технические детали</summary>
                            <?php if ($internalNote !== ''): ?>
                                <p><?= e($internalNote) ?></p>
                            <?php endif; ?>
                            <ul class="facts">
                                <?php if (!empty($entry['work_item_name'])): ?>
                                    <li><strong>Работа каталога:</strong> <?= e((string) $entry['work_item_name']) ?></li>
                                <?php endif; ?>
                                <?php if (!empty($entry['work_item_slug'])): ?>
                                    <li><strong>Slug работы:</strong> <code><?= e((string) $entry['work_item_slug']) ?></code></li>
                                <?php endif; ?>
                                <?php if (!empty($entry['category_slug'])): ?>
                                    <li><strong>Slug категории:</strong> <code><?= e((string) $entry['category_slug']) ?></code></li>
                                <?php endif; ?>
                                <li><strong>Порядок:</strong> <?= e((string) ($entry['sort_order'] ?? '')) ?></li>
                            </ul>
                        </details>
                    <?php endif; ?>

                    <p class="work-entry-card__actions">
                        <?php if ($canEditWorkEntries): ?>
                            <a class="btn btn-secondary btn-sm" href="<?= e(url_path('/monthly-report-work-entries/' . (int) $entry['id'] . '/edit')) ?>">Изменить</a>
                        <?php endif; ?>
                    </p>
                </article>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>
</section>

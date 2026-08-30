<?php
declare(strict_types=1);
/** @var array<string, mixed> $report */
/** @var array<string, mixed>|null $period */
/** @var list<array<string, mixed>> $sourceCheckpoints */
/** @var bool $canEdit */
/** @var list<array<string, mixed>> $reportBlocks */
/** @var bool $canCreateBlock */
/** @var bool $parentFinalized */
/** @var array<string, mixed> $readiness */
/** @var array<string, mixed>|null $activeSnapshot */
/** @var bool $canCreateSnapshot */
/** @var list<array<string, mixed>> $workEntries */
/** @var array<string, int> $workEntryCounters */
/** @var array{categories_active:int,items_active:int,source:string,available:bool} $catalogueSummary */
/** @var array{snapshot_exists:bool,pdf_ready:bool,pdf_export_id:?int,active_share:bool,share_export_id:?int} $deliveryReadiness */
/** @var bool $canCreateWorkEntry */
/** @var bool $canEditWorkEntries */
/** @var bool $isSpecialistFlow */
/** @var bool $showAdminControls */
/** @var \Iseo\Services\CsrfService $csrf */
$periodId = (int) $report['reporting_period_id'];
$reportId = (int) $report['id'];
$sourceCheckpoints = $sourceCheckpoints ?? [];
$reportBlocks = $reportBlocks ?? [];
$canCreateBlock = $canCreateBlock ?? false;
$parentFinalized = !empty($parentFinalized);
$readiness = $readiness ?? ['ready' => false, 'gates' => [], 'failed_gates' => [], 'actions' => []];
$gates = is_array($readiness['gates'] ?? null) ? $readiness['gates'] : [];
$actions = is_array($readiness['actions'] ?? null) ? $readiness['actions'] : [];
$failedGates = is_array($readiness['failed_gates'] ?? null) ? $readiness['failed_gates'] : [];
$activeSnapshot = $activeSnapshot ?? null;
$canCreateSnapshot = !empty($canCreateSnapshot);
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
$deliveryReadiness = $deliveryReadiness ?? [
    'snapshot_exists' => is_array($activeSnapshot),
    'pdf_ready' => false,
    'pdf_export_id' => null,
    'active_share' => false,
    'share_export_id' => null,
];
$canCreateWorkEntry = !empty($canCreateWorkEntry);
$canEditWorkEntries = !empty($canEditWorkEntries);
$isSpecialistFlow = !empty($isSpecialistFlow);
$showAdminControls = !empty($showAdminControls);
$snapshotId = is_array($activeSnapshot) ? (int) ($activeSnapshot['id'] ?? 0) : 0;
// Only link to exports/shares when a ready PDF / active share actually exists.
$filesHref = (!empty($deliveryReadiness['pdf_ready']) && $snapshotId > 0)
    ? url_path('/report-snapshots/' . $snapshotId . '/exports')
    : null;
$shareExportId = (int) ($deliveryReadiness['share_export_id'] ?? 0);
if ($shareExportId <= 0 && !empty($deliveryReadiness['pdf_export_id'])) {
    $shareExportId = (int) $deliveryReadiness['pdf_export_id'];
}
$sharesHref = (!empty($deliveryReadiness['active_share']) && $shareExportId > 0)
    ? url_path('/report-exports/' . $shareExportId . '/shares')
    : null;
$siteLabel = '';
if (is_array($period)) {
    $siteUrl = trim((string) ($period['primary_site_url'] ?? ''));
    $siteName = trim((string) ($period['primary_site_label'] ?? ''));
    if ($siteUrl !== '' && $siteName !== '') {
        $siteLabel = $siteUrl . ' — ' . $siteName;
    } elseif ($siteUrl !== '') {
        $siteLabel = $siteUrl;
    } elseif ($siteName !== '') {
        $siteLabel = $siteName;
    }
}
$contentFields = [
    'executive_summary',
    'work_completed',
    'results_summary',
    'key_findings',
    'risks_and_blockers',
    'next_month_plan',
    'client_notes',
    'internal_notes',
];
$reportStatus = (string) ($report['status'] ?? '');
$isDraftLike = in_array($reportStatus, ['draft', 'in_progress'], true);
$hasWorkEntries = ((int) ($workEntryCounters['total'] ?? 0)) > 0 || $workEntries !== [];
$hasReportBlocks = $reportBlocks !== [];
$hasSnapshot = is_array($activeSnapshot) || !empty($deliveryReadiness['snapshot_exists']);
$hasExports = !empty($deliveryReadiness['pdf_ready']) || !empty($deliveryReadiness['pdf_export_id']);
$isEmptyDraft = $isDraftLike
    && !$parentFinalized
    && !$hasWorkEntries
    && !$hasReportBlocks;
?>
<section class="panel mr-summary-card<?= $isEmptyDraft ? ' mr-summary-card--empty-draft' : '' ?>">
    <div class="panel-head">
        <h2><?= e($isEmptyDraft
            ? \Iseo\Support\UiLabels::emptyDraftHeading()
            : ui_display_label((string) ($report['title'] ?? ''), 'Месячный отчет')) ?></h2>
        <p class="mr-summary-card__badges">
            <span class="status-badge status-<?= e($reportStatus) ?>"><?= e(ui_status_label($reportStatus)) ?></span>
            <?php if ($isEmptyDraft): ?>
                <span class="badge empty-draft-badge"><?= e(\Iseo\Support\UiLabels::emptyDraftLabel()) ?></span>
            <?php elseif ($parentFinalized): ?>
                <span class="finalized-badge">Финализирован — заблокировано</span>
            <?php else: ?>
                <span class="draft-warning-badge">Не финализирован</span>
            <?php endif; ?>
            <?php if (!$isEmptyDraft): ?>
                <?php if (!empty($deliveryReadiness['pdf_ready'])): ?>
                    <span class="badge badge--completed status-badge status-ready">PDF готов</span>
                <?php else: ?>
                    <span class="badge badge--draft">PDF еще не создан</span>
                <?php endif; ?>
                <?php if (!empty($deliveryReadiness['active_share'])): ?>
                    <span class="badge badge--completed">Активная ссылка есть</span>
                <?php else: ?>
                    <span class="badge badge--draft">Активной ссылки нет</span>
                <?php endif; ?>
            <?php endif; ?>
        </p>
    </div>
    <ul class="facts manager-facts mr-summary-facts">
        <li><strong>Период:</strong>
            <code><?= e((string) ($report['period_key'] ?? '')) ?></code>
            · <?= e((string) ($report['period_start'] ?? '')) ?> – <?= e((string) ($report['period_end'] ?? '')) ?>
        </li>
        <li><strong>Клиент:</strong> <?= e(ui_display_label((string) ($report['client_name'] ?? ''), '—')) ?></li>
        <li><strong>Проект:</strong> <?= e(ui_display_label((string) ($report['project_name'] ?? ''), '—')) ?></li>
        <?php if ($siteLabel !== ''): ?>
            <li><strong>Сайт:</strong> <?= e($siteLabel) ?></li>
        <?php endif; ?>
        <?php if (!$isEmptyDraft): ?>
            <li><strong>Финализация:</strong>
                <?php if ($parentFinalized): ?>
                    да<?= !empty($report['finalized_at']) ? ' · ' . e((string) $report['finalized_at']) : '' ?>
                <?php else: ?>
                    нет
                <?php endif; ?>
            </li>
        <?php endif; ?>
    </ul>
    <?php if ($isEmptyDraft): ?>
        <p class="note empty-draft-message"><?= e(\Iseo\Support\UiLabels::emptyDraftMessage()) ?></p>
        <p class="note mr-summary-hint"><?= e(\Iseo\Support\UiLabels::emptyDraftPreviewExpectation()) ?></p>
        <div class="mr-workflow-actions" aria-label="Действия для пустого черновика">
            <p class="mr-workflow-actions__primary action-row">
                <?php if ($canCreateWorkEntry): ?>
                    <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/work-entries/create')) ?>">Добавить работу</a>
                <?php endif; ?>
                <?php if (!$parentFinalized && ($isSpecialistFlow || $canEdit)): ?>
                    <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/content-workflow')) ?>">Тексты отчета</a>
                <?php endif; ?>
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/preview')) ?>">Посмотреть черновик для клиента</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">К периоду</a>
            </p>
            <?php if (!$isSpecialistFlow): ?>
                <p class="mr-workflow-actions__secondary action-row">
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">Блоки отчета</a>
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/assembly-preview')) ?>">Собрать черновик</a>
                    <a class="btn btn-secondary" href="#work-entries">Работы за месяц</a>
                    <?php if ($canEdit): ?>
                        <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/edit')) ?>">Изменить</a>
                    <?php endif; ?>
                </p>
            <?php endif; ?>
        </div>
    <?php else: ?>
        <p class="note mr-summary-hint"><?= $isSpecialistFlow
            ? 'Основной сценарий: работы за месяц и предпросмотр черновика для клиента.'
            : 'Что это за отчет и можно ли его отправлять клиенту — по статусу, PDF и ссылке выше.' ?></p>
        <div class="mr-workflow-actions" aria-label="Основной рабочий сценарий">
            <p class="mr-workflow-actions__primary action-row">
                <?php if ($canCreateWorkEntry): ?>
                    <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/work-entries/create')) ?>">Добавить работу</a>
                <?php endif; ?>
                <?php if (!$parentFinalized && ($isSpecialistFlow || $canEdit)): ?>
                    <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/content-workflow')) ?>">Тексты отчета</a>
                <?php endif; ?>
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/preview')) ?>">Посмотреть черновик для клиента</a>
                <a class="btn btn-secondary" href="#work-entries">Работы за месяц</a>
            </p>
            <?php if (!$isSpecialistFlow): ?>
                <p class="mr-workflow-actions__secondary action-row">
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/assembly-preview')) ?>">Собрать черновик</a>
                    <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Ежедневные заметки</a>
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">Блоки отчета</a>
                    <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">К периоду</a>
                    <?php if ($canEdit): ?>
                        <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/edit')) ?>">Изменить</a>
                    <?php endif; ?>
                    <?php if ($filesHref !== null): ?>
                        <a class="btn btn-secondary" href="<?= e($filesHref) ?>">Файлы отчета</a>
                    <?php endif; ?>
                </p>
            <?php else: ?>
                <p class="mr-workflow-actions__secondary action-row">
                    <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">К периоду</a>
                </p>
            <?php endif; ?>
        </div>
    <?php endif; ?>
</section>

<?php if ($parentFinalized): ?>
    <section class="panel locked-notice">
        <h2>Заблокировано</h2>
        <?php if ($isSpecialistFlow): ?>
            <p>Отчет финализирован. Для SEO-специалиста он открыт только для просмотра.</p>
        <?php else: ?>
            <p>Месячный отчет <strong>финализирован</strong>. Обычное редактирование содержимого и блоков недоступно. Предпросмотр и печать остаются доступны. Администратор может открыть отчет снова для разблокировки.</p>
        <?php endif; ?>
    </section>
<?php endif; ?>

<?php require app_path('Views/partials/monthly-work-entries.php'); ?>

<section class="panel mr-content-summary">
    <div class="panel-head">
        <h2>Содержимое</h2>
    </div>
    <ul class="mr-content-status-list">
        <?php foreach ($contentFields as $fieldKey):
            $raw = (string) ($report[$fieldKey] ?? '');
            $displayField = ui_display_body($raw, $fieldKey, '');
            $isFilled = $displayField !== '';
            ?>
            <li class="mr-content-status-list__item<?= $isFilled ? ' is-filled' : ' is-empty' ?>">
                <span class="mr-content-status-list__title field-label-with-help"><?= e(ui_block_label($fieldKey)) ?><?= field_help(\Iseo\Support\FieldHelp::keyForMonthlyField($fieldKey)) ?></span>
                <span class="mr-content-status-list__state"><?= $isFilled ? 'Заполнено' : 'Пусто' ?></span>
            </li>
        <?php endforeach; ?>
    </ul>
    <details class="tech-details">
        <summary>Тексты разделов (кратко)</summary>
        <ul class="facts">
            <?php foreach ($contentFields as $fieldKey): ?>
                <li><strong><?= e(ui_block_label($fieldKey)) ?>:</strong> <?= e(ui_display_body((string) ($report[$fieldKey] ?? ''), $fieldKey, '—')) ?></li>
            <?php endforeach; ?>
        </ul>
    </details>
</section>

<section class="panel snapshot-card mr-delivery-card">
    <div class="panel-head">
        <h2>Снимок, PDF и ссылка</h2>
    </div>
    <ul class="facts manager-facts mr-delivery-facts">
        <li><strong>Снимок:</strong> <?= !empty($deliveryReadiness['snapshot_exists']) ? 'есть' : 'нет' ?></li>
        <li><strong>PDF:</strong> <?= !empty($deliveryReadiness['pdf_ready']) ? 'готов' : 'ещё не создан' ?></li>
        <li><strong>Активная ссылка:</strong> <?= !empty($deliveryReadiness['active_share']) ? 'есть' : 'ещё не создана' ?></li>
    </ul>
    <p class="note">Экспорт отчета пока отключен. PDF и публичные ссылки будут подключены позже.</p>
    <p class="action-row mr-delivery-actions">
        <?php if ($filesHref !== null && $showAdminControls): ?>
            <a class="btn btn-secondary" href="<?= e($filesHref) ?>">Файлы отчета</a>
        <?php else: ?>
            <button type="button" class="btn btn-secondary" disabled>PDF ещё не создан</button>
        <?php endif; ?>
        <?php if ($sharesHref !== null && $showAdminControls): ?>
            <a class="btn btn-secondary" href="<?= e($sharesHref) ?>">Ссылки для клиента</a>
        <?php else: ?>
            <button type="button" class="btn btn-secondary" disabled>Публичная ссылка ещё не создана</button>
        <?php endif; ?>
        <?php if ($showAdminControls): ?>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/snapshot')) ?>">Открыть страницу снимка</a>
        <?php endif; ?>
    </p>
    <?php if ($showAdminControls): ?>
    <details class="tech-details">
        <summary>Технические детали снимка</summary>
        <?php if (!is_array($activeSnapshot)): ?>
            <p class="note">Снимок ещё не создан.</p>
            <?php if ($canCreateSnapshot): ?>
                <p class="field-hint">Создание снимка доступно в блоке «Административные действия» ниже.</p>
            <?php elseif ($parentFinalized): ?>
                <p class="field-hint">Финализирован — откройте страницу снимка для создания, если ваша роль это позволяет.</p>
            <?php else: ?>
                <p class="field-hint">Перед созданием снимка финализируйте месячный отчет.</p>
            <?php endif; ?>
        <?php else: ?>
            <?php
            $snapChecksum = (string) ($activeSnapshot['checksum_sha256'] ?? '');
            $snapShort = $snapChecksum !== '' ? substr($snapChecksum, 0, 12) . '…' : '—';
            ?>
            <p>
                <span class="immutable-badge">Неизменяемый</span>
                · <span class="status-badge status-<?= e((string) $activeSnapshot['status']) ?>"><?= e(ui_status_label((string) $activeSnapshot['status'])) ?></span>
            </p>
            <ul class="facts">
                <li><strong>Версия:</strong> <?= e((string) $activeSnapshot['version']) ?></li>
                <li><strong>Контрольная сумма:</strong> <code class="checksum-display" title="<?= e($snapChecksum) ?>"><?= e($snapShort) ?></code></li>
                <li><strong>Создан:</strong> <?= e((string) ($activeSnapshot['created_at'] ?? '—')) ?></li>
                <li><strong>ID:</strong> <?= e((string) $activeSnapshot['id']) ?></li>
                <li><strong>Ключ:</strong> <code><?= e((string) $activeSnapshot['snapshot_key']) ?></code></li>
            </ul>
            <p>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . (int) $activeSnapshot['id'])) ?>">Открыть снимок</a>
            </p>
        <?php endif; ?>
    </details>
    <?php endif; ?>
</section>

<?php if ($showAdminControls): ?>
<details class="panel tech-details mr-admin-zone">
    <summary>Административные действия</summary>
    <p class="note">Изменение статуса и создание снимка. Не путать с обычной работой над отчетом.</p>
    <div class="finalization-actions mr-admin-actions">
        <?php
        $actionDefs = [
            'submit_review' => [
                'label' => 'Отправить на проверку',
                'path' => '/monthly-reports/' . $reportId . '/submit-review',
            ],
            'mark_reviewed' => [
                'label' => 'Отметить проверенным',
                'path' => '/monthly-reports/' . $reportId . '/mark-reviewed',
            ],
            'finalize' => [
                'label' => 'Финализировать',
                'path' => '/monthly-reports/' . $reportId . '/finalize',
            ],
            'reopen' => [
                'label' => 'Открыть снова',
                'path' => '/monthly-reports/' . $reportId . '/reopen',
            ],
        ];
        foreach ($actionDefs as $key => $def):
            $meta = is_array($actions[$key] ?? null) ? $actions[$key] : ['allowed' => false, 'reason' => 'Недоступно'];
            $allowed = !empty($meta['allowed']);
            $reason = isset($meta['reason']) && is_string($meta['reason']) ? ui_message($meta['reason']) : null;
            ?>
            <div class="finalization-action">
                <?php if ($allowed): ?>
                    <form method="post" action="<?= e(url_path($def['path'])) ?>">
                        <?= $csrf->field() ?>
                        <button type="submit" class="btn btn-secondary<?= $key === 'finalize' || $key === 'reopen' ? ' mr-admin-action--caution' : '' ?>"><?= e($def['label']) ?></button>
                    </form>
                <?php else: ?>
                    <button type="button" class="btn btn-secondary" disabled><?= e($def['label']) ?></button>
                    <?php if (is_string($reason) && $reason !== ''): ?>
                        <p class="field-hint"><?= e($reason) ?></p>
                    <?php endif; ?>
                <?php endif; ?>
            </div>
        <?php endforeach; ?>

        <?php if (!is_array($activeSnapshot) && $canCreateSnapshot): ?>
            <div class="finalization-action">
                <form method="post" action="<?= e(url_path('/monthly-reports/' . $reportId . '/snapshot')) ?>">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Создать снимок</button>
                </form>
            </div>
        <?php endif; ?>
    </div>
</details>

<details class="panel tech-details mr-diagnostics-zone">
    <summary><?= $isEmptyDraft
        ? e(\Iseo\Support\UiLabels::emptyDraftNotReadyToFinalize())
        : 'Диагностика финализации' ?></summary>
    <?php if ($isEmptyDraft): ?>
        <p class="note empty-draft-diagnostics-note">
            <?= e(\Iseo\Support\UiLabels::emptyDraftNotReadyToFinalize()) ?>
            Сначала добавьте работы и блоки — подробный чек-лист ниже, когда понадобится.
        </p>
    <?php endif; ?>
    <ul class="facts">
        <li><strong>Статус:</strong> <span class="status-badge status-<?= e((string) $report['status']) ?>"><?= e(ui_status_label((string) $report['status'])) ?></span></li>
        <li><strong>Финализирован:</strong> <?= e((string) ($report['finalized_at'] ?? '—')) ?></li>
        <li><strong>Готовность:</strong>
            <?php if (!empty($readiness['ready'])): ?>
                <span class="readiness-pass"><?= e(ui_pass_fail(true)) ?></span>
            <?php else: ?>
                <span class="readiness-fail"><?= e(ui_pass_fail(false)) ?></span>
                <?php if ($failedGates !== [] && !$isEmptyDraft): ?>
                    · <?= e(implode(', ', array_map(static fn ($g) => ui_readiness_label((string) $g), $failedGates))) ?>
                <?php endif; ?>
            <?php endif; ?>
        </li>
    </ul>
    <h3>Чек-лист готовности</h3>
    <?php if ($gates === []): ?>
        <p class="note">Чек-лист готовности недоступен.</p>
    <?php else: ?>
        <ul class="readiness-checklist">
            <?php foreach ($gates as $gateKey => $gate): ?>
                <?php
                $pass = !empty($gate['pass']);
                $detail = ui_message((string) ($gate['detail'] ?? ''));
                ?>
                <li class="<?= $pass ? 'readiness-item--pass' : 'readiness-item--fail' ?>">
                    <span class="readiness-mark"><?= e(ui_pass_fail($pass)) ?></span>
                    <strong><?= e(ui_readiness_label((string) $gateKey)) ?></strong>
                    <?php if ($detail !== ''): ?>
                        — <?= e($detail) ?>
                    <?php endif; ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</details>
<?php endif; ?>

<details class="panel tech-details">
    <summary>Технические детали отчета</summary>
    <h3>Родительский период</h3>
    <ul class="facts">
        <li><strong>Период:</strong>
            <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                <code><?= e((string) ($report['period_key'] ?? '')) ?></code>
            </a>
            · <span class="status-badge status-<?= e((string) ($report['period_status'] ?? '')) ?>"><?= e(ui_status_label((string) ($report['period_status'] ?? ''))) ?></span>
        </li>
        <li><strong>Проект:</strong> <?= e(ui_display_label((string) ($report['project_name'] ?? ''), '—')) ?></li>
        <li><strong>Клиент:</strong> <?= e(ui_display_label((string) ($report['client_name'] ?? ''), '—')) ?></li>
        <li><strong>Даты периода:</strong> <?= e((string) ($report['period_start'] ?? '')) ?> – <?= e((string) ($report['period_end'] ?? '')) ?></li>
    </ul>
    <h3>Детали</h3>
    <ul class="facts">
        <li><strong>Название:</strong> <?= e(ui_display_label((string) ($report['title'] ?? ''), '—')) ?></li>
        <li><strong>Проверен:</strong> <?= e((string) ($report['reviewed_at'] ?? '—')) ?></li>
        <li><strong>Финализирован:</strong> <?= e((string) ($report['finalized_at'] ?? '—')) ?></li>
        <li><strong>Ответственный:</strong> <?= e(ui_display_user_name($report['owner_name'] ?? null, $report['owner_email'] ?? null)) ?></li>
        <li><strong>Проверяющий:</strong> <?= e(ui_display_user_name($report['reviewer_name'] ?? null, $report['reviewer_email'] ?? null)) ?></li>
        <li><strong>Создал:</strong> <?= e(ui_display_user_name($report['created_by_name'] ?? null, null)) ?> · <?= e((string) ($report['created_at'] ?? '')) ?></li>
        <li><strong>Обновил:</strong> <?= e(ui_display_user_name($report['updated_by_name'] ?? null, null)) ?> · <?= e((string) ($report['updated_at'] ?? '')) ?></li>
        <li><strong>ID:</strong> <?= e((string) $report['id']) ?></li>
    </ul>
</details>

<details class="panel tech-details">
    <summary>Исходные заметки</summary>
    <?php if ($sourceCheckpoints === []): ?>
        <p class="note">Связанные еженедельные заметки не указаны.</p>
    <?php else: ?>
        <ul class="facts">
            <?php foreach ($sourceCheckpoints as $wc): ?>
                <li>
                    <a href="<?= e(url_path('/weekly-checkpoints/' . (int) $wc['id'])) ?>">
                        <code><?= e((string) $wc['checkpoint_key']) ?></code>
                    </a>
                    · <span class="status-badge status-<?= e((string) $wc['status']) ?>"><?= e(ui_status_label((string) $wc['status'])) ?></span>
                    · <?= e(ui_display_label((string) ($wc['title'] ?? ''), '—')) ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</details>

<details class="panel tech-details">
    <summary>Блоки отчета</summary>
    <?php if ($isSpecialistFlow): ?>
        <p class="note">Редактирование технических блоков недоступно SEO-специалисту. Содержимое видно в предпросмотре черновика.</p>
    <?php else: ?>
    <p class="action-row">
        <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">Открыть список</a>
        <?php if ($canCreateBlock): ?>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks/create')) ?>">Создать блок</a>
        <?php endif; ?>
    </p>
    <?php if ($reportBlocks === []): ?>
        <p class="note">Блоков отчета пока нет.</p>
    <?php else: ?>
        <div class="table-wrap">
            <table class="data-table">
                <thead>
                <tr>
                    <th>Порядок</th>
                    <th>Раздел</th>
                    <th>Тип</th>
                    <th>Название</th>
                    <th>Статус</th>
                    <th>Действия</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ($reportBlocks as $rb): ?>
                    <?php
                    $bid = (int) $rb['id'];
                    $canEditBlock = !empty($rb['_can_edit']);
                    $blockKey = (string) $rb['block_key'];
                    $sectionLabel = ui_block_label($blockKey);
                    $hasHumanKey = $sectionLabel !== $blockKey;
                    ?>
                    <tr>
                        <td><?= e((string) $rb['sort_order']) ?></td>
                        <td>
                            <?php if ($hasHumanKey): ?>
                                <?= e($sectionLabel) ?>
                                <span class="meta-muted"><code><?= e($blockKey) ?></code></span>
                            <?php else: ?>
                                <?= e(ui_display_label((string) ($rb['title'] ?? ''), '—')) ?>
                                <span class="meta-muted"><code><?= e($blockKey) ?></code></span>
                            <?php endif; ?>
                        </td>
                        <td><span class="type-badge"><?= e(ui_block_label((string) $rb['block_type'])) ?></span></td>
                        <td><?= e(ui_display_label((string) ($rb['title'] ?? ''), '—')) ?></td>
                        <td><span class="status-badge status-<?= e((string) $rb['status']) ?>"><?= e(ui_status_label((string) $rb['status'])) ?></span></td>
                        <td class="actions">
                            <a href="<?= e(url_path('/report-blocks/' . $bid)) ?>">Открыть</a>
                            <?php if ($canEditBlock): ?>
                                · <a href="<?= e(url_path('/report-blocks/' . $bid . '/edit')) ?>">Изменить</a>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    <?php endif; ?>
    <?php endif; ?>
</details>

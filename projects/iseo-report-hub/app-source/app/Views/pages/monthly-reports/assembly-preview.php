<?php
declare(strict_types=1);

/** @var array<string, mixed> $report */
/** @var string $periodKey */
/** @var array<string, int> $stats */
/** @var array<string, array<string, mixed>> $drafts */
/** @var array<string, array<string, mixed>> $manual */
/** @var list<array<string, mixed>> $candidatesKeyFindings */
/** @var list<array<string, mixed>> $excluded */
/** @var array<string, array<string, mixed>> $existingBlocks */
/** @var array<string, array<string, mixed>> $applyBlocks */
/** @var list<string> $warnings */
/** @var bool $parentFinalized */
/** @var bool $parentArchived */
/** @var bool $canApply */
/** @var bool $applyLocked */
/** @var bool $emitApplyForm */
/** @var string $finalizedApplyCopy */
/** @var \Iseo\Services\CsrfService $csrf */

$reportId = (int) ($report['id'] ?? 0);
$periodId = (int) ($report['reporting_period_id'] ?? 0);
$periodKey = $periodKey ?? (string) ($report['period_key'] ?? '');
$stats = $stats ?? [];
$drafts = $drafts ?? [];
$manual = $manual ?? [];
$candidatesKeyFindings = $candidatesKeyFindings ?? [];
$excluded = $excluded ?? [];
$existingBlocks = $existingBlocks ?? [];
$applyBlocks = $applyBlocks ?? [];
$warnings = $warnings ?? [];
$parentFinalized = !empty($parentFinalized);
$parentArchived = !empty($parentArchived);
$canApply = !empty($canApply);
$applyLocked = !empty($applyLocked);
$emitApplyForm = !empty($emitApplyForm);
$finalizedApplyCopy = $finalizedApplyCopy ?? \Iseo\Services\MonthlyReportSummaryAssemblyService::FINALIZED_APPLY_COPY;
$lockedBannerCopy = 'Отчет финализирован. Применение черновика заблокировано. Чтобы применить изменения, нужен отдельный безопасный процесс reopen/update/finalize/export.';

$hasLocalTechnicalMarker = static function (string $text): bool {
    return $text !== '' && (
        stripos($text, 'LOCAL_FIXTURE_ONLY') !== false
        || stripos($text, 'MARS_FIXTURE') !== false
    );
};

$infoNotes = [];
$visibleWarnings = [];
foreach ($warnings as $warning) {
    $warningText = (string) $warning;
    if (str_contains($warningText, 'финализирован')) {
        continue;
    }
    if (str_contains($warningText, 'предварительная сборка')) {
        $infoNotes[] = $warningText;
        continue;
    }
    $visibleWarnings[] = $warningText;
}

$reasonLabels = [
    'internal' => 'internal',
    'cancelled' => 'cancelled',
    'no_matching_rule' => 'no matching rule',
    'empty_title' => 'empty title',
];

$draftOrder = ['work_completed', 'next_month_plan', 'risks_and_blockers'];
$manualOrder = ['executive_summary', 'results_summary', 'key_findings'];
?>
<article class="assembly-preview">
    <section class="panel assembly-preview__header">
        <div class="panel-head">
            <h2>Черновик отчета из работ</h2>
            <p class="assembly-preview__controls">
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId)) ?>">Назад к месячному отчету</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '#work-entries')) ?>">К списку работ</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/preview')) ?>">Предпросмотр отчета</a>
            </p>
        </div>
        <p>
            <span class="status-badge assembly-preview-badge">Предпросмотр</span>
            <span class="status-badge status-<?= e((string) ($report['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($report['status'] ?? ''))) ?></span>
            <?php if ($parentFinalized): ?>
                <span class="finalized-badge">Финализирован</span>
            <?php endif; ?>
            · <code><?= e($periodKey) ?></code>
        </p>
        <ul class="facts">
            <li><strong>Отчет:</strong> <?= e(ui_display_label((string) ($report['title'] ?? ''), '—')) ?></li>
            <li><strong>Клиент:</strong> <?= e(ui_display_label((string) ($report['client_name'] ?? ''), '—')) ?></li>
            <li><strong>Проект:</strong> <?= e(ui_display_label((string) ($report['project_name'] ?? ''), '—')) ?></li>
            <li><strong>Период:</strong>
                <?php if ($periodId > 0): ?>
                    <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>"><code><?= e($periodKey) ?></code></a>
                <?php else: ?>
                    <code><?= e($periodKey) ?></code>
                <?php endif; ?>
            </li>
        </ul>
    </section>

    <?php if ($applyLocked): ?>
        <p class="note assembly-preview-locked" role="status"><?= e($lockedBannerCopy) ?></p>
    <?php endif; ?>

    <?php foreach ($infoNotes as $infoNote): ?>
        <p class="field-hint assembly-preview-info"><?= e($infoNote) ?></p>
    <?php endforeach; ?>

    <?php foreach ($visibleWarnings as $warning): ?>
        <p class="note assembly-preview-warning"><?= e($warning) ?></p>
    <?php endforeach; ?>

    <section class="panel assembly-preview__stats">
        <h2>Сводка по работам</h2>
        <ul class="assembly-stats">
            <li><strong>Всего работ</strong> <span><?= e((string) ($stats['total'] ?? 0)) ?></span></li>
            <li><strong>Включено в черновик</strong> <span><?= e((string) ($stats['included'] ?? 0)) ?></span></li>
            <li><strong>Сделано</strong> <span><?= e((string) ($stats['work_completed'] ?? 0)) ?></span></li>
            <li><strong>План</strong> <span><?= e((string) ($stats['next_month_plan'] ?? 0)) ?></span></li>
            <li><strong>Риски</strong> <span><?= e((string) ($stats['risks_and_blockers'] ?? 0)) ?></span></li>
            <li><strong>Исключено</strong> <span><?= e((string) ($stats['excluded'] ?? 0)) ?></span></li>
        </ul>
    </section>

    <?php if ((int) ($stats['total'] ?? 0) === 0): ?>
        <p class="note">
            <a href="<?= e(url_path('/monthly-reports/' . $reportId . '/work-entries/create')) ?>">Добавить работу</a>
        </p>
    <?php endif; ?>

    <?php foreach ($draftOrder as $key): ?>
        <?php
        $draft = $drafts[$key] ?? null;
        if (!is_array($draft)) {
            continue;
        }
        $groups = is_array($draft['groups'] ?? null) ? $draft['groups'] : [];
        $apply = is_array($applyBlocks[$key] ?? null) ? $applyBlocks[$key] : [];
        $applyBody = is_string($apply['body'] ?? null) ? (string) $apply['body'] : null;
        $currentBody = is_string($apply['current_body'] ?? null) ? (string) $apply['current_body'] : '';
        $currentSummary = is_string($apply['current_summary'] ?? null) ? (string) $apply['current_summary'] : '';
        $blockFound = !empty($apply['block_found']);
        $writable = !empty($apply['writable']);
        $checkboxDisabled = $applyLocked || !$canApply || !$writable;
        $currentHasMarker = $hasLocalTechnicalMarker($currentBody) || $hasLocalTechnicalMarker($currentSummary);
        $currentSummaryVisible = \Iseo\Support\UiTextSanitizer::cleanBodyOrEmpty($currentSummary, $key);
        $currentBodyVisible = \Iseo\Support\UiTextSanitizer::cleanBodyOrEmpty($currentBody, $key);
        $currentNeedsTech = $currentHasMarker
            || (trim($currentSummary) !== '' && $currentSummaryVisible === '')
            || (trim($currentBody) !== '' && $currentBodyVisible === '');
        ?>
        <section class="panel assembly-draft-block assembly-apply-card" data-block-key="<?= e((string) $draft['key']) ?>">
            <div class="panel-head">
                <h2><?= e((string) ($draft['title_ru'] ?? ui_block_label($key))) ?></h2>
                <p><span class="type-badge"><?= e((string) ($draft['count'] ?? 0)) ?></span></p>
            </div>

            <div class="assembly-client-draft">
                <h3 class="field-label-with-help">Будущий текст блока<?= field_help('assembly.future_block_text') ?></h3>
                <?php if ($applyBody !== null): ?>
                    <?php
                    $applyBodyVisible = \Iseo\Support\UiTextSanitizer::cleanBodyOrEmpty($applyBody, $key);
                    ?>
                    <?php if ($applyBodyVisible !== ''): ?>
                        <pre class="assembly-client-draft__body"><?= e($applyBodyVisible) ?></pre>
                    <?php else: ?>
                        <p class="note"><?= e(\Iseo\Support\UiTextSanitizer::fallbackForSection($key)) ?></p>
                    <?php endif; ?>
                <?php else: ?>
                    <p class="note"><?= e((string) ($draft['empty_copy'] ?? 'Нет работ, подходящих для этого раздела.')) ?></p>
                <?php endif; ?>
            </div>

            <details class="assembly-secondary-details">
                <summary>Показать текущий текст отчета</summary>
                <?php if (!$blockFound): ?>
                    <p class="note">Блок в отчете не найден. Автосборка не создаёт новые разделы.</p>
                <?php else: ?>
                    <?php if ($currentSummaryVisible !== ''): ?>
                        <p class="field-hint">Краткое описание блока не меняется.</p>
                        <p><?= e($currentSummaryVisible) ?></p>
                    <?php endif; ?>
                    <?php if ($currentBodyVisible !== ''): ?>
                        <pre class="assembly-current-body"><?= e($currentBodyVisible) ?></pre>
                    <?php elseif ($currentSummaryVisible === ''): ?>
                        <p class="note">пусто</p>
                    <?php endif; ?>
                    <?php if ($currentNeedsTech): ?>
                        <p class="field-hint">Технический локальный маркер скрыт в обычном режиме.</p>
                        <details class="tech-details assembly-technical-current">
                            <summary>Технический текущий текст</summary>
                            <?php if (trim($currentSummary) !== ''): ?>
                                <p><?= e($currentSummary) ?></p>
                            <?php endif; ?>
                            <?php if (trim($currentBody) !== ''): ?>
                                <pre class="assembly-current-body"><?= e($currentBody) ?></pre>
                            <?php endif; ?>
                        </details>
                    <?php endif; ?>
                    <?php if (!empty($apply['overwrite'])): ?>
                        <?php if ($applyLocked): ?>
                            <p class="field-hint">Сравнение справочное: применение заблокировано.</p>
                        <?php else: ?>
                            <p class="field-hint">Будет заменен при применении.</p>
                        <?php endif; ?>
                    <?php endif; ?>
                <?php endif; ?>
            </details>

            <?php if (!$applyLocked && !empty($apply['overwrite'])): ?>
                <p class="assembly-apply-replace-hint">Текущий текст блока будет перезаписан.</p>
            <?php elseif (!$applyLocked && !empty($apply['identical']) && trim($currentBody) !== ''): ?>
                <p class="field-hint">Текст совпадает с черновиком — запись будет пропущена.</p>
            <?php endif; ?>

            <label class="assembly-apply-check<?= $checkboxDisabled ? ' is-disabled' : '' ?>">
                <input
                    type="checkbox"
                    value="<?= e($key) ?>"
                    <?php if ($emitApplyForm && !$checkboxDisabled): ?>
                        name="block_keys[]"
                        form="assembly-apply-form"
                        data-assembly-apply-block
                    <?php else: ?>
                        disabled
                    <?php endif; ?>
                >
                Применить этот блок
            </label>
            <?= field_help('assembly.apply_block') ?>
            <?php if ($checkboxDisabled && $applyLocked): ?>
                <p class="field-hint">Применение недоступно: отчет финализирован.</p>
            <?php elseif ($checkboxDisabled && !$writable && $applyBody === null): ?>
                <p class="field-hint">Пустой черновик этого раздела нельзя записать.</p>
            <?php elseif ($checkboxDisabled && !$blockFound): ?>
                <p class="field-hint">В отчете нет готовой строки этого раздела.</p>
            <?php elseif ($checkboxDisabled && !$canApply): ?>
                <p class="field-hint">Применение доступно руководителю или владельцу.</p>
            <?php endif; ?>

            <?php if (empty($draft['empty'])): ?>
                <details class="tech-details assembly-source-details">
                    <summary>Показать источники работ</summary>
                    <?php foreach ($groups as $group): ?>
                        <div class="assembly-draft-group">
                            <h3 class="assembly-draft-group__title"><?= e((string) ($group['category_name'] ?? 'Без категории')) ?></h3>
                            <ul class="assembly-draft-list">
                                <?php foreach (($group['items'] ?? []) as $item): ?>
                                    <li class="assembly-draft-item">
                                        <p class="assembly-draft-item__text"><?= e(ui_clean_text((string) ($item['text'] ?? ''))) ?></p>
                                        <ul class="facts assembly-source-meta">
                                            <li><strong>ID работы:</strong> <?= e((string) ($item['id'] ?? '')) ?></li>
                                            <li><strong>Название:</strong> <?= e(ui_display_label((string) ($item['title'] ?? ''), '—')) ?></li>
                                            <?php if (trim((string) ($item['category_name'] ?? '')) !== ''): ?>
                                                <li><strong>Категория:</strong> <?= e(ui_display_label((string) $item['category_name'], '—')) ?></li>
                                            <?php endif; ?>
                                        </ul>
                                    </li>
                                <?php endforeach; ?>
                            </ul>
                        </div>
                    <?php endforeach; ?>
                </details>
            <?php endif; ?>
        </section>
    <?php endforeach; ?>

    <?php foreach ($manualOrder as $key): ?>
        <?php
        $block = $manual[$key] ?? null;
        if (!is_array($block)) {
            continue;
        }
        $stored = $existingBlocks[$key] ?? null;
        $storedSummary = is_array($stored) ? trim((string) ($stored['summary'] ?? '')) : '';
        $storedBody = is_array($stored) ? trim((string) ($stored['body'] ?? '')) : '';
        $storedHasMarker = $hasLocalTechnicalMarker($storedBody) || $hasLocalTechnicalMarker($storedSummary);
        $storedSummaryVisible = \Iseo\Support\UiTextSanitizer::cleanBodyOrEmpty($storedSummary, $key);
        $storedBodyVisible = \Iseo\Support\UiTextSanitizer::cleanBodyOrEmpty($storedBody, $key);
        $storedNeedsTech = $storedHasMarker
            || ($storedSummary !== '' && $storedSummaryVisible === '')
            || ($storedBody !== '' && $storedBodyVisible === '');
        ?>
        <section class="panel assembly-manual-block" data-block-key="<?= e($key) ?>">
            <div class="panel-head">
                <h2><?= e((string) ($block['title_ru'] ?? ui_block_label($key))) ?></h2>
                <p><span class="type-badge">Вручную</span></p>
            </div>
            <p class="note"><?= e((string) ($block['copy'] ?? 'Требуется ручная редактура.')) ?></p>
            <p class="field-hint">Этот раздел нельзя заполнить автосборкой. Правка только вручную в редакторе блока.</p>
            <?php if ($key === 'key_findings' && $candidatesKeyFindings !== []): ?>
                <div class="assembly-candidates">
                    <h3>Кандидаты в выводы</h3>
                    <p class="field-hint">Это не финальный текст раздела.</p>
                    <ul class="assembly-draft-list">
                        <?php foreach ($candidatesKeyFindings as $item): ?>
                            <li class="assembly-draft-item">
                                <p class="assembly-draft-item__text"><?= e(ui_clean_text((string) ($item['text'] ?? ''))) ?></p>
                                <details class="tech-details assembly-source-details">
                                    <summary>Показать источники работ</summary>
                                    <ul class="facts assembly-source-meta">
                                        <li><strong>ID работы:</strong> <?= e((string) ($item['id'] ?? '')) ?></li>
                                        <li><strong>Название:</strong> <?= e(ui_display_label((string) ($item['title'] ?? ''), '—')) ?></li>
                                        <?php if (trim((string) ($item['category_name'] ?? '')) !== ''): ?>
                                            <li><strong>Категория:</strong> <?= e(ui_display_label((string) $item['category_name'], '—')) ?></li>
                                        <?php endif; ?>
                                    </ul>
                                </details>
                            </li>
                        <?php endforeach; ?>
                    </ul>
                </div>
            <?php endif; ?>
            <?php if (is_array($stored) && ($storedSummary !== '' || $storedBody !== '')): ?>
                <details class="assembly-secondary-details">
                    <summary>Показать текущий текст отчета</summary>
                    <?php if ($storedSummaryVisible !== ''): ?>
                        <p><?= e($storedSummaryVisible) ?></p>
                    <?php endif; ?>
                    <?php if ($storedBodyVisible !== ''): ?>
                        <p><?= nl2br(e($storedBodyVisible), false) ?></p>
                    <?php elseif ($storedSummaryVisible === ''): ?>
                        <p class="note">пусто</p>
                    <?php endif; ?>
                    <?php if ($storedNeedsTech): ?>
                        <p class="field-hint">Технический локальный маркер скрыт в обычном режиме.</p>
                        <details class="tech-details assembly-technical-current">
                            <summary>Технический текущий текст</summary>
                            <?php if ($storedSummary !== ''): ?>
                                <p><?= e($storedSummary) ?></p>
                            <?php endif; ?>
                            <?php if ($storedBody !== ''): ?>
                                <p><?= nl2br(e($storedBody), false) ?></p>
                            <?php endif; ?>
                        </details>
                    <?php endif; ?>
                </details>
            <?php endif; ?>
        </section>
    <?php endforeach; ?>

    <?php if ($excluded !== []): ?>
        <section class="panel">
            <details class="tech-details assembly-excluded">
                <summary>Не вошли в клиентский черновик (<?= e((string) count($excluded)) ?>)</summary>
                <ul class="assembly-excluded-list">
                    <?php foreach ($excluded as $row): ?>
                        <li>
                            <?= e((string) ($row['title'] ?? '—')) ?>
                            · <code><?= e($reasonLabels[(string) ($row['reason'] ?? '')] ?? (string) ($row['reason'] ?? '')) ?></code>
                        </li>
                    <?php endforeach; ?>
                </ul>
            </details>
        </section>
    <?php endif; ?>

    <section class="panel assembly-apply-panel<?= $applyLocked ? ' is-locked' : '' ?>">
        <h2>Применение черновика</h2>
        <?php if ($applyLocked): ?>
            <p class="note"><?= e('Применение заблокировано, потому что отчет финализирован.') ?></p>
            <label class="assembly-apply-check is-disabled">
                <input type="checkbox" disabled>
                Подтверждаю перезапись выбранных блоков черновиком.
            </label>
            <p class="assembly-preview__footer-actions">
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId)) ?>">Назад к месячному отчету</a>
                <button type="button" class="btn btn-secondary" disabled>Применить выбранные блоки</button>
            </p>
        <?php elseif (!$canApply): ?>
            <p class="note">Предпросмотр доступен. Применение черновика доступно руководителю или владельцу.</p>
            <p class="assembly-preview__footer-actions">
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId)) ?>">Назад к месячному отчету</a>
            </p>
        <?php else: ?>
            <form
                id="assembly-apply-form"
                class="assembly-apply-form"
                method="post"
                action="<?= e(url_path('/monthly-reports/' . $reportId . '/assembly-apply')) ?>"
                data-assembly-apply-form
            >
                <?= $csrf->field() ?>
                <label class="assembly-apply-check">
                    <input type="checkbox" name="confirm_overwrite" value="1" required data-assembly-apply-confirm>
                    Подтверждаю перезапись выбранных блоков черновиком.
                </label>
                <p class="field-hint">PDF, снимки и публичные ссылки этим действием не обновляются.</p>
                <p class="assembly-preview__footer-actions">
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId)) ?>">Назад к месячному отчету</a>
                    <button type="submit" class="btn btn-primary" data-assembly-apply-submit disabled>Применить выбранные блоки</button>
                </p>
            </form>
        <?php endif; ?>
    </section>
</article>

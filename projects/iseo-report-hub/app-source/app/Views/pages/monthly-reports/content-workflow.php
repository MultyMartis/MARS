<?php
declare(strict_types=1);

/** @var array<string, mixed> $report */
/** @var string $periodKey */
/** @var bool $editable */
/** @var string|null $readOnlyReason */
/** @var list<array<string, mixed>> $sections */
/** @var bool $isSpecialistFlow */
/** @var \Iseo\Services\CsrfService $csrf */

$reportId = (int) ($report['id'] ?? 0);
$periodId = (int) ($report['reporting_period_id'] ?? 0);
$periodKey = $periodKey ?? (string) ($report['period_key'] ?? '');
$editable = !empty($editable);
$readOnlyReason = is_string($readOnlyReason ?? null) ? $readOnlyReason : null;
$sections = $sections ?? [];
$isSpecialistFlow = !empty($isSpecialistFlow);

$title = (string) ($report['title'] ?? 'Месячный отчет');
$status = (string) ($report['status'] ?? '');
$clientName = ui_display_label((string) ($report['client_name'] ?? ''), '—');
$projectName = ui_display_label((string) ($report['project_name'] ?? ''), '—');
$siteLabel = trim((string) ($report['site_hostname'] ?? $report['site_name'] ?? ''));
$statusLabel = \Iseo\Support\UiLabels::status($status);
?>
<article class="content-workflow" data-content-workflow>
    <nav class="breadcrumb" aria-label="Навигация">
        <a href="<?= e(url_path('/reporting-periods')) ?>">Периоды</a>
        <span aria-hidden="true">/</span>
        <a href="<?= e(url_path('/monthly-reports/' . $reportId)) ?>"><?= e($title) ?></a>
        <span aria-hidden="true">/</span>
        <span>Тексты отчета</span>
    </nav>

    <section class="panel content-workflow__header">
        <div class="panel-head">
            <h1>Тексты отчета</h1>
            <p class="content-workflow__controls action-row">
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId)) ?>">Вернуться к отчету</a>
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/preview')) ?>">Посмотреть черновик для клиента</a>
            </p>
        </div>
        <p class="note">Здесь можно подготовить клиентские тексты отчета без технических полей.</p>
        <ul class="meta-list">
            <li><strong>Отчет:</strong> <?= e($title) ?></li>
            <li><strong>Период:</strong> <?= e($periodKey !== '' ? $periodKey : '—') ?></li>
            <li><strong>Клиент:</strong> <?= e($clientName) ?></li>
            <li><strong>Проект:</strong> <?= e($projectName) ?></li>
            <?php if ($siteLabel !== ''): ?>
                <li><strong>Сайт:</strong> <?= e($siteLabel) ?></li>
            <?php endif; ?>
            <li><strong>Статус:</strong> <?= e($statusLabel) ?></li>
        </ul>
        <?php if (!$editable && $readOnlyReason !== null && $readOnlyReason !== ''): ?>
            <p class="locked-notice content-workflow__lock" role="status"><?= e($readOnlyReason) ?></p>
        <?php endif; ?>
    </section>

    <?php foreach ($sections as $section):
        $key = (string) ($section['key'] ?? '');
        if ($key === '') {
            continue;
        }
        $label = (string) ($section['label'] ?? $key);
        $helper = (string) ($section['helper'] ?? '');
        $text = (string) ($section['text'] ?? '');
        $missing = !empty($section['missing_block']);
        $hintAvailable = !empty($section['hint_available']);
        $hintText = (string) ($section['hint_text'] ?? '');
        $fieldId = 'section-text-' . $key;
        $hintId = 'section-hint-' . $key;
        ?>
        <section class="panel content-workflow__section" id="section-<?= e($key) ?>" data-section-key="<?= e($key) ?>">
            <div class="panel-head">
                <h2><?= e($label) ?></h2>
            </div>
            <?php if ($helper !== ''): ?>
                <p class="note content-workflow__helper"><?= e($helper) ?></p>
            <?php endif; ?>

            <?php if ($missing): ?>
                <p class="warn-note" role="status">Раздел пока не найден в структуре отчета.</p>
            <?php endif; ?>

            <?php if ($hintAvailable): ?>
                <details class="content-workflow__hint">
                    <summary>Черновик из работ за месяц</summary>
                    <pre class="content-workflow__hint-text" id="<?= e($hintId) ?>"><?= e($hintText) ?></pre>
                    <?php if ($editable && !$missing): ?>
                        <p class="action-row">
                            <button type="button" class="btn btn-secondary" data-fill-hint="<?= e($fieldId) ?>" data-hint-source="<?= e($hintId) ?>">Подставить в поле</button>
                        </p>
                    <?php endif; ?>
                </details>
            <?php endif; ?>

            <?php if ($editable && !$missing): ?>
                <form method="post" action="<?= e(url_path('/monthly-reports/' . $reportId . '/content-workflow/sections/' . rawurlencode($key))) ?>" class="content-workflow__form">
                    <?= $csrf->field() ?>
                    <label class="sr-only" for="<?= e($fieldId) ?>">Текст раздела «<?= e($label) ?>»</label>
                    <textarea
                        id="<?= e($fieldId) ?>"
                        name="section_text"
                        class="content-workflow__textarea"
                        rows="8"
                        maxlength="20000"
                    ><?= e($text) ?></textarea>
                    <p class="action-row">
                        <button type="submit" class="btn btn-primary">Сохранить раздел</button>
                    </p>
                </form>
            <?php else: ?>
                <?php if ($text !== ''): ?>
                    <div class="content-workflow__readonly">
                        <pre class="content-workflow__readonly-text"><?= e($text) ?></pre>
                    </div>
                <?php elseif (!$missing): ?>
                    <p class="note">Текст раздела пока пуст.</p>
                <?php endif; ?>
            <?php endif; ?>
        </section>
    <?php endforeach; ?>
</article>

<script>
(function () {
    var root = document.querySelector('[data-content-workflow]');
    if (!root) {
        return;
    }
    root.addEventListener('click', function (event) {
        var btn = event.target.closest('[data-fill-hint]');
        if (!btn || !root.contains(btn)) {
            return;
        }
        var fieldId = btn.getAttribute('data-fill-hint');
        var hintId = btn.getAttribute('data-hint-source');
        if (!fieldId || !hintId) {
            return;
        }
        var field = document.getElementById(fieldId);
        var hint = document.getElementById(hintId);
        if (!field || !hint) {
            return;
        }
        field.value = hint.textContent || '';
        field.focus();
    });
})();
</script>

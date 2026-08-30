<?php
declare(strict_types=1);

/** @var array<string, mixed> $document */
/** @var int $monthlyReportId */
/** @var bool $printMode */

$document = $document ?? [];
$monthlyReportId = (int) ($monthlyReportId ?? 0);
$printMode = !empty($printMode);
?>
<div class="client-report-shell">
    <nav class="client-report-operator no-print" aria-label="Служебная навигация">
        <?php if ($monthlyReportId > 0): ?>
            <a class="client-report-operator__back" href="<?= e(url_path('/monthly-reports/' . $monthlyReportId)) ?>">Вернуться к месячному отчету</a>
        <?php endif; ?>
        <?php if ($printMode): ?>
            <button class="client-report-operator__print" type="button" onclick="window.print(); return false;">Печать</button>
        <?php endif; ?>
    </nav>
    <?php require app_path('Views/partials/client-report/document.php'); ?>
</div>

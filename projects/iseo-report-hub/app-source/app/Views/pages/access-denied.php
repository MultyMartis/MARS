<?php
declare(strict_types=1);
/** @var string $message */
/** @var bool $showPeriodsLink */
/** @var string|null $backHref */
/** @var string|null $backLabel */

$showPeriodsLink = $showPeriodsLink ?? true;
$backHref = $backHref ?? null;
$backLabel = $backLabel ?? null;
?>
<section class="panel access-denied" aria-labelledby="access-denied-title">
    <p class="access-denied__eyebrow">Ограничение доступа</p>
    <h1 id="access-denied-title" class="access-denied__title">Доступ ограничен</h1>
    <p class="access-denied__message"><?= e((string) $message) ?></p>
    <div class="form-actions access-denied__actions">
        <a class="btn btn-primary" href="<?= e(url_path('/')) ?>">На главную</a>
        <?php if ($showPeriodsLink): ?>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods')) ?>">К отчетным периодам</a>
        <?php endif; ?>
        <?php if (is_string($backHref) && $backHref !== '' && is_string($backLabel) && $backLabel !== ''): ?>
            <a class="btn btn-secondary" href="<?= e($backHref) ?>"><?= e($backLabel) ?></a>
        <?php endif; ?>
    </div>
</section>

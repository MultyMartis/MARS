<?php
declare(strict_types=1);

/** @var array<string, mixed> $snapshot */
/** @var list<array<string, mixed>> $exports */
/** @var bool $canCreate */
/** @var bool $canCreatePdf */
/** @var bool $hasHtmlExport */
/** @var bool $hasPdfExport */
/** @var bool $canCreateStyledHtml */
/** @var bool $canCreateStyledPdf */
/** @var array<string, mixed>|null $styledHtmlExport */
/** @var array<string, mixed>|null $styledPdfExport */
/** @var string $message */
/** @var \Iseo\Services\CsrfService $csrf */

$snapshot = $snapshot ?? [];
$exports = $exports ?? [];
$canCreate = !empty($canCreate);
$canCreatePdf = !empty($canCreatePdf);
$hasHtmlExport = !empty($hasHtmlExport);
$hasPdfExport = !empty($hasPdfExport);
$canCreateStyledHtml = !empty($canCreateStyledHtml);
$canCreateStyledPdf = !empty($canCreateStyledPdf);
$styledHtmlExport = is_array($styledHtmlExport ?? null) ? $styledHtmlExport : null;
$styledPdfExport = is_array($styledPdfExport ?? null) ? $styledPdfExport : null;
$message = (string) ($message ?? '');
/** @var array{id?:string,version?:int,display_label?:string}|null $futureTemplate */
$futureTemplate = is_array($futureTemplate ?? null) ? $futureTemplate : [];
$legacyTemplateLabel = (string) ($legacyTemplateLabel ?? 'устаревший / не записан');
$futureTemplateId = (string) ($futureTemplate['id'] ?? 'iseo_default_v1');
$futureTemplateVersion = (string) (int) ($futureTemplate['version'] ?? 1);
$styledTemplateLabel = $futureTemplateId . ' v' . $futureTemplateVersion;

$snapshotId = (int) ($snapshot['id'] ?? 0);
$monthlyId = (int) ($snapshot['monthly_report_content_id'] ?? 0);
$snapshotKey = (string) ($snapshot['snapshot_key'] ?? '');

$statusRu = static function (string $status): string {
    return match ($status) {
        'ready' => 'Готово',
        'pending' => 'В работе',
        'failed' => 'Ошибка',
        'revoked' => 'Отозвана',
        'expired' => 'Истекла',
        default => $status,
    };
};

$rowTemplateLabel = static function (array $row) use ($legacyTemplateLabel): string {
    if (isset($row['display_template_label']) && is_string($row['display_template_label']) && $row['display_template_label'] !== '') {
        return $row['display_template_label'];
    }
    $templateId = trim((string) ($row['template_id'] ?? ''));
    $templateVersion = trim((string) ($row['template_version'] ?? ''));
    if ($templateId !== '' && $templateVersion !== '') {
        return $templateId . ' v' . $templateVersion;
    }
    return $legacyTemplateLabel;
};

$primaryExport = null;
$primaryId = is_array($styledPdfExport) ? (int) ($styledPdfExport['id'] ?? 0) : 0;
if ($primaryId > 0) {
    foreach ($exports as $row) {
        if (is_array($row) && (int) ($row['id'] ?? 0) === $primaryId) {
            $primaryExport = $row;
            break;
        }
    }
    if ($primaryExport === null) {
        $primaryExport = $styledPdfExport;
    }
}
$primaryShareable = is_array($primaryExport) && !empty($primaryExport['share_eligible']);
$primaryStatus = is_array($primaryExport) ? (string) ($primaryExport['status'] ?? '') : '';
?>
<section class="card panel export-card mb-24">
    <div class="panel-head">
        <h2>Файлы отчета</h2>
        <p>
            <?php if ($snapshotId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId)) ?>">Снимок отчета</a>
            <?php endif; ?>
            <?php if ($monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Месячный отчет</a>
            <?php endif; ?>
        </p>
    </div>

    <p class="note">Здесь лежат файлы для скачивания и отправки клиенту. Основной файл для клиента — PDF.</p>
    <p>
        <span class="internal-only-badge">Только внутри</span>
        <span class="artifact-badge artifact-badge--pdf">PDF-файл</span>
        <span class="artifact-badge">HTML-файл</span>
    </p>

    <?php if (is_array($primaryExport) && $primaryId > 0): ?>
        <article class="card panel primary-file-card">
            <h3>PDF для клиента</h3>
            <p>
                <span class="status-badge status-<?= e($primaryStatus) ?>"><?= e($statusRu($primaryStatus)) ?></span>
                <?php if ($primaryShareable): ?>
                    <span class="share-badge share-badge--eligible">Можно отправлять</span>
                <?php else: ?>
                    <span class="share-badge share-badge--blocked">Нельзя отправлять</span>
                <?php endif; ?>
            </p>
            <p class="note">Рекомендуемый файл для передачи клиенту.</p>
            <p>
                <a class="btn btn-primary" href="<?= e(url_path('/report-exports/' . $primaryId . '/download')) ?>">Скачать PDF</a>
                <a class="btn btn-primary" href="<?= e(url_path('/report-exports/' . $primaryId)) ?>">Открыть файл</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-exports/' . $primaryId . '/shares')) ?>">Ссылки для клиента</a>
            </p>
        </article>
    <?php endif; ?>

    <?php if ($exports === []): ?>
        <p class="note">Файлов для этого снимка пока нет.</p>
        <?php if ($canCreate && $snapshotId > 0): ?>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html')) ?>">
                <?= $csrf->field() ?>
                <button type="submit" class="btn btn-primary">Создать HTML-файл</button>
            </form>
        <?php elseif ($snapshotId > 0): ?>
            <p class="field-hint">Создание файлов доступно ролям admin_owner или seo_lead_reviewer.</p>
        <?php endif; ?>
    <?php else: ?>
        <h3 class="handoff-subhead section-title">Все файлы</h3>
        <p class="note">Ниже полный список. Старые HTML/PDF без шаблона — архив / технический файл.</p>
        <div class="table-wrap">
            <table class="data-table table export-table">
                <thead>
                <tr>
                    <th>Файл</th>
                    <th>Формат</th>
                    <th>Статус</th>
                    <th>Для клиента</th>
                    <th>Имя файла</th>
                    <th>Создан</th>
                    <th>Действия</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ($exports as $row): ?>
                    <?php
                    if (!is_array($row)) {
                        continue;
                    }
                    $eid = (int) ($row['id'] ?? 0);
                    $format = (string) ($row['format'] ?? '');
                    $tplLabel = $rowTemplateLabel($row);
                    $isLegacyRow = !empty($row['is_legacy_template_metadata'])
                        || $tplLabel === $legacyTemplateLabel;
                    $shareEligible = !empty($row['share_eligible']);
                    $activeShares = (int) ($row['active_share_count'] ?? 0);
                    $rowStatus = (string) ($row['status'] ?? '');
                    $isPrimary = $eid === $primaryId;
                    ?>
                    <tr class="<?= $isPrimary ? 'row-primary' : ($isLegacyRow ? 'row-archive' : '') ?>">
                        <td>
                            <?php if ($isPrimary): ?>
                                <strong>PDF для клиента</strong>
                            <?php elseif ($isLegacyRow): ?>
                                Архив / технический файл
                            <?php else: ?>
                                Файл #<?= e((string) $eid) ?>
                            <?php endif; ?>
                        </td>
                        <td>
                            <span class="type-badge<?= $format === 'pdf' ? ' type-badge--pdf' : '' ?>"><?= e(strtoupper($format)) ?></span>
                        </td>
                        <td><span class="status-badge status-<?= e($rowStatus) ?>"><?= e($statusRu($rowStatus)) ?></span></td>
                        <td>
                            <?php if ($shareEligible): ?>
                                <span class="share-badge share-badge--eligible">Можно отправлять</span>
                                <?php if ($activeShares > 0): ?>
                                    <br><span class="meta-muted">Активных ссылок: <?= e((string) $activeShares) ?></span>
                                <?php endif; ?>
                            <?php else: ?>
                                <span class="share-badge share-badge--blocked">Нельзя отправлять</span>
                            <?php endif; ?>
                        </td>
                        <td><code><?= e((string) ($row['filename'] ?? '')) ?></code></td>
                        <td><?= e((string) ($row['created_at'] ?? '—')) ?></td>
                        <td class="actions">
                            <a href="<?= e(url_path('/report-exports/' . $eid)) ?>">Открыть</a>
                            · <a class="btn-download" href="<?= e(url_path('/report-exports/' . $eid . '/download')) ?>">Скачать</a>
                            · <a href="<?= e(url_path('/report-exports/' . $eid . '/shares')) ?>">Ссылки</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>

        <details class="tech-details technical-details">
            <summary>Технические детали</summary>
            <p class="template-state-note">
                <strong>Ключ снимка:</strong> <code><?= e($snapshotKey) ?></code>
                <br>
                <strong>Шаблон по умолчанию:</strong>
                <code><?= e($futureTemplateId) ?></code> v<?= e($futureTemplateVersion) ?>
                (новые версии; старые файлы не перезаписываются).
                <br>
                <strong>Устаревший / NULL:</strong> <?= e($legacyTemplateLabel) ?>.
            </p>

            <?php if ($canCreate && $snapshotId > 0): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Проверить HTML-файл (без дубля)</button>
                </form>
            <?php endif; ?>

            <?php if ($canCreatePdf && $snapshotId > 0 && $hasHtmlExport && !$hasPdfExport): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-primary">Создать PDF</button>
                </form>
            <?php elseif ($canCreatePdf && $snapshotId > 0 && $hasPdfExport): ?>
                <p class="export-ready-note">Старый PDF уже готов. Используйте скачивание или проверку ниже.</p>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Проверить PDF (без дубля)</button>
                </form>
            <?php elseif ($hasHtmlExport && !$hasPdfExport && $snapshotId > 0 && !$canCreatePdf): ?>
                <p class="field-hint">Создание PDF доступно ролям admin_owner или seo_lead_reviewer.</p>
            <?php endif; ?>

            <?php if ($canCreateStyledHtml && $snapshotId > 0): ?>
                <?php if ($styledHtmlExport === null): ?>
                    <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                        <?= $csrf->field() ?>
                        <button type="submit" class="btn btn-primary">Создать оформленный HTML (<?= e($styledTemplateLabel) ?>)</button>
                    </form>
                <?php else: ?>
                    <p class="export-ready-note">Оформленный HTML готов.</p>
                    <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                        <?= $csrf->field() ?>
                        <button type="submit" class="btn btn-secondary">Проверить оформленный HTML</button>
                    </form>
                <?php endif; ?>
            <?php endif; ?>

            <?php if ($canCreateStyledPdf && $snapshotId > 0): ?>
                <?php if ($styledPdfExport === null): ?>
                    <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                        <?= $csrf->field() ?>
                        <button type="submit" class="btn btn-primary">Создать оформленный PDF</button>
                    </form>
                <?php else: ?>
                    <p class="export-ready-note">Оформленный PDF готов.</p>
                    <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                        <?= $csrf->field() ?>
                        <button type="submit" class="btn btn-secondary">Проверить оформленный PDF</button>
                    </form>
                <?php endif; ?>
            <?php elseif ($styledHtmlExport !== null && $styledPdfExport === null && $snapshotId > 0 && !$canCreateStyledPdf): ?>
                <p class="field-hint">Создание оформленного PDF требует роли и локального PDF-движка.</p>
            <?php endif; ?>

            <p class="field-hint export-hint">Скачивание требует входа. Ссылку клиенту можно создать только для готового оформленного PDF.</p>
        </details>
    <?php endif; ?>
</section>

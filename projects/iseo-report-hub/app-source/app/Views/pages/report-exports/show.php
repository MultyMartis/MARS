<?php
declare(strict_types=1);

/** @var array<string, mixed> $export */
/** @var string $message */
/** @var string $templateLabel */
/** @var string $renderTargetLabel */
/** @var string $renderEngineLabel */
/** @var array{id?:int,export_key?:string,label?:string}|null $sourceHtmlSummary */
/** @var bool $isStyledExport */
/** @var bool $isLegacyTemplateMetadata */
/** @var array{eligible?:bool,reason?:string,code?:string}|null $shareEligibility */
/** @var int $activeShareCount */
/** @var bool $canManageShares */
/** @var \Iseo\Services\ReportExportShareService|null $reportExportShareService */

$export = $export ?? [];
$message = (string) ($message ?? '');

$exportId = (int) ($export['id'] ?? 0);
$snapshotId = (int) ($export['report_snapshot_id'] ?? 0);
$monthlyId = (int) ($export['monthly_report_content_id'] ?? 0);
$format = (string) ($export['format'] ?? '');
$isPdf = $format === 'pdf';
$checksum = (string) ($export['checksum_sha256'] ?? '');
$checksumShort = $checksum !== '' ? substr($checksum, 0, 12) . '…' : '—';
$sourceChecksum = (string) ($export['source_snapshot_checksum_sha256'] ?? '');
$sourceShort = $sourceChecksum !== '' ? substr($sourceChecksum, 0, 12) . '…' : '—';
$fileSize = isset($export['file_size_bytes']) ? (int) $export['file_size_bytes'] : 0;
$downloadLabel = $isPdf ? 'Скачать PDF' : 'Скачать HTML';
$artifactLabel = $isPdf ? 'PDF-файл' : 'HTML-файл';
/** @var array{id?:string,version?:int}|null $futureTemplate */
$futureTemplate = is_array($futureTemplate ?? null) ? $futureTemplate : [];
$legacyTemplateLabel = (string) ($legacyTemplateLabel ?? 'устаревший / не записан');
$futureTemplateId = (string) ($futureTemplate['id'] ?? 'iseo_default_v1');
$futureTemplateVersion = (string) (int) ($futureTemplate['version'] ?? 1);
$isLegacyTemplateMetadata = !empty($isLegacyTemplateMetadata);
$isStyledExport = !empty($isStyledExport);
$templateLabel = (string) ($templateLabel ?? ($export['display_template_label'] ?? $legacyTemplateLabel));
$renderTargetLabel = (string) ($renderTargetLabel ?? ($export['display_render_target_label'] ?? 'не записан'));
$renderEngineLabel = (string) ($renderEngineLabel ?? ($export['display_render_engine_label'] ?? 'не записан'));
$sourceHtmlSummary = is_array($sourceHtmlSummary ?? null) ? $sourceHtmlSummary : null;
$sourceHtmlLabel = is_array($sourceHtmlSummary) && isset($sourceHtmlSummary['label'])
    ? (string) $sourceHtmlSummary['label']
    : (string) ($export['display_source_html_label'] ?? 'не записан');
$shareEligibility = is_array($shareEligibility ?? null) ? $shareEligibility : [];
$shareEligible = !empty($shareEligibility['eligible']);
$shareReason = (string) ($shareEligibility['reason'] ?? 'Готовность не оценена.');
$activeShareCount = (int) ($activeShareCount ?? 0);
$canManageShares = !empty($canManageShares);

$statusRu = static function (string $status): string {
    return match ($status) {
        'ready' => 'Готово',
        'pending' => 'В работе',
        'failed' => 'Ошибка',
        'revoked' => 'Отозвана',
        'expired' => 'Истекла',
        'finalized' => 'Финализирован',
        default => $status,
    };
};

$handoff = null;
if (isset($reportExportShareService) && $reportExportShareService instanceof \Iseo\Services\ReportExportShareService) {
    $handoff = $reportExportShareService->buildHandoffState($export, null, null, null);
}
$handoff = is_array($handoff) ? $handoff : null;
$hCtx = is_array($handoff['context'] ?? null) ? $handoff['context'] : [];
$hShare = is_array($handoff['share_status'] ?? null) ? $handoff['share_status'] : [];
$hChecks = is_array($handoff['checklist'] ?? null) ? $handoff['checklist'] : [];
$hWarnings = is_array($handoff['warnings'] ?? null) ? $handoff['warnings'] : [];
$urlLost = is_string($handoff['url_lost_guidance'] ?? null) ? (string) $handoff['url_lost_guidance'] : '';
$storagePath = (string) ($export['storage_path'] ?? '');
$exportStatus = (string) ($export['status'] ?? '');
?>
<section class="panel export-card export-detail">
    <div class="panel-head">
        <h2>Файл отчета</h2>
        <p>
            <?php if ($exportId > 0 && $exportStatus === 'ready'): ?>
                <a class="btn" href="<?= e(url_path('/report-exports/' . $exportId . '/download')) ?>"><?= e($downloadLabel) ?></a>
            <?php endif; ?>
            <?php if ($exportId > 0): ?>
                <a class="btn" href="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>">Ссылки для клиента</a>
            <?php endif; ?>
            <?php if ($snapshotId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">Все файлы отчета</a>
            <?php endif; ?>
            <?php if ($monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Месячный отчет</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Только внутри</span>
        <span class="artifact-badge<?= $isPdf ? ' artifact-badge--pdf' : '' ?>"><?= e($artifactLabel) ?></span>
        <?php if ($isLegacyTemplateMetadata): ?>
            <span class="template-badge template-badge--legacy">Старый файл</span>
        <?php else: ?>
            <span class="template-badge template-badge--styled">Шаблон сохранен</span>
        <?php endif; ?>
        <?php if ($shareEligible): ?>
            <span class="share-badge share-badge--eligible">Можно отправлять</span>
        <?php else: ?>
            <span class="share-badge share-badge--blocked" title="<?= e($shareReason) ?>">Нельзя отправлять</span>
        <?php endif; ?>
        · <span class="status-badge status-<?= e($exportStatus) ?>"><?= e($statusRu($exportStatus)) ?></span>
    </p>
</section>

<section class="panel export-card handoff-panel" data-handoff-panel>
    <div class="panel-head">
        <h2>Готовность к отправке клиенту</h2>
        <p>
            <a class="btn" href="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>">Открыть ссылки и тексты</a>
        </p>
    </div>

    <ul class="facts handoff-context-list manager-facts">
        <li><strong>Клиент:</strong> <?= e((string) ($hCtx['client_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Проект:</strong> <?= e((string) ($hCtx['project_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Период:</strong> <?= e((string) ($hCtx['period'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>PDF:</strong>
            <?php if ($isPdf && $exportStatus === 'ready'): ?>
                готов
            <?php else: ?>
                не готов
            <?php endif; ?>
        </li>
        <li><strong>Отправка:</strong>
            <?php if ($shareEligible): ?>
                Можно отправлять
            <?php else: ?>
                Нельзя отправлять
            <?php endif; ?>
        </li>
        <li><strong>Ссылка:</strong>
            <?php if (!empty($hShare['has_active'])): ?>
                Есть активная ссылка
            <?php else: ?>
                Активной ссылки нет
            <?php endif; ?>
        </li>
    </ul>

    <?php if ($shareEligible): ?>
        <p>
            <span class="share-badge share-badge--eligible">Можно отправлять</span>
            · Активные ссылки: <strong><?= e((string) ($hShare['active_count'] ?? $activeShareCount)) ?></strong>
            <?php if (!empty($hShare['expires_at'])): ?>
                · Действует до: <code><?= e((string) $hShare['expires_at']) ?></code>
            <?php endif; ?>
            <?php if ((int) ($hShare['revoked_count'] ?? 0) > 0): ?>
                · Отозванные ссылки: <strong><?= e((string) (int) $hShare['revoked_count']) ?></strong>
            <?php endif; ?>
        </p>
    <?php else: ?>
        <p>
            <span class="share-badge share-badge--blocked">Нельзя отправлять</span>
            · <?= e($shareReason) ?>
        </p>
        <p class="field-hint handoff-not-ready">Не готово к отправке. Тексты для отправки недоступны для этого файла.</p>
    <?php endif; ?>

    <?php if ($hChecks !== []): ?>
        <h3 class="handoff-subhead">Чек-лист готовности</h3>
        <ul class="handoff-checklist">
            <?php foreach ($hChecks as $item): ?>
                <?php if (!is_array($item)) { continue; } ?>
                <li class="<?= !empty($item['pass']) ? 'check-pass' : 'check-fail' ?>">
                    <span class="check-mark"><?= !empty($item['pass']) ? '✓' : '○' ?></span>
                    <?= e((string) ($item['label'] ?? '')) ?>
                    <span class="meta-muted">— <?= e((string) ($item['note'] ?? '')) ?></span>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <?php if ($urlLost !== ''): ?>
        <p class="handoff-once-gone" role="status"><?= e($urlLost) ?></p>
    <?php elseif ($shareEligible && empty($hShare['has_active'])): ?>
        <p class="field-hint">Активной ссылки нет. Создайте ссылку на странице «Ссылки для клиента», чтобы получить URL и тексты для отправки.</p>
    <?php endif; ?>

    <?php if ($hWarnings !== []): ?>
        <h3 class="handoff-subhead">Предупреждения</h3>
        <ul class="handoff-warnings">
            <?php foreach ($hWarnings as $w): ?>
                <li><?= e((string) $w) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <p class="field-hint">Тексты для отправки появляются сразу после создания ссылки, пока URL ещё виден на экране.</p>
</section>

<details class="panel tech-details">
    <summary>Технические детали</summary>
    <ul class="facts export-meta-list">
        <li><strong>ID:</strong> <?= e((string) $exportId) ?></li>
        <li><strong>Ключ файла:</strong> <code><?= e((string) ($export['export_key'] ?? '')) ?></code></li>
        <li><strong>Формат:</strong> <code><?= e($format) ?></code></li>
        <li><strong>Статус:</strong> <span class="status-badge status-<?= e($exportStatus) ?>"><?= e($statusRu($exportStatus)) ?></span></li>
        <li><strong>Шаблон:</strong>
            <span class="template-badge<?= $isLegacyTemplateMetadata ? ' template-badge--legacy' : ' template-badge--styled' ?>"><?= e($templateLabel) ?></span>
        </li>
        <li><strong>Тип генерации:</strong> <?= e($renderTargetLabel) ?></li>
        <li><strong>Генератор:</strong> <?= e($renderEngineLabel) ?></li>
        <?php if ($isPdf): ?>
            <li><strong>Исходный HTML:</strong>
                <span class="source-lineage<?= $sourceHtmlLabel === 'не записан' || $sourceHtmlLabel === 'not recorded' ? ' source-lineage--unknown' : '' ?>">
                    <?= e($sourceHtmlLabel) ?>
                </span>
            </li>
        <?php endif; ?>
        <?php if ($isLegacyTemplateMetadata): ?>
            <li><strong>Шаблон по умолчанию (для новых версий):</strong> <code><?= e($futureTemplateId) ?></code> v<?= e($futureTemplateVersion) ?></li>
        <?php endif; ?>
        <li><strong>Имя файла:</strong> <code><?= e((string) ($export['filename'] ?? '')) ?></code></li>
        <li><strong>MIME-тип:</strong> <code><?= e((string) ($export['mime_type'] ?? '')) ?></code></li>
        <li><strong>Размер файла:</strong> <?= e($fileSize > 0 ? number_format($fileSize) . ' байт' : '—') ?></li>
        <li><strong>Контрольная сумма:</strong> <code class="checksum-display" title="<?= e($checksum) ?>"><?= e($checksumShort) ?></code></li>
        <li><strong>Полная контрольная сумма:</strong> <code class="checksum-full"><?= e($checksum) ?></code></li>
        <li><strong>Контрольная сумма снимка:</strong> <code class="checksum-display" title="<?= e($sourceChecksum) ?>"><?= e($sourceShort) ?></code></li>
        <li><strong>Полная сумма снимка:</strong> <code class="checksum-full"><?= e($sourceChecksum) ?></code></li>
        <li><strong>Диск хранения:</strong> <?= e((string) ($export['storage_disk'] ?? 'local')) ?></li>
        <li><strong>Снимок:</strong> <?= e((string) $snapshotId) ?>
            <?php if (!empty($export['snapshot_key'])): ?>
                · <code><?= e((string) $export['snapshot_key']) ?></code>
            <?php endif; ?>
        </li>
        <li><strong>Месячный отчет:</strong> <?= e((string) $monthlyId) ?></li>
        <li><strong>Создан:</strong> <?= e((string) ($export['created_at'] ?? '—')) ?></li>
        <li><strong>Создал:</strong>
            <?= e((string) ($export['created_by_name'] ?? '—')) ?>
        </li>
        <?php if ($storagePath !== ''): ?>
            <li><strong>Путь к файлу:</strong> <code class="storage-path-tech"><?= e($storagePath) ?></code></li>
        <?php endif; ?>
    </ul>
</details>

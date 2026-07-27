<?php
declare(strict_types=1);

/** @var array<string, mixed> $export */
/** @var string $message */
/** @var string $templateLabel */
/** @var bool $isStyledExport */

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
$downloadLabel = $isPdf ? 'Download PDF' : 'Download HTML';
$artifactLabel = $isPdf ? 'PDF artifact' : 'HTML artifact';
/** @var array{id?:string,version?:int}|null $futureTemplate */
$futureTemplate = is_array($futureTemplate ?? null) ? $futureTemplate : [];
$legacyTemplateLabel = (string) ($legacyTemplateLabel ?? 'not recorded (legacy/current exporter)');
$futureTemplateId = (string) ($futureTemplate['id'] ?? 'iseo_default_v1');
$futureTemplateVersion = (string) (int) ($futureTemplate['version'] ?? 1);
$isStyledExport = !empty($isStyledExport);
$templateLabel = (string) ($templateLabel ?? ($isStyledExport
    ? ($futureTemplateId . ' v' . $futureTemplateVersion)
    : $legacyTemplateLabel));
?>
<section class="panel export-card export-detail">
    <div class="panel-head">
        <h2>Export detail</h2>
        <p>
            <?php if ($snapshotId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId)) ?>">Snapshot</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">All exports</a>
            <?php endif; ?>
            <?php if ($monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Monthly report</a>
            <?php endif; ?>
            <?php if ($exportId > 0 && (string) ($export['status'] ?? '') === 'ready'): ?>
                <a class="btn" href="<?= e(url_path('/report-exports/' . $exportId . '/download')) ?>"><?= e($downloadLabel) ?></a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Internal only</span>
        <span class="artifact-badge<?= $isPdf ? ' artifact-badge--pdf' : '' ?>"><?= e($artifactLabel) ?></span>
        <?php if ($isStyledExport): ?>
            <span class="template-badge template-badge--styled">Styled export</span>
        <?php else: ?>
            <span class="template-badge">Historical v1</span>
        <?php endif; ?>
        · <span class="status-badge status-<?= e((string) ($export['status'] ?? '')) ?>"><?= e((string) ($export['status'] ?? '')) ?></span>
    </p>

    <ul class="facts export-meta-list">
        <li><strong>ID:</strong> <?= e((string) $exportId) ?></li>
        <li><strong>Export key:</strong> <code><?= e((string) ($export['export_key'] ?? '')) ?></code></li>
        <li><strong>Format:</strong> <code><?= e($format) ?></code></li>
        <li><strong>Status:</strong> <span class="status-badge status-<?= e((string) ($export['status'] ?? '')) ?>"><?= e((string) ($export['status'] ?? '')) ?></span></li>
        <li><strong>Template:</strong>
            <span class="template-badge<?= $isStyledExport ? ' template-badge--styled' : '' ?>"><?= e($templateLabel) ?></span>
        </li>
        <?php if (!$isStyledExport): ?>
            <li><strong>Default template (for new versions):</strong> <code><?= e($futureTemplateId) ?></code> v<?= e($futureTemplateVersion) ?></li>
        <?php endif; ?>
        <li><strong>Filename:</strong> <code><?= e((string) ($export['filename'] ?? '')) ?></code></li>
        <li><strong>MIME type:</strong> <code><?= e((string) ($export['mime_type'] ?? '')) ?></code></li>
        <li><strong>File size:</strong> <?= e($fileSize > 0 ? number_format($fileSize) . ' bytes' : '—') ?></li>
        <li><strong>File checksum:</strong> <code class="checksum-display" title="<?= e($checksum) ?>"><?= e($checksumShort) ?></code></li>
        <li><strong>Full file checksum:</strong> <code class="checksum-full"><?= e($checksum) ?></code></li>
        <li><strong>Source snapshot checksum:</strong> <code class="checksum-display" title="<?= e($sourceChecksum) ?>"><?= e($sourceShort) ?></code></li>
        <li><strong>Full source checksum:</strong> <code class="checksum-full"><?= e($sourceChecksum) ?></code></li>
        <li><strong>Storage disk:</strong> <?= e((string) ($export['storage_disk'] ?? 'local')) ?></li>
        <li><strong>Storage path:</strong> <code><?= e((string) ($export['storage_path'] ?? '')) ?></code></li>
        <li><strong>Snapshot ID:</strong> <?= e((string) $snapshotId) ?>
            <?php if (!empty($export['snapshot_key'])): ?>
                · <code><?= e((string) $export['snapshot_key']) ?></code>
            <?php endif; ?>
        </li>
        <li><strong>Monthly report ID:</strong> <?= e((string) $monthlyId) ?></li>
        <li><strong>Created at:</strong> <?= e((string) ($export['created_at'] ?? '—')) ?></li>
        <li><strong>Created by:</strong>
            <?= e((string) ($export['created_by_name'] ?? '—')) ?>
            <?php if (!empty($export['created_by_email'])): ?>
                · <?= e((string) $export['created_by_email']) ?>
            <?php endif; ?>
        </li>
    </ul>

    <p class="field-hint export-hint">
        No public link. Download requires authentication. Path/MIME/size/checksum<?= $isPdf ? '/PDF-magic' : '' ?> are validated before streaming.
        <?php if ($isStyledExport): ?>
            This styled export uses <code><?= e($futureTemplateId) ?></code> v<?= e($futureTemplateVersion) ?> and does not replace historical v1 artifacts.
        <?php else: ?>
            This historical row has no DB template_id; restyle requires a new export version (v2+), not an overwrite.
        <?php endif; ?>
    </p>
</section>

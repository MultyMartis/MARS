<?php
declare(strict_types=1);

/** @var array<string, mixed> $export */
/** @var string $message */

$export = $export ?? [];
$message = (string) ($message ?? '');

$exportId = (int) ($export['id'] ?? 0);
$snapshotId = (int) ($export['report_snapshot_id'] ?? 0);
$monthlyId = (int) ($export['monthly_report_content_id'] ?? 0);
$checksum = (string) ($export['checksum_sha256'] ?? '');
$checksumShort = $checksum !== '' ? substr($checksum, 0, 12) . '…' : '—';
$sourceChecksum = (string) ($export['source_snapshot_checksum_sha256'] ?? '');
$sourceShort = $sourceChecksum !== '' ? substr($sourceChecksum, 0, 12) . '…' : '—';
$fileSize = isset($export['file_size_bytes']) ? (int) $export['file_size_bytes'] : 0;
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
                <a class="btn" href="<?= e(url_path('/report-exports/' . $exportId . '/download')) ?>">Download HTML</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Internal only</span>
        <span class="artifact-badge">HTML artifact</span>
        · <span class="status-badge status-<?= e((string) ($export['status'] ?? '')) ?>"><?= e((string) ($export['status'] ?? '')) ?></span>
    </p>

    <ul class="facts export-meta-list">
        <li><strong>ID:</strong> <?= e((string) $exportId) ?></li>
        <li><strong>Export key:</strong> <code><?= e((string) ($export['export_key'] ?? '')) ?></code></li>
        <li><strong>Format:</strong> <code><?= e((string) ($export['format'] ?? '')) ?></code></li>
        <li><strong>Status:</strong> <span class="status-badge status-<?= e((string) ($export['status'] ?? '')) ?>"><?= e((string) ($export['status'] ?? '')) ?></span></li>
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

    <p class="field-hint">No public link. Download requires authentication.</p>
</section>

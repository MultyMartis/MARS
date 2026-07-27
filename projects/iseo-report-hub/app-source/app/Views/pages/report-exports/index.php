<?php
declare(strict_types=1);

/** @var array<string, mixed> $snapshot */
/** @var list<array<string, mixed>> $exports */
/** @var bool $canCreate */
/** @var bool $canCreatePdf */
/** @var bool $hasHtmlExport */
/** @var bool $hasPdfExport */
/** @var string $message */
/** @var \Iseo\Services\CsrfService $csrf */

$snapshot = $snapshot ?? [];
$exports = $exports ?? [];
$canCreate = !empty($canCreate);
$canCreatePdf = !empty($canCreatePdf);
$hasHtmlExport = !empty($hasHtmlExport);
$hasPdfExport = !empty($hasPdfExport);
$message = (string) ($message ?? '');

$snapshotId = (int) ($snapshot['id'] ?? 0);
$monthlyId = (int) ($snapshot['monthly_report_content_id'] ?? 0);
$snapshotKey = (string) ($snapshot['snapshot_key'] ?? '');
?>
<section class="panel export-card">
    <div class="panel-head">
        <h2>Report exports</h2>
        <p>
            <?php if ($snapshotId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId)) ?>">Snapshot detail</a>
            <?php endif; ?>
            <?php if ($monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Monthly report</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Internal only</span>
        <span class="artifact-badge">HTML artifact</span>
        <span class="artifact-badge artifact-badge--pdf">PDF artifact</span>
        · Snapshot <code><?= e($snapshotKey) ?></code>
    </p>

    <?php if ($exports === []): ?>
        <p class="note">No exports yet for this snapshot.</p>
        <?php if ($canCreate && $snapshotId > 0): ?>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html')) ?>">
                <?= $csrf->field() ?>
                <button type="submit" class="btn">Create HTML export</button>
            </form>
        <?php elseif ($snapshotId > 0): ?>
            <p class="field-hint">Export creation requires admin_owner or seo_lead_reviewer role.</p>
        <?php endif; ?>
    <?php else: ?>
        <div class="table-wrap">
            <table class="data-table export-table">
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Key</th>
                    <th>Format</th>
                    <th>Status</th>
                    <th>Filename</th>
                    <th>Checksum</th>
                    <th>Size</th>
                    <th>Created</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ($exports as $row): ?>
                    <?php
                    if (!is_array($row)) {
                        continue;
                    }
                    $eid = (int) ($row['id'] ?? 0);
                    $checksum = (string) ($row['checksum_sha256'] ?? '');
                    $short = $checksum !== '' ? substr($checksum, 0, 12) . '…' : '—';
                    $size = isset($row['file_size_bytes']) ? (int) $row['file_size_bytes'] : 0;
                    $format = (string) ($row['format'] ?? '');
                    ?>
                    <tr>
                        <td><?= e((string) $eid) ?></td>
                        <td><code><?= e((string) ($row['export_key'] ?? '')) ?></code></td>
                        <td>
                            <span class="type-badge<?= $format === 'pdf' ? ' type-badge--pdf' : '' ?>"><?= e($format) ?></span>
                        </td>
                        <td><span class="status-badge status-<?= e((string) ($row['status'] ?? '')) ?>"><?= e((string) ($row['status'] ?? '')) ?></span></td>
                        <td><code><?= e((string) ($row['filename'] ?? '')) ?></code></td>
                        <td><code class="checksum-display" title="<?= e($checksum) ?>"><?= e($short) ?></code></td>
                        <td><?= e($size > 0 ? number_format($size) . ' B' : '—') ?></td>
                        <td><?= e((string) ($row['created_at'] ?? '—')) ?></td>
                        <td class="actions">
                            <a href="<?= e(url_path('/report-exports/' . $eid)) ?>">View</a>
                            · <a class="btn-download" href="<?= e(url_path('/report-exports/' . $eid . '/download')) ?>">Download</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>

        <?php if ($canCreate && $snapshotId > 0): ?>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html')) ?>" class="export-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn btn-secondary">Create / re-check HTML export (idempotent)</button>
            </form>
        <?php endif; ?>

        <?php if ($canCreatePdf && $snapshotId > 0 && $hasHtmlExport && !$hasPdfExport): ?>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>" class="export-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn">Create PDF export</button>
            </form>
        <?php elseif ($canCreatePdf && $snapshotId > 0 && $hasPdfExport): ?>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>" class="export-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn btn-secondary">Create / re-check PDF export (idempotent)</button>
            </form>
        <?php elseif ($hasHtmlExport && !$hasPdfExport && $snapshotId > 0 && !$canCreatePdf): ?>
            <p class="field-hint">PDF creation requires admin_owner or seo_lead_reviewer role.</p>
        <?php endif; ?>
    <?php endif; ?>
</section>

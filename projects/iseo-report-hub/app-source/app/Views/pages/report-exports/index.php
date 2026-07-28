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
$legacyTemplateLabel = (string) ($legacyTemplateLabel ?? 'not recorded / legacy');
$futureTemplateId = (string) ($futureTemplate['id'] ?? 'iseo_default_v1');
$futureTemplateVersion = (string) (int) ($futureTemplate['version'] ?? 1);
$styledTemplateLabel = $futureTemplateId . ' v' . $futureTemplateVersion;

$snapshotId = (int) ($snapshot['id'] ?? 0);
$monthlyId = (int) ($snapshot['monthly_report_content_id'] ?? 0);
$snapshotKey = (string) ($snapshot['snapshot_key'] ?? '');

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
    <p class="template-state-note">
        <strong>DB template metadata:</strong> preferred over filename/key inference.
        <br>
        <strong>Legacy / NULL:</strong> <?= e($legacyTemplateLabel) ?>.
        <br>
        <strong>Recorded default:</strong>
        <code><?= e($futureTemplateId) ?></code> v<?= e($futureTemplateVersion) ?>
        (styled export versions; does not rewrite v1 artifacts).
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
                    <th>Template</th>
                    <th>Render</th>
                    <th>Source HTML</th>
                    <th>Share</th>
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
                    $tplLabel = $rowTemplateLabel($row);
                    $isLegacyRow = !empty($row['is_legacy_template_metadata'])
                        || $tplLabel === $legacyTemplateLabel;
                    $renderTarget = (string) ($row['display_render_target_label'] ?? 'not recorded');
                    $renderEngine = (string) ($row['display_render_engine_label'] ?? 'not recorded');
                    $sourceHtmlLabel = (string) ($row['display_source_html_label'] ?? 'not recorded');
                    if ($format !== 'pdf') {
                        $sourceHtmlLabel = '—';
                    }
                    $shareEligible = !empty($row['share_eligible']);
                    $activeShares = (int) ($row['active_share_count'] ?? 0);
                    ?>
                    <tr>
                        <td><?= e((string) $eid) ?></td>
                        <td><code><?= e((string) ($row['export_key'] ?? '')) ?></code></td>
                        <td>
                            <span class="type-badge<?= $format === 'pdf' ? ' type-badge--pdf' : '' ?>"><?= e($format) ?></span>
                        </td>
                        <td><span class="status-badge status-<?= e((string) ($row['status'] ?? '')) ?>"><?= e((string) ($row['status'] ?? '')) ?></span></td>
                        <td>
                            <span class="template-badge<?= $isLegacyRow ? ' template-badge--legacy' : ' template-badge--styled' ?>">
                                <?= e($tplLabel) ?>
                            </span>
                        </td>
                        <td>
                            <span class="meta-muted"><?= e($renderTarget) ?></span>
                            <br>
                            <span class="meta-muted"><?= e($renderEngine) ?></span>
                        </td>
                        <td>
                            <?php if ($format === 'pdf'): ?>
                                <span class="source-lineage<?= $sourceHtmlLabel === 'not recorded' ? ' source-lineage--unknown' : '' ?>">
                                    <?= e($sourceHtmlLabel) ?>
                                </span>
                            <?php else: ?>
                                <span class="meta-muted">—</span>
                            <?php endif; ?>
                        </td>
                        <td>
                            <?php if ($shareEligible): ?>
                                <span class="share-badge share-badge--eligible">Shareable</span>
                                <?php if ($activeShares > 0): ?>
                                    <br><span class="meta-muted">Active: <?= e((string) $activeShares) ?></span>
                                <?php endif; ?>
                            <?php else: ?>
                                <span class="share-badge share-badge--blocked">No</span>
                            <?php endif; ?>
                        </td>
                        <td><code><?= e((string) ($row['filename'] ?? '')) ?></code></td>
                        <td><code class="checksum-display" title="<?= e($checksum) ?>"><?= e($short) ?></code></td>
                        <td><?= e($size > 0 ? number_format($size) . ' B' : '—') ?></td>
                        <td><?= e((string) ($row['created_at'] ?? '—')) ?></td>
                        <td class="actions">
                            <a href="<?= e(url_path('/report-exports/' . $eid)) ?>">View</a>
                            · <a class="btn-download" href="<?= e(url_path('/report-exports/' . $eid . '/download')) ?>">Download</a>
                            · <a href="<?= e(url_path('/report-exports/' . $eid . '/shares')) ?>">Shares</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>

        <?php if ($canCreate && $snapshotId > 0): ?>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html')) ?>" class="export-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn btn-secondary">Re-check HTML export (idempotent)</button>
            </form>
            <p class="field-hint export-hint">Legacy HTML re-check returns the existing ready v1 artifact when checksums match; it does not create a duplicate row.</p>
        <?php endif; ?>

        <?php if ($canCreatePdf && $snapshotId > 0 && $hasHtmlExport && !$hasPdfExport): ?>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>" class="export-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn">Create PDF export</button>
            </form>
            <p class="field-hint export-hint">PDF is generated from the ready HTML artifact via Edge headless (Chrome fallback). No public URL.</p>
        <?php elseif ($canCreatePdf && $snapshotId > 0 && $hasPdfExport): ?>
            <p class="export-ready-note">Legacy PDF export is ready. Create is not needed — use Download or re-check below.</p>
            <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>" class="export-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn btn-secondary">Re-check PDF export (idempotent)</button>
            </form>
            <p class="field-hint export-hint">Re-check validates metadata and file integrity and returns the existing PDF (id unchanged; no rewrite).</p>
        <?php elseif ($hasHtmlExport && !$hasPdfExport && $snapshotId > 0 && !$canCreatePdf): ?>
            <p class="field-hint">PDF creation requires admin_owner or seo_lead_reviewer role.</p>
        <?php endif; ?>

        <?php if ($canCreateStyledHtml && $snapshotId > 0): ?>
            <?php if ($styledHtmlExport === null): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Create styled HTML export (<?= e($styledTemplateLabel) ?>)</button>
                </form>
                <p class="field-hint export-hint">Creates a new HTML export version with embedded default template CSS. Does not overwrite historical v1.</p>
            <?php else: ?>
                <p class="export-ready-note">
                    Styled HTML ready:
                    <code><?= e((string) ($styledHtmlExport['export_key'] ?? '')) ?></code>
                    · template <code><?= e((string) ($styledHtmlExport['display_template_label'] ?? $styledTemplateLabel)) ?></code>
                </p>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Re-check styled HTML (idempotent)</button>
                </form>
            <?php endif; ?>
        <?php endif; ?>

        <?php if ($canCreateStyledPdf && $snapshotId > 0): ?>
            <?php if ($styledPdfExport === null): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Create styled PDF export from HTML v2</button>
                </form>
                <p class="field-hint export-hint">PDF is printed from styled HTML v2 via Edge headless. Does not overwrite historical v1 PDF.</p>
            <?php else: ?>
                <p class="export-ready-note">
                    Styled PDF ready:
                    <code><?= e((string) ($styledPdfExport['export_key'] ?? '')) ?></code>
                    · source HTML <?= e((string) ($styledPdfExport['display_source_html_label'] ?? 'not recorded')) ?>
                </p>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Re-check styled PDF (idempotent)</button>
                </form>
            <?php endif; ?>
        <?php elseif ($styledHtmlExport !== null && $styledPdfExport === null && $snapshotId > 0 && !$canCreateStyledPdf): ?>
            <p class="field-hint">Styled PDF creation requires admin_owner or seo_lead_reviewer role and a browser PDF engine.</p>
        <?php endif; ?>

        <p class="field-hint export-hint">Auth downloads require authentication. Public share is available only for ready styled PDF exports (MVP: export id 4).</p>
    <?php endif; ?>
</section>

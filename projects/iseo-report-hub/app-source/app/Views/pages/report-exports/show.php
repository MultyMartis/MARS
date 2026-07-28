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
$legacyTemplateLabel = (string) ($legacyTemplateLabel ?? 'not recorded / legacy');
$futureTemplateId = (string) ($futureTemplate['id'] ?? 'iseo_default_v1');
$futureTemplateVersion = (string) (int) ($futureTemplate['version'] ?? 1);
$isLegacyTemplateMetadata = !empty($isLegacyTemplateMetadata);
$isStyledExport = !empty($isStyledExport);
$templateLabel = (string) ($templateLabel ?? ($export['display_template_label'] ?? $legacyTemplateLabel));
$renderTargetLabel = (string) ($renderTargetLabel ?? ($export['display_render_target_label'] ?? 'not recorded'));
$renderEngineLabel = (string) ($renderEngineLabel ?? ($export['display_render_engine_label'] ?? 'not recorded'));
$sourceHtmlSummary = is_array($sourceHtmlSummary ?? null) ? $sourceHtmlSummary : null;
$sourceHtmlLabel = is_array($sourceHtmlSummary) && isset($sourceHtmlSummary['label'])
    ? (string) $sourceHtmlSummary['label']
    : (string) ($export['display_source_html_label'] ?? 'not recorded');
$shareEligibility = is_array($shareEligibility ?? null) ? $shareEligibility : [];
$shareEligible = !empty($shareEligibility['eligible']);
$shareReason = (string) ($shareEligibility['reason'] ?? 'Eligibility not evaluated.');
$activeShareCount = (int) ($activeShareCount ?? 0);
$canManageShares = !empty($canManageShares);
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
            <?php if ($exportId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>">Public shares</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Internal only</span>
        <span class="artifact-badge<?= $isPdf ? ' artifact-badge--pdf' : '' ?>"><?= e($artifactLabel) ?></span>
        <?php if ($isLegacyTemplateMetadata): ?>
            <span class="template-badge template-badge--legacy">Legacy / not recorded</span>
        <?php else: ?>
            <span class="template-badge template-badge--styled">Recorded template</span>
        <?php endif; ?>
        <?php if ($shareEligible): ?>
            <span class="share-badge share-badge--eligible">Shareable PDF</span>
        <?php else: ?>
            <span class="share-badge share-badge--blocked">Not shareable</span>
        <?php endif; ?>
        · <span class="status-badge status-<?= e((string) ($export['status'] ?? '')) ?>"><?= e((string) ($export['status'] ?? '')) ?></span>
    </p>

    <ul class="facts export-meta-list">
        <li><strong>ID:</strong> <?= e((string) $exportId) ?></li>
        <li><strong>Export key:</strong> <code><?= e((string) ($export['export_key'] ?? '')) ?></code></li>
        <li><strong>Format:</strong> <code><?= e($format) ?></code></li>
        <li><strong>Status:</strong> <span class="status-badge status-<?= e((string) ($export['status'] ?? '')) ?>"><?= e((string) ($export['status'] ?? '')) ?></span></li>
        <li><strong>Template:</strong>
            <span class="template-badge<?= $isLegacyTemplateMetadata ? ' template-badge--legacy' : ' template-badge--styled' ?>"><?= e($templateLabel) ?></span>
        </li>
        <li><strong>Render target:</strong> <?= e($renderTargetLabel) ?></li>
        <li><strong>Render engine:</strong> <?= e($renderEngineLabel) ?></li>
        <?php if ($isPdf): ?>
            <li><strong>Source HTML:</strong>
                <span class="source-lineage<?= $sourceHtmlLabel === 'not recorded' ? ' source-lineage--unknown' : '' ?>">
                    <?= e($sourceHtmlLabel) ?>
                </span>
            </li>
        <?php endif; ?>
        <?php if ($isLegacyTemplateMetadata): ?>
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
        Auth download requires authentication. Path/MIME/size/checksum<?= $isPdf ? '/PDF-magic' : '' ?> are validated before streaming.
        Template/render fields come from DB-09 columns when present; NULL rows stay <?= e($legacyTemplateLabel) ?> and are never inferred as <code><?= e($futureTemplateId) ?></code>.
    </p>
</section>

<section class="panel export-card share-card">
    <div class="panel-head">
        <h2>Public share</h2>
        <p>
            <a class="btn" href="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>">Manage shares</a>
        </p>
    </div>
    <p>
        <?php if ($shareEligible): ?>
            <span class="share-badge share-badge--eligible">Eligible</span>
        <?php else: ?>
            <span class="share-badge share-badge--blocked">Not eligible</span>
        <?php endif; ?>
        · Active shares: <strong><?= e((string) $activeShareCount) ?></strong>
    </p>
    <p class="field-hint share-hint"><?= e($shareReason) ?></p>
    <?php if ($shareEligible && $canManageShares): ?>
        <p class="field-hint">Create or revoke opaque token links on the shares page. Plaintext URL is shown once.</p>
    <?php elseif ($shareEligible): ?>
        <p class="field-hint">View share status on the shares page. Create/revoke requires admin_owner or seo_lead_reviewer.</p>
    <?php endif; ?>
</section>

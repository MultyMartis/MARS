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
            <span class="share-badge share-badge--eligible">Shareable</span>
        <?php else: ?>
            <span class="share-badge share-badge--blocked" title="<?= e($shareReason) ?>">Not shareable</span>
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

    <?php if ($storagePath !== ''): ?>
        <details class="tech-details">
            <summary>Technical details (internal)</summary>
            <p class="field-hint">
                <strong>Internal technical artifact path</strong> (not for client messages):
                <code class="storage-path-tech"><?= e($storagePath) ?></code>
            </p>
        </details>
    <?php endif; ?>

    <p class="field-hint export-hint">
        Auth download requires authentication. Path/MIME/size/checksum<?= $isPdf ? '/PDF-magic' : '' ?> are validated before streaming.
        Template/render fields come from DB-09 columns when present; NULL rows stay <?= e($legacyTemplateLabel) ?> and are never inferred as <code><?= e($futureTemplateId) ?></code>.
    </p>
</section>

<section class="panel export-card handoff-panel" data-handoff-panel>
    <div class="panel-head">
        <h2>Client handoff readiness</h2>
        <p>
            <a class="btn" href="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>">Open shares / copy pack</a>
        </p>
    </div>

    <?php if ($shareEligible): ?>
        <p>
            <span class="share-badge share-badge--eligible">Shareable</span>
            · Active shares: <strong><?= e((string) ($hShare['active_count'] ?? $activeShareCount)) ?></strong>
            <?php if (!empty($hShare['expires_at'])): ?>
                · Expires: <code><?= e((string) $hShare['expires_at']) ?></code>
            <?php endif; ?>
            <?php if ((int) ($hShare['revoked_count'] ?? 0) > 0): ?>
                · Revoked rows: <strong><?= e((string) (int) $hShare['revoked_count']) ?></strong>
            <?php endif; ?>
        </p>
    <?php else: ?>
        <p>
            <span class="share-badge share-badge--blocked">Not shareable</span>
            · <?= e($shareReason) ?>
        </p>
        <p class="field-hint handoff-not-ready">Not delivery ready. No handoff copy pack for this export.</p>
    <?php endif; ?>

    <ul class="facts handoff-context-list">
        <li><strong>Client:</strong> <?= e((string) ($hCtx['client_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Project:</strong> <?= e((string) ($hCtx['project_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Period:</strong> <?= e((string) ($hCtx['period'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Report status:</strong> <?= e((string) ($hCtx['report_status'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Snapshot key:</strong> <code><?= e((string) ($hCtx['snapshot_key'] ?? 'SAFE UNKNOWN')) ?></code></li>
        <li><strong>Export:</strong> id <?= e((string) $exportId) ?> · <code><?= e((string) ($export['export_key'] ?? '')) ?></code></li>
        <li><strong>Export format:</strong> <code><?= e($format) ?></code></li>
        <li><strong>Template:</strong> <?= e((string) ($hCtx['template_label'] ?? $templateLabel)) ?></li>
        <li><strong>Share status:</strong>
            <?php if (!empty($hShare['has_active'])): ?>
                active exists
            <?php else: ?>
                no active share
            <?php endif; ?>
        </li>
    </ul>

    <?php if ($hChecks !== []): ?>
        <h3 class="handoff-subhead">Readiness checklist</h3>
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
        <p class="field-hint">No active share. Create a share on the shares page to get the once-only public URL and copy pack.</p>
    <?php endif; ?>

    <?php if ($hWarnings !== []): ?>
        <h3 class="handoff-subhead">Warnings</h3>
        <ul class="handoff-warnings">
            <?php foreach ($hWarnings as $w): ?>
                <li><?= e((string) $w) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <p class="field-hint">Copy pack (short / email / internal note) appears only immediately after share creation while the plaintext URL is available. No DB delivery tracking in this MVP.</p>
</section>

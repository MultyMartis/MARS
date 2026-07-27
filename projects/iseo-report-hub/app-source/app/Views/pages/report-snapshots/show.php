<?php
declare(strict_types=1);

/** @var string $mode */
/** @var array<string, mixed>|null $monthly */
/** @var array<string, mixed>|null $snapshot */
/** @var array<string, mixed>|null $payload */
/** @var bool $canCreate */
/** @var string $message */
/** @var array<string, mixed>|null $htmlExport */
/** @var array<string, mixed>|null $pdfExport */
/** @var array<string, mixed>|null $styledHtmlExport */
/** @var array<string, mixed>|null $styledPdfExport */
/** @var bool $canCreateExport */
/** @var bool $canCreatePdfExport */
/** @var bool $canCreateStyledHtml */
/** @var bool $canCreateStyledPdf */
/** @var \Iseo\Services\CsrfService $csrf */

$mode = $mode ?? 'detail';
$monthly = $monthly ?? null;
$snapshot = $snapshot ?? null;
$payload = $payload ?? null;
$canCreate = !empty($canCreate);
$message = (string) ($message ?? '');
$htmlExport = $htmlExport ?? null;
$pdfExport = $pdfExport ?? null;
$styledHtmlExport = $styledHtmlExport ?? null;
$styledPdfExport = $styledPdfExport ?? null;
$canCreateExport = !empty($canCreateExport);
$canCreatePdfExport = !empty($canCreatePdfExport);
$canCreateStyledHtml = !empty($canCreateStyledHtml);
$canCreateStyledPdf = !empty($canCreateStyledPdf);
$legacyTemplateLabel = (string) ($legacyTemplateLabel ?? 'not recorded (legacy/current exporter)');
$futureTemplate = is_array($futureTemplate ?? null) ? $futureTemplate : [];
$futureTemplateId = (string) ($futureTemplate['id'] ?? 'iseo_default_v1');
$futureTemplateVersion = (string) (int) ($futureTemplate['version'] ?? 1);
$styledTemplateLabel = $futureTemplateId . ' v' . $futureTemplateVersion;

$monthlyId = 0;
if (is_array($snapshot) && isset($snapshot['monthly_report_content_id'])) {
    $monthlyId = (int) $snapshot['monthly_report_content_id'];
} elseif (is_array($monthly)) {
    $monthlyId = (int) $monthly['id'];
}

$checksum = is_array($snapshot) ? (string) ($snapshot['checksum_sha256'] ?? '') : '';
$checksumShort = $checksum !== '' ? substr($checksum, 0, 12) . '…' : '—';

$blocks = [];
$weeklySources = [];
$periodKey = '';
if (is_array($payload)) {
    $blocks = is_array($payload['blocks'] ?? null) ? $payload['blocks'] : [];
    $weeklySources = is_array($payload['weekly_sources'] ?? null) ? $payload['weekly_sources'] : [];
    $periodKey = (string) (($payload['period']['key'] ?? '') ?: '');
}
if ($periodKey === '' && is_array($monthly)) {
    $periodKey = (string) ($monthly['period_key'] ?? '');
}

/**
 * @param mixed $raw
 * @return list<int>
 */
$decodeIds = static function (mixed $raw): array {
    if (is_array($raw)) {
        $out = [];
        foreach ($raw as $v) {
            $id = (int) $v;
            if ($id > 0) {
                $out[] = $id;
            }
        }
        return array_values(array_unique($out));
    }
    if (!is_string($raw) || $raw === '') {
        return [];
    }
    $decoded = json_decode($raw, true);
    if (!is_array($decoded)) {
        return [];
    }
    $out = [];
    foreach ($decoded as $v) {
        $id = (int) $v;
        if ($id > 0) {
            $out[] = $id;
        }
    }
    return array_values(array_unique($out));
};
?>
<section class="panel snapshot-card">
    <div class="panel-head">
        <h2><?= $mode === 'monthly' ? 'Report snapshot' : 'Snapshot detail' ?></h2>
        <p>
            <?php if ($monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Monthly report</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/preview')) ?>">Preview</a>
            <?php endif; ?>
            <?php if ($mode === 'detail' && $monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/snapshot')) ?>">Snapshot summary</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Internal only</span>
        <span class="immutable-badge">Immutable</span>
        <?php if (is_array($snapshot)): ?>
            · <span class="status-badge status-<?= e((string) $snapshot['status']) ?>"><?= e((string) $snapshot['status']) ?></span>
        <?php endif; ?>
    </p>

    <?php if ($mode === 'monthly' && $snapshot === null): ?>
        <p class="note">No snapshot yet for this monthly report.</p>
        <?php if ($canCreate && $monthlyId > 0): ?>
            <form method="post" action="<?= e(url_path('/monthly-reports/' . $monthlyId . '/snapshot')) ?>">
                <?= $csrf->field() ?>
                <button type="submit" class="btn">Create snapshot</button>
            </form>
        <?php elseif (is_array($monthly) && (string) ($monthly['status'] ?? '') !== 'finalized'): ?>
            <p class="field-hint">Snapshot creation requires a finalized monthly report.</p>
        <?php endif; ?>
    <?php elseif (is_array($snapshot)): ?>
        <ul class="facts snapshot-meta">
            <li><strong>ID:</strong> <?= e((string) $snapshot['id']) ?></li>
            <li><strong>Key:</strong> <code><?= e((string) $snapshot['snapshot_key']) ?></code></li>
            <li><strong>Version:</strong> <?= e((string) $snapshot['version']) ?></li>
            <li><strong>Status:</strong> <span class="status-badge status-<?= e((string) $snapshot['status']) ?>"><?= e((string) $snapshot['status']) ?></span></li>
            <li><strong>Title:</strong> <?= e((string) $snapshot['title']) ?></li>
            <li><strong>Period:</strong> <code><?= e($periodKey !== '' ? $periodKey : '—') ?></code></li>
            <li><strong>Render mode:</strong> <code><?= e((string) $snapshot['render_mode']) ?></code></li>
            <li><strong>Checksum:</strong> <code class="checksum-display" title="<?= e($checksum) ?>"><?= e($checksumShort) ?></code></li>
            <li><strong>Full checksum:</strong> <code class="checksum-full"><?= e($checksum) ?></code></li>
            <li><strong>Created at:</strong> <?= e((string) ($snapshot['created_at'] ?? '—')) ?></li>
            <li><strong>Created by:</strong>
                <?= e((string) ($snapshot['created_by_name'] ?? '—')) ?>
                <?php if (!empty($snapshot['created_by_email'])): ?>
                    · <?= e((string) $snapshot['created_by_email']) ?>
                <?php endif; ?>
            </li>
        </ul>
        <p>
            <a class="btn" href="<?= e(url_path('/report-snapshots/' . (int) $snapshot['id'])) ?>">View snapshot</a>
            <?php if ($mode === 'monthly'): ?>
                <span class="field-hint">Create is idempotent while the active checksum matches.</span>
            <?php endif; ?>
        </p>
        <?php if ($mode === 'monthly' && $monthlyId > 0): ?>
            <form method="post" action="<?= e(url_path('/monthly-reports/' . $monthlyId . '/snapshot')) ?>" class="snapshot-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn btn-secondary">Re-check / create (idempotent)</button>
            </form>
        <?php endif; ?>
    <?php endif; ?>
</section>

<?php if (is_array($snapshot)): ?>
    <?php
    $snapshotId = (int) $snapshot['id'];
    $exportChecksum = is_array($htmlExport) ? (string) ($htmlExport['checksum_sha256'] ?? '') : '';
    $exportShort = $exportChecksum !== '' ? substr($exportChecksum, 0, 12) . '…' : '—';
    $exportSize = is_array($htmlExport) && isset($htmlExport['file_size_bytes']) ? (int) $htmlExport['file_size_bytes'] : 0;
    ?>
    <section class="panel export-card">
        <div class="panel-head">
            <h2>HTML export</h2>
            <p>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">All exports</a>
            </p>
        </div>
        <p>
            <span class="internal-only-badge">Internal only</span>
            <span class="artifact-badge">HTML artifact</span>
        </p>
        <p class="template-state-note">
            Historical v1 template: <?= e($legacyTemplateLabel) ?>.
            Styled default: <code><?= e($futureTemplateId) ?></code> v<?= e($futureTemplateVersion) ?> (new export version only).
        </p>
        <?php if (!is_array($htmlExport)): ?>
            <p class="note">No HTML export yet.</p>
            <?php if ($canCreateExport): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html')) ?>">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Create HTML export</button>
                </form>
            <?php endif; ?>
        <?php else: ?>
            <?php
            $displayHtml = is_array($styledHtmlExport) ? $styledHtmlExport : $htmlExport;
            $displayHtmlIsStyled = is_array($styledHtmlExport);
            $exportChecksum = (string) ($displayHtml['checksum_sha256'] ?? '');
            $exportShort = $exportChecksum !== '' ? substr($exportChecksum, 0, 12) . '…' : '—';
            $exportSize = isset($displayHtml['file_size_bytes']) ? (int) $displayHtml['file_size_bytes'] : 0;
            ?>
            <ul class="facts">
                <li><strong>Export ID:</strong> <?= e((string) $displayHtml['id']) ?></li>
                <li><strong>Key:</strong> <code><?= e((string) ($displayHtml['export_key'] ?? '')) ?></code></li>
                <li><strong>Format / status:</strong>
                    <span class="type-badge">html</span>
                    · <span class="status-badge status-<?= e((string) ($displayHtml['status'] ?? '')) ?>"><?= e((string) ($displayHtml['status'] ?? '')) ?></span>
                </li>
                <li><strong>Filename:</strong> <code><?= e((string) ($displayHtml['filename'] ?? '')) ?></code></li>
                <li><strong>Checksum:</strong> <code class="checksum-display" title="<?= e($exportChecksum) ?>"><?= e($exportShort) ?></code></li>
                <li><strong>Size:</strong> <?= e($exportSize > 0 ? number_format($exportSize) . ' B' : '—') ?></li>
                <li><strong>Template:</strong>
                    <span class="template-badge<?= $displayHtmlIsStyled ? ' template-badge--styled' : '' ?>">
                        <?= e($displayHtmlIsStyled ? $styledTemplateLabel : $legacyTemplateLabel) ?>
                    </span>
                </li>
            </ul>
            <p>
                <a class="btn" href="<?= e(url_path('/report-exports/' . (int) $displayHtml['id'])) ?>">View export</a>
                <a class="btn btn-secondary btn-download" href="<?= e(url_path('/report-exports/' . (int) $displayHtml['id'] . '/download')) ?>">Download HTML</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">All versions</a>
            </p>
            <?php if ($canCreateStyledHtml && !is_array($styledHtmlExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Create styled HTML (<?= e($styledTemplateLabel) ?>)</button>
                </form>
            <?php elseif ($canCreateStyledHtml && is_array($styledHtmlExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Re-check styled HTML (idempotent)</button>
                </form>
            <?php endif; ?>
            <p class="field-hint export-hint">No public URL. Historical v1 remains available on the exports list.</p>
        <?php endif; ?>
    </section>

    <?php
    $pdfChecksum = is_array($pdfExport) ? (string) ($pdfExport['checksum_sha256'] ?? '') : '';
    $pdfShort = $pdfChecksum !== '' ? substr($pdfChecksum, 0, 12) . '…' : '—';
    $pdfSize = is_array($pdfExport) && isset($pdfExport['file_size_bytes']) ? (int) $pdfExport['file_size_bytes'] : 0;
    ?>
    <section class="panel export-card">
        <div class="panel-head">
            <h2>PDF export</h2>
            <p>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">All exports</a>
            </p>
        </div>
        <p>
            <span class="internal-only-badge">Internal only</span>
            <span class="artifact-badge artifact-badge--pdf">PDF artifact</span>
        </p>
        <?php if (!is_array($htmlExport)): ?>
            <p class="note">Create an HTML export before generating PDF.</p>
        <?php elseif (!is_array($pdfExport)): ?>
            <p class="note">No PDF export yet.</p>
            <?php if ($canCreatePdfExport): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Create PDF export</button>
                </form>
            <?php endif; ?>
        <?php else: ?>
            <?php
            $displayPdf = is_array($styledPdfExport) ? $styledPdfExport : $pdfExport;
            $displayPdfIsStyled = is_array($styledPdfExport);
            $pdfChecksum = (string) ($displayPdf['checksum_sha256'] ?? '');
            $pdfShort = $pdfChecksum !== '' ? substr($pdfChecksum, 0, 12) . '…' : '—';
            $pdfSize = isset($displayPdf['file_size_bytes']) ? (int) $displayPdf['file_size_bytes'] : 0;
            ?>
            <ul class="facts">
                <li><strong>Export ID:</strong> <?= e((string) $displayPdf['id']) ?></li>
                <li><strong>Key:</strong> <code><?= e((string) ($displayPdf['export_key'] ?? '')) ?></code></li>
                <li><strong>Format / status:</strong>
                    <span class="type-badge type-badge--pdf">pdf</span>
                    · <span class="status-badge status-<?= e((string) ($displayPdf['status'] ?? '')) ?>"><?= e((string) ($displayPdf['status'] ?? '')) ?></span>
                </li>
                <li><strong>Filename:</strong> <code><?= e((string) ($displayPdf['filename'] ?? '')) ?></code></li>
                <li><strong>Checksum:</strong> <code class="checksum-display" title="<?= e($pdfChecksum) ?>"><?= e($pdfShort) ?></code></li>
                <li><strong>Size:</strong> <?= e($pdfSize > 0 ? number_format($pdfSize) . ' B' : '—') ?></li>
                <li><strong>Template:</strong>
                    <span class="template-badge<?= $displayPdfIsStyled ? ' template-badge--styled' : '' ?>">
                        <?= e($displayPdfIsStyled ? $styledTemplateLabel : $legacyTemplateLabel) ?>
                    </span>
                    <?= $displayPdfIsStyled ? ' (from styled HTML)' : ' (legacy HTML)' ?>
                </li>
            </ul>
            <p class="export-ready-note">Latest PDF shown above. Historical versions remain on the exports list.</p>
            <p>
                <a class="btn" href="<?= e(url_path('/report-exports/' . (int) $displayPdf['id'])) ?>">View export</a>
                <a class="btn btn-secondary btn-download" href="<?= e(url_path('/report-exports/' . (int) $displayPdf['id'] . '/download')) ?>">Download PDF</a>
            </p>
            <?php if ($canCreateStyledPdf && is_array($styledHtmlExport) && !is_array($styledPdfExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Create styled PDF from HTML v2</button>
                </form>
            <?php elseif ($canCreateStyledPdf && is_array($styledPdfExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Re-check styled PDF (idempotent)</button>
                </form>
            <?php endif; ?>
            <p class="field-hint export-hint">No public URL.</p>
        <?php endif; ?>
    </section>
<?php endif; ?>

<?php if ($mode === 'detail' && is_array($snapshot)): ?>
    <section class="panel">
        <h2>Source weekly references</h2>
        <?php
        $weeklyIds = $decodeIds($snapshot['source_weekly_checkpoint_ids'] ?? null);
        ?>
        <?php if ($weeklySources !== []): ?>
            <ul class="facts">
                <?php foreach ($weeklySources as $wc): ?>
                    <?php if (!is_array($wc)) {
                        continue;
                    } ?>
                    <li>
                        <a href="<?= e(url_path('/weekly-checkpoints/' . (int) ($wc['id'] ?? 0))) ?>">
                            <code><?= e((string) ($wc['checkpoint_key'] ?? ('#' . (int) ($wc['id'] ?? 0)))) ?></code>
                        </a>
                        · <span class="status-badge status-<?= e((string) ($wc['status'] ?? '')) ?>"><?= e((string) ($wc['status'] ?? '')) ?></span>
                        · <?= e((string) ($wc['title'] ?? '')) ?>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php elseif ($weeklyIds !== []): ?>
            <ul class="facts">
                <?php foreach ($weeklyIds as $wid): ?>
                    <li><a href="<?= e(url_path('/weekly-checkpoints/' . $wid)) ?>">Weekly #<?= e((string) $wid) ?></a></li>
                <?php endforeach; ?>
            </ul>
        <?php else: ?>
            <p class="note">No weekly source references stored.</p>
        <?php endif; ?>
    </section>

    <section class="panel snapshot-blocks">
        <h2>Frozen blocks (<?= e((string) count($blocks)) ?>)</h2>
        <?php if ($blocks === []): ?>
            <p class="note">No blocks in payload.</p>
        <?php else: ?>
            <?php foreach ($blocks as $block): ?>
                <?php if (!is_array($block)) {
                    continue;
                } ?>
                <article class="snapshot-block">
                    <h3><?= e((string) ($block['title'] ?? '')) ?></h3>
                    <p>
                        <code><?= e((string) ($block['block_key'] ?? '')) ?></code>
                        · <span class="type-badge"><?= e((string) ($block['block_type'] ?? '')) ?></span>
                        · <span class="status-badge status-<?= e((string) ($block['status'] ?? '')) ?>"><?= e((string) ($block['status'] ?? '')) ?></span>
                        · sort <?= e((string) ($block['sort_order'] ?? '')) ?>
                    </p>
                    <?php if (trim((string) ($block['summary'] ?? '')) !== ''): ?>
                        <p class="snapshot-block__summary"><?= e((string) $block['summary']) ?></p>
                    <?php endif; ?>
                    <?php if (trim((string) ($block['body'] ?? '')) !== ''): ?>
                        <div class="snapshot-block__body"><?= nl2br(e((string) $block['body']), false) ?></div>
                    <?php endif; ?>
                </article>
            <?php endforeach; ?>
        <?php endif; ?>
    </section>

    <?php if (!empty($snapshot['rendered_text'])): ?>
        <section class="panel">
            <h2>Rendered text</h2>
            <pre class="snapshot-rendered-text"><?= e((string) $snapshot['rendered_text']) ?></pre>
        </section>
    <?php endif; ?>
<?php endif; ?>

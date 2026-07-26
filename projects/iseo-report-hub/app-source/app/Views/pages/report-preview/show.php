<?php
declare(strict_types=1);

use Iseo\Services\ReportPreviewService;

/** @var array<string, mixed> $report */
/** @var list<array<string, mixed>> $blocks */
/** @var string $renderMode */
/** @var array<string, string> $flatFields */
/** @var bool $flatPresent */
/** @var list<array<string, mixed>> $sourceWeekly */
/** @var array<string, mixed> $diagnostics */
/** @var string $generatedAt */
/** @var bool $printMode */
/** @var array<string, mixed>|null $activeSnapshot */

$reportId = (int) $report['id'];
$periodId = (int) $report['reporting_period_id'];
$blocks = $blocks ?? [];
$flatFields = $flatFields ?? [];
$sourceWeekly = $sourceWeekly ?? [];
$diagnostics = $diagnostics ?? [];
$printMode = !empty($printMode);
$activeSnapshot = $activeSnapshot ?? null;
$flatLabels = [
    'executive_summary' => 'Executive summary',
    'work_completed' => 'Work completed',
    'results_summary' => 'Results summary',
    'key_findings' => 'Key findings',
    'risks_and_blockers' => 'Risks and blockers',
    'next_month_plan' => 'Next month plan',
    'client_notes' => 'Client notes',
    'internal_notes' => 'Internal notes',
];
?>
<article class="report-preview<?= $printMode ? ' report-preview--print' : '' ?>">
    <section class="panel report-preview__header">
        <div class="panel-head">
            <h2><?= e((string) $report['title']) ?></h2>
            <?php if (!$printMode): ?>
                <p class="report-preview__controls">
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId)) ?>">Back to monthly report</a>
                    <?php if ((string) ($report['status'] ?? '') !== 'finalized'): ?>
                        <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/edit')) ?>">Edit monthly report</a>
                        <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">Manage report blocks</a>
                    <?php else: ?>
                        <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">View report blocks</a>
                    <?php endif; ?>
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/preview/print')) ?>">Print view</a>
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/snapshot')) ?>">Snapshot</a>
                </p>
            <?php else: ?>
                <p class="report-preview__controls no-print">
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/preview')) ?>">Back to preview</a>
                    <a class="btn" href="#" onclick="window.print(); return false;">Print</a>
                </p>
            <?php endif; ?>
        </div>
        <p>
            <span class="internal-only-badge">Internal only</span>
            · <span class="status-badge status-<?= e((string) $report['status']) ?>"><?= e((string) $report['status']) ?></span>
            <?php if ((string) ($report['status'] ?? '') === 'finalized'): ?>
                · <span class="finalized-badge">Finalized</span>
            <?php else: ?>
                · <span class="draft-warning-badge">Not finalized</span>
            <?php endif; ?>
            · <code><?= e((string) ($report['period_key'] ?? '')) ?></code>
        </p>
        <ul class="facts">
            <li><strong>Client:</strong> <?= e((string) ($report['client_name'] ?? '—')) ?></li>
            <li><strong>Project:</strong> <?= e((string) ($report['project_name'] ?? '—')) ?></li>
            <li><strong>Site:</strong>
                <?php if (!empty($report['primary_site_url'])): ?>
                    <?= e((string) $report['primary_site_url']) ?>
                    <?php if (!empty($report['primary_site_label'])): ?>
                        — <?= e((string) $report['primary_site_label']) ?>
                    <?php endif; ?>
                <?php else: ?>
                    —
                <?php endif; ?>
            </li>
            <li><strong>Period:</strong>
                <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                    <code><?= e((string) ($report['period_key'] ?? '')) ?></code>
                </a>
                · <?= e((string) ($report['period_start'] ?? '')) ?> – <?= e((string) ($report['period_end'] ?? '')) ?>
            </li>
            <li><strong>Finalized at:</strong> <?= e((string) ($report['finalized_at'] ?? '—')) ?></li>
            <li><strong>Generated at:</strong> <?= e((string) $generatedAt) ?></li>
            <li><strong>Snapshot:</strong>
                <?php if (is_array($activeSnapshot)): ?>
                    <span class="immutable-badge">Active</span>
                    · <a href="<?= e(url_path('/report-snapshots/' . (int) $activeSnapshot['id'])) ?>">
                        <code><?= e((string) $activeSnapshot['snapshot_key']) ?></code>
                    </a>
                    · v<?= e((string) $activeSnapshot['version']) ?>
                <?php else: ?>
                    <span class="note">No snapshot yet</span>
                    · <a href="<?= e(url_path('/monthly-reports/' . $reportId . '/snapshot')) ?>">Open snapshot page</a>
                <?php endif; ?>
            </li>
        </ul>
        <?php if ((string) ($report['status'] ?? '') !== 'finalized'): ?>
            <p class="note draft-warning<?= $printMode ? '' : '' ?>">This preview is not finalized. Treat as working draft.</p>
        <?php endif; ?>
    </section>

    <section class="panel report-preview__sources">
        <h2>Source weekly checkpoints</h2>
        <?php if ($sourceWeekly === []): ?>
            <p class="note">No source weekly checkpoints resolved.</p>
        <?php else: ?>
            <ul class="facts report-preview__weekly-list">
                <?php foreach ($sourceWeekly as $wc): ?>
                    <li>
                        <a href="<?= e(url_path('/weekly-checkpoints/' . (int) $wc['id'])) ?>">
                            W<?= e((string) $wc['week_index']) ?>
                            · <code><?= e((string) $wc['checkpoint_key']) ?></code>
                        </a>
                        · <span class="status-badge status-<?= e((string) $wc['status']) ?>"><?= e((string) $wc['status']) ?></span>
                        · <?= e((string) $wc['title']) ?>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php endif; ?>
    </section>

    <?php if ($renderMode === 'blocks_primary'): ?>
        <section class="panel report-preview__blocks">
            <h2>Report blocks (<?= e((string) count($blocks)) ?>)</h2>
            <?php foreach ($blocks as $block): ?>
                <article class="report-preview__block" data-block-key="<?= e((string) $block['block_key']) ?>" data-sort-order="<?= e((string) $block['sort_order']) ?>">
                    <header class="report-preview__block-head">
                        <h3><?= e((string) $block['title']) ?></h3>
                        <p>
                            <code><?= e((string) $block['block_key']) ?></code>
                            · <span class="type-badge"><?= e((string) $block['block_type']) ?></span>
                            · <span class="status-badge status-<?= e((string) $block['status']) ?>"><?= e((string) $block['status']) ?></span>
                            · sort <?= e((string) $block['sort_order']) ?>
                        </p>
                    </header>
                    <?php
                    $summary = trim((string) ($block['summary'] ?? ''));
                    $body = trim((string) ($block['body'] ?? ''));
                    ?>
                    <?php if ($summary !== ''): ?>
                        <div class="report-preview__summary">
                            <h4>Summary</h4>
                            <div class="report-preview__text"><?= ReportPreviewService::safeMultiline($summary) ?></div>
                        </div>
                    <?php endif; ?>
                    <?php if ($body !== ''): ?>
                        <div class="report-preview__body">
                            <h4>Body</h4>
                            <div class="report-preview__text"><?= ReportPreviewService::safeMultiline($body) ?></div>
                        </div>
                    <?php elseif ($summary === ''): ?>
                        <p class="note">No body or summary content for this block.</p>
                    <?php endif; ?>
                    <?php
                    $blockSources = $block['_source_rows'] ?? [];
                    if (is_array($blockSources) && $blockSources !== []):
                    ?>
                        <p class="report-preview__block-sources">
                            <strong>Sources:</strong>
                            <?php foreach ($blockSources as $i => $wc): ?>
                                <?php if ($i > 0): ?> · <?php endif; ?>
                                <a href="<?= e(url_path('/weekly-checkpoints/' . (int) $wc['id'])) ?>">
                                    W<?= e((string) $wc['week_index']) ?>
                                </a>
                            <?php endforeach; ?>
                        </p>
                    <?php endif; ?>
                    <?php if (!empty($block['_has_metric_refs']) || !empty($block['_has_data_json'])): ?>
                        <details class="report-preview__block-diag">
                            <summary>Block diagnostics (metric refs / data_json)</summary>
                            <?php if (!empty($block['_has_metric_refs'])): ?>
                                <p><strong>source_metric_refs</strong></p>
                                <pre class="json-preview"><?= e((string) ($block['source_metric_refs'] ?? '')) ?></pre>
                            <?php endif; ?>
                            <?php if (!empty($block['_has_data_json'])): ?>
                                <p><strong>data_json</strong></p>
                                <pre class="json-preview"><?= e((string) ($block['data_json'] ?? '')) ?></pre>
                            <?php endif; ?>
                        </details>
                    <?php endif; ?>
                </article>
            <?php endforeach; ?>
        </section>
    <?php elseif ($renderMode === 'flat_fallback'): ?>
        <section class="panel report-preview__flat-fallback">
            <h2>Flat content (DB-05 fallback)</h2>
            <?php foreach ($flatLabels as $key => $label): ?>
                <?php $value = (string) ($flatFields[$key] ?? ''); ?>
                <?php if ($value !== ''): ?>
                    <article class="report-preview__flat-section">
                        <h3><?= e($label) ?></h3>
                        <div class="report-preview__text"><?= ReportPreviewService::safeMultiline($value) ?></div>
                    </article>
                <?php endif; ?>
            <?php endforeach; ?>
        </section>
    <?php else: ?>
        <section class="panel report-preview__empty">
            <h2>Empty report</h2>
            <p class="note">No non-archived report blocks and no DB-05 flat content available.</p>
        </section>
    <?php endif; ?>

    <section class="panel report-preview__diagnostics<?= $printMode ? ' no-print' : '' ?>">
        <h2>Internal diagnostics</h2>
        <ul class="facts">
            <li><strong>Render mode:</strong> <code><?= e((string) ($diagnostics['render_mode'] ?? $renderMode)) ?></code></li>
            <li><strong>Block count:</strong> <?= e((string) ($diagnostics['block_count'] ?? count($blocks))) ?></li>
            <li><strong>Archived excluded:</strong> <?= e((string) ($diagnostics['archived_excluded_count'] ?? 0)) ?></li>
            <li><strong>Flat DB-05 fallback available:</strong> <?= !empty($diagnostics['flat_fallback_available']) || $flatPresent ? 'yes' : 'no' ?></li>
            <li><strong>Flat fallback active:</strong> <?= !empty($diagnostics['flat_fallback_active']) ? 'yes' : 'no' ?></li>
            <li><strong>Source weekly IDs:</strong>
                <?php
                $ids = $diagnostics['source_weekly_ids'] ?? [];
                echo e(is_array($ids) && $ids !== [] ? implode(', ', array_map('strval', $ids)) : '—');
                ?>
            </li>
            <li><strong>Missing weekly IDs:</strong>
                <?php
                $missing = $diagnostics['missing_weekly_ids'] ?? [];
                echo e(is_array($missing) && $missing !== [] ? implode(', ', array_map('strval', $missing)) : 'none');
                ?>
            </li>
            <li><strong>Metric refs placeholder:</strong> <?= !empty($diagnostics['metric_refs_present']) ? 'present' : 'none' ?></li>
            <li><strong>Generated at:</strong> <?= e((string) ($diagnostics['generated_at'] ?? $generatedAt)) ?></li>
        </ul>

        <?php if ($renderMode === 'blocks_primary' && $flatPresent): ?>
            <details class="report-preview__legacy-flat">
                <summary>Legacy DB-05 flat fields (diagnostics only)</summary>
                <?php foreach ($flatLabels as $key => $label): ?>
                    <?php $value = (string) ($flatFields[$key] ?? ''); ?>
                    <?php if ($value !== ''): ?>
                        <p><strong><?= e($label) ?></strong></p>
                        <div class="report-preview__text"><?= ReportPreviewService::safeMultiline($value) ?></div>
                    <?php endif; ?>
                <?php endforeach; ?>
            </details>
        <?php endif; ?>
    </section>
</article>

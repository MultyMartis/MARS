<?php
declare(strict_types=1);
/** @var array<string, mixed> $block */
/** @var array<string, mixed>|null $monthly */
/** @var list<array<string, mixed>> $sourceCheckpoints */
/** @var bool $canEdit */
$monthlyId = (int) $block['monthly_report_content_id'];
$periodId = (int) $block['reporting_period_id'];
$sourceCheckpoints = $sourceCheckpoints ?? [];
$parentFinalized = !empty($parentFinalized);
?>
<section class="panel">
    <div class="panel-head">
        <h2>Block <code><?= e((string) $block['block_key']) ?></code></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/blocks')) ?>">Back to blocks</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Parent monthly report</a>
            <?php if ($canEdit): ?>
                <a class="btn" href="<?= e(url_path('/report-blocks/' . (int) $block['id'] . '/edit')) ?>">Edit</a>
            <?php endif; ?>
        </p>
    </div>
    <p>
        <span class="status-badge status-<?= e((string) $block['status']) ?>"><?= e((string) $block['status']) ?></span>
        · <span class="type-badge"><?= e((string) $block['block_type']) ?></span>
        · sort <?= e((string) $block['sort_order']) ?>
        <?php if ($parentFinalized): ?>
            · <span class="finalized-badge">Parent finalized</span>
        <?php endif; ?>
    </p>
</section>

<?php if ($parentFinalized): ?>
    <section class="panel locked-notice">
        <h2>Locked</h2>
        <p>Parent monthly report is finalized. Editing this block is blocked until reopen.</p>
    </section>
<?php endif; ?>

<section class="panel">
    <h2>Parent context</h2>
    <ul class="facts">
        <li><strong>Monthly report:</strong>
            <a href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">
                <?= e((string) ($block['monthly_title'] ?? ('#' . $monthlyId))) ?>
            </a>
            · <span class="status-badge status-<?= e((string) ($block['monthly_status'] ?? '')) ?>"><?= e((string) ($block['monthly_status'] ?? '')) ?></span>
        </li>
        <li><strong>Period:</strong>
            <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                <code><?= e((string) ($block['period_key'] ?? '')) ?></code>
            </a>
            · <span class="status-badge status-<?= e((string) ($block['period_status'] ?? '')) ?>"><?= e((string) ($block['period_status'] ?? '')) ?></span>
        </li>
        <li><strong>Project:</strong> <?= e((string) ($block['project_name'] ?? '—')) ?></li>
        <li><strong>Client:</strong> <?= e((string) ($block['client_name'] ?? '—')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Details</h2>
    <ul class="facts">
        <li><strong>ID:</strong> <?= e((string) $block['id']) ?></li>
        <li><strong>Key:</strong> <code><?= e((string) $block['block_key']) ?></code></li>
        <li><strong>Type:</strong> <span class="type-badge"><?= e((string) $block['block_type']) ?></span></li>
        <li><strong>Sort order:</strong> <?= e((string) $block['sort_order']) ?></li>
        <li><strong>Title:</strong> <?= e((string) $block['title']) ?></li>
        <li><strong>Reviewed at:</strong> <?= e((string) ($block['reviewed_at'] ?? '—')) ?></li>
        <li><strong>Approved at:</strong> <?= e((string) ($block['approved_at'] ?? '—')) ?></li>
        <li><strong>Owner:</strong> <?= e((string) ($block['owner_name'] ?? '—')) ?><?php if (!empty($block['owner_email'])): ?> · <?= e((string) $block['owner_email']) ?><?php endif; ?></li>
        <li><strong>Reviewer:</strong> <?= e((string) ($block['reviewer_name'] ?? '—')) ?><?php if (!empty($block['reviewer_email'])): ?> · <?= e((string) $block['reviewer_email']) ?><?php endif; ?></li>
        <li><strong>Created by:</strong> <?= e((string) ($block['created_by_name'] ?? '—')) ?> · <?= e((string) ($block['created_at'] ?? '')) ?></li>
        <li><strong>Updated by:</strong> <?= e((string) ($block['updated_by_name'] ?? '—')) ?> · <?= e((string) ($block['updated_at'] ?? '')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Source weekly checkpoints</h2>
    <?php if ($sourceCheckpoints === []): ?>
        <p class="note">No source weekly checkpoints linked.</p>
    <?php else: ?>
        <ul class="facts">
            <?php foreach ($sourceCheckpoints as $wc): ?>
                <li>
                    <a href="<?= e(url_path('/weekly-checkpoints/' . (int) $wc['id'])) ?>">
                        <code><?= e((string) $wc['checkpoint_key']) ?></code>
                    </a>
                    · <span class="status-badge status-<?= e((string) $wc['status']) ?>"><?= e((string) $wc['status']) ?></span>
                    · <?= e((string) $wc['title']) ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</section>

<section class="panel">
    <h2>Content</h2>
    <ul class="facts">
        <li><strong>Summary:</strong> <?= e((string) ($block['summary'] ?? '—')) ?></li>
        <li><strong>Body:</strong> <?= e((string) ($block['body'] ?? '—')) ?></li>
        <li><strong>data_json:</strong> <pre class="json-preview"><?= e((string) ($block['data_json'] ?? '—')) ?></pre></li>
        <li><strong>source_metric_refs:</strong> <pre class="json-preview"><?= e((string) ($block['source_metric_refs'] ?? '—')) ?></pre></li>
    </ul>
</section>

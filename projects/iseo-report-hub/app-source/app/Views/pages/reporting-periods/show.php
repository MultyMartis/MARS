<?php
declare(strict_types=1);
/** @var array<string, mixed> $period */
/** @var bool $canEdit */
?>
<section class="panel">
    <div class="panel-head">
        <h2>Reporting period <?= e((string) $period['period_key']) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods')) ?>">Back to list</a>
            <?php if ($canEdit): ?>
                <a class="btn" href="<?= e(url_path('/reporting-periods/' . (int) $period['id'] . '/edit')) ?>">Edit</a>
            <?php endif; ?>
        </p>
    </div>
    <p>
        <span class="status-badge status-<?= e((string) $period['status']) ?>"><?= e((string) $period['status']) ?></span>
    </p>
</section>

<section class="panel">
    <h2>Details</h2>
    <ul class="facts">
        <li><strong>ID:</strong> <?= e((string) $period['id']) ?></li>
        <li><strong>Period key:</strong> <code><?= e((string) $period['period_key']) ?></code></li>
        <li><strong>Title:</strong> <?= e((string) ($period['title'] ?? '—')) ?></li>
        <li><strong>Summary:</strong> <?= e((string) ($period['summary'] ?? '—')) ?></li>
        <li><strong>Dates:</strong> <?= e((string) $period['period_start']) ?> – <?= e((string) $period['period_end']) ?></li>
        <li><strong>Finalized at:</strong> <?= e((string) ($period['finalized_at'] ?? '—')) ?></li>
        <li><strong>Project:</strong> <?= e((string) $period['project_name']) ?> (<code><?= e((string) $period['project_slug']) ?></code>, id <?= e((string) $period['project_id']) ?>)</li>
        <li><strong>Client:</strong> <?= e((string) $period['client_name']) ?> (<code><?= e((string) $period['client_slug']) ?></code>)</li>
        <li><strong>Primary site:</strong> <?= e((string) ($period['primary_site_url'] ?? '—')) ?><?php if (!empty($period['primary_site_label'])): ?> — <?= e((string) $period['primary_site_label']) ?><?php endif; ?></li>
        <li><strong>Owner:</strong> <?= e((string) ($period['owner_name'] ?? '—')) ?><?php if (!empty($period['owner_email'])): ?> · <?= e((string) $period['owner_email']) ?><?php endif; ?></li>
        <li><strong>Reviewer:</strong> <?= e((string) ($period['reviewer_name'] ?? '—')) ?><?php if (!empty($period['reviewer_email'])): ?> · <?= e((string) $period['reviewer_email']) ?><?php endif; ?></li>
        <li><strong>Created by:</strong> <?= e((string) ($period['created_by_name'] ?? '—')) ?> · <?= e((string) ($period['created_at'] ?? '')) ?></li>
        <li><strong>Updated by:</strong> <?= e((string) ($period['updated_by_name'] ?? '—')) ?> · <?= e((string) ($period['updated_at'] ?? '')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Content scope</h2>
    <p class="note">Weekly checkpoints / monthly report content: not implemented.</p>
</section>

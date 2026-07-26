<?php
declare(strict_types=1);
/** @var array<string, mixed> $checkpoint */
/** @var array<string, mixed>|null $period */
/** @var bool $canEdit */
$periodId = (int) $checkpoint['reporting_period_id'];
?>
<section class="panel">
    <div class="panel-head">
        <h2>Checkpoint <?= e((string) $checkpoint['checkpoint_key']) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Back to list</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">Parent period</a>
            <?php if ($canEdit): ?>
                <a class="btn" href="<?= e(url_path('/weekly-checkpoints/' . (int) $checkpoint['id'] . '/edit')) ?>">Edit</a>
            <?php endif; ?>
        </p>
    </div>
    <p>
        <span class="status-badge status-<?= e((string) $checkpoint['status']) ?>"><?= e((string) $checkpoint['status']) ?></span>
    </p>
</section>

<section class="panel">
    <h2>Parent period</h2>
    <ul class="facts">
        <li><strong>Period:</strong>
            <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                <code><?= e((string) ($checkpoint['period_key'] ?? '')) ?></code>
            </a>
            · <span class="status-badge status-<?= e((string) ($checkpoint['period_status'] ?? '')) ?>"><?= e((string) ($checkpoint['period_status'] ?? '')) ?></span>
        </li>
        <li><strong>Project:</strong> <?= e((string) ($checkpoint['project_name'] ?? '—')) ?></li>
        <li><strong>Client:</strong> <?= e((string) ($checkpoint['client_name'] ?? '—')) ?></li>
        <li><strong>Period dates:</strong> <?= e((string) ($checkpoint['period_start'] ?? '')) ?> – <?= e((string) ($checkpoint['period_end'] ?? '')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Details</h2>
    <ul class="facts">
        <li><strong>ID:</strong> <?= e((string) $checkpoint['id']) ?></li>
        <li><strong>Week:</strong> W<?= e((string) $checkpoint['week_index']) ?></li>
        <li><strong>Key:</strong> <code><?= e((string) $checkpoint['checkpoint_key']) ?></code></li>
        <li><strong>Title:</strong> <?= e((string) $checkpoint['title']) ?></li>
        <li><strong>Dates:</strong> <?= e((string) $checkpoint['checkpoint_start']) ?> – <?= e((string) $checkpoint['checkpoint_end']) ?></li>
        <li><strong>Reviewed at:</strong> <?= e((string) ($checkpoint['reviewed_at'] ?? '—')) ?></li>
        <li><strong>Completed at:</strong> <?= e((string) ($checkpoint['completed_at'] ?? '—')) ?></li>
        <li><strong>Owner:</strong> <?= e((string) ($checkpoint['owner_name'] ?? '—')) ?><?php if (!empty($checkpoint['owner_email'])): ?> · <?= e((string) $checkpoint['owner_email']) ?><?php endif; ?></li>
        <li><strong>Reviewer:</strong> <?= e((string) ($checkpoint['reviewer_name'] ?? '—')) ?><?php if (!empty($checkpoint['reviewer_email'])): ?> · <?= e((string) $checkpoint['reviewer_email']) ?><?php endif; ?></li>
        <li><strong>Created by:</strong> <?= e((string) ($checkpoint['created_by_name'] ?? '—')) ?> · <?= e((string) ($checkpoint['created_at'] ?? '')) ?></li>
        <li><strong>Updated by:</strong> <?= e((string) ($checkpoint['updated_by_name'] ?? '—')) ?> · <?= e((string) ($checkpoint['updated_at'] ?? '')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Notes</h2>
    <ul class="facts">
        <li><strong>Summary:</strong> <?= e((string) ($checkpoint['summary'] ?? '—')) ?></li>
        <li><strong>Work done:</strong> <?= e((string) ($checkpoint['work_done'] ?? '—')) ?></li>
        <li><strong>Findings:</strong> <?= e((string) ($checkpoint['findings'] ?? '—')) ?></li>
        <li><strong>Next steps:</strong> <?= e((string) ($checkpoint['next_steps'] ?? '—')) ?></li>
        <li><strong>Risks:</strong> <?= e((string) ($checkpoint['risks'] ?? '—')) ?></li>
    </ul>
</section>

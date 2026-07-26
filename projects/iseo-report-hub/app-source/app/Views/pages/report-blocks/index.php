<?php
declare(strict_types=1);
/** @var array<string, mixed> $monthly */
/** @var list<array<string, mixed>> $blocks */
/** @var bool $canCreate */
$monthlyId = (int) $monthly['id'];
$periodId = (int) $monthly['reporting_period_id'];
?>
<section class="panel">
    <div class="panel-head">
        <h2>Report blocks — <?= e((string) ($monthly['period_key'] ?? '')) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Parent monthly report</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">Parent period</a>
            <?php if ($canCreate): ?>
                <a class="btn" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/blocks/create')) ?>">Create block</a>
            <?php endif; ?>
        </p>
    </div>
    <p class="note">
        Monthly: <strong><?= e((string) ($monthly['title'] ?? '')) ?></strong>
        · <span class="status-badge status-<?= e((string) ($monthly['status'] ?? '')) ?>"><?= e((string) ($monthly['status'] ?? '')) ?></span>
        · <?= e((string) ($monthly['project_name'] ?? '')) ?> / <?= e((string) ($monthly['client_name'] ?? '')) ?>
        · No hard delete — archive via status.
    </p>
</section>

<?php if ($blocks === []): ?>
    <section class="panel">
        <p>No report blocks for this monthly report yet.</p>
        <?php if ($canCreate): ?>
            <p><a class="btn" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/blocks/create')) ?>">Create the first block</a></p>
        <?php endif; ?>
    </section>
<?php else: ?>
    <section class="panel table-wrap">
        <table class="data-table">
            <thead>
            <tr>
                <th>Sort</th>
                <th>Key</th>
                <th>Type</th>
                <th>Title</th>
                <th>Status</th>
                <th>Updated</th>
                <th>Actions</th>
            </tr>
            </thead>
            <tbody>
            <?php foreach ($blocks as $row): ?>
                <?php
                $id = (int) $row['id'];
                $status = (string) $row['status'];
                $canEditRow = !empty($row['_can_edit']);
                ?>
                <tr>
                    <td><?= e((string) $row['sort_order']) ?></td>
                    <td><code><?= e((string) $row['block_key']) ?></code></td>
                    <td><span class="type-badge"><?= e((string) $row['block_type']) ?></span></td>
                    <td><?= e((string) $row['title']) ?></td>
                    <td><span class="status-badge status-<?= e($status) ?>"><?= e($status) ?></span></td>
                    <td><?= e((string) ($row['updated_at'] ?? '')) ?></td>
                    <td class="actions">
                        <a href="<?= e(url_path('/report-blocks/' . $id)) ?>">View</a>
                        <?php if ($canEditRow): ?>
                            · <a href="<?= e(url_path('/report-blocks/' . $id . '/edit')) ?>">Edit</a>
                        <?php endif; ?>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
<?php endif; ?>

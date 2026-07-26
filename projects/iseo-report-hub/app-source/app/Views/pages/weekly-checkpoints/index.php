<?php
declare(strict_types=1);
/** @var array<string, mixed> $period */
/** @var list<array<string, mixed>> $checkpoints */
/** @var bool $canCreate */
$periodId = (int) $period['id'];
?>
<section class="panel">
    <div class="panel-head">
        <h2>Weekly checkpoints — <?= e((string) $period['period_key']) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">Parent period</a>
            <?php if ($canCreate): ?>
                <a class="btn" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints/create')) ?>">Create checkpoint</a>
            <?php endif; ?>
        </p>
    </div>
    <p class="note">
        Parent: <strong><?= e((string) ($period['title'] ?? $period['period_key'])) ?></strong>
        · <?= e((string) $period['project_name']) ?> / <?= e((string) $period['client_name']) ?>
        · <span class="status-badge status-<?= e((string) $period['status']) ?>"><?= e((string) $period['status']) ?></span>
        · <?= e((string) $period['period_start']) ?> – <?= e((string) $period['period_end']) ?>
    </p>
</section>

<?php if ($checkpoints === []): ?>
    <section class="panel">
        <p>No weekly checkpoints for this period yet.</p>
        <?php if ($canCreate): ?>
            <p><a class="btn" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints/create')) ?>">Create the first checkpoint</a></p>
        <?php endif; ?>
    </section>
<?php else: ?>
    <section class="panel table-wrap">
        <table class="data-table">
            <thead>
            <tr>
                <th>Week</th>
                <th>Key</th>
                <th>Title</th>
                <th>Status</th>
                <th>Dates</th>
                <th>Owner</th>
                <th>Updated</th>
                <th>Actions</th>
            </tr>
            </thead>
            <tbody>
            <?php foreach ($checkpoints as $row): ?>
                <?php
                $id = (int) $row['id'];
                $status = (string) $row['status'];
                $owner = trim((string) ($row['owner_name'] ?? ''));
                if ($owner === '') {
                    $owner = '—';
                }
                $canEditRow = !empty($row['_can_edit']);
                ?>
                <tr>
                    <td>W<?= e((string) $row['week_index']) ?></td>
                    <td><code><?= e((string) $row['checkpoint_key']) ?></code></td>
                    <td><?= e((string) $row['title']) ?></td>
                    <td><span class="status-badge status-<?= e($status) ?>"><?= e($status) ?></span></td>
                    <td><?= e((string) $row['checkpoint_start']) ?> – <?= e((string) $row['checkpoint_end']) ?></td>
                    <td><?= e($owner) ?></td>
                    <td><?= e((string) ($row['updated_at'] ?? '')) ?></td>
                    <td class="actions">
                        <a href="<?= e(url_path('/weekly-checkpoints/' . $id)) ?>">View</a>
                        <?php if ($canEditRow): ?>
                            · <a href="<?= e(url_path('/weekly-checkpoints/' . $id . '/edit')) ?>">Edit</a>
                        <?php endif; ?>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
<?php endif; ?>

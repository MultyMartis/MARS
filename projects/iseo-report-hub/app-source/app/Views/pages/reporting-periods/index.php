<?php
declare(strict_types=1);
/** @var list<array<string, mixed>> $periods */
/** @var bool $canCreate */
?>
<section class="panel">
    <div class="panel-head">
        <h2>Reporting periods</h2>
        <?php if ($canCreate): ?>
            <a class="btn" href="<?= e(url_path('/reporting-periods/create')) ?>">Create period</a>
        <?php endif; ?>
    </div>
    <p class="note">Internal monthly shells only. No report content editor in this MVP.</p>
</section>

<?php if ($periods === []): ?>
    <section class="panel">
        <p>No reporting periods yet.</p>
        <?php if ($canCreate): ?>
            <p><a class="btn" href="<?= e(url_path('/reporting-periods/create')) ?>">Create the first period</a></p>
        <?php endif; ?>
    </section>
<?php else: ?>
    <section class="panel table-wrap">
        <table class="data-table">
            <thead>
            <tr>
                <th>ID</th>
                <th>Period</th>
                <th>Title</th>
                <th>Project</th>
                <th>Client</th>
                <th>Dates</th>
                <th>Status</th>
                <th>Owner</th>
                <th>Actions</th>
            </tr>
            </thead>
            <tbody>
            <?php foreach ($periods as $row): ?>
                <?php
                $id = (int) $row['id'];
                $status = (string) $row['status'];
                $title = trim((string) ($row['title'] ?? ''));
                if ($title === '') {
                    $title = (string) $row['period_key'];
                }
                $owner = trim((string) ($row['owner_name'] ?? ''));
                if ($owner === '') {
                    $owner = '—';
                }
                $canEditRow = !empty($row['_can_edit']);
                ?>
                <tr>
                    <td><?= e((string) $id) ?></td>
                    <td><code><?= e((string) $row['period_key']) ?></code></td>
                    <td><?= e($title) ?></td>
                    <td><?= e((string) $row['project_name']) ?></td>
                    <td><?= e((string) $row['client_name']) ?></td>
                    <td><?= e((string) $row['period_start']) ?> – <?= e((string) $row['period_end']) ?></td>
                    <td><span class="status-badge status-<?= e($status) ?>"><?= e($status) ?></span></td>
                    <td><?= e($owner) ?></td>
                    <td class="actions">
                        <a href="<?= e(url_path('/reporting-periods/' . $id)) ?>">View</a>
                        <?php if ($canEditRow): ?>
                            · <a href="<?= e(url_path('/reporting-periods/' . $id . '/edit')) ?>">Edit</a>
                        <?php endif; ?>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
<?php endif; ?>

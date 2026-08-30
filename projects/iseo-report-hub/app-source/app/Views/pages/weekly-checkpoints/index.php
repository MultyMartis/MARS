<?php
declare(strict_types=1);
/** @var array<string, mixed> $period */
/** @var list<array<string, mixed>> $checkpoints */
/** @var bool $canCreate */
$periodId = (int) $period['id'];
?>
<section class="panel">
    <div class="panel-head">
        <h2>Еженедельные заметки — <?= e((string) $period['period_key']) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">Родительский период</a>
            <?php if ($canCreate): ?>
                <a class="btn" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints/create')) ?>">Создать заметку</a>
            <?php endif; ?>
        </p>
    </div>
    <p class="note">
        Родитель: <strong><?= e((string) ($period['title'] ?? $period['period_key'])) ?></strong>
        · <?= e((string) $period['project_name']) ?> / <?= e((string) $period['client_name']) ?>
        · <span class="status-badge status-<?= e((string) $period['status']) ?>"><?= e(ui_status_label((string) $period['status'])) ?></span>
        · <?= e((string) $period['period_start']) ?> – <?= e((string) $period['period_end']) ?>
    </p>
</section>

<?php if ($checkpoints === []): ?>
    <section class="panel">
        <p>Еженедельных заметок для этого периода пока нет.</p>
        <?php if ($canCreate): ?>
            <p><a class="btn" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints/create')) ?>">Создать первую заметку</a></p>
        <?php endif; ?>
    </section>
<?php else: ?>
    <section class="panel table-wrap">
        <table class="data-table">
            <thead>
            <tr>
                <th>Неделя</th>
                <th>Ключ</th>
                <th>Название</th>
                <th>Статус</th>
                <th>Даты</th>
                <th>Ответственный</th>
                <th>Обновлено</th>
                <th>Действия</th>
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
                } else {
                    $owner = ui_display_user_name($row['owner_name'] ?? null, $row['owner_email'] ?? null);
                }
                $canEditRow = !empty($row['_can_edit']);
                ?>
                <tr>
                    <td>W<?= e((string) $row['week_index']) ?></td>
                    <td><code><?= e((string) $row['checkpoint_key']) ?></code></td>
                    <td><?= e((string) $row['title']) ?></td>
                    <td><span class="status-badge status-<?= e($status) ?>"><?= e(ui_status_label($status)) ?></span></td>
                    <td><?= e((string) $row['checkpoint_start']) ?> – <?= e((string) $row['checkpoint_end']) ?></td>
                    <td><?= e($owner) ?></td>
                    <td><?= e((string) ($row['updated_at'] ?? '')) ?></td>
                    <td class="actions">
                        <a href="<?= e(url_path('/weekly-checkpoints/' . $id)) ?>">Открыть</a>
                        <?php if ($canEditRow): ?>
                            · <a href="<?= e(url_path('/weekly-checkpoints/' . $id . '/edit')) ?>">Изменить</a>
                        <?php endif; ?>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
<?php endif; ?>

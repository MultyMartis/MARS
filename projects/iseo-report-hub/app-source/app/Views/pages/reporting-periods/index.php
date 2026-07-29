<?php
declare(strict_types=1);
/** @var list<array<string, mixed>> $periods */
/** @var bool $canCreate */
?>
<section class="panel">
    <div class="panel-head">
        <h2>Отчетные периоды</h2>
        <?php if ($canCreate): ?>
            <a class="btn" href="<?= e(url_path('/reporting-periods/create')) ?>">Создать период</a>
        <?php endif; ?>
    </div>
    <p class="note">Список месяцев для работы с отчетами. Откройте период, чтобы перейти к отчету и файлам.</p>
</section>

<?php if ($periods === []): ?>
    <section class="panel">
        <p>Отчетных периодов пока нет.</p>
        <?php if ($canCreate): ?>
            <p><a class="btn" href="<?= e(url_path('/reporting-periods/create')) ?>">Создать первый период</a></p>
        <?php endif; ?>
    </section>
<?php else: ?>
    <section class="panel table-wrap">
        <table class="data-table">
            <thead>
            <tr>
                <th>ID</th>
                <th>Период</th>
                <th>Название</th>
                <th>Проект</th>
                <th>Клиент</th>
                <th>Даты</th>
                <th>Статус</th>
                <th>Ответственный</th>
                <th>Действия</th>
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
                $statusRu = match ($status) {
                    'active' => 'Активен',
                    'draft' => 'Черновик',
                    'archived' => 'В архиве',
                    'closed' => 'Закрыт',
                    default => $status,
                };
                ?>
                <tr>
                    <td><?= e((string) $id) ?></td>
                    <td><code><?= e((string) $row['period_key']) ?></code></td>
                    <td><?= e($title) ?></td>
                    <td><?= e((string) $row['project_name']) ?></td>
                    <td><?= e((string) $row['client_name']) ?></td>
                    <td><?= e((string) $row['period_start']) ?> – <?= e((string) $row['period_end']) ?></td>
                    <td><span class="status-badge status-<?= e($status) ?>"><?= e($statusRu) ?></span></td>
                    <td><?= e($owner) ?></td>
                    <td class="actions">
                        <a href="<?= e(url_path('/reporting-periods/' . $id)) ?>">Открыть</a>
                        <?php if ($canEditRow): ?>
                            · <a href="<?= e(url_path('/reporting-periods/' . $id . '/edit')) ?>">Изменить</a>
                        <?php endif; ?>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
<?php endif; ?>

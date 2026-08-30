<?php
declare(strict_types=1);
/** @var array<string, mixed> $monthly */
/** @var list<array<string, mixed>> $blocks */
/** @var bool $canCreate */
$monthlyId = (int) $monthly['id'];
$periodId = (int) $monthly['reporting_period_id'];
$parentFinalized = !empty($parentFinalized) || ((string) ($monthly['status'] ?? '') === 'finalized');
?>
<section class="panel">
    <div class="panel-head">
        <h2>Блоки отчета — <?= e((string) ($monthly['period_key'] ?? '')) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">К месячному отчету</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">К периоду</a>
            <?php if ($canCreate): ?>
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/blocks/create')) ?>">Создать блок</a>
            <?php endif; ?>
        </p>
    </div>
    <p class="note">
        Месячный отчет: <strong><?= e((string) ($monthly['title'] ?? '')) ?></strong>
        · <span class="status-badge status-<?= e((string) ($monthly['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($monthly['status'] ?? ''))) ?></span>
        · <?= e((string) ($monthly['project_name'] ?? '')) ?> / <?= e((string) ($monthly['client_name'] ?? '')) ?>
        · Удаление недоступно — архивируйте через статус.
    </p>
</section>

<?php if ($parentFinalized): ?>
    <section class="panel locked-notice">
        <h2>Заблокировано</h2>
        <p>Месячный отчет финализирован. Создание и изменение блоков недоступны до повторного открытия. Список и карточки остаются только для чтения.</p>
    </section>
<?php endif; ?>
<?php if ($blocks === []): ?>
    <section class="panel">
        <p>Блоков отчета для этого месячного отчета пока нет.</p>
        <?php if ($canCreate): ?>
            <p><a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/blocks/create')) ?>">Создать первый блок</a></p>
        <?php endif; ?>
    </section>
<?php else: ?>
    <section class="panel table-wrap">
        <table class="data-table">
            <thead>
            <tr>
                <th>Порядок</th>
                <th>Раздел</th>
                <th>Тип</th>
                <th>Название</th>
                <th>Статус</th>
                <th>Обновлено</th>
                <th>Действия</th>
            </tr>
            </thead>
            <tbody>
            <?php foreach ($blocks as $row): ?>
                <?php
                $id = (int) $row['id'];
                $status = (string) $row['status'];
                $canEditRow = !empty($row['_can_edit']);
                $blockKey = (string) $row['block_key'];
                ?>
                <tr>
                    <td><?= e((string) $row['sort_order']) ?></td>
                    <td>
                        <?= e(ui_block_label($blockKey)) ?>
                        <div class="tech-muted"><code><?= e($blockKey) ?></code></div>
                    </td>
                    <td><span class="type-badge"><?= e(ui_block_label((string) $row['block_type'])) ?></span></td>
                    <td><?= e((string) $row['title']) ?></td>
                    <td><span class="status-badge status-<?= e($status) ?>"><?= e(ui_status_label($status)) ?></span></td>
                    <td><?= e((string) ($row['updated_at'] ?? '')) ?></td>
                    <td class="actions">
                        <a href="<?= e(url_path('/report-blocks/' . $id)) ?>">Открыть</a>
                        <?php if ($canEditRow): ?>
                            · <a href="<?= e(url_path('/report-blocks/' . $id . '/edit')) ?>">Изменить</a>
                        <?php endif; ?>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </section>
<?php endif; ?>

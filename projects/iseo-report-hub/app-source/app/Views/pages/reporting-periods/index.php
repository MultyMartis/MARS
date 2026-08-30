<?php
declare(strict_types=1);
/** @var list<array<string, mixed>> $periods */
/** @var bool $canCreate */
?>
<section class="mb-24">
    <div class="section-heading section-title">
        <span class="section-number">01</span>
        <div class="section-heading__text">
            <h2>Отчетные периоды</h2>
            <p>Список месяцев для работы с отчетами. Откройте период, чтобы посмотреть отчет и работы за месяц. Файлы и публичные ссылки будут подключены позже.</p>
        </div>
    </div>

    <div class="card panel">
        <div class="card__body panel-head">
            <p class="note" style="margin:0"><?= e(\Iseo\Support\UiLabels::fixtureBadge()) ?> · не продакшен</p>
            <?php if ($canCreate): ?>
                <a class="btn btn-primary" href="<?= e(url_path('/reporting-periods/create')) ?>">Создать период</a>
            <?php endif; ?>
        </div>
    </div>
</section>

<?php if ($periods === []): ?>
    <section class="card panel">
        <div class="card__body">
            <p>Отчетных периодов пока нет.</p>
            <?php if ($canCreate): ?>
                <p class="action-row"><a class="btn btn-primary" href="<?= e(url_path('/reporting-periods/create')) ?>">Создать первый период</a></p>
            <?php endif; ?>
        </div>
    </section>
<?php else: ?>
    <section class="card panel table-wrap">
        <div class="card__body">
            <table class="data-table table periods-table">
                <thead>
                <tr>
                    <th class="cell-nowrap">ID</th>
                    <th class="cell-nowrap">Период</th>
                    <th>Название</th>
                    <th>Проект</th>
                    <th>Клиент</th>
                    <th class="cell-nowrap">Даты</th>
                    <th class="cell-nowrap">Статус</th>
                    <th class="cell-nowrap">Месячный отчет</th>
                    <th>Ответственный</th>
                    <th class="cell-nowrap">Действия</th>
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
                    $title = ui_display_label($title, (string) $row['period_key']);
                    $projectName = ui_display_label((string) ($row['project_name'] ?? ''), '—');
                    $clientName = ui_display_label((string) ($row['client_name'] ?? ''), '—');
                    $owner = ui_display_user_name(
                        trim((string) ($row['owner_name'] ?? '')) !== '' ? (string) $row['owner_name'] : null,
                        null
                    );
                    if ($owner === 'Пользователь') {
                        $owner = '—';
                    }
                    $canEditRow = !empty($row['_can_edit']);
                    $monthlyEmptyDraft = !empty($row['_monthly_empty_draft']);
                    $monthlyDemotion = trim((string) ($row['_monthly_demotion_label'] ?? ''));
                    $monthlyStatus = (string) ($row['_monthly_status'] ?? '');
                    $monthlyStatusLabel = trim((string) ($row['_monthly_status_label'] ?? ''));
                    $monthlyId = (int) ($row['_monthly_id'] ?? 0);
                    $statusRu = ui_status_label($status);
                    ?>
                    <tr<?= $monthlyEmptyDraft ? ' class="period-row--empty-draft"' : '' ?>>
                        <td class="cell-nowrap"><?= e((string) $id) ?></td>
                        <td class="cell-nowrap"><code class="period-key"><?= e((string) $row['period_key']) ?></code></td>
                        <td><?= e($title) ?></td>
                        <td><?= e($projectName) ?></td>
                        <td><?= e($clientName) ?></td>
                        <td class="cell-nowrap cell-dates"><?= e((string) $row['period_start']) ?> – <?= e((string) $row['period_end']) ?></td>
                        <td class="cell-nowrap"><span class="badge status-badge status-<?= e($status) ?>"><?= e($statusRu) ?></span></td>
                        <td class="cell-nowrap">
                            <?php if ($monthlyEmptyDraft && $monthlyDemotion !== ''): ?>
                                <span class="badge empty-draft-badge"><?= e($monthlyDemotion) ?></span>
                            <?php elseif ($monthlyStatusLabel !== '' && $monthlyStatusLabel !== '—'): ?>
                                <span class="badge status-badge status-<?= e($monthlyStatus) ?>"><?= e($monthlyStatusLabel) ?></span>
                                <?php if ($monthlyId > 0): ?>
                                    <a class="btn btn-secondary btn-sm" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Открыть</a>
                                <?php endif; ?>
                            <?php else: ?>
                                <span class="meta-muted">—</span>
                            <?php endif; ?>
                        </td>
                        <td><?= e($owner) ?></td>
                        <td class="actions cell-nowrap">
                            <a class="btn btn-primary btn-sm" href="<?= e(url_path('/reporting-periods/' . $id)) ?>">Открыть</a>
                            <?php if ($canEditRow): ?>
                                <a class="btn btn-secondary btn-sm" href="<?= e(url_path('/reporting-periods/' . $id . '/edit')) ?>">Изменить</a>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    </section>
<?php endif; ?>

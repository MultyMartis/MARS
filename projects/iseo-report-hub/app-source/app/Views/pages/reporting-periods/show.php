<?php
declare(strict_types=1);
/** @var array<string, mixed> $period */
/** @var bool $canEdit */
/** @var list<array<string, mixed>> $weeklyCheckpoints */
/** @var bool $canCreateCheckpoint */
/** @var array<string, mixed>|null $monthlyReport */
/** @var bool $canCreateMonthly */
/** @var bool $canEditMonthly */
/** @var bool $monthlyIsEmptyDraft */
$periodId = (int) $period['id'];
$weeklyCheckpoints = $weeklyCheckpoints ?? [];
$canCreateCheckpoint = $canCreateCheckpoint ?? false;
$monthlyReport = $monthlyReport ?? null;
$canCreateMonthly = $canCreateMonthly ?? false;
$canEditMonthly = $canEditMonthly ?? false;
$monthlyIsEmptyDraft = !empty($monthlyIsEmptyDraft);
?>
<section class="panel">
    <div class="panel-head">
        <h2>Отчетный период <?= e((string) $period['period_key']) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods')) ?>">К списку</a>
            <?php if ($canEdit): ?>
                <a class="btn btn-primary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/edit')) ?>">Изменить</a>
            <?php endif; ?>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Еженедельные заметки</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/monthly-report')) ?>">Месячный отчет</a>
        </p>
    </div>
    <p>
        <span class="status-badge status-<?= e((string) $period['status']) ?>"><?= e(ui_status_label((string) $period['status'])) ?></span>
        <span class="fixture-badge"><?= e(\Iseo\Support\UiLabels::fixtureBadge()) ?></span>
    </p>
</section>

<section class="panel">
    <h2>Детали периода</h2>
    <ul class="facts">
        <li><strong>Название:</strong> <?= e(ui_display_label((string) ($period['title'] ?? ''), '—')) ?></li>
        <li><strong>Краткое описание:</strong> <?= e(ui_display_body((string) ($period['summary'] ?? ''), null, '—')) ?></li>
        <li><strong>Даты:</strong> <?= e((string) $period['period_start']) ?> – <?= e((string) $period['period_end']) ?></li>
        <li><strong>Финализирован:</strong> <?= e((string) ($period['finalized_at'] ?? '—')) ?></li>
        <li><strong>Проект:</strong> <?= e(ui_display_label((string) ($period['project_name'] ?? ''), '—')) ?></li>
        <li><strong>Клиент:</strong> <?= e(ui_display_label((string) ($period['client_name'] ?? ''), '—')) ?></li>
        <li><strong>Сайт:</strong> <?= e((string) ($period['primary_site_url'] ?? '—')) ?><?php if (!empty($period['primary_site_label'])): ?> — <?= e((string) $period['primary_site_label']) ?><?php endif; ?></li>
        <li><strong>Ответственный:</strong> <?= e((string) ($period['owner_name'] ?? '—')) ?><?php if (!empty($period['owner_email'])): ?> · <?= e((string) $period['owner_email']) ?><?php endif; ?></li>
        <li><strong>Проверяющий:</strong> <?= e((string) ($period['reviewer_name'] ?? '—')) ?><?php if (!empty($period['reviewer_email'])): ?> · <?= e((string) $period['reviewer_email']) ?><?php endif; ?></li>
        <li><strong>Создал:</strong> <?= e((string) ($period['created_by_name'] ?? '—')) ?> · <?= e((string) ($period['created_at'] ?? '')) ?></li>
        <li><strong>Обновил:</strong> <?= e((string) ($period['updated_by_name'] ?? '—')) ?> · <?= e((string) ($period['updated_at'] ?? '')) ?></li>
    </ul>
    <details class="tech-details">
        <summary>Технические детали</summary>
        <ul class="facts">
            <li><strong>ID:</strong> <?= e((string) $period['id']) ?></li>
            <li><strong>Ключ периода:</strong> <code><?= e((string) $period['period_key']) ?></code></li>
            <li><strong>Проект (slug / id):</strong> <code><?= e((string) $period['project_slug']) ?></code> / <?= e((string) $period['project_id']) ?></li>
            <li><strong>Клиент (slug):</strong> <code><?= e((string) $period['client_slug']) ?></code></li>
        </ul>
    </details>
</section>

<section class="panel">
    <div class="panel-head">
        <h2>Еженедельные заметки (<?= e((string) count($weeklyCheckpoints)) ?>)</h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Открыть список</a>
            <?php if ($canCreateCheckpoint): ?>
                <a class="btn btn-primary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints/create')) ?>">Создать заметку</a>
            <?php endif; ?>
        </p>
    </div>
    <?php if ($weeklyCheckpoints === []): ?>
        <p class="note">Еженедельных заметок для этого периода пока нет.</p>
    <?php else: ?>
        <div class="table-wrap">
            <table class="data-table">
                <thead>
                <tr>
                    <th>Неделя</th>
                    <th>Название</th>
                    <th>Статус</th>
                    <th>Действия</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ($weeklyCheckpoints as $wc): ?>
                    <?php $wcId = (int) $wc['id']; ?>
                    <tr>
                        <td>W<?= e((string) $wc['week_index']) ?></td>
                        <td>
                            <?= e(ui_display_label((string) ($wc['title'] ?? ''), '—')) ?>
                            <div class="tech-muted"><code><?= e((string) $wc['checkpoint_key']) ?></code></div>
                        </td>
                        <td><span class="status-badge status-<?= e((string) $wc['status']) ?>"><?= e(ui_status_label((string) $wc['status'])) ?></span></td>
                        <td class="actions">
                            <a href="<?= e(url_path('/weekly-checkpoints/' . $wcId)) ?>">Открыть</a>
                            <?php if (!empty($wc['_can_edit'])): ?>
                                · <a href="<?= e(url_path('/weekly-checkpoints/' . $wcId . '/edit')) ?>">Изменить</a>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    <?php endif; ?>
</section>

<section class="panel<?= $monthlyIsEmptyDraft ? ' monthly-card--empty-draft' : '' ?>">
    <div class="panel-head">
        <h2>Месячный отчет</h2>
        <p>
            <?php if ($monthlyReport !== null): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . (int) $monthlyReport['id'])) ?>">Открыть отчет</a>
                <a class="btn btn-primary" href="<?= e(url_path('/monthly-reports/' . (int) $monthlyReport['id'] . '/preview')) ?>">Предпросмотр</a>
                <?php if ($canEditMonthly): ?>
                    <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . (int) $monthlyReport['id'] . '/edit')) ?>">Изменить</a>
                <?php endif; ?>
            <?php elseif ($canCreateMonthly): ?>
                <a class="btn btn-primary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/monthly-report/create')) ?>">Создать месячный отчет</a>
            <?php endif; ?>
        </p>
    </div>
    <?php if ($monthlyReport === null): ?>
        <p class="note">Месячного отчета для этого периода пока нет.</p>
    <?php else: ?>
        <ul class="facts">
            <li><strong>Название:</strong>
                <?php if ($monthlyIsEmptyDraft): ?>
                    <?= e(\Iseo\Support\UiLabels::emptyDraftHeading()) ?>
                <?php else: ?>
                    <?= e(ui_display_label((string) ($monthlyReport['title'] ?? ''), '—')) ?>
                <?php endif; ?>
            </li>
            <li><strong>Статус:</strong>
                <span class="status-badge status-<?= e((string) $monthlyReport['status']) ?>"><?= e(ui_status_label((string) $monthlyReport['status'])) ?></span>
                <?php if ($monthlyIsEmptyDraft): ?>
                    <span class="badge empty-draft-badge"><?= e(\Iseo\Support\UiLabels::emptyDraftWithoutWorkLabel()) ?></span>
                <?php endif; ?>
            </li>
        </ul>
        <?php if ($monthlyIsEmptyDraft): ?>
            <p class="note empty-draft-message">Работ и блоков пока нет. Это намеренный пустой черновик, не основной демо-отчет.</p>
        <?php endif; ?>
        <details class="tech-details">
            <summary>Технические детали</summary>
            <ul class="facts">
                <li><strong>ID:</strong> <?= e((string) $monthlyReport['id']) ?></li>
            </ul>
        </details>
        <?php if (!$monthlyIsEmptyDraft): ?>
            <p class="note">Блоки и предпросмотр доступны из карточки месячного отчета. Файлы PDF и публичные ссылки пока отключены.</p>
        <?php endif; ?>
    <?php endif; ?>
</section>

<?php
declare(strict_types=1);
/** @var array<string, mixed> $checkpoint */
/** @var array<string, mixed>|null $period */
/** @var bool $canEdit */
$periodId = (int) $checkpoint['reporting_period_id'];
?>
<section class="panel">
    <div class="panel-head">
        <h2>Заметка <?= e((string) $checkpoint['checkpoint_key']) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">К списку</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">Родительский период</a>
            <?php if ($canEdit): ?>
                <a class="btn" href="<?= e(url_path('/weekly-checkpoints/' . (int) $checkpoint['id'] . '/edit')) ?>">Изменить</a>
            <?php endif; ?>
        </p>
    </div>
    <p>
        <span class="status-badge status-<?= e((string) $checkpoint['status']) ?>"><?= e(ui_status_label((string) $checkpoint['status'])) ?></span>
    </p>
</section>

<section class="panel">
    <h2>Родительский период</h2>
    <ul class="facts">
        <li><strong>Период:</strong>
            <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                <code><?= e((string) ($checkpoint['period_key'] ?? '')) ?></code>
            </a>
            · <span class="status-badge status-<?= e((string) ($checkpoint['period_status'] ?? '')) ?>"><?= e(ui_status_label((string) ($checkpoint['period_status'] ?? ''))) ?></span>
        </li>
        <li><strong>Проект:</strong> <?= e((string) ($checkpoint['project_name'] ?? '—')) ?></li>
        <li><strong>Клиент:</strong> <?= e((string) ($checkpoint['client_name'] ?? '—')) ?></li>
        <li><strong>Даты периода:</strong> <?= e((string) ($checkpoint['period_start'] ?? '')) ?> – <?= e((string) ($checkpoint['period_end'] ?? '')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Детали</h2>
    <ul class="facts">
        <li><strong>Неделя:</strong> W<?= e((string) $checkpoint['week_index']) ?></li>
        <li><strong>Название:</strong> <?= e((string) $checkpoint['title']) ?></li>
        <li><strong>Даты:</strong> <?= e((string) $checkpoint['checkpoint_start']) ?> – <?= e((string) $checkpoint['checkpoint_end']) ?></li>
        <li><strong>Проверен:</strong> <?= e((string) ($checkpoint['reviewed_at'] ?? '—')) ?></li>
        <li><strong>Завершён:</strong> <?= e((string) ($checkpoint['completed_at'] ?? '—')) ?></li>
        <li><strong>Ответственный:</strong> <?= e(ui_display_user_name($checkpoint['owner_name'] ?? null, $checkpoint['owner_email'] ?? null)) ?></li>
        <li><strong>Проверяющий:</strong> <?= e(ui_display_user_name($checkpoint['reviewer_name'] ?? null, $checkpoint['reviewer_email'] ?? null)) ?></li>
        <li><strong>Создал:</strong> <?= e(ui_display_user_name($checkpoint['created_by_name'] ?? null, null)) ?> · <?= e((string) ($checkpoint['created_at'] ?? '')) ?></li>
        <li><strong>Обновил:</strong> <?= e(ui_display_user_name($checkpoint['updated_by_name'] ?? null, null)) ?> · <?= e((string) ($checkpoint['updated_at'] ?? '')) ?></li>
    </ul>
    <details class="tech-details">
        <summary>Технические детали</summary>
        <ul class="facts">
            <li><strong>ID:</strong> <?= e((string) $checkpoint['id']) ?></li>
            <li><strong>Ключ:</strong> <code><?= e((string) $checkpoint['checkpoint_key']) ?></code></li>
        </ul>
    </details>
</section>

<section class="panel">
    <h2>Заметки</h2>
    <ul class="facts">
        <li><strong>Кратко:</strong> <?= e((string) ($checkpoint['summary'] ?? '—')) ?></li>
        <li><strong>Сделано:</strong> <?= e((string) ($checkpoint['work_done'] ?? '—')) ?></li>
        <li><strong>Выводы:</strong> <?= e((string) ($checkpoint['findings'] ?? '—')) ?></li>
        <li><strong>Следующие шаги:</strong> <?= e((string) ($checkpoint['next_steps'] ?? '—')) ?></li>
        <li><strong>Риски:</strong> <?= e((string) ($checkpoint['risks'] ?? '—')) ?></li>
    </ul>
</section>

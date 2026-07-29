<?php
declare(strict_types=1);
/** @var list<array{title:string,status:string,detail:string,status_label?:string}> $cards */
/** @var array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user */
/** @var string $authStatus */
/** @var int|null $periodCount */
/** @var int|null $checkpointCount */
/** @var int|null $monthlyCount */
/** @var int|null $blockCount */
/** @var int $quickMonthlyId */
/** @var int $quickSnapshotId */
/** @var int $quickExportId */

$statusRu = static function (string $status): string {
    return match ($status) {
        'ready' => 'Готово',
        'pending' => 'В работе',
        'failed' => 'Ошибка',
        default => $status,
    };
};

$quickMonthlyId = (int) ($quickMonthlyId ?? 1);
$quickSnapshotId = (int) ($quickSnapshotId ?? 1);
$quickExportId = (int) ($quickExportId ?? 4);
?>
<section class="panel dashboard-hero">
    <h2>Система отчетов i-SEO</h2>
    <p class="note dashboard-auth-line">
        <strong><?= e($authStatus) ?></strong>
        · Локальная тестовая среда
    </p>
    <?php if (is_array($user)): ?>
        <ul class="facts">
            <li><strong>Имя:</strong> <?= e($user['name']) ?></li>
            <li><strong>Email:</strong> <?= e($user['email']) ?></li>
            <li><strong>Роли:</strong> <?= e(implode(', ', $user['roles'])) ?></li>
        </ul>
    <?php endif; ?>
</section>

<section class="panel">
    <h2>Быстрые действия</h2>
    <p class="quick-actions">
        <a class="btn" href="<?= e(url_path('/reporting-periods')) ?>">Отчетные периоды<?= isset($periodCount) && $periodCount !== null ? ' (' . e((string) $periodCount) . ')' : '' ?></a>
        <a class="btn" href="<?= e(url_path('/monthly-reports/' . $quickMonthlyId)) ?>">Последний отчет</a>
        <a class="btn" href="<?= e(url_path('/report-snapshots/' . $quickSnapshotId . '/exports')) ?>">Файлы отчета</a>
        <a class="btn" href="<?= e(url_path('/report-exports/' . $quickExportId . '/shares')) ?>">Ссылки для клиента</a>
        <a class="btn btn-secondary" href="<?= e(url_path('/health')) ?>">Состояние системы</a>
        <a class="btn btn-secondary" href="<?= e(url_path('/logout')) ?>">Выйти</a>
    </p>
    <p class="note">Рабочий путь менеджера: периоды → отчет → файлы → PDF → ссылка → скопировать сообщение → отправить вручную.</p>
</section>

<details class="panel tech-details dashboard-status-details">
    <summary>Статус модулей</summary>
    <section class="status-grid">
        <?php foreach ($cards as $card): ?>
            <article class="panel status-card status-<?= e($card['status']) ?>">
                <h2><?= e($card['title']) ?></h2>
                <p class="status-pill"><?= e((string) ($card['status_label'] ?? $statusRu($card['status']))) ?></p>
                <p><?= e($card['detail']) ?></p>
            </article>
        <?php endforeach; ?>
    </section>
    <p class="note">
        Еженедельные заметки, месячные отчеты и блоки открываются через отчетный период.
        <?php if (isset($checkpointCount) && $checkpointCount !== null): ?>
            Заметок: <?= e((string) $checkpointCount) ?>.
        <?php endif; ?>
        <?php if (isset($monthlyCount) && $monthlyCount !== null): ?>
            Месячных отчетов: <?= e((string) $monthlyCount) ?>.
        <?php endif; ?>
        <?php if (isset($blockCount) && $blockCount !== null): ?>
            Блоков: <?= e((string) $blockCount) ?>.
        <?php endif; ?>
    </p>
</details>

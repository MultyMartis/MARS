<?php
declare(strict_types=1);
/** @var array<string, mixed> $block */
/** @var array<string, mixed>|null $monthly */
/** @var list<array<string, mixed>> $sourceCheckpoints */
/** @var bool $canEdit */
$monthlyId = (int) $block['monthly_report_content_id'];
$periodId = (int) $block['reporting_period_id'];
$sourceCheckpoints = $sourceCheckpoints ?? [];
$parentFinalized = !empty($parentFinalized);
$blockKey = (string) $block['block_key'];
$sectionLabel = ui_block_label($blockKey);
?>
<section class="panel">
    <div class="panel-head">
        <h2>Блок: <?= e((string) $block['title']) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/blocks')) ?>">К списку блоков</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Родительский отчет</a>
            <?php if ($canEdit): ?>
                <a class="btn" href="<?= e(url_path('/report-blocks/' . (int) $block['id'] . '/edit')) ?>">Изменить</a>
            <?php endif; ?>
        </p>
    </div>
    <p>
        <span class="status-badge status-<?= e((string) $block['status']) ?>"><?= e(ui_status_label((string) $block['status'])) ?></span>
        · <span class="type-badge"><?= e((string) $block['block_type']) ?></span>
        · порядок <?= e((string) $block['sort_order']) ?>
        <?php if ($sectionLabel !== $blockKey): ?>
            · <?= e($sectionLabel) ?>
        <?php endif; ?>
        <span class="meta-muted"><code><?= e($blockKey) ?></code></span>
        <?php if ($parentFinalized): ?>
            · <span class="finalized-badge">Родитель финализирован</span>
        <?php endif; ?>
    </p>
</section>

<?php if ($parentFinalized): ?>
    <section class="panel locked-notice">
        <h2>Заблокировано</h2>
        <p>Родительский месячный отчет финализирован. Редактирование блока недоступно до повторного открытия отчета.</p>
    </section>
<?php endif; ?>

<section class="panel">
    <h2>Контекст</h2>
    <ul class="facts">
        <li><strong>Месячный отчет:</strong>
            <a href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">
                <?= e((string) ($block['monthly_title'] ?? ('#' . $monthlyId))) ?>
            </a>
            · <span class="status-badge status-<?= e((string) ($block['monthly_status'] ?? '')) ?>"><?= e(ui_status_label((string) ($block['monthly_status'] ?? ''))) ?></span>
        </li>
        <li><strong>Период:</strong>
            <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                <code><?= e((string) ($block['period_key'] ?? '')) ?></code>
            </a>
            · <span class="status-badge status-<?= e((string) ($block['period_status'] ?? '')) ?>"><?= e(ui_status_label((string) ($block['period_status'] ?? ''))) ?></span>
        </li>
        <li><strong>Проект:</strong> <?= e((string) ($block['project_name'] ?? '—')) ?></li>
        <li><strong>Клиент:</strong> <?= e((string) ($block['client_name'] ?? '—')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Детали</h2>
    <ul class="facts">
        <li><strong>Название:</strong> <?= e((string) $block['title']) ?></li>
        <li><strong>Проверен:</strong> <?= e((string) ($block['reviewed_at'] ?? '—')) ?></li>
        <li><strong>Утверждён:</strong> <?= e((string) ($block['approved_at'] ?? '—')) ?></li>
        <li><strong>Ответственный:</strong> <?= e(ui_display_user_name($block['owner_name'] ?? null, $block['owner_email'] ?? null)) ?></li>
        <li><strong>Проверяющий:</strong> <?= e(ui_display_user_name($block['reviewer_name'] ?? null, $block['reviewer_email'] ?? null)) ?></li>
        <li><strong>Создал:</strong> <?= e(ui_display_user_name($block['created_by_name'] ?? null, null)) ?> · <?= e((string) ($block['created_at'] ?? '')) ?></li>
        <li><strong>Обновил:</strong> <?= e(ui_display_user_name($block['updated_by_name'] ?? null, null)) ?> · <?= e((string) ($block['updated_at'] ?? '')) ?></li>
    </ul>
    <details class="tech-details">
        <summary>Технические детали</summary>
        <ul class="facts">
            <li><strong>ID:</strong> <?= e((string) $block['id']) ?></li>
            <li><strong>Ключ:</strong> <code><?= e($blockKey) ?></code></li>
            <li><strong>Тип:</strong> <span class="type-badge"><?= e((string) $block['block_type']) ?></span></li>
            <li><strong>Порядок:</strong> <?= e((string) $block['sort_order']) ?></li>
        </ul>
    </details>
</section>

<section class="panel">
    <h2>Исходные еженедельные заметки</h2>
    <?php if ($sourceCheckpoints === []): ?>
        <p class="note">Связанные еженедельные заметки не указаны.</p>
    <?php else: ?>
        <ul class="facts">
            <?php foreach ($sourceCheckpoints as $wc): ?>
                <li>
                    <a href="<?= e(url_path('/weekly-checkpoints/' . (int) $wc['id'])) ?>">
                        <code><?= e((string) $wc['checkpoint_key']) ?></code>
                    </a>
                    · <span class="status-badge status-<?= e((string) $wc['status']) ?>"><?= e(ui_status_label((string) $wc['status'])) ?></span>
                    · <?= e((string) $wc['title']) ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</section>

<section class="panel">
    <h2>Содержимое</h2>
    <ul class="facts">
        <li><strong>Кратко:</strong> <?= e((string) ($block['summary'] ?? '—')) ?></li>
        <li><strong>Текст:</strong> <?= e((string) ($block['body'] ?? '—')) ?></li>
    </ul>
    <details class="tech-details">
        <summary>Технические детали</summary>
        <ul class="facts">
            <li><strong>data_json:</strong> <pre class="json-preview"><?= e((string) ($block['data_json'] ?? '—')) ?></pre></li>
            <li><strong>source_metric_refs:</strong> <pre class="json-preview"><?= e((string) ($block['source_metric_refs'] ?? '—')) ?></pre></li>
        </ul>
    </details>
</section>

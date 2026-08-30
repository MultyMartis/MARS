<?php
declare(strict_types=1);
/** @var string $mode create|edit */
/** @var array<string, mixed> $monthly */
/** @var array<string, mixed>|null $block */
/** @var array<string, mixed> $old */
/** @var array<string, string> $errors */
/** @var string|null $formMessage */
/** @var list<array{id:int,name:string,email:string}> $users */
/** @var list<string> $statuses */
/** @var list<string> $blockTypes */
/** @var list<array<string, mixed>> $availableCheckpoints */
/** @var bool $canAssignUsers */
/** @var array{monthly_report_content_id:bool,block_key:bool,block_type:bool,sort_order:bool,content:bool,source_ids:bool} $locks */
/** @var \Iseo\Services\CsrfService $csrf */

$isEdit = $mode === 'edit';
$monthlyId = (int) $monthly['id'];
$periodId = (int) $monthly['reporting_period_id'];
$action = $isEdit
    ? url_path('/report-blocks/' . (int) $block['id'])
    : url_path('/monthly-reports/' . $monthlyId . '/blocks');
$cancelHref = $isEdit
    ? url_path('/report-blocks/' . (int) $block['id'])
    : url_path('/monthly-reports/' . $monthlyId . '/blocks');

$selectedSource = $old['source_weekly_checkpoint_ids'] ?? [];
if (!is_array($selectedSource)) {
    $selectedSource = [];
}
$selectedMap = [];
foreach ($selectedSource as $sid) {
    $selectedMap[(string) $sid] = true;
}
?>
<section class="panel">
    <p class="note">
        Родительский месячный отчет:
        <a href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">
            <?= e((string) ($monthly['title'] ?? ('#' . $monthlyId))) ?>
        </a>
        · <span class="status-badge status-<?= e((string) ($monthly['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($monthly['status'] ?? ''))) ?></span>
        · период
        <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
            <code><?= e((string) ($monthly['period_key'] ?? '')) ?></code>
        </a>
        · <?= e((string) ($monthly['project_name'] ?? '')) ?> / <?= e((string) ($monthly['client_name'] ?? '')) ?>
        · <a href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/blocks')) ?>">Список блоков</a>
    </p>
</section>

<?php if (!empty($formMessage) || $errors !== []): ?>
    <section class="panel flash flash-warn">
        <p><?= e((string) ($formMessage ?? 'Исправьте ошибки в форме.')) ?></p>
        <?php if ($errors !== []): ?>
            <ul class="facts">
                <?php foreach ($errors as $field => $message): ?>
                    <li><strong><?= e((string) $field) ?>:</strong> <?= e($message) ?></li>
                <?php endforeach; ?>
            </ul>
        <?php endif; ?>
    </section>
<?php endif; ?>

<section class="panel">
    <h2><?= $isEdit ? 'Изменить блок отчета' : 'Создать блок отчета' ?></h2>
    <form class="rp-form rb-form" method="post" action="<?= e($action) ?>" novalidate>
        <?= $csrf->field() ?>

        <label>
            <span>Месячный отчет</span>
            <input type="text" value="<?= e((string) ($monthly['period_key'] ?? '') . ' / #' . $monthlyId) ?>" disabled>
            <span class="field-hint">Родительский отчет неизменяем. Жёсткое удаление недоступно — используйте архив через статус.</span>
        </label>

        <div class="form-row">
            <label>
                <span class="field-label-with-help">Ключ блока<?= field_help('report_block.block_key') ?></span>
                <input type="text" name="block_key" value="<?= e((string) $old['block_key']) ?>" maxlength="64" pattern="[a-z0-9_\-]+"<?= $locks['block_key'] ? ' readonly' : ' required' ?>>
                <?php if ($locks['block_key']): ?><span class="field-hint">Ключ блока заблокирован вне черновика (admin_owner может изменить).</span><?php endif; ?>
                <?php if (isset($errors['block_key'])): ?><span class="field-error"><?= e($errors['block_key']) ?></span><?php endif; ?>
            </label>
            <label>
                <span class="field-label-with-help">Тип блока<?= field_help('report_block.block_type') ?></span>
                <select name="block_type"<?= $locks['block_type'] ? ' disabled' : ' required' ?>>
                    <?php foreach ($blockTypes as $type): ?>
                        <option value="<?= e($type) ?>"<?= ((string) $old['block_type'] === $type) ? ' selected' : '' ?>><?= e($type) ?></option>
                    <?php endforeach; ?>
                </select>
                <?php if ($locks['block_type']): ?>
                    <input type="hidden" name="block_type" value="<?= e((string) $old['block_type']) ?>">
                    <span class="field-hint">Тип блока заблокирован вне черновика.</span>
                <?php endif; ?>
                <?php if (isset($errors['block_type'])): ?><span class="field-error"><?= e($errors['block_type']) ?></span><?php endif; ?>
            </label>
        </div>

        <div class="form-row">
            <label>
                <span class="field-label-with-help">Порядок сортировки<?= field_help('report_block.sort_order') ?></span>
                <input type="number" name="sort_order" min="0" step="1" value="<?= e((string) $old['sort_order']) ?>"<?= $locks['sort_order'] ? ' readonly' : ' required' ?>>
                <?php if (isset($errors['sort_order'])): ?><span class="field-error"><?= e($errors['sort_order']) ?></span><?php endif; ?>
                <span class="field-hint">Целое число вручную (без drag-and-drop).</span>
            </label>
            <label>
                <span class="field-label-with-help">Статус<?= field_help('report_block.status') ?></span>
                <select name="status" required>
                    <?php foreach ($statuses as $status): ?>
                        <option value="<?= e($status) ?>"<?= ((string) $old['status'] === $status) ? ' selected' : '' ?>><?= e(ui_status_label($status)) ?></option>
                    <?php endforeach; ?>
                </select>
                <?php if (isset($errors['status'])): ?><span class="field-error"><?= e($errors['status']) ?></span><?php endif; ?>
            </label>
        </div>

        <label>
            <span class="field-label-with-help">Название<?= field_help('report_block.title') ?></span>
            <input type="text" name="title" value="<?= e((string) $old['title']) ?>" maxlength="255"<?= $locks['content'] ? ' readonly' : ' required' ?>>
            <?php if (isset($errors['title'])): ?><span class="field-error"><?= e($errors['title']) ?></span><?php endif; ?>
        </label>

        <label>
            <span class="field-label-with-help">Кратко<?= field_help('report_block.summary') ?></span>
            <textarea name="summary" rows="3"<?= $locks['content'] ? ' readonly' : '' ?>><?= e((string) $old['summary']) ?></textarea>
            <?php if (isset($errors['summary'])): ?><span class="field-error"><?= e($errors['summary']) ?></span><?php endif; ?>
        </label>

        <label>
            <span class="field-label-with-help">Текст<?= field_help('report_block.body') ?></span>
            <textarea name="body" rows="8"<?= $locks['content'] ? ' readonly' : '' ?>><?= e((string) $old['body']) ?></textarea>
            <?php if (isset($errors['body'])): ?><span class="field-error"><?= e($errors['body']) ?></span><?php endif; ?>
        </label>

        <fieldset class="checkbox-fieldset"<?= $locks['source_ids'] ? ' disabled' : '' ?>>
            <legend>Исходные еженедельные заметки</legend>
            <?php if ($availableCheckpoints === []): ?>
                <p class="note">В родительском периоде нет еженедельных заметок.</p>
            <?php else: ?>
                <?php foreach ($availableCheckpoints as $wc): ?>
                    <?php $wid = (string) $wc['id']; ?>
                    <label class="checkbox-row">
                        <input type="checkbox" name="source_weekly_checkpoint_ids[]" value="<?= e($wid) ?>"<?= isset($selectedMap[$wid]) ? ' checked' : '' ?>>
                        <span>
                            <code><?= e((string) $wc['checkpoint_key']) ?></code>
                            · <span class="status-badge status-<?= e((string) $wc['status']) ?>"><?= e(ui_status_label((string) $wc['status'])) ?></span>
                            · <?= e((string) $wc['title']) ?>
                        </span>
                    </label>
                <?php endforeach; ?>
            <?php endif; ?>
            <?php if (isset($errors['source_weekly_checkpoint_ids'])): ?>
                <span class="field-error"><?= e($errors['source_weekly_checkpoint_ids']) ?></span>
            <?php endif; ?>
        </fieldset>
        <?php if ($locks['source_ids']): ?>
            <?php foreach ($selectedSource as $sid): ?>
                <input type="hidden" name="source_weekly_checkpoint_ids[]" value="<?= e((string) $sid) ?>">
            <?php endforeach; ?>
        <?php endif; ?>

        <label>
            <span class="field-label-with-help">data_json (объект или массив)<?= field_help('report_block.data_json') ?></span>
            <textarea name="data_json" rows="4" class="json-input"<?= $locks['content'] ? ' readonly' : '' ?>><?= e((string) ($old['data_json'] ?? '')) ?></textarea>
            <?php if (isset($errors['data_json'])): ?><span class="field-error"><?= e($errors['data_json']) ?></span><?php endif; ?>
        </label>

        <label>
            <span class="field-label-with-help">source_metric_refs (объект или массив)<?= field_help('report_block.source_metric_refs') ?></span>
            <textarea name="source_metric_refs" rows="4" class="json-input"<?= $locks['content'] ? ' readonly' : '' ?>><?= e((string) ($old['source_metric_refs'] ?? '')) ?></textarea>
            <?php if (isset($errors['source_metric_refs'])): ?><span class="field-error"><?= e($errors['source_metric_refs']) ?></span><?php endif; ?>
        </label>

        <div class="form-row">
            <label>
                <span>Ответственный</span>
                <select name="owner_user_id"<?= $canAssignUsers ? '' : ' disabled' ?>>
                    <option value="">— не назначен —</option>
                    <?php foreach ($users as $u): ?>
                        <option value="<?= e((string) $u['id']) ?>"<?= ((string) $old['owner_user_id'] === (string) $u['id']) ? ' selected' : '' ?>>
                            <?= e(ui_display_user_name($u['name'], $u['email'])) ?>
                        </option>
                    <?php endforeach; ?>
                </select>
                <?php if (!$canAssignUsers): ?>
                    <input type="hidden" name="owner_user_id" value="<?= e((string) $old['owner_user_id']) ?>">
                <?php endif; ?>
                <?php if (isset($errors['owner_user_id'])): ?><span class="field-error"><?= e($errors['owner_user_id']) ?></span><?php endif; ?>
            </label>
            <label>
                <span>Проверяющий</span>
                <select name="reviewer_user_id"<?= $canAssignUsers ? '' : ' disabled' ?>>
                    <option value="">— не назначен —</option>
                    <?php foreach ($users as $u): ?>
                        <option value="<?= e((string) $u['id']) ?>"<?= ((string) $old['reviewer_user_id'] === (string) $u['id']) ? ' selected' : '' ?>>
                            <?= e(ui_display_user_name($u['name'], $u['email'])) ?>
                        </option>
                    <?php endforeach; ?>
                </select>
                <?php if (!$canAssignUsers): ?>
                    <input type="hidden" name="reviewer_user_id" value="<?= e((string) $old['reviewer_user_id']) ?>">
                <?php endif; ?>
                <?php if (isset($errors['reviewer_user_id'])): ?><span class="field-error"><?= e($errors['reviewer_user_id']) ?></span><?php endif; ?>
            </label>
        </div>

        <p class="form-actions">
            <button type="submit" class="btn"><?= $isEdit ? 'Сохранить блок' : 'Создать блок' ?></button>
            <a class="btn btn-secondary" href="<?= e($cancelHref) ?>">Отмена</a>
        </p>
    </form>
</section>

<?php
declare(strict_types=1);
/** @var string $mode create|edit */
/** @var array<string, mixed> $period */
/** @var array<string, mixed>|null $report */
/** @var array<string, mixed> $old */
/** @var array<string, string> $errors */
/** @var string|null $formMessage */
/** @var list<array{id:int,name:string,email:string}> $users */
/** @var list<string> $statuses */
/** @var list<array<string, mixed>> $availableCheckpoints */
/** @var bool $canAssignUsers */
/** @var array{reporting_period_id:bool,content:bool,source_ids:bool} $locks */
/** @var \Iseo\Services\CsrfService $csrf */

$isEdit = $mode === 'edit';
$periodId = (int) $period['id'];
$action = $isEdit
    ? url_path('/monthly-reports/' . (int) $report['id'])
    : url_path('/reporting-periods/' . $periodId . '/monthly-report');
$cancelHref = $isEdit
    ? url_path('/monthly-reports/' . (int) $report['id'])
    : url_path('/reporting-periods/' . $periodId);
$parentFinalized = !empty($parentFinalized) || !empty($formLocked);
$formLocked = !empty($formLocked) || $parentFinalized;

$selectedSource = $old['source_weekly_checkpoint_ids'] ?? [];
if (!is_array($selectedSource)) {
    $selectedSource = [];
}
$selectedMap = [];
foreach ($selectedSource as $sid) {
    $selectedMap[(string) $sid] = true;
}

$textFields = \Iseo\Support\UiLabels::blockKeyMap();
?>
<section class="panel">
    <p class="note">
        Родительский период:
        <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
            <code><?= e((string) $period['period_key']) ?></code>
        </a>
        · <?= e((string) $period['project_name']) ?> / <?= e((string) $period['client_name']) ?>
        · <?= e((string) $period['period_start']) ?> – <?= e((string) $period['period_end']) ?>
        · <a href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Еженедельные заметки</a>
    </p>
</section>

<?php if ($parentFinalized): ?>
    <section class="panel locked-notice">
        <h2>Заблокировано — финализирован</h2>
        <p>Месячный отчет финализирован. Обычное редактирование недоступно. Используйте <strong>Открыть снова</strong> на странице отчета (admin_owner) перед изменениями.</p>
        <p><a class="btn btn-secondary" href="<?= e($cancelHref) ?>">К месячному отчету</a></p>
    </section>
<?php endif; ?>

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
    <h2><?= $isEdit ? 'Изменить содержимое месячного отчета' : 'Создать содержимое месячного отчета' ?></h2>
    <?php if ($formLocked): ?>
        <p class="note">Форма заблокирована, пока отчет финализирован.</p>
    <?php else: ?>
    <form class="rp-form mrc-form" method="post" action="<?= e($action) ?>" novalidate>
        <?= $csrf->field() ?>

        <label>
            <span>Отчетный период</span>
            <input type="text" value="<?= e((string) $period['period_key'] . ' (id ' . $periodId . ')') ?>" disabled>
            <span class="field-hint">Родительский период неизменяем. Одна строка содержимого месячного отчета на период.</span>
        </label>

        <label>
            <span class="field-label-with-help">Статус<?= field_help('report_section.status') ?></span>
            <select name="status" required>
                <?php foreach ($statuses as $status): ?>
                    <option value="<?= e($status) ?>"<?= ((string) $old['status'] === $status) ? ' selected' : '' ?>><?= e(ui_status_label($status)) ?></option>
                <?php endforeach; ?>
            </select>
            <?php if (isset($errors['status'])): ?><span class="field-error"><?= e($errors['status']) ?></span><?php endif; ?>
            <span class="field-hint">Жёсткое удаление недоступно — используйте «В архиве».</span>
        </label>

        <label>
            <span class="field-label-with-help">Название<?= field_help('report_section.title') ?></span>
            <input type="text" name="title" value="<?= e((string) $old['title']) ?>" maxlength="255"<?= $locks['content'] ? ' readonly' : ' required' ?>>
            <?php if (isset($errors['title'])): ?><span class="field-error"><?= e($errors['title']) ?></span><?php endif; ?>
        </label>

        <fieldset class="mrc-source-fieldset"<?= $locks['source_ids'] ? ' disabled' : '' ?>>
            <legend>Исходные еженедельные заметки</legend>
            <?php if ($availableCheckpoints === []): ?>
                <p class="note">В этом периоде ещё нет еженедельных заметок.</p>
            <?php else: ?>
                <ul class="mrc-source-list">
                    <?php foreach ($availableCheckpoints as $wc): ?>
                        <?php $wcId = (string) $wc['id']; ?>
                        <li>
                            <label class="mrc-source-item">
                                <input type="checkbox" name="source_weekly_checkpoint_ids[]" value="<?= e($wcId) ?>"<?= isset($selectedMap[$wcId]) ? ' checked' : '' ?>>
                                <span>
                                    <code><?= e((string) $wc['checkpoint_key']) ?></code>
                                    · <?= e(ui_status_label((string) $wc['status'])) ?>
                                    · <?= e((string) $wc['title']) ?>
                                </span>
                            </label>
                        </li>
                    <?php endforeach; ?>
                </ul>
            <?php endif; ?>
            <?php if (isset($errors['source_weekly_checkpoint_ids'])): ?>
                <span class="field-error"><?= e($errors['source_weekly_checkpoint_ids']) ?></span>
            <?php endif; ?>
            <span class="field-hint">Пустой выбор допустим (предупреждение при сохранении). ID должны принадлежать этому периоду.</span>
        </fieldset>
        <?php if ($locks['source_ids']): ?>
            <?php foreach ($selectedSource as $sid): ?>
                <input type="hidden" name="source_weekly_checkpoint_ids[]" value="<?= e((string) $sid) ?>">
            <?php endforeach; ?>
            <p class="field-hint">Исходные заметки заблокированы, пока отчет финализирован (только admin_owner).</p>
        <?php endif; ?>

        <?php foreach ($textFields as $name => $label): ?>
            <label>
                <span class="field-label-with-help"><?= e($label) ?><?= field_help(\Iseo\Support\FieldHelp::keyForMonthlyField($name)) ?></span>
                <textarea name="<?= e($name) ?>" rows="4"<?= $locks['content'] ? ' readonly' : '' ?>><?= e((string) ($old[$name] ?? '')) ?></textarea>
                <?php if (isset($errors[$name])): ?><span class="field-error"><?= e($errors[$name]) ?></span><?php endif; ?>
            </label>
        <?php endforeach; ?>

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

        <p>
            <button class="btn" type="submit"><?= $isEdit ? 'Сохранить изменения' : 'Создать месячный отчет' ?></button>
            <a class="btn btn-secondary" href="<?= e($cancelHref) ?>">Отмена</a>
        </p>
    </form>
    <?php endif; ?>
</section>

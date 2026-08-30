<?php
declare(strict_types=1);
/** @var string $mode create|edit */
/** @var array<string, mixed> $monthly */
/** @var array<string, mixed>|null $entry */
/** @var array<string, mixed> $old */
/** @var array<string, string> $errors */
/** @var string|null $formMessage */
/** @var list<array<string, mixed>> $categories */
/** @var list<array<string, mixed>> $workItems */
/** @var list<string> $statuses */
/** @var list<string> $periodRoles */
/** @var list<string> $visibilities */
/** @var bool $parentFinalized */
/** @var string|null $finalizedWarning */
/** @var \Iseo\Services\CsrfService $csrf */

$isEdit = $mode === 'edit';
$monthlyId = (int) $monthly['id'];
$periodId = (int) ($monthly['reporting_period_id'] ?? 0);
$action = $isEdit
    ? url_path('/monthly-report-work-entries/' . (int) $entry['id'])
    : url_path('/monthly-reports/' . $monthlyId . '/work-entries');
$cancelHref = url_path('/monthly-reports/' . $monthlyId . '#work-entries');

$selectedWorkItem = (string) ($old['work_item_id'] ?? '');
$selectedCategory = (string) ($old['category_id'] ?? '');
?>
<section class="panel">
    <p class="note">
        Родительский месячный отчет:
        <a href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">
            <?= e(ui_display_label((string) ($monthly['title'] ?? ''), '#' . $monthlyId)) ?>
        </a>
        · <span class="status-badge status-<?= e((string) ($monthly['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($monthly['status'] ?? ''))) ?></span>
        <?php if ($periodId > 0): ?>
            · период
            <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                <code><?= e((string) ($monthly['period_key'] ?? '')) ?></code>
            </a>
        <?php endif; ?>
        · <?= e(ui_display_label((string) ($monthly['project_name'] ?? ''), '—')) ?> / <?= e(ui_display_label((string) ($monthly['client_name'] ?? ''), '—')) ?>
        · <a href="<?= e(url_path('/monthly-reports/' . $monthlyId . '#work-entries')) ?>">Работы за месяц</a>
    </p>
</section>

<?php if (!empty($finalizedWarning)): ?>
    <section class="panel flash flash-warn work-entry-finalized-warning">
        <p><?= e((string) $finalizedWarning) ?></p>
        <p class="field-hint">Изменения не пересобирают PDF и не меняют уже созданные ссылки.</p>
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
    <h2><?= $isEdit ? 'Изменить работу' : 'Добавить работу' ?></h2>
    <form class="rp-form work-entry-form form-grid" method="post" action="<?= e($action) ?>" novalidate>
        <?= $csrf->field() ?>

        <label class="field">
            <span>Месячный отчет</span>
            <input type="text" value="<?= e((string) ($monthly['period_key'] ?? '') . ' / #' . $monthlyId) ?>" disabled>
            <span class="field-hint">Родительский отчет неизменяем. Физическое удаление недоступно — используйте статусы «Отменено» / «Отложено» или видимость «Внутреннее».</span>
        </label>

        <fieldset class="work-entry-section">
            <legend class="work-entry-section__title">Что сделали</legend>
            <div class="form-row">
                <label class="field">
                    <span class="field-label-with-help">Категория<?= field_help('work_entry.category') ?></span>
                    <select name="category_id">
                        <option value="">— без категории / ручная работа —</option>
                        <?php foreach ($categories as $category): ?>
                            <?php $cid = (string) $category['id']; ?>
                            <option value="<?= e($cid) ?>"<?= $selectedCategory === $cid ? ' selected' : '' ?>>
                                <?= e((string) $category['name']) ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                    <?php if (isset($errors['category_id'])): ?><span class="field-error"><?= e($errors['category_id']) ?></span><?php endif; ?>
                </label>
                <label class="field">
                    <span class="field-label-with-help">Работа из каталога<?= field_help('work_entry.catalog_item') ?></span>
                    <select name="work_item_id">
                        <option value="">— ручная работа —</option>
                        <?php foreach ($workItems as $item): ?>
                            <?php
                            $iid = (string) $item['id'];
                            $itemLabel = (string) ($item['name'] ?? '');
                            if (!empty($item['category_name'])) {
                                $itemLabel = (string) $item['category_name'] . ' — ' . $itemLabel;
                            }
                            if ((int) ($item['is_active'] ?? 1) !== 1) {
                                $itemLabel .= ' (неактивна)';
                            }
                            ?>
                            <option value="<?= e($iid) ?>"<?= $selectedWorkItem === $iid ? ' selected' : '' ?>>
                                <?= e($itemLabel) ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                    <?php if (isset($errors['work_item_id'])): ?><span class="field-error"><?= e($errors['work_item_id']) ?></span><?php endif; ?>
                </label>
            </div>
            <p class="field-hint work-entry-catalogue-hint">
                Для ручной работы можно оставить каталог пустым и заполнить название/описание вручную.
            </p>

            <label class="field">
                <span class="field-label-with-help">Название<?= field_help('work_entry.title') ?></span>
                <input type="text" name="title" value="<?= e((string) ($old['title'] ?? '')) ?>" maxlength="240">
                <span class="field-hint">Если выбрана работа из каталога, название можно оставить пустым — оно подставится автоматически.</span>
                <?php if (isset($errors['title'])): ?><span class="field-error"><?= e($errors['title']) ?></span><?php endif; ?>
            </label>

            <label class="field">
                <span class="field-label-with-help">Описание<?= field_help('work_entry.description') ?></span>
                <textarea name="description" rows="4"><?= e((string) ($old['description'] ?? '')) ?></textarea>
                <?php if (isset($errors['description'])): ?><span class="field-error"><?= e($errors['description']) ?></span><?php endif; ?>
            </label>
        </fieldset>

        <fieldset class="work-entry-section">
            <legend class="work-entry-section__title">Статус и роль в отчете</legend>
            <div class="form-row">
                <label class="field">
                    <span class="field-label-with-help">Статус<?= field_help('work_entry.status') ?></span>
                    <select name="status" required>
                        <?php foreach ($statuses as $status): ?>
                            <option value="<?= e($status) ?>"<?= ((string) ($old['status'] ?? '') === $status) ? ' selected' : '' ?>>
                                <?= e(ui_work_entry_status_label($status)) ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                    <?php if (isset($errors['status'])): ?><span class="field-error"><?= e($errors['status']) ?></span><?php endif; ?>
                </label>
                <label class="field">
                    <span class="field-label-with-help">Роль в периоде<?= field_help('work_entry.period_role') ?></span>
                    <select name="period_role" required>
                        <?php foreach ($periodRoles as $role): ?>
                            <option value="<?= e($role) ?>"<?= ((string) ($old['period_role'] ?? '') === $role) ? ' selected' : '' ?>>
                                <?= e(ui_work_entry_period_role_label($role)) ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                    <?php if (isset($errors['period_role'])): ?><span class="field-error"><?= e($errors['period_role']) ?></span><?php endif; ?>
                </label>
                <label class="field">
                    <span class="field-label-with-help">Видимость для клиента<?= field_help('work_entry.client_visibility') ?></span>
                    <select name="client_visibility" required>
                        <?php foreach ($visibilities as $visibility): ?>
                            <option value="<?= e($visibility) ?>"<?= ((string) ($old['client_visibility'] ?? '') === $visibility) ? ' selected' : '' ?>>
                                <?= e(ui_work_entry_visibility_label($visibility)) ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                    <?php if (isset($errors['client_visibility'])): ?><span class="field-error"><?= e($errors['client_visibility']) ?></span><?php endif; ?>
                </label>
            </div>
        </fieldset>

        <fieldset class="work-entry-section">
            <legend class="work-entry-section__title">Комментарий для клиента</legend>
            <label class="field">
                <span class="field-label-with-help">Кратко для клиента<?= field_help('work_entry.client_summary') ?></span>
                <textarea name="client_summary" rows="3"><?= e((string) ($old['client_summary'] ?? '')) ?></textarea>
                <?php if (isset($errors['client_summary'])): ?><span class="field-error"><?= e($errors['client_summary']) ?></span><?php endif; ?>
            </label>
        </fieldset>

        <fieldset class="work-entry-section">
            <legend class="work-entry-section__title">Внутренние заметки</legend>
            <label class="field">
                <span class="field-label-with-help">Внутренняя заметка<?= field_help('work_entry.internal_note') ?></span>
                <textarea name="internal_note" rows="3"><?= e((string) ($old['internal_note'] ?? '')) ?></textarea>
                <?php if (isset($errors['internal_note'])): ?><span class="field-error"><?= e($errors['internal_note']) ?></span><?php endif; ?>
            </label>

            <label class="field">
                <span class="field-label-with-help">Заметка по доказательствам<?= field_help('work_entry.evidence_note') ?></span>
                <textarea name="evidence_note" rows="3"><?= e((string) ($old['evidence_note'] ?? '')) ?></textarea>
                <?php if (isset($errors['evidence_note'])): ?><span class="field-error"><?= e($errors['evidence_note']) ?></span><?php endif; ?>
            </label>
        </fieldset>

        <fieldset class="work-entry-section">
            <legend class="work-entry-section__title">Порядок</legend>
            <label class="field">
                <span class="field-label-with-help">Порядок<?= field_help('work_entry.sort_order') ?></span>
                <input type="number" name="sort_order" step="1" value="<?= e((string) ($old['sort_order'] ?? '100')) ?>">
                <?php if (isset($errors['sort_order'])): ?><span class="field-error"><?= e($errors['sort_order']) ?></span><?php endif; ?>
            </label>
        </fieldset>

        <div class="form-actions">
            <button type="submit" class="btn btn-primary">Сохранить</button>
            <a class="btn btn-secondary" href="<?= e($cancelHref) ?>">Отмена</a>
        </div>
    </form>
</section>

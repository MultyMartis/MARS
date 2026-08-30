<?php
declare(strict_types=1);
/** @var string $mode create|edit */
/** @var array<string, mixed>|null $period */
/** @var array<string, mixed> $old */
/** @var array<string, string> $errors */
/** @var string|null $formMessage */
/** @var list<array{id:int,name:string,slug:string,client_name:string}> $projects */
/** @var list<array{id:int,name:string,email:string}> $users */
/** @var list<string> $statuses */
/** @var array{project_id:bool,period_key:bool,dates:bool} $locks */
/** @var \Iseo\Services\CsrfService $csrf */

$isEdit = $mode === 'edit';
$action = $isEdit
    ? url_path('/reporting-periods/' . (int) $period['id'])
    : url_path('/reporting-periods');
?>
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
    <h2><?= $isEdit ? 'Редактирование отчетного периода' : 'Создание отчетного периода' ?></h2>
    <form class="rp-form" method="post" action="<?= e($action) ?>" novalidate>
        <?= $csrf->field() ?>

        <label>
            <span>Проект</span>
            <?php if ($locks['project_id']): ?>
                <input type="text" value="<?= e((string) ($period['project_name'] ?? '') . ' / ' . (string) ($period['client_name'] ?? '')) ?>" disabled>
                <input type="hidden" name="project_id" value="<?= e((string) $old['project_id']) ?>">
                <span class="field-hint">Проект нельзя изменить после создания.</span>
            <?php else: ?>
                <select name="project_id" required>
                    <option value="">Выберите проект…</option>
                    <?php foreach ($projects as $project): ?>
                        <option value="<?= e((string) $project['id']) ?>"<?= ((string) $old['project_id'] === (string) $project['id']) ? ' selected' : '' ?>>
                            <?= e($project['client_name'] . ' — ' . $project['name']) ?>
                        </option>
                    <?php endforeach; ?>
                </select>
                <?php if (isset($errors['project_id'])): ?><span class="field-error"><?= e($errors['project_id']) ?></span><?php endif; ?>
            <?php endif; ?>
        </label>

        <label>
            <span>Ключ периода (ГГГГ-ММ)</span>
            <input type="text" name="period_key" value="<?= e((string) $old['period_key']) ?>"<?= $locks['period_key'] ? ' readonly' : ' required' ?> pattern="\d{4}-(0[1-9]|1[0-2])" maxlength="7">
            <?php if ($locks['period_key']): ?><span class="field-hint">Ключ периода заблокирован после черновика.</span><?php endif; ?>
            <?php if (isset($errors['period_key'])): ?><span class="field-error"><?= e($errors['period_key']) ?></span><?php endif; ?>
        </label>

        <div class="form-row">
            <label>
                <span>Начало периода</span>
                <input type="date" name="period_start" value="<?= e((string) $old['period_start']) ?>"<?= $locks['dates'] ? ' readonly' : ' required' ?>>
                <?php if (isset($errors['period_start'])): ?><span class="field-error"><?= e($errors['period_start']) ?></span><?php endif; ?>
            </label>
            <label>
                <span>Конец периода</span>
                <input type="date" name="period_end" value="<?= e((string) $old['period_end']) ?>"<?= $locks['dates'] ? ' readonly' : ' required' ?>>
                <?php if (isset($errors['period_end'])): ?><span class="field-error"><?= e($errors['period_end']) ?></span><?php endif; ?>
            </label>
        </div>
        <?php if ($locks['dates']): ?><p class="field-hint">Даты заблокированы вне статусов черновик/активен.</p><?php endif; ?>

        <label>
            <span>Статус</span>
            <select name="status" required>
                <?php foreach ($statuses as $status): ?>
                    <option value="<?= e($status) ?>"<?= ((string) $old['status'] === $status) ? ' selected' : '' ?>><?= e(ui_status_label($status)) ?></option>
                <?php endforeach; ?>
            </select>
            <?php if (isset($errors['status'])): ?><span class="field-error"><?= e($errors['status']) ?></span><?php endif; ?>
        </label>

        <label>
            <span>Название</span>
            <input type="text" name="title" value="<?= e((string) $old['title']) ?>" maxlength="255">
            <?php if (isset($errors['title'])): ?><span class="field-error"><?= e($errors['title']) ?></span><?php endif; ?>
        </label>

        <label>
            <span>Краткое описание</span>
            <textarea name="summary" rows="4"><?= e((string) $old['summary']) ?></textarea>
            <?php if (isset($errors['summary'])): ?><span class="field-error"><?= e($errors['summary']) ?></span><?php endif; ?>
        </label>

        <div class="form-row">
            <label>
                <span>Ответственный</span>
                <select name="owner_user_id">
                    <option value="">— нет —</option>
                    <?php foreach ($users as $u): ?>
                        <option value="<?= e((string) $u['id']) ?>"<?= ((string) $old['owner_user_id'] === (string) $u['id']) ? ' selected' : '' ?>>
                            <?= e($u['name'] . ' · ' . $u['email']) ?>
                        </option>
                    <?php endforeach; ?>
                </select>
                <?php if (isset($errors['owner_user_id'])): ?><span class="field-error"><?= e($errors['owner_user_id']) ?></span><?php endif; ?>
            </label>
            <label>
                <span>Проверяющий</span>
                <select name="reviewer_user_id">
                    <option value="">— нет —</option>
                    <?php foreach ($users as $u): ?>
                        <option value="<?= e((string) $u['id']) ?>"<?= ((string) $old['reviewer_user_id'] === (string) $u['id']) ? ' selected' : '' ?>>
                            <?= e($u['name'] . ' · ' . $u['email']) ?>
                        </option>
                    <?php endforeach; ?>
                </select>
                <?php if (isset($errors['reviewer_user_id'])): ?><span class="field-error"><?= e($errors['reviewer_user_id']) ?></span><?php endif; ?>
            </label>
        </div>

        <p>
            <button class="btn btn-primary" type="submit"><?= $isEdit ? 'Сохранить изменения' : 'Создать период' ?></button>
            <a class="btn btn-secondary" href="<?= e($isEdit ? url_path('/reporting-periods/' . (int) $period['id']) : url_path('/reporting-periods')) ?>">Отмена</a>
        </p>
    </form>
</section>

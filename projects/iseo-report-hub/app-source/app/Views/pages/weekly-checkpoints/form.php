<?php
declare(strict_types=1);
/** @var string $mode create|edit */
/** @var array<string, mixed> $period */
/** @var array<string, mixed>|null $checkpoint */
/** @var array<string, mixed> $old */
/** @var array<string, string> $errors */
/** @var string|null $formMessage */
/** @var list<array{id:int,name:string,email:string}> $users */
/** @var list<string> $statuses */
/** @var bool $canAssignUsers */
/** @var array{reporting_period_id:bool,week_index:bool,checkpoint_key:bool,dates:bool,text:bool} $locks */
/** @var \Iseo\Services\CsrfService $csrf */

$isEdit = $mode === 'edit';
$periodId = (int) $period['id'];
$action = $isEdit
    ? url_path('/weekly-checkpoints/' . (int) $checkpoint['id'])
    : url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints');
$cancelHref = $isEdit
    ? url_path('/weekly-checkpoints/' . (int) $checkpoint['id'])
    : url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints');
?>
<section class="panel">
    <p class="note">
        Parent period:
        <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
            <code><?= e((string) $period['period_key']) ?></code>
        </a>
        · <?= e((string) $period['project_name']) ?> / <?= e((string) $period['client_name']) ?>
        · <?= e((string) $period['period_start']) ?> – <?= e((string) $period['period_end']) ?>
        · <a href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Checkpoint list</a>
    </p>
</section>

<?php if (!empty($formMessage) || $errors !== []): ?>
    <section class="panel flash flash-warn">
        <p><?= e((string) ($formMessage ?? 'Please correct the form errors.')) ?></p>
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
    <h2><?= $isEdit ? 'Edit weekly checkpoint' : 'Create weekly checkpoint' ?></h2>
    <form class="rp-form" method="post" action="<?= e($action) ?>" novalidate>
        <?= $csrf->field() ?>

        <label>
            <span>Reporting period</span>
            <input type="text" value="<?= e((string) $period['period_key'] . ' (id ' . $periodId . ')') ?>" disabled>
            <span class="field-hint">Parent period is immutable.</span>
        </label>

        <div class="form-row">
            <label>
                <span>Week index (1–6)</span>
                <input type="number" name="week_index" min="1" max="6" value="<?= e((string) $old['week_index']) ?>"<?= $locks['week_index'] ? ' readonly' : ' required' ?>>
                <?php if ($locks['week_index']): ?><span class="field-hint">Week index locked after draft.</span><?php endif; ?>
                <?php if (isset($errors['week_index'])): ?><span class="field-error"><?= e($errors['week_index']) ?></span><?php endif; ?>
            </label>
            <label>
                <span>Checkpoint key (YYYY-MM-WN)</span>
                <input type="text" name="checkpoint_key" value="<?= e((string) $old['checkpoint_key']) ?>" maxlength="32"<?= $locks['checkpoint_key'] ? ' readonly' : ' required' ?> pattern="\d{4}-(0[1-9]|1[0-2])-W[1-6]">
                <?php if ($locks['checkpoint_key']): ?><span class="field-hint">Checkpoint key locked after draft.</span><?php endif; ?>
                <?php if (isset($errors['checkpoint_key'])): ?><span class="field-error"><?= e($errors['checkpoint_key']) ?></span><?php endif; ?>
            </label>
        </div>

        <div class="form-row">
            <label>
                <span>Checkpoint start</span>
                <input type="date" name="checkpoint_start" value="<?= e((string) $old['checkpoint_start']) ?>"<?= $locks['dates'] ? ' readonly' : ' required' ?>>
                <?php if (isset($errors['checkpoint_start'])): ?><span class="field-error"><?= e($errors['checkpoint_start']) ?></span><?php endif; ?>
            </label>
            <label>
                <span>Checkpoint end</span>
                <input type="date" name="checkpoint_end" value="<?= e((string) $old['checkpoint_end']) ?>"<?= $locks['dates'] ? ' readonly' : ' required' ?>>
                <?php if (isset($errors['checkpoint_end'])): ?><span class="field-error"><?= e($errors['checkpoint_end']) ?></span><?php endif; ?>
            </label>
        </div>
        <?php if ($locks['dates']): ?><p class="field-hint">Dates locked outside draft/in_progress.</p><?php endif; ?>

        <label>
            <span>Status</span>
            <select name="status" required>
                <?php foreach ($statuses as $status): ?>
                    <option value="<?= e($status) ?>"<?= ((string) $old['status'] === $status) ? ' selected' : '' ?>><?= e($status) ?></option>
                <?php endforeach; ?>
            </select>
            <?php if (isset($errors['status'])): ?><span class="field-error"><?= e($errors['status']) ?></span><?php endif; ?>
            <span class="field-hint">No hard delete — use skipped or archived.</span>
        </label>

        <label>
            <span>Title</span>
            <input type="text" name="title" value="<?= e((string) $old['title']) ?>" maxlength="255"<?= $locks['text'] ? ' readonly' : ' required' ?>>
            <?php if (isset($errors['title'])): ?><span class="field-error"><?= e($errors['title']) ?></span><?php endif; ?>
        </label>

        <label>
            <span>Summary</span>
            <textarea name="summary" rows="3"<?= $locks['text'] ? ' readonly' : '' ?>><?= e((string) $old['summary']) ?></textarea>
            <?php if (isset($errors['summary'])): ?><span class="field-error"><?= e($errors['summary']) ?></span><?php endif; ?>
        </label>

        <label>
            <span>Work done</span>
            <textarea name="work_done" rows="3"<?= $locks['text'] ? ' readonly' : '' ?>><?= e((string) $old['work_done']) ?></textarea>
            <?php if (isset($errors['work_done'])): ?><span class="field-error"><?= e($errors['work_done']) ?></span><?php endif; ?>
        </label>

        <label>
            <span>Findings</span>
            <textarea name="findings" rows="3"<?= $locks['text'] ? ' readonly' : '' ?>><?= e((string) $old['findings']) ?></textarea>
            <?php if (isset($errors['findings'])): ?><span class="field-error"><?= e($errors['findings']) ?></span><?php endif; ?>
        </label>

        <label>
            <span>Next steps</span>
            <textarea name="next_steps" rows="3"<?= $locks['text'] ? ' readonly' : '' ?>><?= e((string) $old['next_steps']) ?></textarea>
            <?php if (isset($errors['next_steps'])): ?><span class="field-error"><?= e($errors['next_steps']) ?></span><?php endif; ?>
        </label>

        <label>
            <span>Risks</span>
            <textarea name="risks" rows="3"<?= $locks['text'] ? ' readonly' : '' ?>><?= e((string) $old['risks']) ?></textarea>
            <?php if (isset($errors['risks'])): ?><span class="field-error"><?= e($errors['risks']) ?></span><?php endif; ?>
        </label>

        <div class="form-row">
            <label>
                <span>Owner</span>
                <select name="owner_user_id"<?= $canAssignUsers ? '' : ' disabled' ?>>
                    <option value="">— none —</option>
                    <?php foreach ($users as $u): ?>
                        <option value="<?= e((string) $u['id']) ?>"<?= ((string) $old['owner_user_id'] === (string) $u['id']) ? ' selected' : '' ?>>
                            <?= e($u['name'] . ' · ' . $u['email']) ?>
                        </option>
                    <?php endforeach; ?>
                </select>
                <?php if (!$canAssignUsers): ?>
                    <input type="hidden" name="owner_user_id" value="<?= e((string) $old['owner_user_id']) ?>">
                <?php endif; ?>
                <?php if (isset($errors['owner_user_id'])): ?><span class="field-error"><?= e($errors['owner_user_id']) ?></span><?php endif; ?>
            </label>
            <label>
                <span>Reviewer</span>
                <select name="reviewer_user_id"<?= $canAssignUsers ? '' : ' disabled' ?>>
                    <option value="">— none —</option>
                    <?php foreach ($users as $u): ?>
                        <option value="<?= e((string) $u['id']) ?>"<?= ((string) $old['reviewer_user_id'] === (string) $u['id']) ? ' selected' : '' ?>>
                            <?= e($u['name'] . ' · ' . $u['email']) ?>
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
            <button class="btn" type="submit"><?= $isEdit ? 'Save changes' : 'Create checkpoint' ?></button>
            <a class="btn btn-secondary" href="<?= e($cancelHref) ?>">Cancel</a>
        </p>
    </form>
</section>

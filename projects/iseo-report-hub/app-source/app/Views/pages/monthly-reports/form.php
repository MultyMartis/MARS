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

$textFields = [
    'executive_summary' => 'Executive summary',
    'work_completed' => 'Work completed',
    'results_summary' => 'Results summary',
    'key_findings' => 'Key findings',
    'risks_and_blockers' => 'Risks and blockers',
    'next_month_plan' => 'Next month plan',
    'client_notes' => 'Client notes',
    'internal_notes' => 'Internal notes',
];
?>
<section class="panel">
    <p class="note">
        Parent period:
        <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
            <code><?= e((string) $period['period_key']) ?></code>
        </a>
        · <?= e((string) $period['project_name']) ?> / <?= e((string) $period['client_name']) ?>
        · <?= e((string) $period['period_start']) ?> – <?= e((string) $period['period_end']) ?>
        · <a href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Weekly checkpoints</a>
    </p>
</section>

<?php if ($parentFinalized): ?>
    <section class="panel locked-notice">
        <h2>Locked — finalized</h2>
        <p>This monthly report is finalized. Normal edits are blocked. Use <strong>Reopen</strong> on the monthly detail page (admin_owner) before editing.</p>
        <p><a class="btn btn-secondary" href="<?= e($cancelHref) ?>">Back to monthly report</a></p>
    </section>
<?php endif; ?>

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
    <h2><?= $isEdit ? 'Edit monthly report content' : 'Create monthly report content' ?></h2>
    <?php if ($formLocked): ?>
        <p class="note">Form locked while finalized.</p>
    <?php else: ?>
    <form class="rp-form mrc-form" method="post" action="<?= e($action) ?>" novalidate>
        <?= $csrf->field() ?>

        <label>
            <span>Reporting period</span>
            <input type="text" value="<?= e((string) $period['period_key'] . ' (id ' . $periodId . ')') ?>" disabled>
            <span class="field-hint">Parent period is immutable. One monthly report content row per period.</span>
        </label>

        <label>
            <span>Status</span>
            <select name="status" required>
                <?php foreach ($statuses as $status): ?>
                    <option value="<?= e($status) ?>"<?= ((string) $old['status'] === $status) ? ' selected' : '' ?>><?= e($status) ?></option>
                <?php endforeach; ?>
            </select>
            <?php if (isset($errors['status'])): ?><span class="field-error"><?= e($errors['status']) ?></span><?php endif; ?>
            <span class="field-hint">No hard delete — use archived.</span>
        </label>

        <label>
            <span>Title</span>
            <input type="text" name="title" value="<?= e((string) $old['title']) ?>" maxlength="255"<?= $locks['content'] ? ' readonly' : ' required' ?>>
            <?php if (isset($errors['title'])): ?><span class="field-error"><?= e($errors['title']) ?></span><?php endif; ?>
        </label>

        <fieldset class="mrc-source-fieldset"<?= $locks['source_ids'] ? ' disabled' : '' ?>>
            <legend>Source weekly checkpoints</legend>
            <?php if ($availableCheckpoints === []): ?>
                <p class="note">No weekly checkpoints in this period yet.</p>
            <?php else: ?>
                <ul class="mrc-source-list">
                    <?php foreach ($availableCheckpoints as $wc): ?>
                        <?php $wcId = (string) $wc['id']; ?>
                        <li>
                            <label class="mrc-source-item">
                                <input type="checkbox" name="source_weekly_checkpoint_ids[]" value="<?= e($wcId) ?>"<?= isset($selectedMap[$wcId]) ? ' checked' : '' ?>>
                                <span>
                                    <code><?= e((string) $wc['checkpoint_key']) ?></code>
                                    · <?= e((string) $wc['status']) ?>
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
            <span class="field-hint">Empty selection is allowed (warning on save). IDs must belong to this period.</span>
        </fieldset>
        <?php if ($locks['source_ids']): ?>
            <?php foreach ($selectedSource as $sid): ?>
                <input type="hidden" name="source_weekly_checkpoint_ids[]" value="<?= e((string) $sid) ?>">
            <?php endforeach; ?>
            <p class="field-hint">Source weekly checkpoints locked while finalized (admin_owner only).</p>
        <?php endif; ?>

        <?php foreach ($textFields as $name => $label): ?>
            <label>
                <span><?= e($label) ?></span>
                <textarea name="<?= e($name) ?>" rows="4"<?= $locks['content'] ? ' readonly' : '' ?>><?= e((string) ($old[$name] ?? '')) ?></textarea>
                <?php if (isset($errors[$name])): ?><span class="field-error"><?= e($errors[$name]) ?></span><?php endif; ?>
            </label>
        <?php endforeach; ?>

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
            <button class="btn" type="submit"><?= $isEdit ? 'Save changes' : 'Create monthly report' ?></button>
            <a class="btn btn-secondary" href="<?= e($cancelHref) ?>">Cancel</a>
        </p>
    </form>
    <?php endif; ?>
</section>

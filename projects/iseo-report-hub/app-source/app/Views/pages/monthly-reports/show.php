<?php
declare(strict_types=1);
/** @var array<string, mixed> $report */
/** @var array<string, mixed>|null $period */
/** @var list<array<string, mixed>> $sourceCheckpoints */
/** @var bool $canEdit */
/** @var list<array<string, mixed>> $reportBlocks */
/** @var bool $canCreateBlock */
/** @var bool $parentFinalized */
/** @var array<string, mixed> $readiness */
/** @var \Iseo\Services\CsrfService $csrf */
$periodId = (int) $report['reporting_period_id'];
$reportId = (int) $report['id'];
$sourceCheckpoints = $sourceCheckpoints ?? [];
$reportBlocks = $reportBlocks ?? [];
$canCreateBlock = $canCreateBlock ?? false;
$parentFinalized = !empty($parentFinalized);
$readiness = $readiness ?? ['ready' => false, 'gates' => [], 'failed_gates' => [], 'actions' => []];
$gates = is_array($readiness['gates'] ?? null) ? $readiness['gates'] : [];
$actions = is_array($readiness['actions'] ?? null) ? $readiness['actions'] : [];
$failedGates = is_array($readiness['failed_gates'] ?? null) ? $readiness['failed_gates'] : [];
?>
<section class="panel">
    <div class="panel-head">
        <h2>Monthly report — <?= e((string) ($report['period_key'] ?? '')) ?></h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">Parent period</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/reporting-periods/' . $periodId . '/weekly-checkpoints')) ?>">Weekly checkpoints</a>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">Report blocks</a>
            <a class="btn" href="<?= e(url_path('/monthly-reports/' . $reportId . '/preview')) ?>">Preview</a>
            <?php if ($canEdit): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/edit')) ?>">Edit</a>
            <?php endif; ?>
        </p>
    </div>
    <p>
        <span class="status-badge status-<?= e((string) $report['status']) ?>"><?= e((string) $report['status']) ?></span>
        <?php if ($parentFinalized): ?>
            <span class="finalized-badge">Finalized — locked</span>
        <?php endif; ?>
    </p>
</section>

<?php if ($parentFinalized): ?>
    <section class="panel locked-notice">
        <h2>Locked</h2>
        <p>This monthly report is <strong>finalized</strong>. Normal content and block edits are blocked. Preview/print remain available. Admin owner may reopen to unlock.</p>
    </section>
<?php endif; ?>

<section class="panel finalization-card">
    <div class="panel-head">
        <h2>Finalization</h2>
    </div>
    <ul class="facts">
        <li><strong>Status:</strong> <span class="status-badge status-<?= e((string) $report['status']) ?>"><?= e((string) $report['status']) ?></span></li>
        <li><strong>Finalized at:</strong> <?= e((string) ($report['finalized_at'] ?? '—')) ?></li>
        <li><strong>Readiness:</strong>
            <?php if (!empty($readiness['ready'])): ?>
                <span class="readiness-pass">PASS</span>
            <?php else: ?>
                <span class="readiness-fail">FAIL</span>
                <?php if ($failedGates !== []): ?>
                    · <?= e(implode(', ', array_map('strval', $failedGates))) ?>
                <?php endif; ?>
            <?php endif; ?>
        </li>
    </ul>

    <h3>Readiness checklist</h3>
    <?php if ($gates === []): ?>
        <p class="note">Readiness checklist unavailable.</p>
    <?php else: ?>
        <ul class="readiness-checklist">
            <?php foreach ($gates as $gateKey => $gate): ?>
                <?php
                $pass = !empty($gate['pass']);
                $detail = (string) ($gate['detail'] ?? '');
                ?>
                <li class="<?= $pass ? 'readiness-item--pass' : 'readiness-item--fail' ?>">
                    <span class="readiness-mark"><?= $pass ? 'PASS' : 'FAIL' ?></span>
                    <code><?= e((string) $gateKey) ?></code>
                    — <?= e($detail) ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <h3>Actions</h3>
    <div class="finalization-actions">
        <?php
        $actionDefs = [
            'submit_review' => [
                'label' => 'Submit for review',
                'path' => '/monthly-reports/' . $reportId . '/submit-review',
            ],
            'mark_reviewed' => [
                'label' => 'Mark reviewed',
                'path' => '/monthly-reports/' . $reportId . '/mark-reviewed',
            ],
            'finalize' => [
                'label' => 'Finalize',
                'path' => '/monthly-reports/' . $reportId . '/finalize',
            ],
            'reopen' => [
                'label' => 'Reopen',
                'path' => '/monthly-reports/' . $reportId . '/reopen',
            ],
        ];
        foreach ($actionDefs as $key => $def):
            $meta = is_array($actions[$key] ?? null) ? $actions[$key] : ['allowed' => false, 'reason' => 'Unavailable'];
            $allowed = !empty($meta['allowed']);
            $reason = $meta['reason'] ?? null;
            ?>
            <div class="finalization-action">
                <?php if ($allowed): ?>
                    <form method="post" action="<?= e(url_path($def['path'])) ?>">
                        <?= $csrf->field() ?>
                        <button type="submit" class="btn<?= $key === 'finalize' ? '' : ' btn-secondary' ?>"><?= e($def['label']) ?></button>
                    </form>
                <?php else: ?>
                    <button type="button" class="btn btn-secondary" disabled><?= e($def['label']) ?></button>
                    <?php if (is_string($reason) && $reason !== ''): ?>
                        <p class="field-hint"><?= e($reason) ?></p>
                    <?php endif; ?>
                <?php endif; ?>
            </div>
        <?php endforeach; ?>
    </div>
</section>

<section class="panel">
    <h2>Parent period</h2>
    <ul class="facts">
        <li><strong>Period:</strong>
            <a href="<?= e(url_path('/reporting-periods/' . $periodId)) ?>">
                <code><?= e((string) ($report['period_key'] ?? '')) ?></code>
            </a>
            · <span class="status-badge status-<?= e((string) ($report['period_status'] ?? '')) ?>"><?= e((string) ($report['period_status'] ?? '')) ?></span>
        </li>
        <li><strong>Project:</strong> <?= e((string) ($report['project_name'] ?? '—')) ?></li>
        <li><strong>Client:</strong> <?= e((string) ($report['client_name'] ?? '—')) ?></li>
        <li><strong>Period dates:</strong> <?= e((string) ($report['period_start'] ?? '')) ?> – <?= e((string) ($report['period_end'] ?? '')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Details</h2>
    <ul class="facts">
        <li><strong>ID:</strong> <?= e((string) $report['id']) ?></li>
        <li><strong>Title:</strong> <?= e((string) $report['title']) ?></li>
        <li><strong>Reviewed at:</strong> <?= e((string) ($report['reviewed_at'] ?? '—')) ?></li>
        <li><strong>Finalized at:</strong> <?= e((string) ($report['finalized_at'] ?? '—')) ?></li>
        <li><strong>Owner:</strong> <?= e((string) ($report['owner_name'] ?? '—')) ?><?php if (!empty($report['owner_email'])): ?> · <?= e((string) $report['owner_email']) ?><?php endif; ?></li>
        <li><strong>Reviewer:</strong> <?= e((string) ($report['reviewer_name'] ?? '—')) ?><?php if (!empty($report['reviewer_email'])): ?> · <?= e((string) $report['reviewer_email']) ?><?php endif; ?></li>
        <li><strong>Created by:</strong> <?= e((string) ($report['created_by_name'] ?? '—')) ?> · <?= e((string) ($report['created_at'] ?? '')) ?></li>
        <li><strong>Updated by:</strong> <?= e((string) ($report['updated_by_name'] ?? '—')) ?> · <?= e((string) ($report['updated_at'] ?? '')) ?></li>
    </ul>
</section>

<section class="panel">
    <h2>Source weekly checkpoints</h2>
    <?php if ($sourceCheckpoints === []): ?>
        <p class="note">No source weekly checkpoints linked.</p>
    <?php else: ?>
        <ul class="facts">
            <?php foreach ($sourceCheckpoints as $wc): ?>
                <li>
                    <a href="<?= e(url_path('/weekly-checkpoints/' . (int) $wc['id'])) ?>">
                        <code><?= e((string) $wc['checkpoint_key']) ?></code>
                    </a>
                    · <span class="status-badge status-<?= e((string) $wc['status']) ?>"><?= e((string) $wc['status']) ?></span>
                    · <?= e((string) $wc['title']) ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</section>

<section class="panel">
    <h2>Content</h2>
    <ul class="facts">
        <li><strong>Executive summary:</strong> <?= e((string) ($report['executive_summary'] ?? '—')) ?></li>
        <li><strong>Work completed:</strong> <?= e((string) ($report['work_completed'] ?? '—')) ?></li>
        <li><strong>Results summary:</strong> <?= e((string) ($report['results_summary'] ?? '—')) ?></li>
        <li><strong>Key findings:</strong> <?= e((string) ($report['key_findings'] ?? '—')) ?></li>
        <li><strong>Risks and blockers:</strong> <?= e((string) ($report['risks_and_blockers'] ?? '—')) ?></li>
        <li><strong>Next month plan:</strong> <?= e((string) ($report['next_month_plan'] ?? '—')) ?></li>
        <li><strong>Client notes:</strong> <?= e((string) ($report['client_notes'] ?? '—')) ?></li>
        <li><strong>Internal notes:</strong> <?= e((string) ($report['internal_notes'] ?? '—')) ?></li>
    </ul>
</section>

<section class="panel">
    <div class="panel-head">
        <h2>Report blocks</h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks')) ?>">Open block list</a>
            <?php if ($canCreateBlock): ?>
                <a class="btn" href="<?= e(url_path('/monthly-reports/' . $reportId . '/blocks/create')) ?>">Create block</a>
            <?php endif; ?>
        </p>
    </div>
    <?php if ($reportBlocks === []): ?>
        <p class="note">No report blocks yet.</p>
    <?php else: ?>
        <div class="table-wrap">
            <table class="data-table">
                <thead>
                <tr>
                    <th>Sort</th>
                    <th>Key</th>
                    <th>Type</th>
                    <th>Title</th>
                    <th>Status</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ($reportBlocks as $rb): ?>
                    <?php
                    $bid = (int) $rb['id'];
                    $canEditBlock = !empty($rb['_can_edit']);
                    ?>
                    <tr>
                        <td><?= e((string) $rb['sort_order']) ?></td>
                        <td><code><?= e((string) $rb['block_key']) ?></code></td>
                        <td><span class="type-badge"><?= e((string) $rb['block_type']) ?></span></td>
                        <td><?= e((string) $rb['title']) ?></td>
                        <td><span class="status-badge status-<?= e((string) $rb['status']) ?>"><?= e((string) $rb['status']) ?></span></td>
                        <td class="actions">
                            <a href="<?= e(url_path('/report-blocks/' . $bid)) ?>">View</a>
                            <?php if ($canEditBlock): ?>
                                · <a href="<?= e(url_path('/report-blocks/' . $bid . '/edit')) ?>">Edit</a>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    <?php endif; ?>
</section>

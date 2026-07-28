<?php
declare(strict_types=1);

/** @var array<string, mixed> $export */
/** @var list<array<string, mixed>> $shares */
/** @var array<string, mixed>|null $activeShare */
/** @var array{eligible?:bool,reason?:string,code?:string} $eligibility */
/** @var bool $canManage */
/** @var string|null $plaintextShareUrl */
/** @var \Iseo\Services\CsrfService $csrf */

$export = $export ?? [];
$shares = $shares ?? [];
$activeShare = is_array($activeShare ?? null) ? $activeShare : null;
$eligibility = is_array($eligibility ?? null) ? $eligibility : [];
$canManage = !empty($canManage);
$plaintextShareUrl = is_string($plaintextShareUrl ?? null) ? $plaintextShareUrl : null;

$exportId = (int) ($export['id'] ?? 0);
$snapshotId = (int) ($export['report_snapshot_id'] ?? 0);
$eligible = !empty($eligibility['eligible']);
$reason = (string) ($eligibility['reason'] ?? '');
$format = (string) ($export['format'] ?? '');
?>
<section class="panel export-card share-card">
    <div class="panel-head">
        <h2>Public share links</h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/report-exports/' . $exportId)) ?>">Export detail</a>
            <?php if ($snapshotId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">All exports</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Internal manage</span>
        <?php if ($eligible): ?>
            <span class="share-badge share-badge--eligible">Shareable PDF</span>
        <?php else: ?>
            <span class="share-badge share-badge--blocked">Not shareable</span>
        <?php endif; ?>
        · Export <code><?= e((string) ($export['export_key'] ?? '')) ?></code>
        · Format <code><?= e($format) ?></code>
    </p>

    <p class="field-hint share-hint">
        <?= e($eligible ? $reason : ('Not eligible: ' . $reason)) ?>
        Token plaintext is shown once after create. Only the token hash is stored.
        No client portal. No email delivery.
    </p>

    <?php if ($plaintextShareUrl !== null && $plaintextShareUrl !== ''): ?>
        <div class="share-once-box" data-share-once>
            <p><strong>Copy this public URL now</strong> — it will not be shown again.</p>
            <div class="share-once-row">
                <input
                    type="text"
                    class="share-url-input"
                    readonly
                    autocomplete="off"
                    spellcheck="false"
                    value="<?= e($plaintextShareUrl) ?>"
                    data-share-url
                    aria-label="Public share URL"
                >
                <button type="button" class="btn" data-share-copy>Copy</button>
            </div>
            <p class="field-hint">Default expiry: 30 days. Revoke anytime from this page.</p>
        </div>
    <?php endif; ?>

    <?php if ($canManage && $eligible && $activeShare === null): ?>
        <form method="post" action="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>" class="share-create-form">
            <?= $csrf->field() ?>
            <label for="token_label">Optional label</label>
            <input type="text" id="token_label" name="token_label" maxlength="150" placeholder="e.g. Client handoff July">
            <button type="submit" class="btn">Create public share link</button>
        </form>
    <?php elseif ($canManage && $eligible && $activeShare !== null): ?>
        <p class="export-ready-note">An active share exists. Revoke it before creating a new link. Plaintext token is not recoverable.</p>
    <?php elseif (!$canManage): ?>
        <p class="field-hint">Share create/revoke requires admin_owner or seo_lead_reviewer.</p>
    <?php endif; ?>

    <?php if ($shares === []): ?>
        <p class="note">No share rows for this export yet.</p>
    <?php else: ?>
        <div class="table-wrap">
            <table class="data-table share-table">
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Status</th>
                    <th>Label</th>
                    <th>Expires</th>
                    <th>Access count</th>
                    <th>Last access</th>
                    <th>Created</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ($shares as $row): ?>
                    <?php
                    if (!is_array($row)) {
                        continue;
                    }
                    $sid = (int) ($row['id'] ?? 0);
                    $status = (string) ($row['status'] ?? '');
                    $label = (string) ($row['token_label'] ?? '');
                    ?>
                    <tr>
                        <td><?= e((string) $sid) ?></td>
                        <td><span class="status-badge status-<?= e($status) ?>"><?= e($status) ?></span></td>
                        <td><?= e($label !== '' ? $label : '—') ?></td>
                        <td><?= e((string) ($row['expires_at'] ?? '—')) ?></td>
                        <td><?= e((string) (int) ($row['access_count'] ?? 0)) ?></td>
                        <td><?= e((string) ($row['last_accessed_at'] ?? '—')) ?></td>
                        <td><?= e((string) ($row['created_at'] ?? '—')) ?></td>
                        <td class="actions">
                            <?php if ($canManage && $status === 'active'): ?>
                                <form method="post" action="<?= e(url_path('/report-export-shares/' . $sid . '/revoke')) ?>" class="inline-form">
                                    <?= $csrf->field() ?>
                                    <button type="submit" class="btn btn-secondary btn-revoke">Revoke</button>
                                </form>
                            <?php else: ?>
                                <span class="meta-muted">—</span>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    <?php endif; ?>
</section>

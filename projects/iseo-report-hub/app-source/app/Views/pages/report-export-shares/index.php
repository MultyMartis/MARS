<?php
declare(strict_types=1);

/** @var array<string, mixed> $export */
/** @var list<array<string, mixed>> $shares */
/** @var array<string, mixed>|null $activeShare */
/** @var array{eligible?:bool,reason?:string,code?:string} $eligibility */
/** @var bool $canManage */
/** @var string|null $plaintextShareUrl */
/** @var array<string, mixed>|null $handoff */
/** @var \Iseo\Services\CsrfService $csrf */

$export = $export ?? [];
$shares = $shares ?? [];
$activeShare = is_array($activeShare ?? null) ? $activeShare : null;
$eligibility = is_array($eligibility ?? null) ? $eligibility : [];
$canManage = !empty($canManage);
$plaintextShareUrl = is_string($plaintextShareUrl ?? null) ? $plaintextShareUrl : null;
$handoff = is_array($handoff ?? null) ? $handoff : null;

$exportId = (int) ($export['id'] ?? 0);
$snapshotId = (int) ($export['report_snapshot_id'] ?? 0);
$eligible = !empty($eligibility['eligible']);
$reason = (string) ($eligibility['reason'] ?? '');
$format = (string) ($export['format'] ?? '');

$hCtx = is_array($handoff['context'] ?? null) ? $handoff['context'] : [];
$hShare = is_array($handoff['share_status'] ?? null) ? $handoff['share_status'] : [];
$hChecks = is_array($handoff['checklist'] ?? null) ? $handoff['checklist'] : [];
$hWarnings = is_array($handoff['warnings'] ?? null) ? $handoff['warnings'] : [];
$copyPack = is_array($handoff['copy_pack'] ?? null) ? $handoff['copy_pack'] : null;
$urlLost = is_string($handoff['url_lost_guidance'] ?? null) ? (string) $handoff['url_lost_guidance'] : '';
$onceAvailable = $plaintextShareUrl !== null && $plaintextShareUrl !== '';
?>
<section class="panel export-card handoff-panel" data-handoff-panel>
    <div class="panel-head">
        <h2>Client handoff readiness</h2>
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
            <span class="share-badge share-badge--eligible">Shareable</span>
        <?php else: ?>
            <span class="share-badge share-badge--blocked" title="<?= e($reason) ?>">Not shareable</span>
        <?php endif; ?>
        · Export <code><?= e((string) ($export['export_key'] ?? '')) ?></code>
        · Format <code><?= e($format) ?></code>
    </p>

    <?php if (!$eligible): ?>
        <p class="field-hint handoff-not-ready">Not eligible: <?= e($reason) ?>. No handoff copy pack. Not delivery ready.</p>
    <?php endif; ?>

    <ul class="facts handoff-context-list">
        <li><strong>Client:</strong> <?= e((string) ($hCtx['client_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Project:</strong> <?= e((string) ($hCtx['project_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Period:</strong> <?= e((string) ($hCtx['period'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Report status:</strong> <?= e((string) ($hCtx['report_status'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Snapshot key:</strong> <code><?= e((string) ($hCtx['snapshot_key'] ?? 'SAFE UNKNOWN')) ?></code></li>
        <li><strong>Export:</strong> id <?= e((string) $exportId) ?> · <code><?= e((string) ($export['export_key'] ?? '')) ?></code></li>
        <li><strong>Export format:</strong> <code><?= e((string) ($hCtx['format'] ?? $format)) ?></code></li>
        <li><strong>Template:</strong> <?= e((string) ($hCtx['template_label'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Share status:</strong>
            <?php if (!empty($hShare['has_active'])): ?>
                active exists
                <?php if (!empty($hShare['expires_at'])): ?>
                    · expires <code><?= e((string) $hShare['expires_at']) ?></code>
                <?php endif; ?>
            <?php else: ?>
                no active share
            <?php endif; ?>
            <?php if ((int) ($hShare['revoked_count'] ?? 0) > 0): ?>
                · revoked rows: <?= e((string) (int) $hShare['revoked_count']) ?>
            <?php endif; ?>
        </li>
    </ul>

    <?php if ($hChecks !== []): ?>
        <h3 class="handoff-subhead">Readiness checklist</h3>
        <ul class="handoff-checklist">
            <?php foreach ($hChecks as $item): ?>
                <?php if (!is_array($item)) { continue; } ?>
                <li class="<?= !empty($item['pass']) ? 'check-pass' : 'check-fail' ?>">
                    <span class="check-mark"><?= !empty($item['pass']) ? '✓' : '○' ?></span>
                    <?= e((string) ($item['label'] ?? '')) ?>
                    <span class="meta-muted">— <?= e((string) ($item['note'] ?? '')) ?></span>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <?php if ($hWarnings !== []): ?>
        <h3 class="handoff-subhead">Warnings</h3>
        <ul class="handoff-warnings">
            <?php foreach ($hWarnings as $w): ?>
                <li><?= e((string) $w) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</section>

<section class="panel export-card share-card">
    <div class="panel-head">
        <h2>Public share links</h2>
    </div>

    <p class="field-hint share-hint">
        <?= e($eligible ? $reason : ('Not eligible: ' . $reason)) ?>
        Token plaintext is shown once after create. Only the token hash is stored.
        No client portal. No email delivery.
    </p>

    <?php if ($onceAvailable): ?>
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
                <button type="button" class="btn" data-share-copy>Copy URL</button>
            </div>
            <p class="field-hint">Default expiry: 30 days. Revoke anytime from this page.</p>
        </div>

        <?php if (is_array($copyPack)): ?>
            <div class="handoff-copy-pack" data-handoff-copy-pack>
                <h3 class="handoff-subhead">Client handoff copy pack</h3>
                <p class="field-hint">Russian templates filled from fixture context. Do not include storage paths or token hashes.</p>

                <div class="copy-pack-block">
                    <label for="copy-short">Short messenger message</label>
                    <textarea id="copy-short" class="copy-pack-text" readonly autocomplete="off" spellcheck="false" data-copy-target><?= e((string) ($copyPack['short_message'] ?? '')) ?></textarea>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Copy short message</button>
                </div>

                <div class="copy-pack-block">
                    <label for="copy-email-subject">Formal email — subject</label>
                    <input id="copy-email-subject" type="text" class="share-url-input" readonly autocomplete="off" spellcheck="false" value="<?= e((string) ($copyPack['email_subject'] ?? '')) ?>" data-copy-target>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Copy subject</button>
                </div>

                <div class="copy-pack-block">
                    <label for="copy-email-body">Formal email — body</label>
                    <textarea id="copy-email-body" class="copy-pack-text" readonly autocomplete="off" spellcheck="false" data-copy-target><?= e((string) ($copyPack['email_body'] ?? '')) ?></textarea>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Copy email body</button>
                </div>

                <div class="copy-pack-block">
                    <label for="copy-internal">Internal operator note</label>
                    <textarea id="copy-internal" class="copy-pack-text" readonly autocomplete="off" spellcheck="false" data-copy-target><?= e((string) ($copyPack['internal_note'] ?? '')) ?></textarea>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Copy internal note</button>
                </div>
            </div>
        <?php endif; ?>
    <?php elseif ($urlLost !== ''): ?>
        <p class="handoff-once-gone" role="status"><?= e($urlLost) ?></p>
    <?php endif; ?>

    <?php if ($canManage && $eligible && $activeShare === null): ?>
        <form method="post" action="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>" class="share-create-form">
            <?= $csrf->field() ?>
            <label for="token_label">Optional label</label>
            <input type="text" id="token_label" name="token_label" maxlength="150" placeholder="e.g. Client handoff July">
            <button type="submit" class="btn">Create share for handoff</button>
        </form>
    <?php elseif ($canManage && $eligible && $activeShare !== null): ?>
        <p class="export-ready-note">An active share exists. If the URL was lost, revoke it and create a new link. Plaintext token is not recoverable from the database.</p>
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

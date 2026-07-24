<?php
declare(strict_types=1);
/** @var array<string, mixed> $status */
$db = is_array($status['db'] ?? null) ? $status['db'] : [];
$overall = (string) ($status['overall'] ?? 'unknown');
?>
<section class="panel">
    <h2>Overall</h2>
    <p>
        <span class="badge badge-<?= e($overall) ?>"><?= e($overall) ?></span>
    </p>
</section>

<section class="panel">
    <h2>Runtime / PHP</h2>
    <ul class="facts">
        <li><strong>PHP running:</strong> yes</li>
        <li><strong>PHP version:</strong> <?= e((string) $status['php_version']) ?></li>
        <li><strong>SAPI:</strong> <?= e((string) $status['sapi']) ?></li>
        <li><strong>App:</strong> <?= e((string) $status['app_skeleton']) ?></li>
        <li><strong>.env.local present:</strong> <?= !empty($status['env_local_present']) ? 'yes' : 'no' ?></li>
        <li><strong>.env required:</strong> no</li>
        <li><strong>WordPress:</strong> <?= e((string) $status['wordpress']) ?></li>
        <li><strong>Required extensions:</strong>
            <span class="<?= !empty($status['all_required_ok']) ? 'ok' : 'warn' ?>">
                <?= !empty($status['all_required_ok']) ? 'all present' : 'missing one or more' ?>
            </span>
        </li>
    </ul>
</section>

<section class="panel">
    <h2>Database (safe status)</h2>
    <ul class="facts">
        <li><strong>DB configured:</strong> <?= !empty($db['configured']) ? 'yes' : 'no' ?></li>
        <li><strong>DB connection:</strong>
            <span class="badge badge-<?= e((string) ($db['connection_label'] ?? 'n/a')) ?>">
                <?= e((string) ($db['connection_label'] ?? 'n/a')) ?>
            </span>
        </li>
        <li><strong>DB name:</strong> <?= e((string) ($db['database'] ?? '—')) ?></li>
        <li><strong>Migration count:</strong> <?= e((string) ($db['migration_count'] ?? '—')) ?></li>
        <li><strong>Latest migration:</strong> <?= e((string) ($db['latest_migration'] ?? '—')) ?></li>
        <li><strong>Tables present / expected:</strong>
            <?= e((string) ($db['tables_present'] ?? '—')) ?> /
            <?= e((string) ($db['tables_expected'] ?? '—')) ?>
        </li>
        <li><strong>Users count:</strong> <?= e((string) ($db['users_count'] ?? '—')) ?></li>
        <li><strong>Roles count:</strong> <?= e((string) ($db['roles_count'] ?? '—')) ?></li>
        <li><strong>DB status:</strong> <?= e((string) ($db['status'] ?? 'unknown')) ?></li>
    </ul>
    <p class="note">Credentials, DSN with password, and SQL exception details are never shown here.</p>
</section>

<section class="panel">
    <h2>Required extensions</h2>
    <ul class="ext-list">
        <?php foreach ($status['required'] as $name => $present): ?>
            <li class="<?= $present ? 'ok' : 'missing' ?>">
                <?= e((string) $name) ?> — <?= $present ? 'present' : 'missing' ?>
            </li>
        <?php endforeach; ?>
    </ul>
</section>

<section class="panel">
    <h2>Optional extensions</h2>
    <ul class="ext-list">
        <?php foreach ($status['optional'] as $name => $present): ?>
            <li class="<?= $present ? 'ok' : 'warn' ?>">
                <?= e((string) $name) ?> — <?= $present ? 'present' : 'absent' ?>
            </li>
        <?php endforeach; ?>
    </ul>
    <p><a class="btn btn-secondary" href="<?= e(url_path('/')) ?>">Back to dashboard</a></p>
</section>

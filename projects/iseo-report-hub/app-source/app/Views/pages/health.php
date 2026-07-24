<?php
declare(strict_types=1);
/** @var array<string, mixed> $status */
?>
<section class="panel">
    <h2>Runtime / PHP</h2>
    <ul class="facts">
        <li><strong>PHP running:</strong> yes</li>
        <li><strong>PHP version:</strong> <?= e((string) $status['php_version']) ?></li>
        <li><strong>SAPI:</strong> <?= e((string) $status['sapi']) ?></li>
        <li><strong>App skeleton:</strong> <?= e((string) $status['app_skeleton']) ?></li>
        <li><strong>Database:</strong> <?= e((string) $status['db_status']) ?></li>
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

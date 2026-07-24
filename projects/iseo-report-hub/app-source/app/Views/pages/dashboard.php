<?php
declare(strict_types=1);
/** @var list<array{title:string,status:string,detail:string}> $cards */
/** @var string $authStatus */
?>
<section class="panel">
    <h2>Project status</h2>
    <p class="note">Source-only Phase 1A dashboard stub. No database. No runtime sync.</p>
    <p class="note"><strong>Auth:</strong> <?= e($authStatus) ?></p>
</section>

<section class="status-grid">
    <?php foreach ($cards as $card): ?>
        <article class="panel status-card status-<?= e($card['status']) ?>">
            <h2><?= e($card['title']) ?></h2>
            <p class="status-pill"><?= e($card['status']) ?></p>
            <p><?= e($card['detail']) ?></p>
        </article>
    <?php endforeach; ?>
</section>

<section class="panel">
    <h2>Quick links</h2>
    <p>
        <a class="btn" href="<?= e(url_path('/health')) ?>">Health</a>
        <a class="btn btn-secondary" href="<?= e(url_path('/login')) ?>">Login stub</a>
    </p>
</section>

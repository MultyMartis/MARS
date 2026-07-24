<?php
declare(strict_types=1);
/** @var list<array{title:string,status:string,detail:string}> $cards */
/** @var array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user */
/** @var string $authStatus */
?>
<section class="panel">
    <h2>Dashboard</h2>
    <p class="note"><strong>Auth:</strong> <?= e($authStatus) ?></p>
    <?php if (is_array($user)): ?>
        <ul class="facts">
            <li><strong>Name:</strong> <?= e($user['name']) ?></li>
            <li><strong>Email:</strong> <?= e($user['email']) ?></li>
            <li><strong>Roles:</strong> <?= e(implode(', ', $user['roles'])) ?></li>
        </ul>
    <?php endif; ?>
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
        <a class="btn btn-secondary" href="<?= e(url_path('/logout')) ?>">Logout</a>
    </p>
</section>

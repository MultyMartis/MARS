<?php
declare(strict_types=1);
/** @var string $warning */
/** @var bool $authImplemented */
/** @var \Iseo\Services\CsrfService $csrf */
?>
<section class="panel">
    <h2>Login</h2>
    <p class="flash flash-warn"><?= e($warning) ?></p>
    <p class="note">Auth status: <?= e($authImplemented ? 'implemented' : 'not implemented') ?> · no password verification · no DB</p>

    <form class="login-form" method="post" action="<?= e(url_path('/login')) ?>" autocomplete="off">
        <?= $csrf->field() ?>
        <label>
            <span>Email</span>
            <input type="email" name="email" placeholder="operator@example.local" required>
        </label>
        <label>
            <span>Password</span>
            <input type="password" name="password" placeholder="not checked in Phase 1A" required>
        </label>
        <button class="btn" type="submit">Submit (stub)</button>
    </form>
</section>

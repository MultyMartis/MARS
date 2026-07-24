<?php
declare(strict_types=1);
/** @var bool $authImplemented */
/** @var \Iseo\Services\CsrfService $csrf */
?>
<section class="panel">
    <h2>Login</h2>
    <p class="note">
        Local DB-backed authentication.
        <?= $authImplemented ? 'Auth is implemented.' : 'Auth not implemented.' ?>
    </p>

    <form class="login-form" method="post" action="<?= e(url_path('/login')) ?>" autocomplete="username">
        <?= $csrf->field() ?>
        <label>
            <span>Email</span>
            <input type="email" name="email" required autocomplete="username">
        </label>
        <label>
            <span>Password</span>
            <input type="password" name="password" required autocomplete="current-password">
        </label>
        <button class="btn" type="submit">Sign in</button>
    </form>
</section>

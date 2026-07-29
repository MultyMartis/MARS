<?php
declare(strict_types=1);
/** @var bool $authImplemented */
/** @var \Iseo\Services\CsrfService $csrf */
?>
<section class="panel">
    <h2>Вход</h2>
    <p class="note">
        Локальный вход для сотрудников i-SEO.
        <?= $authImplemented ? 'Авторизация подключена.' : 'Авторизация пока не подключена.' ?>
    </p>

    <form class="login-form" method="post" action="<?= e(url_path('/login')) ?>" autocomplete="username">
        <?= $csrf->field() ?>
        <label>
            <span>Email</span>
            <input type="email" name="email" required autocomplete="username">
        </label>
        <label>
            <span>Пароль</span>
            <input type="password" name="password" required autocomplete="current-password">
        </label>
        <button class="btn" type="submit">Войти</button>
    </form>
</section>

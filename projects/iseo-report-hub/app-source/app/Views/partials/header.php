<?php
declare(strict_types=1);
/** @var string $appName */
/** @var string $phaseLabel */
/** @var array|null $currentUser */
?>
<header class="site-header">
    <div class="container header-row">
        <div>
            <p class="brand">INTLSEO / i-SEO</p>
            <h1><?= e($appName) ?></h1>
            <p class="tagline"><?= e($phaseLabel) ?></p>
        </div>
        <nav class="site-nav" aria-label="Основная навигация">
            <?php if ($currentUser !== null): ?>
                <a href="<?= e(url_path('/')) ?>">Главная</a>
                <a href="<?= e(url_path('/reporting-periods')) ?>">Отчетные периоды</a>
            <?php endif; ?>
            <a href="<?= e(url_path('/health')) ?>">Состояние системы</a>
            <?php if ($currentUser !== null): ?>
                <span class="nav-user"><?= e(($currentUser['name'] ?? 'Пользователь') . ' · ' . ($currentUser['email'] ?? '')) ?></span>
                <a href="<?= e(url_path('/logout')) ?>">Выйти</a>
            <?php else: ?>
                <a href="<?= e(url_path('/login')) ?>">Вход</a>
            <?php endif; ?>
        </nav>
    </div>
</header>

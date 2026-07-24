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
        <nav class="site-nav" aria-label="Main">
            <a href="<?= e(url_path('/')) ?>">Dashboard</a>
            <a href="<?= e(url_path('/health')) ?>">Health</a>
            <a href="<?= e(url_path('/login')) ?>">Login</a>
            <?php if ($currentUser !== null): ?>
                <a href="<?= e(url_path('/logout')) ?>">Logout</a>
                <span class="nav-user"><?= e($currentUser['name'] ?? 'User') ?></span>
            <?php endif; ?>
        </nav>
    </div>
</header>

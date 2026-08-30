<?php
declare(strict_types=1);
/** @var string $appName */
/** @var string $pageTitle */
/** @var array|null $currentUser */
?>
<header class="app-topbar topbar">
    <div class="topbar__left">
        <button type="button" class="sidebar-toggle" data-sidebar-toggle aria-controls="app-sidebar" aria-expanded="false" aria-label="Меню">
            Меню
        </button>
        <h1 class="topbar__title page-header"><?= e((string) ($pageTitle ?? $appName)) ?></h1>
    </div>
    <div class="topbar__meta">
        <?php if ($currentUser !== null): ?>
            <span class="nav-user"><?= e(ui_display_user_name($currentUser['name'] ?? null, $currentUser['email'] ?? null)) ?><?php if (!empty($currentUser['email'])): ?> · <?= e((string) $currentUser['email']) ?><?php endif; ?></span>
            <a class="btn btn-secondary btn-sm" href="<?= e(url_path('/logout')) ?>">Выйти</a>
        <?php else: ?>
            <a class="btn btn-primary btn-sm" href="<?= e(url_path('/login')) ?>">Вход</a>
        <?php endif; ?>
    </div>
</header>

<?php
declare(strict_types=1);
/** @var array|null $currentUser */
/** @var string $appName */

$path = request_path();
$authed = $currentUser !== null;
$isPrivileged = is_array($currentUser)
    && (
        in_array('admin_owner', $currentUser['roles'] ?? [], true)
        || in_array('seo_lead_reviewer', $currentUser['roles'] ?? [], true)
    );

$isActive = static function (string $prefix) use ($path): bool {
    if ($prefix === '/') {
        return $path === '/';
    }
    return $path === $prefix || str_starts_with($path, $prefix . '/');
};

$linkClass = static function (bool $active): string {
    return $active ? 'is-active' : '';
};
?>
<aside class="app-sidebar sidebar" id="app-sidebar" aria-label="Боковая навигация">
    <div class="app-sidebar__brand sidebar__brand">
        <p class="sidebar__brand-mark">INTLSEO</p>
        <p class="sidebar__brand-title"><?= e($appName) ?></p>
        <p class="sidebar__brand-sub">локальная тестовая среда</p>
    </div>

    <nav class="app-sidebar__nav sidebar__nav">
        <p class="sidebar__section-label">Главное</p>
        <?php if ($authed): ?>
            <a href="<?= e(url_path('/')) ?>" class="<?= e($linkClass($isActive('/'))) ?>">Главная</a>
        <?php else: ?>
            <a href="<?= e(url_path('/login')) ?>" class="<?= e($linkClass($isActive('/login'))) ?>">Вход</a>
        <?php endif; ?>

        <?php if ($authed): ?>
            <p class="sidebar__section-label">Отчеты</p>
            <a href="<?= e(url_path('/reporting-periods')) ?>" class="<?= e($linkClass($isActive('/reporting-periods'))) ?>">Отчетные периоды</a>

            <?php if ($isPrivileged): ?>
                <p class="sidebar__section-label">Администрирование</p>
                <a href="<?= e(url_path('/health')) ?>" class="<?= e($linkClass($isActive('/health'))) ?>">Состояние системы</a>
            <?php endif; ?>
        <?php else: ?>
            <p class="sidebar__section-label">Проверка</p>
            <a href="<?= e(url_path('/health')) ?>" class="<?= e($linkClass($isActive('/health'))) ?>">Состояние системы</a>
        <?php endif; ?>
    </nav>

    <?php if ($authed): ?>
        <div class="sidebar-status-block" role="status" aria-label="Статус доставки отчета">
            <p class="sidebar-status-block__label">
                Доставка
                <span class="sidebar-status-block__later">Позже</span>
            </p>
            <p class="sidebar-status-block__item">PDF ещё не создан</p>
            <p class="sidebar-status-block__item">Публичная ссылка ещё не создана</p>
        </div>
    <?php endif; ?>

    <div class="app-sidebar__footer sidebar__footer">
        Локальная среда · не продакшен
    </div>
</aside>

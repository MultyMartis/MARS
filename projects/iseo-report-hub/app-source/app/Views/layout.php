<?php
declare(strict_types=1);
/** @var string $content */
/** @var string $appName */
/** @var string $phaseLabel */
/** @var string $pageTitle */
/** @var array|null $currentUser */
/** @var string $authStatus */
$isLoginPage = (request_path() === '/login');
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?= e(($pageTitle ?? 'App') . ' — ' . $appName) ?></title>
    <link rel="stylesheet" href="<?= e(url_path('/assets/css/app.css')) ?>">
</head>
<body data-phase="local-ux" class="iseo-shell<?= $isLoginPage ? ' iseo-shell--login' : '' ?>">
<?php if ($isLoginPage): ?>
    <div class="login-shell">
        <div class="login-shell__brand">
            <p class="login-shell__mark">INTLSEO</p>
            <h1 class="login-shell__title"><?= e($appName) ?></h1>
            <p class="login-shell__sub">локальная тестовая среда</p>
        </div>
        <main class="login-shell__main">
            <?php require app_path('Views/partials/flash.php'); ?>
            <?= $content ?>
        </main>
        <p class="login-shell__footer">Локальная среда · не продакшен</p>
    </div>
<?php else: ?>
    <div class="app-shell admin-shell">
        <?php require app_path('Views/partials/sidebar.php'); ?>
        <div class="app-main admin-main">
            <?php require app_path('Views/partials/header.php'); ?>
            <main class="page-content container">
                <?php require app_path('Views/partials/flash.php'); ?>
                <?= $content ?>
            </main>
            <?php require app_path('Views/partials/footer.php'); ?>
        </div>
    </div>
<?php endif; ?>
<script src="<?= e(url_path('/assets/js/app.js')) ?>" defer></script>
</body>
</html>

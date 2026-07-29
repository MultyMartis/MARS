<?php
declare(strict_types=1);
/** @var string $content */
/** @var string $appName */
/** @var string $phaseLabel */
/** @var string $pageTitle */
/** @var array|null $currentUser */
/** @var string $authStatus */
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?= e(($pageTitle ?? 'App') . ' — ' . $appName) ?></title>
    <link rel="stylesheet" href="<?= e(url_path('/assets/css/app.css')) ?>">
</head>
<body data-phase="local-ux">
<?php require app_path('Views/partials/header.php'); ?>
<main class="container">
    <?php require app_path('Views/partials/flash.php'); ?>
    <?= $content ?>
</main>
<?php require app_path('Views/partials/footer.php'); ?>
<script src="<?= e(url_path('/assets/js/app.js')) ?>" defer></script>
</body>
</html>

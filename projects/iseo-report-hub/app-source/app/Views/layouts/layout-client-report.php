<?php
declare(strict_types=1);
/** @var string $content */
/** @var string $appName */
/** @var string $pageTitle */
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?= e(($pageTitle ?? 'SEO-отчёт') . ' — ' . ($appName ?? 'i-SEO Report Hub')) ?></title>
    <link rel="stylesheet" href="<?= e(url_path('/assets/css/client-report.css')) ?>">
</head>
<body class="client-report-page">
<?= $content ?>
</body>
</html>

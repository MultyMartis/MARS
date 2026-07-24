<?php
declare(strict_types=1);

/**
 * i-SEO Report Hub — Phase 0 health check.
 * No database connection. No environment file required.
 */

$required = [
    'pdo',
    'pdo_mysql',
    'mbstring',
    'json',
    'openssl',
    'fileinfo',
    'session',
];

$optional = [
    'gd',
    'curl',
    'intl',
    'mysqli',
    'imagick',
];

$loaded = get_loaded_extensions();
$loadedLower = array_map('strtolower', $loaded);

$check = static function (array $names) use ($loadedLower): array {
    $out = [];
    foreach ($names as $name) {
        $out[$name] = in_array(strtolower($name), $loadedLower, true);
    }
    return $out;
};

$requiredStatus = $check($required);
$optionalStatus = $check($optional);
$allRequiredOk = !in_array(false, $requiredStatus, true);
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Health — i-SEO Report Hub</title>
    <link rel="stylesheet" href="assets/css/app.css">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <p class="brand">INTLSEO / i-SEO</p>
            <h1>Health check</h1>
            <p class="tagline">Phase 0 · PHP only · no DB</p>
        </div>
    </header>

    <main class="container">
        <section class="panel">
            <h2>Runtime</h2>
            <ul class="facts">
                <li><strong>PHP running:</strong> yes</li>
                <li><strong>PHP version:</strong> <?= htmlspecialchars(PHP_VERSION, ENT_QUOTES, 'UTF-8') ?></li>
                <li><strong>SAPI:</strong> <?= htmlspecialchars(PHP_SAPI, ENT_QUOTES, 'UTF-8') ?></li>
                <li><strong>Database connection:</strong> not attempted</li>
                <li><strong>Environment file:</strong> not required for this page</li>
                <li><strong>Required extensions:</strong>
                    <span class="<?= $allRequiredOk ? 'ok' : 'warn' ?>">
                        <?= $allRequiredOk ? 'all present' : 'missing one or more' ?>
                    </span>
                </li>
            </ul>
        </section>

        <section class="panel">
            <h2>Required extensions</h2>
            <ul class="ext-list">
                <?php foreach ($requiredStatus as $name => $present): ?>
                    <li class="<?= $present ? 'ok' : 'missing' ?>">
                        <?= htmlspecialchars($name, ENT_QUOTES, 'UTF-8') ?> —
                        <?= $present ? 'present' : 'missing' ?>
                    </li>
                <?php endforeach; ?>
            </ul>
        </section>

        <section class="panel">
            <h2>Optional extensions</h2>
            <ul class="ext-list">
                <?php foreach ($optionalStatus as $name => $present): ?>
                    <li class="<?= $present ? 'ok' : 'warn' ?>">
                        <?= htmlspecialchars($name, ENT_QUOTES, 'UTF-8') ?> —
                        <?= $present ? 'present' : 'absent' ?>
                    </li>
                <?php endforeach; ?>
            </ul>
            <p><a class="btn btn-secondary" href="index.php">Back to index</a></p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>No MySQL probe · no secrets loaded</p>
        </div>
    </footer>
    <script src="assets/js/app.js" defer></script>
</body>
</html>

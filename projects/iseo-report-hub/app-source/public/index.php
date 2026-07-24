<?php
declare(strict_types=1);

/**
 * i-SEO Report Hub — Phase 0 public entrypoint.
 * Scaffold only: no database connection, no auth, no framework.
 */

$appName = 'i-SEO Report Hub';
$phase = 'Phase 0 — Runtime scaffold only';
$phpVersion = PHP_VERSION;
$runtimePath = dirname(__DIR__);
$noDb = true;
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?= htmlspecialchars($appName, ENT_QUOTES, 'UTF-8') ?> — Phase 0</title>
    <link rel="stylesheet" href="assets/css/app.css">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <p class="brand">INTLSEO / i-SEO</p>
            <h1><?= htmlspecialchars($appName, ENT_QUOTES, 'UTF-8') ?></h1>
            <p class="tagline">Custom PHP + SQL/MySQL reporting runtime (scaffold)</p>
        </div>
    </header>

    <main class="container">
        <section class="panel">
            <h2>Status</h2>
            <ul class="facts">
                <li><strong>Stage:</strong> <?= htmlspecialchars($phase, ENT_QUOTES, 'UTF-8') ?></li>
                <li><strong>PHP version:</strong> <?= htmlspecialchars($phpVersion, ENT_QUOTES, 'UTF-8') ?></li>
                <li><strong>Database connection:</strong> <?= $noDb ? 'not attempted' : 'n/a' ?></li>
                <li><strong>WordPress:</strong> not used</li>
                <li><strong>Runtime path:</strong> <code><?= htmlspecialchars($runtimePath, ENT_QUOTES, 'UTF-8') ?></code></li>
            </ul>
            <p class="note">This page is a safe static entrypoint. No `.env` is required. No credentials are loaded.</p>
            <p><a class="btn" href="health.php">Open health check</a></p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>MARS Localhost · Phase 0 scaffold · no production deployment</p>
        </div>
    </footer>
    <script src="assets/js/app.js" defer></script>
</body>
</html>

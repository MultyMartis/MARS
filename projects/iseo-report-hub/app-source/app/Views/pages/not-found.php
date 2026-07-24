<?php
declare(strict_types=1);
/** @var string $path */
?>
<section class="panel">
    <h2>404 — Not Found</h2>
    <p>No route matches <code><?= e($path) ?></code>.</p>
    <p class="note">Phase 1A exact-path router only. No regex routes yet.</p>
    <p><a class="btn" href="<?= e(url_path('/')) ?>">Dashboard</a></p>
</section>

<?php
declare(strict_types=1);
/** @var string $path */

$host = (string) ($_SERVER['HTTP_HOST'] ?? '');
$appEnv = (string) (getenv('APP_ENV') ?: getenv('ISEO_APP_ENV') ?: '');
$isLocal = str_contains($host, '.test')
    || str_contains($host, 'localhost')
    || str_contains($host, '127.0.0.1')
    || in_array(strtolower($appEnv), ['local', 'dev', 'development'], true);
?>
<section class="panel">
    <h2>Страница не найдена</h2>
    <p>Такой страницы нет или ссылка устарела. Вернитесь на главную страницу и продолжите работу.</p>
    <p><a class="btn btn-primary" href="<?= e(url_path('/')) ?>">На главную</a></p>
    <?php if ($isLocal): ?>
        <details class="tech-details">
            <summary>Технические детали</summary>
            <ul class="facts">
                <li><strong>HTTP:</strong> 404</li>
                <li><strong>Путь:</strong> <code><?= e($path) ?></code></li>
            </ul>
        </details>
    <?php endif; ?>
</section>

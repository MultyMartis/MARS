<?php
declare(strict_types=1);
/** @var array<string, mixed> $status */
$db = is_array($status['db'] ?? null) ? $status['db'] : [];
$overall = (string) ($status['overall'] ?? 'unknown');
$overallRu = match ($overall) {
    'ok' => 'В порядке',
    'degraded' => 'Есть замечания',
    'fail', 'failed', 'error' => 'Ошибка',
    default => $overall,
};
?>
<section class="panel">
    <h2>Общее состояние</h2>
    <p>
        <span class="badge badge-<?= e($overall) ?>"><?= e($overallRu) ?></span>
    </p>
    <p class="note">Техническая страница для проверки локального запуска. Не для клиента.</p>
</section>

<section class="panel">
    <h2>Локальный запуск / PHP</h2>
    <ul class="facts">
        <li><strong>PHP работает:</strong> да</li>
        <li><strong>Версия PHP:</strong> <?= e((string) $status['php_version']) ?></li>
        <li><strong>SAPI:</strong> <?= e((string) $status['sapi']) ?></li>
        <li><strong>Приложение:</strong> <?= e((string) $status['app_skeleton']) ?></li>
        <li><strong>.env.local есть:</strong> <?= !empty($status['env_local_present']) ? 'да' : 'нет' ?></li>
        <li><strong>.env обязателен:</strong> нет</li>
        <li><strong>WordPress:</strong> <?= e((string) $status['wordpress']) ?></li>
        <li><strong>Нужные расширения:</strong>
            <span class="<?= !empty($status['all_required_ok']) ? 'ok' : 'warn' ?>">
                <?= !empty($status['all_required_ok']) ? 'все есть' : 'чего-то не хватает' ?>
            </span>
        </li>
    </ul>
</section>

<section class="panel">
    <h2>База данных (безопасный статус)</h2>
    <ul class="facts">
        <li><strong>База настроена:</strong> <?= !empty($db['configured']) ? 'да' : 'нет' ?></li>
        <li><strong>Подключение:</strong>
            <span class="badge badge-<?= e((string) ($db['connection_label'] ?? 'n/a')) ?>">
                <?= e((string) ($db['connection_label'] ?? 'n/a')) ?>
            </span>
        </li>
        <li><strong>Имя БД:</strong> <?= e((string) ($db['database'] ?? '—')) ?></li>
        <li><strong>Число миграций:</strong> <?= e((string) ($db['migration_count'] ?? '—')) ?></li>
        <li><strong>Последняя миграция:</strong> <?= e((string) ($db['latest_migration'] ?? '—')) ?></li>
        <li><strong>Таблиц есть / ожидается:</strong>
            <?= e((string) ($db['tables_present'] ?? '—')) ?> /
            <?= e((string) ($db['tables_expected'] ?? '—')) ?>
        </li>
        <li><strong>Пользователей:</strong> <?= e((string) ($db['users_count'] ?? '—')) ?></li>
        <li><strong>Ролей:</strong> <?= e((string) ($db['roles_count'] ?? '—')) ?></li>
        <li><strong>Статус БД:</strong> <?= e((string) ($db['status'] ?? 'unknown')) ?></li>
    </ul>
    <p class="note">Пароли, DSN с паролем и детали SQL-ошибок здесь не показываются.</p>
</section>

<section class="panel">
    <h2>Нужные расширения</h2>
    <ul class="ext-list">
        <?php foreach ($status['required'] as $name => $present): ?>
            <li class="<?= $present ? 'ok' : 'missing' ?>">
                <?= e((string) $name) ?> — <?= $present ? 'есть' : 'нет' ?>
            </li>
        <?php endforeach; ?>
    </ul>
</section>

<section class="panel">
    <h2>Дополнительные расширения</h2>
    <ul class="ext-list">
        <?php foreach ($status['optional'] as $name => $present): ?>
            <li class="<?= $present ? 'ok' : 'warn' ?>">
                <?= e((string) $name) ?> — <?= $present ? 'есть' : 'нет' ?>
            </li>
        <?php endforeach; ?>
    </ul>
    <p><a class="btn btn-secondary" href="<?= e(url_path('/')) ?>">На главную</a></p>
</section>

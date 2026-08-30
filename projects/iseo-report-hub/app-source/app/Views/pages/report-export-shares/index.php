<?php
declare(strict_types=1);

/** @var array<string, mixed> $export */
/** @var list<array<string, mixed>> $shares */
/** @var array<string, mixed>|null $activeShare */
/** @var array{eligible?:bool,reason?:string,code?:string} $eligibility */
/** @var bool $canManage */
/** @var string|null $plaintextShareUrl */
/** @var array<string, mixed>|null $handoff */
/** @var \Iseo\Services\CsrfService $csrf */

$export = $export ?? [];
$shares = $shares ?? [];
$activeShare = is_array($activeShare ?? null) ? $activeShare : null;
$eligibility = is_array($eligibility ?? null) ? $eligibility : [];
$canManage = !empty($canManage);
$plaintextShareUrl = is_string($plaintextShareUrl ?? null) ? $plaintextShareUrl : null;
$handoff = is_array($handoff ?? null) ? $handoff : null;

$exportId = (int) ($export['id'] ?? 0);
$snapshotId = (int) ($export['report_snapshot_id'] ?? 0);
$eligible = !empty($eligibility['eligible']);
$reason = ui_message((string) ($eligibility['reason'] ?? ''));
$format = (string) ($export['format'] ?? '');

$hCtx = is_array($handoff['context'] ?? null) ? $handoff['context'] : [];
$hShare = is_array($handoff['share_status'] ?? null) ? $handoff['share_status'] : [];
$hChecks = is_array($handoff['checklist'] ?? null) ? $handoff['checklist'] : [];
$hWarnings = is_array($handoff['warnings'] ?? null) ? $handoff['warnings'] : [];
$copyPack = is_array($handoff['copy_pack'] ?? null) ? $handoff['copy_pack'] : null;
$urlLost = is_string($handoff['url_lost_guidance'] ?? null) ? (string) $handoff['url_lost_guidance'] : '';
$onceAvailable = $plaintextShareUrl !== null && $plaintextShareUrl !== '';

$statusRu = static function (string $status): string {
    return match ($status) {
        'ready' => 'Готово',
        'pending' => 'В работе',
        'failed' => 'Ошибка',
        'active' => 'Активна',
        'revoked' => 'Отозвана',
        'expired' => 'Истекла',
        'finalized' => 'Финализирован',
        default => $status,
    };
};

$activeShares = [];
$revokedShares = [];
foreach ($shares as $row) {
    if (!is_array($row)) {
        continue;
    }
    $st = (string) ($row['status'] ?? '');
    if ($st === 'active') {
        $activeShares[] = $row;
    } else {
        $revokedShares[] = $row;
    }
}
?>
<section class="card panel export-card handoff-panel mb-24" data-handoff-panel>
    <div class="panel-head">
        <h2>Готовность к отправке клиенту</h2>
        <p>
            <a class="btn btn-secondary" href="<?= e(url_path('/report-exports/' . $exportId)) ?>">Файл отчета</a>
            <?php if ($snapshotId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">Все файлы отчета</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Только внутри</span>
        <?php if ($eligible): ?>
            <span class="share-badge share-badge--eligible">Можно отправлять</span>
        <?php else: ?>
            <span class="share-badge share-badge--blocked" title="<?= e($reason) ?>">Нельзя отправлять</span>
        <?php endif; ?>
    </p>

    <?php if (!$eligible): ?>
        <p class="field-hint handoff-not-ready">Не готово к отправке: <?= e($reason) ?>. Тексты для отправки недоступны.</p>
    <?php endif; ?>

    <ul class="facts handoff-context-list manager-facts">
        <li><strong>Клиент:</strong> <?= e((string) ($hCtx['client_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Проект:</strong> <?= e((string) ($hCtx['project_name'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Период:</strong> <?= e((string) ($hCtx['period'] ?? 'SAFE UNKNOWN')) ?></li>
        <li><strong>Статус отчета:</strong> <?= e($statusRu((string) ($hCtx['report_status'] ?? 'SAFE UNKNOWN'))) ?></li>
        <li><strong>Ссылка:</strong>
            <?php if (!empty($hShare['has_active'])): ?>
                Есть активная ссылка
                <?php if (!empty($hShare['expires_at'])): ?>
                    · действует до <code><?= e((string) $hShare['expires_at']) ?></code>
                <?php endif; ?>
            <?php else: ?>
                Активной ссылки нет
            <?php endif; ?>
            <?php if ((int) ($hShare['revoked_count'] ?? 0) > 0): ?>
                · отозванных: <?= e((string) (int) $hShare['revoked_count']) ?>
            <?php endif; ?>
        </li>
    </ul>

    <?php if ($hChecks !== []): ?>
        <h3 class="handoff-subhead">Чек-лист готовности</h3>
        <ul class="handoff-checklist">
            <?php foreach ($hChecks as $item): ?>
                <?php if (!is_array($item)) { continue; } ?>
                <li class="<?= !empty($item['pass']) ? 'check-pass' : 'check-fail' ?>">
                    <span class="check-mark"><?= !empty($item['pass']) ? '✓' : '○' ?></span>
                    <?= e((string) ($item['label'] ?? '')) ?>
                    <span class="meta-muted">— <?= e((string) ($item['note'] ?? '')) ?></span>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <?php if ($hWarnings !== []): ?>
        <h3 class="handoff-subhead">Предупреждения</h3>
        <ul class="handoff-warnings">
            <?php foreach ($hWarnings as $w): ?>
                <li><?= e((string) $w) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</section>

<section class="card panel export-card share-card mb-24">
    <div class="panel-head">
        <h2>Ссылки для клиента</h2>
    </div>

    <p class="field-hint share-hint">
        <?= e($eligible ? $reason : ('Нельзя создать ссылку: ' . $reason)) ?>
        Полная ссылка показывается только один раз после создания.
        Клиентский кабинет и email-рассылка в этом MVP не используются — отправка вручную.
    </p>

    <?php if ($onceAvailable): ?>
        <div class="share-once-box" data-share-once>
            <p><strong>Скопируйте ссылку сейчас</strong> — она больше не отобразится.</p>
            <div class="share-once-row">
                <input
                    type="text"
                    class="share-url-input"
                    readonly
                    autocomplete="off"
                    spellcheck="false"
                    value="<?= e($plaintextShareUrl) ?>"
                    data-share-url
                    aria-label="Ссылка для клиента"
                >
                <button type="button" class="btn btn-primary" data-share-copy>Скопировать ссылку</button>
            </div>
            <p class="field-hint">Срок по умолчанию: 30 дней. Отозвать можно в любой момент.</p>
        </div>

        <?php if (is_array($copyPack)): ?>
            <div class="handoff-copy-pack" data-handoff-copy-pack>
                <h3 class="handoff-subhead">Тексты для отправки</h3>
                <p class="field-hint">Русские шаблоны заполнены из данных отчета. Не включайте пути к файлам и хеши токенов.</p>

                <div class="copy-pack-block">
                    <label for="copy-short">Короткое сообщение</label>
                    <textarea id="copy-short" class="copy-pack-text" readonly autocomplete="off" spellcheck="false" data-copy-target><?= e((string) ($copyPack['short_message'] ?? '')) ?></textarea>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Скопировать короткое сообщение</button>
                </div>

                <div class="copy-pack-block">
                    <label for="copy-email-subject">Письмо — тема</label>
                    <input id="copy-email-subject" type="text" class="share-url-input" readonly autocomplete="off" spellcheck="false" value="<?= e((string) ($copyPack['email_subject'] ?? '')) ?>" data-copy-target>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Скопировать тему</button>
                </div>

                <div class="copy-pack-block">
                    <label for="copy-email-body">Письмо — текст</label>
                    <textarea id="copy-email-body" class="copy-pack-text" readonly autocomplete="off" spellcheck="false" data-copy-target><?= e((string) ($copyPack['email_body'] ?? '')) ?></textarea>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Скопировать письмо</button>
                </div>

                <div class="copy-pack-block">
                    <label for="copy-internal">Внутренняя заметка</label>
                    <textarea id="copy-internal" class="copy-pack-text" readonly autocomplete="off" spellcheck="false" data-copy-target><?= e((string) ($copyPack['internal_note'] ?? '')) ?></textarea>
                    <button type="button" class="btn btn-secondary" data-copy-btn>Скопировать внутреннюю заметку</button>
                </div>
            </div>
        <?php endif; ?>
    <?php elseif ($urlLost !== ''): ?>
        <p class="handoff-once-gone" role="status"><?= e($urlLost) ?></p>
    <?php endif; ?>

    <?php if ($canManage && $eligible && $activeShare === null): ?>
        <form method="post" action="<?= e(url_path('/report-exports/' . $exportId . '/shares')) ?>" class="share-create-form">
            <?= $csrf->field() ?>
            <label for="token_label">Название ссылки</label>
            <input type="text" id="token_label" name="token_label" maxlength="150" placeholder="например: Клиенту за июль">
            <button type="submit" class="btn btn-primary">Создать ссылку для клиента</button>
        </form>
    <?php elseif ($canManage && $eligible && $activeShare !== null): ?>
        <p class="export-ready-note">Есть активная ссылка. Если ссылку не скопировали — отзовите её и создайте новую. Полный URL из базы не восстанавливается.</p>
    <?php elseif (!$canManage): ?>
        <p class="field-hint">Создание и отзыв ссылок доступны ролям admin_owner или seo_lead_reviewer.</p>
    <?php endif; ?>

    <h3 class="handoff-subhead">Активные ссылки</h3>
    <?php if ($activeShares === []): ?>
        <p class="note">Активной ссылки нет.</p>
    <?php else: ?>
        <div class="table-wrap">
            <table class="data-table table share-table">
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Статус</th>
                    <th>Название</th>
                    <th>Действует до</th>
                    <th>Открытий</th>
                    <th>Последний доступ</th>
                    <th>Создана</th>
                    <th>Действия</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ($activeShares as $row): ?>
                    <?php
                    $sid = (int) ($row['id'] ?? 0);
                    $status = (string) ($row['status'] ?? '');
                    $label = (string) ($row['token_label'] ?? '');
                    ?>
                    <tr>
                        <td><?= e((string) $sid) ?></td>
                        <td><span class="status-badge status-<?= e($status) ?>"><?= e($statusRu($status)) ?></span></td>
                        <td><?= e($label !== '' ? $label : '—') ?></td>
                        <td><?= e((string) ($row['expires_at'] ?? '—')) ?></td>
                        <td><?= e((string) (int) ($row['access_count'] ?? 0)) ?></td>
                        <td><?= e((string) ($row['last_accessed_at'] ?? '—')) ?></td>
                        <td><?= e((string) ($row['created_at'] ?? '—')) ?></td>
                        <td class="actions">
                            <?php if ($canManage): ?>
                                <form method="post" action="<?= e(url_path('/report-export-shares/' . $sid . '/revoke')) ?>" class="inline-form">
                                    <?= $csrf->field() ?>
                                    <button type="submit" class="btn btn-secondary btn-revoke">Отозвать</button>
                                </form>
                            <?php else: ?>
                                <span class="meta-muted">—</span>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    <?php endif; ?>

    <details class="tech-details technical-details">
        <summary>Отозванные ссылки</summary>
        <?php if ($revokedShares === []): ?>
            <p class="note">Отозванных ссылок нет.</p>
        <?php else: ?>
            <div class="table-wrap">
                <table class="data-table table share-table">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Статус</th>
                        <th>Название</th>
                        <th>Действует до</th>
                        <th>Открытий</th>
                        <th>Последний доступ</th>
                        <th>Создана</th>
                    </tr>
                    </thead>
                    <tbody>
                    <?php foreach ($revokedShares as $row): ?>
                        <?php
                        $sid = (int) ($row['id'] ?? 0);
                        $status = (string) ($row['status'] ?? '');
                        $label = (string) ($row['token_label'] ?? '');
                        ?>
                        <tr>
                            <td><?= e((string) $sid) ?></td>
                            <td><span class="status-badge status-<?= e($status) ?>"><?= e($statusRu($status)) ?></span></td>
                            <td><?= e($label !== '' ? $label : '—') ?></td>
                            <td><?= e((string) ($row['expires_at'] ?? '—')) ?></td>
                            <td><?= e((string) (int) ($row['access_count'] ?? 0)) ?></td>
                            <td><?= e((string) ($row['last_accessed_at'] ?? '—')) ?></td>
                            <td><?= e((string) ($row['created_at'] ?? '—')) ?></td>
                        </tr>
                    <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
        <?php endif; ?>
        <p class="field-hint">Не отправляйте отозванные или просроченные ссылки.</p>
    </details>
</section>

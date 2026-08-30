<?php
declare(strict_types=1);

/** @var string $mode */
/** @var array<string, mixed>|null $monthly */
/** @var array<string, mixed>|null $snapshot */
/** @var array<string, mixed>|null $payload */
/** @var bool $canCreate */
/** @var string $message */
/** @var array<string, mixed>|null $htmlExport */
/** @var array<string, mixed>|null $pdfExport */
/** @var array<string, mixed>|null $styledHtmlExport */
/** @var array<string, mixed>|null $styledPdfExport */
/** @var bool $canCreateExport */
/** @var bool $canCreatePdfExport */
/** @var bool $canCreateStyledHtml */
/** @var bool $canCreateStyledPdf */
/** @var \Iseo\Services\CsrfService $csrf */

$mode = $mode ?? 'detail';
$monthly = $monthly ?? null;
$snapshot = $snapshot ?? null;
$payload = $payload ?? null;
$canCreate = !empty($canCreate);
$message = (string) ($message ?? '');
$htmlExport = $htmlExport ?? null;
$pdfExport = $pdfExport ?? null;
$styledHtmlExport = $styledHtmlExport ?? null;
$styledPdfExport = $styledPdfExport ?? null;
$canCreateExport = !empty($canCreateExport);
$canCreatePdfExport = !empty($canCreatePdfExport);
$canCreateStyledHtml = !empty($canCreateStyledHtml);
$canCreateStyledPdf = !empty($canCreateStyledPdf);
$legacyTemplateLabel = (string) ($legacyTemplateLabel ?? 'не записан / устаревший');
$futureTemplate = is_array($futureTemplate ?? null) ? $futureTemplate : [];
$futureTemplateId = (string) ($futureTemplate['id'] ?? 'iseo_default_v1');
$futureTemplateVersion = (string) (int) ($futureTemplate['version'] ?? 1);
$styledTemplateLabel = $futureTemplateId . ' v' . $futureTemplateVersion;

$monthlyId = 0;
if (is_array($snapshot) && isset($snapshot['monthly_report_content_id'])) {
    $monthlyId = (int) $snapshot['monthly_report_content_id'];
} elseif (is_array($monthly)) {
    $monthlyId = (int) $monthly['id'];
}

$checksum = is_array($snapshot) ? (string) ($snapshot['checksum_sha256'] ?? '') : '';
$checksumShort = $checksum !== '' ? substr($checksum, 0, 12) . '…' : '—';

$blocks = [];
$weeklySources = [];
$periodKey = '';
if (is_array($payload)) {
    $blocks = is_array($payload['blocks'] ?? null) ? $payload['blocks'] : [];
    $weeklySources = is_array($payload['weekly_sources'] ?? null) ? $payload['weekly_sources'] : [];
    $periodKey = (string) (($payload['period']['key'] ?? '') ?: '');
}
if ($periodKey === '' && is_array($monthly)) {
    $periodKey = (string) ($monthly['period_key'] ?? '');
}

/**
 * @param mixed $raw
 * @return list<int>
 */
$decodeIds = static function (mixed $raw): array {
    if (is_array($raw)) {
        $out = [];
        foreach ($raw as $v) {
            $id = (int) $v;
            if ($id > 0) {
                $out[] = $id;
            }
        }
        return array_values(array_unique($out));
    }
    if (!is_string($raw) || $raw === '') {
        return [];
    }
    $decoded = json_decode($raw, true);
    if (!is_array($decoded)) {
        return [];
    }
    $out = [];
    foreach ($decoded as $v) {
        $id = (int) $v;
        if ($id > 0) {
            $out[] = $id;
        }
    }
    return array_values(array_unique($out));
};
?>
<section class="panel snapshot-card">
    <div class="panel-head">
        <h2><?= $mode === 'monthly' ? 'Снимок отчета' : 'Детали снимка' ?></h2>
        <p>
            <?php if ($monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId)) ?>">Месячный отчет</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/preview')) ?>">Предпросмотр</a>
            <?php endif; ?>
            <?php if ($mode === 'detail' && $monthlyId > 0): ?>
                <a class="btn btn-secondary" href="<?= e(url_path('/monthly-reports/' . $monthlyId . '/snapshot')) ?>">Сводка снимка</a>
            <?php endif; ?>
        </p>
    </div>

    <p>
        <span class="internal-only-badge">Только внутри</span>
        <span class="immutable-badge">Неизменяемый</span>
        <?php if (is_array($snapshot)): ?>
            · <span class="status-badge status-<?= e((string) $snapshot['status']) ?>"><?= e(ui_status_label((string) $snapshot['status'])) ?></span>
        <?php endif; ?>
    </p>

    <?php if ($mode === 'monthly' && $snapshot === null): ?>
        <p class="note">Для этого месячного отчета снимок ещё не создан.</p>
        <?php if ($canCreate && $monthlyId > 0): ?>
            <form method="post" action="<?= e(url_path('/monthly-reports/' . $monthlyId . '/snapshot')) ?>">
                <?= $csrf->field() ?>
                <button type="submit" class="btn">Создать снимок</button>
            </form>
        <?php elseif (is_array($monthly) && (string) ($monthly['status'] ?? '') !== 'finalized'): ?>
            <p class="field-hint">Создание снимка требует финализированного месячного отчета.</p>
        <?php endif; ?>
    <?php elseif (is_array($snapshot)): ?>
        <ul class="facts snapshot-meta">
            <li><strong>Версия:</strong> <?= e((string) $snapshot['version']) ?></li>
            <li><strong>Название:</strong> <?= e((string) $snapshot['title']) ?></li>
            <li><strong>Период:</strong> <code><?= e($periodKey !== '' ? $periodKey : '—') ?></code></li>
            <li><strong>Статус:</strong> <span class="status-badge status-<?= e((string) $snapshot['status']) ?>"><?= e(ui_status_label((string) $snapshot['status'])) ?></span></li>
            <li><strong>Контрольная сумма:</strong> <code class="checksum-display" title="<?= e($checksum) ?>"><?= e($checksumShort) ?></code></li>
            <li><strong>Создан:</strong> <?= e((string) ($snapshot['created_at'] ?? '—')) ?></li>
            <li><strong>Создал:</strong>
                <?= e(ui_display_user_name($snapshot['created_by_name'] ?? null, $snapshot['created_by_email'] ?? null)) ?>
            </li>
        </ul>
        <p>
            <a class="btn" href="<?= e(url_path('/report-snapshots/' . (int) $snapshot['id'])) ?>">Открыть снимок</a>
            <?php if ($mode === 'monthly'): ?>
                <span class="field-hint">Создание идемпотентно, пока активная контрольная сумма совпадает.</span>
            <?php endif; ?>
        </p>
        <?php if ($mode === 'monthly' && $monthlyId > 0): ?>
            <form method="post" action="<?= e(url_path('/monthly-reports/' . $monthlyId . '/snapshot')) ?>" class="snapshot-idempotent-form">
                <?= $csrf->field() ?>
                <button type="submit" class="btn btn-secondary">Проверить / создать (идемпотентно)</button>
            </form>
        <?php endif; ?>
        <details class="tech-details">
            <summary>Технические детали</summary>
            <ul class="facts">
                <li><strong>ID:</strong> <?= e((string) $snapshot['id']) ?></li>
                <li><strong>Ключ:</strong> <code><?= e((string) $snapshot['snapshot_key']) ?></code></li>
                <li><strong>Режим генерации:</strong> <code><?= e((string) $snapshot['render_mode']) ?></code></li>
                <li><strong>Полная контрольная сумма:</strong> <code class="checksum-full"><?= e($checksum) ?></code></li>
            </ul>
        </details>
    <?php endif; ?>
</section>

<?php if (is_array($snapshot)): ?>
    <?php
    $snapshotId = (int) $snapshot['id'];
    $exportChecksum = is_array($htmlExport) ? (string) ($htmlExport['checksum_sha256'] ?? '') : '';
    $exportShort = $exportChecksum !== '' ? substr($exportChecksum, 0, 12) . '…' : '—';
    $exportSize = is_array($htmlExport) && isset($htmlExport['file_size_bytes']) ? (int) $htmlExport['file_size_bytes'] : 0;
    ?>
    <section class="panel export-card">
        <div class="panel-head">
            <h2>HTML-экспорт</h2>
            <p>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">Все файлы</a>
            </p>
        </div>
        <p>
            <span class="internal-only-badge">Только внутри</span>
            <span class="artifact-badge">HTML-файл</span>
        </p>
        <p class="template-state-note">
            Предпочитаются метаданные шаблона из БД. Устаревшие / NULL: <?= e($legacyTemplateLabel) ?>.
            Записанный по умолчанию: <code><?= e($futureTemplateId) ?></code> v<?= e($futureTemplateVersion) ?> (только для новых версий экспорта).
        </p>
        <?php if (!is_array($htmlExport)): ?>
            <p class="note">HTML-экспорт ещё не создан.</p>
            <?php if ($canCreateExport): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html')) ?>">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Создать HTML-экспорт</button>
                </form>
            <?php endif; ?>
        <?php else: ?>
            <?php
            $displayHtml = is_array($styledHtmlExport) ? $styledHtmlExport : $htmlExport;
            $displayHtmlIsLegacy = is_array($displayHtml)
                && (!empty($displayHtml['is_legacy_template_metadata'])
                    || trim((string) ($displayHtml['template_id'] ?? '')) === '');
            $displayHtmlTemplate = is_array($displayHtml)
                ? (string) ($displayHtml['display_template_label'] ?? ($displayHtmlIsLegacy ? $legacyTemplateLabel : $styledTemplateLabel))
                : $legacyTemplateLabel;
            $exportChecksum = (string) ($displayHtml['checksum_sha256'] ?? '');
            $exportShort = $exportChecksum !== '' ? substr($exportChecksum, 0, 12) . '…' : '—';
            $exportSize = isset($displayHtml['file_size_bytes']) ? (int) $displayHtml['file_size_bytes'] : 0;
            ?>
            <ul class="facts">
                <li><strong>ID экспорта:</strong> <?= e((string) $displayHtml['id']) ?></li>
                <li><strong>Формат / статус:</strong>
                    <span class="type-badge">html</span>
                    · <span class="status-badge status-<?= e((string) ($displayHtml['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($displayHtml['status'] ?? ''))) ?></span>
                </li>
                <li><strong>Имя файла:</strong> <code><?= e((string) ($displayHtml['filename'] ?? '')) ?></code></li>
                <li><strong>Контрольная сумма:</strong> <code class="checksum-display" title="<?= e($exportChecksum) ?>"><?= e($exportShort) ?></code></li>
                <li><strong>Размер:</strong> <?= e($exportSize > 0 ? number_format($exportSize) . ' байт' : '—') ?></li>
                <li><strong>Шаблон:</strong>
                    <span class="template-badge<?= $displayHtmlIsLegacy ? ' template-badge--legacy' : ' template-badge--styled' ?>">
                        <?= e($displayHtmlTemplate) ?>
                    </span>
                </li>
                <?php if (is_array($displayHtml) && !$displayHtmlIsLegacy): ?>
                    <li><strong>Генерация:</strong>
                        <span class="meta-muted"><?= e((string) ($displayHtml['display_render_target_label'] ?? 'HTML-экспорт')) ?></span>
                        · <span class="meta-muted"><?= e((string) ($displayHtml['display_render_engine_label'] ?? 'PHP-шаблонизатор')) ?></span>
                    </li>
                <?php endif; ?>
            </ul>
            <details class="tech-details">
                <summary>Технические детали</summary>
                <ul class="facts">
                    <li><strong>Ключ:</strong> <code><?= e((string) ($displayHtml['export_key'] ?? '')) ?></code></li>
                </ul>
            </details>
            <p>
                <a class="btn" href="<?= e(url_path('/report-exports/' . (int) $displayHtml['id'])) ?>">Открыть экспорт</a>
                <a class="btn btn-secondary btn-download" href="<?= e(url_path('/report-exports/' . (int) $displayHtml['id'] . '/download')) ?>">Скачать HTML</a>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">Все версии</a>
            </p>
            <?php if ($canCreateStyledHtml && !is_array($styledHtmlExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Создать оформленный HTML (<?= e($styledTemplateLabel) ?>)</button>
                </form>
            <?php elseif ($canCreateStyledHtml && is_array($styledHtmlExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/html/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Проверить оформленный HTML (идемпотентно)</button>
                </form>
            <?php endif; ?>
            <p class="field-hint export-hint">Скачивание HTML — только с авторизацией. Публичная ссылка доступна только для готового оформленного PDF.</p>
        <?php endif; ?>
    </section>

    <?php
    $pdfChecksum = is_array($pdfExport) ? (string) ($pdfExport['checksum_sha256'] ?? '') : '';
    $pdfShort = $pdfChecksum !== '' ? substr($pdfChecksum, 0, 12) . '…' : '—';
    $pdfSize = is_array($pdfExport) && isset($pdfExport['file_size_bytes']) ? (int) $pdfExport['file_size_bytes'] : 0;
    ?>
    <section class="panel export-card">
        <div class="panel-head">
            <h2>PDF-экспорт</h2>
            <p>
                <a class="btn btn-secondary" href="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports')) ?>">Все файлы</a>
            </p>
        </div>
        <p>
            <span class="internal-only-badge">Только внутри</span>
            <span class="artifact-badge artifact-badge--pdf">PDF-файл</span>
        </p>
        <?php if (!is_array($htmlExport)): ?>
            <p class="note">Сначала создайте HTML-экспорт, затем можно сгенерировать PDF.</p>
        <?php elseif (!is_array($pdfExport)): ?>
            <p class="note">PDF-экспорт ещё не создан.</p>
            <?php if ($canCreatePdfExport): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf')) ?>">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Создать PDF-экспорт</button>
                </form>
            <?php endif; ?>
        <?php else: ?>
            <?php
            $displayPdf = is_array($styledPdfExport) ? $styledPdfExport : $pdfExport;
            $displayPdfIsLegacy = is_array($displayPdf)
                && (!empty($displayPdf['is_legacy_template_metadata'])
                    || trim((string) ($displayPdf['template_id'] ?? '')) === '');
            $displayPdfTemplate = is_array($displayPdf)
                ? (string) ($displayPdf['display_template_label'] ?? ($displayPdfIsLegacy ? $legacyTemplateLabel : $styledTemplateLabel))
                : $legacyTemplateLabel;
            $displayPdfSource = is_array($displayPdf)
                ? (string) ($displayPdf['display_source_html_label'] ?? 'не записан')
                : 'не записан';
            $pdfChecksum = (string) ($displayPdf['checksum_sha256'] ?? '');
            $pdfShort = $pdfChecksum !== '' ? substr($pdfChecksum, 0, 12) . '…' : '—';
            $pdfSize = isset($displayPdf['file_size_bytes']) ? (int) $displayPdf['file_size_bytes'] : 0;
            ?>
            <ul class="facts">
                <li><strong>ID экспорта:</strong> <?= e((string) $displayPdf['id']) ?></li>
                <li><strong>Формат / статус:</strong>
                    <span class="type-badge type-badge--pdf">pdf</span>
                    · <span class="status-badge status-<?= e((string) ($displayPdf['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($displayPdf['status'] ?? ''))) ?></span>
                </li>
                <li><strong>Имя файла:</strong> <code><?= e((string) ($displayPdf['filename'] ?? '')) ?></code></li>
                <li><strong>Контрольная сумма:</strong> <code class="checksum-display" title="<?= e($pdfChecksum) ?>"><?= e($pdfShort) ?></code></li>
                <li><strong>Размер:</strong> <?= e($pdfSize > 0 ? number_format($pdfSize) . ' байт' : '—') ?></li>
                <li><strong>Шаблон:</strong>
                    <span class="template-badge<?= $displayPdfIsLegacy ? ' template-badge--legacy' : ' template-badge--styled' ?>">
                        <?= e($displayPdfTemplate) ?>
                    </span>
                </li>
                <li><strong>Исходный HTML:</strong>
                    <span class="source-lineage<?= $displayPdfSource === 'не записан' || $displayPdfSource === 'not recorded' ? ' source-lineage--unknown' : '' ?>">
                        <?= e($displayPdfSource === 'not recorded' ? 'не записан' : $displayPdfSource) ?>
                    </span>
                </li>
                <?php if (is_array($displayPdf) && !$displayPdfIsLegacy): ?>
                    <li><strong>Генерация:</strong>
                        <span class="meta-muted"><?= e((string) ($displayPdf['display_render_target_label'] ?? 'PDF-экспорт')) ?></span>
                        · <span class="meta-muted"><?= e((string) ($displayPdf['display_render_engine_label'] ?? 'Edge headless PDF')) ?></span>
                    </li>
                <?php endif; ?>
            </ul>
            <details class="tech-details">
                <summary>Технические детали</summary>
                <ul class="facts">
                    <li><strong>Ключ:</strong> <code><?= e((string) ($displayPdf['export_key'] ?? '')) ?></code></li>
                </ul>
            </details>
            <p class="export-ready-note">Выше показан последний PDF. Предыдущие версии — в списке экспортов.</p>
            <p>
                <a class="btn" href="<?= e(url_path('/report-exports/' . (int) $displayPdf['id'])) ?>">Открыть экспорт</a>
                <a class="btn btn-secondary btn-download" href="<?= e(url_path('/report-exports/' . (int) $displayPdf['id'] . '/download')) ?>">Скачать PDF</a>
            </p>
            <?php if ($canCreateStyledPdf && is_array($styledHtmlExport) && !is_array($styledPdfExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn">Создать оформленный PDF из HTML v2</button>
                </form>
            <?php elseif ($canCreateStyledPdf && is_array($styledPdfExport)): ?>
                <form method="post" action="<?= e(url_path('/report-snapshots/' . $snapshotId . '/exports/pdf/styled')) ?>" class="export-idempotent-form">
                    <?= $csrf->field() ?>
                    <button type="submit" class="btn btn-secondary">Проверить оформленный PDF (идемпотентно)</button>
                </form>
            <?php endif; ?>
            <p class="field-hint export-hint">
                Скачивание с авторизацией всегда доступно.
                <?php if (!empty($displayPdf['template_id']) && (string) ($displayPdf['render_target'] ?? '') === 'pdf_export'): ?>
                    <span class="share-badge share-badge--eligible">PDF подходит для ссылки</span>
                    — управляйте ссылками на странице экспорта / «Ссылки для клиента».
                <?php else: ?>
                    <span class="share-badge share-badge--blocked">Ссылка недоступна (устаревшие/HTML-правила)</span>
                <?php endif; ?>
            </p>
        <?php endif; ?>
    </section>
<?php endif; ?>

<?php if ($mode === 'detail' && is_array($snapshot)): ?>
    <section class="panel">
        <h2>Ссылки на еженедельные заметки</h2>
        <?php
        $weeklyIds = $decodeIds($snapshot['source_weekly_checkpoint_ids'] ?? null);
        ?>
        <?php if ($weeklySources !== []): ?>
            <ul class="facts">
                <?php foreach ($weeklySources as $wc): ?>
                    <?php if (!is_array($wc)) {
                        continue;
                    } ?>
                    <li>
                        <a href="<?= e(url_path('/weekly-checkpoints/' . (int) ($wc['id'] ?? 0))) ?>">
                            <code><?= e((string) ($wc['checkpoint_key'] ?? ('#' . (int) ($wc['id'] ?? 0)))) ?></code>
                        </a>
                        · <span class="status-badge status-<?= e((string) ($wc['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($wc['status'] ?? ''))) ?></span>
                        · <?= e((string) ($wc['title'] ?? '')) ?>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php elseif ($weeklyIds !== []): ?>
            <ul class="facts">
                <?php foreach ($weeklyIds as $wid): ?>
                    <li><a href="<?= e(url_path('/weekly-checkpoints/' . $wid)) ?>">Заметка #<?= e((string) $wid) ?></a></li>
                <?php endforeach; ?>
            </ul>
        <?php else: ?>
            <p class="note">Ссылки на еженедельные заметки не сохранены.</p>
        <?php endif; ?>
    </section>

    <section class="panel snapshot-blocks">
        <h2>Зафиксированные блоки (<?= e((string) count($blocks)) ?>)</h2>
        <?php if ($blocks === []): ?>
            <p class="note">В payload нет блоков.</p>
        <?php else: ?>
            <?php foreach ($blocks as $block): ?>
                <?php if (!is_array($block)) {
                    continue;
                } ?>
                <article class="snapshot-block">
                    <h3><?= e((string) ($block['title'] ?? '')) ?></h3>
                    <p>
                        <span class="type-badge"><?= e((string) ($block['block_type'] ?? '')) ?></span>
                        · <span class="status-badge status-<?= e((string) ($block['status'] ?? '')) ?>"><?= e(ui_status_label((string) ($block['status'] ?? ''))) ?></span>
                        · порядок <?= e((string) ($block['sort_order'] ?? '')) ?>
                        <span class="meta-muted"><code><?= e((string) ($block['block_key'] ?? '')) ?></code></span>
                    </p>
                    <?php if (trim((string) ($block['summary'] ?? '')) !== ''): ?>
                        <p class="snapshot-block__summary"><?= e((string) $block['summary']) ?></p>
                    <?php endif; ?>
                    <?php if (trim((string) ($block['body'] ?? '')) !== ''): ?>
                        <div class="snapshot-block__body"><?= nl2br(e((string) $block['body']), false) ?></div>
                    <?php endif; ?>
                </article>
            <?php endforeach; ?>
        <?php endif; ?>
    </section>

    <?php if (!empty($snapshot['rendered_text'])): ?>
        <section class="panel">
            <h2>Сгенерированный текст</h2>
            <pre class="snapshot-rendered-text"><?= e((string) $snapshot['rendered_text']) ?></pre>
        </section>
    <?php endif; ?>
<?php endif; ?>

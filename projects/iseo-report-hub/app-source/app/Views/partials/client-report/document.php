<?php
declare(strict_types=1);
/** @var array<string, mixed> $document */

$document = $document ?? [];
$sections = is_array($document['sections'] ?? null) ? $document['sections'] : [];
$isFinalized = !empty($document['is_finalized']);
$localDemo = !empty($document['local_demo']);
?>
<article class="client-report-document">
    <header class="client-report-cover">
        <div class="client-report-brand">
            <p class="client-report-brand__mark"><?= e((string) ($document['brand'] ?? 'i-SEO')) ?></p>
            <p class="client-report-brand__type"><?= e((string) ($document['document_type'] ?? 'SEO-отчёт')) ?></p>
        </div>
        <h1 class="client-report-cover__title"><?= e((string) ($document['title'] ?? 'SEO-отчёт')) ?></h1>
        <dl class="client-report-meta">
            <div>
                <dt>Клиент</dt>
                <dd><?= e((string) ($document['client_name'] ?? '—')) ?></dd>
            </div>
            <div>
                <dt>Проект</dt>
                <dd><?= e((string) ($document['project_name'] ?? '—')) ?></dd>
            </div>
            <div>
                <dt>Сайт</dt>
                <dd><?= e((string) ($document['site_display'] ?? '—')) ?></dd>
            </div>
            <div>
                <dt>Период</dt>
                <dd><?= e((string) ($document['period_label'] ?? '—')) ?></dd>
            </div>
            <div>
                <dt>Статус</dt>
                <dd>
                    <span class="client-report-status<?= $isFinalized ? ' client-report-status--final' : ' client-report-status--draft' ?>">
                        <?= e((string) ($document['status_label'] ?? '')) ?>
                    </span>
                </dd>
            </div>
            <div>
                <dt>Дата</dt>
                <dd><?= e((string) ($document['report_date'] ?? '—')) ?></dd>
            </div>
        </dl>
        <?php if ($localDemo): ?>
            <p class="client-report-local">Локальная демо-среда</p>
        <?php endif; ?>
        <?php if (!$isFinalized): ?>
            <p class="client-report-draft-note"><?= e((string) ($document['draft_disclaimer'] ?? \Iseo\Support\UiLabels::draftClientDisclaimer())) ?></p>
        <?php endif; ?>
    </header>

    <?php foreach ($sections as $section): ?>
        <?php
        if (!is_array($section)) {
            continue;
        }
        $isRisk = !empty($section['is_risk']);
        $isEmpty = !empty($section['is_empty']);
        ?>
        <section class="client-report-section<?= $isRisk ? ' client-report-risk' : '' ?>">
            <h2 class="client-report-section-title"><?= e((string) ($section['heading_ru'] ?? '')) ?></h2>
            <?php if ($isEmpty): ?>
                <p class="client-report-empty"><?= e((string) ($section['empty_message'] ?? 'Раздел будет заполнен после ручной редакции.')) ?></p>
            <?php else: ?>
                <div class="client-report-section-body">
                    <?= (string) ($section['body_html'] ?? '') ?>
                </div>
            <?php endif; ?>
        </section>
    <?php endforeach; ?>

    <footer class="client-report-footer">
        <p>
            <?= e((string) ($document['brand'] ?? 'i-SEO')) ?>
            · <?= e((string) ($document['client_name'] ?? '—')) ?>
            · <?= e((string) ($document['site_display'] ?? '—')) ?>
            · <?= e((string) ($document['period_label'] ?? '—')) ?>
        </p>
        <?php if ($localDemo): ?>
            <p>Локальная демо-среда · не продакшен</p>
        <?php endif; ?>
    </footer>
</article>

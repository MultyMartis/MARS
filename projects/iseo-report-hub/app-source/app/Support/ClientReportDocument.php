<?php
declare(strict_types=1);

namespace Iseo\Support;

/**
 * Preview-only mapper: assemble() payload → client document DTO.
 * Does not read or write the database. Does not feed export/PDF.
 *
 * Optional local show-ready demo fallback applies only in preview/print
 * when gated (local env + known demo report id 1). Never mutates DB.
 */
final class ClientReportDocument
{
    /** Known local demo report for show-ready preview overlay. */
    public const SHOW_READY_DEMO_REPORT_ID = 1;

    /** @var list<string> */
    public const SECTION_ORDER = [
        'executive_summary',
        'results_summary',
        'work_completed',
        'key_findings',
        'risks_and_blockers',
        'next_month_plan',
    ];

    /** @var list<string> */
    private const MANUAL_KEYS = [
        'executive_summary',
        'results_summary',
        'key_findings',
    ];

    /** @var list<string> */
    private const AUTO_KEYS = [
        'work_completed',
        'risks_and_blockers',
        'next_month_plan',
    ];

    /** @var array<int, string> */
    private const MONTHS_RU = [
        1 => 'января',
        2 => 'февраля',
        3 => 'марта',
        4 => 'апреля',
        5 => 'мая',
        6 => 'июня',
        7 => 'июля',
        8 => 'августа',
        9 => 'сентября',
        10 => 'октября',
        11 => 'ноября',
        12 => 'декабря',
    ];

    /**
     * @param array{
     *   report: array<string, mixed>,
     *   blocks: list<array<string, mixed>>,
     *   render_mode: string,
     *   flat_fields: array<string, string>,
     *   flat_present: bool,
     *   generated_at: string
     * } $payload
     * @param array<string, string> $assemblyBodies Optional in-memory work-entry assembly text keyed by section.
     * @return array<string, mixed>
     */
    public static function fromAssemble(array $payload, bool $localDemo, array $assemblyBodies = []): array
    {
        $report = is_array($payload['report'] ?? null) ? $payload['report'] : [];
        $blocks = is_array($payload['blocks'] ?? null) ? $payload['blocks'] : [];
        $flatFields = is_array($payload['flat_fields'] ?? null) ? $payload['flat_fields'] : [];
        $renderMode = (string) ($payload['render_mode'] ?? '');
        $generatedAt = (string) ($payload['generated_at'] ?? '');
        $reportId = (int) ($report['id'] ?? 0);

        $blocksByKey = [];
        foreach ($blocks as $block) {
            if (!is_array($block)) {
                continue;
            }
            $key = (string) ($block['block_key'] ?? '');
            if ($key === '' || isset($blocksByKey[$key])) {
                continue;
            }
            $blocksByKey[$key] = $block;
        }

        $statusRaw = (string) ($report['status'] ?? '');
        $finalized = $statusRaw === 'finalized';
        $clientName = self::stripFixtureMarkers((string) ($report['client_name'] ?? ''));
        $projectName = self::stripFixtureMarkers((string) ($report['project_name'] ?? ''));
        $siteUrl = self::stripFixtureMarkers((string) ($report['primary_site_url'] ?? ''));
        $siteLabel = self::stripFixtureMarkers((string) ($report['primary_site_label'] ?? ''));
        $siteDisplay = $siteLabel !== '' ? $siteLabel : $siteUrl;

        $periodLabel = self::periodLabel(
            (string) ($report['period_start'] ?? ''),
            (string) ($report['period_end'] ?? ''),
            (string) ($report['period_title'] ?? ''),
            (string) ($report['period_key'] ?? '')
        );

        $reportDateSource = trim((string) ($report['finalized_at'] ?? ''));
        if ($reportDateSource === '') {
            $reportDateSource = $generatedAt;
        }
        $reportDate = self::formatDateTimeRu($reportDateSource);

        $rawTitle = self::stripFixtureMarkers((string) ($report['title'] ?? ''));
        $title = $rawTitle !== '' && !UiTextSanitizer::isDemoJunk($rawTitle) ? $rawTitle : 'SEO-отчёт';

        $pageTitle = 'SEO-отчёт';
        if ($clientName !== '') {
            $pageTitle .= ' — ' . $clientName;
        }
        if ($periodLabel !== '') {
            $pageTitle .= ' — ' . $periodLabel;
        }

        $allSectionsEmpty = true;
        $sections = [];
        foreach (self::SECTION_ORDER as $key) {
            $bodyText = '';
            $summaryText = '';
            if (isset($blocksByKey[$key]) && is_array($blocksByKey[$key])) {
                $bodyText = self::stripFixtureMarkers((string) ($blocksByKey[$key]['body'] ?? ''));
                $summaryText = self::stripFixtureMarkers((string) ($blocksByKey[$key]['summary'] ?? ''));
            } elseif ($renderMode === 'flat_fallback') {
                $bodyText = self::stripFixtureMarkers((string) ($flatFields[$key] ?? ''));
            }

            $displayText = $bodyText !== '' ? $bodyText : $summaryText;
            $displayText = UiTextSanitizer::cleanBodyOrEmpty($displayText, $key);
            $isEmpty = $displayText === '';
            if (!$isEmpty) {
                $allSectionsEmpty = false;
            }

            $sections[] = [
                'key' => $key,
                'heading_ru' => UiLabels::blockKey($key),
                'body_html' => $isEmpty ? '' : self::formatBodyHtml($displayText),
                'is_empty' => $isEmpty,
                'is_manual' => in_array($key, self::MANUAL_KEYS, true),
                'empty_message' => UiTextSanitizer::fallbackForSection($key),
                'is_risk' => $key === 'risks_and_blockers',
            ];
        }

        $isEmptyDraftPreview = !$finalized && $blocks === [] && $allSectionsEmpty;
        $showReadyDemo = self::isShowReadyDemoReport($reportId, $localDemo, $isEmptyDraftPreview);

        if ($showReadyDemo) {
            $sections = self::applyShowReadyFallbacks($sections, $assemblyBodies);
            $allSectionsEmpty = true;
            foreach ($sections as $section) {
                if (empty($section['is_empty'])) {
                    $allSectionsEmpty = false;
                    break;
                }
            }
            $isEmptyDraftPreview = !$finalized && $blocks === [] && $allSectionsEmpty;
        }

        return [
            'brand' => 'i-SEO',
            'document_type' => 'SEO-отчёт',
            'title' => $isEmptyDraftPreview ? 'SEO-отчёт' : $title,
            'client_name' => $clientName !== '' ? $clientName : '—',
            'project_name' => $projectName !== '' ? $projectName : '—',
            'site_display' => $siteDisplay !== '' ? $siteDisplay : '—',
            'period_label' => $periodLabel !== '' ? $periodLabel : '—',
            'status_label' => $finalized ? 'Итоговый отчёт' : 'Черновик',
            'is_finalized' => $finalized,
            'is_empty_draft' => $isEmptyDraftPreview,
            'draft_disclaimer' => UiLabels::draftClientDisclaimer(),
            'report_date' => $reportDate !== '' ? $reportDate : '—',
            'local_demo' => $localDemo,
            'show_ready_demo' => $showReadyDemo,
            'page_title' => $pageTitle,
            'sections' => $sections,
        ];
    }

    /**
     * Local demo report 1 only. Never applies to empty drafts (e.g. report 5).
     */
    public static function isShowReadyDemoReport(int $reportId, bool $localDemo, bool $isEmptyDraftPreview): bool
    {
        if (!$localDemo) {
            return false;
        }
        if ($reportId !== self::SHOW_READY_DEMO_REPORT_ID) {
            return false;
        }
        if ($isEmptyDraftPreview) {
            return false;
        }

        return true;
    }

    public static function demoCopyForSection(string $sectionKey): ?string
    {
        return match ($sectionKey) {
            'executive_summary' => 'В июле была выполнена базовая SEO-подготовка проекта: проверены технические факторы, собраны приоритетные группы запросов, подготовлены рекомендации по коммерческим страницам и сформирован план работ на следующий месяц.',
            'results_summary' => 'Количественные показатели в текущей версии MVP не заполняются автоматически. В отчете зафиксированы выполненные работы, подготовленные рекомендации и план следующего этапа продвижения.',
            'work_completed' => "- Проведен технический мониторинг сайта.\n"
                . "- Проверена индексация ключевых страниц.\n"
                . "- Актуализирована семантика по приоритетным группам.\n"
                . "- Подготовлены рекомендации по коммерческим факторам.",
            'key_findings' => "- Техническая база проекта требует регулярного контроля, чтобы не терять качество индексации и доступность важных страниц.\n"
                . "- Приоритетные коммерческие страницы нуждаются в доработке факторов доверия и полноты информации.\n"
                . "- Следующий этап работ лучше сфокусировать на мета-тегах, текстах и согласованных группах страниц.",
            'risks_and_blockers' => 'Требуется согласование приоритетных страниц для следующего этапа работ.',
            'next_month_plan' => "- Доработать мета-теги для приоритетных страниц.\n"
                . "- Подготовить новые тексты для выбранных разделов.\n"
                . "- Продолжить улучшение коммерческих факторов.",
            default => null,
        };
    }

    /**
     * Fill empty/junk sections for gated local demo preview only.
     * Priority: existing sanitized body → assembly body (auto keys) → static demo copy.
     *
     * @param list<array<string, mixed>> $sections
     * @param array<string, string> $assemblyBodies
     * @return list<array<string, mixed>>
     */
    public static function applyShowReadyFallbacks(array $sections, array $assemblyBodies = []): array
    {
        $out = [];
        foreach ($sections as $section) {
            if (!is_array($section)) {
                continue;
            }
            $key = (string) ($section['key'] ?? '');
            $isEmpty = !empty($section['is_empty']);
            if (!$isEmpty || $key === '') {
                $out[] = $section;
                continue;
            }

            $candidate = '';
            if (in_array($key, self::AUTO_KEYS, true)) {
                $assembly = trim((string) ($assemblyBodies[$key] ?? ''));
                if ($assembly !== '') {
                    $candidate = UiTextSanitizer::cleanBodyOrEmpty($assembly, $key);
                }
            }

            if ($candidate === '') {
                $demo = self::demoCopyForSection($key);
                if ($demo !== null) {
                    $candidate = UiTextSanitizer::cleanBodyOrEmpty($demo, $key);
                }
            }

            if ($candidate === '') {
                $out[] = $section;
                continue;
            }

            $section['body_html'] = self::formatBodyHtml($candidate);
            $section['is_empty'] = false;
            $out[] = $section;
        }

        return $out;
    }

    public static function stripFixtureMarkers(string $text): string
    {
        return UiTextSanitizer::stripFixtureMarkers($text);
    }

    public static function formatBodyHtml(string $text): string
    {
        $text = UiTextSanitizer::cleanBodyOrEmpty($text);
        $text = str_replace(["\r\n", "\r"], "\n", $text);
        $text = trim($text);
        if ($text === '') {
            return '';
        }

        $lines = explode("\n", $text);
        $html = '';
        $buffer = [];
        $mode = 'none';

        $flush = static function () use (&$html, &$buffer, &$mode): void {
            if ($mode === 'ul' && $buffer !== []) {
                $html .= '<ul class="client-report-list">';
                foreach ($buffer as $item) {
                    $html .= '<li>' . e($item) . '</li>';
                }
                $html .= '</ul>';
            } elseif ($mode === 'p' && $buffer !== []) {
                $para = implode("\n", $buffer);
                $html .= '<p>' . nl2br(e($para), false) . '</p>';
            }
            $buffer = [];
            $mode = 'none';
        };

        foreach ($lines as $line) {
            $trimmed = trim($line);
            if ($trimmed === '') {
                $flush();
                continue;
            }
            if (preg_match('/^[-•*]\s+(.+)$/u', $trimmed, $m) === 1) {
                if ($mode !== 'ul') {
                    $flush();
                    $mode = 'ul';
                }
                $buffer[] = $m[1];
                continue;
            }
            if ($mode !== 'p') {
                $flush();
                $mode = 'p';
            }
            $buffer[] = $line;
        }
        $flush();

        return $html;
    }

    private static function periodLabel(string $start, string $end, string $title, string $key): string
    {
        $startRu = self::formatDateRu($start);
        $endRu = self::formatDateRu($end);
        if ($startRu !== '' && $endRu !== '') {
            return $startRu . ' — ' . $endRu;
        }
        $cleanTitle = UiTextSanitizer::stripFixtureMarkers($title);
        if ($cleanTitle !== '' && !UiTextSanitizer::isDemoJunk($cleanTitle)) {
            return $cleanTitle;
        }
        $cleanKey = UiTextSanitizer::stripFixtureMarkers($key);

        return $cleanKey;
    }

    private static function formatDateRu(string $raw): string
    {
        $raw = trim($raw);
        if ($raw === '') {
            return '';
        }
        $ts = strtotime($raw);
        if ($ts === false) {
            return $raw;
        }
        $month = (int) date('n', $ts);
        $monthName = self::MONTHS_RU[$month] ?? date('m', $ts);

        return ((int) date('j', $ts)) . ' ' . $monthName . ' ' . date('Y', $ts);
    }

    private static function formatDateTimeRu(string $raw): string
    {
        $raw = trim($raw);
        if ($raw === '') {
            return '';
        }
        $date = self::formatDateRu($raw);
        $ts = strtotime($raw);
        if ($ts === false) {
            return $date;
        }
        $time = date('H:i', $ts);
        if ($time === '00:00') {
            return $date;
        }

        return $date . ', ' . $time;
    }
}

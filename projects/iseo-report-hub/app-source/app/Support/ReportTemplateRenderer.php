<?php
declare(strict_types=1);

namespace Iseo\Support;

use Iseo\Services\ReportTemplateService;

/**
 * Renders snapshot payload HTML using the code-first default template.
 */
final class ReportTemplateRenderer
{
    public function __construct(
        private ReportTemplateService $templates
    ) {
    }

    /**
     * @param array<string, mixed> $snapshot
     * @param array<string, mixed> $payload
     */
    public function render(array $snapshot, array $payload, string $generatedAt, ?ReportTemplate $template = null): string
    {
        $template ??= $this->templates->getDefaultTemplate();
        $tokens = $template->tokens;

        $title = (string) ($snapshot['title'] ?? ($payload['monthly_report']['title'] ?? 'SEO-отчет'));
        // Future regenerations should prefer Russian client titles; existing artifacts are not rewritten.
        $snapshotKey = (string) ($snapshot['snapshot_key'] ?? '');
        $version = (int) ($snapshot['version'] ?? 0);
        $checksum = (string) ($snapshot['checksum_sha256'] ?? '');
        $period = is_array($payload['period'] ?? null) ? $payload['period'] : [];
        $client = is_array($payload['client'] ?? null) ? $payload['client'] : [];
        $project = is_array($payload['project'] ?? null) ? $payload['project'] : [];
        $site = is_array($payload['site'] ?? null) ? $payload['site'] : [];
        $monthly = is_array($payload['monthly_report'] ?? null) ? $payload['monthly_report'] : [];
        $blocks = is_array($payload['blocks'] ?? null) ? $payload['blocks'] : [];
        $weeklySources = is_array($payload['weekly_sources'] ?? null) ? $payload['weekly_sources'] : [];

        $periodKey = (string) ($period['key'] ?? '');
        $renderMode = (string) ($snapshot['render_mode'] ?? ($payload['metadata']['render_mode'] ?? ''));

        $esc = static fn (mixed $v): string => htmlspecialchars((string) $v, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');

        $html = '<!DOCTYPE html>' . "\n";
        $html .= '<html lang="ru">' . "\n";
        $html .= '<head>' . "\n";
        $html .= '<meta charset="UTF-8">' . "\n";
        $html .= '<meta name="viewport" content="width=device-width, initial-scale=1">' . "\n";
        $html .= '<meta name="iseo-template-id" content="' . $esc($template->id) . '">' . "\n";
        $html .= '<meta name="iseo-template-version" content="' . $esc((string) $template->version) . '">' . "\n";
        $html .= '<meta name="iseo-render-target" content="' . $esc($template->renderTarget) . '">' . "\n";
        $html .= '<meta name="iseo-template-source" content="' . $esc($template->source) . '">' . "\n";
        $html .= '<meta name="iseo-branding" content="' . $esc($template->branding) . '">' . "\n";
        $html .= '<!-- iseo-report-template id=' . $esc($template->id)
            . ' version=' . $esc((string) $template->version)
            . ' render_target=' . $esc($template->renderTarget)
            . ' source=' . $esc($template->source)
            . ' branding=' . $esc($template->branding)
            . ' snapshot_key=' . $esc($snapshotKey)
            . ' snapshot_checksum=' . $esc($checksum)
            . ' generated_at=' . $esc($generatedAt)
            . ' -->' . "\n";
        $html .= '<title>' . $esc($title) . ' — export</title>' . "\n";
        $html .= '<style>' . $this->embeddedCss($tokens) . '</style>' . "\n";
        $html .= '</head>' . "\n";
        $html .= '<body>' . "\n";

        $html .= '<header class="export-header">' . "\n";
        $html .= '<p class="export-brand">i-SEO</p>' . "\n";
        $html .= '<p class="export-badge">Internal report export — HTML artifact</p>' . "\n";
        $html .= '<h1>' . $esc($title) . '</h1>' . "\n";
        $html .= '<dl class="export-meta">' . "\n";
        $html .= '<dt>Period</dt><dd><code>' . $esc($periodKey) . '</code></dd>' . "\n";
        $html .= '<dt>Client</dt><dd>' . $esc((string) ($client['name'] ?? '—')) . '</dd>' . "\n";
        $html .= '<dt>Project</dt><dd>' . $esc((string) ($project['name'] ?? '—')) . '</dd>' . "\n";
        $html .= '<dt>Site</dt><dd>' . $esc((string) ($site['url'] ?? '—'));
        if (!empty($site['label'])) {
            $html .= ' — ' . $esc((string) $site['label']);
        }
        $html .= '</dd>' . "\n";
        $html .= '<dt>Snapshot key</dt><dd><code>' . $esc($snapshotKey) . '</code></dd>' . "\n";
        $html .= '<dt>Snapshot version</dt><dd>' . $esc((string) $version) . '</dd>' . "\n";
        $html .= '<dt>Snapshot checksum</dt><dd><code class="checksum">' . $esc($checksum) . '</code></dd>' . "\n";
        $html .= '<dt>Render mode</dt><dd><code>' . $esc($renderMode) . '</code></dd>' . "\n";
        $html .= '<dt>Template</dt><dd><code>' . $esc($template->id) . '</code> v'
            . $esc((string) $template->version) . '</dd>' . "\n";
        $html .= '<dt>Export generated at (UTC)</dt><dd>' . $esc($generatedAt) . '</dd>' . "\n";
        $html .= '<dt>Monthly status</dt><dd>' . $esc((string) ($monthly['status'] ?? '—')) . '</dd>' . "\n";
        $html .= '</dl>' . "\n";
        $html .= '</header>' . "\n";

        if ($weeklySources !== []) {
            $html .= '<section class="export-section">' . "\n";
            $html .= '<h2>Source weekly checkpoints</h2>' . "\n";
            $html .= '<ul>' . "\n";
            foreach ($weeklySources as $wc) {
                if (!is_array($wc)) {
                    continue;
                }
                $html .= '<li><code>' . $esc((string) ($wc['checkpoint_key'] ?? '')) . '</code>';
                $html .= ' — ' . $esc((string) ($wc['title'] ?? ''));
                $html .= ' (' . $esc((string) ($wc['status'] ?? '')) . ')</li>' . "\n";
            }
            $html .= '</ul>' . "\n";
            $html .= '</section>' . "\n";
        }

        $flatFields = is_array($monthly['flat_fields'] ?? null) ? $monthly['flat_fields'] : [];
        if ($flatFields !== []) {
            $html .= '<section class="export-section export-section--summary">' . "\n";
            $html .= '<h2>Executive summary / monthly fields</h2>' . "\n";
            foreach ($flatFields as $key => $value) {
                if (!is_string($key)) {
                    continue;
                }
                $label = str_replace('_', ' ', $key);
                $label = ucwords($label);
                $html .= '<article class="export-block">' . "\n";
                $html .= '<h3>' . $esc($label) . '</h3>' . "\n";
                $html .= '<div class="export-body">' . nl2br($esc((string) $value), false) . '</div>' . "\n";
                $html .= '</article>' . "\n";
            }
            $html .= '</section>' . "\n";
        }

        $html .= '<section class="export-section">' . "\n";
        $html .= '<h2>Report blocks</h2>' . "\n";
        if ($blocks === []) {
            $html .= '<p class="note">No blocks in snapshot payload.</p>' . "\n";
        } else {
            foreach ($blocks as $block) {
                if (!is_array($block)) {
                    continue;
                }
                $blockType = strtolower(trim((string) ($block['block_type'] ?? '')));
                $statusClass = $this->statusClassForBlockType($blockType);
                $html .= '<article class="export-block' . ($statusClass !== '' ? ' ' . $statusClass : '') . '">' . "\n";
                $html .= '<h3>' . $esc((string) ($block['title'] ?? '')) . '</h3>' . "\n";
                $html .= '<p class="export-block-meta"><code>' . $esc((string) ($block['block_key'] ?? '')) . '</code>';
                $html .= ' · ' . $esc((string) ($block['block_type'] ?? ''));
                $html .= ' · sort ' . $esc((string) ($block['sort_order'] ?? '')) . '</p>' . "\n";
                $summary = trim((string) ($block['summary'] ?? ''));
                if ($summary !== '') {
                    $html .= '<p class="export-summary"><em>' . $esc($summary) . '</em></p>' . "\n";
                }
                $body = trim((string) ($block['body'] ?? ''));
                if ($body !== '') {
                    $html .= '<div class="export-body">' . nl2br($esc($body), false) . '</div>' . "\n";
                }
                $html .= '</article>' . "\n";
            }
        }
        $html .= '</section>' . "\n";

        $html .= '<footer class="export-footer">' . "\n";
        $html .= '<p>Immutable snapshot export. Source: report_snapshots payload only.</p>' . "\n";
        $html .= '<p class="export-diagnostics">Template: <code>' . $esc($template->id) . '</code> version '
            . $esc((string) $template->version)
            . ' · render target <code>' . $esc($template->renderTarget) . '</code>'
            . ' · branding <code>' . $esc($template->branding) . '</code></p>' . "\n";
        $html .= '<p class="export-diagnostics">Snapshot: <code>' . $esc($snapshotKey) . '</code>'
            . ' · checksum <code class="checksum">' . $esc($checksum) . '</code>'
            . ' · generated_at <code>' . $esc($generatedAt) . '</code></p>' . "\n";
        $html .= '</footer>' . "\n";
        $html .= '</body>' . "\n";
        $html .= '</html>';

        return $html;
    }

    /**
     * @param array<string, mixed> $tokens
     */
    public function embeddedCss(array $tokens): string
    {
        $font = (string) ($tokens['font_stack'] ?? 'Arial, "Segoe UI", Calibri, sans-serif');
        $text = (string) ($tokens['color_text'] ?? '#1a1a1a');
        $muted = (string) ($tokens['color_muted'] ?? '#555555');
        $border = (string) ($tokens['color_border'] ?? '#cccccc');
        $borderSoft = (string) ($tokens['color_border_soft'] ?? '#dddddd');
        $bg = (string) ($tokens['color_bg'] ?? '#ffffff');
        $tableHeader = (string) ($tokens['color_table_header'] ?? '#f5f5f5');
        $brand = (string) ($tokens['color_brand'] ?? '#0f172a');
        $maxWidth = (string) ($tokens['max_width'] ?? '52rem');
        $pageMargin = (string) ($tokens['page_margin'] ?? '14mm 12mm');
        $lineHeight = (string) ($tokens['line_height'] ?? '1.5');
        $h1 = (string) ($tokens['h1_size'] ?? '1.65rem');
        $h2 = (string) ($tokens['h2_size'] ?? '1.25rem');
        $h3 = (string) ($tokens['h3_size'] ?? '1.05rem');
        $ok = (string) ($tokens['status_ok'] ?? '#166534');
        $warn = (string) ($tokens['status_warn'] ?? '#92400e');
        $risk = (string) ($tokens['status_risk'] ?? '#991b1b');
        $info = (string) ($tokens['status_info'] ?? '#334155');

        return <<<CSS
@page { size: A4; margin: {$pageMargin}; }
* { box-sizing: border-box; }
body {
  font-family: {$font};
  color: {$text};
  background: {$bg};
  line-height: {$lineHeight};
  margin: 0 auto;
  padding: 1.5rem 1.25rem 2rem;
  max-width: {$maxWidth};
}
.export-brand {
  margin: 0 0 0.35rem;
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: {$brand};
}
.export-badge {
  margin: 0 0 0.75rem;
  font-size: 0.8rem;
  color: {$muted};
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.export-header h1 {
  margin: 0 0 1rem;
  font-size: {$h1};
  font-weight: 700;
  line-height: 1.25;
}
.export-meta {
  display: grid;
  grid-template-columns: 11rem 1fr;
  gap: 0.3rem 1rem;
  margin: 0;
  padding: 0.75rem 0;
  border-top: 1px solid {$border};
  border-bottom: 1px solid {$border};
  font-size: 0.92rem;
}
.export-meta dt { font-weight: 600; margin: 0; }
.export-meta dd { margin: 0; }
.export-section {
  margin-top: 1.75rem;
  padding-top: 1rem;
  border-top: 1px solid {$borderSoft};
  break-inside: avoid;
  page-break-inside: avoid;
}
.export-section h2 {
  margin: 0 0 0.85rem;
  font-size: {$h2};
  font-weight: 700;
  break-after: avoid;
  page-break-after: avoid;
}
.export-block {
  margin: 0 0 1.35rem;
  padding: 0 0 0 0.75rem;
  border-left: 3px solid transparent;
  break-inside: avoid;
  page-break-inside: avoid;
}
.export-block h3 {
  margin: 0 0 0.35rem;
  font-size: {$h3};
  font-weight: 700;
  break-after: avoid;
  page-break-after: avoid;
}
.export-block-meta { margin: 0 0 0.35rem; font-size: 0.82rem; color: {$muted}; }
.export-summary { margin: 0.25rem 0; color: {$text}; }
.export-body { margin-top: 0.4rem; }
.export-block--ok { border-left-color: {$ok}; }
.export-block--warn { border-left-color: {$warn}; }
.export-block--risk { border-left-color: {$risk}; }
.export-block--info { border-left-color: {$info}; }
.checksum { word-break: break-all; font-size: 0.78rem; }
.export-footer {
  margin-top: 2rem;
  padding-top: 0.85rem;
  border-top: 1px solid {$borderSoft};
  font-size: 0.78rem;
  color: {$muted};
}
.export-diagnostics { margin: 0.35rem 0 0; }
.note { color: {$muted}; }
table.export-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
table.export-table th,
table.export-table td {
  border: 1px solid {$borderSoft};
  padding: 0.4rem 0.5rem;
  text-align: left;
  vertical-align: top;
}
table.export-table th { background: {$tableHeader}; font-weight: 600; }
@media print {
  body {
    max-width: none;
    padding: 0;
    margin: 0;
    color: {$text};
    background: {$bg};
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
  .export-section,
  .export-block {
    break-inside: avoid;
    page-break-inside: avoid;
  }
  .export-section h2,
  .export-block h3 {
    break-after: avoid;
    page-break-after: avoid;
  }
}
CSS;
    }

    private function statusClassForBlockType(string $blockType): string
    {
        if ($blockType === '') {
            return '';
        }
        if (str_contains($blockType, 'risk') || str_contains($blockType, 'blocker') || str_contains($blockType, 'issue')) {
            return 'export-block--risk';
        }
        if (str_contains($blockType, 'warn') || str_contains($blockType, 'attention')) {
            return 'export-block--warn';
        }
        if (str_contains($blockType, 'ok') || str_contains($blockType, 'success') || str_contains($blockType, 'positive')) {
            return 'export-block--ok';
        }
        if (str_contains($blockType, 'info') || str_contains($blockType, 'note')) {
            return 'export-block--info';
        }
        return '';
    }
}

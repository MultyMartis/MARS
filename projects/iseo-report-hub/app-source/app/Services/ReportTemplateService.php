<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Support\ReportTemplate;

/**
 * Code-first default report template registry (no DB).
 */
final class ReportTemplateService
{
    public function getDefaultTemplate(): ReportTemplate
    {
        return new ReportTemplate(
            ReportTemplate::ID_DEFAULT,
            ReportTemplate::VERSION_DEFAULT,
            ReportTemplate::RENDER_TARGET_HTML_EXPORT,
            ReportTemplate::SOURCE_REPORT_SNAPSHOT,
            ReportTemplate::BRANDING_ISEO_DEFAULT,
            ReportTemplate::DISPLAY_LABEL_DEFAULT,
            $this->defaultTokens()
        );
    }

    /**
     * @return array{id:string,version:int,render_target:string,source:string,branding:string,display_label:string}
     */
    public function getDefaultSummary(): array
    {
        return $this->getDefaultTemplate()->toSummary();
    }

    public function isKnownTemplate(string $id, int $version): bool
    {
        return $id === ReportTemplate::ID_DEFAULT && $version === ReportTemplate::VERSION_DEFAULT;
    }

    /**
     * @return array{
     *   ok:bool,
     *   message:string,
     *   template:?ReportTemplate
     * }
     */
    public function resolve(string $id, int $version): array
    {
        if ($this->isKnownTemplate($id, $version)) {
            return [
                'ok' => true,
                'message' => 'Template resolved.',
                'template' => $this->getDefaultTemplate(),
            ];
        }

        return [
            'ok' => false,
            'message' => 'Unknown template id/version.',
            'template' => null,
        ];
    }

    /**
     * Design tokens for iseo_default_v1 (embedded CSS consumes these conceptually).
     *
     * @return array<string, mixed>
     */
    public function defaultTokens(): array
    {
        return [
            'theme' => 'light',
            'font_stack' => 'Arial, "Segoe UI", Calibri, sans-serif',
            'color_text' => '#1a1a1a',
            'color_muted' => '#555555',
            'color_border' => '#cccccc',
            'color_border_soft' => '#dddddd',
            'color_bg' => '#ffffff',
            'color_table_header' => '#f5f5f5',
            'color_brand' => '#0f172a',
            'max_width' => '52rem',
            'radius' => '0',
            'page_size' => 'A4',
            'page_margin' => '14mm 12mm',
            'line_height' => '1.5',
            'h1_size' => '1.65rem',
            'h2_size' => '1.25rem',
            'h3_size' => '1.05rem',
            'status_ok' => '#166534',
            'status_warn' => '#92400e',
            'status_risk' => '#991b1b',
            'status_info' => '#334155',
        ];
    }

    /**
     * UI label for historical export rows without recorded template metadata (DB NULL).
     */
    public function legacyTemplateLabel(): string
    {
        return 'устаревший / не записан';
    }
}

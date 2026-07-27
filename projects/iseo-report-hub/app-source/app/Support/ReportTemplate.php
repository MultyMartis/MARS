<?php
declare(strict_types=1);

namespace Iseo\Support;

/**
 * Code-first report export template identity (MVP registry = Git/source).
 */
final class ReportTemplate
{
    public const ID_DEFAULT = 'iseo_default_v1';

    public const VERSION_DEFAULT = 1;

    public const RENDER_TARGET_HTML_EXPORT = 'html_export';

    public const SOURCE_REPORT_SNAPSHOT = 'report_snapshot';

    public const BRANDING_ISEO_DEFAULT = 'iseo_default';

    public const DISPLAY_LABEL_DEFAULT = 'i-SEO Default Report Template v1';

    /**
     * @param array<string, mixed> $tokens
     */
    public function __construct(
        public readonly string $id,
        public readonly int $version,
        public readonly string $renderTarget,
        public readonly string $source,
        public readonly string $branding,
        public readonly string $displayLabel,
        public readonly array $tokens
    ) {
    }

    public function isDefault(): bool
    {
        return $this->id === self::ID_DEFAULT && $this->version === self::VERSION_DEFAULT;
    }

    /**
     * @return array{id:string,version:int,render_target:string,source:string,branding:string,display_label:string}
     */
    public function toSummary(): array
    {
        return [
            'id' => $this->id,
            'version' => $this->version,
            'render_target' => $this->renderTarget,
            'source' => $this->source,
            'branding' => $this->branding,
            'display_label' => $this->displayLabel,
        ];
    }
}

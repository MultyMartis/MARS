<?php
declare(strict_types=1);

namespace Iseo\Support;

/**
 * Render-layer text sanitizer for normal UI / client preview.
 * Does not mutate the database.
 */
final class UiTextSanitizer
{
    /** @var list<string> */
    private const EXACT_JUNK = [
        'updated body',
        'risks body',
        'test body',
        'demo body',
        'lorem ipsum',
    ];

    public static function stripFixtureMarkers(string $value): string
    {
        $text = $value;
        $text = preg_replace('/\bLOCAL_FIXTURE_ONLY\b/iu', '', $text) ?? $text;
        $text = preg_replace('/\bMARS_FIXTURE[A-Z0-9_]*/iu', '', $text) ?? $text;
        $text = preg_replace('/[ \t]*[—–\-_|]+[ \t]*$/u', '', $text) ?? $text;
        $text = preg_replace('/^[ \t]*[—–\-_|]+[ \t]*/u', '', $text) ?? $text;
        $text = preg_replace('/[ \t]{2,}/u', ' ', $text) ?? $text;
        $text = preg_replace("/\n{3,}/u", "\n\n", $text) ?? $text;
        $text = preg_replace('/[ \t]+([—–\-])/u', ' $1', $text) ?? $text;
        $text = preg_replace('/([—–\-])[ \t]+/u', '$1 ', $text) ?? $text;

        return trim($text);
    }

    public static function isDemoJunk(string $value): bool
    {
        $trimmed = trim($value);
        if ($trimmed === '') {
            return true;
        }

        $cleaned = self::stripFixtureMarkers($trimmed);
        if ($cleaned === '') {
            return true;
        }

        $normalized = mb_strtolower($cleaned);
        if (in_array($normalized, self::EXACT_JUNK, true)) {
            return true;
        }

        // Numeric-only bodies (and short digit junk with optional spaces).
        if (preg_match('/^\d+$/u', $cleaned) === 1) {
            return true;
        }
        if (preg_match('/^[\d\s]+$/u', $cleaned) === 1 && preg_match('/\d/u', $cleaned) === 1) {
            $digits = preg_replace('/\D+/u', '', $cleaned) ?? '';
            if ($digits !== '' && mb_strlen($digits) <= 12) {
                return true;
            }
        }

        // Line/token junk: known placeholders plus leftover digits only.
        if (self::isJunkTokenLine($cleaned)) {
            return true;
        }

        return false;
    }

    public static function cleanBodyOrEmpty(string $value, ?string $sectionKey = null): string
    {
        $cleaned = self::stripFixtureMarkers($value);
        if ($cleaned === '') {
            return '';
        }
        if (self::isDemoJunk($cleaned)) {
            return '';
        }

        $lines = preg_split("/\r\n|\n|\r/u", $cleaned) ?: [];
        $kept = [];
        foreach ($lines as $line) {
            $trimmed = trim($line);
            if ($trimmed === '') {
                $kept[] = '';
                continue;
            }
            $core = $trimmed;
            if (preg_match('/^[-•*]\s+(.+)$/u', $trimmed, $m) === 1) {
                $core = $m[1];
            }
            if (self::isDemoJunk($core) || self::isJunkTokenLine($core)) {
                continue;
            }
            $kept[] = $line;
        }

        while ($kept !== [] && trim((string) $kept[0]) === '') {
            array_shift($kept);
        }
        while ($kept !== [] && trim((string) $kept[count($kept) - 1]) === '') {
            array_pop($kept);
        }

        $result = implode("\n", $kept);
        $result = preg_replace("/\n{3,}/u", "\n\n", $result) ?? $result;
        $result = trim($result);
        if ($result === '' || self::isDemoJunk($result)) {
            return '';
        }

        return $result;
    }

    private static function isJunkTokenLine(string $value): bool
    {
        $tmp = preg_replace('/\b(updated body|risks body|test body|demo body|lorem ipsum)\b/iu', '', $value) ?? $value;
        $tmp = preg_replace('/\d+/u', '', $tmp) ?? $tmp;
        $tmp = preg_replace('/[\s\|_\-—–.,;:]+/u', '', $tmp) ?? $tmp;

        return $tmp === '';
    }

    public static function fallbackForSection(string $sectionKey): string
    {
        return match ($sectionKey) {
            'results_summary' => 'Метрики и результаты не заполнены в текущей версии отчета.',
            'risks_and_blockers' => 'Существенных рисков и блокеров на текущий момент не зафиксировано.',
            default => 'Раздел будет заполнен после ручной редакции.',
        };
    }

    /**
     * Clean a visible title/label; empty after sanitize → em dash.
     */
    public static function displayLabel(string $value, string $empty = '—'): string
    {
        $cleaned = self::stripFixtureMarkers($value);
        if ($cleaned === '' || self::isDemoJunk($cleaned)) {
            return $empty;
        }

        return $cleaned;
    }

    /**
     * Body for manager lists: cleaned text or calm empty placeholder.
     */
    public static function displayBody(string $value, ?string $sectionKey = null, string $empty = '—'): string
    {
        $cleaned = self::cleanBodyOrEmpty($value, $sectionKey);
        if ($cleaned === '') {
            return $empty;
        }

        return $cleaned;
    }
}

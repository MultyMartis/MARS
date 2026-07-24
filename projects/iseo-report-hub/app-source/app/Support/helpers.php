<?php
declare(strict_types=1);

/**
 * Global helpers for i-SEO Report Hub (Phase 1A).
 * No database helpers.
 */

if (!function_exists('e')) {
    /**
     * Escape a value for safe HTML output.
     */
    function e(mixed $value): string
    {
        if ($value === null) {
            return '';
        }

        if (is_bool($value)) {
            return $value ? '1' : '0';
        }

        if (is_scalar($value)) {
            return htmlspecialchars((string) $value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
        }

        return htmlspecialchars(json_encode($value, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR), ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    }
}

if (!function_exists('base_path')) {
    function base_path(string $path = ''): string
    {
        $root = defined('ISEO_BASE_PATH') ? ISEO_BASE_PATH : dirname(__DIR__, 2);
        if ($path === '') {
            return $root;
        }

        return $root . DIRECTORY_SEPARATOR . ltrim(str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $path), DIRECTORY_SEPARATOR);
    }
}

if (!function_exists('app_path')) {
    function app_path(string $path = ''): string
    {
        $root = defined('ISEO_APP_PATH') ? ISEO_APP_PATH : (base_path('app'));
        if ($path === '') {
            return $root;
        }

        return $root . DIRECTORY_SEPARATOR . ltrim(str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $path), DIRECTORY_SEPARATOR);
    }
}

if (!function_exists('config_path')) {
    function config_path(string $path = ''): string
    {
        $root = base_path('config');
        if ($path === '') {
            return $root;
        }

        return $root . DIRECTORY_SEPARATOR . ltrim(str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $path), DIRECTORY_SEPARATOR);
    }
}

if (!function_exists('public_path')) {
    function public_path(string $path = ''): string
    {
        $root = base_path('public');
        if ($path === '') {
            return $root;
        }

        return $root . DIRECTORY_SEPARATOR . ltrim(str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $path), DIRECTORY_SEPARATOR);
    }
}

if (!function_exists('storage_path')) {
    function storage_path(string $path = ''): string
    {
        $root = base_path('storage');
        if ($path === '') {
            return $root;
        }

        return $root . DIRECTORY_SEPARATOR . ltrim(str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $path), DIRECTORY_SEPARATOR);
    }
}

if (!function_exists('url_path')) {
    /**
     * Build an application path for links (no host).
     */
    function url_path(string $path = '/'): string
    {
        if ($path === '' || $path === '/') {
            return '/';
        }

        return '/' . ltrim($path, '/');
    }
}

if (!function_exists('request_method')) {
    function request_method(): string
    {
        $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
        return strtoupper((string) $method);
    }
}

if (!function_exists('request_path')) {
    function request_path(): string
    {
        $uri = $_SERVER['REQUEST_URI'] ?? '/';
        $path = parse_url($uri, PHP_URL_PATH);
        if (!is_string($path) || $path === '') {
            return '/';
        }

        // Normalize when served via /index.php/...
        $scriptName = $_SERVER['SCRIPT_NAME'] ?? '';
        if (is_string($scriptName) && $scriptName !== '' && str_starts_with($path, $scriptName)) {
            $path = substr($path, strlen($scriptName)) ?: '/';
        }

        if ($path !== '/' && str_ends_with($path, '/')) {
            $path = rtrim($path, '/') ?: '/';
        }

        return $path === '' ? '/' : $path;
    }
}

if (!function_exists('flash_set')) {
    function flash_set(string $type, string $message): void
    {
        if (!isset($_SESSION['_flash']) || !is_array($_SESSION['_flash'])) {
            $_SESSION['_flash'] = [];
        }
        $_SESSION['_flash'][] = [
            'type' => $type,
            'message' => $message,
        ];
    }
}

if (!function_exists('flash_get')) {
    /**
     * @return list<array{type:string,message:string}>
     */
    function flash_get(): array
    {
        $messages = $_SESSION['_flash'] ?? [];
        unset($_SESSION['_flash']);
        if (!is_array($messages)) {
            return [];
        }

        $out = [];
        foreach ($messages as $item) {
            if (!is_array($item)) {
                continue;
            }
            $out[] = [
                'type' => (string) ($item['type'] ?? 'info'),
                'message' => (string) ($item['message'] ?? ''),
            ];
        }

        return $out;
    }
}

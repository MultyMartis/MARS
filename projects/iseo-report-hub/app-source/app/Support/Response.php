<?php
declare(strict_types=1);

namespace Iseo\Support;

final class Response
{
    public static function html(string $body, int $status = 200, array $headers = []): void
    {
        http_response_code($status);
        if (!array_key_exists('Content-Type', $headers)) {
            $headers['Content-Type'] = 'text/html; charset=UTF-8';
        }
        foreach ($headers as $name => $value) {
            header($name . ': ' . $value);
        }
        echo $body;
    }

    public static function redirect(string $location, int $status = 302): void
    {
        http_response_code($status);
        header('Location: ' . $location);
        exit;
    }

    public static function text(string $body, int $status = 200): void
    {
        self::html($body, $status, ['Content-Type' => 'text/plain; charset=UTF-8']);
    }

    /**
     * Method-not-allowed response with Allow header.
     *
     * @param list<string> $allowed
     */
    public static function methodNotAllowed(array $allowed): void
    {
        $allow = implode(', ', $allowed);
        self::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>405</title></head>'
            . '<body><h1>405 Method Not Allowed</h1><p>Allowed: ' . \e($allow) . '</p></body></html>',
            405,
            ['Allow' => $allow]
        );
    }
}

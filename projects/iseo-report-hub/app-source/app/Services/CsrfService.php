<?php
declare(strict_types=1);

namespace Iseo\Services;

/**
 * CSRF token helper skeleton (session-backed).
 * Phase 1A: include in forms; no overbuilt middleware.
 */
final class CsrfService
{
    private const SESSION_KEY = '_csrf_token';

    public function token(): string
    {
        if (empty($_SESSION[self::SESSION_KEY]) || !is_string($_SESSION[self::SESSION_KEY])) {
            $_SESSION[self::SESSION_KEY] = bin2hex(random_bytes(32));
        }

        return $_SESSION[self::SESSION_KEY];
    }

    public function validate(?string $token): bool
    {
        if ($token === null || $token === '') {
            return false;
        }

        $sessionToken = $_SESSION[self::SESSION_KEY] ?? null;
        if (!is_string($sessionToken) || $sessionToken === '') {
            return false;
        }

        return hash_equals($sessionToken, $token);
    }

    /**
     * HTML hidden input markup (already escaped values).
     */
    public function field(): string
    {
        $token = \e($this->token());
        return '<input type="hidden" name="_csrf" value="' . $token . '">';
    }
}

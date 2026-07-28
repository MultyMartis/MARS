<?php
declare(strict_types=1);

namespace Iseo\Support;

/**
 * Cryptographic opaque tokens for public share links.
 * Plaintext is never persisted; only SHA-256 hashes are stored.
 */
final class SafeToken
{
    public const BYTE_LENGTH = 32;

    /** Hex length of bin2hex(random_bytes(32)). */
    public const PUBLIC_TOKEN_HEX_LENGTH = 64;

    /**
     * Generate a URL-safe hex token (32 bytes entropy → 64 hex chars).
     */
    public static function generate(): string
    {
        $token = bin2hex(random_bytes(self::BYTE_LENGTH));
        if (!self::isValidPublicToken($token)) {
            throw new \RuntimeException('Generated token failed public format validation.');
        }

        return $token;
    }

    /**
     * Strict public token format: exactly 64 hex chars; no path/encoded separators.
     */
    public static function isValidPublicToken(string $token): bool
    {
        if ($token === '' || strlen($token) !== self::PUBLIC_TOKEN_HEX_LENGTH) {
            return false;
        }
        if (str_contains($token, "\0")) {
            return false;
        }
        // Reject path-like / encoded path fragments before any hashing.
        if (
            str_contains($token, '/')
            || str_contains($token, '\\')
            || str_contains($token, '.')
            || str_contains($token, '%')
        ) {
            return false;
        }

        return preg_match('/^[a-fA-F0-9]{64}$/', $token) === 1;
    }

    public static function hash(string $token): string
    {
        return hash('sha256', $token);
    }

    /**
     * Hash only after format validation. Returns null for malformed tokens.
     */
    public static function hashPublicToken(string $token): ?string
    {
        if (!self::isValidPublicToken($token)) {
            return null;
        }

        return self::hash($token);
    }

    public static function equalsHash(string $storedHash, string $token): bool
    {
        if (!self::isValidPublicToken($token)) {
            return false;
        }

        $stored = strtolower(trim($storedHash));
        $computed = strtolower(self::hash($token));
        if ($stored === '' || $computed === '' || strlen($stored) !== 64 || strlen($computed) !== 64) {
            return false;
        }

        return hash_equals($stored, $computed);
    }
}

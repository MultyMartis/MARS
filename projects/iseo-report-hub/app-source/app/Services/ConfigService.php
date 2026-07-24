<?php
declare(strict_types=1);

namespace Iseo\Services;

/**
 * Config loader — defaults + optional .env.local (runtime).
 * DB credentials loaded when present; secrets never printed.
 */
final class ConfigService
{
    /** @var array<string, mixed> */
    private array $config = [];

    /** @var array<string, string> */
    private array $env = [];

    private bool $envLocalPresent = false;

    public function __construct(
        private string $basePath,
        private string $configPath
    ) {
    }

    public function load(): void
    {
        $this->env = [];
        $this->envLocalPresent = false;

        // Optional future local env — do not require; do not create.
        $envLocal = $this->basePath . DIRECTORY_SEPARATOR . '.env.local';
        if (is_file($envLocal) && is_readable($envLocal)) {
            $this->envLocalPresent = true;
            $this->env = $this->parseEnvFile($envLocal);
            $this->applyEnvToProcess($this->env);
        }

        $appDefaults = $this->loadPhpConfig($this->configPath . DIRECTORY_SEPARATOR . 'app.example.php', [
            'name' => 'i-SEO Report Hub',
            'env' => 'local',
            'debug' => true,
            'url' => 'http://iseo-report-hub.test',
            'timezone' => 'Europe/Moscow',
        ]);

        $databaseDefaults = $this->loadPhpConfig($this->configPath . DIRECTORY_SEPARATOR . 'database.example.php', [
            'driver' => 'mysql',
            'host' => '127.0.0.1',
            'port' => 3306,
            'database' => 'iseo_report_hub_dev',
            'username' => 'CHANGE_ME',
            'password' => 'CHANGE_ME',
            'charset' => 'utf8mb4',
        ]);

        $dbHost = $this->envValue('DB_HOST', (string) ($databaseDefaults['host'] ?? '127.0.0.1'));
        $dbPort = (int) $this->envValue('DB_PORT', (string) ($databaseDefaults['port'] ?? 3306));
        $dbName = $this->envValue('DB_DATABASE', (string) ($databaseDefaults['database'] ?? 'iseo_report_hub_dev'));
        $dbUser = $this->envValue('DB_USERNAME', (string) ($databaseDefaults['username'] ?? 'CHANGE_ME'));
        $dbPass = $this->envValue('DB_PASSWORD', (string) ($databaseDefaults['password'] ?? 'CHANGE_ME'));
        $dbConfigured = $this->detectDatabaseConfigured($dbHost, $dbName, $dbUser, $dbPass);

        $this->config = [
            'app' => [
                'name' => $this->envValue('APP_NAME', (string) ($appDefaults['name'] ?? 'i-SEO Report Hub')),
                'env' => $this->envValue('APP_ENV', (string) ($appDefaults['env'] ?? 'local')),
                'debug' => $this->envBool('APP_DEBUG', (bool) ($appDefaults['debug'] ?? true)),
                'url' => $this->envValue('APP_URL', (string) ($appDefaults['url'] ?? 'http://iseo-report-hub.test')),
                'timezone' => (string) ($appDefaults['timezone'] ?? 'Europe/Moscow'),
                'phase' => 'auth',
                'phase_label' => 'Auth persistence — local DB-backed login',
            ],
            'database' => [
                'driver' => (string) ($databaseDefaults['driver'] ?? 'mysql'),
                'host' => $dbHost,
                'port' => $dbPort,
                'database' => $dbName,
                'username' => $dbUser,
                'password' => $dbPass,
                'charset' => (string) ($databaseDefaults['charset'] ?? 'utf8mb4'),
                'configured' => $dbConfigured,
                'connected' => false,
            ],
            'auth' => [
                'implemented' => true,
                'status' => $dbConfigured
                    ? 'DB-backed auth available'
                    : 'Auth code present; database not configured',
            ],
            'meta' => [
                'env_local_present' => $this->envLocalPresent,
                'env_required' => false,
            ],
        ];
    }

    /**
     * @return array<string, mixed>
     */
    public function all(): array
    {
        return $this->config;
    }

    public function get(string $key, mixed $default = null): mixed
    {
        $segments = explode('.', $key);
        $value = $this->config;
        foreach ($segments as $segment) {
            if (!is_array($value) || !array_key_exists($segment, $value)) {
                return $default;
            }
            $value = $value[$segment];
        }

        return $value;
    }

    public function appName(): string
    {
        return (string) $this->get('app.name', 'i-SEO Report Hub');
    }

    public function debug(): bool
    {
        return (bool) $this->get('app.debug', false);
    }

    public function envLocalPresent(): bool
    {
        return $this->envLocalPresent;
    }

    /**
     * @return array<string, mixed>
     */
    private function loadPhpConfig(string $file, array $fallback): array
    {
        if (!is_file($file)) {
            return $fallback;
        }

        $loaded = require $file;
        if (!is_array($loaded)) {
            return $fallback;
        }

        return array_merge($fallback, $loaded);
    }

    /**
     * Minimal .env parser (KEY=VALUE). No shell expansion. No secrets invented.
     *
     * @return array<string, string>
     */
    private function parseEnvFile(string $file): array
    {
        $lines = file($file, FILE_IGNORE_NEW_LINES);
        if ($lines === false) {
            return [];
        }

        $out = [];
        foreach ($lines as $line) {
            $line = trim($line);
            if ($line === '' || str_starts_with($line, '#')) {
                continue;
            }
            if (!str_contains($line, '=')) {
                continue;
            }
            [$key, $value] = explode('=', $line, 2);
            $key = trim($key);
            if ($key === '' || !preg_match('/^[A-Z_][A-Z0-9_]*$/', $key)) {
                continue;
            }
            $value = trim($value);
            if (
                (str_starts_with($value, '"') && str_ends_with($value, '"'))
                || (str_starts_with($value, "'") && str_ends_with($value, "'"))
            ) {
                $value = substr($value, 1, -1);
            }
            $out[$key] = $value;
        }

        return $out;
    }

    /**
     * @param array<string, string> $env
     */
    private function applyEnvToProcess(array $env): void
    {
        foreach ($env as $key => $value) {
            if (getenv($key) === false) {
                putenv($key . '=' . $value);
                $_ENV[$key] = $value;
            }
        }
    }

    private function envValue(string $key, string $default): string
    {
        if (array_key_exists($key, $this->env)) {
            return $this->env[$key];
        }
        $fromProcess = getenv($key);
        if ($fromProcess !== false && $fromProcess !== '') {
            return (string) $fromProcess;
        }

        return $default;
    }

    private function envBool(string $key, bool $default): bool
    {
        $raw = $this->envValue($key, $default ? 'true' : 'false');
        $normalized = strtolower(trim($raw));
        if (in_array($normalized, ['1', 'true', 'yes', 'on'], true)) {
            return true;
        }
        if (in_array($normalized, ['0', 'false', 'no', 'off'], true)) {
            return false;
        }

        return $default;
    }

    /**
     * DB is configured when .env.local (or process env) supplies non-placeholder credentials.
     * Empty password is allowed for local Laragon; username/database must be real.
     */
    private function detectDatabaseConfigured(string $host, string $database, string $username, string $password): bool
    {
        if (!$this->envLocalPresent && getenv('DB_DATABASE') === false) {
            return false;
        }

        if ($host === '' || $database === '' || $username === '') {
            return false;
        }

        $placeholders = ['CHANGE_ME', 'changeme', 'your_password', 'your_username'];
        if (in_array($username, $placeholders, true)) {
            return false;
        }
        if (in_array($password, $placeholders, true)) {
            return false;
        }

        return true;
    }
}

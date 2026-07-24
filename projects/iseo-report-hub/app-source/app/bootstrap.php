<?php
declare(strict_types=1);

/**
 * i-SEO Report Hub — application bootstrap (Phase 1A).
 *
 * - Defines paths
 * - Loads helpers / classes / services
 * - Starts session safely
 * - Loads config defaults (optional .env.local if present later)
 * - No database connection
 *
 * @return array<string, mixed>
 */

define('ISEO_BASE_PATH', dirname(__DIR__));
define('ISEO_APP_PATH', __DIR__);
define('ISEO_PUBLIC_PATH', ISEO_BASE_PATH . DIRECTORY_SEPARATOR . 'public');
define('ISEO_CONFIG_PATH', ISEO_BASE_PATH . DIRECTORY_SEPARATOR . 'config');
define('ISEO_STORAGE_PATH', ISEO_BASE_PATH . DIRECTORY_SEPARATOR . 'storage');
define('ISEO_VIEWS_PATH', ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Views');

require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Support' . DIRECTORY_SEPARATOR . 'helpers.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Support' . DIRECTORY_SEPARATOR . 'Response.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Support' . DIRECTORY_SEPARATOR . 'Router.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Support' . DIRECTORY_SEPARATOR . 'View.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Services' . DIRECTORY_SEPARATOR . 'ConfigService.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Services' . DIRECTORY_SEPARATOR . 'AuthService.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Services' . DIRECTORY_SEPARATOR . 'CsrfService.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Controllers' . DIRECTORY_SEPARATOR . 'BaseController.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Controllers' . DIRECTORY_SEPARATOR . 'DashboardController.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Controllers' . DIRECTORY_SEPARATOR . 'AuthController.php';
require_once ISEO_APP_PATH . DIRECTORY_SEPARATOR . 'Controllers' . DIRECTORY_SEPARATOR . 'HealthController.php';

use Iseo\Services\AuthService;
use Iseo\Services\ConfigService;
use Iseo\Services\CsrfService;
use Iseo\Support\Router;
use Iseo\Support\View;

// Safe session start (no custom cookie secrets required in Phase 1A).
if (session_status() !== PHP_SESSION_ACTIVE) {
    session_name('iseo_report_hub_session');
    session_start([
        'cookie_httponly' => true,
        'cookie_samesite' => 'Lax',
        'use_strict_mode' => true,
    ]);
}

$config = new ConfigService(ISEO_BASE_PATH, ISEO_CONFIG_PATH);
$config->load();

$timezone = (string) $config->get('app.timezone', 'Europe/Moscow');
if ($timezone !== '') {
    date_default_timezone_set($timezone);
}

$auth = new AuthService();
$csrf = new CsrfService();
$view = new View(ISEO_VIEWS_PATH);
$router = new Router();

$app = [
    'base_path' => ISEO_BASE_PATH,
    'app_path' => ISEO_APP_PATH,
    'public_path' => ISEO_PUBLIC_PATH,
    'config' => $config,
    'auth' => $auth,
    'csrf' => $csrf,
    'view' => $view,
    'router' => $router,
    'phase' => '1A',
    'db_connected' => false,
];

return $app;

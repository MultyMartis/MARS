<?php
declare(strict_types=1);

/**
 * Conceptual Phase 1A routes.
 * No database. POST /login does not authenticate.
 *
 * @var array<string, mixed> $app
 */

use Iseo\Controllers\AuthController;
use Iseo\Controllers\DashboardController;
use Iseo\Controllers\HealthController;
use Iseo\Services\AuthService;
use Iseo\Services\ConfigService;
use Iseo\Services\CsrfService;
use Iseo\Support\Router;
use Iseo\Support\View;

/** @var Router $router */
$router = $app['router'];
/** @var View $view */
$view = $app['view'];
/** @var ConfigService $config */
$config = $app['config'];
/** @var AuthService $auth */
$auth = $app['auth'];
/** @var CsrfService $csrf */
$csrf = $app['csrf'];

$dashboard = new DashboardController($app, $view, $config, $auth, $csrf);
$authController = new AuthController($app, $view, $config, $auth, $csrf);
$health = new HealthController($app, $view, $config, $auth, $csrf);

$router->get('/', static function () use ($dashboard): void {
    $dashboard->index();
});

$router->get('/login', static function () use ($authController): void {
    $authController->showLogin();
});

$router->post('/login', static function () use ($authController): void {
    $authController->attemptLogin();
});

$router->get('/logout', static function () use ($authController): void {
    $authController->logout();
});

$router->get('/health', static function () use ($health): void {
    $health->index();
});

$router->setNotFound(static function () use ($health): void {
    $health->notFound();
});

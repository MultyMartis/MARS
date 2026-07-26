<?php
declare(strict_types=1);

/**
 * Conceptual routes — DB-backed auth + reporting period CRUD + weekly checkpoints.
 *
 * Dynamic /reporting-periods/{id} and /weekly-checkpoints/{id} matching is
 * registered at request time against the exact path (Router remains
 * exact-match only; no overbuilt pattern engine). Static /create segments
 * and nested weekly-checkpoint paths are matched before bare period ids.
 *
 * @var array<string, mixed> $app
 */

use Iseo\Controllers\AuthController;
use Iseo\Controllers\DashboardController;
use Iseo\Controllers\HealthController;
use Iseo\Controllers\ReportingPeriodController;
use Iseo\Controllers\WeeklyCheckpointController;
use Iseo\Repositories\ReportingPeriodRepository;
use Iseo\Repositories\WeeklyCheckpointRepository;
use Iseo\Services\AuthService;
use Iseo\Services\ConfigService;
use Iseo\Services\CsrfService;
use Iseo\Services\DatabaseService;
use Iseo\Services\ReportingPeriodService;
use Iseo\Services\WeeklyCheckpointService;
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
/** @var DatabaseService $db */
$db = $app['db'];

$dashboard = new DashboardController($app, $view, $config, $auth, $csrf);
$authController = new AuthController($app, $view, $config, $auth, $csrf);
$health = new HealthController($app, $view, $config, $auth, $csrf);

$periodRepo = new ReportingPeriodRepository($db);
$periodService = new ReportingPeriodService($periodRepo, $db);
$checkpointRepo = new WeeklyCheckpointRepository($db);
$checkpointService = new WeeklyCheckpointService($checkpointRepo, $db);
$reportingPeriods = new ReportingPeriodController($app, $view, $config, $auth, $csrf, $periodService, $checkpointService);
$weeklyCheckpoints = new WeeklyCheckpointController($app, $view, $config, $auth, $csrf, $checkpointService);

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

// Reporting periods — static routes before dynamic id matching.
$router->get('/reporting-periods', static function () use ($reportingPeriods): void {
    $reportingPeriods->index();
});

$router->get('/reporting-periods/create', static function () use ($reportingPeriods): void {
    $reportingPeriods->create();
});

$router->post('/reporting-periods', static function () use ($reportingPeriods): void {
    $reportingPeriods->store();
});

$requestPath = request_path();
if (preg_match('#^/reporting-periods/(\d+)/weekly-checkpoints/create$#', $requestPath, $m) === 1) {
    $periodId = (int) $m[1];
    $router->get($requestPath, static function () use ($weeklyCheckpoints, $periodId): void {
        $weeklyCheckpoints->create($periodId);
    });
} elseif (preg_match('#^/reporting-periods/(\d+)/weekly-checkpoints$#', $requestPath, $m) === 1) {
    $periodId = (int) $m[1];
    $router->get($requestPath, static function () use ($weeklyCheckpoints, $periodId): void {
        $weeklyCheckpoints->indexForPeriod($periodId);
    });
    $router->post($requestPath, static function () use ($weeklyCheckpoints, $periodId): void {
        $weeklyCheckpoints->store($periodId);
    });
} elseif (preg_match('#^/weekly-checkpoints/(\d+)/edit$#', $requestPath, $m) === 1) {
    $checkpointId = (int) $m[1];
    $router->get($requestPath, static function () use ($weeklyCheckpoints, $checkpointId): void {
        $weeklyCheckpoints->edit($checkpointId);
    });
} elseif (preg_match('#^/weekly-checkpoints/(\d+)$#', $requestPath, $m) === 1) {
    $checkpointId = (int) $m[1];
    $router->get($requestPath, static function () use ($weeklyCheckpoints, $checkpointId): void {
        $weeklyCheckpoints->show($checkpointId);
    });
    $router->post($requestPath, static function () use ($weeklyCheckpoints, $checkpointId): void {
        $weeklyCheckpoints->update($checkpointId);
    });
} elseif (preg_match('#^/reporting-periods/(\d+)/edit$#', $requestPath, $m) === 1) {
    $periodId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportingPeriods, $periodId): void {
        $reportingPeriods->edit($periodId);
    });
} elseif (preg_match('#^/reporting-periods/(\d+)$#', $requestPath, $m) === 1) {
    $periodId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportingPeriods, $periodId): void {
        $reportingPeriods->show($periodId);
    });
    $router->post($requestPath, static function () use ($reportingPeriods, $periodId): void {
        $reportingPeriods->update($periodId);
    });
}

$router->setNotFound(static function () use ($health): void {
    $health->notFound();
});

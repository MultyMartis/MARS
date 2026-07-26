<?php
declare(strict_types=1);

/**
 * Conceptual routes — DB-backed auth + reporting period CRUD + weekly checkpoints
 * + monthly report content CRUD + report blocks CRUD + report preview
 * + report finalization workflow + report snapshots.
 *
 * Dynamic /reporting-periods/{id}, /weekly-checkpoints/{id}, /monthly-reports/{id},
 * /report-blocks/{id}, and /report-snapshots/{id} matching is registered at request
 * time against the exact path (Router remains exact-match only; no overbuilt
 * pattern engine). Static /create segments and nested paths are matched before bare ids.
 *
 * @var array<string, mixed> $app
 */

use Iseo\Controllers\AuthController;
use Iseo\Controllers\DashboardController;
use Iseo\Controllers\HealthController;
use Iseo\Controllers\MonthlyReportContentController;
use Iseo\Controllers\ReportBlockController;
use Iseo\Controllers\ReportPreviewController;
use Iseo\Controllers\ReportSnapshotController;
use Iseo\Controllers\ReportingPeriodController;
use Iseo\Controllers\WeeklyCheckpointController;
use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\ReportBlockRepository;
use Iseo\Repositories\ReportPreviewRepository;
use Iseo\Repositories\ReportSnapshotRepository;
use Iseo\Repositories\ReportingPeriodRepository;
use Iseo\Repositories\WeeklyCheckpointRepository;
use Iseo\Services\AuthService;
use Iseo\Services\ConfigService;
use Iseo\Services\CsrfService;
use Iseo\Services\DatabaseService;
use Iseo\Services\MonthlyReportContentService;
use Iseo\Services\ReportBlockService;
use Iseo\Services\ReportFinalizationService;
use Iseo\Services\ReportPreviewService;
use Iseo\Services\ReportSnapshotService;
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
$monthlyRepo = new MonthlyReportContentRepository($db);
$monthlyService = new MonthlyReportContentService($monthlyRepo, $db);
$blockRepo = new ReportBlockRepository($db);
$blockService = new ReportBlockService($blockRepo, $db);
$previewRepo = new ReportPreviewRepository($db);
$previewService = new ReportPreviewService($previewRepo, $db);
$finalizationService = new ReportFinalizationService($monthlyRepo, $blockRepo, $previewService, $db);
$snapshotRepo = new ReportSnapshotRepository($db);
$snapshotService = new ReportSnapshotService($snapshotRepo, $monthlyRepo, $blockRepo, $previewService, $db);
$reportingPeriods = new ReportingPeriodController(
    $app,
    $view,
    $config,
    $auth,
    $csrf,
    $periodService,
    $checkpointService,
    $monthlyService
);
$weeklyCheckpoints = new WeeklyCheckpointController($app, $view, $config, $auth, $csrf, $checkpointService);
$monthlyReports = new MonthlyReportContentController(
    $app,
    $view,
    $config,
    $auth,
    $csrf,
    $monthlyService,
    $blockService,
    $finalizationService,
    $snapshotService
);
$reportBlocks = new ReportBlockController($app, $view, $config, $auth, $csrf, $blockService);
$reportPreview = new ReportPreviewController($app, $view, $config, $auth, $csrf, $previewService, $snapshotService);
$reportSnapshots = new ReportSnapshotController($app, $view, $config, $auth, $csrf, $snapshotService);

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
if (preg_match('#^/reporting-periods/(\d+)/monthly-report/create$#', $requestPath, $m) === 1) {
    $periodId = (int) $m[1];
    $router->get($requestPath, static function () use ($monthlyReports, $periodId): void {
        $monthlyReports->create($periodId);
    });
} elseif (preg_match('#^/reporting-periods/(\d+)/monthly-report$#', $requestPath, $m) === 1) {
    $periodId = (int) $m[1];
    $router->get($requestPath, static function () use ($monthlyReports, $periodId): void {
        $monthlyReports->showForPeriod($periodId);
    });
    $router->post($requestPath, static function () use ($monthlyReports, $periodId): void {
        $monthlyReports->store($periodId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/blocks/create$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportBlocks, $reportId): void {
        $reportBlocks->create($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/blocks$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportBlocks, $reportId): void {
        $reportBlocks->indexForMonthlyReport($reportId);
    });
    $router->post($requestPath, static function () use ($reportBlocks, $reportId): void {
        $reportBlocks->store($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/preview/print$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportPreview, $reportId): void {
        $reportPreview->print($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/preview$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportPreview, $reportId): void {
        $reportPreview->show($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/snapshot$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportSnapshots, $reportId): void {
        $reportSnapshots->monthlySnapshot($reportId);
    });
    $router->post($requestPath, static function () use ($reportSnapshots, $reportId): void {
        $reportSnapshots->createForMonthly($reportId);
    });
} elseif (preg_match('#^/report-snapshots/(\d+)$#', $requestPath, $m) === 1) {
    $snapshotId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportSnapshots, $snapshotId): void {
        $reportSnapshots->show($snapshotId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/submit-review$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->post($requestPath, static function () use ($monthlyReports, $reportId): void {
        $monthlyReports->submitReview($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/mark-reviewed$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->post($requestPath, static function () use ($monthlyReports, $reportId): void {
        $monthlyReports->markReviewed($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/finalize$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->post($requestPath, static function () use ($monthlyReports, $reportId): void {
        $monthlyReports->finalize($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/reopen$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->post($requestPath, static function () use ($monthlyReports, $reportId): void {
        $monthlyReports->reopen($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)/edit$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->get($requestPath, static function () use ($monthlyReports, $reportId): void {
        $monthlyReports->edit($reportId);
    });
} elseif (preg_match('#^/monthly-reports/(\d+)$#', $requestPath, $m) === 1) {
    $reportId = (int) $m[1];
    $router->get($requestPath, static function () use ($monthlyReports, $reportId): void {
        $monthlyReports->show($reportId);
    });
    $router->post($requestPath, static function () use ($monthlyReports, $reportId): void {
        $monthlyReports->update($reportId);
    });
} elseif (preg_match('#^/report-blocks/(\d+)/edit$#', $requestPath, $m) === 1) {
    $blockId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportBlocks, $blockId): void {
        $reportBlocks->edit($blockId);
    });
} elseif (preg_match('#^/report-blocks/(\d+)$#', $requestPath, $m) === 1) {
    $blockId = (int) $m[1];
    $router->get($requestPath, static function () use ($reportBlocks, $blockId): void {
        $reportBlocks->show($blockId);
    });
    $router->post($requestPath, static function () use ($reportBlocks, $blockId): void {
        $reportBlocks->update($blockId);
    });
} elseif (preg_match('#^/reporting-periods/(\d+)/weekly-checkpoints/create$#', $requestPath, $m) === 1) {
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

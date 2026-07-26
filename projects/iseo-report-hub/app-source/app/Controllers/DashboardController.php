<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Repositories\ReportingPeriodRepository;
use Iseo\Repositories\WeeklyCheckpointRepository;
use Iseo\Services\ReportingPeriodService;
use Iseo\Services\WeeklyCheckpointService;
use Throwable;

final class DashboardController extends BaseController
{
    public function index(): void
    {
        if (!$this->auth->isAuthenticated() || !$this->auth->hasInternalRole()) {
            $this->redirect('/login');
            return;
        }

        $user = $this->auth->currentUser();
        $dbConfigured = (bool) $this->config->get('database.configured', false);

        $periodCount = null;
        $checkpointCount = null;
        $reportingDetail = 'Internal CRUD ready — list / detail / create / edit / archive-by-status.';
        $checkpointDetail = 'Period-scoped CRUD ready — list / detail / create / edit / skip-or-archive-by-status.';
        if ($dbConfigured) {
            try {
                /** @var \Iseo\Services\DatabaseService $db */
                $db = $this->app['db'];
                $periodService = new ReportingPeriodService(new ReportingPeriodRepository($db), $db);
                $periodCount = $periodService->countPeriods();
                $reportingDetail = 'Internal CRUD ready. Periods in DB: ' . $periodCount . '.';
                $checkpointService = new WeeklyCheckpointService(new WeeklyCheckpointRepository($db), $db);
                $checkpointCount = $checkpointService->countCheckpoints();
                $checkpointDetail = 'Period-scoped CRUD ready. Checkpoints in DB: ' . $checkpointCount . '.';
            } catch (Throwable) {
                $reportingDetail = 'CRUD code ready; period count unavailable.';
                $checkpointDetail = 'CRUD code ready; checkpoint count unavailable.';
            }
        }

        $this->render('dashboard', [
            'pageTitle' => 'Dashboard',
            'user' => $user,
            'periodCount' => $periodCount,
            'checkpointCount' => $checkpointCount,
            'cards' => [
                [
                    'title' => 'Auth',
                    'status' => 'ready',
                    'detail' => 'DB-backed login active for internal roles.',
                ],
                [
                    'title' => 'Database',
                    'status' => $dbConfigured ? 'ready' : 'pending',
                    'detail' => $dbConfigured
                        ? 'Configured via runtime .env.local (credentials not shown).'
                        : 'Database not configured.',
                ],
                [
                    'title' => 'Runtime',
                    'status' => 'ready',
                    'detail' => 'Local Laragon runtime at iseo-report-hub.test.',
                ],
                [
                    'title' => 'Reporting CRUD',
                    'status' => 'ready',
                    'detail' => $reportingDetail,
                ],
                [
                    'title' => 'Weekly checkpoints',
                    'status' => 'ready',
                    'detail' => $checkpointDetail,
                ],
            ],
        ]);
    }
}

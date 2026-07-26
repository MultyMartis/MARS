<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Repositories\ReportingPeriodRepository;
use Iseo\Services\ReportingPeriodService;
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
        $reportingDetail = 'Internal CRUD ready — list / detail / create / edit / archive-by-status.';
        if ($dbConfigured) {
            try {
                /** @var \Iseo\Services\DatabaseService $db */
                $db = $this->app['db'];
                $service = new ReportingPeriodService(new ReportingPeriodRepository($db), $db);
                $periodCount = $service->countPeriods();
                $reportingDetail = 'Internal CRUD ready. Periods in DB: ' . $periodCount . '.';
            } catch (Throwable) {
                $reportingDetail = 'CRUD code ready; period count unavailable.';
            }
        }

        $this->render('dashboard', [
            'pageTitle' => 'Dashboard',
            'user' => $user,
            'periodCount' => $periodCount,
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
            ],
        ]);
    }
}

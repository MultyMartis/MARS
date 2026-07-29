<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\ReportBlockRepository;
use Iseo\Repositories\ReportingPeriodRepository;
use Iseo\Repositories\WeeklyCheckpointRepository;
use Iseo\Services\MonthlyReportContentService;
use Iseo\Services\ReportBlockService;
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
        $monthlyCount = null;
        $blockCount = null;
        $reportingDetail = 'Внутренние отчеты готовы — список / карточка / создание / правка.';
        $checkpointDetail = 'Еженедельные заметки готовы — через отчетный период.';
        $monthlyDetail = 'Месячные отчеты готовы — через отчетный период.';
        $blockDetail = 'Блоки отчета готовы — через месячный отчет.';
        if ($dbConfigured) {
            try {
                /** @var \Iseo\Services\DatabaseService $db */
                $db = $this->app['db'];
                $periodService = new ReportingPeriodService(new ReportingPeriodRepository($db), $db);
                $periodCount = $periodService->countPeriods();
                $reportingDetail = 'Отчетные периоды в базе: ' . $periodCount . '.';
                $checkpointService = new WeeklyCheckpointService(new WeeklyCheckpointRepository($db), $db);
                $checkpointCount = $checkpointService->countCheckpoints();
                $checkpointDetail = 'Еженедельных заметок в базе: ' . $checkpointCount . '.';
                $monthlyService = new MonthlyReportContentService(new MonthlyReportContentRepository($db), $db);
                $monthlyCount = $monthlyService->countReports();
                $monthlyDetail = 'Месячных отчетов в базе: ' . $monthlyCount . '.';
                $blockService = new ReportBlockService(new ReportBlockRepository($db), $db);
                $blockCount = $blockService->countBlocks();
                $blockDetail = 'Блоков отчета в базе: ' . $blockCount . '.';
            } catch (Throwable) {
                $reportingDetail = 'Модуль отчетов готов; счётчик периодов недоступен.';
                $checkpointDetail = 'Модуль заметок готов; счётчик недоступен.';
                $monthlyDetail = 'Модуль месячных отчетов готов; счётчик недоступен.';
                $blockDetail = 'Модуль блоков готов; счётчик недоступен.';
            }
        }

        $this->render('dashboard', [
            'pageTitle' => 'Главная',
            'user' => $user,
            'periodCount' => $periodCount,
            'checkpointCount' => $checkpointCount,
            'monthlyCount' => $monthlyCount,
            'blockCount' => $blockCount,
            // Local fixture manager shortcuts (stable smoke IDs).
            'quickMonthlyId' => 1,
            'quickSnapshotId' => 1,
            'quickExportId' => 4,
            'cards' => [
                [
                    'title' => 'Вход',
                    'status' => 'ready',
                    'status_label' => 'Готово',
                    'detail' => 'Вход выполнен. Сессия сохраняется в базе.',
                ],
                [
                    'title' => 'База данных',
                    'status' => $dbConfigured ? 'ready' : 'pending',
                    'status_label' => $dbConfigured ? 'Готово' : 'В работе',
                    'detail' => $dbConfigured
                        ? 'Подключена через локальный .env.local (учётные данные не показываются).'
                        : 'База данных не настроена.',
                ],
                [
                    'title' => 'Локальный запуск',
                    'status' => 'ready',
                    'status_label' => 'Готово',
                    'detail' => 'Локальный запуск: iseo-report-hub.test.',
                ],
                [
                    'title' => 'Отчеты',
                    'status' => 'ready',
                    'status_label' => 'Готово',
                    'detail' => $reportingDetail,
                ],
                [
                    'title' => 'Еженедельные заметки',
                    'status' => 'ready',
                    'status_label' => 'Готово',
                    'detail' => $checkpointDetail,
                ],
                [
                    'title' => 'Месячные отчеты',
                    'status' => 'ready',
                    'status_label' => 'Готово',
                    'detail' => $monthlyDetail,
                ],
                [
                    'title' => 'Блоки отчета',
                    'status' => 'ready',
                    'status_label' => 'Готово',
                    'detail' => $blockDetail,
                ],
            ],
        ]);
    }
}

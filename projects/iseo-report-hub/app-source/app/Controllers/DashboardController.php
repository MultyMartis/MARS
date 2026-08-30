<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\ReportBlockRepository;
use Iseo\Repositories\ReportExportShareRepository;
use Iseo\Repositories\ReportingPeriodRepository;
use Iseo\Repositories\WeeklyCheckpointRepository;
use Iseo\Services\MonthlyReportContentService;
use Iseo\Services\ReportBlockService;
use Iseo\Services\ReportingPeriodService;
use Iseo\Services\WeeklyCheckpointService;
use Iseo\Support\UiLabels;
use PDO;
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
        /** @var int|null null = share state not checked / unavailable */
        $activeShareCount = null;
        $reportingDetail = 'Внутренние отчеты готовы — список / карточка / создание / правка.';
        $checkpointDetail = 'Еженедельные заметки готовы — через отчетный период.';
        $monthlyDetail = 'Месячные отчеты готовы — через отчетный период.';
        $blockDetail = 'Блоки отчета готовы — через месячный отчет.';

        $scenario = [
            'available' => false,
            'client_name' => '',
            'project_name' => '',
            'period_count' => 0,
            'report_count' => 0,
            'latest_monthly_id' => null,
            'has_ready_pdf' => false,
            'has_active_share' => false,
            'export_href' => null,
            'shares_href' => null,
        ];

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
                $shareCounts = (new ReportExportShareRepository($db))->countByStatus();
                $activeShareCount = (int) ($shareCounts['active'] ?? 0);
                $scenario = $this->loadPrimaryScenario($db->connect());
            } catch (Throwable) {
                $reportingDetail = 'Модуль отчетов готов; счётчик периодов недоступен.';
                $checkpointDetail = 'Модуль заметок готов; счётчик недоступен.';
                $monthlyDetail = 'Модуль месячных отчетов готов; счётчик недоступен.';
                $blockDetail = 'Модуль блоков готов; счётчик недоступен.';
                $activeShareCount = null;
            }
        }

        $this->render('dashboard', [
            'pageTitle' => 'Обзор отчетов',
            'user' => $user,
            'periodCount' => $periodCount,
            'checkpointCount' => $checkpointCount,
            'monthlyCount' => $monthlyCount,
            'blockCount' => $blockCount,
            'activeShareCount' => $activeShareCount,
            'scenario' => $scenario,
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

    /**
     * Primary visible scenario for local demo / manager handoff.
     *
     * @return array{
     *   available:bool,
     *   client_name:string,
     *   project_name:string,
     *   period_count:int,
     *   report_count:int,
     *   latest_monthly_id:?int,
     *   has_ready_pdf:bool,
     *   has_active_share:bool,
     *   export_href:?string,
     *   shares_href:?string
     * }
     */
    private function loadPrimaryScenario(PDO $pdo): array
    {
        $empty = [
            'available' => false,
            'client_name' => '',
            'project_name' => '',
            'period_count' => 0,
            'report_count' => 0,
            'latest_monthly_id' => null,
            'has_ready_pdf' => false,
            'has_active_share' => false,
            'export_href' => null,
            'shares_href' => null,
        ];

        $stmt = $pdo->query(
            'SELECT c.id AS client_id, c.name AS client_name, p.id AS project_id, p.name AS project_name
             FROM clients c
             INNER JOIN projects p ON p.client_id = c.id
             ORDER BY c.id DESC
             LIMIT 1'
        );
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
        if (!is_array($row)) {
            return $empty;
        }

        $projectId = (int) ($row['project_id'] ?? 0);
        if ($projectId <= 0) {
            return $empty;
        }

        $st = $pdo->prepare('SELECT COUNT(*) FROM reporting_periods WHERE project_id = :p');
        $st->execute([':p' => $projectId]);
        $periodCount = (int) $st->fetchColumn();

        $st = $pdo->prepare(
            'SELECT COUNT(*) FROM monthly_report_contents mrc
             INNER JOIN reporting_periods rp ON rp.id = mrc.reporting_period_id
             WHERE rp.project_id = :p'
        );
        $st->execute([':p' => $projectId]);
        $reportCount = (int) $st->fetchColumn();

        $st = $pdo->prepare(
            'SELECT mrc.id
             FROM monthly_report_contents mrc
             INNER JOIN reporting_periods rp ON rp.id = mrc.reporting_period_id
             WHERE rp.project_id = :p
             ORDER BY mrc.id DESC
             LIMIT 1'
        );
        $st->execute([':p' => $projectId]);
        $latestMonthlyId = (int) $st->fetchColumn();
        if ($latestMonthlyId <= 0) {
            $latestMonthlyId = null;
        }

        $hasReadyPdf = false;
        $hasActiveShare = false;
        $exportHref = null;
        $sharesHref = null;

        if ($latestMonthlyId !== null) {
            $st = $pdo->prepare(
                "SELECT id FROM report_exports
                 WHERE monthly_report_content_id = :m AND format = 'pdf' AND status = 'ready'
                 ORDER BY id DESC LIMIT 1"
            );
            $st->execute([':m' => $latestMonthlyId]);
            $exportId = (int) $st->fetchColumn();
            if ($exportId > 0) {
                $hasReadyPdf = true;
                $st = $pdo->prepare('SELECT report_snapshot_id FROM report_exports WHERE id = :id');
                $st->execute([':id' => $exportId]);
                $snapshotId = (int) $st->fetchColumn();
                if ($snapshotId > 0) {
                    $exportHref = '/report-snapshots/' . $snapshotId . '/exports';
                }
                $sharesHref = '/report-exports/' . $exportId . '/shares';
                $st = $pdo->prepare(
                    "SELECT COUNT(*) FROM report_export_shares WHERE report_export_id = :e AND status = 'active'"
                );
                $st->execute([':e' => $exportId]);
                $hasActiveShare = (int) $st->fetchColumn() > 0;
            }
        }

        return [
            'available' => true,
            'client_name' => UiLabels::decodeLiteralUnicodeEscapes(trim((string) ($row['client_name'] ?? ''))),
            'project_name' => UiLabels::decodeLiteralUnicodeEscapes(trim((string) ($row['project_name'] ?? ''))),
            'period_count' => $periodCount,
            'report_count' => $reportCount,
            'latest_monthly_id' => $latestMonthlyId,
            'has_ready_pdf' => $hasReadyPdf,
            'has_active_share' => $hasActiveShare,
            'export_href' => $exportHref,
            'shares_href' => $sharesHref,
        ];
    }
}

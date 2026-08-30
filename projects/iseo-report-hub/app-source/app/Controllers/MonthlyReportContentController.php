<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\MonthlyReportContentService;
use Iseo\Services\ReportBlockService;
use Iseo\Services\ReportFinalizationService;
use Iseo\Services\ReportSnapshotService;
use Iseo\Repositories\MonthlyReportWorkEntryRepository;
use Iseo\Repositories\ReportExportRepository;
use Iseo\Repositories\ReportExportShareRepository;
use Iseo\Repositories\SeoWorkCategoryRepository;
use Iseo\Repositories\SeoWorkItemRepository;
use Iseo\Support\Response;
use Throwable;

final class MonthlyReportContentController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private MonthlyReportContentService $monthlyReports,
        private ReportBlockService $reportBlocks,
        private ReportFinalizationService $finalization,
        private ReportSnapshotService $snapshots,
        private ?MonthlyReportWorkEntryRepository $workEntries = null,
        private ?SeoWorkCategoryRepository $workCategories = null,
        private ?SeoWorkItemRepository $workItems = null
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function showForPeriod(int $periodId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->monthlyReports->canList($user)) {
            $this->denyAccess();
            return;
        }

        $period = $this->monthlyReports->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        $report = $this->monthlyReports->getByPeriodId($periodId);
        if ($report === null) {
            if ($this->monthlyReports->canCreate($user)
                && $this->monthlyReports->canMutateAgainstParent($user, $period)) {
                $this->redirect('/reporting-periods/' . $periodId . '/monthly-report/create');
                return;
            }
            Response::html(
                '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>No monthly report</title></head>'
                . '<body><h1>No monthly report content</h1>'
                . '<p>No monthly report content exists for this period.</p>'
                . '<p><a href="' . e(url_path('/reporting-periods/' . $periodId)) . '">Back to period</a></p>'
                . '</body></html>',
                404
            );
            return;
        }

        $this->renderShow($user, $report, $period);
    }

    public function show(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->monthlyReports->canList($user)) {
            $this->denyAccess();
            return;
        }

        $report = $this->monthlyReports->getById($id);
        if ($report === null) {
            $this->notFoundReport();
            return;
        }

        $period = $this->monthlyReports->getPeriod((int) $report['reporting_period_id']);
        $this->renderShow($user, $report, $period);
    }

    public function create(int $periodId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $period = $this->monthlyReports->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canCreate($user)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        $existing = $this->monthlyReports->getByPeriodId($periodId);
        if ($existing !== null) {
            flash_set('warn', 'A monthly report content row already exists for this reporting period.');
            $this->redirect('/monthly-reports/' . (int) $existing['id']);
            return;
        }

        $available = $this->monthlyReports->selectableWeeklyCheckpoints($periodId);

        $this->render('monthly-reports/create', [
            'pageTitle' => 'Создание месячного отчета',
            'mode' => 'create',
            'period' => $period,
            'report' => null,
            'old' => $this->defaultCreateOld($period, $available),
            'errors' => [],
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, null),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => [
                'reporting_period_id' => true,
                'content' => false,
                'source_ids' => false,
            ],
        ]);
    }

    public function store(int $periodId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $period = $this->monthlyReports->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canCreate($user)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/reporting-periods/' . $periodId . '/monthly-report/create');
            return;
        }

        $existing = $this->monthlyReports->getByPeriodId($periodId);
        if ($existing !== null) {
            flash_set('warn', 'A monthly report content row already exists for this reporting period.');
            $this->redirect('/monthly-reports/' . (int) $existing['id']);
            return;
        }

        $input = $this->readInput();
        $result = $this->monthlyReports->create($user, $period, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Monthly report content created.');
            if (!empty($result['notice'])) {
                flash_set('warn', (string) $result['notice']);
            }
            $this->redirect('/monthly-reports/' . (int) $result['id']);
            return;
        }

        $available = $this->monthlyReports->selectableWeeklyCheckpoints($periodId);
        $this->render('monthly-reports/create', [
            'pageTitle' => 'Создание месячного отчета',
            'mode' => 'create',
            'period' => $period,
            'report' => null,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, null),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => [
                'reporting_period_id' => true,
                'content' => false,
                'source_ids' => false,
            ],
        ], 422);
    }

    public function edit(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $report = $this->monthlyReports->getById($id);
        if ($report === null) {
            $this->notFoundReport();
            return;
        }

        $period = $this->monthlyReports->getPeriod((int) $report['reporting_period_id']);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canEdit($user, $report)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        $parentFinalized = $this->finalization->isMonthlyFinalizedLocked($report);
        $available = $this->monthlyReports->selectableWeeklyCheckpoints((int) $period['id']);

        $this->render('monthly-reports/edit', [
            'pageTitle' => 'Редактирование месячного отчета',
            'mode' => 'edit',
            'period' => $period,
            'report' => $report,
            'old' => $this->reportToOld($report),
            'errors' => [],
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, (string) $report['status']),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => $this->locksForReport($report, $user),
            'parentFinalized' => $parentFinalized,
            'formLocked' => $parentFinalized,
        ]);
    }

    public function update(int $id): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $report = $this->monthlyReports->getById($id);
        if ($report === null) {
            $this->notFoundReport();
            return;
        }

        $period = $this->monthlyReports->getPeriod((int) $report['reporting_period_id']);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canEdit($user, $report)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/monthly-reports/' . $id . '/edit');
            return;
        }

        if ($this->finalization->isMonthlyFinalizedLocked($report)) {
            flash_set('warn', 'Monthly report is finalized. Reopen before editing content.');
            $this->redirect('/monthly-reports/' . $id);
            return;
        }

        $input = $this->readInput();
        $result = $this->monthlyReports->update($user, $report, $period, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Monthly report content updated.');
            if (!empty($result['notice'])) {
                flash_set('warn', (string) $result['notice']);
            }
            $this->redirect('/monthly-reports/' . $id);
            return;
        }

        $available = $this->monthlyReports->selectableWeeklyCheckpoints((int) $period['id']);
        $this->render('monthly-reports/edit', [
            'pageTitle' => 'Редактирование месячного отчета',
            'mode' => 'edit',
            'period' => $period,
            'report' => $report,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, (string) $report['status']),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => $this->locksForReport($report, $user),
            'parentFinalized' => false,
            'formLocked' => false,
        ], 422);
    }

    public function submitReview(int $id): void
    {
        $this->runFinalizationAction($id, 'submitForReview');
    }

    public function markReviewed(int $id): void
    {
        $this->runFinalizationAction($id, 'markReviewed');
    }

    public function finalize(int $id): void
    {
        $this->runFinalizationAction($id, 'finalize');
    }

    public function reopen(int $id): void
    {
        $this->runFinalizationAction($id, 'reopen');
    }

    private function runFinalizationAction(int $id, string $method): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->monthlyReports->canList($user)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/monthly-reports/' . $id);
            return;
        }

        $result = $this->finalization->{$method}($id, $user);
        if (!empty($result['ok'])) {
            flash_set('info', (string) ($result['message'] ?? 'Action completed.'));
        } else {
            flash_set('warn', (string) ($result['message'] ?? 'Action failed.'));
        }
        $this->redirect('/monthly-reports/' . $id);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $report
     * @param array<string, mixed>|null $period
     */
    private function renderShow(array $user, array $report, ?array $period): void
    {
        $periodId = (int) $report['reporting_period_id'];
        $available = $this->monthlyReports->selectableWeeklyCheckpoints($periodId);
        $sourceIds = $this->monthlyReports->decodeSourceIds($report['source_weekly_checkpoint_ids'] ?? null);
        $sourceRows = $this->monthlyReports->resolveSourceCheckpointRows($sourceIds, $available);

        $parentFinalized = $this->finalization->isMonthlyFinalizedLocked($report);
        $canEdit = $period !== null
            && !$parentFinalized
            && $this->monthlyReports->canEdit($user, $report)
            && $this->monthlyReports->canMutateAgainstParent($user, $period);

        $reportBlocks = [];
        $canCreateBlock = false;
        try {
            $reportBlocks = $this->reportBlocks->listForMonthlyReport((int) $report['id']);
            $canCreateBlock = !$parentFinalized
                && $this->reportBlocks->canCreate($user)
                && $this->reportBlocks->canMutateAgainstParent($user, [
                    'id' => (int) $report['id'],
                    'status' => (string) $report['status'],
                    'reporting_period_id' => (int) $report['reporting_period_id'],
                ]);
            foreach ($reportBlocks as &$blockRow) {
                $blockRow['_can_edit'] = !$parentFinalized
                    && $this->reportBlocks->canEdit($user, $blockRow)
                    && $this->reportBlocks->canMutateAgainstParent($user, [
                        'id' => (int) $report['id'],
                        'status' => (string) $report['status'],
                        'reporting_period_id' => (int) $report['reporting_period_id'],
                    ]);
            }
            unset($blockRow);
        } catch (\Throwable) {
            $reportBlocks = [];
            $canCreateBlock = false;
        }

        $readiness = [
            'ok' => false,
            'ready' => false,
            'gates' => [],
            'failed_gates' => [],
            'actions' => [],
        ];
        try {
            $readiness = $this->finalization->getReadiness((int) $report['id'], $user);
        } catch (\Throwable) {
            // Show page even if readiness computation fails.
        }

        $activeSnapshot = null;
        $canCreateSnapshot = false;
        try {
            $snapState = $this->snapshots->getActiveForMonthly((int) $report['id'], $user);
            if (!empty($snapState['ok'])) {
                $activeSnapshot = $snapState['snapshot'] ?? null;
                $canCreateSnapshot = !empty($snapState['can_create']);
            }
        } catch (\Throwable) {
            $activeSnapshot = null;
            $canCreateSnapshot = false;
        }

        $workEntries = [];
        $workEntryCounters = [
            'total' => 0,
            'status_done' => 0,
            'period_planned_next' => 0,
            'period_risk_note' => 0,
            'visibility_client_facing' => 0,
            'visibility_client_safe' => 0,
            'visibility_internal' => 0,
        ];
        $catalogueSummary = [
            'categories_active' => 0,
            'items_active' => 0,
            'source' => 'nikita_catalogue_v1',
            'available' => false,
        ];
        try {
            if ($this->workEntries !== null) {
                $workEntries = $this->workEntries->listByMonthlyReportId((int) $report['id']);
                $workEntryCounters['total'] = count($workEntries);
                foreach ($workEntries as $entry) {
                    $status = (string) ($entry['status'] ?? '');
                    $role = (string) ($entry['period_role'] ?? '');
                    $visibility = (string) ($entry['client_visibility'] ?? '');
                    if ($status === 'done') {
                        $workEntryCounters['status_done']++;
                    }
                    if ($role === 'planned_next') {
                        $workEntryCounters['period_planned_next']++;
                    }
                    if ($role === 'risk' || $role === 'note') {
                        $workEntryCounters['period_risk_note']++;
                    }
                    if ($visibility === 'client_facing') {
                        $workEntryCounters['visibility_client_facing']++;
                    } elseif ($visibility === 'client_safe') {
                        $workEntryCounters['visibility_client_safe']++;
                    } elseif ($visibility === 'internal') {
                        $workEntryCounters['visibility_internal']++;
                    }
                }
            }
            if ($this->workCategories !== null && $this->workItems !== null) {
                $catalogueSummary['categories_active'] = $this->workCategories->countActive();
                $catalogueSummary['items_active'] = $this->workItems->countActive();
                $catalogueSummary['available'] = true;
            }
        } catch (\Throwable) {
            $workEntries = [];
            $catalogueSummary['available'] = false;
        }

        // Display-only delivery indicators for manager summary (no mutation).
        $deliveryReadiness = [
            'snapshot_exists' => is_array($activeSnapshot),
            'pdf_ready' => false,
            'pdf_export_id' => null,
            'active_share' => false,
            'share_export_id' => null,
        ];
        try {
            if (is_array($activeSnapshot)) {
                $snapshotId = (int) ($activeSnapshot['id'] ?? 0);
                if ($snapshotId > 0 && isset($this->app['db'])) {
                    /** @var \Iseo\Services\DatabaseService $db */
                    $db = $this->app['db'];
                    $exportRepo = new ReportExportRepository($db);
                    $styledPdf = $exportRepo->findReadyStyledVersionForSnapshotFormat($snapshotId, 'pdf');
                    $pdfExport = is_array($styledPdf)
                        ? $styledPdf
                        : $exportRepo->findReadyBySnapshotAndFormat($snapshotId, 'pdf');
                    if (is_array($pdfExport) && (string) ($pdfExport['status'] ?? '') === 'ready') {
                        $exportId = (int) ($pdfExport['id'] ?? 0);
                        $deliveryReadiness['pdf_ready'] = $exportId > 0;
                        $deliveryReadiness['pdf_export_id'] = $exportId > 0 ? $exportId : null;
                        if ($exportId > 0) {
                            $shareRepo = new ReportExportShareRepository($db);
                            $activeCount = $shareRepo->countActiveForExport($exportId);
                            $deliveryReadiness['active_share'] = $activeCount > 0;
                            $deliveryReadiness['share_export_id'] = $exportId;
                        }
                    }
                }
            }
        } catch (Throwable) {
            // Keep defaults; page remains usable without delivery indicators.
        }

        $this->render('monthly-reports/show', [
            'pageTitle' => 'Месячный отчет — ' . (string) ($report['period_key'] ?? $report['id']),
            'report' => $report,
            'period' => $period,
            'sourceCheckpoints' => $sourceRows,
            'canEdit' => $canEdit,
            'reportBlocks' => $reportBlocks,
            'canCreateBlock' => $canCreateBlock,
            'parentFinalized' => $parentFinalized,
            'readiness' => $readiness,
            'activeSnapshot' => $activeSnapshot,
            'canCreateSnapshot' => $canCreateSnapshot,
            'workEntries' => $workEntries,
            'workEntryCounters' => $workEntryCounters,
            'catalogueSummary' => $catalogueSummary,
            'canCreateWorkEntry' => $this->workEntries !== null
                && $this->workEntriesCanMutate($user, $report),
            'canEditWorkEntries' => $this->workEntries !== null
                && $this->workEntriesCanMutate($user, $report),
            'isSpecialistFlow' => $this->auth->isSpecialistFlow($user),
            'showAdminControls' => $this->auth->isPrivilegedEditor($user),
            'deliveryReadiness' => $deliveryReadiness,
        ]);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $report
     */
    private function workEntriesCanMutate(array $user, array $report): bool
    {
        if ($this->workEntries === null) {
            return false;
        }
        // Reuse same finalized rule as work-entry service (inline to avoid wiring service here).
        $roles = $user['roles'] ?? [];
        $isPrivileged = in_array('admin_owner', $roles, true)
            || in_array('seo_lead_reviewer', $roles, true);
        if ($isPrivileged) {
            return true;
        }
        if (!in_array('seo_specialist', $roles, true)) {
            return false;
        }

        return (string) ($report['status'] ?? '') !== 'finalized';
    }

    /**
     * @return array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null
     */
    private function requireInternalUser(): ?array
    {
        if (!$this->auth->isAuthenticated() || !$this->auth->hasInternalRole()) {
            $this->redirect('/login');
            return null;
        }

        $user = $this->auth->currentUser();
        if ($user === null) {
            $this->redirect('/login');
            return null;
        }

        return $user;
    }

    private function validateCsrf(): bool
    {
        $token = $_POST['_csrf'] ?? null;
        return $this->csrf->validate(is_string($token) ? $token : null);
    }

    /**
     * @return array<string, mixed>
     */
    private function readInput(): array
    {
        $sourceRaw = $_POST['source_weekly_checkpoint_ids'] ?? [];
        if (!is_array($sourceRaw)) {
            $sourceRaw = [];
        }

        return [
            'status' => $_POST['status'] ?? 'draft',
            'title' => $_POST['title'] ?? '',
            'executive_summary' => $_POST['executive_summary'] ?? '',
            'work_completed' => $_POST['work_completed'] ?? '',
            'results_summary' => $_POST['results_summary'] ?? '',
            'key_findings' => $_POST['key_findings'] ?? '',
            'risks_and_blockers' => $_POST['risks_and_blockers'] ?? '',
            'next_month_plan' => $_POST['next_month_plan'] ?? '',
            'client_notes' => $_POST['client_notes'] ?? '',
            'internal_notes' => $_POST['internal_notes'] ?? '',
            'source_weekly_checkpoint_ids' => $sourceRaw,
            'owner_user_id' => $_POST['owner_user_id'] ?? '',
            'reviewer_user_id' => $_POST['reviewer_user_id'] ?? '',
        ];
    }

    /**
     * @param array<string, mixed> $period
     * @param list<array<string, mixed>> $available
     * @return array<string, mixed>
     */
    private function defaultCreateOld(array $period, array $available): array
    {
        $defaultIds = [];
        foreach ($available as $row) {
            $defaultIds[] = (string) $row['id'];
        }

        return [
            'status' => 'draft',
            'title' => 'Monthly report — ' . (string) $period['period_key'] . ' — LOCAL_FIXTURE_ONLY',
            'executive_summary' => '',
            'work_completed' => '',
            'results_summary' => '',
            'key_findings' => '',
            'risks_and_blockers' => '',
            'next_month_plan' => '',
            'client_notes' => '',
            'internal_notes' => '',
            'source_weekly_checkpoint_ids' => $defaultIds,
            'owner_user_id' => '',
            'reviewer_user_id' => '',
        ];
    }

    /**
     * @param array<string, mixed> $report
     * @return array<string, mixed>
     */
    private function reportToOld(array $report): array
    {
        $ids = $this->monthlyReports->decodeSourceIds($report['source_weekly_checkpoint_ids'] ?? null);
        $idStrings = [];
        foreach ($ids as $id) {
            $idStrings[] = (string) $id;
        }

        return [
            'status' => (string) $report['status'],
            'title' => (string) ($report['title'] ?? ''),
            'executive_summary' => (string) ($report['executive_summary'] ?? ''),
            'work_completed' => (string) ($report['work_completed'] ?? ''),
            'results_summary' => (string) ($report['results_summary'] ?? ''),
            'key_findings' => (string) ($report['key_findings'] ?? ''),
            'risks_and_blockers' => (string) ($report['risks_and_blockers'] ?? ''),
            'next_month_plan' => (string) ($report['next_month_plan'] ?? ''),
            'client_notes' => (string) ($report['client_notes'] ?? ''),
            'internal_notes' => (string) ($report['internal_notes'] ?? ''),
            'source_weekly_checkpoint_ids' => $idStrings,
            'owner_user_id' => $report['owner_user_id'] !== null ? (string) $report['owner_user_id'] : '',
            'reviewer_user_id' => $report['reviewer_user_id'] !== null ? (string) $report['reviewer_user_id'] : '',
        ];
    }

    /**
     * @param array<string, mixed> $report
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array{reporting_period_id:bool,content:bool,source_ids:bool}
     */
    private function locksForReport(array $report, array $user): array
    {
        $status = (string) $report['status'];
        $lockContent = $status === 'finalized';

        return [
            'reporting_period_id' => true,
            'content' => $lockContent,
            'source_ids' => $lockContent,
        ];
    }

    private function denyAccess(): void
    {
        $this->renderAccessDenied('У вас нет прав на это действие с месячным отчетом.');
    }

    private function notFoundPeriod(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Reporting period not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }

    private function notFoundReport(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Monthly report content not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }
}

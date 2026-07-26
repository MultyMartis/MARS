<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\ReportBlockService;
use Iseo\Support\Response;

final class ReportBlockController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private ReportBlockService $blocks
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function indexForMonthlyReport(int $monthlyReportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->blocks->canList($user)) {
            $this->denyAccess();
            return;
        }

        $monthly = $this->blocks->getMonthlyReport($monthlyReportId);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        $rows = $this->blocks->listForMonthlyReport($monthlyReportId);
        $canCreate = $this->blocks->canCreate($user)
            && $this->blocks->canMutateAgainstParent($user, $monthly);

        foreach ($rows as &$row) {
            $row['_can_edit'] = $this->blocks->canEdit($user, $row)
                && $this->blocks->canMutateAgainstParent($user, $monthly);
        }
        unset($row);

        $this->render('report-blocks/index', [
            'pageTitle' => 'Report blocks — ' . (string) ($monthly['period_key'] ?? $monthlyReportId),
            'monthly' => $monthly,
            'blocks' => $rows,
            'canCreate' => $canCreate,
            'parentFinalized' => (string) ($monthly['status'] ?? '') === 'finalized',
        ]);
    }

    public function create(int $monthlyReportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $monthly = $this->blocks->getMonthlyReport($monthlyReportId);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if ((string) ($monthly['status'] ?? '') === 'finalized') {
            flash_set('warn', 'Parent monthly report is finalized. Reopen before creating blocks.');
            $this->redirect('/monthly-reports/' . $monthlyReportId . '/blocks');
            return;
        }

        if (!$this->blocks->canCreate($user)
            || !$this->blocks->canMutateAgainstParent($user, $monthly)) {
            $this->denyAccess();
            return;
        }

        $periodId = (int) $monthly['reporting_period_id'];
        $available = $this->blocks->selectableWeeklyCheckpoints($periodId);

        $this->render('report-blocks/create', [
            'pageTitle' => 'Create report block',
            'mode' => 'create',
            'monthly' => $monthly,
            'block' => null,
            'old' => $this->defaultCreateOld($monthly, $available),
            'errors' => [],
            'users' => $this->blocks->selectableInternalUsers(),
            'statuses' => $this->blocks->allowedStatusesForForm($user, null),
            'blockTypes' => ReportBlockService::BLOCK_TYPES,
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->blocks->canAssignOwnerReviewer($user),
            'locks' => [
                'monthly_report_content_id' => true,
                'block_key' => false,
                'block_type' => false,
                'sort_order' => false,
                'content' => false,
                'source_ids' => false,
            ],
        ]);
    }

    public function store(int $monthlyReportId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $monthly = $this->blocks->getMonthlyReport($monthlyReportId);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if ((string) ($monthly['status'] ?? '') === 'finalized') {
            flash_set('warn', 'Parent monthly report is finalized. Reopen before creating blocks.');
            $this->redirect('/monthly-reports/' . $monthlyReportId . '/blocks');
            return;
        }

        if (!$this->blocks->canCreate($user)
            || !$this->blocks->canMutateAgainstParent($user, $monthly)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/monthly-reports/' . $monthlyReportId . '/blocks/create');
            return;
        }

        $input = $this->readInput();
        $result = $this->blocks->create($user, $monthly, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Report block created.');
            if (!empty($result['notice'])) {
                flash_set('warn', (string) $result['notice']);
            }
            $this->redirect('/report-blocks/' . (int) $result['id']);
            return;
        }

        $periodId = (int) $monthly['reporting_period_id'];
        $available = $this->blocks->selectableWeeklyCheckpoints($periodId);
        $this->render('report-blocks/create', [
            'pageTitle' => 'Create report block',
            'mode' => 'create',
            'monthly' => $monthly,
            'block' => null,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->blocks->selectableInternalUsers(),
            'statuses' => $this->blocks->allowedStatusesForForm($user, null),
            'blockTypes' => ReportBlockService::BLOCK_TYPES,
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->blocks->canAssignOwnerReviewer($user),
            'locks' => [
                'monthly_report_content_id' => true,
                'block_key' => false,
                'block_type' => false,
                'sort_order' => false,
                'content' => false,
                'source_ids' => false,
            ],
        ], 422);
    }

    public function show(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->blocks->canList($user)) {
            $this->denyAccess();
            return;
        }

        $block = $this->blocks->getById($id);
        if ($block === null) {
            $this->notFoundBlock();
            return;
        }

        $monthly = $this->blocks->getMonthlyReport((int) $block['monthly_report_content_id']);
        $periodId = (int) $block['reporting_period_id'];
        $available = $this->blocks->selectableWeeklyCheckpoints($periodId);
        $sourceIds = $this->blocks->decodeSourceIds($block['source_weekly_checkpoint_ids'] ?? null);
        $sourceRows = $this->blocks->resolveSourceCheckpointRows($sourceIds, $available);

        $canEdit = $monthly !== null
            && $this->blocks->canEdit($user, $block)
            && $this->blocks->canMutateAgainstParent($user, $monthly);

        $this->render('report-blocks/show', [
            'pageTitle' => 'Report block — ' . (string) $block['block_key'],
            'block' => $block,
            'monthly' => $monthly,
            'sourceCheckpoints' => $sourceRows,
            'canEdit' => $canEdit,
            'parentFinalized' => $monthly !== null && (string) ($monthly['status'] ?? '') === 'finalized',
        ]);
    }

    public function edit(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $block = $this->blocks->getById($id);
        if ($block === null) {
            $this->notFoundBlock();
            return;
        }

        $monthly = $this->blocks->getMonthlyReport((int) $block['monthly_report_content_id']);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if ((string) ($monthly['status'] ?? '') === 'finalized') {
            flash_set('warn', 'Parent monthly report is finalized. Reopen before editing blocks.');
            $this->redirect('/report-blocks/' . $id);
            return;
        }

        if (!$this->blocks->canEdit($user, $block)
            || !$this->blocks->canMutateAgainstParent($user, $monthly)) {
            $this->denyAccess();
            return;
        }

        $periodId = (int) $monthly['reporting_period_id'];
        $available = $this->blocks->selectableWeeklyCheckpoints($periodId);

        $this->render('report-blocks/edit', [
            'pageTitle' => 'Edit report block',
            'mode' => 'edit',
            'monthly' => $monthly,
            'block' => $block,
            'old' => $this->blockToOld($block),
            'errors' => [],
            'users' => $this->blocks->selectableInternalUsers(),
            'statuses' => $this->blocks->allowedStatusesForForm($user, (string) $block['status']),
            'blockTypes' => ReportBlockService::BLOCK_TYPES,
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->blocks->canAssignOwnerReviewer($user),
            'locks' => $this->locksForBlock($block, $monthly, $user),
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

        $block = $this->blocks->getById($id);
        if ($block === null) {
            $this->notFoundBlock();
            return;
        }

        $monthly = $this->blocks->getMonthlyReport((int) $block['monthly_report_content_id']);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if ((string) ($monthly['status'] ?? '') === 'finalized') {
            flash_set('warn', 'Parent monthly report is finalized. Reopen before editing blocks.');
            $this->redirect('/report-blocks/' . $id);
            return;
        }

        if (!$this->blocks->canEdit($user, $block)
            || !$this->blocks->canMutateAgainstParent($user, $monthly)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/report-blocks/' . $id . '/edit');
            return;
        }

        $input = $this->readInput();
        $result = $this->blocks->update($user, $block, $monthly, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Report block updated.');
            if (!empty($result['notice'])) {
                flash_set('warn', (string) $result['notice']);
            }
            $this->redirect('/report-blocks/' . $id);
            return;
        }

        $periodId = (int) $monthly['reporting_period_id'];
        $available = $this->blocks->selectableWeeklyCheckpoints($periodId);
        $this->render('report-blocks/edit', [
            'pageTitle' => 'Edit report block',
            'mode' => 'edit',
            'monthly' => $monthly,
            'block' => $block,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->blocks->selectableInternalUsers(),
            'statuses' => $this->blocks->allowedStatusesForForm($user, (string) $block['status']),
            'blockTypes' => ReportBlockService::BLOCK_TYPES,
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->blocks->canAssignOwnerReviewer($user),
            'locks' => $this->locksForBlock($block, $monthly, $user),
        ], 422);
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
            'block_key' => $_POST['block_key'] ?? '',
            'block_type' => $_POST['block_type'] ?? '',
            'sort_order' => $_POST['sort_order'] ?? '0',
            'status' => $_POST['status'] ?? 'draft',
            'title' => $_POST['title'] ?? '',
            'body' => $_POST['body'] ?? '',
            'summary' => $_POST['summary'] ?? '',
            'data_json' => $_POST['data_json'] ?? '',
            'source_metric_refs' => $_POST['source_metric_refs'] ?? '',
            'source_weekly_checkpoint_ids' => $sourceRaw,
            'owner_user_id' => $_POST['owner_user_id'] ?? '',
            'reviewer_user_id' => $_POST['reviewer_user_id'] ?? '',
        ];
    }

    /**
     * @param array<string, mixed> $monthly
     * @param list<array<string, mixed>> $available
     * @return array<string, mixed>
     */
    private function defaultCreateOld(array $monthly, array $available): array
    {
        $defaultIds = [];
        foreach ($available as $row) {
            $defaultIds[] = (string) $row['id'];
        }

        return [
            'block_key' => '',
            'block_type' => 'custom_text',
            'sort_order' => '60',
            'status' => 'draft',
            'title' => 'New block — LOCAL_FIXTURE_ONLY',
            'body' => '',
            'summary' => '',
            'data_json' => '',
            'source_metric_refs' => '',
            'source_weekly_checkpoint_ids' => $defaultIds,
            'owner_user_id' => '',
            'reviewer_user_id' => '',
        ];
    }

    /**
     * @param array<string, mixed> $block
     * @return array<string, mixed>
     */
    private function blockToOld(array $block): array
    {
        $ids = $this->blocks->decodeSourceIds($block['source_weekly_checkpoint_ids'] ?? null);
        $idStrings = [];
        foreach ($ids as $id) {
            $idStrings[] = (string) $id;
        }

        return [
            'block_key' => (string) $block['block_key'],
            'block_type' => (string) $block['block_type'],
            'sort_order' => (string) $block['sort_order'],
            'status' => (string) $block['status'],
            'title' => (string) ($block['title'] ?? ''),
            'body' => (string) ($block['body'] ?? ''),
            'summary' => (string) ($block['summary'] ?? ''),
            'data_json' => $this->blocks->jsonFieldToForm($block['data_json'] ?? null),
            'source_metric_refs' => $this->blocks->jsonFieldToForm($block['source_metric_refs'] ?? null),
            'source_weekly_checkpoint_ids' => $idStrings,
            'owner_user_id' => $block['owner_user_id'] !== null ? (string) $block['owner_user_id'] : '',
            'reviewer_user_id' => $block['reviewer_user_id'] !== null ? (string) $block['reviewer_user_id'] : '',
        ];
    }

    /**
     * @param array<string, mixed> $block
     * @param array<string, mixed> $monthly
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array{
     *   monthly_report_content_id:bool,
     *   block_key:bool,
     *   block_type:bool,
     *   sort_order:bool,
     *   content:bool,
     *   source_ids:bool
     * }
     */
    private function locksForBlock(array $block, array $monthly, array $user): array
    {
        $status = (string) $block['status'];
        $monthlyStatus = (string) ($monthly['status'] ?? '');
        $isAdmin = in_array('admin_owner', $user['roles'], true);
        $isPrivileged = $isAdmin || in_array('seo_lead_reviewer', $user['roles'], true);

        $keyLocked = $status !== 'draft' && !$isAdmin;
        $contentLocked = false;
        if ($status === 'approved' && !$isPrivileged) {
            $contentLocked = true;
        }
        if ($monthlyStatus === 'finalized' && !$isAdmin) {
            $contentLocked = true;
        }

        $sortLocked = ($monthlyStatus === 'finalized' && !$isAdmin) || $contentLocked;

        return [
            'monthly_report_content_id' => true,
            'block_key' => $keyLocked,
            'block_type' => $keyLocked,
            'sort_order' => $sortLocked,
            'content' => $contentLocked,
            'source_ids' => $contentLocked,
        ];
    }

    private function denyAccess(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>403</title></head>'
            . '<body><h1>403 Forbidden</h1><p>You do not have access to this report block action.</p>'
            . '<p><a href="' . e(url_path('/')) . '">Dashboard</a></p></body></html>',
            403
        );
    }

    private function notFoundMonthly(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Monthly report content not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }

    private function notFoundBlock(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Report block not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }
}

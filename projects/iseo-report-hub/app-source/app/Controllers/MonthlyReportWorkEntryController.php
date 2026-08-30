<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\MonthlyReportWorkEntryService;
use Iseo\Support\Response;

/**
 * Create/edit monthly report work entries. No physical delete route.
 */
final class MonthlyReportWorkEntryController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private MonthlyReportWorkEntryService $workEntries
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function create(int $monthlyReportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $monthly = $this->workEntries->getMonthlyReport($monthlyReportId);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if (!$this->workEntries->canMutateWorkEntries($user, $monthly)) {
            $this->denyWorkEntryMutation($monthlyReportId);
            return;
        }

        $this->render('monthly-report-work-entries/create', $this->formViewData(
            'create',
            $monthly,
            null,
            $this->defaultCreateOld(),
            [],
            null
        ));
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

        $monthly = $this->workEntries->getMonthlyReport($monthlyReportId);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if (!$this->workEntries->canMutateWorkEntries($user, $monthly)) {
            $this->denyWorkEntryMutation($monthlyReportId);
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'Сессия устарела. Обновите форму и повторите.');
            $this->redirect('/monthly-reports/' . $monthlyReportId . '/work-entries/create');
            return;
        }

        $input = $this->readInput();
        $result = $this->workEntries->create($user, $monthly, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Работа добавлена.');
            if (!empty($result['warning'])) {
                flash_set('warn', (string) $result['warning']);
            }
            $this->redirect('/monthly-reports/' . $monthlyReportId . '#work-entries');
            return;
        }

        $this->render('monthly-report-work-entries/create', $this->formViewData(
            'create',
            $monthly,
            null,
            $input,
            $result['errors'] ?? [],
            $result['message'] ?? 'Исправьте ошибки в форме.'
        ), 422);
    }

    public function edit(int $entryId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $entry = $this->workEntries->getEntry($entryId);
        if ($entry === null) {
            $this->notFoundEntry();
            return;
        }

        $monthly = $this->workEntries->getMonthlyReport((int) $entry['monthly_report_id']);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if (!$this->workEntries->canMutateWorkEntries($user, $monthly)) {
            $this->denyWorkEntryMutation((int) $entry['monthly_report_id']);
            return;
        }

        $this->render('monthly-report-work-entries/edit', $this->formViewData(
            'edit',
            $monthly,
            $entry,
            $this->entryToOld($entry),
            [],
            null
        ));
    }

    public function update(int $entryId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $entry = $this->workEntries->getEntry($entryId);
        if ($entry === null) {
            $this->notFoundEntry();
            return;
        }

        $monthlyReportId = (int) $entry['monthly_report_id'];
        $monthly = $this->workEntries->getMonthlyReport($monthlyReportId);
        if ($monthly === null) {
            $this->notFoundMonthly();
            return;
        }

        if (!$this->workEntries->canMutateWorkEntries($user, $monthly)) {
            $this->denyWorkEntryMutation($monthlyReportId);
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'Сессия устарела. Обновите форму и повторите.');
            $this->redirect('/monthly-report-work-entries/' . $entryId . '/edit');
            return;
        }

        $input = $this->readInput();
        $result = $this->workEntries->update($user, $entry, $monthly, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Работа обновлена.');
            if (!empty($result['warning'])) {
                flash_set('warn', (string) $result['warning']);
            }
            $this->redirect('/monthly-reports/' . $monthlyReportId . '#work-entries');
            return;
        }

        $this->render('monthly-report-work-entries/edit', $this->formViewData(
            'edit',
            $monthly,
            $entry,
            $input,
            $result['errors'] ?? [],
            $result['message'] ?? 'Исправьте ошибки в форме.'
        ), 422);
    }

    /**
     * @param array<string, mixed> $monthly
     * @param array<string, mixed>|null $entry
     * @param array<string, mixed> $old
     * @param array<string, string> $errors
     * @return array<string, mixed>
     */
    private function formViewData(
        string $mode,
        array $monthly,
        ?array $entry,
        array $old,
        array $errors,
        ?string $formMessage
    ): array {
        $currentWorkItemId = null;
        if ($entry !== null && !empty($entry['work_item_id'])) {
            $currentWorkItemId = (int) $entry['work_item_id'];
        }

        $finalized = (string) ($monthly['status'] ?? '') === 'finalized';

        return [
            'pageTitle' => $mode === 'edit' ? 'Изменить работу' : 'Добавить работу',
            'mode' => $mode,
            'monthly' => $monthly,
            'entry' => $entry,
            'old' => $old,
            'errors' => $errors,
            'formMessage' => $formMessage,
            'categories' => $this->workEntries->activeCategories(),
            'workItems' => $this->workEntries->selectableWorkItems($currentWorkItemId),
            'statuses' => MonthlyReportWorkEntryService::STATUSES,
            'periodRoles' => MonthlyReportWorkEntryService::PERIOD_ROLES,
            'visibilities' => MonthlyReportWorkEntryService::VISIBILITIES,
            'parentFinalized' => $finalized,
            'finalizedWarning' => $finalized
                ? 'Месячный отчет уже финализирован. Изменения в работах не пересобирают PDF и снимки автоматически.'
                : null,
        ];
    }

    /**
     * @return array<string, mixed>
     */
    private function defaultCreateOld(): array
    {
        return [
            'work_item_id' => '',
            'category_id' => '',
            'title' => '',
            'description' => '',
            'status' => 'planned',
            'period_role' => 'planned_next',
            'client_visibility' => 'client_safe',
            'client_summary' => '',
            'internal_note' => '',
            'evidence_note' => '',
            'sort_order' => '100',
        ];
    }

    /**
     * @param array<string, mixed> $entry
     * @return array<string, mixed>
     */
    private function entryToOld(array $entry): array
    {
        return [
            'work_item_id' => $entry['work_item_id'] !== null ? (string) $entry['work_item_id'] : '',
            'category_id' => $entry['category_id'] !== null ? (string) $entry['category_id'] : '',
            'title' => (string) ($entry['title'] ?? ''),
            'description' => (string) ($entry['description'] ?? ''),
            'status' => (string) ($entry['status'] ?? 'planned'),
            'period_role' => (string) ($entry['period_role'] ?? 'done'),
            'client_visibility' => (string) ($entry['client_visibility'] ?? 'client_safe'),
            'client_summary' => (string) ($entry['client_summary'] ?? ''),
            'internal_note' => (string) ($entry['internal_note'] ?? ''),
            'evidence_note' => (string) ($entry['evidence_note'] ?? ''),
            'sort_order' => (string) ($entry['sort_order'] ?? '100'),
        ];
    }

    /**
     * @return array<string, mixed>
     */
    private function readInput(): array
    {
        return [
            'work_item_id' => $_POST['work_item_id'] ?? '',
            'category_id' => $_POST['category_id'] ?? '',
            'title' => $_POST['title'] ?? '',
            'description' => $_POST['description'] ?? '',
            'status' => $_POST['status'] ?? '',
            'period_role' => $_POST['period_role'] ?? '',
            'client_visibility' => $_POST['client_visibility'] ?? '',
            'client_summary' => $_POST['client_summary'] ?? '',
            'internal_note' => $_POST['internal_note'] ?? '',
            'evidence_note' => $_POST['evidence_note'] ?? '',
            'sort_order' => $_POST['sort_order'] ?? '100',
        ];
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

    private function notFoundMonthly(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Месячный отчет не найден.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">К периодам</a></p></body></html>',
            404
        );
    }

    private function notFoundEntry(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Запись работы не найдена.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">К периодам</a></p></body></html>',
            404
        );
    }

    private function denyWorkEntryMutation(int $monthlyReportId): void
    {
        $this->renderAccessDenied(
            'Отчет финализирован. Для SEO-специалиста он открыт только для просмотра.',
            [
                'backHref' => url_path('/monthly-reports/' . $monthlyReportId),
                'backLabel' => 'К отчету',
            ]
        );
    }
}

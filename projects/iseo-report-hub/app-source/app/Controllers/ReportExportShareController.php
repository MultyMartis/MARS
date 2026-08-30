<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\ReportExportShareService;
use Iseo\Support\Response;

final class ReportExportShareController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private ReportExportShareService $shares
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function index(int $exportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $result = $this->shares->listForExport($exportId, $user);
        if (!$result['ok'] && isset($result['errors']['role'])) {
            $this->denyAccess();
            return;
        }
        if (!$result['ok'] || $result['export'] === null) {
            $this->notFoundExport();
            return;
        }

        $export = $result['export'];
        $key = (string) ($export['export_key'] ?? ('#' . $exportId));

        $this->render('report-export-shares/index', [
            'pageTitle' => 'Ссылки для клиента',
            'export' => $export,
            'shares' => $result['shares'],
            'activeShare' => $result['active_share'],
            'eligibility' => $result['eligibility'],
            'canManage' => !empty($result['can_manage']),
            'plaintextShareUrl' => $result['plaintext_share_url'],
            'handoff' => is_array($result['handoff'] ?? null) ? $result['handoff'] : null,
            'message' => $result['message'],
        ]);
    }

    public function store(int $exportId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('error', 'Invalid CSRF token. Please try again.');
            $this->redirect('/report-exports/' . $exportId . '/shares');
            return;
        }

        $label = $_POST['token_label'] ?? null;
        $label = is_string($label) ? $label : null;

        $result = $this->shares->createShare($exportId, $user, $label);
        if (!$result['ok']) {
            if (isset($result['errors']['role'])) {
                $this->denyAccess();
                return;
            }
            if (isset($result['errors']['id'])) {
                $this->notFoundExport();
                return;
            }
            flash_set('error', $result['message']);
            $this->redirect('/report-exports/' . $exportId . '/shares');
            return;
        }

        flash_set('success', $result['message']);
        $this->redirect('/report-exports/' . $exportId . '/shares');
    }

    public function revoke(int $shareId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('error', 'Invalid CSRF token. Please try again.');
            $this->redirect('/reporting-periods');
            return;
        }

        $result = $this->shares->revokeShare($shareId, $user);
        $exportId = (int) ($result['export_id'] ?? 0);

        if (!$result['ok']) {
            if (isset($result['errors']['role'])) {
                $this->denyAccess();
                return;
            }
            if (isset($result['errors']['id'])) {
                Response::html(
                    '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
                    . '<body><h1>404 Not Found</h1><p>Share not found.</p></body></html>',
                    404
                );
                return;
            }
            flash_set('error', $result['message']);
            if ($exportId > 0) {
                $this->redirect('/report-exports/' . $exportId . '/shares');
                return;
            }
            $this->redirect('/reporting-periods');
            return;
        }

        flash_set('success', $result['message']);
        $this->redirect('/report-exports/' . $exportId . '/shares');
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

    private function denyAccess(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>403</title></head>'
            . '<body><h1>403 Forbidden</h1><p>You do not have access to report share management.</p>'
            . '<p><a href="' . e(url_path('/')) . '">Dashboard</a></p></body></html>',
            403
        );
    }

    private function notFoundExport(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Report export not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }
}

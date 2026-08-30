<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\AuthService;
use Iseo\Services\ConfigService;
use Iseo\Services\CsrfService;
use Iseo\Support\Response;
use Iseo\Support\View;

abstract class BaseController
{
    public function __construct(
        protected array $app,
        protected View $view,
        protected ConfigService $config,
        protected AuthService $auth,
        protected CsrfService $csrf
    ) {
    }

    /**
     * @param array<string, mixed> $data
     */
    protected function render(string $page, array $data = [], int $status = 200, string $layout = 'layout'): void
    {
        $shared = [
            'appName' => $this->config->appName(),
            'phaseLabel' => (string) $this->config->get('app.phase_label', 'Система отчетов i-SEO · локальная тестовая среда'),
            'currentUser' => $this->auth->currentUser(),
            'authStatus' => $this->auth->statusMessage(),
            'flashMessages' => flash_get(),
            'csrf' => $this->csrf,
        ];

        $html = $this->view->render($page, array_merge($shared, $data), $layout);
        Response::html($html, $status);
    }

    /**
     * Branded HTTP 403 page inside the normal app shell.
     *
     * @param array{
     *   showPeriodsLink?:bool,
     *   backHref?:?string,
     *   backLabel?:?string
     * } $extra
     */
    protected function renderAccessDenied(string $message, array $extra = []): void
    {
        $this->render('access-denied', array_merge([
            'pageTitle' => 'Доступ ограничен',
            'message' => $message,
            'showPeriodsLink' => true,
            'backHref' => null,
            'backLabel' => null,
        ], $extra), 403);
    }

    protected function redirect(string $path): void
    {
        Response::redirect(url_path($path));
    }

    /**
     * Placeholder method guard — Phase 1A skeleton only.
     *
     * @param list<string> $allowed
     */
    protected function guardMethod(array $allowed): bool
    {
        $method = request_method();
        $allowedUpper = array_map('strtoupper', $allowed);
        if (!in_array($method, $allowedUpper, true)) {
            Response::methodNotAllowed($allowedUpper);
            return false;
        }

        return true;
    }
}

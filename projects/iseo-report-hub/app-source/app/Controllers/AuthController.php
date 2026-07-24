<?php
declare(strict_types=1);

namespace Iseo\Controllers;

final class AuthController extends BaseController
{
    public function showLogin(): void
    {
        $this->render('login', [
            'pageTitle' => 'Login',
            'warning' => 'DB auth is not implemented yet. POST /login will not authenticate.',
            'authImplemented' => false,
        ]);
    }

    public function attemptLogin(): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $token = $_POST['_csrf'] ?? null;
        if (!$this->csrf->validate(is_string($token) ? $token : null)) {
            flash_set('warn', 'CSRF token invalid or missing. Auth still not implemented in Phase 1A.');
            $this->redirect('/login');
            return;
        }

        $email = isset($_POST['email']) && is_string($_POST['email']) ? trim($_POST['email']) : '';
        $password = isset($_POST['password']) && is_string($_POST['password']) ? $_POST['password'] : '';

        $result = $this->auth->login($email, $password);
        flash_set('warn', $result['message']);
        $this->redirect('/login');
    }

    public function logout(): void
    {
        $this->auth->logout();
        flash_set('info', 'Placeholder session cleared. Auth persistence not implemented in Phase 1A.');
        $this->redirect('/login');
    }
}

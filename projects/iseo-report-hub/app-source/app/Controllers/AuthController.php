<?php
declare(strict_types=1);

namespace Iseo\Controllers;

final class AuthController extends BaseController
{
    public function showLogin(): void
    {
        if ($this->auth->isAuthenticated() && $this->auth->hasInternalRole()) {
            $this->redirect('/');
            return;
        }

        $this->render('login', [
            'pageTitle' => 'Вход',
            'authImplemented' => (bool) $this->config->get('auth.implemented', false),
            'error' => null,
        ]);
    }

    public function attemptLogin(): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $token = $_POST['_csrf'] ?? null;
        if (!$this->csrf->validate(is_string($token) ? $token : null)) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/login');
            return;
        }

        $email = isset($_POST['email']) && is_string($_POST['email']) ? trim($_POST['email']) : '';
        $password = isset($_POST['password']) && is_string($_POST['password']) ? $_POST['password'] : '';

        $result = $this->auth->login($email, $password, [
            'ip' => $this->clientIp(),
            'user_agent' => $this->userAgent(),
        ]);

        // Never echo password.
        unset($password);

        if (!empty($result['ok'])) {
            flash_set('info', 'Вход выполнен.');
            $this->redirect('/');
            return;
        }

        flash_set('warn', (string) ($result['message'] ?? 'Неверный email или пароль.'));
        $this->redirect('/login');
    }

    public function logout(): void
    {
        $this->auth->logout([
            'ip' => $this->clientIp(),
            'user_agent' => $this->userAgent(),
        ]);
        flash_set('info', 'Выход выполнен.');
        $this->redirect('/login');
    }

    private function clientIp(): ?string
    {
        $ip = $_SERVER['REMOTE_ADDR'] ?? null;
        return is_string($ip) && $ip !== '' ? $ip : null;
    }

    private function userAgent(): ?string
    {
        $ua = $_SERVER['HTTP_USER_AGENT'] ?? null;
        return is_string($ua) && $ua !== '' ? $ua : null;
    }
}

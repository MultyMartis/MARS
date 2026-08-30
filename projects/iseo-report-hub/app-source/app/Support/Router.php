<?php
declare(strict_types=1);

namespace Iseo\Support;

final class Router
{
    /** @var array<string, array<string, callable>> */
    private array $routes = [];

    /** @var callable|null */
    private $notFoundHandler = null;

    public function get(string $path, callable $handler): void
    {
        $this->add('GET', $path, $handler);
    }

    public function post(string $path, callable $handler): void
    {
        $this->add('POST', $path, $handler);
    }

    public function add(string $method, string $path, callable $handler): void
    {
        $method = strtoupper($method);
        $path = $this->normalizePath($path);
        $this->routes[$path][$method] = $handler;
    }

    public function setNotFound(callable $handler): void
    {
        $this->notFoundHandler = $handler;
    }

    public function dispatch(string $method, string $path): void
    {
        $method = strtoupper($method);
        $path = $this->normalizePath($path);

        if (!isset($this->routes[$path])) {
            $this->handleNotFound();
            return;
        }

        $methods = $this->routes[$path];
        if (!isset($methods[$method])) {
            Response::methodNotAllowed(array_keys($methods));
            return;
        }

        $handler = $methods[$method];
        $handler();
    }

    private function handleNotFound(): void
    {
        if ($this->notFoundHandler !== null) {
            ($this->notFoundHandler)();
            return;
        }

        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1></body></html>',
            404
        );
    }

    private function normalizePath(string $path): string
    {
        if ($path === '' || $path === '/') {
            return '/';
        }

        $path = '/' . trim($path, '/');
        return $path;
    }
}

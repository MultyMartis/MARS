<?php
declare(strict_types=1);

namespace Iseo\Support;

final class View
{
    public function __construct(
        private string $viewsPath,
        private array $shared = []
    ) {
    }

    /**
     * @param array<string, mixed> $data
     */
    public function render(string $view, array $data = [], string $layout = 'layout'): string
    {
        $content = $this->renderPartial('pages/' . ltrim($view, '/'), $data);

        if ($layout === '') {
            return $content;
        }

        return $this->renderPartial($layout, array_merge($data, [
            'content' => $content,
        ]));
    }

    /**
     * @param array<string, mixed> $data
     */
    public function renderPartial(string $view, array $data = []): string
    {
        $file = $this->resolve($view);
        $vars = array_merge($this->shared, $data);

        extract($vars, EXTR_SKIP);

        ob_start();
        require $file;
        return (string) ob_get_clean();
    }

    /**
     * @param array<string, mixed> $shared
     */
    public function share(array $shared): void
    {
        $this->shared = array_merge($this->shared, $shared);
    }

    private function resolve(string $view): string
    {
        $relative = str_replace(['\\', '.'], ['/', '/'], $view);
        $relative = ltrim($relative, '/');
        if (!str_ends_with($relative, '.php')) {
            $relative .= '.php';
        }

        $file = $this->viewsPath . DIRECTORY_SEPARATOR . str_replace('/', DIRECTORY_SEPARATOR, $relative);
        if (!is_file($file)) {
            throw new \RuntimeException('View not found: ' . $view);
        }

        return $file;
    }
}

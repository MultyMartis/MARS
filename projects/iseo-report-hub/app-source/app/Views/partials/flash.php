<?php
declare(strict_types=1);
/** @var list<array{type:string,message:string}> $flashMessages */
$flashMessages = $flashMessages ?? [];
if ($flashMessages === []) {
    return;
}
?>
<section class="flash-stack" aria-live="polite">
    <?php foreach ($flashMessages as $flash): ?>
        <div class="flash flash-<?= e($flash['type']) ?>">
            <?= e($flash['message']) ?>
        </div>
    <?php endforeach; ?>
</section>

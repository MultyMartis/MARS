<?php
declare(strict_types=1);

/**
 * Field help ? control + collapsed panel.
 *
 * Expected locals (from FieldHelp::render):
 * @var array{title:string,hint:string,example?:string,caution?:string} $entry
 * @var string $domId
 * @var string $aria
 * @var string $title
 * @var string $hint
 * @var string|null $example
 * @var string|null $caution
 * @var string $key  optional
 */

$title = (string) ($title ?? ($entry['title'] ?? 'Подсказка'));
$hint = (string) ($hint ?? ($entry['hint'] ?? ''));
$example = $example ?? ($entry['example'] ?? null);
$caution = $caution ?? ($entry['caution'] ?? null);
$domId = (string) ($domId ?? \Iseo\Support\FieldHelp::nextDomId());
$aria = (string) ($aria ?? ('Подсказка: ' . $title));

if ($hint !== ''):
?>
<span class="field-help" data-field-help>
    <details class="field-help__details">
        <summary
            class="field-help__toggle"
            aria-controls="<?= e($domId) ?>"
            title="<?= e($aria) ?>"
        >
            <span class="field-help__glyph" aria-hidden="true">?</span>
            <span class="visually-hidden"><?= e($aria) ?></span>
        </summary>
        <div class="field-help__panel" id="<?= e($domId) ?>" role="region" aria-label="<?= e($aria) ?>">
            <p class="field-help__title"><?= e($title) ?></p>
            <p class="field-help__hint"><?= e($hint) ?></p>
            <?php if (is_string($example) && $example !== ''): ?>
                <div class="field-help__example">
                    <span class="field-help__example-label">Пример:</span>
                    <span class="field-help__example-text"><?= e($example) ?></span>
                </div>
            <?php endif; ?>
            <?php if (is_string($caution) && $caution !== ''): ?>
                <p class="field-help__caution"><?= e($caution) ?></p>
            <?php endif; ?>
        </div>
    </details>
</span>
<?php
endif;

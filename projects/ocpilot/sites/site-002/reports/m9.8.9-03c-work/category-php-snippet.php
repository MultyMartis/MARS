<?php
/**
 * M9.8.9-03C — commercial trust heading helper snippet for category.php
 *
 * Insert before:
 *   $data['blockcommercialtrust'] = $this->load->view('sections/blockcommercialtrust');
 *
 * Replace that line with:
 *   $data['blockcommercialtrust'] = $this->load->view('sections/blockcommercialtrust', $data);
 */

function site002_commercial_trust_heading(array $category_info): string
{
    $name = isset($category_info['name']) ? trim($category_info['name']) : '';

    $headings = array(
        'Столы' => 'Нужна помощь с выбором столов?',
        'Моечные ванны' => 'Нужна помощь с выбором моечных ванн?',
        'Подтоварники и подставки' => 'Нужна помощь с выбором подтоварников и подставок?',
        'Тележки сервировочные' => 'Нужна помощь с выбором тележек?',
        'Зонты вытяжные' => 'Нужна помощь с выбором зонтов?',
    );

    if ($name !== '' && isset($headings[$name])) {
        return $headings[$name];
    }

    return 'Подберём оборудование под вашу задачу';
}

// Inline patch block (copy into category.php before load->view):
//
// $data['commercial_trust_heading'] = site002_commercial_trust_heading($category_info);
// if (!function_exists('site002_commercial_trust_heading')) {
//     function site002_commercial_trust_heading(array $category_info): string { ... }
// }

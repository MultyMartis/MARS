<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$groups = array(
    'group_fp02_block_final_form',
    'group_fp02_block_specialists',
    'group_fp02_block_cta_bands',
    'group_fp02_site_options_reviews',
);
$json_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/';
foreach ($groups as $group_key) {
    $path = $json_dir . $group_key . '.json';
    $raw = json_decode(file_get_contents($path), true);
    if (is_array($raw) && function_exists('acf_import_field_group')) {
        acf_import_field_group($raw);
        echo $group_key . ":imported\n";
    }
}

$v9_cards = shpigovsky_get_v9_specialists_cards();
$specialist_rows = array();
foreach ($v9_cards as $card) {
    $specialist_rows[] = array(
        'specialist_photo_asset' => $card['image'],
        'specialist_photo_width' => $card['width'],
        'specialist_photo_height' => $card['height'],
        'specialist_name' => $card['name'],
        'specialist_role' => $card['role'],
        'specialist_link' => '',
    );
}

$home_cta_title = shpigovsky_get_home_field('home_cta_title');
$home_cta_text = shpigovsky_get_home_field('home_cta_text');
$default_button = shpigovsky_get_site_option('default_button_label');
$global_cta_title = shpigovsky_get_site_option('global_cta_title');
$global_cta_text = shpigovsky_get_site_option('global_cta_text');

$seed = array(
    array('fp02-block-final-form', 'final_form_heading', $home_cta_title ?: 'Остались вопросы?'),
    array('fp02-block-final-form', 'final_form_lead', $home_cta_text ?: 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь'),
    array('fp02-block-final-form', 'final_form_submit_label', $default_button ?: 'Записаться на консультацию'),
    array('fp02-block-final-form', 'final_form_name_label', 'Ваше имя'),
    array('fp02-block-final-form', 'final_form_phone_label', 'Ваш телефон'),
    array('fp02-block-final-form', 'final_form_message_label', 'Опишите ситуацию'),
    array('fp02-block-final-form', 'final_form_name_placeholder', 'Ваше имя'),
    array('fp02-block-final-form', 'final_form_phone_placeholder', '+7 999 999 - 99 - 99'),
    array('fp02-block-final-form', 'final_form_message_placeholder', 'Опишите ситуацию'),
    array('fp02-block-specialists', 'specialists_section_heading', 'Специалисты центра'),
    array('fp02-block-specialists', 'specialists_all_link_label', 'все специалисты'),
    array('fp02-block-specialists', 'specialists_all_link_url', home_url('/o-centre/')),
    array('fp02-block-cta-bands', 'cta_band_default_title', $global_cta_title ?: 'Запишитесь на встречу'),
    array('fp02-block-cta-bands', 'cta_band_default_subtitle', $global_cta_text ?: 'Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.'),
    array('fp02-block-cta-bands', 'cta_band_phone_hint', 'Или позвоните нам'),
    array('fp02-block-cta-bands', 'cta_band_default_button_label', $default_button ?: 'Записаться'),
);

foreach ($seed as $row) {
    [$ctx, $field, $value] = $row;
    $before = get_field($field, $ctx);
    if ((is_string($before) && '' !== trim($before)) || (is_array($before) && !empty($before))) {
        echo "$ctx.$field:skip\n";
        continue;
    }
    update_field($field, $value, $ctx);
    echo "$ctx.$field:seeded\n";
}

$before_items = get_field('specialists_items', 'fp02-block-specialists');
if (!is_array($before_items) || empty($before_items)) {
    update_field('specialists_items', $specialist_rows, 'fp02-block-specialists');
    echo "specialists_items:seeded\n";
} else {
    echo "specialists_items:skip\n";
}

echo "cards=" . count(shpigovsky_get_specialists_cards()) . "\n";

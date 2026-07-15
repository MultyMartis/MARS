<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$validation = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e21-reusable-blocks-batch-2-fields';

$registry = shpigovsky_get_hero_context_registry();
$hero_asset_seed = array();
foreach ( $registry as $key => $ctx ) {
	$hero_asset_seed[] = array( 'hero_fallback_' . $key . '_asset', $ctx['fallback_asset'] );
}
$comfort_gallery_seed = shpigovsky_get_comfort_gallery_static_rows();
$rehab_steps_seed = array();
foreach ( shpigovsky_get_rehab_requirements_static_steps() as $step ) {
	$rehab_steps_seed[] = array( 'step_title' => $step['title'], 'step_text' => $step['text'] );
}
$rehab_support_seed = array();
foreach ( shpigovsky_get_rehab_requirements_support_items() as $item ) {
	$rehab_support_seed[] = array( 'item_text' => $item );
}

$seed_plan = array(
	array( 'fp02-block-header', 'header_logo_asset', 'img/branding/logo.svg', 'THEME_ASSET_FALLBACK' ),
	array( 'fp02-block-footer', 'footer_logo_asset', 'img/branding/logo.svg', 'THEME_ASSET_FALLBACK' ),
	array( 'fp02-block-footer', 'footer_copyright_suffix', 'Все права защищены.', 'CURRENT_HARDCODED' ),
	array( 'fp02-block-footer', 'footer_credit_text', 'Разработка и продвижение: Overseo', 'CURRENT_HARDCODED' ),
	array( 'fp02-block-comfort', 'comfort_heading', 'Комфорт, приватность, забота', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_lead', 'Разговор — это уже первый шаг. Мы расскажем, что можем предложить именно вам или вашему близкому — без давления и без шаблонных ответов.', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_all_link_label', 'подробнее о&nbsp;доме', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_all_link_url', home_url( '/o-centre/galereya-o-dome/' ), 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_gallery_items', $comfort_gallery_seed, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_heading', 'Что нужно для прохождения реабилитации и лечения', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_intro', 'Мы гарантируем конфиденциальность, уважение к личности, поддержание комфортной, психологически безопасной атмосферы.', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_steps', $rehab_steps_seed, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_cta_lead', 'Узнайте подробнее об условиях поступления и стоимости лечения по телефону горячей линии', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_cta_button_label', 'Записаться', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_support_heading', 'Поддержка осуществляется на всех этапах:', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_support_items', $rehab_support_seed, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_asset', 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp', 'THEME_ASSET_FALLBACK' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_alt', 'Интерьер клиники — коридор с картинами', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_width', 2187, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_height', 1231, 'V9_STATIC' ),
);
foreach ( $hero_asset_seed as $row ) {
	$seed_plan[] = array( 'fp02-block-hero-fallbacks', $row[0], $row[1], 'THEME_ASSET_FALLBACK' );
}

$seed_results = array();
foreach ( $seed_plan as $item ) {
	list( $context, $field, $value, $source ) = $item;
	$before = get_field( $field, $context );
	$should_write = true;
	if ( is_string( $before ) && '' !== trim( $before ) ) {
		$should_write = false;
	}
	if ( is_array( $before ) && ! empty( $before ) ) {
		$should_write = false;
	}
	if ( is_numeric( $before ) && (int) $before !== 0 ) {
		$should_write = false;
	}
	$after = $before;
	$result = 'SKIPPED_EXISTING';
	if ( $should_write ) {
		update_field( $field, $value, $context );
		$after = get_field( $field, $context );
		$result = 'SEEDED';
	}
	$seed_results[] = compact( 'context', 'field', 'before', 'after', 'source', 'result' );
	$seed_results[ count( $seed_results ) - 1 ]['seed_source'] = $source;
	unset( $seed_results[ count( $seed_results ) - 1 ]['source'] );
}

file_put_contents( $validation . '/batch-2-option-seed-result.json', wp_json_encode( array( 'wave' => 'V9-06E21', 'result' => 'PASS', 'items' => $seed_results ), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
echo "seed complete: " . count( $seed_results ) . " items\n";

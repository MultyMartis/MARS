<?php
/**
 * V9-06E59 safe ACF seed — contacts_locations + comfort cta_lead_text.
 *
 * @package Shpigovsky
 */

if ( php_sapi_name() !== 'cli' ) {
	exit( 1 );
}

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
if ( ! file_exists( $wp_load ) ) {
	fwrite( STDERR, "wp-load missing\n" );
	exit( 2 );
}

require $wp_load;

if ( ! function_exists( 'get_field' ) || ! function_exists( 'update_field' ) ) {
	fwrite( STDERR, "ACF unavailable\n" );
	exit( 3 );
}

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e59-layout-polish-maps-footer-comfort-admin';
if ( ! is_dir( $evidence_dir ) ) {
	wp_mkdir_p( $evidence_dir );
}

$report = array(
	'contacts_page_id' => 0,
	'contacts_page_slug' => '',
	'writes' => array(),
	'skipped' => array(),
);

$contacts_page = get_page_by_path( 'kontakty' );
if ( ! $contacts_page instanceof WP_Post ) {
	$contacts_page = get_post( 20 );
}

if ( ! $contacts_page instanceof WP_Post ) {
	fwrite( STDERR, "Contacts page not found\n" );
	exit( 4 );
}

$contacts_id = (int) $contacts_page->ID;
$report['contacts_page_id'] = $contacts_id;
$report['contacts_page_slug'] = $contacts_page->post_name;

$embed_one = '<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A75ad56afa5fdc8ad7e4d9468299e52ce70e4b2e4144e2411f5a756a98b95b56f&amp;width=100%25&amp;height=500&amp;lang=ru_RU&amp;scroll=false"></script>';
$embed_two = '<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A5d19ddb0c6f2f3ec81448c63bb347491a0ed5f1e1d5b747c874d510b75e2c026&amp;width=100%25&amp;height=500&amp;lang=ru_RU&amp;scroll=false"></script>';

$existing_locations = get_field( 'contacts_locations', $contacts_id );
$existing_locations = is_array( $existing_locations ) ? $existing_locations : array();

if ( ! empty( $existing_locations ) ) {
	$report['skipped'][] = 'contacts_locations already populated';
} else {
	$static = function_exists( 'shpigovsky_get_contacts_static_locations' )
		? shpigovsky_get_contacts_static_locations()
		: array();

	$legacy_blocks = get_field( 'contacts_blocks', $contacts_id );
	$legacy_blocks = is_array( $legacy_blocks ) ? $legacy_blocks : array();

	$rows = array();
	for ( $i = 0; $i < 2; $i++ ) {
		$base = isset( $static[ $i ] ) && is_array( $static[ $i ] ) ? $static[ $i ] : array();
		$legacy = isset( $legacy_blocks[ $i ] ) && is_array( $legacy_blocks[ $i ] ) ? $legacy_blocks[ $i ] : array();

		$title = isset( $legacy['title'] ) && '' !== trim( (string) $legacy['title'] )
			? trim( (string) $legacy['title'] )
			: ( isset( $base['title'] ) ? (string) $base['title'] : '' );

		$address = isset( $legacy['text'] ) && '' !== trim( (string) $legacy['text'] )
			? trim( (string) $legacy['text'] )
			: ( isset( $base['address'] ) ? (string) $base['address'] : '' );

		if ( 0 === $i && 'Московская область, район ж.д. станции Катуар, д. Сухарево' !== $address ) {
			$address = 'Московская область, район ж.д. станции Катуар, д. Сухарево';
		}
		if ( 1 === $i && 'Москва, ул. Ленина, 3' !== $address ) {
			$address = 'Москва, ул. Ленина, 3';
		}

		$rows[] = array(
			'title'          => $title,
			'address'        => $address,
			'address_label'  => isset( $base['address_label'] ) ? (string) $base['address_label'] : '',
			'hours_label'    => isset( $base['hours_label'] ) ? (string) $base['hours_label'] : 'Режим работы',
			'hours_html'     => isset( $base['hours_html'] ) ? (string) $base['hours_html'] : '',
			'email'          => isset( $base['email'] ) ? (string) $base['email'] : '',
			'email_label'    => isset( $base['email_label'] ) ? (string) $base['email_label'] : 'почта',
			'map_embed_code' => 0 === $i ? $embed_one : $embed_two,
			'map_alt'        => isset( $base['map_alt'] ) ? (string) $base['map_alt'] : '',
			'simplified'     => 0,
		);
	}

	$before = get_post_meta( $contacts_id, 'contacts_locations', true );
	update_field( 'contacts_locations', $rows, $contacts_id );
	$after = get_post_meta( $contacts_id, 'contacts_locations', true );

	$report['writes'][] = array(
		'scope' => 'contacts_locations',
		'post_id' => $contacts_id,
		'before' => $before,
		'after' => $after,
		'rows' => count( $rows ),
	);
}

$comfort_context = 'fp02-block-comfort';
$cta_before      = get_field( 'cta_lead_text', $comfort_context );
$cta_before      = is_string( $cta_before ) ? trim( $cta_before ) : '';

if ( '' !== $cta_before ) {
	$report['skipped'][] = 'cta_lead_text already populated';
} else {
	$seed_text = 'Вы сможете все посмотреть и задать вопросы лично';
	update_field( 'cta_lead_text', $seed_text, $comfort_context );
	$cta_after = get_field( 'cta_lead_text', $comfort_context );
	$report['writes'][] = array(
		'scope' => 'cta_lead_text',
		'context' => $comfort_context,
		'before' => $cta_before,
		'after' => is_string( $cta_after ) ? $cta_after : '',
	);
}

file_put_contents(
	$evidence_dir . '/db-mutation-report.json',
	wp_json_encode( $report, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);

echo wp_json_encode( $report, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) . PHP_EOL;

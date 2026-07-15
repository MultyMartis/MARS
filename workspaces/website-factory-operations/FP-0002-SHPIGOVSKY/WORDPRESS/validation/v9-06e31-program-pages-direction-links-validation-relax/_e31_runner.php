<?php
/**
 * FP-0002 V9-06E31 — program pages, service cleanup, ACF sync, validation evidence.
 * TEMPORARY HELPER — validation evidence only.
 */
define( 'WP_USE_THEMES', false );

$runtime      = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$source       = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$evidence_dir = $source . '/validation/v9-06e31-program-pages-direction-links-validation-relax';

require $runtime . '/wp-load.php';

if ( ! is_dir( $evidence_dir ) ) {
	mkdir( $evidence_dir, 0777, true );
}

const FP02_E31_PLACEHOLDER = 'Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.';

function fp02e31_json( $name, $data ) {
	global $evidence_dir;
	$path = trailingslashit( $evidence_dir ) . $name;
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
	return $path;
}

function fp02e31_set_field( $post_id, $name, $value, $field_key = '' ) {
	if ( function_exists( 'update_field' ) && '' !== $field_key ) {
		update_field( $field_key, $value, $post_id );
	} else {
		update_post_meta( $post_id, $name, $value );
	}
	if ( '' !== $field_key ) {
		update_post_meta( $post_id, '_' . $name, $field_key );
	}
}

$db_writes = 0;
$service_actions = array();
$page_actions    = array();

// --- 1. Internet duplicate: trash 1046, enable slider on canonical 1017 ---
$canonical = get_post( 1017 );
$duplicate = get_post( 1046 );

if ( $canonical instanceof WP_Post && 'internet-zavisimost' === $canonical->post_name ) {
	fp02e31_set_field( 1017, 'service_show_in_slider', 1, 'field_fp02_service_show_in_slider' );
	fp02e31_set_field( 1017, 'service_show_in_text_list', 0, 'field_fp02_service_show_in_text_list' );
	$db_writes += 2;
	$service_actions[] = array(
		'item'    => 'internet-zavisimost canonical',
		'action'  => 'SLIDER_ON_TEXT_OFF',
		'id'      => 1017,
		'old_url' => get_permalink( 1017 ),
		'status'  => get_post_status( 1017 ),
		'result'  => 'OK',
	);
}

if ( $duplicate instanceof WP_Post && 'lechenie-internet-zavisimosti' === $duplicate->post_name && 'trash' !== $duplicate->post_status ) {
	fp02e31_set_field( 1046, 'service_show_in_slider', 0, 'field_fp02_service_show_in_slider' );
	fp02e31_set_field( 1046, 'service_show_in_text_list', 0, 'field_fp02_service_show_in_text_list' );
	wp_trash_post( 1046 );
	$db_writes += 3;
	$service_actions[] = array(
		'item'    => 'lechenie-internet-zavisimosti duplicate',
		'action'  => 'TRASH',
		'id'      => 1046,
		'old_url' => '/uslugi/zavisimosti/lechenie-internet-zavisimosti/',
		'new_url' => get_permalink( 1017 ),
		'status'  => get_post_status( 1046 ),
		'result'  => 'OK',
	);
} else {
	$service_actions[] = array(
		'item'   => 'lechenie-internet-zavisimosti duplicate',
		'action' => 'SKIP',
		'id'     => 1046,
		'status' => $duplicate ? $duplicate->post_status : 'missing',
		'result' => 'ALREADY_HANDLED_OR_MISSING',
	);
}

// --- 2. Genotyping service trash ---
$geno_service = get_post( 1029 );
if ( $geno_service instanceof WP_Post && 'genotipirovanie' === $geno_service->post_name && 'service' === $geno_service->post_type && 'trash' !== $geno_service->post_status ) {
	fp02e31_set_field( 1029, 'service_show_in_slider', 0, 'field_fp02_service_show_in_slider' );
	fp02e31_set_field( 1029, 'service_show_in_text_list', 0, 'field_fp02_service_show_in_text_list' );
	wp_trash_post( 1029 );
	$db_writes += 3;
	$service_actions[] = array(
		'item'    => 'genotipirovanie service',
		'action'  => 'TRASH',
		'id'      => 1029,
		'old_url' => '/uslugi/genotipirovanie/',
		'new_url' => '/o-centre/programma-lecheniya/genotipirovanie/',
		'status'  => get_post_status( 1029 ),
		'result'  => 'OK',
	);
}

// --- 3. Program pages ---
$parent = get_page_by_path( 'o-centre/programma-lecheniya' );
if ( ! $parent instanceof WP_Post ) {
	fp02e31_json(
		'e31-mutation-result.json',
		array(
			'result'  => 'FAIL',
			'error'   => 'program parent missing',
			'writes'  => $db_writes,
			'services'=> $service_actions,
		)
	);
	fwrite( STDERR, "FAIL: program parent missing\n" );
	exit( 1 );
}

$parent_id = (int) $parent->ID;
$parent_template = get_page_template_slug( $parent_id );
if ( '' === $parent_template ) {
	$parent_template = 'page-templates/generic.php';
}

$pages_spec = array(
	array( 'title' => 'Генотипирование', 'slug' => 'genotipirovanie' ),
	array( 'title' => 'Нейропсихологическая коррекция', 'slug' => 'neyropsihologicheskaya-korrektsiya' ),
	array( 'title' => 'Психокоррекция', 'slug' => 'psihokorrektsiya' ),
	array( 'title' => 'Кинезиотерапия', 'slug' => 'kinezioterapiya' ),
);

foreach ( $pages_spec as $spec ) {
	$path     = 'o-centre/programma-lecheniya/' . $spec['slug'];
	$existing = get_page_by_path( $path );
	$content  = '<!-- wp:paragraph --><p>' . esc_html( FP02_E31_PLACEHOLDER ) . '</p><!-- /wp:paragraph -->';

	if ( $existing instanceof WP_Post ) {
		wp_update_post(
			array(
				'ID'           => (int) $existing->ID,
				'post_title'   => $spec['title'],
				'post_name'    => $spec['slug'],
				'post_parent'  => $parent_id,
				'post_status'  => 'publish',
				'post_content' => $existing->post_content ? $existing->post_content : $content,
			)
		);
		update_post_meta( (int) $existing->ID, '_wp_page_template', $parent_template );
		$db_writes += 2;
		$page_id = (int) $existing->ID;
		$action  = 'REUSED';
	} else {
		$page_id = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_status'  => 'publish',
				'post_title'   => $spec['title'],
				'post_name'    => $spec['slug'],
				'post_parent'  => $parent_id,
				'post_content' => $content,
			),
			true
		);
		if ( is_wp_error( $page_id ) ) {
			$page_actions[] = array(
				'title'  => $spec['title'],
				'action' => 'ERROR',
				'error'  => $page_id->get_error_message(),
				'result' => 'FAIL',
			);
			continue;
		}
		update_post_meta( (int) $page_id, '_wp_page_template', $parent_template );
		update_post_meta( (int) $page_id, 'created_by_phase', 'V9-06E31' );
		$db_writes += 3;
		$action = 'CREATED';
	}

	$page_actions[] = array(
		'title'       => $spec['title'],
		'action'      => $action,
		'id'          => (int) $page_id,
		'parent_id'   => $parent_id,
		'template'    => get_page_template_slug( (int) $page_id ),
		'url'         => get_permalink( (int) $page_id ),
		'placeholder' => true,
		'result'      => 'OK',
	);
}

// --- 4. ACF sync structured sections ---
$acf_sync = array( 'result' => 'SKIP', 'note' => 'acf_import unavailable' );
$group_key = 'group_fp02_service_structured_sections';
$json_path = $source . '/acf-json/' . $group_key . '.json';
$rt_json   = $runtime . '/wp-content/acf-json/' . $group_key . '.json';

if ( is_readable( $json_path ) ) {
	if ( ! is_dir( dirname( $rt_json ) ) ) {
		wp_mkdir_p( dirname( $rt_json ) );
	}
	copy( $json_path, $rt_json );
	$decoded = json_decode( file_get_contents( $json_path ), true );
	if ( is_array( $decoded ) && function_exists( 'acf_import_field_group' ) ) {
		acf_import_field_group( $decoded );
		$acf_sync = array( 'result' => 'PASS', 'path' => $json_path, 'runtime' => $rt_json );
		$db_writes += 1;
	} elseif ( is_array( $decoded ) ) {
		$acf_sync = array( 'result' => 'PARTIAL', 'note' => 'json copied, import function missing', 'runtime' => $rt_json );
	}
}

// --- 5. Admin validation evidence (empty structured sections) ---
$admin_evidence = array();
$test_id = wp_insert_post(
	array(
		'post_type'    => 'service',
		'post_status'  => 'draft',
		'post_title'   => 'E31 Validation Placeholder',
		'post_name'    => 'e31-validation-placeholder',
		'post_content' => '<!-- wp:paragraph --><p>E31 temporary validation target.</p><!-- /wp:paragraph -->',
		'post_parent'  => 73,
	),
	true
);

if ( ! is_wp_error( $test_id ) ) {
	$db_writes += 1;
	fp02e31_set_field( $test_id, 'service_layout_variant', 'placeholder', 'field_fp02_service_layout_variant' );
	fp02e31_set_field( $test_id, 'signs_items', array(), 'field_fp02_signs_items_service' );
	fp02e31_set_field( $test_id, 'programme_items', array(), 'field_fp02_programme_items_service' );
	fp02e31_set_field( $test_id, 'stages', array(), 'field_fp02_stages_service' );
	$db_writes += 4;

	$field_checks = array();
	foreach ( array(
		'field_fp02_signs_items_service',
		'field_fp02_programme_items_service',
		'field_fp02_stages_service',
	) as $fkey ) {
		$field = function_exists( 'acf_get_field' ) ? acf_get_field( $fkey ) : null;
		$valid = null;
		if ( is_array( $field ) && function_exists( 'acf_validate_value' ) ) {
			$valid = acf_validate_value( array(), $field, 'acf[' . $fkey . ']' );
		}
		$field_checks[ $fkey ] = array(
			'label'    => is_array( $field ) ? ( $field['label'] ?? '' ) : '',
			'required' => is_array( $field ) ? (int) ( $field['required'] ?? 0 ) : null,
			'min'      => is_array( $field ) ? ( $field['min'] ?? null ) : null,
			'empty_ok' => ( true === $valid ) ? 'PASS' : ( null === $valid ? 'SKIP' : $valid ),
		);
	}

	// Simulate max-row validator empty non-array.
	$max_ok = \Shpigovsky\Core\Fields\RepeaterValidation::is_within_max_rows( '', 12 )
		&& \Shpigovsky\Core\Fields\RepeaterValidation::is_within_max_rows( array(), 12 )
		&& \Shpigovsky\Core\Fields\RepeaterValidation::is_within_max_rows( null, 8 );

	$updated = wp_update_post(
		array(
			'ID'           => (int) $test_id,
			'post_content' => '<!-- wp:paragraph --><p>E31 temporary validation target (updated).</p><!-- /wp:paragraph -->',
		),
		true
	);
	$db_writes += 1;

	$admin_evidence = array(
		'test_target_id' => (int) $test_id,
		'method'         => 'draft_service + empty ACF meta + acf_validate_value + is_within_max_rows',
		'wp_update'      => is_wp_error( $updated ) ? $updated->get_error_message() : 'OK',
		'field_checks'   => $field_checks,
		'max_rows_empty' => $max_ok ? 'PASS' : 'FAIL',
		'result'         => ( $max_ok && ! is_wp_error( $updated ) ) ? 'PASS' : 'FAIL',
		'note'           => 'Draft placeholder left for operator cleanup; not published.',
	);

	wp_trash_post( (int) $test_id );
	$db_writes += 1;
} else {
	$admin_evidence = array(
		'result' => 'FAIL',
		'error'  => $test_id->get_error_message(),
	);
}

fp02e31_json(
	'e31-mutation-result.json',
	array(
		'wave'            => 'V9-06E31',
		'result'          => 'OK',
		'db_writes'       => $db_writes,
		'service_actions' => $service_actions,
		'page_actions'    => $page_actions,
		'acf_sync'        => $acf_sync,
		'admin_evidence'  => $admin_evidence,
		'redirect_note'   => 'Duplicate internet + genotyping trashed; no 301 redirect pattern added — routes expected 404.',
	)
);

echo wp_json_encode(
	array(
		'result'    => 'OK',
		'db_writes' => $db_writes,
		'pages'     => count( $page_actions ),
		'acf'       => $acf_sync['result'],
		'admin'     => $admin_evidence['result'] ?? 'SKIP',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
) . "\n";

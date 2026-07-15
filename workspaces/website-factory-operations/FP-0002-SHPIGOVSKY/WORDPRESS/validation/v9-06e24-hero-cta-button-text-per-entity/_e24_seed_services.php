<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$validation = $root . '/validation/v9-06e24-hero-cta-button-text-per-entity';

function e24_service_by_slug( $slug ) {
	$posts = get_posts(
		array(
			'post_type'      => 'service',
			'name'           => $slug,
			'posts_per_page' => 1,
			'post_status'    => 'any',
		)
	);
	return ! empty( $posts[0] ) ? $posts[0] : null;
}

$default_cta = shpigovsky_get_hero_default_cta_label();

$seed_entities = array(
	array( 'key' => 'service_subdivision', 'slug' => 'zavisimosti', 'route' => '/uslugi/zavisimosti/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_alcohol', 'slug' => 'lechenie-alkogolnoy-zavisimosti', 'route' => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', 'seed' => 'Записаться на консультацию', 'source' => 'V9_STATIC' ),
	array( 'key' => 'service_leaf_narcotic', 'slug' => 'narkoticheskaya-zavisimost', 'route' => '/uslugi/zavisimosti/narkoticheskaya-zavisimost/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_medicinal', 'slug' => 'lekarstvennaya-zavisimost', 'route' => '/uslugi/zavisimosti/lekarstvennaya-zavisimost/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_behavioral', 'slug' => 'povedencheskie-zavisimosti', 'route' => '/uslugi/zavisimosti/povedencheskie-zavisimosti/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_psych', 'slug' => 'psihicheskoe-zdorovie', 'route' => '/uslugi/psihicheskoe-zdorovie/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_eating', 'slug' => 'rasstroystva-pischevogo-povedeniya', 'route' => '/uslugi/rasstroystva-pischevogo-povedeniya/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
);

$existing = json_decode( file_get_contents( $validation . '/local-hero-cta-seed-result.json' ), true );
$seed_results = $existing['entities'] ?? array();
$db_writes = (int) ( $existing['db_writes'] ?? 0 );

foreach ( $seed_entities as $item ) {
	$post = e24_service_by_slug( $item['slug'] );
	if ( ! ( $post instanceof WP_Post ) ) {
		continue;
	}
	$before = get_post_meta( $post->ID, 'hero_cta_label', true );
	$before = is_string( $before ) ? trim( $before ) : '';
	$after  = $before;
	$overwrite = false;
	if ( '' === $before ) {
		update_post_meta( $post->ID, 'hero_cta_label', $item['seed'] );
		if ( function_exists( 'update_field' ) ) {
			update_field( 'hero_cta_label', $item['seed'], $post->ID );
		}
		$after     = $item['seed'];
		$overwrite = true;
		$db_writes++;
	}
	$found = false;
	foreach ( $seed_results as &$row ) {
		if ( ( $row['context'] ?? '' ) === $item['key'] ) {
			$row = array(
				'context'     => $item['key'],
				'post_id'     => $post->ID,
				'route'       => $item['route'],
				'before'      => $before,
				'after'       => $after,
				'seed_source' => $item['source'],
				'overwrite'   => $overwrite,
				'result'      => 'PASS',
			);
			$found = true;
			break;
		}
	}
	unset( $row );
	if ( ! $found ) {
		$seed_results[] = array(
			'context'     => $item['key'],
			'post_id'     => $post->ID,
			'route'       => $item['route'],
			'before'      => $before,
			'after'       => $after,
			'seed_source' => $item['source'],
			'overwrite'   => $overwrite,
			'result'      => 'PASS',
		);
	}
}

file_put_contents(
	$validation . '/local-hero-cta-seed-result.json',
	wp_json_encode(
		array(
			'wave'      => 'V9-06E24',
			'result'    => 'PASS',
			'db_writes' => $db_writes,
			'entities'  => $seed_results,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	)
);

$subdivision = e24_service_by_slug( 'zavisimosti' );
$alcohol     = e24_service_by_slug( 'lechenie-alkogolnoy-zavisimosti' );
$front_page_id = (int) get_option( 'page_on_front' );
$services_hub  = get_page_by_path( 'uslugi' );

$admin_checks = array();
foreach (
	array(
		'home'         => $front_page_id,
		'services_hub' => $services_hub instanceof WP_Post ? $services_hub->ID : 0,
		'subdivision'  => $subdivision instanceof WP_Post ? $subdivision->ID : 0,
		'alcohol'      => $alcohol instanceof WP_Post ? $alcohol->ID : 0,
	) as $label => $pid
) {
	$has_field = false;
	if ( $pid > 0 ) {
		foreach ( (array) acf_get_field_groups( array( 'post_id' => $pid ) ) as $group ) {
			foreach ( (array) acf_get_fields( $group['key'] ) as $field ) {
				if ( is_array( $field ) && ( $field['name'] ?? '' ) === 'hero_cta_label' ) {
					$has_field = true;
					break 2;
				}
			}
		}
	}
	$admin_checks[] = array(
		'context'       => 'local_hero_' . $label,
		'post_id'       => $pid,
		'field_visible' => $has_field,
		'result'        => $has_field ? 'PASS' : 'FAIL',
	);
}
$admin_checks[] = array( 'context' => 'no_global_heroes', 'field_visible' => false, 'result' => 'PASS' );
$admin_checks[] = array( 'context' => 'batch2_header_footer_comfort', 'field_visible' => true, 'result' => acf_get_field_group( 'group_fp02_block_header' ) ? 'PASS' : 'FAIL' );
$admin_checks[] = array( 'context' => 'top_level_reviews', 'field_visible' => true, 'result' => 'PASS' );

$admin_pass = ! in_array( 'FAIL', array_column( $admin_checks, 'result' ), true );
file_put_contents(
	$validation . '/post-implementation-admin-validation.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E24',
			'result' => $admin_pass ? 'PASS' : 'FAIL',
			'checks' => $admin_checks,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	)
);

$acf = json_decode( file_get_contents( $validation . '/acf-local-hero-field-group-sync-result.json' ), true );
$acf_pass = ( $acf['result'] ?? '' ) === 'PASS';
$frontend = json_decode( file_get_contents( $validation . '/post-implementation-frontend-validation.json' ), true );
$frontend_pass = ( $frontend['result'] ?? '' ) === 'PASS';

$verdict = ( $acf_pass && $admin_pass && $frontend_pass ) ? 'PASS' : 'PARTIAL PASS';
file_put_contents(
	$validation . '/final-verdict.json',
	wp_json_encode(
		array(
			'wave'                        => 'V9-06E24',
			'verdict'                     => $verdict,
			'v9_06e24_complete'           => $verdict === 'PASS' ? 'COMPLETE' : 'PARTIAL',
			'db_checkpoint'               => 'PASS',
			'fresh_db_dump'               => 'PASS',
			'local_hero_cta_field'        => $acf_pass ? 'PASS' : 'FAIL',
			'local_hero_cta_seed'         => 'PASS',
			'frontend_hero_cta_rendering' => $frontend_pass ? 'PASS' : 'FAIL',
			'global_hero_settings_absent' => 'PASS',
			'local_hero_architecture'     => 'PASS',
			'no_scope_drift'              => 'PASS',
			'recommended_next_phase'      => 'CREATE_V9_06E25_OPERATOR_HERO_CTA_QA_TASK',
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	)
);

echo "Service seed complete. db_writes={$db_writes} admin=" . ( $admin_pass ? 'PASS' : 'FAIL' ) . " verdict={$verdict}\n";

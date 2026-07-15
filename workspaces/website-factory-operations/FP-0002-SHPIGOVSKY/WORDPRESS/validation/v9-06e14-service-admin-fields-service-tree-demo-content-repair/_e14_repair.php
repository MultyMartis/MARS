<?php
/**
 * FP-0002 V9-06E14 — Service tree + mini-description seed runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e14-service-admin-fields-service-tree-demo-content-repair';
if ( ! is_dir( $evidence_dir ) ) {
	mkdir( $evidence_dir, 0777, true );
}

const FP02_E14_ZAVISIMOSTI_PARENT = 73;
const FP02_E14_SPECIALISTAM_SERVICE = 76;
const FP02_E14_CANONICAL_SPECIALISTAM_PAGE = 15;

const FP02_E14_DEMO_LOREM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.';

function fp02e14_json_write( $path, $data ) {
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
}

function fp02e14_classify_v9_text( $text ) {
	if ( '' === trim( (string) $text ) ) {
		return 'EMPTY_DEFERRED';
	}
	if ( false !== stripos( $text, 'DEMO —' ) || false !== stripos( $text, 'Lorem ipsum' ) ) {
		return 'DEMO';
	}
	return 'EXACT_V9';
}

function fp02e14_get_v9_child_text( $slug ) {
	if ( ! function_exists( 'shpigovsky_get_v9_services_hub_child_copy' ) ) {
		return null;
	}
	$v9 = shpigovsky_get_v9_services_hub_child_copy( $slug );
	return is_array( $v9 ) ? $v9 : null;
}

function fp02e14_set_field( $post_id, $field, $value ) {
	$before = function_exists( 'get_field' ) ? get_field( $field, $post_id ) : get_post_meta( $post_id, $field, true );
	if ( function_exists( 'update_field' ) ) {
		update_field( $field, $value, $post_id );
	} else {
		update_post_meta( $post_id, $field, $value );
	}
	return $before;
}

function fp02e14_service_route( $post_id ) {
	$post = get_post( $post_id );
	if ( ! $post instanceof WP_Post ) {
		return '';
	}
	$url = get_permalink( $post );
	return is_string( $url ) ? $url : '';
}

function fp02e14_all_services() {
	return get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => array( 'publish', 'draft', 'trash', 'pending', 'private' ),
			'posts_per_page' => 100,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
		)
	);
}

$results = array(
	'generated_at' => gmdate( 'c' ),
	'mini_description_seed' => array(),
	'dependencies_tree' => array(),
	'new_leaves' => array(),
	'psych_eating' => array(),
	'db_write_count' => 0,
);

// --- 1. Trash specialistam service under zavisimosti (not canonical page) ---
$spec_before = get_post( FP02_E14_SPECIALISTAM_SERVICE );
$canon_page  = get_post( FP02_E14_CANONICAL_SPECIALISTAM_PAGE );
$spec_action = array(
	'service_id' => FP02_E14_SPECIALISTAM_SERVICE,
	'before_status' => $spec_before instanceof WP_Post ? $spec_before->post_status : 'missing',
	'canonical_page_id' => FP02_E14_CANONICAL_SPECIALISTAM_PAGE,
	'canonical_page_status' => $canon_page instanceof WP_Post ? $canon_page->post_status : 'missing',
);

if ( $spec_before instanceof WP_Post && 'trash' !== $spec_before->post_status ) {
	wp_trash_post( FP02_E14_SPECIALISTAM_SERVICE );
	$results['db_write_count']++;
	$spec_action['action'] = 'wp_trash_post';
} else {
	$spec_action['action'] = 'already_trashed_or_missing';
}
$spec_after = get_post( FP02_E14_SPECIALISTAM_SERVICE );
$spec_action['after_status'] = $spec_after instanceof WP_Post ? $spec_after->post_status : 'missing';
$results['dependencies_tree']['specialistam_service'] = $spec_action;

// --- 2. Create new dependency demo leaf pages ---
$new_leaves = array(
	array(
		'slug'  => 'narkoticheskaya-zavisimost',
		'title' => 'Наркотическая зависимость',
		'order' => 20,
	),
	array(
		'slug'  => 'lekarstvennaya-zavisimost',
		'title' => 'Лекарственная зависимость',
		'order' => 30,
	),
	array(
		'slug'  => 'povedencheskie-zavisimosti',
		'title' => 'Поведенческие зависимости',
		'order' => 40,
	),
);

$demo_leaf_hero = 'DEMO — демонстрационная страница услуги. Финальный контент будет согласован оператором. Материал не является медицинской рекомендацией.';
$demo_leaf_intro = 'DEMO — вводный блок страницы услуги. Техническое наполнение для проверки макета листовой страницы по аналогии с алкогольной программой.';
$demo_leaf_note  = 'DEMO — статус контента: демонстрационный шаблон, не финальный клинический текст.';

foreach ( $new_leaves as $leaf ) {
	$existing = get_posts(
		array(
			'post_type'      => 'service',
			'name'           => $leaf['slug'],
			'post_status'    => array( 'publish', 'draft', 'trash', 'pending', 'private' ),
			'posts_per_page' => 1,
		)
	);
	$post_id = 0;
	$created = false;
	if ( ! empty( $existing[0] ) && $existing[0] instanceof WP_Post ) {
		$post_id = (int) $existing[0]->ID;
		if ( 'trash' === $existing[0]->post_status ) {
			wp_untrash_post( $post_id );
			$results['db_write_count']++;
		}
		wp_update_post(
			array(
				'ID'          => $post_id,
				'post_parent' => FP02_E14_ZAVISIMOSTI_PARENT,
				'post_status' => 'publish',
				'menu_order'  => $leaf['order'],
				'post_title'  => $leaf['title'],
			)
		);
		$results['db_write_count']++;
	} else {
		$post_id = (int) wp_insert_post(
			array(
				'post_type'    => 'service',
				'post_status'  => 'publish',
				'post_parent'  => FP02_E14_ZAVISIMOSTI_PARENT,
				'post_name'    => $leaf['slug'],
				'post_title'   => $leaf['title'],
				'menu_order'   => $leaf['order'],
				'post_content' => '',
			),
			true
		);
		$created = ! is_wp_error( $post_id ) && $post_id > 0;
		if ( $created ) {
			$results['db_write_count']++;
		}
	}

	$v9 = fp02e14_get_v9_child_text( $leaf['slug'] );
	$mini = is_array( $v9 ) && '' !== $v9['text'] ? $v9['text'] : $demo_leaf_intro;

	fp02e14_set_field( $post_id, 'service_layout_variant', 'placeholder' );
	fp02e14_set_field( $post_id, 'hero_lead', $demo_leaf_hero );
	fp02e14_set_field( $post_id, 'intro_text', $demo_leaf_intro );
	fp02e14_set_field( $post_id, 'intro_note', $demo_leaf_note );
	fp02e14_set_field( $post_id, 'service_short_description', $mini );
	$results['db_write_count'] += 5;

	$results['new_leaves'][] = array(
		'id'             => $post_id,
		'slug'           => $leaf['slug'],
		'title'          => $leaf['title'],
		'route'          => fp02e14_service_route( $post_id ),
		'parent'         => FP02_E14_ZAVISIMOSTI_PARENT,
		'menu_order'     => $leaf['order'],
		'created'        => $created,
		'content_status' => 'DEMO',
		'layout'         => 'leaf',
	);
}

// --- 3. Reorder zavisimosti children: alcohol first, profilakticheskiy last ---
$order_map = array(
	74 => 10, // alcohol
	75 => 50, // profilakticheskiy analiz — bottom
);
foreach ( $new_leaves as $leaf ) {
	$p = get_page_by_path( 'zavisimosti/' . $leaf['slug'], OBJECT, 'service' );
	if ( $p instanceof WP_Post ) {
		$order_map[ (int) $p->ID ] = $leaf['order'];
	}
}
foreach ( $order_map as $id => $order ) {
	wp_update_post(
		array(
			'ID'         => $id,
			'menu_order' => $order,
		)
	);
	$results['db_write_count']++;
}
$results['dependencies_tree']['child_order'] = $order_map;

// --- 4. Psych / eating subdivision demo ---
$subdivision_demo = array(
	77 => 'psihicheskoe-zdorovie',
	84 => 'rasstroystva-pischevogo-povedeniya',
);

foreach ( $subdivision_demo as $post_id => $slug ) {
	$v9_group = function_exists( 'shpigovsky_get_v9_services_hub_group_copy' )
		? shpigovsky_get_v9_services_hub_group_copy( $slug )
		: null;

	$hero = is_array( $v9_group ) && '' !== $v9_group['intro']
		? $v9_group['intro']
		: 'DEMO — раздел «' . get_the_title( $post_id ) . '». Техническое наполнение subdivision-шаблона.';
	$intro = is_array( $v9_group ) && '' !== $v9_group['lead']
		? $v9_group['lead']
		: 'DEMO — вводный текст раздела для блока зависимостей/направлений. Финальный контент будет согласован оператором.';

	fp02e14_set_field( $post_id, 'service_layout_variant', 'subdivision' );
	fp02e14_set_field( $post_id, 'hero_lead', $hero );
	fp02e14_set_field( $post_id, 'intro_text', $intro );
	fp02e14_set_field( $post_id, 'intro_note', 'DEMO — subdivision demo content (E14). Не заявляется как exact V9 page port.' );

	$mini_v9 = fp02e14_get_v9_child_text( $slug );
	$mini    = ( is_array( $mini_v9 ) && '' !== $mini_v9['text'] )
		? $mini_v9['text']
		: shpigovsky_get_service_demo_mini_description_fallback( $slug );
	fp02e14_set_field( $post_id, 'service_short_description', $mini );

	$results['db_write_count'] += 5;
	$results['psych_eating'][] = array(
		'id'             => $post_id,
		'slug'           => $slug,
		'route'          => fp02e14_service_route( $post_id ),
		'layout_variant' => 'subdivision',
		'content_status' => 'DEMO',
		'hero_seeded'    => true,
		'intro_seeded'   => true,
	);
}

// --- 5. Seed mini-descriptions for all services ---
foreach ( fp02e14_all_services() as $service ) {
	if ( ! $service instanceof WP_Post ) {
		continue;
	}
	if ( 'trash' === $service->post_status ) {
		continue;
	}

	$before = function_exists( 'get_field' )
		? get_field( 'service_short_description', $service->ID )
		: get_post_meta( $service->ID, 'service_short_description', true );

	if ( is_array( $before ) || is_object( $before ) ) {
		$before = '';
	}
	$before = is_string( $before ) ? trim( $before ) : '';

	$status = 'PRESERVED';
	$after  = $before;

	if ( '' === $before ) {
		$v9 = fp02e14_get_v9_child_text( $service->post_name );
		if ( is_array( $v9 ) && '' !== trim( (string) $v9['text'] ) ) {
			$after  = trim( (string) $v9['text'] );
			$status = fp02e14_classify_v9_text( $after );
		} else {
			$after  = shpigovsky_get_service_demo_mini_description_fallback( $service->post_name );
			$status = 'DEMO';
		}
		fp02e14_set_field( $service->ID, 'service_short_description', $after );
		$results['db_write_count']++;
	}

	$layout = function_exists( 'get_field' )
		? get_field( 'service_layout_variant', $service->ID )
		: get_post_meta( $service->ID, 'service_layout_variant', true );

	$results['mini_description_seed'][] = array(
		'id'     => (int) $service->ID,
		'title'  => $service->post_title,
		'slug'   => $service->post_name,
		'parent' => (int) $service->post_parent,
		'before' => $before,
		'after'  => $after,
		'status' => $status,
		'layout' => is_string( $layout ) ? $layout : '',
	);
}

fp02e14_json_write( $evidence_dir . '/_e14_repair_runner_output.json', $results );

echo wp_json_encode( $results, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );

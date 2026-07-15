<?php
/**
 * FP-0002 V9-06E30 — services catalog seed + reorder runner.
 * TEMPORARY HELPER — validation evidence only.
 */
define( 'WP_USE_THEMES', false );

$root         = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e30-services-catalog-child-services-listing-controls';

require $root . '/wp-load.php';

if ( ! is_dir( $evidence_dir ) ) {
	mkdir( $evidence_dir, 0777, true );
}

const FP02_E30_PLACEHOLDER = 'Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.';
const FP02_E30_DEMO_MINI   = 'DEMO — краткое описание услуги для карточки на /uslugi/. Контент ожидает согласования оператором.';

function fp02e30_json( $name, $data ) {
	global $evidence_dir;
	$path = trailingslashit( $evidence_dir ) . $name;
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
	return $path;
}

function fp02e30_set_field( $post_id, $name, $value, $field_key = '' ) {
	if ( function_exists( 'update_field' ) && '' !== $field_key ) {
		update_field( $field_key, $value, $post_id );
	} else {
		update_post_meta( $post_id, $name, $value );
	}
	if ( '' !== $field_key ) {
		update_post_meta( $post_id, '_' . $name, $field_key );
	}
}

function fp02e30_get_by_slug( $slug ) {
	$posts = get_posts(
		array(
			'name'           => $slug,
			'post_type'      => 'service',
			'post_status'    => array( 'publish', 'draft', 'private', 'trash' ),
			'posts_per_page' => 5,
		)
	);
	return $posts;
}

function fp02e30_ensure_service( array $spec, $parent_id ) {
	$slug     = $spec['slug'];
	$existing = fp02e30_get_by_slug( $slug );
	$active   = null;
	$trashed  = array();

	foreach ( $existing as $post ) {
		if ( 'trash' === $post->post_status ) {
			$trashed[] = (int) $post->ID;
			continue;
		}
		if ( null === $active ) {
			$active = $post;
		}
	}

	$result = array(
		'title'           => $spec['title'],
		'slug'            => $slug,
		'parent_id'       => (int) $parent_id,
		'trashed_matches' => $trashed,
		'demo_source'     => $spec['demo_source'],
	);

	if ( $active instanceof WP_Post ) {
		$post_id = (int) $active->ID;
		wp_update_post(
			array(
				'ID'          => $post_id,
				'post_title'  => $spec['title'],
				'post_name'   => $slug,
				'post_parent' => (int) $parent_id,
				'post_status' => 'publish',
				'menu_order'  => (int) $spec['menu_order'],
			)
		);
		$result['action'] = 'UPDATED';
		$result['id']     = $post_id;
	} else {
		$post_id = wp_insert_post(
			array(
				'post_type'    => 'service',
				'post_status'  => 'publish',
				'post_title'   => $spec['title'],
				'post_name'    => $slug,
				'post_parent'  => (int) $parent_id,
				'menu_order'   => (int) $spec['menu_order'],
				'post_content' => '<!-- wp:paragraph --><p>' . esc_html( FP02_E30_PLACEHOLDER ) . '</p><!-- /wp:paragraph -->',
			),
			true
		);
		if ( is_wp_error( $post_id ) ) {
			$result['action'] = 'ERROR';
			$result['error']  = $post_id->get_error_message();
			return $result;
		}
		$result['action'] = 'CREATED';
		$result['id']     = (int) $post_id;
	}

	fp02e30_set_field( $result['id'], 'service_layout_variant', 'placeholder', 'field_fp02_service_layout_variant' );
	fp02e30_set_field( $result['id'], 'intro_text', FP02_E30_PLACEHOLDER, 'field_fp02_intro_text_service' );
	fp02e30_set_field( $result['id'], 'service_short_description', FP02_E30_DEMO_MINI, 'field_fp02_service_short_description' );
	fp02e30_set_field( $result['id'], 'service_show_in_text_list', (int) $spec['text_list'], 'field_fp02_service_show_in_text_list' );
	fp02e30_set_field( $result['id'], 'service_show_in_slider', (int) $spec['slider'], 'field_fp02_service_show_in_slider' );

	update_post_meta( $result['id'], 'created_by_phase', 'V9-06E30' );
	update_post_meta( $result['id'], 'content_source', 'demo_placeholder' );

	$result['final_url'] = get_permalink( $result['id'] );
	$result['text_list'] = (int) $spec['text_list'];
	$result['slider']    = (int) $spec['slider'];
	$result['result']    = 'OK';

	return $result;
}

$parents = array(
	'zavisimosti'                        => get_page_by_path( 'zavisimosti', OBJECT, 'service' ),
	'psihicheskoe-zdorovie'              => get_page_by_path( 'psihicheskoe-zdorovie', OBJECT, 'service' ),
	'rasstroystva-pischevogo-povedeniya' => get_page_by_path( 'rasstroystva-pischevogo-povedeniya', OBJECT, 'service' ),
	'genotipirovanie'                    => get_page_by_path( 'genotipirovanie', OBJECT, 'service' ),
);

$reorder = array();
if ( $parents['genotipirovanie'] instanceof WP_Post ) {
	$before = (int) $parents['genotipirovanie']->menu_order;
	wp_update_post(
		array(
			'ID'         => (int) $parents['genotipirovanie']->ID,
			'menu_order' => 200,
		)
	);
	$reorder[] = array(
		'id'           => (int) $parents['genotipirovanie']->ID,
		'slug'         => 'genotipirovanie',
		'menu_before'  => $before,
		'menu_after'   => 200,
		'action'       => 'REORDERED_LAST',
	);
}

$new_specs = array(
	array(
		'title'       => 'Лечение интернет зависимости',
		'slug'        => 'lechenie-internet-zavisimosti',
		'parent'      => 'zavisimosti',
		'menu_order'  => 60,
		'text_list'   => 0,
		'slider'      => 1,
		'demo_source' => 'placeholder_same_level_as_leaf_under_zavisimosti',
	),
	array(
		'title'       => 'Компьютерная зависимость',
		'slug'        => 'kompyuternaya-zavisimost',
		'parent'      => 'zavisimosti',
		'menu_order'  => 61,
		'text_list'   => 0,
		'slider'      => 1,
		'demo_source' => 'placeholder_same_level_as_leaf_under_zavisimosti',
	),
	array(
		'title'       => 'Лечение опиумной зависимости',
		'slug'        => 'lechenie-opiumnoy-zavisimosti',
		'parent'      => 'zavisimosti',
		'menu_order'  => 62,
		'text_list'   => 0,
		'slider'      => 1,
		'demo_source' => 'placeholder_same_level_as_leaf_under_zavisimosti',
	),
	array(
		'title'       => 'Хроническая усталость',
		'slug'        => 'hronicheskaya-ustalost',
		'parent'      => 'psihicheskoe-zdorovie',
		'menu_order'  => 120,
		'text_list'   => 0,
		'slider'      => 1,
		'demo_source' => 'placeholder_same_level_as_leaf_under_psihicheskoe-zdorovie',
	),
	array(
		'title'       => 'Стресс',
		'slug'        => 'stress',
		'parent'      => 'psihicheskoe-zdorovie',
		'menu_order'  => 121,
		'text_list'   => 0,
		'slider'      => 1,
		'demo_source' => 'placeholder_same_level_as_leaf_under_psihicheskoe-zdorovie',
	),
	array(
		'title'       => 'Нарциссизм',
		'slug'        => 'nartsissizm',
		'parent'      => 'psihicheskoe-zdorovie',
		'menu_order'  => 122,
		'text_list'   => 0,
		'slider'      => 1,
		'demo_source' => 'placeholder_same_level_as_leaf_under_psihicheskoe-zdorovie',
	),
);

$created = array();
foreach ( $new_specs as $spec ) {
	$parent = isset( $parents[ $spec['parent'] ] ) ? $parents[ $spec['parent'] ] : null;
	if ( ! $parent instanceof WP_Post ) {
		$created[] = array(
			'title'  => $spec['title'],
			'action' => 'ERROR',
			'error'  => 'parent_missing:' . $spec['parent'],
		);
		continue;
	}
	$created[] = fp02e30_ensure_service( $spec, (int) $parent->ID );
}

// Seed display flags for all published services.
$all = get_posts(
	array(
		'post_type'      => 'service',
		'post_status'    => 'publish',
		'posts_per_page' => 200,
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);

$slider_slugs = array(
	'lechenie-internet-zavisimosti' => true,
	'kompyuternaya-zavisimost'      => true,
	'lechenie-opiumnoy-zavisimosti' => true,
	'hronicheskaya-ustalost'        => true,
	'stress'                        => true,
	'nartsissizm'                   => true,
);

$seeded_flags = array();
foreach ( $all as $service ) {
	$is_slider = isset( $slider_slugs[ $service->post_name ] );
	$text_list = $is_slider ? 0 : 1;
	$slider    = $is_slider ? 1 : 0;

	// Top-level category parents stay out of child text-list cards when they have children,
	// but flags still default text_list=1 for admin clarity; render uses children first.
	fp02e30_set_field( $service->ID, 'service_show_in_text_list', $text_list, 'field_fp02_service_show_in_text_list' );
	fp02e30_set_field( $service->ID, 'service_show_in_slider', $slider, 'field_fp02_service_show_in_slider' );

	$seeded_flags[] = array(
		'id'        => (int) $service->ID,
		'slug'      => $service->post_name,
		'text_list' => $text_list,
		'slider'    => $slider,
	);
}

flush_rewrite_rules( false );

$route_inventory = array();
foreach ( $all as $service ) {
	$route_inventory[] = array(
		'id'     => (int) $service->ID,
		'title'  => get_the_title( $service ),
		'slug'   => $service->post_name,
		'parent' => (int) $service->post_parent,
		'url'    => get_permalink( $service ),
		'menu'   => (int) $service->menu_order,
	);
}

// Refresh after mutations.
$groups = function_exists( 'shpigovsky_get_services_hub_groups' ) ? shpigovsky_get_services_hub_groups() : array();
$group_summary = array();
foreach ( $groups as $g ) {
	$group_summary[] = array(
		'slug'           => isset( $g['slug'] ) ? $g['slug'] : '',
		'icon'           => isset( $g['icon'] ) ? $g['icon'] : '',
		'title'          => isset( $g['title'] ) ? $g['title'] : '',
		'text_count'     => isset( $g['children'] ) ? count( $g['children'] ) : 0,
		'gallery_count'  => isset( $g['gallery'] ) ? count( $g['gallery'] ) : 0,
		'gallery_captions' => array_map(
			static function ( $item ) {
				return isset( $item['caption'] ) ? $item['caption'] : '';
			},
			isset( $g['gallery'] ) && is_array( $g['gallery'] ) ? $g['gallery'] : array()
		),
	);
}

$note_existing_internet = array(
	'existing_slug' => 'internet-zavisimost',
	'existing_path' => '/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/',
	'note'          => 'Kept intact. New gallery service lechenie-internet-zavisimosti is a separate slider card under zavisimosti.',
);

fp02e30_json(
	'e30-seed-result.json',
	array(
		'reorder'                 => $reorder,
		'created_or_updated'      => $created,
		'seeded_flags_count'      => count( $seeded_flags ),
		'seeded_flags'            => $seeded_flags,
		'group_summary'           => $group_summary,
		'existing_internet_note'  => $note_existing_internet,
		'db_writes_estimate'      => count( $created ) + count( $seeded_flags ) + count( $reorder ),
	)
);

fp02e30_json( 'e30-route-inventory-after.json', $route_inventory );

echo wp_json_encode(
	array(
		'ok'      => true,
		'created' => $created,
		'reorder' => $reorder,
		'groups'  => $group_summary,
	),
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
) . PHP_EOL;

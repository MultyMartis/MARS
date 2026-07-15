<?php
/**
 * V9-06E34 — create/reuse specialist child pages + seed meta from slider.
 */
require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider';
@mkdir( $evidence, 0777, true );

$GENERIC = 'page-templates/generic.php';
$parent  = get_page_by_path( 'specyalisty' );
$out     = array(
	'db_writes' => 0,
	'actions'   => array(),
	'parent_id' => 0,
	'errors'    => array(),
);

if ( ! ( $parent instanceof WP_Post ) ) {
	$out['errors'][] = 'Parent /specyalisty/ not found';
	file_put_contents( $evidence . '/e34-mutation-result.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
	fwrite( STDERR, "FAIL parent missing\n" );
	exit( 1 );
}

$out['parent_id'] = (int) $parent->ID;

/**
 * Unique specialists from current slider (ACF if present else static), deduped by normalized name.
 *
 * @return array<int, array{name:string,role:string,image:string,width:int,height:int,slug_hint:string,match_slugs:array<int,string>,match_titles:array<int,string>}>
 */
function fp02_e34_unique_specialists() {
	$rows = array();
	if ( function_exists( 'get_field' ) && function_exists( 'shpigovsky_get_specialists_block_context' ) ) {
		$acf = get_field( 'specialists_items', shpigovsky_get_specialists_block_context() );
		if ( is_array( $acf ) && ! empty( $acf ) ) {
			foreach ( $acf as $row ) {
				$rows[] = array(
					'name'   => isset( $row['specialist_name'] ) ? trim( (string) $row['specialist_name'] ) : '',
					'role'   => isset( $row['specialist_role'] ) ? trim( (string) $row['specialist_role'] ) : '',
					'image'  => isset( $row['specialist_photo_asset'] ) ? trim( (string) $row['specialist_photo_asset'] ) : '',
					'width'  => isset( $row['specialist_photo_width'] ) ? (int) $row['specialist_photo_width'] : 615,
					'height' => isset( $row['specialist_photo_height'] ) ? (int) $row['specialist_photo_height'] : 605,
				);
			}
		}
	}
	if ( empty( $rows ) && function_exists( 'shpigovsky_get_v9_specialists_cards' ) ) {
		foreach ( shpigovsky_get_v9_specialists_cards() as $row ) {
			$rows[] = array(
				'name'   => isset( $row['name'] ) ? trim( (string) $row['name'] ) : '',
				'role'   => isset( $row['role'] ) ? trim( (string) $row['role'] ) : '',
				'image'  => isset( $row['image'] ) ? trim( (string) $row['image'] ) : '',
				'width'  => isset( $row['width'] ) ? (int) $row['width'] : 615,
				'height' => isset( $row['height'] ) ? (int) $row['height'] : 605,
			);
		}
	}

	$map = array(
		array(
			'keys'         => array( 'шпиговский', 'shipovsky', 'sergey' ),
			'slug_hint'    => 'shipovsky',
			'match_slugs'  => array( 'shipovsky' ),
			'match_titles' => array( 'сергей шпиговский', 'сергей юрьевич шпиговский' ),
		),
		array(
			'keys'         => array( 'казаков', 'kazakov', 'maxim' ),
			'slug_hint'    => 'kazakov',
			'match_slugs'  => array( 'kazakov' ),
			'match_titles' => array( 'казаков', 'максим михайлович казаков' ),
		),
		array(
			'keys'         => array( 'костюк', 'kostyuk', 'darya', 'дарья' ),
			'slug_hint'    => 'kostyuk',
			'match_slugs'  => array( 'kostyuk' ),
			'match_titles' => array( 'костюк', 'дарья владимировна костюк' ),
		),
		array(
			'keys'         => array( 'шапигузова', 'shapiguzova', 'татьяна' ),
			'slug_hint'    => 'shapiguzova',
			'match_slugs'  => array( 'shapiguzova', 'tatyana-shapiguzova' ),
			'match_titles' => array( 'шапигузова татьяна андреевна', 'татьяна андреевна шапигузова' ),
		),
	);

	$unique = array();
	$seen   = array();
	foreach ( $rows as $row ) {
		$name = $row['name'];
		if ( '' === $name ) {
			continue;
		}
		$norm = mb_strtolower( $name );
		$hint = '';
		$meta = null;
		foreach ( $map as $m ) {
			foreach ( $m['keys'] as $k ) {
				if ( false !== mb_strpos( $norm, $k ) ) {
					$hint = $m['slug_hint'];
					$meta = $m;
					break 2;
				}
			}
		}
		if ( '' === $hint ) {
			$hint = sanitize_title( $name );
			$meta = array(
				'slug_hint'    => $hint,
				'match_slugs'  => array( $hint ),
				'match_titles' => array( $norm ),
			);
		}
		if ( isset( $seen[ $hint ] ) ) {
			continue; // dedupe Sergey duplicate etc.
		}
		$seen[ $hint ] = true;
		$role          = html_entity_decode( str_replace( '&nbsp;', ' ', $row['role'] ), ENT_QUOTES | ENT_HTML5, 'UTF-8' );
		$unique[]      = array(
			'name'         => $name,
			'role'         => trim( wp_strip_all_tags( $role ) ),
			'image'        => $row['image'],
			'width'        => $row['width'] > 0 ? $row['width'] : 615,
			'height'       => $row['height'] > 0 ? $row['height'] : 605,
			'slug_hint'    => $meta['slug_hint'],
			'match_slugs'  => $meta['match_slugs'],
			'match_titles' => $meta['match_titles'],
		);
	}

	return $unique;
}

/**
 * Find existing child page match.
 *
 * @param int                  $parent_id Parent ID.
 * @param array<string,mixed>  $spec Specialist row.
 * @return WP_Post|null
 */
function fp02_e34_find_child( $parent_id, $spec ) {
	$children = get_posts(
		array(
			'post_type'      => 'page',
			'post_parent'    => $parent_id,
			'post_status'    => array( 'publish', 'draft', 'private', 'pending' ),
			'numberposts'    => 100,
		)
	);
	foreach ( $children as $child ) {
		$slug  = mb_strtolower( $child->post_name );
		$title = mb_strtolower( trim( $child->post_title ) );
		if ( in_array( $slug, $spec['match_slugs'], true ) ) {
			return $child;
		}
		if ( in_array( $title, $spec['match_titles'], true ) ) {
			return $child;
		}
		foreach ( $spec['match_titles'] as $t ) {
			if ( '' !== $t && ( false !== mb_strpos( $title, $t ) || false !== mb_strpos( $t, $title ) ) ) {
				return $child;
			}
		}
	}
	return null;
}

/**
 * Ensure featured image from theme asset (reuse attachment by filename if possible).
 *
 * @param int    $page_id Page ID.
 * @param string $rel     Theme-relative asset path.
 * @return int Attachment ID or 0.
 */
function fp02_e34_ensure_featured( $page_id, $rel ) {
	if ( '' === $rel ) {
		return 0;
	}
	$theme_file = get_template_directory() . '/assets/' . ltrim( str_replace( '\\', '/', $rel ), '/' );
	if ( ! is_readable( $theme_file ) ) {
		return 0;
	}
	$basename = basename( $theme_file );
	$existing = get_posts(
		array(
			'post_type'      => 'attachment',
			'post_status'    => 'inherit',
			'numberposts'    => 5,
			'meta_query'     => array(
				array(
					'key'     => '_wp_attached_file',
					'value'   => $basename,
					'compare' => 'LIKE',
				),
			),
		)
	);
	$att_id = 0;
	if ( ! empty( $existing ) ) {
		$att_id = (int) $existing[0]->ID;
	} else {
		require_once ABSPATH . 'wp-admin/includes/file.php';
		require_once ABSPATH . 'wp-admin/includes/media.php';
		require_once ABSPATH . 'wp-admin/includes/image.php';
		$tmp = wp_tempnam( $basename );
		if ( ! $tmp || ! copy( $theme_file, $tmp ) ) {
			return 0;
		}
		$file_array = array(
			'name'     => $basename,
			'tmp_name' => $tmp,
		);
		$att_id = media_handle_sideload( $file_array, $page_id );
		if ( is_wp_error( $att_id ) ) {
			@unlink( $tmp );
			return 0;
		}
	}
	if ( $att_id > 0 && (int) get_post_thumbnail_id( $page_id ) !== $att_id ) {
		set_post_thumbnail( $page_id, $att_id );
	}
	return (int) $att_id;
}

$specialists = fp02_e34_unique_specialists();
$order       = 10;
foreach ( $specialists as $spec ) {
	$existing = fp02_e34_find_child( (int) $parent->ID, $spec );
	$role_html = esc_html( $spec['role'] );
	$content   = '<!-- wp:paragraph --><p><strong>' . esc_html( $spec['name'] ) . '</strong></p><!-- /wp:paragraph -->'
		. '<!-- wp:paragraph --><p>' . $role_html . '</p><!-- /wp:paragraph -->'
		. '<!-- wp:paragraph --><p>Раздел находится в подготовке. Здесь будет опубликована расширенная информация о специалисте.</p><!-- /wp:paragraph -->';

	if ( $existing instanceof WP_Post ) {
		$update = array(
			'ID'           => (int) $existing->ID,
			'post_title'   => $spec['name'],
			'post_excerpt' => $spec['role'],
			'post_content' => $content,
			'post_status'  => 'publish',
			'post_parent'  => (int) $parent->ID,
			'menu_order'   => $order,
		);
		// Preserve existing stable slug (shipovsky etc.).
		$uid = wp_update_post( $update, true );
		if ( is_wp_error( $uid ) ) {
			$out['errors'][] = $uid->get_error_message();
			continue;
		}
		$out['db_writes']++;
		update_post_meta( (int) $existing->ID, '_wp_page_template', $GENERIC );
		update_post_meta( (int) $existing->ID, '_shpigovsky_specialist_role', $spec['role'] );
		update_post_meta( (int) $existing->ID, '_shpigovsky_specialist_photo_asset', $spec['image'] );
		update_post_meta( (int) $existing->ID, '_shpigovsky_specialist_photo_width', $spec['width'] );
		update_post_meta( (int) $existing->ID, '_shpigovsky_specialist_photo_height', $spec['height'] );
		$out['db_writes'] += 5;
		$thumb = fp02_e34_ensure_featured( (int) $existing->ID, $spec['image'] );
		if ( $thumb > 0 ) {
			$out['db_writes']++;
		}
		$out['actions'][] = array(
			'specialist' => $spec['name'],
			'action'     => 'UPDATED',
			'page_id'    => (int) $existing->ID,
			'slug'       => $existing->post_name,
			'url'        => get_permalink( $existing->ID ),
			'menu_order' => $order,
			'thumb'      => $thumb,
		);
	} else {
		$new_id = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_title'   => $spec['name'],
				'post_name'    => $spec['slug_hint'],
				'post_excerpt' => $spec['role'],
				'post_content' => $content,
				'post_status'  => 'publish',
				'post_parent'  => (int) $parent->ID,
				'menu_order'   => $order,
			),
			true
		);
		if ( is_wp_error( $new_id ) ) {
			$out['errors'][] = $new_id->get_error_message();
			continue;
		}
		$out['db_writes']++;
		update_post_meta( (int) $new_id, '_wp_page_template', $GENERIC );
		update_post_meta( (int) $new_id, '_shpigovsky_specialist_role', $spec['role'] );
		update_post_meta( (int) $new_id, '_shpigovsky_specialist_photo_asset', $spec['image'] );
		update_post_meta( (int) $new_id, '_shpigovsky_specialist_photo_width', $spec['width'] );
		update_post_meta( (int) $new_id, '_shpigovsky_specialist_photo_height', $spec['height'] );
		$out['db_writes'] += 5;
		$thumb = fp02_e34_ensure_featured( (int) $new_id, $spec['image'] );
		if ( $thumb > 0 ) {
			$out['db_writes']++;
		}
		$out['actions'][] = array(
			'specialist' => $spec['name'],
			'action'     => 'CREATED',
			'page_id'    => (int) $new_id,
			'slug'       => get_post_field( 'post_name', $new_id ),
			'url'        => get_permalink( $new_id ),
			'menu_order' => $order,
			'thumb'      => $thumb,
		);
	}
	$order += 10;
}

// Point "all specialists" link to /specyalisty/ when empty or pointing to o-centre.
if ( function_exists( 'update_field' ) ) {
	$ctx = shpigovsky_get_specialists_block_context();
	$cur = function_exists( 'get_field' ) ? (string) get_field( 'specialists_all_link_url', $ctx ) : '';
	$target = get_permalink( $parent->ID );
	if ( '' === trim( $cur ) || false !== stripos( $cur, '/o-centre' ) ) {
		update_field( 'specialists_all_link_url', $target, $ctx );
		$out['db_writes']++;
		$out['actions'][] = array(
			'specialist' => '(block option)',
			'action'     => 'UPDATED_ALL_LINK',
			'url'        => $target,
			'previous'   => $cur,
		);
	}
}

file_put_contents( $evidence . '/e34-mutation-result.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
echo 'MUTATION_OK writes=' . $out['db_writes'] . ' actions=' . count( $out['actions'] ) . ' errors=' . count( $out['errors'] ) . PHP_EOL;

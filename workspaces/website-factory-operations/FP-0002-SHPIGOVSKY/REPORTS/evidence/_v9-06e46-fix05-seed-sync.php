<?php
/**
 * V9-06E46-FIX05 — sync ACF JSON, ensure corridor media, seed demo into empty ACF fields.
 *
 * @package FP0002
 */

declare(strict_types=1);

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require $wp_load;

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$src_root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content';

if ( ! function_exists( 'update_field' ) || ! class_exists( '\\Shpigovsky\\Core\\Fields\\ServiceSectionParity' ) ) {
	fwrite( STDERR, "ACF or ServiceSectionParity missing\n" );
	exit( 1 );
}

/**
 * Copy source file to runtime if different.
 *
 * @param string $src Source path.
 * @param string $dst Dest path.
 * @return array{src:string,dst:string,copied:bool,match:bool,hash_src:string,hash_dst:string}
 */
function fp02_fix05_sync_file( string $src, string $dst ): array {
	$hash_src = is_file( $src ) ? md5_file( $src ) : '';
	$hash_dst = is_file( $dst ) ? md5_file( $dst ) : '';
	$copied   = false;
	if ( $hash_src && $hash_src !== $hash_dst ) {
		$dir = dirname( $dst );
		if ( ! is_dir( $dir ) ) {
			wp_mkdir_p( $dir );
		}
		copy( $src, $dst );
		$copied   = true;
		$hash_dst = md5_file( $dst );
	}
	return array(
		'src'      => $src,
		'dst'      => $dst,
		'copied'   => $copied,
		'match'    => ( $hash_src && $hash_src === $hash_dst ),
		'hash_src' => $hash_src,
		'hash_dst' => $hash_dst,
	);
}

$sync = array(
	fp02_fix05_sync_file(
		$src_root . '/plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php',
		$rt_root . '/plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php'
	),
	fp02_fix05_sync_file(
		$src_root . '/theme/shpigovsky/inc/service-section-helpers.php',
		$rt_root . '/themes/shpigovsky/inc/service-section-helpers.php'
	),
	fp02_fix05_sync_file(
		$src_root . '/theme/shpigovsky/template-parts/service/team-stats.php',
		$rt_root . '/themes/shpigovsky/template-parts/service/team-stats.php'
	),
);

// Export ACF JSON from PHP group definition.
$group = \Shpigovsky\Core\Fields\ServiceSectionParity::group();
$json  = wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
if ( ! is_string( $json ) ) {
	fwrite( STDERR, "JSON encode failed\n" );
	exit( 1 );
}
$json .= "\n";
$json_src = $src_root . '/acf-json/group_fp02_service_section_parity.json';
$json_rt  = $rt_root . '/acf-json/group_fp02_service_section_parity.json';
file_put_contents( $json_src, $json );
file_put_contents( $json_rt, $json );
$sync[] = array(
	'src'      => $json_src,
	'dst'      => $json_rt,
	'copied'   => true,
	'match'    => md5_file( $json_src ) === md5_file( $json_rt ),
	'hash_src' => md5_file( $json_src ),
	'hash_dst' => md5_file( $json_rt ),
);

// Flush ACF local field cache if available.
if ( function_exists( 'acf_get_store' ) ) {
	$store = acf_get_store( 'local-fields' );
	if ( $store && method_exists( $store, 'reset' ) ) {
		$store->reset();
	}
}
if ( function_exists( 'acf_get_store' ) ) {
	$store = acf_get_store( 'local-groups' );
	if ( $store && method_exists( $store, 'reset' ) ) {
		$store->reset();
	}
}

/**
 * Ensure corridor attachment exists (copy theme asset into uploads once).
 *
 * @return array{id:int,created:bool,url:string,note:string}
 */
function fp02_fix05_ensure_corridor_attachment(): array {
	global $wpdb;
	$existing = $wpdb->get_var(
		"SELECT p.ID FROM {$wpdb->posts} p
		 INNER JOIN {$wpdb->postmeta} pm ON pm.post_id = p.ID AND pm.meta_key = '_wp_attached_file'
		 WHERE p.post_type = 'attachment' AND pm.meta_value LIKE '%shpigovsky-interior-corridor%'
		 ORDER BY p.ID DESC LIMIT 1"
	);
	if ( $existing ) {
		$id = (int) $existing;
		return array(
			'id'      => $id,
			'created' => false,
			'url'     => (string) wp_get_attachment_url( $id ),
			'note'    => 'reused existing',
		);
	}

	$theme_file = get_template_directory() . '/assets/img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp';
	if ( ! is_file( $theme_file ) ) {
		return array( 'id' => 0, 'created' => false, 'url' => '', 'note' => 'theme file missing' );
	}

	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/image.php';

	$upload_dir = wp_upload_dir();
	$dest_dir   = trailingslashit( $upload_dir['path'] );
	$dest_file  = $dest_dir . 'shpigovsky-interior-corridor.webp';
	if ( ! is_file( $dest_file ) ) {
		copy( $theme_file, $dest_file );
	}

	$filetype = wp_check_filetype( $dest_file, null );
	$attachment = array(
		'post_mime_type' => $filetype['type'] ?: 'image/webp',
		'post_title'     => 'Шпиговский — интерьер коридора (section)',
		'post_content'   => '',
		'post_status'    => 'inherit',
	);
	$attach_id = wp_insert_attachment( $attachment, $dest_file, 0 );
	if ( is_wp_error( $attach_id ) || ! $attach_id ) {
		return array( 'id' => 0, 'created' => false, 'url' => '', 'note' => 'insert failed' );
	}
	$meta = wp_generate_attachment_metadata( $attach_id, $dest_file );
	wp_update_attachment_metadata( $attach_id, $meta );
	update_post_meta( $attach_id, '_wp_attachment_image_alt', 'Интерьер клиники — коридор с картинами' );

	return array(
		'id'      => (int) $attach_id,
		'created' => true,
		'url'     => (string) wp_get_attachment_url( $attach_id ),
		'note'    => 'created from theme asset copy',
	);
}

$corridor_media = fp02_fix05_ensure_corridor_attachment();
$team_id        = (int) get_post_meta( 4, 'home_staff_photo_image', true );
if ( $team_id <= 0 ) {
	$team_id = 1238;
}
$landscape_id = (int) get_post_meta( 4, 'home_clinic_landscape_image', true );
if ( $landscape_id <= 0 ) {
	$landscape_id = 1239;
}

/**
 * Whether a scalar field is empty.
 *
 * @param mixed $v Value.
 * @return bool
 */
function fp02_fix05_is_empty_scalar( $v ): bool {
	if ( null === $v || false === $v ) {
		return true;
	}
	if ( is_string( $v ) ) {
		return '' === trim( $v );
	}
	if ( is_numeric( $v ) ) {
		return (int) $v === 0;
	}
	return false;
}

/**
 * Whether repeater is empty/unusable.
 *
 * @param mixed $v Value.
 * @return bool
 */
function fp02_fix05_is_empty_repeater( $v ): bool {
	if ( null === $v || false === $v || '' === $v ) {
		return true;
	}
	if ( is_numeric( $v ) && (int) $v === 0 ) {
		return true;
	}
	if ( ! is_array( $v ) ) {
		return true;
	}
	return ! shpigovsky_has_meaningful_repeater_rows( $v );
}

/**
 * Seed field only when empty.
 *
 * @param int    $post_id Post ID.
 * @param string $field Field name.
 * @param mixed  $value Value.
 * @param string $source Source label.
 * @param array  $log Log by ref.
 * @return bool Seeded.
 */
function fp02_fix05_seed_if_empty( int $post_id, string $field, $value, string $source, array &$log ): bool {
	$before = function_exists( 'get_field' ) ? get_field( $field, $post_id ) : get_post_meta( $post_id, $field, true );
	$is_image = in_array( $field, array( 'section_team_image', 'section_corridor_image', 'section_clinic_landscape_image', 'section_approach_staff_image', 'section_approach_corridor_image' ), true );
	$is_rep   = in_array( $field, array( 'section_nature_text_blocks', 'section_nature_cards', 'section_program_intro_items', 'section_stages_items', 'section_stages_support_items', 'section_approach_cards' ), true );

	$empty = $is_rep ? fp02_fix05_is_empty_repeater( $before ) : ( $is_image ? ( ! is_array( $before ) && (int) ( is_numeric( $before ) ? $before : 0 ) <= 0 && empty( $before ) ) : fp02_fix05_is_empty_scalar( $before ) );

	if ( ! $empty ) {
		$log[] = array(
			'post_id'   => $post_id,
			'field'     => $field,
			'action'    => 'preserved',
			'before'    => is_scalar( $before ) ? $before : 'non-scalar',
			'seeded'    => null,
			'source'    => '',
			'result'    => 'SKIP_EXISTING',
		);
		return false;
	}

	update_field( $field, $value, $post_id );
	$after = function_exists( 'get_field' ) ? get_field( $field, $post_id ) : get_post_meta( $post_id, $field, true );
	$log[] = array(
		'post_id'   => $post_id,
		'field'     => $field,
		'action'    => 'seeded',
		'before'    => is_scalar( $before ) ? $before : ( empty( $before ) ? 'empty' : 'non-scalar-empty' ),
		'seeded'    => is_scalar( $value ) ? $value : ( is_array( $value ) ? 'array:' . count( $value ) : gettype( $value ) ),
		'source'    => $source,
		'result'    => 'SEEDED',
		'after_ok'  => ! fp02_fix05_is_empty_scalar( is_scalar( $after ) ? $after : ( is_array( $after ) ? 'x' : '' ) ) || ( is_array( $after ) && ! empty( $after ) ) || ( is_numeric( $after ) && (int) $after > 0 ) || ( is_array( $after ) && isset( $after['ID'] ) ),
	);
	return true;
}

$demo_nature_blocks = shpigovsky_get_section_nature_text_blocks_fallback();
$demo_nature_cards  = shpigovsky_get_section_nature_fallback_cards();
$demo_intros        = array();
foreach ( shpigovsky_get_section_program_intro_demo_fallback() as $t ) {
	$demo_intros[] = array( 'text' => $t );
}
$demo_stages        = shpigovsky_get_section_stages_items_fallback();
foreach ( $demo_stages as &$st ) {
	$st['enabled'] = 1;
}
unset( $st );
$demo_support = array();
foreach ( shpigovsky_get_section_stages_support_fallback() as $t ) {
	$demo_support[] = array( 'text' => $t );
}
$demo_approach_cards = shpigovsky_get_section_approach_fallback_cards();

$section_posts = array( 73, 77, 84 );
$seed_log      = array();
$db_writes     = 0;

foreach ( $section_posts as $pid ) {
	// Migrate legacy alt/image meta if new keys empty.
	$legacy_map = array(
		'section_approach_corridor_alt'   => 'section_corridor_image_alt',
		'section_approach_staff_alt'      => 'section_team_image_alt',
		'section_approach_corridor_image' => 'section_corridor_image',
		'section_approach_staff_image'    => 'section_team_image',
	);
	foreach ( $legacy_map as $old => $new ) {
		$new_val = get_field( $new, $pid );
		$old_val = get_field( $old, $pid );
		$new_empty = fp02_fix05_is_empty_scalar( is_array( $new_val ) ? ( $new_val['ID'] ?? '' ) : $new_val ) && empty( $new_val );
		if ( $new_empty && ! empty( $old_val ) ) {
			$seed_val = is_array( $old_val ) && isset( $old_val['ID'] ) ? (int) $old_val['ID'] : $old_val;
			update_field( $new, $seed_val, $pid );
			$db_writes++;
			$seed_log[] = array(
				'post_id' => $pid,
				'field'   => $new,
				'action'  => 'migrated_from_legacy',
				'before'  => 'empty',
				'seeded'  => is_scalar( $seed_val ) ? $seed_val : 'array',
				'source'  => $old,
				'result'  => 'MIGRATED',
			);
		}
	}

	// Page-specific nature blocks when legacy exists (e.g. #73).
	$nature_seed = $demo_nature_blocks;
	if ( function_exists( 'shpigovsky_get_section_nature_text_blocks' ) ) {
		$resolved = shpigovsky_get_section_nature_text_blocks( $pid );
		if ( ! empty( $resolved ) ) {
			$nature_seed = $resolved;
		}
	}
	$stages_seed = $demo_stages;
	if ( function_exists( 'shpigovsky_get_section_stages_items' ) ) {
		$resolved_st = shpigovsky_get_section_stages_items( $pid );
		if ( ! empty( $resolved_st ) ) {
			$stages_seed = array();
			foreach ( $resolved_st as $row ) {
				$stages_seed[] = array(
					'title'   => $row['title'],
					'text'    => $row['text'],
					'enabled' => 1,
				);
			}
		}
	}

	$scalars = array(
		'section_dependencies_heading' => array( shpigovsky_get_service_subdivision_dependencies_heading(), 'template_emergency_heading' ),
		'section_dependencies_lead'    => array( shpigovsky_get_service_subdivision_dependencies_lead_fallback(), 'template_emergency_lead' ),
		'section_dependencies_footer'  => array( shpigovsky_get_service_subdivision_dependencies_footer_fallback(), 'template_emergency_footer' ),
		'section_nature_heading'       => array( 'Природа зависимости', 'demo_heading' ),
		'section_nature_lead'          => array( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor', 'demo_lead' ),
		'section_program_heading'      => array( 'Наша программа включает 4 направления', 'demo_heading' ),
		'section_program_more_label'   => array( 'подробнее', 'demo_label' ),
		'section_program_lead'         => array( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'demo_lead' ),
		'section_stages_heading'       => array( 'Что нужно для прохождения реабилитации и лечения', 'demo_heading' ),
		'section_stages_lead'          => array( 'Мы гарантируем конфиденциальность, уважение к личности, поддержание комфортной, психологически безопасной атмосферы.', 'demo_lead' ),
		'section_stages_support_heading' => array( 'Поддержка осуществляется на всех этапах:', 'demo_heading' ),
		'section_approach_heading'     => array( 'Наш подход к лечению зависимостей', 'demo_heading' ),
		'section_approach_more_label'  => array( 'подробнее', 'demo_label' ),
		'section_approach_more_url'    => array( home_url( '/o-centre/programma-lecheniya/' ), 'demo_url' ),
		'section_approach_highlight'   => array( 'Мы используем мультидисциплинарный подход — когда лечение одного пациента обеспечивается командой специалистов разных профилей.', 'demo_text' ),
		'section_approach_intro'       => array( 'Лечение в нашем реабилитационном центре совмещает современный и мультидисциплинарный подход, направленный на устранение истинных причин зависимости.', 'demo_text' ),
		'section_corridor_image_alt'   => array( 'Интерьер клиники — коридор с картинами', 'demo_alt' ),
		'section_team_image_alt'       => array( 'Команда специалистов реабилитационного центра', 'demo_alt' ),
		'section_faq_heading'          => array( 'Нас часто спрашивают', 'demo_heading' ),
	);

	foreach ( $scalars as $field => list( $val, $src ) ) {
		if ( fp02_fix05_seed_if_empty( $pid, $field, $val, $src, $seed_log ) ) {
			$db_writes++;
		}
	}

	$repeaters = array(
		'section_nature_text_blocks'     => array( $nature_seed, 'resolved_or_demo_nature_blocks' ),
		'section_nature_cards'           => array( $demo_nature_cards, 'demo_nature_cards' ),
		'section_program_intro_items'    => array( $demo_intros, 'demo_program_intros' ),
		'section_stages_items'           => array( $stages_seed, 'resolved_or_demo_stages' ),
		'section_stages_support_items'   => array( $demo_support, 'demo_support' ),
		'section_approach_cards'         => array( $demo_approach_cards, 'demo_approach_cards' ),
	);
	foreach ( $repeaters as $field => list( $val, $src ) ) {
		if ( fp02_fix05_seed_if_empty( $pid, $field, $val, $src, $seed_log ) ) {
			$db_writes++;
		}
	}

	// Images.
	if ( $corridor_media['id'] > 0 && fp02_fix05_seed_if_empty( $pid, 'section_corridor_image', $corridor_media['id'], 'corridor_media:' . $corridor_media['note'], $seed_log ) ) {
		$db_writes++;
	}
	if ( $team_id > 0 && fp02_fix05_seed_if_empty( $pid, 'section_team_image', $team_id, 'home_staff_photo_image_id_reused_as_section', $seed_log ) ) {
		$db_writes++;
	}
	if ( $landscape_id > 0 && fp02_fix05_seed_if_empty( $pid, 'section_clinic_landscape_image', $landscape_id, 'already_or_landscape', $seed_log ) ) {
		$db_writes++;
	}
}

// Resolve check after seed for #73.
$resolve73 = array(
	'team'     => shpigovsky_section_image_or_asset_prefer( 73, array( 'section_team_image', 'section_approach_staff_image' ), 'img/content/pre-reviews/shpigovsky-staff-group.webp', 'alt', 1139, 443 ),
	'corridor' => shpigovsky_section_image_or_asset_prefer( 73, array( 'section_corridor_image', 'section_approach_corridor_image' ), 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp', 'alt', 2187, 1231 ),
	'landscape'=> shpigovsky_section_image_or_asset( 73, 'section_clinic_landscape_image', 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp', 'alt', 1139, 584 ),
);

$out = array(
	'sync'            => $sync,
	'corridor_media'  => $corridor_media,
	'team_id'         => $team_id,
	'landscape_id'    => $landscape_id,
	'db_writes'       => $db_writes,
	'seed_log_count'  => count( $seed_log ),
	'seed_log'        => $seed_log,
	'resolve73'       => $resolve73,
	'home_staff_untouched' => (int) get_post_meta( 4, 'home_staff_photo_image', true ),
	'home_landscape_untouched' => (int) get_post_meta( 4, 'home_clinic_landscape_image', true ),
);

file_put_contents( $evidence . '/_v9-06e46-fix05-seed-result.json', wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// Seeded CSV.
$csv = "post_id,field,action,before,seeded_value_or_source,source,result\n";
foreach ( $seed_log as $row ) {
	$csv .= sprintf(
		"%d,%s,%s,%s,%s,%s,%s\n",
		$row['post_id'],
		$row['field'],
		$row['action'],
		str_replace( array( "\n", ',' ), array( ' ', ';' ), (string) ( $row['before'] ?? '' ) ),
		str_replace( array( "\n", ',' ), array( ' ', ';' ), (string) ( $row['seeded'] ?? '' ) ),
		str_replace( ',', ';', (string) ( $row['source'] ?? '' ) ),
		$row['result']
	);
}
file_put_contents( $evidence . '/v9-06e46-fix05-seeded-fields.csv', $csv );

echo wp_json_encode(
	array(
		'db_writes' => $db_writes,
		'corridor'  => $corridor_media,
		'team_id'   => $team_id,
		'resolve73_team_source' => $resolve73['team']['source'] ?? '',
		'resolve73_corridor_source' => $resolve73['corridor']['source'] ?? '',
		'sync_ok' => array_reduce( $sync, static function ( $ok, $s ) { return $ok && ! empty( $s['match'] ); }, true ),
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
) . "\n";

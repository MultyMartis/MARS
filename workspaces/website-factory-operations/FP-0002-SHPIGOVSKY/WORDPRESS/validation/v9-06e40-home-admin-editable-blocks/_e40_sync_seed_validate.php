<?php
/**
 * V9-06E40 phase 2: import Home ACF from FieldGroups, seed meta, attach media, validate.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/image.php';

$root     = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$val_dir  = $root . '/validation/v9-06e40-home-admin-editable-blocks';
$home_id  = (int) get_option( 'page_on_front' );

if ( ! is_dir( $evidence ) ) {
	mkdir( $evidence, 0777, true );
}

function e40_ensure_attachment( $asset_rel, $title ) {
	$path = get_stylesheet_directory() . '/assets/' . ltrim( $asset_rel, '/' );
	if ( ! is_readable( $path ) ) {
		echo "ATTACH_MISS path={$path}\n";
		return 0;
	}
	$basename = basename( $path );
	$hash     = md5_file( $path );

	// Reuse by content hash meta if present.
	$found = get_posts(
		array(
			'post_type'      => 'attachment',
			'post_status'    => 'inherit',
			'posts_per_page' => 1,
			'meta_key'       => '_fp02_source_md5',
			'meta_value'     => $hash,
		)
	);
	if ( ! empty( $found ) ) {
		return (int) $found[0]->ID;
	}

	$upload = wp_upload_bits( $basename, null, file_get_contents( $path ) );
	if ( ! empty( $upload['error'] ) ) {
		echo "UPLOAD_ERR {$basename}: {$upload['error']}\n";
		return 0;
	}
	$filetype  = wp_check_filetype( $basename, null );
	$attach_id = wp_insert_attachment(
		array(
			'post_mime_type' => $filetype['type'] ?? 'application/octet-stream',
			'post_title'     => $title,
			'post_content'   => '',
			'post_status'    => 'inherit',
		),
		$upload['file']
	);
	if ( is_wp_error( $attach_id ) || ! $attach_id ) {
		return 0;
	}
	$meta = wp_generate_attachment_metadata( $attach_id, $upload['file'] );
	if ( is_array( $meta ) ) {
		wp_update_attachment_metadata( $attach_id, $meta );
	}
	update_post_meta( $attach_id, '_fp02_source_md5', $hash );
	update_post_meta( $attach_id, '_fp02_source_asset', $asset_rel );
	return (int) $attach_id;
}

// --- Import Home group from PHP authority ---
$all   = \Shpigovsky\Core\Fields\FieldGroups::get_field_groups();
$group = null;
foreach ( $all as $g ) {
	if ( ( $g['key'] ?? '' ) === 'group_fp02_page_home' ) {
		$group = $g;
		break;
	}
}
if ( ! $group ) {
	fwrite( STDERR, "FAIL: group_fp02_page_home missing from FieldGroups\n" );
	exit( 1 );
}

$field_count = count( $group['fields'] ?? array() );
echo "PHP_FIELD_COUNT={$field_count}\n";

if ( function_exists( 'acf_import_field_group' ) ) {
	$imported = acf_import_field_group( $group );
	echo 'IMPORT_ID=' . ( is_array( $imported ) ? ( $imported['ID'] ?? 'arr' ) : (string) $imported ) . "\n";
} else {
	fwrite( STDERR, "FAIL: acf_import_field_group missing\n" );
	exit( 1 );
}

$json = wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
file_put_contents( $root . '/acf-json/group_fp02_page_home.json', $json );
copy( $root . '/acf-json/group_fp02_page_home.json', $runtime . '/wp-content/acf-json/group_fp02_page_home.json' );
echo 'JSON_HASH=' . hash_file( 'sha256', $root . '/acf-json/group_fp02_page_home.json' ) . "\n";

// Trash duplicate Home groups if any (keep imported key).
$dup_q = new WP_Query(
	array(
		'post_type'      => 'acf-field-group',
		'post_status'    => array( 'publish', 'acf-disabled' ),
		'posts_per_page' => 20,
		'meta_key'       => 'key', // may not work; scan titles
	)
);
// Prefer scanning by acf_get_field_groups local/db.
$db_fields = acf_get_fields( 'group_fp02_page_home' );
echo 'DB_FIELD_COUNT=' . count( (array) $db_fields ) . "\n";

// --- Media attachments ---
$staff_id = e40_ensure_attachment( 'img/content/pre-reviews/shpigovsky-staff-group.webp', 'Шпиговский — фото команды (Home)' );
$land_id  = e40_ensure_attachment( 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp', 'Шпиговский — территория клиники (Home)' );
// Prefer existing 755 if it is the clinic landscape.
if ( $land_id <= 0 && get_post( 755 ) ) {
	$land_id = 755;
}
$v1_id  = e40_ensure_attachment( 'video/sergey-shpigovsky-interview.mp4', 'Интервью с Сергеем Шпиговским' );
$vp1_id = e40_ensure_attachment( 'img/content/videos/sergey-shpigovsky-interview-poster.webp', 'Превью — интервью Сергея Шпиговского' );
$v2_id  = e40_ensure_attachment( 'video/shpigovsky-center.mp4', 'Центр профилактики зависимостей Сергея Шпиговского' );
$vp2_id = e40_ensure_attachment( 'img/content/videos/shpigovsky-center-poster.webp', 'Превью — центр Шпиговского' );

echo "MEDIA staff={$staff_id} land={$land_id} v1={$v1_id} vp1={$vp1_id} v2={$v2_id} vp2={$vp2_id}\n";

// --- Seed Home fields ---
$seeds = array();

$seeds[] = array( 'field' => 'home_recovery_intro_benefits_enabled', 'value' => 1 );
$seeds[] = array(
	'field' => 'home_recovery_intro_benefits',
	'value' => shpigovsky_home_recovery_intro_benefits_fallback_rows(),
);

$seeds[] = array(
	'field' => 'home_treatment_prevention_heading',
	'value' => 'Лечение и&nbsp;профилактика',
);
$seeds[] = array(
	'field' => 'home_treatment_prevention_lead',
	'value' => 'Мы работаем с&nbsp;зависимостью не&nbsp;как с&nbsp;проступком, а&nbsp;как с&nbsp;состоянием, у&nbsp;которого есть биологические, психологические и&nbsp;социальные причины.',
);

$seeds[] = array( 'field' => 'home_gallery_display_mode', 'value' => 'random' );
$seeds[] = array( 'field' => 'home_gallery_random_count', 'value' => 12 );

$seeds[] = array(
	'field' => 'home_why_us_heading',
	'value' => 'Нас выбирают за&nbsp;мультидисциплинарный подход к&nbsp;лечению',
);
$seeds[] = array(
	'field' => 'home_why_us_lead',
	'value' => 'У&nbsp;нас команда, а&nbsp;не&nbsp;конвейер. Каждый клиент получает полное внимание&nbsp;— психолога, нейропсихолога, специалиста по&nbsp;кинезиотерапии, специалиста по&nbsp;телесноориентированной терапии и&nbsp;координатора программы.',
);
$seeds[] = array( 'field' => 'home_why_us_body_enabled', 'value' => 1 );
$seeds[] = array( 'field' => 'home_why_us_body', 'value' => shpigovsky_home_why_us_body_fallback_rows() );
$seeds[] = array( 'field' => 'home_why_us_items_enabled', 'value' => 1 );
$seeds[] = array( 'field' => 'home_why_us_items', 'value' => shpigovsky_home_why_us_items_fallback_rows() );

if ( $staff_id > 0 ) {
	$seeds[] = array( 'field' => 'home_staff_photo_image', 'value' => $staff_id );
}
if ( $land_id > 0 ) {
	$seeds[] = array( 'field' => 'home_clinic_landscape_image', 'value' => $land_id );
}

$seeds[] = array(
	'field' => 'home_recovery_life_heading',
	'value' => 'Как меняется жизнь человека в&nbsp;процессе восстановления',
);
$seeds[] = array(
	'field' => 'home_recovery_life_highlight',
	'value' => 'У&nbsp;нас команда, а&nbsp;не&nbsp;конвейер. Каждый клиент получает полное внимание&nbsp;— психолога, нейропсихолога, специалиста по&nbsp;кинезиотерапии, специалиста по&nbsp;телесноориентированной терапии и&nbsp;координатора программы.',
);
$seeds[] = array( 'field' => 'home_recovery_life_intro_enabled', 'value' => 1 );
$seeds[] = array( 'field' => 'home_recovery_life_intro', 'value' => shpigovsky_home_recovery_life_intro_fallback_rows() );
$seeds[] = array( 'field' => 'home_recovery_life_stages_enabled', 'value' => 1 );
$seeds[] = array( 'field' => 'home_recovery_life_stages', 'value' => shpigovsky_home_recovery_life_stages_fallback_rows() );

$seeds[] = array(
	'field' => 'home_genotyping_heading',
	'value' => 'Генотипирование&nbsp;— инструмент диагностики',
);
$seeds[] = array( 'field' => 'home_genotyping_link_text', 'value' => 'подробнее' );
$seeds[] = array(
	'field' => 'home_genotyping_link_url',
	'value' => home_url( '/uslugi/zavisimosti/profilakticheskiy-analiz/' ),
);
$seeds[] = array(
	'field' => 'home_genotyping_lead',
	'value' => 'анализ, который позволяет увидеть индивидуальные генетические особенности системы регуляции настроения. Не&nbsp;угадать. Не&nbsp;предположить. Измерить.',
);
$seeds[] = array( 'field' => 'home_genotyping_body_enabled', 'value' => 1 );
$seeds[] = array( 'field' => 'home_genotyping_body', 'value' => shpigovsky_home_genotyping_body_fallback_rows() );
$seeds[] = array(
	'field' => 'home_genotyping_subheading',
	'value' => 'Кому полезно генетическоее исследование особенностей зависимости',
);
$seeds[] = array(
	'field' => 'home_genotyping_list_intro',
	'value' => 'В&nbsp;нашей лаборатории мы исследуем полиморфизмы генов, участвующих в&nbsp;индивидуальной реакции мозга на&nbsp;вещества, на&nbsp;самоощущения. Определенная генетическая панель показывает риски, снимает социальную стигму и&nbsp;чувство вины, доказывая, что зависимость&nbsp;— это комплексное заболевание, а&nbsp;не&nbsp;просто отсутствие силы воли. Чаще всего для проведения этого исследования к&nbsp;нам обращаются:',
);
$seeds[] = array( 'field' => 'home_genotyping_items_enabled', 'value' => 1 );
$seeds[] = array( 'field' => 'home_genotyping_items', 'value' => shpigovsky_home_genotyping_items_fallback_rows() );
$seeds[] = array( 'field' => 'home_genotyping_cta_label', 'value' => 'Записаться на консультацию' );

$seeds[] = array( 'field' => 'home_videos_heading', 'value' => 'Видео о&nbsp;нашем центре' );
$seeds[] = array( 'field' => 'home_videos_items_enabled', 'value' => 1 );

$video_rows = array();
if ( $v1_id > 0 ) {
	$video_rows[] = array(
		'title'        => 'Интервью с&nbsp;Сергеем Шпиговским',
		'video_file'   => $v1_id,
		'poster'       => $vp1_id > 0 ? $vp1_id : null,
		'item_enabled' => 1,
	);
}
if ( $v2_id > 0 ) {
	$video_rows[] = array(
		'title'        => 'Центр профилактики зависимостей Сергея Шпиговского',
		'video_file'   => $v2_id,
		'poster'       => $vp2_id > 0 ? $vp2_id : null,
		'item_enabled' => 1,
	);
}
if ( ! empty( $video_rows ) ) {
	$seeds[] = array( 'field' => 'home_videos_items', 'value' => $video_rows );
}

$seed_results = array();
foreach ( $seeds as $seed ) {
	$ok = update_field( $seed['field'], $seed['value'], $home_id );
	$rb = get_field( $seed['field'], $home_id );
	$seed_results[] = array(
		'field'  => $seed['field'],
		'update' => (bool) $ok,
		'read'   => is_array( $rb ) ? ( 'array:' . count( $rb ) ) : ( is_scalar( $rb ) ? mb_substr( (string) $rb, 0, 80 ) : gettype( $rb ) ),
	);
	echo 'SEED ' . $seed['field'] . ' ok=' . ( $ok ? '1' : '0' ) . "\n";
}

// --- Validation probes ---
$eligible = function_exists( 'shpigovsky_get_home_gallery_eligible_slides' )
	? shpigovsky_get_home_gallery_eligible_slides()
	: array();
$random_slides = shpigovsky_get_home_gallery_service_slides();

// Force mode all temporarily via meta for probe then restore.
$prev_mode = get_field( 'home_gallery_display_mode', $home_id );
update_field( 'home_gallery_display_mode', 'all', $home_id );
$all_slides = shpigovsky_get_home_gallery_service_slides();
update_field( 'home_gallery_display_mode', 'selected', $home_id );
// pick up to 3 eligible ids
$sel_ids = array_slice( array_map( static function ( $s ) { return (int) $s['id']; }, $eligible ), 0, 3 );
update_field( 'home_gallery_selected_services', $sel_ids, $home_id );
$sel_slides = shpigovsky_get_home_gallery_service_slides();
// restore default random
update_field( 'home_gallery_display_mode', 'random', $home_id );
update_field( 'home_gallery_random_count', 12, $home_id );
update_field( 'home_gallery_selected_services', array(), $home_id );
$random_again = shpigovsky_get_home_gallery_service_slides();

$videos_now = shpigovsky_get_home_videos_items();

$admin_fields = acf_get_fields( 'group_fp02_page_home' );
$admin_names  = array();
foreach ( (array) $admin_fields as $f ) {
	$admin_names[] = $f['name'] ?? '';
}

$http = wp_remote_get(
	home_url( '/' ),
	array(
		'timeout'   => 30,
		'sslverify' => false,
	)
);
$home_code = wp_remote_retrieve_response_code( $http );
$home_body = is_wp_error( $http ) ? '' : wp_remote_retrieve_body( $http );

$checks = array(
	'home_http'              => $home_code,
	'benefits_in_html'       => ( false !== strpos( $home_body, 'home-recovery-intro__benefits' ) ),
	'treatment_heading'      => ( false !== strpos( $home_body, 'home-treatment-prevention__heading' ) ),
	'why_us'                 => ( false !== strpos( $home_body, 'home-why-us' ) ),
	'staff'                  => ( false !== strpos( $home_body, 'home-staff-photo' ) ),
	'landscape'              => ( false !== strpos( $home_body, 'clinic-landscape' ) ),
	'recovery_life'          => ( false !== strpos( $home_body, 'home-recovery-life__stages' ) ),
	'genotyping'             => ( false !== strpos( $home_body, 'home-genotyping' ) ),
	'videos'                 => ( false !== strpos( $home_body, 'home-videos' ) ),
	'gallery_slider'         => ( false !== strpos( $home_body, 'data-gallery-slider' ) ),
	'admin_field_count'      => count( (array) $admin_fields ),
	'eligible_count'         => count( $eligible ),
	'random_count'           => count( $random_again ),
	'all_count'              => count( $all_slides ),
	'selected_count'         => count( $sel_slides ),
	'selected_ids'           => $sel_ids,
	'videos_count'           => count( $videos_now ),
	'has_new_fields'         => array(
		'home_recovery_intro_benefits' => in_array( 'home_recovery_intro_benefits', $admin_names, true ),
		'home_gallery_display_mode'    => in_array( 'home_gallery_display_mode', $admin_names, true ),
		'home_why_us_heading'          => in_array( 'home_why_us_heading', $admin_names, true ),
		'home_staff_photo_image'       => in_array( 'home_staff_photo_image', $admin_names, true ),
		'home_videos_items'            => in_array( 'home_videos_items', $admin_names, true ),
		'home_genotyping_heading'      => in_array( 'home_genotyping_heading', $admin_names, true ),
	),
);

$out = array(
	'wave'          => 'V9-06E40',
	'home_id'       => $home_id,
	'php_fields'    => $field_count,
	'db_fields'     => count( (array) $db_fields ),
	'media'         => compact( 'staff_id', 'land_id', 'v1_id', 'vp1_id', 'v2_id', 'vp2_id' ),
	'seeds'         => $seed_results,
	'checks'        => $checks,
	'admin_names'   => $admin_names,
	'video_urls'    => array_map(
		static function ( $v ) {
			return array(
				'title' => $v['title'] ?? '',
				'url'   => $v['video_url'] ?? '',
				'poster'=> $v['poster_url'] ?? '',
			);
		},
		$videos_now
	),
);

file_put_contents( $val_dir . '/_e40_sync_seed_result.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
echo 'HOME_HTTP=' . $home_code . "\n";
echo 'ADMIN_FIELDS=' . count( (array) $admin_fields ) . "\n";
echo 'RANDOM_SLIDES=' . count( $random_again ) . ' ALL=' . count( $all_slides ) . ' SEL=' . count( $sel_slides ) . "\n";
echo 'VIDEOS=' . count( $videos_now ) . "\n";
echo "PHASE2_OK\n";

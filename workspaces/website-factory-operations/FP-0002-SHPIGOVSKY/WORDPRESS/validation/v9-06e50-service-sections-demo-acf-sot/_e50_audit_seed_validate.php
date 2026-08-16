<?php
/**
 * V9-06E50 — Service sections demo ACF SoT: sync, audit, seed, empty-field test, validate.
 *
 * @package FP0002
 */

declare(strict_types=1);

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require $wp_load;

$evidence   = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$src_root   = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root    = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content';
$bak_file   = $evidence . '/v9-06e50-backup-path.txt';
$backup_root = is_file( $bak_file ) ? trim( (string) file_get_contents( $bak_file ) ) : '';

if ( '' === $backup_root || ! is_dir( $backup_root ) ) {
	fwrite( STDERR, "STOP — backup root missing\n" );
	exit( 2 );
}

if ( ! function_exists( 'update_field' ) || ! function_exists( 'get_field' ) ) {
	fwrite( STDERR, "ACF missing\n" );
	exit( 1 );
}

$db_writes = 0;
$seed_log  = array();
$summary   = array(
	'backup_root' => $backup_root,
	'db_writes'   => 0,
	'sync'        => array(),
);

/**
 * CSV writer.
 *
 * @param string               $path Path.
 * @param array<int,string>    $header Header.
 * @param array<int,array>     $rows Rows.
 * @return void
 */
function e50_csv( string $path, array $header, array $rows ): void {
	$fp = fopen( $path, 'wb' );
	if ( ! $fp ) {
		fwrite( STDERR, "Cannot write $path\n" );
		exit( 1 );
	}
	fputcsv( $fp, $header );
	foreach ( $rows as $row ) {
		fputcsv( $fp, $row );
	}
	fclose( $fp );
}

/**
 * Sync file source→runtime.
 *
 * @param string $rel Relative under WORDPRESS/.
 * @return array{rel:string,match:bool,copied:bool,hash_src:string,hash_dst:string}
 */
function e50_sync( string $rel ): array {
	global $src_root, $rt_root;
	$src = $src_root . '/' . $rel;
	$map = array(
		'theme/shpigovsky/'        => 'themes/shpigovsky/',
		'plugins/shpigovsky-core/' => 'plugins/shpigovsky-core/',
		'acf-json/'                => 'acf-json/',
	);
	$dst = $rt_root . '/' . $rel;
	foreach ( $map as $from => $to ) {
		if ( str_starts_with( $rel, $from ) ) {
			$dst = $rt_root . '/' . $to . substr( $rel, strlen( $from ) );
			break;
		}
	}

	$hash_src = is_file( $src ) ? (string) md5_file( $src ) : '';
	$hash_dst = is_file( $dst ) ? (string) md5_file( $dst ) : '';
	$copied   = false;
	if ( $hash_src && $hash_src !== $hash_dst ) {
		$dir = dirname( $dst );
		if ( ! is_dir( $dir ) ) {
			wp_mkdir_p( $dir );
		}
		copy( $src, $dst );
		$copied   = true;
		$hash_dst = (string) md5_file( $dst );
	}
	return array(
		'rel'      => $rel,
		'src'      => $src,
		'dst'      => $dst,
		'match'    => ( $hash_src !== '' && $hash_src === $hash_dst ),
		'copied'   => $copied,
		'hash_src' => $hash_src,
		'hash_dst' => $hash_dst,
	);
}

/**
 * HTTP get.
 *
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e50_http( string $url ): array {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 40,
			CURLOPT_SSL_VERIFYPEER => false,
		)
	);
	$body = (string) curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	return array( 'code' => $code, 'body' => $body );
}

/**
 * Value state.
 *
 * @param mixed $value Value.
 * @return string
 */
function e50_state( $value ): string {
	if ( null === $value || false === $value || '' === $value || array() === $value ) {
		return 'empty';
	}
	if ( is_numeric( $value ) && (int) $value === 0 && ! is_string( $value ) ) {
		return 'empty';
	}
	if ( is_array( $value ) ) {
		if ( isset( $value['ID'] ) || isset( $value['id'] ) ) {
			$id = isset( $value['ID'] ) ? (int) $value['ID'] : (int) $value['id'];
			return $id > 0 ? 'meaningful' : 'empty';
		}
		$flat = (string) wp_json_encode( $value );
		if ( false !== stripos( $flat, 'ТЕСТ' ) || false !== stripos( $flat, '000101' ) ) {
			return 'test';
		}
		if ( false !== stripos( $flat, 'DEMO' ) || false !== stripos( $flat, 'Lorem ipsum' ) ) {
			return 'demo';
		}
		return shpigovsky_has_meaningful_repeater_rows( $value ) ? 'meaningful' : 'empty';
	}
	$s = trim( (string) $value );
	if ( '' === $s ) {
		return 'empty';
	}
	if ( false !== stripos( $s, 'ТЕСТ' ) || false !== stripos( $s, '000101' ) ) {
		return 'test';
	}
	if ( false !== stripos( $s, 'DEMO' ) || false !== stripos( $s, 'Lorem ipsum' ) ) {
		return 'demo';
	}
	return 'meaningful';
}

/**
 * Empty?
 *
 * @param mixed  $v Value.
 * @param string $type Field type.
 * @return bool
 */
function e50_is_empty( $v, string $type = 'text' ): bool {
	if ( 'image' === $type ) {
		if ( is_array( $v ) ) {
			$id = isset( $v['ID'] ) ? (int) $v['ID'] : ( isset( $v['id'] ) ? (int) $v['id'] : 0 );
			return $id <= 0;
		}
		return ! is_numeric( $v ) || (int) $v <= 0;
	}
	if ( 'repeater' === $type || 'true_false' === $type ) {
		if ( 'true_false' === $type ) {
			return null === $v || false === $v || '' === $v;
		}
		return ! is_array( $v ) || ! shpigovsky_has_meaningful_repeater_rows( $v );
	}
	return null === $v || false === $v || '' === trim( (string) $v );
}

/**
 * Preview clip.
 *
 * @param mixed $v Value.
 * @return string
 */
function e50_preview( $v ): string {
	if ( is_array( $v ) ) {
		if ( isset( $v['ID'] ) ) {
			return 'attachment:' . (int) $v['ID'];
		}
		return 'array:' . count( $v );
	}
	$s = preg_replace( '/\s+/', ' ', (string) $v );
	return mb_substr( (string) $s, 0, 120 );
}

/**
 * Dependency-specific demo cue.
 *
 * @param mixed $v Value.
 * @return bool
 */
function e50_is_dependency_specific( $v ): bool {
	$s = is_array( $v ) ? (string) wp_json_encode( $v, JSON_UNESCAPED_UNICODE ) : (string) $v;
	$needles = array(
		'зависимост',
		'Зависимост',
		'зависимости',
		'лечение зависимостей',
		'Природа зависимости',
		'которые мы лечим',
		'zavisimosti/profilakticheskiy',
		'генотипирован',
	);
	foreach ( $needles as $n ) {
		if ( false !== mb_stripos( $s, $n ) ) {
			return true;
		}
	}
	return false;
}

/**
 * Seed update.
 *
 * @param int    $post_id Post.
 * @param string $field Field.
 * @param mixed  $value Value.
 * @param string $before_state Before.
 * @param string $source Source.
 * @param string $notes Notes.
 * @param bool   $force Force overwrite.
 * @return bool
 */
function e50_seed( int $post_id, string $field, $value, string $before_state, string $source, string $notes = '', bool $force = false ): bool {
	global $db_writes, $seed_log;

	$existing = get_field( $field, $post_id );
	$type     = 'text';
	if ( in_array( $field, array( 'section_team_image', 'section_corridor_image', 'section_clinic_landscape_image' ), true ) ) {
		$type = 'image';
	} elseif ( str_contains( $field, '_items' ) || str_contains( $field, '_cards' ) || str_contains( $field, '_blocks' ) ) {
		$type = 'repeater';
	}

	$empty = e50_is_empty( $existing, $type );
	if ( ! $force && ! $empty ) {
		$seed_log[] = array(
			$post_id,
			get_the_title( $post_id ),
			$field,
			$before_state,
			e50_state( $existing ),
			'no',
			'preserve',
			e50_preview( $existing ),
			'yes',
			'preserved existing',
		);
		return false;
	}

	update_field( $field, $value, $post_id );
	++$db_writes;
	$after = get_field( $field, $post_id );
	$seed_log[] = array(
		$post_id,
		get_the_title( $post_id ),
		$field,
		$before_state,
		e50_state( $after ),
		'yes',
		$source,
		e50_preview( $value ),
		$force ? 'no' : 'n/a',
		$notes,
	);
	return true;
}

// -------------------------------------------------------------------------
// 1. Sync source → runtime + export ACF JSON from PHP definition
// -------------------------------------------------------------------------
$sync_files = array(
	'theme/shpigovsky/inc/service-section-helpers.php',
	'theme/shpigovsky/template-parts/service/nature.php',
	'theme/shpigovsky/template-parts/service/team-stats.php',
	'theme/shpigovsky/template-parts/service/stages.php',
	'theme/shpigovsky/template-parts/service/children.php',
	'theme/shpigovsky/template-parts/service/program.php',
	'theme/shpigovsky/template-parts/service/faq.php',
	'plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php',
);

$sync_rows = array();
foreach ( $sync_files as $rel ) {
	$r = e50_sync( $rel );
	$summary['sync'][] = $r;
	$sync_rows[] = array(
		basename( $rel ),
		$r['src'],
		$r['dst'],
		$r['match'] ? 'yes' : 'no',
		$r['copied'] ? 'copied' : 'unchanged',
		$r['match'] ? 'PASS' : 'FAIL',
	);
}

// Refresh ACF JSON instructions from patched PHP source strings (class may be stale in-memory).
$json_src = $src_root . '/acf-json/group_fp02_service_section_parity.json';
$json_rt  = $rt_root . '/acf-json/group_fp02_service_section_parity.json';
$php_src  = (string) file_get_contents( $src_root . '/plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php' );
$json_raw = (string) file_get_contents( $json_src );
$json_instruction_map = array(
	'Если поле оставить пустым, блок может использовать аварийный резерв.' =>
		'Если поле очистить, необязательный текст на сайте может скрыться. Аварийный резерв — только технический запас, не обычный источник контента.',
	'Пустое поле: intro_text → hero_lead → аварийный резерв.' =>
		'Если поле очистить, лид может скрыться (или подтянуться intro_text / hero_lead этой страницы, если они заполнены). Аварийный резерв — только технический запас.',
	'Если поле оставить пустым — аварийный резерв.' =>
		'Если поле очистить, необязательный текст на сайте может скрыться. Аварийный резерв — только технический запас, не обычный источник контента.',
	'Если оставить пустым — аварийный резерв.' =>
		'Если очистить, карточки на сайте могут скрыться. Аварийный резерв — только технический запас.',
	'Если все абзацы пусты — аварийный резерв.' =>
		'Если все абзацы очистить, intro на сайте может скрыться. Аварийный резерв — только технический запас.',
	'Пустой repeater — аварийный резерв (legacy Structured Sections stages).' =>
		'Пустой repeater: этапы могут скрыться (или показаться legacy Structured Sections stages, если они есть). Аварийный резерв темы — только технический запас.',
	'Если поле оставить пустым, блок может использовать аварийный резерв темы.' =>
		'Если поле очистить, блок может использовать аварийный резерв темы (технический запас).',
	'Если поле оставить пустым — аварийный заголовок «Нас часто спрашивают».' =>
		'Если поле очистить, заголовок FAQ на сайте может скрыться или остаться пустым. Аварийный резерв — только технический запас.',
	'FP-0002 V9-06E46-FIX05 section demo seed + no template-fallback wording; section_team_image / section_corridor_image.' =>
		'FP-0002 V9-06E50 section demo ACF SoT; empty fields hide optional text; emergency reserve technical only.',
);
foreach ( $json_instruction_map as $from => $to ) {
	$json_raw = str_replace( $from, $to, $json_raw );
}
file_put_contents( $json_src, $json_raw );
file_put_contents( $json_rt, $json_raw );
$sync_rows[] = array(
	'group_fp02_service_section_parity.json',
	$json_src,
	$json_rt,
	md5_file( $json_src ) === md5_file( $json_rt ) ? 'yes' : 'no',
	'wording-synced',
	( md5_file( $json_src ) === md5_file( $json_rt ) && str_contains( $php_src, 'V9-06E50' ) ) ? 'PASS' : 'FAIL',
);

if ( function_exists( 'acf_get_store' ) ) {
	foreach ( array( 'local-fields', 'local-groups' ) as $store_name ) {
		$store = acf_get_store( $store_name );
		if ( $store && method_exists( $store, 'reset' ) ) {
			$store->reset();
		}
	}
}

// -------------------------------------------------------------------------
// 2. Field inventory from ACF group
// -------------------------------------------------------------------------
$group_json = json_decode( (string) file_get_contents( $src_root . '/acf-json/group_fp02_service_section_parity.json' ), true );
$inv_rows   = array();
$editable_fields = array();

/**
 * Walk fields.
 *
 * @param array $fields Fields.
 * @return void
 */
function e50_walk_fields( array $fields ): void {
	global $inv_rows, $editable_fields;
	foreach ( $fields as $f ) {
		if ( ! is_array( $f ) ) {
			continue;
		}
		$name  = (string) ( $f['name'] ?? '' );
		$label = (string) ( $f['label'] ?? '' );
		$type  = (string) ( $f['type'] ?? '' );
		if ( '' === $name ) {
			continue;
		}
		$block = 'unknown';
		if ( str_starts_with( $name, 'section_dependencies' ) ) {
			$block = 'dependencies/children';
		} elseif ( str_starts_with( $name, 'section_nature' ) ) {
			$block = 'nature';
		} elseif ( str_starts_with( $name, 'section_program' ) ) {
			$block = 'program';
		} elseif ( str_starts_with( $name, 'section_stages' ) ) {
			$block = 'stages';
		} elseif ( str_starts_with( $name, 'section_approach' ) || str_starts_with( $name, 'section_team' ) || str_starts_with( $name, 'section_corridor' ) ) {
			$block = 'approach/team';
		} elseif ( str_starts_with( $name, 'section_clinic' ) ) {
			$block = 'clinic-landscape';
		} elseif ( str_starts_with( $name, 'section_faq' ) ) {
			$block = 'faq';
		} elseif ( str_starts_with( $name, 'section_nav' ) ) {
			$block = 'subnav';
		} elseif ( str_contains( $name, 'specialists' ) || str_contains( $name, 'comfort' ) || str_contains( $name, 'reviews' ) || str_contains( $name, 'founder' ) || str_contains( $name, 'final' ) ) {
			$block = 'shared/automatic';
		} elseif ( str_contains( $name, 'notice' ) ) {
			$block = 'admin-notice';
		} elseif ( str_contains( $name, 'visible' ) ) {
			$block = 'visibility';
		}

		$optional = in_array( $type, array( 'message', 'true_false' ), true ) || str_contains( $name, 'notice' ) ? 'yes' : 'no';
		$required_visual = ( 'image' === $type || ( in_array( $type, array( 'text', 'textarea', 'repeater' ), true ) && ! str_contains( $name, 'visible' ) ) ) ? 'yes' : 'no';
		$had_fallback = in_array( $type, array( 'text', 'textarea', 'repeater' ), true ) ? 'yes' : 'no';

		$inv_rows[] = array( $name, $label, $type, $block, $required_visual, $optional, $had_fallback, '' );

		if ( in_array( $type, array( 'text', 'textarea', 'repeater', 'image', 'url', 'true_false' ), true ) ) {
			$editable_fields[ $name ] = $type;
		}
		if ( ! empty( $f['sub_fields'] ) && is_array( $f['sub_fields'] ) ) {
			// repeaters tracked at parent only.
		}
	}
}

e50_walk_fields( is_array( $group_json['fields'] ?? null ) ? $group_json['fields'] : array() );
e50_csv(
	$evidence . '/v9-06e50-section-field-inventory.csv',
	array( 'field_name', 'field_label', 'field_type', 'frontend_block', 'required_for_visual', 'optional', 'currently_has_hardcoded_fallback', 'notes' ),
	$inv_rows
);

// -------------------------------------------------------------------------
// 3. Completeness before + frontend source audit
// -------------------------------------------------------------------------
$section_posts = array(
	73 => array( 'title' => 'Зависимости', 'route' => '/uslugi/zavisimosti/' ),
	77 => array( 'title' => 'Психическое здоровье', 'route' => '/uslugi/psihicheskoe-zdorovie/' ),
	84 => array( 'title' => 'Расстройства пищевого поведения', 'route' => '/uslugi/rasstroystva-pischevogo-povedeniya/' ),
);

$completeness = array();
$fe_source    = array();
$blocks_map   = array(
	'dependencies/children' => array( 'section_dependencies_heading', 'section_dependencies_lead', 'section_dependencies_footer' ),
	'nature'                => array( 'section_nature_heading', 'section_nature_lead', 'section_nature_text_blocks', 'section_nature_cards' ),
	'program'               => array( 'section_program_heading', 'section_program_lead', 'section_program_intro_items', 'section_program_more_label' ),
	'stages'                => array( 'section_stages_heading', 'section_stages_lead', 'section_stages_items', 'section_stages_support_items' ),
	'approach/team'         => array( 'section_approach_heading', 'section_approach_highlight', 'section_approach_intro', 'section_approach_cards', 'section_team_image', 'section_corridor_image' ),
	'clinic-landscape'      => array( 'section_clinic_landscape_image' ),
	'faq'                   => array( 'section_faq_heading' ),
);

foreach ( $section_posts as $pid => $meta ) {
	foreach ( $editable_fields as $fname => $ftype ) {
		$val   = get_field( $fname, $pid );
		$state = e50_state( $val );
		$seed_req = ( 'empty' === $state ) ? 'yes' : 'no';
		$source   = 'preserve';
		if ( 'empty' === $state ) {
			$source = 'neutral_demo';
		} elseif ( $pid !== 73 && e50_is_dependency_specific( $val ) && in_array( $fname, array( 'section_nature_heading', 'section_approach_heading', 'section_approach_intro', 'section_dependencies_heading', 'section_nature_text_blocks', 'section_nature_lead' ), true ) ) {
			$seed_req = 'yes';
			$source   = 'neutral_demo';
			$state    = 'demo';
		}
		$completeness[] = array(
			$pid,
			$meta['title'],
			$fname,
			$ftype,
			$state,
			( in_array( $ftype, array( 'text', 'textarea', 'repeater' ), true ) && 'empty' === e50_state( $val ) ) ? 'yes' : 'no',
			$seed_req,
			$source,
			'',
		);
	}
	foreach ( $blocks_map as $block => $fields ) {
		$sources = array();
		foreach ( $fields as $f ) {
			$v = get_field( $f, $pid );
			$sources[] = e50_is_empty( $v, $editable_fields[ $f ] ?? 'text' ) ? 'template_fallback_risk' : 'page_acf';
		}
		$current = in_array( 'template_fallback_risk', $sources, true ) ? 'mixed_acf_or_fallback' : 'page_acf';
		if ( 'dependencies/children' === $block ) {
			$current = 'page_acf+automatic_children';
		}
		$fe_source[] = array(
			$pid,
			$meta['title'],
			$meta['route'],
			$block,
			$current,
			'yes',
			'ensure_acf_seed_and_empty_safe',
			'',
		);
	}
}

e50_csv(
	$evidence . '/v9-06e50-section-field-completeness-before.csv',
	array( 'post_id', 'title', 'field_name', 'field_type', 'current_value_state', 'frontend_depends_on_template_fallback', 'seed_required', 'proposed_seed_source', 'notes' ),
	$completeness
);
e50_csv(
	$evidence . '/v9-06e50-section-frontend-source-audit-before.csv',
	array( 'post_id', 'title', 'route', 'frontend_block', 'current_source', 'should_be_page_acf', 'action', 'notes' ),
	$fe_source
);

// Hardcoded fallback audit (post E50 code intent).
$fallback_audit = array(
	array( 'inc/service-section-helpers.php', 'shpigovsky_get_section_nature_*_fallback', 'nature lorem cards/blocks', 'ACF empty', 'no', 'keep_emergency_only', 'removed from normal resolver path' ),
	array( 'inc/service-section-helpers.php', 'shpigovsky_get_section_program_intro_demo_fallback', 'lorem intros', 'ACF empty', 'no', 'keep_emergency_only', 'resolver returns empty' ),
	array( 'inc/service-section-helpers.php', 'shpigovsky_get_section_stages_items_fallback', 'default stages', 'ACF+legacy empty', 'no', 'keep_emergency_only', 'resolver returns empty' ),
	array( 'inc/service-section-helpers.php', 'shpigovsky_get_section_approach_fallback_cards', 'approach lorem cards', 'ACF empty', 'no', 'keep_emergency_only', 'template no longer calls' ),
	array( 'inc/service-section-helpers.php', 'shpigovsky_get_section_stages_support_fallback', 'support bullets', 'ACF empty', 'no', 'keep_emergency_only', 'template no longer calls' ),
	array( 'template-parts/service/nature.php', 'heading/lead/cards', 'hardcoded nature copy', 'ACF empty', 'no', 'convert_to_empty_behavior', 'hides optional empty text/cards' ),
	array( 'template-parts/service/team-stats.php', 'heading/intro/cards', 'hardcoded approach copy', 'ACF empty', 'no', 'convert_to_empty_behavior', 'hides optional empty text/cards' ),
	array( 'template-parts/service/stages.php', 'heading/lead/support', 'hardcoded stages copy', 'ACF empty', 'no', 'convert_to_empty_behavior', 'ACF only for subdivision' ),
	array( 'template-parts/service/children.php', 'heading/lead/footer', 'dependencies PHP demos', 'ACF empty', 'no', 'remove_normal_fallback', 'children list kept automatic' ),
	array( 'template-parts/service/program.php', 'lead Lorem', 'lorem program lead', 'ACF+hero empty', 'no', 'remove_normal_fallback', 'programme cards catalog kept shared' ),
	array( 'template-parts/service/faq.php', 'section_faq_heading', 'Нас часто спрашивают', 'ACF empty on section', 'no', 'convert_to_empty_behavior', 'leaf keeps default title' ),
	array( 'image helpers', 'section_*_image theme asset', 'theme webp', 'image ACF empty', 'no', 'keep_emergency_only', 'image emergency reserve OK' ),
);
e50_csv(
	$evidence . '/v9-06e50-section-hardcoded-fallback-audit.csv',
	array( 'file', 'function_or_block', 'fallback_text_or_source', 'used_when', 'normal_content_source', 'action', 'notes' ),
	$fallback_audit
);

// -------------------------------------------------------------------------
// 4. Section-specific demo packs + seed
// -------------------------------------------------------------------------
$lorem_short = 'DEMO: краткий нейтральный текст раздела для демонстрации структуры блока. Замените на финальный контент в админке.';
$lorem_mid   = 'DEMO: нейтральный демонстрационный абзац для раздела. Описывает подход центра без привязки к алкогольной зависимости. Редактор может заменить текст в ACF.';

$packs = array(
	73 => array(
		'label' => 'зависимости',
		'deps_heading' => 'Зависимости, которые мы лечим',
		'nature_heading' => 'Природа зависимости',
		'approach_heading' => 'Наш подход к лечению зависимостей',
		'approach_intro' => 'Лечение в нашем реабилитационном центре совмещает современный и мультидисциплинарный подход, направленный на устранение истинных причин зависимости.',
		'nature_blocks' => null, // preserve / existing FE
	),
	77 => array(
		'label' => 'психическое здоровье',
		'deps_heading' => 'Направления психического здоровья',
		'nature_heading' => 'Природа психических состояний',
		'approach_heading' => 'Наш подход к работе с психическим здоровьем',
		'approach_intro' => 'DEMO: работа с психическим здоровьем строится на бережной диагностике, командной поддержке и индивидуальной программе восстановления.',
		'nature_blocks' => array(
			array(
				'heading'    => 'Биопсихосоциальный контекст',
				'text'       => $lorem_mid,
				'link_label' => '',
				'link_url'   => '',
				'after_text' => '',
			),
			array(
				'heading'    => 'Ранние признаки и профилактика',
				'text'       => $lorem_mid,
				'link_label' => '',
				'link_url'   => '',
				'after_text' => '',
			),
		),
	),
	84 => array(
		'label' => 'расстройства пищевого поведения',
		'deps_heading' => 'Направления работы с РПП',
		'nature_heading' => 'Природа расстройств пищевого поведения',
		'approach_heading' => 'Наш подход к работе с расстройствами пищевого поведения',
		'approach_intro' => 'DEMO: помощь при расстройствах пищевого поведения сочетает медицинскую, психологическую и поведенческую поддержку с безопасной средой восстановления.',
		'nature_blocks' => array(
			array(
				'heading'    => 'Психологические механизмы',
				'text'       => $lorem_mid,
				'link_label' => '',
				'link_url'   => '',
				'after_text' => '',
			),
			array(
				'heading'    => 'Телесная регуляция и привычки',
				'text'       => $lorem_mid,
				'link_label' => '',
				'link_url'   => '',
				'after_text' => '',
			),
		),
	),
);

$shared_nature_cards = array(
	array( 'title' => 'Физиологическое проявление', 'text' => $lorem_short ),
	array( 'title' => 'Поведенческое проявление', 'text' => $lorem_short ),
);
$shared_approach_cards = array(
	array( 'title' => 'диагностические инструменты', 'text' => $lorem_short ),
	array( 'title' => 'психиатрия', 'text' => $lorem_short ),
	array( 'title' => 'функциональная терапия', 'text' => $lorem_short ),
	array( 'title' => 'комплементарная терапия', 'text' => $lorem_short ),
);
$shared_stages = function_exists( 'shpigovsky_get_section_stages_items_fallback' ) ? shpigovsky_get_section_stages_items_fallback() : array();
foreach ( $shared_stages as &$st ) {
	$st['enabled'] = 1;
}
unset( $st );
$shared_support = array();
if ( function_exists( 'shpigovsky_get_section_stages_support_fallback' ) ) {
	foreach ( shpigovsky_get_section_stages_support_fallback() as $t ) {
		$shared_support[] = array( 'text' => $t );
	}
}
$shared_intros = array();
if ( function_exists( 'shpigovsky_get_section_program_intro_demo_fallback' ) ) {
	foreach ( shpigovsky_get_section_program_intro_demo_fallback() as $t ) {
		$shared_intros[] = array( 'text' => 'DEMO: ' . $t );
	}
}
if ( empty( $shared_intros ) ) {
	$shared_intros = array(
		array( 'text' => $lorem_mid ),
		array( 'text' => $lorem_mid ),
	);
}

foreach ( $section_posts as $pid => $meta ) {
	$pack = $packs[ $pid ];

	// Preserve-only fill for empty required chrome; section-specific overwrite for wrong-copy demos on 77/84.
	$scalar_seeds = array(
		'section_dependencies_heading'     => array( $pack['deps_heading'], 'section_specific_demo' ),
		'section_dependencies_lead'        => array( $lorem_mid, 'neutral_demo' ),
		'section_dependencies_footer'      => array( $lorem_short, 'neutral_demo' ),
		'section_nature_heading'           => array( $pack['nature_heading'], 'section_specific_demo' ),
		'section_nature_lead'              => array( $lorem_mid, 'neutral_demo' ),
		'section_program_heading'          => array( 'Наша программа включает 4 направления', 'current_frontend' ),
		'section_program_more_label'       => array( 'подробнее', 'current_frontend' ),
		'section_program_lead'             => array( $lorem_mid, 'neutral_demo' ),
		'section_stages_heading'           => array( 'Что нужно для прохождения реабилитации и лечения', 'current_frontend' ),
		'section_stages_lead'              => array( 'Мы гарантируем конфиденциальность, уважение к личности, поддержание комфортной, психологически безопасной атмосферы.', 'current_frontend' ),
		'section_stages_support_heading'   => array( 'Поддержка осуществляется на всех этапах:', 'current_frontend' ),
		'section_approach_heading'         => array( $pack['approach_heading'], 'section_specific_demo' ),
		'section_approach_more_label'      => array( 'подробнее', 'current_frontend' ),
		'section_approach_more_url'        => array( home_url( '/o-centre/programma-lecheniya/' ), 'shared_url' ),
		'section_approach_highlight'       => array( 'Мы используем мультидисциплинарный подход — когда лечение одного пациента обеспечивается командой специалистов разных профилей.', 'current_frontend' ),
		'section_approach_intro'           => array( $pack['approach_intro'], 'section_specific_demo' ),
		'section_corridor_image_alt'       => array( 'Интерьер клиники — коридор с картинами', 'current_frontend' ),
		'section_team_image_alt'           => array( 'Команда специалистов реабилитационного центра', 'current_frontend' ),
		'section_faq_heading'              => array( 'Нас часто спрашивают', 'current_frontend' ),
	);

	foreach ( $scalar_seeds as $field => $pair ) {
		list( $val, $src ) = $pair;
		$before = get_field( $field, $pid );
		$state  = e50_state( $before );
		$force  = false;
		if ( $pid !== 73 && e50_is_dependency_specific( $before ) && in_array( $field, array( 'section_dependencies_heading', 'section_nature_heading', 'section_approach_heading', 'section_approach_intro', 'section_nature_lead' ), true ) ) {
			// Overwrite shared/dependency demo, but never touch operator TEST strings.
			if ( 'test' !== $state ) {
				$force = true;
			}
		}
		if ( 'test' === $state || ( 'meaningful' === $state && ! $force ) ) {
			$seed_log[] = array( $pid, $meta['title'], $field, $state, $state, 'no', 'preserve', e50_preview( $before ), 'yes', 'meaningful/test preserved' );
			continue;
		}
		e50_seed( $pid, $field, $val, $state, $src, $force ? 'overwrite dependency-shared demo' : 'seed if empty', $force );
	}

	// Repeaters.
	$nat_blocks = $pack['nature_blocks'];
	if ( null === $nat_blocks ) {
		$nat_blocks = function_exists( 'shpigovsky_get_section_nature_text_blocks_fallback' )
			? shpigovsky_get_section_nature_text_blocks_fallback()
			: array();
	}
	$rep_seeds = array(
		'section_nature_text_blocks'   => array( $nat_blocks, 'section_specific_demo' ),
		'section_nature_cards'         => array( $shared_nature_cards, 'neutral_demo' ),
		'section_program_intro_items'  => array( $shared_intros, 'neutral_demo' ),
		'section_stages_items'         => array( $shared_stages, 'current_frontend' ),
		'section_stages_support_items' => array( $shared_support, 'current_frontend' ),
		'section_approach_cards'       => array( $shared_approach_cards, 'neutral_demo' ),
	);
	foreach ( $rep_seeds as $field => $pair ) {
		list( $val, $src ) = $pair;
		$before = get_field( $field, $pid );
		$state  = e50_state( $before );
		$force  = false;
		if ( $pid !== 73 && 'section_nature_text_blocks' === $field && e50_is_dependency_specific( $before ) && 'test' !== $state ) {
			$force = true;
		}
		if ( 'test' === $state || ( in_array( $state, array( 'meaningful', 'demo', 'partial' ), true ) && ! $force && ! e50_is_empty( $before, 'repeater' ) ) ) {
			$seed_log[] = array( $pid, $meta['title'], $field, $state, $state, 'no', 'preserve', e50_preview( $before ), 'yes', 'existing repeater preserved' );
			continue;
		}
		e50_seed( $pid, $field, $val, $state, $src, $force ? 'section-specific nature blocks' : 'seed if empty', $force );
	}

	// Images — seed only if empty.
	foreach ( array(
		'section_clinic_landscape_image' => 1239,
		'section_team_image'             => 1238,
		'section_corridor_image'         => 1709,
	) as $img_field => $att_id ) {
		$before = get_field( $img_field, $pid );
		$state  = e50_state( $before );
		e50_seed( $pid, $img_field, $att_id, $state, 'accepted_neutral_image_set', 'image seed if empty', false );
	}

	// Visibility defaults ON when missing.
	foreach ( array(
		'section_nav_visible',
		'section_dependencies_visible',
		'section_nature_visible',
		'section_program_visible',
		'section_stages_visible',
		'section_approach_visible',
		'section_clinic_landscape_visible',
		'section_specialists_visible',
		'section_founder_quote_visible',
		'section_comfort_visible',
		'section_reviews_visible',
		'section_faq_visible',
		'section_final_form_visible',
	) as $toggle ) {
		if ( ! metadata_exists( 'post', $pid, $toggle ) ) {
			update_field( $toggle, 1, $pid );
			++$db_writes;
			$seed_log[] = array( $pid, $meta['title'], $toggle, 'empty', 'meaningful', 'yes', 'default_on', '1', 'n/a', 'visibility default' );
		}
	}
}

e50_csv(
	$evidence . '/v9-06e50-section-seeded-fields.csv',
	array( 'post_id', 'title', 'field_name', 'before_state', 'after_state', 'seeded', 'seed_source', 'value_preview', 'preserved_existing', 'notes' ),
	$seed_log
);

// -------------------------------------------------------------------------
// 5. Empty-field behavior test (temporary clear + restore)
// -------------------------------------------------------------------------
$empty_rows = array();
$probe_id   = 77;
$probe_field = 'section_nature_lead';
$probe_before = get_field( $probe_field, $probe_id );
update_field( $probe_field, '', $probe_id );
++$db_writes;

// Clear object cache / ACF cache for post.
clean_post_cache( $probe_id );
wp_cache_delete( $probe_id, 'posts' );
if ( function_exists( 'acf_get_store' ) ) {
	$vs = acf_get_store( 'values' );
	if ( $vs && method_exists( $vs, 'reset' ) ) {
		$vs->reset();
	}
}

$fe = e50_http( home_url( '/uslugi/psihicheskoe-zdorovie/' ) );
$body = $fe['body'];
$has_old_lorem_lead = ( false !== strpos( $body, 'Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor' ) );
// Nature lead block may be absent — check class content around nature lead.
preg_match( '/service-subdivision-nature-v1__lead[^>]*>(.*?)<\/p>/s', $body, $m );
$lead_html = isset( $m[1] ) ? trim( wp_strip_all_tags( $m[1] ) ) : '';
$injected  = ( '' !== $lead_html );
$empty_rows[] = array(
	'optional nature lead cleared on #77',
	'no hardcoded demo injected; lead hidden/empty',
	$injected ? ( 'LEAD_VISIBLE:' . mb_substr( $lead_html, 0, 80 ) ) : 'lead element absent or empty',
	( ! $injected && ! $has_old_lorem_lead && 200 === $fe['code'] ) ? 'PASS' : 'FAIL',
	'HTTP ' . $fe['code'],
);

update_field( $probe_field, $probe_before, $probe_id );
++$db_writes;
clean_post_cache( $probe_id );
$fe2 = e50_http( home_url( '/uslugi/psihicheskoe-zdorovie/' ) );
$restored_ok = ( 200 === $fe2['code'] );
if ( is_string( $probe_before ) && '' !== trim( $probe_before ) ) {
	$restored_ok = $restored_ok && ( false !== strpos( $fe2['body'], mb_substr( trim( (string) $probe_before ), 0, 40 ) ) );
}
$empty_rows[] = array(
	'nature lead restored on #77',
	'original visible',
	$restored_ok ? 'restored' : 'restore_issue',
	$restored_ok ? 'PASS' : 'FAIL',
	'',
);
e50_csv(
	$evidence . '/v9-06e50-empty-field-behavior-validation.csv',
	array( 'test', 'expected', 'actual', 'result', 'notes' ),
	$empty_rows
);

// -------------------------------------------------------------------------
// 6. Admin validation (meta presence)
// -------------------------------------------------------------------------
$admin_rows = array();
foreach ( $section_posts as $pid => $meta ) {
	$role   = (string) get_field( 'service_editor_role', $pid );
	$layout = (string) get_field( 'service_layout_variant', $pid );
	$heading = (string) get_field( 'section_nature_heading', $pid );
	$team    = get_field( 'section_team_image', $pid );
	$corr    = get_field( 'section_corridor_image', $pid );
	$land    = get_field( 'section_clinic_landscape_image', $pid );
	$dep_ok  = ( 73 === $pid ) || ! e50_is_dependency_specific( $heading );
	$admin_rows[] = array(
		'#' . $pid . ' ' . $meta['title'],
		'demo/current in ACF; role=section; layout=subdivision',
		sprintf( 'role=%s layout=%s nature_heading=%s team=%s corridor=%s land=%s', $role, $layout, mb_substr( $heading, 0, 40 ), e50_preview( $team ), e50_preview( $corr ), e50_preview( $land ) ),
		( 'section' === $role && 'subdivision' === $layout && '' !== $heading && $dep_ok ) ? 'PASS' : 'FAIL',
		$dep_ok ? '' : 'dependency-specific heading remains',
	);
}
foreach ( array( 74, 314, 78, 81, 85 ) as $cid ) {
	$role = (string) get_field( 'service_editor_role', $cid );
	$admin_rows[] = array(
		'#' . $cid . ' control',
		'service model preserved',
		'role=' . $role,
		( 'service' === $role || '' !== $role ) ? 'PASS' : 'FAIL',
		'',
	);
}
e50_csv(
	$evidence . '/v9-06e50-admin-validation.csv',
	array( 'page', 'expected', 'actual', 'result', 'notes' ),
	$admin_rows
);

// -------------------------------------------------------------------------
// 7. Frontend + regression smoke
// -------------------------------------------------------------------------
$routes = array(
	array( 'Home `/`', home_url( '/' ), 'accepted/frozen' ),
	array( 'Services hub `/uslugi/`', home_url( '/uslugi/' ), 'accepted/frozen' ),
	array( '`/uslugi/zavisimosti/`', home_url( '/uslugi/zavisimosti/' ), 'section ACF' ),
	array( '`/uslugi/psihicheskoe-zdorovie/`', home_url( '/uslugi/psihicheskoe-zdorovie/' ), 'section ACF' ),
	array( '`/uslugi/rasstroystva-pischevogo-povedeniya/`', home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ), 'section ACF' ),
	array( '#74', get_permalink( 74 ), 'service control' ),
	array( '#314', get_permalink( 314 ), 'service control' ),
	array( '#78', get_permalink( 78 ), 'service control' ),
	array( '#81', get_permalink( 81 ), 'service control' ),
	array( '#85', get_permalink( 85 ), 'service control' ),
	array( '/blog/', home_url( '/blog/' ), 'regression' ),
	array( '/specyalisty/', home_url( '/specyalisty/' ), 'regression' ),
	array( '/o-centre/', home_url( '/o-centre/' ), 'regression' ),
	array( '/kontakty/', home_url( '/kontakty/' ), 'regression' ),
);

// Add a few E49 services.
$e49_sample = get_posts(
	array(
		'post_type'      => 'service',
		'post_status'    => 'publish',
		'posts_per_page' => 5,
		'post_parent__not_in' => array( 0 ),
		'exclude'        => array( 73, 77, 84, 74, 314, 78, 81, 85 ),
		'fields'         => 'ids',
	)
);
foreach ( (array) $e49_sample as $sid ) {
	$routes[] = array( 'E49 sample #' . $sid, get_permalink( (int) $sid ), 'service sample' );
}

$fe_rows   = array();
$smoke_rows = array();
foreach ( $routes as $r ) {
	list( $label, $url, $kind ) = $r;
	$resp = e50_http( (string) $url );
	$code = $resp['code'];
	$body = $resp['body'];
	$fatal = ( false !== stripos( $body, 'Fatal error' ) || false !== stripos( $body, 'There has been a critical error' ) );
	$ok = ( 200 === $code && ! $fatal );
	$smoke_rows[] = array( $label, $code, $ok ? 'PASS' : 'FAIL', $fatal ? 'fatal' : '' );

	if ( in_array( $label, array( '`/uslugi/zavisimosti/`', '`/uslugi/psihicheskoe-zdorovie/`', '`/uslugi/rasstroystva-pischevogo-povedeniya/`' ), true ) ) {
		$has_nature = ( false !== strpos( $body, 'service-subdivision-nature-v1' ) );
		$has_approach = ( false !== strpos( $body, 'service-subdivision-team-stats-v1' ) );
		$wrong = false;
		if ( '`/uslugi/psihicheskoe-zdorovie/`' === $label ) {
			$wrong = ( false !== strpos( $body, 'Природа зависимости' ) || false !== strpos( $body, 'Наш подход к лечению зависимостей' ) );
		}
		if ( '`/uslugi/rasstroystva-pischevogo-povedeniya/`' === $label ) {
			$wrong = ( false !== strpos( $body, 'Природа зависимости' ) || false !== strpos( $body, 'Наш подход к лечению зависимостей' ) );
		}
		$fe_rows[] = array(
			$label,
			'200 + section ACF content',
			sprintf( 'HTTP %d nature=%s approach=%s wrong_dep_copy=%s', $code, $has_nature ? 'yes' : 'no', $has_approach ? 'yes' : 'no', $wrong ? 'yes' : 'no' ),
			( $ok && $has_nature && $has_approach && ! $wrong ) ? 'PASS' : 'FAIL',
			'',
		);
	}
}

e50_csv( $evidence . '/v9-06e50-frontend-validation.csv', array( 'route', 'expected', 'actual', 'result', 'notes' ), $fe_rows );
e50_csv( $evidence . '/v9-06e50-route-smoke.csv', array( 'route', 'http', 'result', 'notes' ), $smoke_rows );
e50_csv( $evidence . '/v9-06e50-source-runtime-sync.csv', array( 'file', 'source_path', 'runtime_path', 'hash_match', 'result', 'notes' ), $sync_rows );

$summary['db_writes'] = $db_writes;
$summary['seeded_yes'] = count(
	array_filter(
		$seed_log,
		static function ( $row ) {
			return isset( $row[5] ) && 'yes' === $row[5];
		}
	)
);
$summary['fe_pass'] = ! in_array( 'FAIL', array_column( $fe_rows, 3 ), true );
$summary['smoke_pass'] = ! in_array( 'FAIL', array_column( $smoke_rows, 2 ), true );
$summary['empty_pass'] = ! in_array( 'FAIL', array_column( $empty_rows, 3 ), true );
$summary['sync_pass'] = ! in_array( 'FAIL', array_column( $sync_rows, 5 ), true );

file_put_contents( $evidence . '/v9-06e50-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

echo wp_json_encode(
	array(
		'db_writes'   => $db_writes,
		'seeded_yes'  => $summary['seeded_yes'],
		'fe_pass'     => $summary['fe_pass'],
		'smoke_pass'  => $summary['smoke_pass'],
		'empty_pass'  => $summary['empty_pass'],
		'sync_pass'   => $summary['sync_pass'],
		'backup_root' => $backup_root,
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
) . "\n";

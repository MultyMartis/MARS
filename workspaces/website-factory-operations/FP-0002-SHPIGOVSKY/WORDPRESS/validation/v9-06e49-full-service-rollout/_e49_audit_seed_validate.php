<?php
/**
 * V9-06E49 — Full service rollout: backup exports, inventory, audit, seed, validate.
 *
 * Rules:
 * - No alcohol copy-paste into non-alcohol pages.
 * - Seed only empty fields; preserve meaningful values.
 * - Controls #74/#314/#78/#81/#85 validate-only (mutate only if critical missing).
 * - Sections #73/#77/#84 excluded.
 * - ACF SoT; emergency PHP fallback remains safety-only.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
}

if ( ! function_exists( 'update_field' ) || ! function_exists( 'get_field' ) ) {
	fwrite( STDERR, "ACF missing\n" );
	exit( 1 );
}

$evidence_dir  = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$bak_path_file = $evidence_dir . '/v9-06e49-backup-path.txt';
$backup_root   = is_file( $bak_path_file ) ? trim( (string) file_get_contents( $bak_path_file ) ) : '';
if ( '' === $backup_root || ! is_dir( $backup_root ) ) {
	fwrite( STDERR, "STOP — backup root missing\n" );
	exit( 2 );
}

$db_writes = 0;
$seed_log  = array();
$summary   = array(
	'backup_root' => $backup_root,
	'db_writes'   => 0,
	'targets'     => array(),
	'controls'    => array(),
);

$section_ids  = array( 73, 77, 84 );
$control_ids  = array( 74, 314, 78, 81, 85 );
$accepted_base = 74;

/**
 * CSV helper.
 *
 * @param resource $fp File.
 * @param array    $row Row.
 * @return void
 */
function e49_fputcsv( $fp, array $row ) {
	fputcsv( $fp, $row );
}

/**
 * HTTP fetch.
 *
 * @param string $url URL.
 * @return array{code:int,body:string,error:string}
 */
function e49_http_get( $url ) {
	if ( ! function_exists( 'curl_init' ) ) {
		return array( 'code' => 0, 'body' => '', 'error' => 'curl_missing' );
	}
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 30,
			CURLOPT_SSL_VERIFYPEER => false,
		)
	);
	$body = (string) curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	$err  = (string) curl_error( $ch );
	curl_close( $ch );
	return array( 'code' => $code, 'body' => $body, 'error' => $err );
}

/**
 * Value state classifier.
 *
 * @param mixed $value Value.
 * @return string
 */
function e49_value_state( $value ) {
	if ( null === $value || false === $value || '' === $value || array() === $value ) {
		return 'empty';
	}
	if ( is_array( $value ) ) {
		$flat = wp_json_encode( $value );
		if ( false !== stripos( (string) $flat, 'DEMO' ) || false !== stripos( (string) $flat, 'Lorem ipsum' ) ) {
			return 'demo';
		}
		return count( $value ) > 0 ? 'meaningful' : 'empty';
	}
	$s = (string) $value;
	if ( '' === trim( $s ) ) {
		return 'empty';
	}
	if ( false !== stripos( $s, 'DEMO' ) || false !== stripos( $s, 'Lorem ipsum' ) ) {
		return 'demo';
	}
	return 'meaningful';
}

/**
 * Empty check for seeding.
 *
 * @param mixed $existing Existing.
 * @return bool
 */
function e49_is_empty( $existing ) {
	if ( null === $existing || false === $existing || '' === $existing || array() === $existing ) {
		return true;
	}
	if ( is_numeric( $existing ) && (int) $existing === 0 && ! is_string( $existing ) ) {
		return true;
	}
	if ( is_array( $existing ) ) {
		if ( isset( $existing['ID'] ) || isset( $existing['id'] ) ) {
			$id = isset( $existing['ID'] ) ? (int) $existing['ID'] : (int) $existing['id'];
			return $id <= 0;
		}
		return count( $existing ) === 0;
	}
	return false;
}

/**
 * Seed if empty.
 *
 * @param int    $post_id Post.
 * @param string $field Field.
 * @param mixed  $value Value.
 * @param string $note Note.
 * @param string $source Source label.
 * @return string
 */
function e49_seed_if_empty( $post_id, $field, $value, $note = '', $source = 'neutral_demo' ) {
	global $db_writes, $seed_log;

	$existing = get_field( $field, $post_id );
	if ( metadata_exists( 'post', $post_id, $field ) ) {
		$raw = get_post_meta( $post_id, $field, true );
		if ( '0' === (string) $raw || 0 === $raw || false === $raw || '1' === (string) $raw || 1 === $raw ) {
			if ( str_ends_with( $field, '_visible' ) ) {
				$seed_log[] = array(
					'post_id'     => $post_id,
					'field_name'  => $field,
					'action'      => 'preserved',
					'seed_source' => $source,
					'notes'       => $note . ' (toggle already set)',
					'preview'     => (string) $raw,
				);
				return 'preserved';
			}
		}
	}

	if ( ! e49_is_empty( $existing ) ) {
		$seed_log[] = array(
			'post_id'     => $post_id,
			'field_name'  => $field,
			'action'      => 'preserved',
			'seed_source' => $source,
			'notes'       => $note,
			'preview'     => is_scalar( $existing ) ? substr( (string) $existing, 0, 100 ) : 'non-scalar',
		);
		return 'preserved';
	}

	$ok = update_field( $field, $value, $post_id );
	++$db_writes;
	$seed_log[] = array(
		'post_id'     => $post_id,
		'field_name'  => $field,
		'action'      => $ok ? 'seeded' : 'seed_failed',
		'seed_source' => $source,
		'notes'       => $note,
		'preview'     => is_scalar( $value ) ? substr( (string) $value, 0, 100 ) : ( is_array( $value ) ? 'array:' . count( $value ) : gettype( $value ) ),
	);
	return $ok ? 'seeded' : 'seed_failed';
}

/**
 * Top-level section title for a service.
 *
 * @param WP_Post $post Post.
 * @return string
 */
function e49_parent_section_title( WP_Post $post ) {
	$cur = $post->post_parent ? get_post( (int) $post->post_parent ) : null;
	while ( $cur && (int) $cur->post_parent > 0 ) {
		$cur = get_post( (int) $cur->post_parent );
	}
	return $cur ? (string) $cur->post_title : '';
}

/**
 * Build neutral page-specific demo pack (no alcohol copy).
 *
 * @param WP_Post $post Post.
 * @return array
 */
function e49_neutral_demo_pack( WP_Post $post ) {
	$title   = trim( $post->post_title );
	$section = e49_parent_section_title( $post );
	$ctx     = $section ? ( $title . ' / ' . $section ) : $title;

	return array(
		'intro_heading'   => sprintf( '%s — состояние, с которым можно работать системно и бережно.', $title ),
		'intro_highlight' => 'DEMO — ЭТО НЕ ПРИГОВОР. ЭТО СОСТОЯНИЕ, КОТОРОЕ ПОДДАЁТСЯ ЛЕЧЕНИЮ ПРИ ПОДХОДЯЩЕЙ ПОДДЕРЖКЕ.',
		'bordered'        => array(
			array(
				'heading' => 'ПОЧЕМУ ВАЖНО ОБРАТИТЬСЯ ВОВРЕМЯ',
				'text'    => sprintf( 'DEMO — страница «%s». Раннее обращение помогает снизить риск осложнений и подобрать более мягкий маршрут помощи. Текст демонстрационный и ожидает согласования оператором.', $ctx ),
			),
			array(
				'heading' => 'МЫ РАБОТАЕМ БЕЗ ОСУЖДЕНИЯ',
				'text'    => 'DEMO — команда центра помогает разобраться в симптомах, триггерах и доступных вариантах терапии. Материал не является медицинской рекомендацией.',
			),
			array(
				'heading' => 'ИНДИВИДУАЛЬНЫЙ МАРШРУТ',
				'text'    => 'DEMO — программа подбирается после первичной консультации с учётом состояния, сопутствующих факторов и целей пациента и семьи.',
			),
		),
		'signs_heading'   => sprintf( 'Признаки, на которые стоит обратить внимание (%s)', $title ),
		'signs_intro'     => sprintf( 'DEMO — если вы замечаете у себя или близкого изменения, связанные с запросом «%s», имеет смысл обсудить это со специалистом.', $title ),
		'signs_items'     => array(
			array( 'text' => 'DEMO — симптомы стали чаще или заметно сильнее, чем раньше.' ),
			array( 'text' => 'DEMO — состояние мешает работе, учёбе или отношениям.' ),
			array( 'text' => 'DEMO — появляются мысли о безысходности или избегании привычных дел.' ),
			array( 'text' => 'DEMO — самостоятельные попытки «справиться» не дают устойчивого эффекта.' ),
			array( 'text' => 'DEMO — близкие выражают тревогу и просят обратиться за помощью.' ),
		),
		'signs_editorial' => sprintf(
			"DEMO — краткий редакционный блок для страницы «%s».\n\nЗдесь может быть развёрнутый комментарий специалиста о том, как распознать проблему раньше и почему важно не откладывать консультацию. Текст демонстрационный, финальная редакция согласуется оператором.",
			$title
		),
		'approach_heading'    => sprintf( 'Наш подход к работе с запросом «%s»', $title ),
		'approach_highlight'  => 'DEMO — МЫ СОЧЕТАЕМ ДИАГНОСТИКУ, ТЕРАПИЮ И ПОДДЕРЖКУ СЕМЬИ.',
		'approach_intro'      => sprintf( 'DEMO — помощь по направлению «%s» строится как команда: оценка специалиста, психотерапия и сопровождение. Это демонстрационный текст.', $title ),
		'approach_more_label' => 'подробнее',
		'approach_more_url'   => home_url( '/o-centre/programma-lecheniya/' ),
		'approach_cards'      => array(
			array(
				'title' => 'диагностика состояния',
				'text'  => 'DEMO — первичная оценка симптомов, истории и рисков, чтобы выбрать безопасный старт.',
			),
			array(
				'title' => 'персональный план',
				'text'  => 'DEMO — маршрут терапии и сопровождения формируется под конкретную ситуацию.',
			),
			array(
				'title' => 'психотерапевтическая поддержка',
				'text'  => 'DEMO — работа с триггерами, навыками саморегуляции и устойчивыми изменениями.',
			),
			array(
				'title' => 'вовлечение близких',
				'text'  => 'DEMO — при согласии пациента семья получает понятные ориентиры, как помогать без давления.',
			),
		),
		'program_heading' => 'Наша программа включает 4 направления',
		'program_more'    => 'подробнее',
		'program_lead'    => sprintf( 'DEMO — программа для «%s»: медицинская, психотерапевтическая, социальная и поддержка после основного этапа.', $title ),
		'program_intros'  => array(
			array( 'text' => sprintf( 'DEMO — на странице «%s» показана структура программы центра. Финальные формулировки согласуются отдельно.', $title ) ),
			array( 'text' => 'DEMO — направления можно адаптировать под амбулаторный или стационарный формат после консультации.' ),
		),
		'stages_heading'         => 'Что нужно для начала работы с нами',
		'stages_lead'            => 'DEMO — мы соблюдаем конфиденциальность и уважение к границам пациента. Ниже — демонстрационные шаги.',
		'stages_items'           => array(
			array(
				'title'   => 'Связаться с нами',
				'text'    => 'DEMO — расскажите о ситуации коротко; специалист поможет понять следующий шаг.',
				'enabled' => 1,
			),
			array(
				'title'   => 'Консультация',
				'text'    => 'DEMO — разбор симптомов, целей и возможных форматов помощи.',
				'enabled' => 1,
			),
			array(
				'title'   => 'План лечения',
				'text'    => 'DEMO — согласование маршрута, длительности и роли команды.',
				'enabled' => 1,
			),
			array(
				'title'   => 'Сопровождение',
				'text'    => 'DEMO — поддержка на основном этапе и после него.',
				'enabled' => 1,
			),
		),
		'stages_support_heading' => 'Поддержка осуществляется на всех этапах:',
		'stages_support_items'   => array(
			array( 'text' => 'DEMO — первичная ориентация и clarification запроса;' ),
			array( 'text' => 'DEMO — медицинская и психотерапевтическая линия по показаниям;' ),
			array( 'text' => 'DEMO — работа с семьёй при согласии пациента;' ),
			array( 'text' => 'DEMO — рекомендации по поддержанию результата.' ),
		),
		'faq_heading' => 'Нас часто спрашивают',
		'faq_items'   => array(
			array(
				'question' => sprintf( 'С чего начать, если беспокоит «%s»?', $title ),
				'answer'   => "DEMO — начните с консультации: специалист поможет оценить состояние и предложить безопасный следующий шаг.\n\nЭто демонстрационный ответ, не медицинская рекомендация.",
			),
			array(
				'question' => 'Нужна ли госпитализация?',
				'answer'   => 'DEMO — формат зависит от тяжести состояния и рисков. Решение принимается после оценки специалиста.',
			),
			array(
				'question' => 'Можно ли приехать с родственником?',
				'answer'   => 'DEMO — да, близкие могут участвовать в согласованном формате, если это полезно пациенту.',
			),
		),
	);
}

/**
 * Alcohol-marker scan.
 *
 * @param mixed $value Value.
 * @return bool
 */
function e49_has_alcohol_markers( $value ) {
	$s = is_scalar( $value ) ? (string) $value : (string) wp_json_encode( $value );
	$s = function_exists( 'mb_strtolower' ) ? mb_strtolower( $s ) : strtolower( $s );
	$markers = array( 'алкогол', 'выпит', 'пьян', 'трезв', 'запой', 'алкоголик' );
	foreach ( $markers as $m ) {
		if ( false !== strpos( $s, $m ) ) {
			return true;
		}
	}
	return false;
}

/**
 * Ensure role/layout.
 *
 * @param int $post_id ID.
 * @return void
 */
function e49_ensure_role_layout( $post_id ) {
	global $db_writes, $seed_log;
	$role = (string) get_post_meta( $post_id, 'service_editor_role', true );
	if ( 'service' !== $role ) {
		update_post_meta( $post_id, 'service_editor_role', 'service' );
		++$db_writes;
		$seed_log[] = array(
			'post_id'     => $post_id,
			'field_name'  => 'service_editor_role',
			'action'      => 'seeded',
			'seed_source' => 'role_layout',
			'notes'       => 'ensure service role',
			'preview'     => 'service',
		);
	}
	$layout = (string) get_post_meta( $post_id, 'service_layout_variant', true );
	if ( 'service_general' !== $layout && 'alcohol_special' !== $layout ) {
		update_post_meta( $post_id, 'service_layout_variant', 'service_general' );
		++$db_writes;
		$seed_log[] = array(
			'post_id'     => $post_id,
			'field_name'  => 'service_layout_variant',
			'action'      => 'seeded',
			'seed_source' => 'role_layout',
			'notes'       => 'ensure service_general layout',
			'preview'     => 'service_general',
		);
	}
}

/**
 * Seed a service with neutral pack.
 *
 * @param int  $post_id ID.
 * @param bool $control_only Control mode.
 * @return void
 */
function e49_seed_service( $post_id, $control_only = false ) {
	$post = get_post( $post_id );
	if ( ! $post || 'service' !== $post->post_type ) {
		return;
	}

	e49_ensure_role_layout( $post_id );

	if ( $control_only ) {
		e49_seed_if_empty( $post_id, 'service_general_team_image', 1238, 'control image if missing', 'accepted_demo_image' );
		e49_seed_if_empty( $post_id, 'service_general_clinic_landscape_image', 1239, 'control image if missing', 'accepted_demo_image' );
		e49_seed_if_empty( $post_id, 'service_general_corridor_image', 1709, 'control image if missing', 'accepted_demo_image' );
		return;
	}

	$pack = e49_neutral_demo_pack( $post );

	e49_seed_if_empty( $post_id, 'service_general_intro_heading', $pack['intro_heading'], 'page-specific neutral demo', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_intro_highlight', $pack['intro_highlight'], 'neutral demo highlight', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_bordered_info_items', $pack['bordered'], 'neutral bordered', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_signs_heading', $pack['signs_heading'], 'neutral signs', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_signs_intro', $pack['signs_intro'], 'neutral signs', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_signs_items', $pack['signs_items'], 'neutral signs', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_signs_editorial', $pack['signs_editorial'], 'neutral signs editorial', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_approach_heading', $pack['approach_heading'], 'neutral approach', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_approach_highlight', $pack['approach_highlight'], 'neutral approach', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_approach_intro', $pack['approach_intro'], 'neutral approach', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_approach_more_label', $pack['approach_more_label'], 'neutral approach link', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_approach_more_url', $pack['approach_more_url'], 'neutral approach link', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_approach_cards', $pack['approach_cards'], 'neutral approach cards', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_team_image', 1238, 'shared accepted demo image', 'accepted_demo_image' );
	e49_seed_if_empty( $post_id, 'service_general_clinic_landscape_image', 1239, 'shared accepted demo image', 'accepted_demo_image' );
	e49_seed_if_empty( $post_id, 'service_general_corridor_image', 1709, 'shared accepted demo image', 'accepted_demo_image' );
	e49_seed_if_empty( $post_id, 'service_general_program_heading', $pack['program_heading'], 'neutral program', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_program_more_label', $pack['program_more'], 'neutral program', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_program_lead', $pack['program_lead'], 'neutral program', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_program_intro_items', $pack['program_intros'], 'neutral program', 'page_title_demo' );
	e49_seed_if_empty( $post_id, 'service_general_stages_heading', $pack['stages_heading'], 'neutral stages', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_stages_lead', $pack['stages_lead'], 'neutral stages', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_stages_items', $pack['stages_items'], 'neutral stages', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_stages_support_heading', $pack['stages_support_heading'], 'neutral stages', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_stages_support_items', $pack['stages_support_items'], 'neutral stages', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_faq_heading', $pack['faq_heading'], 'neutral faq', 'neutral_demo' );
	e49_seed_if_empty( $post_id, 'service_general_faq_items', $pack['faq_items'], 'neutral faq', 'page_title_demo' );

	if ( ! metadata_exists( 'post', $post_id, 'service_general_specialists_visible' ) ) {
		update_field( 'service_general_specialists_visible', 0, $post_id );
		global $db_writes, $seed_log;
		++$db_writes;
		$seed_log[] = array(
			'post_id'     => $post_id,
			'field_name'  => 'service_general_specialists_visible',
			'action'      => 'seeded',
			'seed_source' => 'historic_layout',
			'notes'       => 'preserve no-specialists leaf layout',
			'preview'     => '0',
		);
	}

	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_parent'    => $post_id,
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'fields'         => 'ids',
		)
	);
	if ( ! empty( $children ) && ! metadata_exists( 'post', $post_id, 'service_general_children_visible' ) ) {
		update_field( 'service_general_children_visible', 1, $post_id );
		global $db_writes, $seed_log;
		++$db_writes;
		$seed_log[] = array(
			'post_id'     => $post_id,
			'field_name'  => 'service_general_children_visible',
			'action'      => 'seeded',
			'seed_source' => 'automatic_children',
			'notes'       => 'keep automatic child tiles visible',
			'preview'     => '1',
		);
	}
}

/**
 * Depth helper.
 *
 * @param int $id Post ID.
 * @return int
 */
function e49_depth( $id ) {
	if ( function_exists( 'shpigovsky_get_service_depth' ) ) {
		return (int) shpigovsky_get_service_depth( $id );
	}
	$depth = 1;
	$walk  = (int) get_post_field( 'post_parent', $id );
	while ( $walk > 0 && $depth < 10 ) {
		++$depth;
		$walk = (int) get_post_field( 'post_parent', $walk );
	}
	return $depth;
}

/**
 * Has published children.
 *
 * @param int $id Post ID.
 * @return bool
 */
function e49_has_children( $id ) {
	$kids = get_posts(
		array(
			'post_type'      => 'service',
			'post_parent'    => $id,
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'fields'         => 'ids',
		)
	);
	return ! empty( $kids );
}

/**
 * Effective layout classification.
 *
 * @param int    $id ID.
 * @param string $role Role.
 * @param string $layout Layout meta.
 * @return string
 */
function e49_effective_layout( $id, $role, $layout ) {
	if ( in_array( $id, array( 73, 77, 84 ), true ) || 'section' === $role ) {
		return 'subdivision';
	}
	if ( 'service_general' === $layout || 'alcohol_special' === $layout || '' === $layout || 'service' === $role ) {
		return 'service_general';
	}
	return $layout ?: 'unknown';
}

/**
 * Seed state label.
 *
 * @param int    $id ID.
 * @param string $status Status.
 * @param string $role Role.
 * @param string $eff Effective layout.
 * @return string
 */
function e49_seed_state( $id, $status, $role, $eff ) {
	global $section_ids, $control_ids, $accepted_base;
	if ( 'trash' === $status ) {
		return 'trashed_excluded';
	}
	if ( in_array( $id, $section_ids, true ) || 'section' === $role || 'subdivision' === $eff ) {
		return 'section_excluded';
	}
	if ( 'service_general' !== $eff ) {
		return 'not_service_general';
	}
	if ( $id === $accepted_base ) {
		return 'accepted_base';
	}
	if ( in_array( $id, $control_ids, true ) ) {
		return 'representative_done';
	}
	return 'remaining_target';
}

// ---------------------------------------------------------------------------
// 0) Backup exports: postmeta + post_content for all service CPT
// ---------------------------------------------------------------------------
$services_all = get_posts(
	array(
		'post_type'      => 'service',
		'post_status'    => array( 'publish', 'draft', 'private', 'trash' ),
		'posts_per_page' => -1,
		'orderby'        => array(
			'parent'     => 'ASC',
			'menu_order' => 'ASC',
			'ID'         => 'ASC',
		),
	)
);

$meta_dir = $backup_root . '/exports/postmeta';
$content_dir = $backup_root . '/exports/post_content';
if ( ! is_dir( $meta_dir ) ) {
	wp_mkdir_p( $meta_dir );
}
if ( ! is_dir( $content_dir ) ) {
	wp_mkdir_p( $content_dir );
}

$inv_csv_bak = $backup_root . '/exports/full-service-inventory-before.csv';
$inv_bak_fp  = fopen( $inv_csv_bak, 'wb' );
e49_fputcsv( $inv_bak_fp, array( 'post_id', 'title', 'slug', 'url', 'post_status', 'parent_id', 'depth', 'role', 'layout' ) );

foreach ( $services_all as $svc ) {
	$id = (int) $svc->ID;
	e49_fputcsv(
		$inv_bak_fp,
		array(
			$id,
			$svc->post_title,
			$svc->post_name,
			get_permalink( $id ),
			$svc->post_status,
			(int) $svc->post_parent,
			e49_depth( $id ),
			(string) get_post_meta( $id, 'service_editor_role', true ),
			(string) get_post_meta( $id, 'service_layout_variant', true ),
		)
	);

	$meta = get_post_meta( $id );
	$mfp  = fopen( $meta_dir . '/post-' . $id . '-postmeta.tsv', 'wb' );
	fwrite( $mfp, "meta_key\tmeta_value\n" );
	foreach ( $meta as $mk => $vals ) {
		foreach ( (array) $vals as $mv ) {
			fwrite( $mfp, $mk . "\t" . str_replace( array( "\r", "\n", "\t" ), array( '\\r', '\\n', '\\t' ), (string) $mv ) . "\n" );
		}
	}
	fclose( $mfp );
	file_put_contents( $content_dir . '/post-' . $id . '-content.txt', (string) $svc->post_content );
}
fclose( $inv_bak_fp );
echo "BACKUP_EXPORTS_DONE services=" . count( $services_all ) . "\n";

// ---------------------------------------------------------------------------
// 0b) Frontend snapshots BEFORE
// ---------------------------------------------------------------------------
$snap_dir = $backup_root . '/frontend';
if ( ! is_dir( $snap_dir ) ) {
	wp_mkdir_p( $snap_dir );
}

$snap_routes = array(
	'home'         => home_url( '/' ),
	'uslugi'       => home_url( '/uslugi/' ),
	'zavisimosti'  => home_url( '/uslugi/zavisimosti/' ),
	'psihicheskoe' => home_url( '/uslugi/psihicheskoe-zdorovie/' ),
	'rpp'          => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ),
	'blog'         => home_url( '/blog/' ),
	'specyalisty'  => home_url( '/specyalisty/' ),
	'o-centre'     => home_url( '/o-centre/' ),
	'kontakty'     => home_url( '/kontakty/' ),
);
foreach ( array( 74, 314, 78, 81, 85, 73, 77, 84 ) as $pid ) {
	$snap_routes[ 'p' . $pid ] = get_permalink( $pid );
}
// All remaining targets snapshotted after inventory classification.

echo "SNAPSHOT_CORE_ROUTES_START\n";
foreach ( $snap_routes as $name => $url ) {
	$r = e49_http_get( $url );
	file_put_contents( $snap_dir . '/' . $name . '.html', $r['body'] );
	echo "SNAP {$name} HTTP={$r['code']}\n";
}

// ---------------------------------------------------------------------------
 // 1) Full service inventory + target selection
// ---------------------------------------------------------------------------
$services = get_posts(
	array(
		'post_type'      => 'service',
		'post_status'    => array( 'publish', 'draft', 'private' ),
		'posts_per_page' => -1,
		'orderby'        => array(
			'parent'     => 'ASC',
			'menu_order' => 'ASC',
			'ID'         => 'ASC',
		),
	)
);

$inv_fp = fopen( $evidence_dir . '/v9-06e49-full-service-inventory.csv', 'wb' );
e49_fputcsv(
	$inv_fp,
	array(
		'post_id',
		'title',
		'slug',
		'url',
		'post_status',
		'parent_id',
		'parent_title',
		'depth',
		'has_children',
		'editor_role',
		'effective_layout',
		'current_acf_seed_state',
		'selected_for_e49',
		'notes',
	)
);

$targets = array();
foreach ( $services as $svc ) {
	$id        = (int) $svc->ID;
	$parent_id = (int) $svc->post_parent;
	$parent    = $parent_id ? get_post( $parent_id ) : null;
	$role      = (string) get_post_meta( $id, 'service_editor_role', true );
	$layout    = (string) get_post_meta( $id, 'service_layout_variant', true );
	$eff       = e49_effective_layout( $id, $role, $layout );
	$state     = e49_seed_state( $id, $svc->post_status, $role, $eff );
	$selected  = ( 'remaining_target' === $state ) ? 'yes' : 'no';
	$notes     = '';
	if ( 'remaining_target' === $state ) {
		$targets[] = $id;
		$notes     = 'E49 remaining service_general target';
	} elseif ( 'representative_done' === $state ) {
		$notes = 'E48 representative — validate only';
	} elseif ( 'accepted_base' === $state ) {
		$notes = 'E47 accepted base — validate only';
	}

	e49_fputcsv(
		$inv_fp,
		array(
			$id,
			$svc->post_title,
			$svc->post_name,
			get_permalink( $id ),
			$svc->post_status,
			$parent_id,
			$parent ? $parent->post_title : '',
			e49_depth( $id ),
			e49_has_children( $id ) ? 'yes' : 'no',
			$role,
			$eff,
			$state,
			$selected,
			$notes,
		)
	);
}
fclose( $inv_fp );

// Cap safety: project expected ~20-25 remaining.
if ( count( $targets ) > 40 ) {
	fwrite( STDERR, 'STOP — unexpected target count: ' . count( $targets ) . "\n" );
	exit( 3 );
}

$tgt_fp = fopen( $evidence_dir . '/v9-06e49-target-services.csv', 'wb' );
e49_fputcsv( $tgt_fp, array( 'post_id', 'title', 'url', 'parent_section', 'depth', 'has_children', 'reason_selected', 'rollout_action', 'notes' ) );
foreach ( $targets as $id ) {
	$p = get_post( $id );
	e49_fputcsv(
		$tgt_fp,
		array(
			$id,
			$p ? $p->post_title : '',
			$p ? get_permalink( $id ) : '',
			$p ? e49_parent_section_title( $p ) : '',
			e49_depth( $id ),
			e49_has_children( $id ) ? 'yes' : 'no',
			'service_general remaining after E48 controls',
			'seed_missing_acf_neutral_preserve_existing',
			'',
		)
	);
	// Snapshot remaining targets before seed.
	$r = e49_http_get( get_permalink( $id ) );
	file_put_contents( $snap_dir . '/p' . $id . '.html', $r['body'] );
}
fclose( $tgt_fp );
$summary['targets'] = $targets;
echo 'TARGETS=' . implode( ',', $targets ) . " count=" . count( $targets ) . "\n";

// ---------------------------------------------------------------------------
// 2) Field completeness BEFORE + copy-paste risk
// ---------------------------------------------------------------------------
$parity_fields  = acf_get_fields( 'group_fp02_service_general_parity' );
$editable_names = array();
if ( is_array( $parity_fields ) ) {
	foreach ( $parity_fields as $f ) {
		if ( empty( $f['name'] ) || 'message' === ( $f['type'] ?? '' ) ) {
			continue;
		}
		$editable_names[] = array(
			'name' => (string) $f['name'],
			'type' => (string) ( $f['type'] ?? '' ),
		);
	}
}

$comp_fp = fopen( $evidence_dir . '/v9-06e49-field-completeness-before.csv', 'wb' );
e49_fputcsv(
	$comp_fp,
	array(
		'post_id',
		'title',
		'field_name',
		'field_type',
		'current_value_state',
		'existing_value_preview',
		'seed_required',
		'proposed_seed_source',
		'preserve_existing',
		'notes',
	)
);

$risk_fp = fopen( $evidence_dir . '/v9-06e49-copy-paste-risk-before.csv', 'wb' );
e49_fputcsv(
	$risk_fp,
	array(
		'post_id',
		'title',
		'parent_section',
		'risky_source_detected',
		'alcohol_terms_present_before',
		'alcohol_terms_expected',
		'action',
		'notes',
	)
);

$scan_fields = array(
	'service_general_intro_heading',
	'service_general_intro_highlight',
	'service_general_signs_heading',
	'service_general_signs_intro',
	'service_general_signs_editorial',
	'service_general_approach_heading',
	'service_general_approach_highlight',
	'service_general_approach_intro',
	'service_general_program_lead',
	'service_general_stages_lead',
	'service_general_faq_heading',
	'service_general_bordered_info_items',
	'service_general_signs_items',
	'service_general_approach_cards',
	'service_general_program_intro_items',
	'service_general_stages_items',
	'service_general_stages_support_items',
	'service_general_faq_items',
);

foreach ( $targets as $id ) {
	$p     = get_post( $id );
	$title = $p ? $p->post_title : '';
	foreach ( $editable_names as $info ) {
		$fname = $info['name'];
		$val   = get_field( $fname, $id );
		$state = e49_value_state( $val );
		if ( 'empty' === $state && metadata_exists( 'post', $id, $fname ) && '0' === (string) get_post_meta( $id, $fname, true ) ) {
			$state = 'meaningful';
		}
		if ( str_ends_with( $fname, '_visible' ) && metadata_exists( 'post', $id, $fname ) ) {
			$state = 'meaningful';
		}
		$preview = is_scalar( $val ) ? substr( (string) $val, 0, 80 ) : ( is_array( $val ) ? 'array:' . count( $val ) : '' );
		$seed_req = ( 'empty' === $state ) ? 'yes' : 'no';
		$preserve = ( 'empty' === $state ) ? 'no' : 'yes';
		$source   = 'page_title_or_neutral_demo';
		e49_fputcsv(
			$comp_fp,
			array( $id, $title, $fname, $info['type'], $state, $preview, $seed_req, $source, $preserve, '' )
		);
	}

	$alc_before = false;
	foreach ( $scan_fields as $fname ) {
		if ( e49_has_alcohol_markers( get_field( $fname, $id ) ) ) {
			$alc_before = true;
			break;
		}
	}
	e49_fputcsv(
		$risk_fp,
		array(
			$id,
			$title,
			$p ? e49_parent_section_title( $p ) : '',
			'no',
			$alc_before ? 'yes' : 'no',
			'no',
			$alc_before ? 'STOP_investigate_before_seed' : 'seed_neutral_page_specific_demo',
			$alc_before ? 'alcohol markers already present' : 'safe for neutral seed',
		)
	);
	if ( $alc_before ) {
		fwrite( STDERR, "STOP — alcohol markers before seed on #{$id}\n" );
		exit( 4 );
	}
}
fclose( $comp_fp );
fclose( $risk_fp );

// ---------------------------------------------------------------------------
// 3) SEED remaining targets; validate-only controls
// ---------------------------------------------------------------------------
foreach ( $control_ids as $id ) {
	e49_seed_service( (int) $id, true );
	$summary['controls'][] = $id;
}
foreach ( $targets as $id ) {
	e49_seed_service( (int) $id, false );
}

$seed_fp = fopen( $evidence_dir . '/v9-06e49-seeded-fields.csv', 'wb' );
e49_fputcsv( $seed_fp, array( 'post_id', 'field_name', 'action', 'seed_source', 'notes', 'preview' ) );
foreach ( $seed_log as $row ) {
	e49_fputcsv(
		$seed_fp,
		array( $row['post_id'], $row['field_name'], $row['action'], $row['seed_source'], $row['notes'], $row['preview'] )
	);
}
fclose( $seed_fp );

// ---------------------------------------------------------------------------
// 4) Admin validation
// ---------------------------------------------------------------------------
require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/post.php';
if ( ! defined( 'WP_ADMIN' ) ) {
	define( 'WP_ADMIN', true );
}

$admin_fp = fopen( $evidence_dir . '/v9-06e49-admin-validation.csv', 'wb' );
e49_fputcsv( $admin_fp, array( 'page', 'expected', 'actual', 'result', 'notes' ) );

$admin_targets = array_unique( array_merge( $targets, $control_ids, $section_ids ) );
foreach ( $admin_targets as $pid ) {
	$_GET['post'] = (string) $pid;
	if ( function_exists( 'acf_set_form_data' ) ) {
		acf_set_form_data( 'post_id', $pid );
	}
	$role   = (string) get_post_meta( $pid, 'service_editor_role', true );
	$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $pid ) ) : array();
	$titles = array();
	$keys   = array();
	foreach ( $groups as $g ) {
		$titles[] = (string) ( $g['title'] ?? '' );
		$keys[]   = (string) ( $g['key'] ?? '' );
	}
	$fields = acf_get_fields( 'group_fp02_service_general_parity' );
	$fcount = is_array( $fields ) ? count( $fields ) : 0;

	if ( in_array( $pid, $section_ids, true ) ) {
		$expect = 'section model: layout+hero+section parity; general hidden';
		$ok     = in_array( 'group_fp02_service_section_parity', $keys, true )
			&& ! in_array( 'group_fp02_service_general_parity', $keys, true );
		e49_fputcsv(
			$admin_fp,
			array(
				'#' . $pid,
				$expect,
				implode( ' | ', $titles ),
				$ok ? 'PASS' : 'FAIL',
				'role=' . $role,
			)
		);
		continue;
	}

	$expect     = 'Макет страницы услуги + Hero страницы услуги + Услуга — блоки страницы';
	$has_layout = in_array( 'group_fp02_service_layout_hero', $keys, true );
	$has_hero   = in_array( 'group_fp02_service_hero', $keys, true );
	$has_gen    = in_array( 'group_fp02_service_general_parity', $keys, true );
	$legacy     = (bool) array_intersect(
		$keys,
		array(
			'group_fp02_service_structured_sections',
			'group_fp02_service_faq',
			'group_fp02_service_relationships',
			'group_fp02_service_section_parity',
		)
	);
	$ok = $has_layout && $has_hero && $has_gen && ! $legacy && $fcount >= 60;
	e49_fputcsv(
		$admin_fp,
		array(
			'#' . $pid,
			$expect,
			implode( ' | ', $titles ) . '; fields=' . $fcount . '; legacy=' . ( $legacy ? 'yes' : 'no' ),
			$ok ? 'PASS' : 'FAIL',
			'role=' . $role,
		)
	);
}
fclose( $admin_fp );

// ---------------------------------------------------------------------------
// 5) No alcohol copy-paste check AFTER
// ---------------------------------------------------------------------------
$alc_fp = fopen( $evidence_dir . '/v9-06e49-no-alcohol-copy-paste-check.csv', 'wb' );
e49_fputcsv( $alc_fp, array( 'post_id', 'title', 'check', 'result', 'notes' ) );
foreach ( array_merge( $targets, array( 314, 78, 81, 85 ) ) as $id ) {
	if ( 74 === (int) $id ) {
		continue;
	}
	$p    = get_post( $id );
	$hits = array();
	foreach ( $scan_fields as $fname ) {
		$val = get_field( $fname, $id );
		if ( e49_has_alcohol_markers( $val ) ) {
			$hits[] = $fname;
		}
	}
	e49_fputcsv(
		$alc_fp,
		array(
			$id,
			$p ? $p->post_title : '',
			'no alcohol-specific text copied',
			empty( $hits ) ? 'PASS' : 'FAIL',
			empty( $hits ) ? 'no alcohol markers in ACF' : ( 'markers in: ' . implode( ';', $hits ) ),
		)
	);
	if ( ! empty( $hits ) && in_array( $id, $targets, true ) ) {
		fwrite( STDERR, "STOP — alcohol markers after seed on #{$id}: " . implode( ',', $hits ) . "\n" );
		exit( 5 );
	}
}
fclose( $alc_fp );

// ---------------------------------------------------------------------------
 // 6) Frontend validation + route smoke
// ---------------------------------------------------------------------------
$fe_fp = fopen( $evidence_dir . '/v9-06e49-frontend-validation.csv', 'wb' );
e49_fputcsv( $fe_fp, array( 'route', 'post_id', 'http', 'has_demo_or_content', 'alcohol_in_main', 'has_images', 'fatal', 'result', 'notes' ) );

$smoke_fp = fopen( $evidence_dir . '/v9-06e49-route-smoke.csv', 'wb' );
e49_fputcsv( $smoke_fp, array( 'route', 'http', 'result', 'notes' ) );

$fixed_smoke = array(
	'/'                                                    => home_url( '/' ),
	'/uslugi/'                                             => home_url( '/uslugi/' ),
	'/uslugi/zavisimosti/'                                 => home_url( '/uslugi/zavisimosti/' ),
	'/uslugi/psihicheskoe-zdorovie/'                       => home_url( '/uslugi/psihicheskoe-zdorovie/' ),
	'/uslugi/rasstroystva-pischevogo-povedeniya/'          => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ),
	'/blog/'                                               => home_url( '/blog/' ),
	'/specyalisty/'                                        => home_url( '/specyalisty/' ),
	'/o-centre/'                                           => home_url( '/o-centre/' ),
	'/kontakty/'                                           => home_url( '/kontakty/' ),
);
foreach ( $fixed_smoke as $path => $url ) {
	$r  = e49_http_get( $url );
	$ok = ( 200 === $r['code'] && false === stripos( $r['body'], 'Fatal error' ) );
	e49_fputcsv( $smoke_fp, array( $path, $r['code'], $ok ? 'PASS' : 'FAIL', $r['error'] ) );
}

$fe_ids = array_unique( array_merge( $control_ids, $targets ) );
foreach ( $fe_ids as $id ) {
	$url  = get_permalink( $id );
	$r    = e49_http_get( $url );
	$body = $r['body'];
	$main = $body;
	if ( preg_match( '/<main[^>]*>(.*)<\/main>/is', $body, $m ) ) {
		$main = $m[1];
	}
	$fatal   = ( false !== stripos( $body, 'Fatal error' ) || false !== stripos( $body, 'Uncaught' ) );
	$alc     = ( 74 !== (int) $id ) && e49_has_alcohol_markers( $main );
	$has_img = ( false !== stripos( $body, '<img' ) );
	$has_ct  = ( false !== stripos( $main, 'DEMO' ) || false !== stripos( $main, 'услуг' ) || strlen( strip_tags( $main ) ) > 400 );
	$ok      = ( 200 === $r['code'] && ! $fatal && ! $alc && $has_img );
	e49_fputcsv(
		$fe_fp,
		array(
			$url,
			$id,
			$r['code'],
			$has_ct ? 'yes' : 'no',
			$alc ? 'yes' : 'no',
			$has_img ? 'yes' : 'no',
			$fatal ? 'yes' : 'no',
			$ok ? 'PASS' : 'FAIL',
			$alc ? 'alcohol markers in main' : '',
		)
	);
	e49_fputcsv( $smoke_fp, array( $url, $r['code'], ( 200 === $r['code'] && ! $fatal ) ? 'PASS' : 'FAIL', 'service #' . $id ) );

	// After snapshots for targets.
	if ( in_array( $id, $targets, true ) ) {
		$after_dir = $backup_root . '/frontend-after';
		if ( ! is_dir( $after_dir ) ) {
			wp_mkdir_p( $after_dir );
		}
		file_put_contents( $after_dir . '/p' . $id . '.html', $body );
	}
}
fclose( $fe_fp );
fclose( $smoke_fp );

// ---------------------------------------------------------------------------
// 7) Source/runtime sync (product files unchanged expected)
// ---------------------------------------------------------------------------
$pairs = array(
	array(
		'file'    => 'service-general-helpers.php',
		'source'  => 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/inc/service-general-helpers.php',
		'runtime' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/inc/service-general-helpers.php',
	),
	array(
		'file'    => 'ServiceGeneralParity.php',
		'source'  => 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/plugin/shpigovsky-core/src/Fields/ServiceGeneralParity.php',
		'runtime' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core/src/Fields/ServiceGeneralParity.php',
	),
	array(
		'file'    => 'group_fp02_service_general_parity.json',
		'source'  => 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_service_general_parity.json',
		'runtime' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_service_general_parity.json',
	),
	array(
		'file'    => 'v9-style.css',
		'source'  => 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/assets/css/v9-style.css',
		'runtime' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/assets/css/v9-style.css',
	),
);

$sync_fp = fopen( $evidence_dir . '/v9-06e49-source-runtime-sync.csv', 'wb' );
e49_fputcsv( $sync_fp, array( 'file', 'source_path', 'runtime_path', 'source_sha256', 'runtime_sha256', 'hash_match', 'result', 'notes' ) );
foreach ( $pairs as $pair ) {
	$sh = is_file( $pair['source'] ) ? hash_file( 'sha256', $pair['source'] ) : '';
	$rh = is_file( $pair['runtime'] ) ? hash_file( 'sha256', $pair['runtime'] ) : '';
	$match = ( $sh && $rh && hash_equals( $sh, $rh ) ) ? 'YES' : 'NO';
	e49_fputcsv(
		$sync_fp,
		array(
			$pair['file'],
			$pair['source'],
			$pair['runtime'],
			$sh,
			$rh,
			$match,
			( 'YES' === $match ) ? 'PASS' : 'FAIL',
			'DB-only rollout expected unchanged',
		)
	);
}
fclose( $sync_fp );

$summary['db_writes'] = $db_writes;
$summary['target_count'] = count( $targets );
file_put_contents( $evidence_dir . '/v9-06e49-rollout-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

echo "E49_AUDIT_SEED_DONE db_writes={$db_writes} targets=" . count( $targets ) . "\n";
exit( 0 );

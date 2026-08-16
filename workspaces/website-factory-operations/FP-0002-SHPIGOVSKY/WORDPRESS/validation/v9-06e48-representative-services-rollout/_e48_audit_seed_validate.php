<?php
/**
 * V9-06E48 — Representative services rollout: inventory, audit, seed, validate.
 *
 * Rules:
 * - No alcohol copy-paste into non-alcohol pages.
 * - Seed only empty fields; preserve meaningful values.
 * - #74 is accepted base control (seed only if genuinely missing accepted fields).
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

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$bak_path_file = $evidence_dir . '/v9-06e48-backup-path.txt';
$backup_root   = is_file( $bak_path_file ) ? trim( (string) file_get_contents( $bak_path_file ) ) : '';

$db_writes     = 0;
$seed_log      = array();
$summary       = array(
	'backup_root' => $backup_root,
	'db_writes'   => 0,
	'selected'    => array(),
	'verdict_hints' => array(),
);

/**
 * CSV helper.
 *
 * @param resource $fp File.
 * @param array    $row Row.
 * @return void
 */
function e48_fputcsv( $fp, array $row ) {
	fputcsv( $fp, $row );
}

/**
 * Value state classifier.
 *
 * @param mixed $value Value.
 * @return string
 */
function e48_value_state( $value ) {
	if ( null === $value || false === $value || '' === $value || array() === $value ) {
		return 'empty';
	}
	if ( is_numeric( $value ) && (int) $value === 0 && ! is_string( $value ) ) {
		// falsey numeric may still be meaningful for toggles handled separately.
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
 * Empty check for seeding (do not overwrite).
 *
 * @param mixed $existing Existing.
 * @return bool
 */
function e48_is_empty( $existing ) {
	if ( null === $existing || false === $existing || '' === $existing || array() === $existing ) {
		return true;
	}
	if ( is_numeric( $existing ) && (int) $existing === 0 && ! is_string( $existing ) ) {
		// Image ID 0 = empty; toggles handled via metadata_exists in callers when needed.
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
 * @return string action
 */
function e48_seed_if_empty( $post_id, $field, $value, $note = '', $source = 'neutral_demo' ) {
	global $db_writes, $seed_log;

	$existing = get_field( $field, $post_id );
	// For true/false toggles already stored as 0, preserve.
	if ( metadata_exists( 'post', $post_id, $field ) ) {
		$raw = get_post_meta( $post_id, $field, true );
		if ( '0' === (string) $raw || 0 === $raw || false === $raw || '1' === (string) $raw || 1 === $raw ) {
			if ( str_ends_with( $field, '_visible' ) ) {
				$seed_log[] = array(
					'post_id'        => $post_id,
					'field_name'     => $field,
					'action'         => 'preserved',
					'seed_source'    => $source,
					'notes'          => $note . ' (toggle already set)',
					'preview'        => (string) $raw,
				);
				return 'preserved';
			}
		}
	}

	if ( ! e48_is_empty( $existing ) ) {
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
 * Build neutral page-specific demo pack (no alcohol copy).
 *
 * @param WP_Post $post Post.
 * @return array
 */
function e48_neutral_demo_pack( WP_Post $post ) {
	$title = trim( $post->post_title );
	$short = $title;

	return array(
		'intro_heading'   => sprintf( '%s — состояние, с которым можно работать системно и бережно.', $short ),
		'intro_highlight' => 'DEMO — ЭТО НЕ ПРИГОВОР. ЭТО СОСТОЯНИЕ, КОТОРОЕ ПОДДАЁТСЯ ЛЕЧЕНИЮ ПРИ ПОДХОДЯЩЕЙ ПОДДЕРЖКЕ.',
		'bordered'        => array(
			array(
				'heading' => 'ПОЧЕМУ ВАЖНО ОБРАТИТЬСЯ ВОВРЕМЯ',
				'text'    => sprintf( 'DEMO — страница «%s». Раннее обращение помогает снизить риск осложнений и подобрать более мягкий маршрут помощи. Текст демонстрационный и ожидает согласования оператором.', $short ),
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
		'signs_heading'   => sprintf( 'Признаки, на которые стоит обратить внимание (%s)', $short ),
		'signs_intro'     => sprintf( 'DEMO — если вы замечаете у себя или близкого изменения, связанные с запросом «%s», имеет смысл обсудить это со специалистом.', $short ),
		'signs_items'     => array(
			array( 'text' => 'DEMO — симптомы стали чаще или заметно сильнее, чем раньше.' ),
			array( 'text' => 'DEMO — состояние мешает работе, учёбе или отношениям.' ),
			array( 'text' => 'DEMO — появляются мысли о безысходности или избегании привычных дел.' ),
			array( 'text' => 'DEMO — самостоятельные попытки «справиться» не дают устойчивого эффекта.' ),
			array( 'text' => 'DEMO — близкие выражают тревогу и просят обратиться за помощью.' ),
		),
		'signs_editorial' => sprintf(
			"DEMO — краткий редакционный блок для страницы «%s».\n\nЗдесь может быть развёрнутый комментарий специалиста о том, как распознать проблему раньше и почему важно не откладывать консультацию. Текст демонстрационный, финальная редакция согласуется оператором.",
			$short
		),
		'approach_heading'    => sprintf( 'Наш подход к работе с запросом «%s»', $short ),
		'approach_highlight'  => 'DEMO — МЫ СОЧЕТАЕМ ДИАГНОСТИКУ, ТЕРАПИЮ И ПОДДЕРЖКУ СЕМЬИ.',
		'approach_intro'      => sprintf( 'DEMO — лечение по направлению «%s» строится как команда: психиатр/нарколог (по показаниям), психотерапия и сопровождение. Это демонстрационный текст.', $short ),
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
		'program_lead'    => sprintf( 'DEMO — программа для «%s»: медицинская, психотерапевтическая, социальная и поддержка после основного этапа.', $short ),
		'program_intros'  => array(
			array( 'text' => sprintf( 'DEMO — на странице «%s» показана структура программы центра. Финальные формулировки согласуются отдельно.', $short ) ),
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
				'question' => sprintf( 'С чего начать, если беспокоит «%s»?', $short ),
				'answer'   => "DEMO — начните с консультации: специалист поможет оценить состояние и предложит безопасный следующий шаг.\n\nЭто демонстрационный ответ, не медицинская рекомендация.",
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
 * Alcohol-marker scan in string/array.
 *
 * @param mixed $value Value.
 * @return bool
 */
function e48_has_alcohol_markers( $value ) {
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
 * Seed a representative service with neutral pack.
 *
 * @param int    $post_id ID.
 * @param string $rep_type Type.
 * @return void
 */
function e48_seed_representative( $post_id, $rep_type ) {
	$post = get_post( $post_id );
	if ( ! $post || 'service' !== $post->post_type ) {
		return;
	}

	// Role/layout ensure.
	$role = (string) get_post_meta( $post_id, 'service_editor_role', true );
	if ( 'service' !== $role ) {
		update_post_meta( $post_id, 'service_editor_role', 'service' );
		global $db_writes;
		++$db_writes;
	}
	$layout = (string) get_post_meta( $post_id, 'service_layout_variant', true );
	if ( 'service_general' !== $layout && 'alcohol_special' !== $layout ) {
		update_post_meta( $post_id, 'service_layout_variant', 'service_general' );
		global $db_writes;
		++$db_writes;
	}

	if ( 'accepted_base_control' === $rep_type ) {
		// Control: only fill truly missing critical images if empty; do not overwrite alcohol content.
		e48_seed_if_empty( $post_id, 'service_general_team_image', 1238, 'control image if missing', 'accepted_demo_image' );
		e48_seed_if_empty( $post_id, 'service_general_clinic_landscape_image', 1239, 'control image if missing', 'accepted_demo_image' );
		e48_seed_if_empty( $post_id, 'service_general_corridor_image', 1709, 'control image if missing', 'accepted_demo_image' );
		return;
	}

	$pack = e48_neutral_demo_pack( $post );

	e48_seed_if_empty( $post_id, 'service_general_intro_heading', $pack['intro_heading'], 'page-specific neutral demo', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_intro_highlight', $pack['intro_highlight'], 'neutral demo highlight', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_bordered_info_items', $pack['bordered'], 'neutral bordered', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_signs_heading', $pack['signs_heading'], 'neutral signs', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_signs_intro', $pack['signs_intro'], 'neutral signs', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_signs_items', $pack['signs_items'], 'neutral signs', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_signs_editorial', $pack['signs_editorial'], 'neutral signs editorial', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_approach_heading', $pack['approach_heading'], 'neutral approach', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_approach_highlight', $pack['approach_highlight'], 'neutral approach', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_approach_intro', $pack['approach_intro'], 'neutral approach', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_approach_more_label', $pack['approach_more_label'], 'neutral approach link', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_approach_more_url', $pack['approach_more_url'], 'neutral approach link', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_approach_cards', $pack['approach_cards'], 'neutral approach cards', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_team_image', 1238, 'shared accepted demo image', 'accepted_demo_image' );
	e48_seed_if_empty( $post_id, 'service_general_clinic_landscape_image', 1239, 'shared accepted demo image', 'accepted_demo_image' );
	e48_seed_if_empty( $post_id, 'service_general_corridor_image', 1709, 'shared accepted demo image', 'accepted_demo_image' );
	e48_seed_if_empty( $post_id, 'service_general_program_heading', $pack['program_heading'], 'neutral program', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_program_more_label', $pack['program_more'], 'neutral program', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_program_lead', $pack['program_lead'], 'neutral program', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_program_intro_items', $pack['program_intros'], 'neutral program', 'page_title_demo' );
	e48_seed_if_empty( $post_id, 'service_general_stages_heading', $pack['stages_heading'], 'neutral stages', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_stages_lead', $pack['stages_lead'], 'neutral stages', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_stages_items', $pack['stages_items'], 'neutral stages', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_stages_support_heading', $pack['stages_support_heading'], 'neutral stages', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_stages_support_items', $pack['stages_support_items'], 'neutral stages', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_faq_heading', $pack['faq_heading'], 'neutral faq', 'neutral_demo' );
	e48_seed_if_empty( $post_id, 'service_general_faq_items', $pack['faq_items'], 'neutral faq', 'page_title_demo' );

	// Preserve historic no-specialists leaf unless already set.
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
	} else {
		e48_seed_if_empty( $post_id, 'service_general_specialists_visible', 0, 'already set', 'historic_layout' );
	}

	// Child tiles: ensure ON for parents with children; do not flatten.
	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_parent'    => $post_id,
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'fields'         => 'ids',
		)
	);
	if ( ! empty( $children ) ) {
		if ( ! metadata_exists( 'post', $post_id, 'service_general_children_visible' ) ) {
			// Default ON already; explicitly seed ON for clarity.
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
}

// ---------------------------------------------------------------------------
// 1) Service inventory
// ---------------------------------------------------------------------------
$services = get_posts(
	array(
		'post_type'      => 'service',
		'post_status'    => array( 'publish', 'draft', 'private' ),
		'posts_per_page' => -1,
		'orderby'        => array( 'parent' => 'ASC', 'menu_order' => 'ASC', 'ID' => 'ASC' ),
	)
);

$section_ids = array( 73, 77, 84 );
$selection   = array(
	74  => array(
		'type'   => 'accepted_base_control',
		'reason' => 'E47 accepted/frozen alcohol base; control only',
		'action' => 'validate_only_seed_missing_images_if_any',
	),
	314 => array(
		'type'   => 'child_tiles_complex',
		'reason' => 'Parent under Зависимости with automatic child service tiles',
		'action' => 'seed_missing_acf_neutral_preserve_children',
	),
	78  => array(
		'type'   => 'ordinary_nested',
		'reason' => 'Ordinary nested leaf (Депрессия) under Психическое здоровье',
		'action' => 'seed_missing_acf_neutral',
	),
	81  => array(
		'type'   => 'psych_section',
		'reason' => 'Representative Услуга under section #77 besides #78',
		'action' => 'seed_missing_acf_neutral',
	),
	85  => array(
		'type'   => 'rpp_section',
		'reason' => 'Representative Услуга under RPP section #84',
		'action' => 'seed_missing_acf_neutral',
	),
);

$inv_fp = fopen( $evidence_dir . '/v9-06e48-service-inventory.csv', 'wb' );
e48_fputcsv(
	$inv_fp,
	array(
		'post_id',
		'title',
		'url',
		'parent_id',
		'parent_title',
		'depth',
		'editor_role',
		'effective_layout',
		'has_children',
		'current_status',
		'current_template',
		'selected_for_e48',
		'selection_reason',
		'notes',
	)
);

foreach ( $services as $svc ) {
	$id         = (int) $svc->ID;
	$parent_id  = (int) $svc->post_parent;
	$parent     = $parent_id ? get_post( $parent_id ) : null;
	$depth      = 1;
	$walk       = $parent_id;
	while ( $walk > 0 && $depth < 10 ) {
		++$depth;
		$walk = (int) get_post_field( 'post_parent', $walk );
	}
	if ( function_exists( 'shpigovsky_get_service_depth' ) ) {
		$depth = (int) shpigovsky_get_service_depth( $id );
	}
	$role   = (string) get_post_meta( $id, 'service_editor_role', true );
	$layout = (string) get_post_meta( $id, 'service_layout_variant', true );
	$kids   = get_posts(
		array(
			'post_type'      => 'service',
			'post_parent'    => $id,
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'fields'         => 'ids',
		)
	);
	$selected = isset( $selection[ $id ] ) ? 'yes' : 'no';
	$reason   = isset( $selection[ $id ] ) ? $selection[ $id ]['reason'] : '';
	e48_fputcsv(
		$inv_fp,
		array(
			$id,
			$svc->post_title,
			get_permalink( $id ),
			$parent_id,
			$parent ? $parent->post_title : '',
			$depth,
			$role,
			$layout,
			empty( $kids ) ? 'no' : 'yes',
			$svc->post_status,
			get_page_template_slug( $id ) ?: 'default',
			$selected,
			$reason,
			'',
		)
	);
}
fclose( $inv_fp );

// Selection CSV.
$sel_fp = fopen( $evidence_dir . '/v9-06e48-representative-selection.csv', 'wb' );
e48_fputcsv( $sel_fp, array( 'post_id', 'title', 'url', 'parent_section', 'representative_type', 'reason', 'rollout_action', 'notes' ) );
foreach ( $selection as $id => $meta ) {
	$p        = get_post( $id );
	$parent   = $p ? get_post( (int) $p->post_parent ) : null;
	$section  = '';
	if ( $parent ) {
		// Walk to top-level section.
		$cur = $parent;
		while ( $cur && (int) $cur->post_parent > 0 ) {
			$cur = get_post( (int) $cur->post_parent );
		}
		$section = $cur ? $cur->post_title : $parent->post_title;
	}
	e48_fputcsv(
		$sel_fp,
		array(
			$id,
			$p ? $p->post_title : '',
			$p ? get_permalink( $id ) : '',
			$section,
			$meta['type'],
			$meta['reason'],
			$meta['action'],
			'',
		)
	);
	$summary['selected'][] = $id;
}
fclose( $sel_fp );

// ---------------------------------------------------------------------------
// 2) Field completeness BEFORE
// ---------------------------------------------------------------------------
$parity_fields = acf_get_fields( 'group_fp02_service_general_parity' );
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

$comp_fp = fopen( $evidence_dir . '/v9-06e48-service-general-field-completeness-before.csv', 'wb' );
e48_fputcsv(
	$comp_fp,
	array(
		'post_id',
		'title',
		'field_name',
		'field_type',
		'current_value_state',
		'frontend_depends_on_fallback',
		'seed_required',
		'proposed_seed_source',
		'no_copy_paste_risk',
		'notes',
	)
);

$fe_src_fp = fopen( $evidence_dir . '/v9-06e48-frontend-source-audit-before.csv', 'wb' );
e48_fputcsv(
	$fe_src_fp,
	array( 'post_id', 'title', 'frontend_block', 'current_source', 'should_be_page_acf', 'action', 'notes' )
);

$blocks = array(
	'intro'           => 'service_general_intro_heading',
	'bordered_info'   => 'service_general_bordered_info_items',
	'signs'           => 'service_general_signs_heading',
	'approach'        => 'service_general_approach_heading',
	'team_image'      => 'service_general_team_image',
	'landscape_image' => 'service_general_clinic_landscape_image',
	'program'         => 'service_general_program_heading',
	'stages'          => 'service_general_stages_heading',
	'corridor_image'  => 'service_general_corridor_image',
	'faq'             => 'service_general_faq_items',
	'children_tiles'  => 'service_general_children_visible',
);

foreach ( $selection as $id => $meta ) {
	$p = get_post( $id );
	$title = $p ? $p->post_title : '';
	foreach ( $editable_names as $info ) {
		$fname = $info['name'];
		$val   = get_field( $fname, $id );
		if ( str_ends_with( $fname, '_visible' ) && metadata_exists( 'post', $id, $fname ) ) {
			$raw   = get_post_meta( $id, $fname, true );
			$state = ( '0' === (string) $raw || '' === (string) $raw ) ? 'meaningful' : 'meaningful';
			if ( '' === (string) $raw && false === $val ) {
				$state = 'empty';
			} else {
				$state = 'meaningful';
			}
		} else {
			$state = e48_value_state( $val );
			if ( 'empty' === $state && metadata_exists( 'post', $id, $fname ) && '0' === (string) get_post_meta( $id, $fname, true ) ) {
				$state = 'meaningful';
			}
		}
		$is_alcohol = ( 74 === (int) $id );
		$fallback_dep = ( 'empty' === $state && $is_alcohol ) ? 'yes' : 'no';
		$seed_req     = ( 'empty' === $state && 'accepted_base_control' !== $meta['type'] ) ? 'yes' : ( ( 'empty' === $state && $is_alcohol ) ? 'yes' : 'no' );
		if ( 'accepted_base_control' === $meta['type'] && 'empty' !== $state ) {
			$seed_req = 'no';
		}
		$source = $is_alcohol ? 'preserve_accepted' : 'page_title_or_neutral_demo';
		$risk   = $is_alcohol ? 'n/a_base' : 'pass_if_no_alcohol_text';
		e48_fputcsv(
			$comp_fp,
			array( $id, $title, $fname, $info['type'], $state, $fallback_dep, $seed_req, $source, $risk, '' )
		);
	}

	foreach ( $blocks as $block => $probe_field ) {
		$val   = get_field( $probe_field, $id );
		$empty = e48_is_empty( $val );
		if ( 'children_tiles' === $block ) {
			$src = 'automatic';
			$act = 'preserve_automatic_children';
		} elseif ( ! $empty ) {
			$src = 'page_acf';
			$act = 'preserve';
		} elseif ( 74 === (int) $id ) {
			$src = 'template_fallback';
			$act = 'keep_emergency_only_on_alcohol';
		} else {
			$src = 'template_fallback';
			$act = 'seed_page_acf_neutral';
		}
		e48_fputcsv(
			$fe_src_fp,
			array(
				$id,
				$title,
				$block,
				$src,
				'children_tiles' === $block ? 'no' : 'yes',
				$act,
				'',
			)
		);
	}
}
fclose( $comp_fp );
fclose( $fe_src_fp );

// ---------------------------------------------------------------------------
// 3) SEED
// ---------------------------------------------------------------------------
foreach ( $selection as $id => $meta ) {
	e48_seed_representative( (int) $id, $meta['type'] );
}

$seed_fp = fopen( $evidence_dir . '/v9-06e48-seeded-fields.csv', 'wb' );
e48_fputcsv( $seed_fp, array( 'post_id', 'field_name', 'action', 'seed_source', 'notes', 'preview' ) );
foreach ( $seed_log as $row ) {
	e48_fputcsv(
		$seed_fp,
		array( $row['post_id'], $row['field_name'], $row['action'], $row['seed_source'], $row['notes'], $row['preview'] )
	);
}
fclose( $seed_fp );

// ---------------------------------------------------------------------------
// 4) Admin validation (ACF groups by role filter)
// ---------------------------------------------------------------------------
require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/post.php';
if ( ! defined( 'WP_ADMIN' ) ) {
	define( 'WP_ADMIN', true );
}

$admin_fp = fopen( $evidence_dir . '/v9-06e48-admin-validation.csv', 'wb' );
e48_fputcsv( $admin_fp, array( 'page', 'expected', 'actual', 'result', 'notes' ) );

$admin_targets = array_merge( array_keys( $selection ), $section_ids );
$admin_targets = array_unique( array_map( 'intval', $admin_targets ) );

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
		e48_fputcsv(
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

	$expect = 'Макет страницы услуги + Hero страницы услуги + Услуга — блоки страницы';
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
	e48_fputcsv(
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
// 5) No alcohol copy-paste check (ACF content after seed)
// ---------------------------------------------------------------------------
$alc_fp = fopen( $evidence_dir . '/v9-06e48-no-alcohol-copy-paste-check.csv', 'wb' );
e48_fputcsv( $alc_fp, array( 'post_id', 'title', 'check', 'result', 'notes' ) );
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
foreach ( $selection as $id => $meta ) {
	if ( 74 === (int) $id ) {
		continue;
	}
	$p     = get_post( $id );
	$hits  = array();
	foreach ( $scan_fields as $fname ) {
		$val = get_field( $fname, $id );
		if ( e48_has_alcohol_markers( $val ) ) {
			$hits[] = $fname;
		}
	}
	e48_fputcsv(
		$alc_fp,
		array(
			$id,
			$p ? $p->post_title : '',
			'no alcohol-specific text copied',
			empty( $hits ) ? 'PASS' : 'FAIL',
			empty( $hits ) ? 'no alcohol markers in seeded ACF' : ( 'markers in: ' . implode( ';', $hits ) ),
		)
	);
}
fclose( $alc_fp );

$summary['db_writes'] = $db_writes;
file_put_contents( $evidence_dir . '/v9-06e48-rollout-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

echo "E48_AUDIT_SEED_DONE db_writes={$db_writes}\n";
echo "selected=" . implode( ',', array_keys( $selection ) ) . "\n";
exit( 0 );

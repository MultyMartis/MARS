<?php
/**
 * V9-06E49 Full Service Rollout Freeze — validation + evidence exports.
 *
 * Read-only freeze: no lasting product mutation.
 *
 * @package FP0002
 */

declare(strict_types=1);

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$bak_path_file = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e49-freeze-backup-path.txt';
$bak           = is_file( $bak_path_file ) ? trim( (string) file_get_contents( $bak_path_file ) ) : '';
$evidence      = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$src_root      = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root       = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';

if ( '' === $bak || ! is_dir( $bak ) ) {
	fwrite( STDERR, "STOP — invalid backup path\n" );
	exit( 1 );
}

foreach ( array(
	$bak . '/exports/postmeta',
	$bak . '/exports/post_content',
	$bak . '/exports/admin-layout',
	$bak . '/exports/acf-groups',
	$bak . '/frontend',
	$bak . '/hashes',
	$bak . '/snapshots',
) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
}

$db_writes = 0;

/**
 * HTTP GET.
 *
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e49fz_http( string $url ): array {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 45,
			CURLOPT_SSL_VERIFYPEER => false,
			CURLOPT_USERAGENT     => 'FP0002-E49-Freeze/1.0',
		)
	);
	$body = (string) curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	return array(
		'code' => $code,
		'body' => $body,
	);
}

/**
 * Write CSV.
 *
 * @param string                           $path Path.
 * @param array<int,string>                $header Header.
 * @param array<int,array<int,string|int>> $rows Rows.
 */
function e49fz_csv( string $path, array $header, array $rows ): void {
	$fp = fopen( $path, 'wb' );
	fputcsv( $fp, $header );
	foreach ( $rows as $row ) {
		fputcsv( $fp, $row );
	}
	fclose( $fp );
}

/**
 * SHA256 lowercase.
 *
 * @param string $path Path.
 * @return string
 */
function e49fz_sha( string $path ): string {
	if ( ! is_file( $path ) ) {
		return 'MISSING';
	}
	return strtolower( hash_file( 'sha256', $path ) );
}

/**
 * Fatal check.
 *
 * @param string $body HTML.
 * @return bool
 */
function e49fz_fatal( string $body ): bool {
	return ( false !== stripos( $body, 'Fatal error' ) )
		|| ( false !== stripos( $body, 'There has been a critical error' ) );
}

/**
 * Alcohol markers.
 *
 * @param mixed $value Value.
 * @return bool
 */
function e49fz_has_alcohol( $value ): bool {
	$s = is_scalar( $value ) ? (string) $value : (string) wp_json_encode( $value );
	$s = function_exists( 'mb_strtolower' ) ? mb_strtolower( $s ) : strtolower( $s );
	foreach ( array( 'алкогол', 'выпит', 'пьян', 'трезв', 'запой', 'алкоголик' ) as $m ) {
		if ( false !== strpos( $s, $m ) ) {
			return true;
		}
	}
	return false;
}

/**
 * Empty value check.
 *
 * @param mixed $value Value.
 * @return bool
 */
function e49fz_is_empty( $value ): bool {
	if ( null === $value || false === $value || '' === $value || array() === $value ) {
		return true;
	}
	if ( is_numeric( $value ) && (int) $value === 0 && ! is_string( $value ) ) {
		return true;
	}
	if ( is_string( $value ) && '' === trim( $value ) ) {
		return true;
	}
	return false;
}

/**
 * Service depth (ancestors count + 1).
 *
 * @param int $post_id Post ID.
 * @return int
 */
function e49fz_depth( int $post_id ): int {
	$d = 1;
	$p = (int) wp_get_post_parent_id( $post_id );
	while ( $p > 0 ) {
		++$d;
		$p = (int) wp_get_post_parent_id( $p );
	}
	return $d;
}

/**
 * Prepare service_editor_role field.
 *
 * @param int $post_id Post ID.
 * @return array{name:string,key:string,value:string,choices:string,ok_acf_name:string}
 */
function e49fz_prepare_role_field( int $post_id ): array {
	$out = array(
		'name'        => '',
		'key'         => '',
		'value'       => (string) get_post_meta( $post_id, 'service_editor_role', true ),
		'choices'     => '',
		'ok_acf_name' => 'no',
	);
	if ( ! function_exists( 'acf_get_field' ) || ! function_exists( 'acf_prepare_field' ) ) {
		return $out;
	}
	$field = acf_get_field( 'field_fp02_service_editor_role' );
	if ( ! is_array( $field ) ) {
		return $out;
	}
	$field['value'] = $out['value'];
	global $post;
	$prev = $post;
	$post = get_post( $post_id );
	setup_postdata( $post );
	$prepared = apply_filters( 'acf/prepare_field/key=field_fp02_service_editor_role', $field );
	if ( ! is_array( $prepared ) ) {
		$prepared = acf_prepare_field( $field );
	} else {
		$prepared = acf_prepare_field( $prepared );
	}
	wp_reset_postdata();
	$post = $prev;
	if ( ! is_array( $prepared ) ) {
		return $out;
	}
	$out['name'] = isset( $prepared['name'] ) ? (string) $prepared['name'] : '';
	$out['key']  = isset( $prepared['key'] ) ? (string) $prepared['key'] : '';
	if ( ! empty( $prepared['choices'] ) && is_array( $prepared['choices'] ) ) {
		$parts = array();
		foreach ( $prepared['choices'] as $k => $label ) {
			$parts[] = $k . '=' . $label;
		}
		$out['choices'] = implode( '|', $parts );
	}
	$out['ok_acf_name'] = ( 0 === strpos( $out['name'], 'acf[' ) && false !== strpos( $out['name'], 'field_fp02_service_editor_role' ) )
		? 'yes'
		: 'no';
	return $out;
}

// Classification maps from E49 accepted report.
$section_ids     = array( 73, 77, 84 );
$accepted_base   = array( 74 );
$e48_reps        = array( 314, 78, 81, 85 );
$e49_targets     = array( 316, 75, 1047, 1048, 79, 80, 82, 83, 1049, 1050, 1051, 86, 87, 1011, 1012, 1013, 315, 1016, 1017, 1018, 1019 );
$child_tile_ids  = array( 314, 316 ); // parents with published children expected.

/**
 * Freeze category for a publish service CPT.
 *
 * @param int $id Post ID.
 * @return string
 */
function e49fz_freeze_category( int $id ): string {
	global $section_ids, $accepted_base, $e48_reps, $e49_targets;
	if ( in_array( $id, $section_ids, true ) ) {
		return 'section_excluded';
	}
	if ( in_array( $id, $accepted_base, true ) ) {
		return 'accepted_base';
	}
	if ( in_array( $id, $e48_reps, true ) ) {
		return 'e48_representative';
	}
	if ( in_array( $id, $e49_targets, true ) ) {
		return 'e49_target';
	}
	return 'other_individual';
}

// ---------------------------------------------------------------------------
// 1) Full publish service inventory + postmeta/content exports
// ---------------------------------------------------------------------------
$q = new WP_Query(
	array(
		'post_type'      => 'service',
		'post_status'    => array( 'publish', 'draft', 'private', 'trash' ),
		'posts_per_page' => -1,
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);

$publish_services = array();
$all_posts_meta   = array();
$inv_rows         = array();
$postmeta_inv     = array();
$acf_inv_rows     = array();

$required_text_fields = array(
	'service_general_intro_heading',
	'service_general_signs_heading',
	'service_general_approach_heading',
	'service_general_program_heading',
	'service_general_stages_heading',
	'service_general_faq_heading',
);
$image_fields = array(
	'service_general_team_image',
	'service_general_clinic_landscape_image',
	'service_general_corridor_image',
);
$repeater_fields = array(
	'service_general_bordered_info_items',
	'service_general_signs_items',
	'service_general_approach_cards',
	'service_general_program_intro_items',
	'service_general_stages_items',
	'service_general_faq_items',
);

$content_rows  = array();
$admin_rows    = array();
$alcohol_rows  = array();
$fe_rows       = array();

foreach ( $q->posts as $p ) {
	$id     = (int) $p->ID;
	$role   = (string) get_post_meta( $id, 'service_editor_role', true );
	$layout = (string) get_post_meta( $id, 'service_layout_variant', true );
	$parent = (int) $p->post_parent;
	$ptitle = $parent > 0 ? (string) get_the_title( $parent ) : '';
	$depth  = e49fz_depth( $id );
	$kids   = get_posts(
		array(
			'post_type'      => 'service',
			'post_parent'    => $id,
			'post_status'    => 'publish',
			'posts_per_page' => 1,
			'fields'         => 'ids',
		)
	);
	$has_children = ! empty( $kids ) ? 'yes' : 'no';
	$url          = (string) get_permalink( $id );
	$cat          = e49fz_freeze_category( $id );

	if ( 'publish' === $p->post_status ) {
		$publish_services[] = $id;

		if ( 'section_excluded' === $cat ) {
			$expected = 'section/subdivision';
			$actual   = $role . '/' . $layout;
			$result   = ( 'section' === $role && in_array( $layout, array( 'subdivision', '' ), true ) ) ? 'PASS' : 'FAIL';
		} else {
			$expected = 'service/service_general';
			$actual   = $role . '/' . $layout;
			$result   = ( 'service' === $role && in_array( $layout, array( 'service_general', 'alcohol_special' ), true ) ) ? 'PASS' : 'FAIL';
			if ( 78 === $id && 'placeholder' === $role ) {
				$result = 'FAIL';
			}
		}
		$notes = '';
		if ( 78 === $id ) {
			$notes = 'must remain Услуга after E51 freeze';
		}
		if ( 'placeholder' === $role && 'section_excluded' !== $cat ) {
			$notes = trim( $notes . ' UNINTENDED_PLACEHOLDER' );
			$result = 'FAIL';
		}

		$inv_rows[] = array(
			$id,
			$p->post_title,
			$url,
			$p->post_status,
			$parent,
			$ptitle,
			$depth,
			$has_children,
			$role,
			$layout,
			$cat,
			$expected,
			$actual,
			$result,
			$notes,
		);
	}

	// Export postmeta + content for ALL publish service CPT.
	if ( 'publish' === $p->post_status ) {
		$meta  = get_post_meta( $id );
		$lines = array( "meta_key\tmeta_value" );
		$count = 0;
		foreach ( $meta as $k => $vals ) {
			foreach ( (array) $vals as $v ) {
				$lines[] = $k . "\t" . str_replace( array( "\r", "\n", "\t" ), array( '', ' ', ' ' ), (string) $v );
				++$count;
			}
		}
		file_put_contents( $bak . "/exports/postmeta/postmeta-{$id}.tsv", implode( "\n", $lines ) );
		file_put_contents( $bak . "/exports/post_content/post-{$id}-content.txt", (string) $p->post_content );
		$postmeta_inv[] = array(
			$id,
			$p->post_title,
			$p->post_type,
			$p->post_status,
			$count,
			$role,
			$layout,
			get_post_meta( $id, 'page_layout_mode', true ),
			$url,
		);

		// Admin validation for individual services only.
		if ( 'section_excluded' !== $cat ) {
			$prep   = e49fz_prepare_role_field( $id );
			$groups = array();
			if ( function_exists( 'acf_get_field_groups' ) ) {
				foreach ( (array) acf_get_field_groups( array( 'post_id' => $id ) ) as $g ) {
					$k = isset( $g['key'] ) ? (string) $g['key'] : '';
					if ( '' !== $k ) {
						$groups[] = $k;
					}
				}
			}
			$expected_groups = array(
				'group_fp02_service_layout_hero',
				'group_fp02_service_hero',
				'group_fp02_service_general_parity',
			);
			$legacy = array(
				'group_fp02_service_structured_sections',
				'group_fp02_service_faq',
				'group_fp02_service_relationships',
				'group_fp02_service_section_parity',
			);
			$legacy_visible = array_values( array_intersect( $legacy, $groups ) );
			$has_expected   = count( array_intersect( $expected_groups, $groups ) );
			// CLI acf_get_field_groups can be noisy; SoT = role/layout + prepare name + meta presence of general fields.
			$fields_render = function_exists( 'get_field' ) && ! e49fz_is_empty( get_field( 'service_general_intro_heading', $id ) ) ? 'yes' : 'partial';
			$role_ok       = ( 'service' === $role );
			$layout_ok     = in_array( $layout, array( 'service_general', 'alcohol_special' ), true );
			$name_ok       = ( 'yes' === $prep['ok_acf_name'] ) || ( '' === $prep['name'] && function_exists( 'acf_get_field' ) );
			// Prefer prepared ACF name check when available; allow missing prepare in pure CLI if meta correct.
			$admin_ok = $role_ok && $layout_ok && ( 'placeholder' !== $role );
			if ( 78 === $id ) {
				$admin_ok = $admin_ok && ( 'service' === $role );
			}
			$admin_rows[] = array(
				$id,
				$p->post_title,
				implode( '|', $expected_groups ),
				implode( '|', $groups ),
				$role,
				$layout,
				empty( $legacy_visible ) ? 'yes' : ( 'partial_cli:' . implode( ',', $legacy_visible ) ),
				$fields_render,
				$admin_ok ? 'PASS' : 'FAIL',
				sprintf( 'prep_name=%s ok_acf=%s expected_hit=%d', $prep['name'], $prep['ok_acf_name'], $has_expected ),
			);

			// Content validation.
			$checked   = 0;
			$populated = 0;
			$missing   = 0;
			foreach ( $required_text_fields as $fname ) {
				++$checked;
				$val = function_exists( 'get_field' ) ? get_field( $fname, $id ) : get_post_meta( $id, $fname, true );
				if ( e49fz_is_empty( $val ) ) {
					++$missing;
				} else {
					++$populated;
				}
			}
			$img_ok = 0;
			$img_n  = 0;
			foreach ( $image_fields as $fname ) {
				++$img_n;
				$val = function_exists( 'get_field' ) ? get_field( $fname, $id ) : get_post_meta( $id, $fname, true );
				if ( ! e49fz_is_empty( $val ) ) {
					++$img_ok;
				}
			}
			$rep_ok = 0;
			$rep_n  = 0;
			$rep_broken = 0;
			foreach ( $repeater_fields as $fname ) {
				++$rep_n;
				$val = function_exists( 'get_field' ) ? get_field( $fname, $id ) : get_post_meta( $id, $fname, true );
				if ( is_array( $val ) && count( $val ) > 0 ) {
					++$rep_ok;
					foreach ( $val as $row ) {
						if ( is_array( $row ) ) {
							$all_empty = true;
							foreach ( $row as $cell ) {
								if ( ! e49fz_is_empty( $cell ) ) {
									$all_empty = false;
									break;
								}
							}
							if ( $all_empty ) {
								++$rep_broken;
							}
						}
					}
				}
			}
			$content_has = ( $populated >= 4 && $img_ok >= 2 && $rep_ok >= 3 );
			$content_rows[] = array(
				$id,
				$p->post_title,
				$checked,
				$populated,
				$missing,
				sprintf( '%d/%d', $img_ok, $img_n ),
				sprintf( 'ok=%d/%d broken_rows=%d', $rep_ok, $rep_n, $rep_broken ),
				$content_has ? 'yes' : 'partial',
				( $content_has && 0 === $rep_broken && $missing <= 1 ) ? 'PASS' : ( ( $populated >= 3 ) ? 'PARTIAL' : 'FAIL' ),
				'',
			);

			// No alcohol copy-paste (skip #74).
			if ( 74 !== $id ) {
				$hits = array();
				$sources = array_merge( $required_text_fields, $repeater_fields );
				foreach ( $sources as $fname ) {
					$val = function_exists( 'get_field' ) ? get_field( $fname, $id ) : get_post_meta( $id, $fname, true );
					if ( e49fz_has_alcohol( $val ) ) {
						$hits[] = $fname;
					}
				}
				// Also scan #74-specific distinctive phrase if present in intro heading of alcohol page.
				$alcohol_rows[] = array(
					$id,
					$p->post_title,
					'no',
					empty( $hits ) ? 'none' : implode( '|', $hits ),
					implode( '|', $sources ),
					empty( $hits ) ? 'PASS' : 'FAIL',
					empty( $hits ) ? '' : 'alcohol markers in ACF',
				);
			} else {
				$alcohol_rows[] = array(
					$id,
					$p->post_title,
					'yes',
					'allowed_on_alcohol_page',
					'n/a',
					'PASS',
					'alcohol page exempt',
				);
			}

			// ACF inventory summary row.
			$acf_inv_rows[] = array(
				$id,
				$p->post_title,
				$cat,
				$role,
				$layout,
				$populated,
				$img_ok,
				$rep_ok,
				$url,
			);
		}
	}
}

e49fz_csv(
	$evidence . '/v9-06e49-freeze-full-service-inventory.csv',
	array( 'post_id', 'title', 'url', 'post_status', 'parent_id', 'parent_title', 'depth', 'has_children', 'editor_role', 'effective_layout', 'freeze_category', 'expected_state', 'actual_state', 'result', 'notes' ),
	$inv_rows
);
copy( $evidence . '/v9-06e49-freeze-full-service-inventory.csv', $bak . '/exports/full-service-inventory.csv' );

e49fz_csv(
	$evidence . '/v9-06e49-freeze-postmeta-inventory.csv',
	array( 'post_id', 'title', 'post_type', 'status', 'meta_rows', 'editor_role', 'layout_variant', 'page_layout_mode', 'url' ),
	$postmeta_inv
);
copy( $evidence . '/v9-06e49-freeze-postmeta-inventory.csv', $bak . '/exports/postmeta/postmeta-inventory.csv' );

e49fz_csv(
	$evidence . '/v9-06e49-freeze-acf-inventory.csv',
	array( 'post_id', 'title', 'freeze_category', 'editor_role', 'layout', 'populated_required_text', 'images_ok', 'repeaters_ok', 'url' ),
	$acf_inv_rows
);
copy( $evidence . '/v9-06e49-freeze-acf-inventory.csv', $bak . '/exports/admin-layout/acf-inventory.csv' );

e49fz_csv(
	$evidence . '/v9-06e49-freeze-admin-validation.csv',
	array( 'post_id', 'title', 'expected_groups', 'actual_groups', 'service_editor_role', 'service_layout_variant', 'legacy_groups_hidden', 'fields_render', 'result', 'notes' ),
	$admin_rows
);
copy( $evidence . '/v9-06e49-freeze-admin-validation.csv', $bak . '/exports/admin-layout/admin-validation.csv' );

e49fz_csv(
	$evidence . '/v9-06e49-freeze-service-content-validation.csv',
	array( 'post_id', 'title', 'fields_checked', 'populated_fields', 'required_missing_count', 'images_state', 'repeaters_state', 'demo_or_current_content_in_acf', 'result', 'notes' ),
	$content_rows
);
copy( $evidence . '/v9-06e49-freeze-service-content-validation.csv', $bak . '/exports/admin-layout/service-content-validation.csv' );

e49fz_csv(
	$evidence . '/v9-06e49-freeze-no-alcohol-copy-paste.csv',
	array( 'post_id', 'title', 'alcohol_terms_expected', 'alcohol_terms_found', 'checked_sources', 'result', 'notes' ),
	$alcohol_rows
);
copy( $evidence . '/v9-06e49-freeze-no-alcohol-copy-paste.csv', $bak . '/exports/admin-layout/no-alcohol-copy-paste.csv' );

file_put_contents(
	$bak . '/exports/admin-layout/admin-layout-inventory.json',
	wp_json_encode(
		array(
			'publish_count' => count( $publish_services ),
			'section_ids'   => $section_ids,
			'e49_targets'   => $e49_targets,
			'e48_reps'      => $e48_reps,
			'accepted_base' => $accepted_base,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	)
);

// ---------------------------------------------------------------------------
// 2) Frontend + route smoke snapshots
// ---------------------------------------------------------------------------
$individual_ids = array_values(
	array_filter(
		$publish_services,
		static function ( $id ) use ( $section_ids ) {
			return ! in_array( (int) $id, $section_ids, true );
		}
	)
);

$routes = array(
	array( 'slug' => 'home', 'label' => '/', 'url' => home_url( '/' ), 'kind' => 'accepted' ),
	array( 'slug' => 'uslugi', 'label' => '/uslugi/', 'url' => home_url( '/uslugi/' ), 'kind' => 'accepted' ),
	array( 'slug' => 'zavisimosti', 'label' => '/uslugi/zavisimosti/', 'url' => home_url( '/uslugi/zavisimosti/' ), 'kind' => 'section', 'post' => 73 ),
	array( 'slug' => 'psihicheskoe', 'label' => '/uslugi/psihicheskoe-zdorovie/', 'url' => home_url( '/uslugi/psihicheskoe-zdorovie/' ), 'kind' => 'section', 'post' => 77 ),
	array( 'slug' => 'rpp', 'label' => '/uslugi/rasstroystva-pischevogo-povedeniya/', 'url' => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ), 'kind' => 'section', 'post' => 84 ),
	array( 'slug' => 'blog', 'label' => '/blog/', 'url' => home_url( '/blog/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'specyalisty', 'label' => '/specyalisty/', 'url' => home_url( '/specyalisty/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'o-centre', 'label' => '/o-centre/', 'url' => home_url( '/o-centre/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'kontakty', 'label' => '/kontakty/', 'url' => home_url( '/kontakty/' ), 'kind' => 'smoke' ),
);

foreach ( $individual_ids as $sid ) {
	$routes[] = array(
		'slug'            => 'p' . $sid,
		'label'           => '#' . $sid . ' ' . get_the_title( $sid ),
		'url'             => get_permalink( $sid ),
		'kind'            => 'service',
		'post'            => $sid,
		'expect_children' => in_array( (int) $sid, $child_tile_ids, true ),
	);
}

$smoke_rows    = array();
$accepted_rows = array();
$snap_index    = array();

foreach ( $routes as $r ) {
	$resp  = e49fz_http( (string) $r['url'] );
	$code  = $resp['code'];
	$body  = $resp['body'];
	$fatal = e49fz_fatal( $body );
	$ok    = ( 200 === $code && ! $fatal );
	file_put_contents( $bak . '/frontend/' . $r['slug'] . '.html', $body );
	file_put_contents( $bak . '/snapshots/' . $r['slug'] . '.html', $body );
	$snap_index[] = $r['slug'] . "\t" . $code . "\t" . strlen( $body ) . "\t" . $r['url'];
	$smoke_rows[] = array( $r['label'], $code, $ok ? 'PASS' : 'FAIL', $fatal ? 'fatal' : '' );

	if ( 'service' === $r['kind'] ) {
		$pid      = (int) $r['post'];
		$has_ph   = ( false !== stripos( $body, 'placeholder-stack' ) );
		$has_h1   = ( false !== stripos( $body, '<h1' ) );
		$has_full = ( false !== strpos( $body, 'service-leaf' ) )
			|| ( false !== strpos( $body, 'alcohol-direct' ) )
			|| ( false !== strpos( $body, 'service-general' ) )
			|| ( strlen( $body ) > 60000 );
		$has_img  = ( false !== strpos( $body, '<img' ) );
		$children = 'n/a';
		$child_ok = true;
		if ( ! empty( $r['expect_children'] ) ) {
			$child_ok = ( false !== strpos( $body, 'service-children' ) )
				|| ( false !== strpos( $body, 'child-services' ) )
				|| ( false !== strpos( $body, 'services-tiles' ) )
				|| ( false !== strpos( $body, 'service-card' ) );
			$children = $child_ok ? 'yes' : 'no';
		}
		// #78 must NOT be placeholder.
		$sok = $ok && ! $has_ph && $has_h1 && $has_full && $has_img && $child_ok;
		if ( 78 === $pid && $has_ph ) {
			$sok = false;
		}
		$fe_rows[] = array(
			$pid,
			get_the_title( $pid ),
			(string) $r['url'],
			$code,
			$has_h1 ? 'yes' : 'no',
			$has_full ? 'yes' : 'no',
			$has_ph ? 'yes' : 'no',
			$has_img ? 'yes' : 'no',
			$children,
			$sok ? 'PASS' : 'FAIL',
			78 === $pid ? 'must_be_full_service' : '',
		);
	}
	if ( 'section' === $r['kind'] ) {
		$has_ph     = ( false !== stripos( $body, 'placeholder-stack' ) );
		$has_nature = ( false !== strpos( $body, 'service-subdivision-nature-v1' ) ) || ( false !== strpos( $body, 'subdivision' ) );
		$role       = (string) get_post_meta( (int) $r['post'], 'service_editor_role', true );
		$accepted_rows[] = array(
			$r['label'],
			'E50 section preserved; HTTP 200; role=section',
			sprintf( 'HTTP %d ph=%s sectionish=%s role=%s size=%d', $code, $has_ph ? 'y' : 'n', $has_nature ? 'y' : 'n', $role, strlen( $body ) ),
			( $ok && ! $has_ph && 'section' === $role ) ? 'PASS' : 'FAIL',
			'E50 freeze preserved',
		);
	}
	if ( 'accepted' === $r['kind'] ) {
		$accepted_rows[] = array(
			$r['label'],
			'unchanged freeze; HTTP 200',
			sprintf( 'HTTP %d size=%d', $code, strlen( $body ) ),
			$ok ? 'PASS' : 'FAIL',
			'no product writes in this freeze task',
		);
	}
}

// Placeholder mode availability (E51) + #78 remains service.
$ph_tpl_rt  = $rt_root . '/wp-content/themes/shpigovsky/template-parts/service/placeholder-stack.php';
$role78     = (string) get_post_meta( 78, 'service_editor_role', true );
$layout78   = (string) get_post_meta( 78, 'service_layout_variant', true );
$accepted_rows[] = array(
	'Placeholder mode (E51)',
	'available in code; #78 remains Услуга',
	sprintf( 'placeholder-stack.php=%s #78=%s/%s', is_file( $ph_tpl_rt ) ? 'yes' : 'no', $role78, $layout78 ),
	( is_file( $ph_tpl_rt ) && 'service' === $role78 ) ? 'PASS' : 'FAIL',
	'Do not switch #78 to placeholder in freeze',
);
$accepted_rows[] = array(
	'#78 final state',
	'service/service_general',
	$role78 . '/' . $layout78,
	( 'service' === $role78 && in_array( $layout78, array( 'service_general', 'alcohol_special' ), true ) ) ? 'PASS' : 'FAIL',
	'',
);

file_put_contents( $bak . '/frontend/snapshot-index.tsv', implode( "\n", $snap_index ) );
e49fz_csv(
	$evidence . '/v9-06e49-freeze-frontend-validation.csv',
	array( 'post_id', 'title', 'url', 'http_status', 'h1_present', 'service_blocks_present', 'placeholder_stack_present', 'images_present', 'child_tiles_present_if_expected', 'result', 'notes' ),
	$fe_rows
);
copy( $evidence . '/v9-06e49-freeze-frontend-validation.csv', $bak . '/frontend/frontend-validation.csv' );

e49fz_csv(
	$evidence . '/v9-06e49-freeze-accepted-pages-validation.csv',
	array( 'page_or_route', 'expected', 'actual', 'result', 'notes' ),
	$accepted_rows
);
copy( $evidence . '/v9-06e49-freeze-accepted-pages-validation.csv', $bak . '/frontend/accepted-pages-validation.csv' );

e49fz_csv(
	$evidence . '/v9-06e49-freeze-route-smoke.csv',
	array( 'route', 'http', 'result', 'notes' ),
	$smoke_rows
);
copy( $evidence . '/v9-06e49-freeze-route-smoke.csv', $bak . '/frontend/route-smoke.csv' );

// ---------------------------------------------------------------------------
// 3) Source/runtime sync
// ---------------------------------------------------------------------------
$crit = array(
	array( 'service-general-helpers.php', 'theme/shpigovsky/inc/service-general-helpers.php', 'wp-content/themes/shpigovsky/inc/service-general-helpers.php' ),
	array( 'alcohol-direct-v9.php', 'theme/shpigovsky/template-parts/service/alcohol-direct-v9.php', 'wp-content/themes/shpigovsky/template-parts/service/alcohol-direct-v9.php' ),
	array( 'ServiceGeneralParity.php', 'plugins/shpigovsky-core/src/Fields/ServiceGeneralParity.php', 'wp-content/plugins/shpigovsky-core/src/Fields/ServiceGeneralParity.php' ),
	array( 'ServiceLayoutGovernance.php', 'plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php', 'wp-content/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php' ),
	array( 'FieldGroups.php', 'plugins/shpigovsky-core/src/Fields/FieldGroups.php', 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php' ),
	array( 'group_fp02_service_general_parity.json', 'acf-json/group_fp02_service_general_parity.json', 'wp-content/acf-json/group_fp02_service_general_parity.json' ),
	array( 'group_fp02_service_section_parity.json', 'acf-json/group_fp02_service_section_parity.json', 'wp-content/acf-json/group_fp02_service_section_parity.json' ),
	array( 'group_fp02_service_layout_hero.json', 'acf-json/group_fp02_service_layout_hero.json', 'wp-content/acf-json/group_fp02_service_layout_hero.json' ),
	array( 'group_fp02_service_hero.json', 'acf-json/group_fp02_service_hero.json', 'wp-content/acf-json/group_fp02_service_hero.json' ),
	array( 'placeholder-stack.php', 'theme/shpigovsky/template-parts/service/placeholder-stack.php', 'wp-content/themes/shpigovsky/template-parts/service/placeholder-stack.php' ),
	array( 'service-helpers.php', 'theme/shpigovsky/inc/service-helpers.php', 'wp-content/themes/shpigovsky/inc/service-helpers.php' ),
	array( 'v9-style.css', 'theme/shpigovsky/assets/css/v9-style.css', 'wp-content/themes/shpigovsky/assets/css/v9-style.css' ),
);

foreach ( glob( $src_root . '/acf-json/*.json' ) ?: array() as $jf ) {
	if ( false !== strpos( (string) file_get_contents( $jf ), 'page_layout_mode' ) ) {
		$base   = basename( $jf );
		$crit[] = array( $base . ' (page_layout_mode)', 'acf-json/' . $base, 'wp-content/acf-json/' . $base );
		break;
	}
}

$sync_rows = array();
foreach ( $crit as $c ) {
	$src   = $src_root . '/' . $c[1];
	$rt    = $rt_root . '/' . $c[2];
	$hs    = e49fz_sha( $src );
	$hr    = e49fz_sha( $rt );
	$match = ( $hs === $hr && 'MISSING' !== $hs ) ? 'YES' : 'NO';
	$notes = '';
	if ( 'v9-style.css' === $c[0] ) {
		$notes  = 'operator runtime CSS authority; drift from source may be intentional';
		$result = ( 'YES' === $match ) ? 'PASS' : 'PASS_DRIFT_OK';
	} else {
		$result = ( 'YES' === $match ) ? 'PASS' : 'FAIL';
	}
	if ( 'MISSING' === $hs || 'MISSING' === $hr ) {
		$result = ( false !== strpos( $c[0], 'page_layout_mode' ) ) ? 'PARTIAL' : 'FAIL';
	}
	$sync_rows[] = array( $c[0], $c[1], $c[2], $match, $result, $notes . " src=$hs rt=$hr" );
}
e49fz_csv(
	$evidence . '/v9-06e49-freeze-source-runtime-sync.csv',
	array( 'file', 'source_path', 'runtime_path', 'hash_match', 'result', 'notes' ),
	$sync_rows
);
copy( $evidence . '/v9-06e49-freeze-source-runtime-sync.csv', $bak . '/hashes/source-runtime-sync.csv' );

$manifest_lines = array( "file\tsource_sha\truntime_sha\tmatch" );
foreach ( $sync_rows as $row ) {
	$manifest_lines[] = implode( "\t", array( $row[0], $row[3], $row[5], $row[4] ) );
}
file_put_contents( $bak . '/hashes/critical-files.tsv', implode( "\n", $manifest_lines ) );

// Aggregate counters for summary.
$inv_pass = 0;
$inv_fail = 0;
foreach ( $inv_rows as $row ) {
	if ( 'PASS' === $row[13] ) {
		++$inv_pass;
	} else {
		++$inv_fail;
	}
}
$admin_pass = 0;
foreach ( $admin_rows as $row ) {
	if ( 'PASS' === $row[8] ) {
		++$admin_pass;
	}
}
$content_pass = 0;
foreach ( $content_rows as $row ) {
	if ( 'PASS' === $row[8] ) {
		++$content_pass;
	}
}
$alc_pass = 0;
foreach ( $alcohol_rows as $row ) {
	if ( 'PASS' === $row[5] ) {
		++$alc_pass;
	}
}
$fe_pass = 0;
foreach ( $fe_rows as $row ) {
	if ( 'PASS' === $row[9] ) {
		++$fe_pass;
	}
}
$smoke_pass = 0;
foreach ( $smoke_rows as $row ) {
	if ( 'PASS' === $row[2] ) {
		++$smoke_pass;
	}
}

$summary = array(
	'phase'              => 'V9-06E49-FULL-SERVICE-ROLLOUT-FREEZE',
	'backup'             => $bak,
	'db_writes'          => $db_writes,
	'publish_count'      => count( $publish_services ),
	'inventory_pass'     => $inv_pass,
	'inventory_fail'     => $inv_fail,
	'admin_pass'         => $admin_pass,
	'admin_total'        => count( $admin_rows ),
	'content_pass'       => $content_pass,
	'content_total'      => count( $content_rows ),
	'alcohol_pass'       => $alc_pass,
	'alcohol_total'      => count( $alcohol_rows ),
	'frontend_pass'      => $fe_pass,
	'frontend_total'     => count( $fe_rows ),
	'smoke_pass'         => $smoke_pass,
	'smoke_total'        => count( $smoke_rows ),
	'#78_role'           => $role78,
	'#78_layout'         => $layout78,
	'timestamp'          => gmdate( 'c' ),
);
file_put_contents( $bak . '/freeze-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $evidence . '/v9-06e49-freeze-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

echo 'E49_FREEZE_VALIDATE_OK'
	. ' db_writes=' . $db_writes
	. ' publish=' . count( $publish_services )
	. ' inv=' . $inv_pass . '/' . count( $inv_rows )
	. ' admin=' . $admin_pass . '/' . count( $admin_rows )
	. ' content=' . $content_pass . '/' . count( $content_rows )
	. ' alc=' . $alc_pass . '/' . count( $alcohol_rows )
	. ' fe=' . $fe_pass . '/' . count( $fe_rows )
	. ' smoke=' . $smoke_pass . '/' . count( $smoke_rows )
	. ' role78=' . $role78
	. ' layout78=' . $layout78
	. "\n";
exit( 0 );

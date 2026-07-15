<?php
/**
 * V9-06E52 — read-only inventory + current-model audit for normal/generic pages.
 *
 * @package FP0002
 */

declare(strict_types=1);

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require $wp_load;

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
if ( ! is_dir( $evidence ) ) {
	wp_mkdir_p( $evidence );
}

$hardcoded_demo = 'Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.';

/**
 * @param string            $path Path.
 * @param array<int,string> $header Header.
 * @param array<int,array>  $rows Rows.
 */
function e52_csv( string $path, array $header, array $rows ): void {
	$fp = fopen( $path, 'wb' );
	if ( ! $fp ) {
		fwrite( STDERR, "Cannot write $path\n" );
		exit( 1 );
	}
	fprintf( $fp, "\xEF\xBB\xBF" );
	fputcsv( $fp, $header );
	foreach ( $rows as $row ) {
		fputcsv( $fp, $row );
	}
	fclose( $fp );
}

/**
 * @param mixed $v Value.
 */
function e52_empty( $v ): bool {
	if ( null === $v || false === $v ) {
		return true;
	}
	if ( is_array( $v ) ) {
		return array() === $v;
	}
	return '' === trim( (string) $v );
}

$front_id = (int) get_option( 'page_on_front' );
$posts_id = (int) get_option( 'page_for_posts' );

$dedicated = array(
	'page-templates/home.php',
	'page-templates/contacts.php',
	'page-templates/reviews.php',
	'page-templates/legal.php',
	'page-templates/institutional.php',
	'page-templates/services-hub.php',
	'page-templates/services.php',
	'page-templates/blog.php',
);

$pages = get_posts(
	array(
		'post_type'      => 'page',
		'post_status'    => array( 'publish', 'draft', 'private', 'pending', 'future' ),
		'numberposts'    => -1,
		'orderby'        => 'ID',
		'order'          => 'ASC',
		'suppress_filters' => true,
	)
);

$inv_rows   = array();
$audit_rows = array();
$included   = array();
$excluded   = 0;
$layout_present_count = 0;
$hardcoded_found      = 0;
$acf_sot_count        = 0;
$seed_needed_count    = 0;

$layout_field = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_page_layout_mode' ) : null;
$generic_content_field = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_generic_page_body' ) : null;
$has_layout_group = is_array( $layout_field );
$has_content_group = is_array( $generic_content_field );

$content_src_file = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/template-parts/generic/content-page.php';
$has_hardcoded_in_tpl = is_file( $content_src_file ) && false !== strpos( (string) file_get_contents( $content_src_file ), 'Раздел находится в подготовке' );

foreach ( $pages as $p ) {
	$id       = (int) $p->ID;
	$title    = (string) $p->post_title;
	$status   = (string) $p->post_status;
	$parent   = (int) $p->post_parent;
	$ptitle   = $parent > 0 ? (string) get_the_title( $parent ) : '';
	$tpl      = (string) get_page_template_slug( $id );
	$url      = (string) get_permalink( $id );
	$is_front = ( $id === $front_id ) ? 'yes' : 'no';
	$is_posts = ( $id === $posts_id ) ? 'yes' : 'no';
	$mode     = function_exists( 'get_field' ) ? get_field( 'page_layout_mode', $id ) : '';
	$mode     = is_string( $mode ) && '' !== $mode ? $mode : ( $tpl === 'page-templates/generic.php' ? 'full(default)' : '' );

	$body_acf = function_exists( 'get_field' ) ? get_field( 'generic_page_body', $id ) : null;
	$lead_acf = function_exists( 'get_field' ) ? get_field( 'generic_page_lead', $id ) : null;
	$pc       = trim( (string) $p->post_content );
	$has_acf_group = ( $tpl === 'page-templates/generic.php' && $has_layout_group ) ? 'yes' : 'no';
	if ( $tpl === 'page-templates/generic.php' && $has_content_group ) {
		$has_acf_group = 'yes+content';
	}

	$exclude_reason = '';
	$included_flag  = 'yes';

	if ( 'yes' === $is_front ) {
		$exclude_reason = 'front_page';
		$included_flag  = 'no';
	} elseif ( 'yes' === $is_posts ) {
		$exclude_reason = 'posts_page';
		$included_flag  = 'no';
	} elseif ( $tpl !== '' && $tpl !== 'page-templates/generic.php' && in_array( $tpl, $dedicated, true ) ) {
		$exclude_reason = 'dedicated_template:' . $tpl;
		$included_flag  = 'no';
	} elseif ( $tpl !== '' && $tpl !== 'page-templates/generic.php' ) {
		$exclude_reason = 'non_generic_template:' . $tpl;
		$included_flag  = 'no';
	} elseif ( $tpl === '' ) {
		// Default page.php — not generic template; exclude unless task wants them.
		$exclude_reason = 'default_page_template';
		$included_flag  = 'no';
	}

	// Specialists children are generic and included (task excludes only if separate accepted model — they use generic).
	if ( 'no' === $included_flag ) {
		++$excluded;
	}

	$fe_status = 'unknown';
	if ( 'publish' === $status ) {
		$fe_status = 'probe_pending';
	}

	$notes = '';
	if ( $tpl === 'page-templates/generic.php' ) {
		if ( ! e52_empty( $body_acf ) || ! e52_empty( $lead_acf ) ) {
			$notes = 'has_generic_acf_content';
		} elseif ( '' !== $pc ) {
			$notes = 'post_content_present';
		} else {
			$notes = 'empty_post_content_would_show_hardcoded_demo';
		}
	}

	$inv_rows[] = array(
		$id,
		$title,
		$url,
		$status,
		$parent,
		$ptitle,
		$tpl !== '' ? $tpl : '(default)',
		$is_front,
		$is_posts,
		$exclude_reason,
		$included_flag,
		$mode,
		$has_acf_group,
		$fe_status,
		$notes,
	);

	if ( 'yes' === $included_flag ) {
		$included[] = $id;
		$frontend_source = 'unknown';
		$hardcoded_demo_found = $has_hardcoded_in_tpl ? 'yes' : 'no';
		$acf_seed_needed = 'no';
		$placeholder_works = $has_layout_group ? 'yes_field_present' : 'no';
		$has_plm = $has_layout_group ? 'yes' : 'no';

		if ( ! e52_empty( $body_acf ) ) {
			$frontend_source = 'acf';
			++$acf_sot_count;
		} elseif ( '' !== $pc ) {
			$frontend_source = 'post_content';
			$acf_seed_needed = 'yes';
			++$seed_needed_count;
		} elseif ( $has_hardcoded_in_tpl ) {
			$frontend_source = 'hardcoded_demo';
			$acf_seed_needed = 'yes';
			++$seed_needed_count;
			++$hardcoded_found;
		} else {
			$frontend_source = 'mixed';
			$acf_seed_needed = 'yes';
			++$seed_needed_count;
		}

		if ( $has_layout_group ) {
			++$layout_present_count;
		}

		$risk = 'low';
		if ( 'hardcoded_demo' === $frontend_source ) {
			$risk = 'medium';
		}
		if ( ! $has_content_group ) {
			$risk = 'medium';
		}

		$audit_rows[] = array(
			$id,
			$title,
			$tpl,
			$frontend_source,
			$has_plm,
			$mode,
			$placeholder_works,
			$hardcoded_demo_found,
			$acf_seed_needed,
			$risk,
			sprintf(
				'pc_len=%d; body_acf=%s; lead_acf=%s; content_group=%s',
				strlen( $pc ),
				e52_empty( $body_acf ) ? 'empty' : 'set',
				e52_empty( $lead_acf ) ? 'empty' : 'set',
				$has_content_group ? 'present' : 'missing'
			),
		);
	}
}

e52_csv(
	$evidence . '/v9-06e52-generic-pages-inventory.csv',
	array(
		'post_id',
		'title',
		'url',
		'post_status',
		'parent_id',
		'parent_title',
		'template',
		'is_front_page',
		'is_posts_page',
		'exclude_reason',
		'included_in_e52',
		'current_layout_mode',
		'has_acf_group',
		'frontend_status',
		'notes',
	),
	$inv_rows
);

e52_csv(
	$evidence . '/v9-06e52-generic-pages-current-model-audit.csv',
	array(
		'post_id',
		'title',
		'template',
		'frontend_source',
		'has_page_layout_mode',
		'current_layout_mode',
		'placeholder_works_now',
		'hardcoded_demo_found',
		'acf_seed_needed',
		'risk',
		'notes',
	),
	$audit_rows
);

$summary = array(
	'total_pages'              => count( $pages ),
	'excluded'                 => $excluded,
	'included'                 => count( $included ),
	'included_ids'             => $included,
	'pages_with_layout_mode'   => $layout_present_count,
	'pages_needing_seed'       => $seed_needed_count,
	'pages_already_acf_sot'    => $acf_sot_count,
	'hardcoded_demo_in_tpl'    => $has_hardcoded_in_tpl,
	'hardcoded_demo_pages'     => $hardcoded_found,
	'layout_field_registered'  => $has_layout_group,
	'content_field_registered' => $has_content_group,
	'hardcoded_demo_text'      => $hardcoded_demo,
	'siteurl'                  => home_url( '/' ),
);

file_put_contents( $evidence . '/v9-06e52-audit-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

echo "AUDIT_OK total=" . count( $pages ) . " included=" . count( $included ) . " excluded=$excluded content_group=" . ( $has_content_group ? 'yes' : 'no' ) . PHP_EOL;
echo 'INCLUDED_IDS=' . implode( ',', $included ) . PHP_EOL;

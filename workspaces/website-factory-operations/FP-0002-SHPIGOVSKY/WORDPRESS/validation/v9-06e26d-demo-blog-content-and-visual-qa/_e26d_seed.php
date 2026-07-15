<?php
/**
 * FP-0002 V9-06E26D — Demo blog article seed helper.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * @package FP0002_E26D
 */

define( 'WP_USE_THEMES', false );

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
if ( ! is_file( $wp_load ) ) {
	fwrite( STDERR, "wp-load.php not found\n" );
	exit( 1 );
}

require $wp_load;

$fixture_path = __DIR__ . '/fixture-data.json';
if ( ! is_file( $fixture_path ) ) {
	fwrite( STDERR, "fixture-data.json not found\n" );
	exit( 1 );
}

$fixture = json_decode( (string) file_get_contents( $fixture_path ), true );
if ( ! is_array( $fixture ) ) {
	fwrite( STDERR, "fixture-data.json invalid\n" );
	exit( 1 );
}

/**
 * Set ACF field with postmeta fallback.
 *
 * @param int    $post_id Post ID.
 * @param string $name Field name.
 * @param mixed  $value Value.
 */
function fp02e26d_set_field( $post_id, $name, $value ) {
	if ( function_exists( 'update_field' ) ) {
		update_field( $name, $value, $post_id );
		return;
	}
	update_post_meta( $post_id, $name, $value );
}

$result = array(
	'wave'           => 'V9-06E26D',
	'result'         => 'FAIL',
	'action'         => 'none',
	'post_id'        => 0,
	'slug'           => $fixture['slug'],
	'status'         => 'publish',
	'url'            => '',
	'db_write_count' => 0,
	'acf_fields'     => array(),
	'media_strategy' => 'theme_asset_fallback_no_upload',
);

$existing = get_posts(
	array(
		'name'           => $fixture['slug'],
		'post_type'      => 'post',
		'post_status'    => array( 'publish', 'draft', 'pending', 'future', 'private', 'auto-draft' ),
		'posts_per_page' => 1,
	)
);

$post_id  = 0;
$action   = 'create';
$existing_post = ! empty( $existing[0] ) && $existing[0] instanceof WP_Post ? $existing[0] : null;

if ( $existing_post ) {
	if ( 'auto-draft' === $existing_post->post_status && '' === $existing_post->post_name ) {
		wp_delete_post( (int) $existing_post->ID, true );
		$result['db_write_count']++;
		$existing_post = null;
	} elseif ( 'nazvanie-stati' === $existing_post->post_name && in_array( $existing_post->post_status, array( 'publish', 'draft' ), true ) ) {
		$post_id = (int) $existing_post->ID;
		$action  = 'update';
	} else {
		$result['error'] = 'Existing non-fixture post blocks seed';
		echo wp_json_encode( $result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );
		exit( 2 );
	}
}

$postarr = array(
	'post_type'    => 'post',
	'post_status'  => 'publish',
	'post_name'    => $fixture['slug'],
	'post_title'   => $fixture['title'],
	'post_excerpt' => $fixture['excerpt'],
	'post_content' => $fixture['body_html'],
	'post_date'    => $fixture['post_date'],
);

if ( $post_id > 0 ) {
	$postarr['ID'] = $post_id;
	$updated       = wp_update_post( $postarr, true );
	if ( is_wp_error( $updated ) ) {
		$result['error'] = $updated->get_error_message();
		echo wp_json_encode( $result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );
		exit( 1 );
	}
	$result['db_write_count']++;
} else {
	$post_id = (int) wp_insert_post( $postarr, true );
	if ( is_wp_error( $post_id ) || $post_id <= 0 ) {
		$result['error'] = is_wp_error( $post_id ) ? $post_id->get_error_message() : 'insert failed';
		echo wp_json_encode( $result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );
		exit( 1 );
	}
	$result['db_write_count']++;
}

$acf_map = array(
	'article_lead'               => $fixture['lead'],
	'article_reading_time'       => (int) $fixture['reading_time_minutes'],
	'article_author_label'       => $fixture['author_label'],
	'article_hide_author_public' => 0,
	'article_show_date_public'   => 1,
	'article_show_toc'           => 1,
	'article_toc_title'          => 'Оглавление:',
	'article_conclusion_heading' => 'Заключение',
	'article_conclusion_quote'   => $fixture['conclusion_quote'],
	'article_source_items'       => $fixture['source_items'],
	'article_source_file_name'   => 'nazvanie-stati.html',
	'article_editor_status'      => 'DEMO_FIXTURE',
	'article_content_qa_status'  => 'LOCAL_QA',
);

foreach ( $acf_map as $name => $value ) {
	fp02e26d_set_field( $post_id, $name, $value );
	$result['acf_fields'][] = $name;
	$result['db_write_count']++;
}

$result['action']  = $action;
$result['post_id'] = $post_id;
$result['url']     = get_permalink( $post_id );
$result['result']  = 'PASS';
$result['content_sections'] = array(
	'h2_count'      => (int) $fixture['h2_count'],
	'h3_count'      => (int) $fixture['h3_count'],
	'inline_images' => (int) $fixture['inline_image_count'],
	'sources_count' => count( $fixture['source_items'] ),
	'faq_count'     => 0,
);

echo wp_json_encode( $result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );

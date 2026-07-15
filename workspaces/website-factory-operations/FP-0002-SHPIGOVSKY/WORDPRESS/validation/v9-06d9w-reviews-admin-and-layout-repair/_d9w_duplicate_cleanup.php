<?php
/**
 * FP-0002 V9-06D9-W — duplicate ACF group cleanup (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix   = $wpdb->prefix;
$group_key = 'group_fp02_site_options_reviews';

$all_posts = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT ID, post_status, post_modified FROM {$prefix}posts WHERE post_type = %s AND post_name = %s ORDER BY ID",
		'acf-field-group',
		$group_key
	),
	ARRAY_A
);

$scored = array();
foreach ( $all_posts as $row ) {
	$content = $wpdb->get_var(
		$wpdb->prepare(
			"SELECT post_content FROM {$prefix}posts WHERE ID = %d",
			$row['ID']
		)
	);
	$location = 'unknown';
	if ( false !== strpos( $content, 'fp02-reviews' ) ) {
		$location = 'fp02-reviews';
	} elseif ( false !== strpos( $content, 'fp02-site-settings' ) ) {
		$location = 'fp02-site-settings';
	}
	$score = 0;
	if ( 'fp02-reviews' === $location ) {
		$score += 100;
	}
	if ( 'publish' === $row['post_status'] ) {
		$score += 10;
	}
	$score += (int) $row['ID'];
	$scored[] = array(
		'ID'       => (int) $row['ID'],
		'location' => $location,
		'status'   => $row['post_status'],
		'score'    => $score,
	);
}

usort(
	$scored,
	static function ( $a, $b ) {
		return $b['score'] <=> $a['score'];
	}
);

$keep_id = ! empty( $scored ) ? $scored[0]['ID'] : null;
$actions = array();

foreach ( $scored as $entry ) {
	if ( $entry['ID'] === $keep_id ) {
		$actions[] = array(
			'ID'     => $entry['ID'],
			'action' => 'KEEP',
			'reason' => 'canonical active group',
		);
		continue;
	}

	$result = wp_trash_post( $entry['ID'] );
	$actions[] = array(
		'ID'     => $entry['ID'],
		'action' => 'TRASH',
		'result' => (bool) $result,
		'reason' => 'stale duplicate',
	);
}

$remaining = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT ID, post_status FROM {$prefix}posts WHERE post_type = %s AND post_name = %s AND post_status != 'trash' ORDER BY ID",
		'acf-field-group',
		$group_key
	),
	ARRAY_A
);

echo wp_json_encode(
	array(
		'phase'              => 'V9-06D9-W',
		'generated_at'       => gmdate( 'c' ),
		'group_key'          => $group_key,
		'keep_id'            => $keep_id,
		'actions'            => $actions,
		'remaining_non_trash'=> $remaining,
		'remaining_count'    => count( $remaining ),
		'result'             => ( 1 === count( $remaining ) && (int) $remaining[0]['ID'] === (int) $keep_id ) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);

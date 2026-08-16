<?php
/**
 * V9-06E62C migration: review UIDs + O-centre bullet seed + reversible reorder test.
 */
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$ev = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression';
$log = array( 'started_at' => gmdate( 'c' ), 'writes' => array() );

$seed_text = 'Мы убеждены, что физическое движение и качество отдыха — такая же часть программы, как психотерапия и нейрокоррекция. Поэтому на территории центра есть всё необходимое для полноценной реабилитации: бассейн и сауна для восстановления тела и снятия физического напряжения, теннисный корт для тех, кто хочет двигаться и соревноваться с собой, тренажёрный зал, обустроенные места для прогулок и отдыха на открытом воздухе.';

$page_id  = 11;
$existing = trim( (string) get_field( 'infrastructure_narrative_bullet_intro', $page_id ) );
if ( '' === $existing ) {
	update_field( 'infrastructure_narrative_bullet_intro', $seed_text, $page_id );
	$log['writes'][] = array(
		'scope'  => 'o-centre-bullet-seed',
		'action' => 'seed_empty',
		'page'   => $page_id,
		'bytes'  => strlen( $seed_text ),
	);
} else {
	$log['writes'][] = array(
		'scope'  => 'o-centre-bullet-seed',
		'action' => 'skip_nonempty',
		'page'   => $page_id,
		'bytes'  => strlen( $existing ),
	);
}

$ctx        = shpigovsky_get_reviews_options_context();
$uid_result = shpigovsky_ensure_review_uids( $ctx );
$log['writes'][] = array( 'scope' => 'review-uid-migration', 'result' => $uid_result );

// Snapshot accepted order AFTER UID assignment.
$accepted_rows = get_field( 'reviews_items', $ctx );
file_put_contents( $ev . '/reviews-items-after-uid-before-reorder.json', wp_json_encode( $accepted_rows, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

$per     = shpigovsky_get_reviews_per_page();
$reorder = array( 'performed' => false, 'restored' => false );

if ( is_array( $accepted_rows ) && count( $accepted_rows ) >= 12 ) {
	$sample_index = 9;
	$sample_uid   = shpigovsky_sanitize_review_uid( $accepted_rows[ $sample_index ]['review_uid'] ?? '' );

	// Compute before page via raw rows.
	$before_page = (int) floor( $sample_index / $per ) + 1;

	$working = $accepted_rows;
	$moved   = $working[ $sample_index ];
	unset( $working[ $sample_index ] );
	$working   = array_values( $working );
	$working[] = $moved;
	update_field( 'reviews_items', $working, $ctx );
	$log['writes'][] = array(
		'scope' => 'reorder-test-move',
		'uid'   => $sample_uid,
		'from'  => $sample_index,
		'to'    => count( $working ) - 1,
	);

	$after_rows  = get_field( 'reviews_items', $ctx );
	$after_index = null;
	$after_uid   = '';
	foreach ( $after_rows as $i => $row ) {
		$u = shpigovsky_sanitize_review_uid( $row['review_uid'] ?? '' );
		if ( $u === $sample_uid ) {
			$after_index = $i;
			$after_uid   = $u;
			break;
		}
	}
	$after_page = null !== $after_index ? ( (int) floor( $after_index / $per ) + 1 ) : null;

	$reorder = array(
		'performed'       => true,
		'sample_uid'      => $sample_uid,
		'before_index'    => $sample_index,
		'before_page'     => $before_page,
		'after_index'     => $after_index,
		'after_page'      => $after_page,
		'uid_unchanged'   => ( $after_uid === $sample_uid ),
		'page_changed'    => ( $before_page !== $after_page ),
		'restored'        => false,
	);

	// Restore accepted order.
	update_field( 'reviews_items', $accepted_rows, $ctx );
	$verify = get_field( 'reviews_items', $ctx );
	$verify_uid = shpigovsky_sanitize_review_uid( $verify[ $sample_index ]['review_uid'] ?? '' );
	$reorder['restored']            = ( $verify_uid === $sample_uid );
	$reorder['restored_index']      = $sample_index;
	$reorder['restored_uid_match']  = ( $verify_uid === $sample_uid );
	$log['writes'][] = array(
		'scope'  => 'reorder-test-restore',
		'action' => 'restored_accepted_order',
		'uid'    => $sample_uid,
	);
}

// Final matrix (after restore).
$items  = shpigovsky_get_reviews_items( array( 'featured_only' => false, 'limit' => 0 ) );
$matrix = array();
foreach ( $items as $i => $item ) {
	$uid      = shpigovsky_sanitize_review_uid( $item['review_uid'] ?? '' );
	$page     = (int) floor( $i / $per ) + 1;
	$text_raw = (string) ( $item['text'] ?? '' );
	$is_demo  = ( false !== stripos( (string) ( $item['author'] ?? '' ), 'demo' ) )
		|| ( false !== stripos( $text_raw, 'e62b-demo' ) )
		|| ( false !== stripos( $text_raw, 'E62B-DEMO' ) );
	$matrix[] = array(
		'index'       => $i,
		'review_id'   => (int) ( $item['review_id'] ?? 0 ),
		'review_uid'  => $uid,
		'author'      => (string) ( $item['author'] ?? '' ),
		'page'        => $page,
		'archive_url' => shpigovsky_get_review_archive_url( $uid ),
		'featured'    => ! empty( $item['featured'] ),
		'is_demo'     => $is_demo,
	);
}

$uids = array_column( $matrix, 'review_uid' );
$log['final_uid_count'] = count( $matrix );
$log['unique_uids']     = count( array_unique( array_filter( $uids ) ) );
$log['empty_uids']      = count( array_filter( $uids, static function ( $u ) { return '' === $u; } ) );
$log['reorder_test']    = $reorder;
$log['finished_at']     = gmdate( 'c' );

file_put_contents( $ev . '/db-writes.json', wp_json_encode( $log, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
file_put_contents( $ev . '/review-uid-migration-matrix.json', wp_json_encode( $matrix, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
file_put_contents( $ev . '/reorder-stability-test.json', wp_json_encode( $reorder, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

$csv = "index,review_id,review_uid,page,author,featured,is_demo,archive_url\n";
foreach ( $matrix as $m ) {
	$csv .= sprintf(
		"%d,%d,%s,%d,\"%s\",%d,%d,%s\n",
		$m['index'],
		$m['review_id'],
		$m['review_uid'],
		$m['page'],
		str_replace( '"', "''", $m['author'] ),
		$m['featured'] ? 1 : 0,
		$m['is_demo'] ? 1 : 0,
		$m['archive_url']
	);
}
file_put_contents( $ev . '/review-uid-migration-matrix.csv', $csv );

echo 'OK rows=' . count( $matrix ) . ' unique=' . $log['unique_uids'] . ' empty=' . $log['empty_uids'] . PHP_EOL;
echo 'REORDER ' . wp_json_encode( $reorder ) . PHP_EOL;
echo 'UID_MIGRATE ' . wp_json_encode( $uid_result ) . PHP_EOL;

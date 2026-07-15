<?php
/**
 * FP-0002 V9-06D9-X — direct DB options context migration (TEMP — NOT FOR GIT).
 * Does not require wp-load.php.
 */
$mysqli = new mysqli( '127.0.0.1', 'root', '', 'mars_wp_fp0002' );

if ( $mysqli->connect_error ) {
	echo json_encode( array( 'result' => 'FAIL', 'error' => $mysqli->connect_error ) );
	exit( 1 );
}

$mysqli->set_charset( 'utf8mb4' );

$source_prefix = 'options_reviews_';
$target_prefix = 'fp02-reviews_reviews_';
$copied        = array();

$result = $mysqli->query(
	"SELECT option_name, option_value FROM fp02_options WHERE option_name LIKE '{$source_prefix}%' OR option_name LIKE '_{$source_prefix}%' ORDER BY option_name"
);

if ( ! $result ) {
	echo json_encode( array( 'result' => 'FAIL', 'error' => $mysqli->error ) );
	exit( 1 );
}

$stmt = $mysqli->prepare( 'UPDATE fp02_options SET option_value = ? WHERE option_name = ?' );

while ( $row = $result->fetch_assoc() ) {
	$source_name = $row['option_name'];
	$target_name = str_replace( 'options_reviews_', $target_prefix, $source_name );
	$target_name = str_replace( '_options_reviews_', '_fp02-reviews_reviews_', $target_name );
	$value       = $row['option_value'];

	if ( 0 === strpos( $source_name, '_' ) ) {
		if ( '_options_reviews_enabled' === $source_name ) {
			$value = 'field_fp02_options_reviews_enabled';
		} elseif ( '_options_reviews_section_heading' === $source_name ) {
			$value = 'field_fp02_options_reviews_section_heading';
		} elseif ( '_options_reviews_items' === $source_name ) {
			$value = 'field_fp02_options_reviews_items';
		} elseif ( preg_match( '/_options_reviews_items_\d+_review_([a-z_]+)$/', $source_name, $matches ) ) {
			$value = 'field_fp02_options_review_' . $matches[1];
		}
	}

	$stmt->bind_param( 'ss', $value, $target_name );
	$stmt->execute();
	$copied[] = array(
		'source' => $source_name,
		'target' => $target_name,
	);
}

$result->free();
$stmt->close();

$fp02_first   = '';
$option_first = '';
$res          = $mysqli->query(
	"SELECT option_name, option_value FROM fp02_options WHERE option_name IN ('fp02-reviews_reviews_items_0_review_author','options_reviews_items_0_review_author')"
);

while ( $row = $res->fetch_assoc() ) {
	if ( 'fp02-reviews_reviews_items_0_review_author' === $row['option_name'] ) {
		$fp02_first = $row['option_value'];
	}
	if ( 'options_reviews_items_0_review_author' === $row['option_name'] ) {
		$option_first = $row['option_value'];
	}
}

$mysqli->close();

echo json_encode(
	array(
		'phase'                   => 'V9-06D9-X',
		'generated_at'            => gmdate( 'c' ),
		'migration_strategy'      => 'copy options_reviews_* to fp02-reviews_reviews_* preserving operator edit',
		'meta_copied_count'       => count( $copied ),
		'meta_copied_sample'      => array_slice( $copied, 0, 6 ),
		'option_first_author'     => $option_first,
		'fp02_first_author_after' => $fp02_first,
		'result'                  => ( 'Андрей, Москва' === $fp02_first ) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);

<?php
/**
 * One-shot evidence dump — comfort options before Task I split.
 */

$mysqli = new mysqli( '127.0.0.1', 'mli_shpigovsky_app', '9st4UPjdkc5MXyuNKEGTQaS0V7AD1ClR', 'mars_wp_fp0002' );
if ( $mysqli->connect_error ) {
	fwrite( STDERR, 'CONNECT: ' . $mysqli->connect_error . PHP_EOL );
	exit( 1 );
}
$mysqli->set_charset( 'utf8mb4' );

$sql = "SELECT option_name, LENGTH(option_value) AS value_len, option_value
	FROM fp02_options
	WHERE option_name LIKE '%comfort%'
	   OR option_name LIKE '%rehab_requirements%'
	   OR option_name LIKE 'fp02-block-comfort%'
	ORDER BY option_name";
$res  = $mysqli->query( $sql );
$rows = array();
while ( $row = $res->fetch_assoc() ) {
	$rows[] = array(
		'option_name'   => $row['option_name'],
		'value_len'     => (int) $row['value_len'],
		'option_value'  => $row['option_value'],
	);
}

$dir = __DIR__;
if ( ! is_dir( $dir ) ) {
	mkdir( $dir, 0755, true );
}

$path = $dir . '/comfort-options-pre-split-evidence.json';
file_put_contents(
	$path,
	json_encode(
		array(
			'exported_at'      => gmdate( 'c' ),
			'purpose'          => 'pre-split comfort option values evidence for Task I',
			'storage_post_id'  => 'fp02-block-comfort',
			'row_count'        => count( $rows ),
			'rows'             => $rows,
		),
		JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
	)
);

echo 'wrote ' . $path . ' rows=' . count( $rows ) . PHP_EOL;
foreach ( $rows as $r ) {
	echo $r['option_name'] . ' len=' . $r['value_len'] . PHP_EOL;
}

$res2 = $mysqli->query( "SELECT option_name, option_value FROM fp02_options WHERE option_name LIKE '%footer_credit%'" );
echo "--- footer_credit ---" . PHP_EOL;
while ( $row = $res2->fetch_assoc() ) {
	echo $row['option_name'] . '=' . $row['option_value'] . PHP_EOL;
}

$mysqli->close();

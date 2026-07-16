<?php
$evidence = __DIR__;
$mysqli   = new mysqli( '127.0.0.1', 'mli_shpigovsky_app', '9st4UPjdkc5MXyuNKEGTQaS0V7AD1ClR', 'mars_wp_fp0002' );
$mysqli->set_charset( 'utf8mb4' );

$pre = json_decode( file_get_contents( $evidence . '/comfort-options-pre-split-evidence.json' ), true );
$map = array();
foreach ( $pre['rows'] as $r ) {
	$map[ $r['option_name'] ] = hash( 'sha256', $r['option_value'] );
}

$res = $mysqli->query(
	"SELECT option_name, option_value FROM fp02_options
	 WHERE option_name LIKE 'fp02-block-comfort_%'
	    OR option_name LIKE '_fp02-block-comfort_%'
	 ORDER BY option_name"
);
$now = array();
while ( $row = $res->fetch_assoc() ) {
	$now[ $row['option_name'] ] = hash( 'sha256', $row['option_value'] );
}

$mismatch = array();
$missing  = array();
$extra    = array();
$checked  = 0;

foreach ( $map as $name => $hash ) {
	if ( ! isset( $now[ $name ] ) ) {
		$missing[] = $name;
		continue;
	}
	$checked++;
	if ( $now[ $name ] !== $hash ) {
		$mismatch[] = $name;
	}
}
foreach ( $now as $name => $_h ) {
	if ( ! isset( $map[ $name ] ) ) {
		$extra[] = $name;
	}
}

$out = array(
	'checked'  => $checked,
	'mismatch' => $mismatch,
	'missing'  => $missing,
	'extra'    => $extra,
	'pass'     => empty( $mismatch ) && empty( $missing ),
);
file_put_contents( $evidence . '/comfort-options-post-split-integrity.json', json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
echo json_encode( $out, JSON_UNESCAPED_UNICODE ) . PHP_EOL;
$mysqli->close();

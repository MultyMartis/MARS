<?php
/**
 * Set footer credit URL + deactivate legacy comfort ACF group post if present.
 */

$mysqli = new mysqli( '127.0.0.1', 'mli_shpigovsky_app', '9st4UPjdkc5MXyuNKEGTQaS0V7AD1ClR', 'mars_wp_fp0002' );
if ( $mysqli->connect_error ) {
	fwrite( STDERR, $mysqli->connect_error . PHP_EOL );
	exit( 1 );
}
$mysqli->set_charset( 'utf8mb4' );

$url   = 'https://overseo.ru/';
$pairs = array(
	'fp02-block-footer_footer_credit_url'  => $url,
	'_fp02-block-footer_footer_credit_url' => 'field_fp02_footer_credit_url',
);

foreach ( $pairs as $name => $value ) {
	$chk = $mysqli->prepare( 'SELECT option_id FROM fp02_options WHERE option_name = ? LIMIT 1' );
	$chk->bind_param( 's', $name );
	$chk->execute();
	$exists = $chk->get_result()->fetch_assoc();
	$chk->close();

	if ( $exists ) {
		$upd = $mysqli->prepare( 'UPDATE fp02_options SET option_value = ? WHERE option_name = ?' );
		$upd->bind_param( 'ss', $value, $name );
		$upd->execute();
		$upd->close();
		echo "updated $name\n";
	} else {
		$autoload = 'no';
		$ins      = $mysqli->prepare( 'INSERT INTO fp02_options (option_name, option_value, autoload) VALUES (?, ?, ?)' );
		$ins->bind_param( 'sss', $name, $value, $autoload );
		$ins->execute();
		$ins->close();
		echo "inserted $name\n";
	}
}

$verify = $mysqli->query( "SELECT option_name, option_value FROM fp02_options WHERE option_name IN ('fp02-block-footer_footer_credit_url','_fp02-block-footer_footer_credit_url')" );
while ( $r = $verify->fetch_assoc() ) {
	echo 'VERIFY ' . $r['option_name'] . '=' . $r['option_value'] . PHP_EOL;
}

$q = $mysqli->query( "SELECT ID, post_title, post_status, post_name FROM fp02_posts WHERE post_type = 'acf-field-group' AND post_name = 'group_fp02_block_comfort'" );
$found = false;
while ( $r = $q->fetch_assoc() ) {
	$found = true;
	echo 'legacy group post ID=' . $r['ID'] . ' status=' . $r['post_status'] . PHP_EOL;
	$id = (int) $r['ID'];
	$mysqli->query( "UPDATE fp02_posts SET post_status = 'acf-disabled' WHERE ID = {$id}" );
	echo "disabled legacy group post {$id}\n";
}
if ( ! $found ) {
	echo "no DB-synced legacy group_fp02_block_comfort post\n";
}

$mysqli->close();
echo "done\n";

<?php
$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
if ( ! is_array( $group ) ) {
	echo json_encode( array( 'error' => 'group missing' ) );
	return;
}

$before_locs = array();
foreach ( (array) ( $group['location'] ?? array() ) as $rule_group ) {
	foreach ( (array) $rule_group as $rule ) {
		if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
			$before_locs[] = (string) ( $rule['value'] ?? '' );
		}
	}
}

$group['location'] = array(
	array(
		array(
			'param'    => 'options_page',
			'operator' => '==',
			'value'    => 'fp02-reviews',
		),
	),
);
$group['description'] = 'FP-0002 V9-06D9-U options reviews — fp02-reviews canonical (E20 removed alias).';
$group['modified']    = 1783780000;

$db_write = false;
if ( function_exists( 'acf_update_field_group' ) ) {
	acf_update_field_group( $group );
	$db_write = true;
}

$after = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$after_locs = array();
foreach ( (array) ( $after['location'] ?? array() ) as $rule_group ) {
	foreach ( (array) $rule_group as $rule ) {
		if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
			$after_locs[] = (string) ( $rule['value'] ?? '' );
		}
	}
}

echo json_encode(
	array(
		'before_locations'    => $before_locs,
		'after_locations'     => $after_locs,
		'db_write'            => $db_write,
		'alias_removed'       => ! in_array( 'fp02-block-reviews', $after_locs, true ),
		'canonical_preserved' => in_array( 'fp02-reviews', $after_locs, true ),
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);

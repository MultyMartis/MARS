<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$rows = shpigovsky_get_comfort_gallery_static_rows();
echo 'rows=' . count($rows) . "\n";
update_field('comfort_gallery_items', $rows, 'fp02-block-comfort');
echo "seeded gallery\n";
global $submenu;
echo 'submenu=' . (isset($submenu['fp02-site-settings']) ? count($submenu['fp02-site-settings']) : 0) . "\n";

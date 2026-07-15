<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$map = array(
    'plugins/shpigovsky-core/src/Admin/OptionsPage.php' => 'wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
    'plugins/shpigovsky-core/src/Fields/FieldGroups.php' => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
    'theme/shpigovsky/inc/reusable-blocks-helpers.php' => 'wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php',
    'theme/shpigovsky/inc/hero-helpers.php' => 'wp-content/themes/shpigovsky/inc/hero-helpers.php',
    'theme/shpigovsky/template-parts/layout/header.php' => 'wp-content/themes/shpigovsky/template-parts/layout/header.php',
    'theme/shpigovsky/template-parts/layout/footer.php' => 'wp-content/themes/shpigovsky/template-parts/layout/footer.php',
    'theme/shpigovsky/template-parts/home/comfort.php' => 'wp-content/themes/shpigovsky/template-parts/home/comfort.php',
    'theme/shpigovsky/template-parts/home/rehabilitation-requirements.php' => 'wp-content/themes/shpigovsky/template-parts/home/rehabilitation-requirements.php',
);
foreach ($map as $src_rel => $rt_rel) {
    copy($root . '/' . $src_rel, $runtime . '/' . $rt_rel);
}
echo "copied\n";
define('WP_USE_THEMES', false);
require $runtime . '/wp-load.php';
echo "loaded\n";

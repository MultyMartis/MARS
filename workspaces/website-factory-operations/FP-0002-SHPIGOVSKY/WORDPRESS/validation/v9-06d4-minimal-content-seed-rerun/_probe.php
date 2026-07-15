<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$hero = get_field("home_hero_slides", 4);
$nav = get_field("home_service_nav_items", 4);
echo "HERO:\n";
var_export($hero);
echo "\nNAV:\n";
var_export($nav);
echo "\n";

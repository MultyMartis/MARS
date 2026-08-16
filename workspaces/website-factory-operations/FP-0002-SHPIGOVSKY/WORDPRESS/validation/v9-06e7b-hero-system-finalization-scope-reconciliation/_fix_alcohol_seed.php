<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$att = 305;
$r = update_field('hero_media', (int)$att, 74);
echo json_encode(['update_74' => (bool)$r, 'get' => get_field('hero_media', 74)], JSON_UNESCAPED_UNICODE);

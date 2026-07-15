<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
foreach ([73,74,77,84,6] as $id) {
  $p = get_post($id);
  echo $id." type=".$p->post_type." slug=".$p->post_name." parent=".$p->post_parent." permalink=".get_permalink($id)."\n";
}

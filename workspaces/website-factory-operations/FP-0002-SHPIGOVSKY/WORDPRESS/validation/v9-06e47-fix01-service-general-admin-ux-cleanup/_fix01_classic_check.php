<?php
require_once "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$supports = post_type_supports("service", "editor");
echo "post_type_supports_editor=" . ($supports ? "yes" : "no") . "\n";
// EditorRestrictions patterns
$files = array(
  "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core/src/Admin/EditorRestrictions.php",
);
foreach ($files as $f) {
  $c = file_get_contents($f);
  echo "has_remove_post_type_support=" . (strpos($c, "remove_post_type_support") !== false ? "yes" : "no") . "\n";
}

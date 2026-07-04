<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$r = get_option("rewrite_rules");
$depth2 = null;
if (is_array($r)) {
  foreach ($r as $p => $q) {
    if ($p === "^uslugi/([^/]+)/([^/]+)/?$") { $depth2 = $q; break; }
  }
}
echo json_encode([
  "rewrite_rules_hash" => hash("sha256", wp_json_encode($r)),
  "rewrite_rules_count" => is_array($r) ? count($r) : 0,
  "depth2_query" => $depth2,
  "service_74_permalink" => get_permalink(74),
], JSON_UNESCAPED_SLASHES), "\n";

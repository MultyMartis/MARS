<?php
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$p = get_page_by_path("specyalisty");
echo "page=" . ($p ? $p->ID : "none") . "\n";
if ($p) {
  $c = get_pages(array("child_of" => $p->ID, "post_status" => "publish"));
  echo "children=" . count($c) . "\n";
  foreach (array_slice($c, 0, 5) as $x) {
    echo get_permalink($x) . "\n";
  }
}
$html = file_get_contents("http://shpigovsky.test/specyalisty/");
preg_match_all('/href="(https?:\/\/shpigovsky\.test)?(\/specyalisty\/[^"#]+)"/', $html, $m);
$links = array_unique($m[2]);
echo "links=\n";
foreach (array_slice($links, 0, 10) as $l) echo $l . "\n";

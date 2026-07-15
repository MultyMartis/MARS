<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
header("Content-Type: text/plain; charset=utf-8");
foreach (array(1053,1054,1055,1056) as $id) {
  $p = get_post($id);
  echo $id."|".$p->post_title."|".$p->post_name."|".get_page_template_slug($id)."|".get_permalink($id)."\n";
}
// marker check on /uslugi/
$html = wp_remote_retrieve_body(wp_remote_get(home_url("/uslugi/"), array("timeout"=>15)));
preg_match_all('/services-category-section-v2__marker[^>]*>\s*(\d+)\s*</u', $html, $m);
echo "MARKERS=".implode(",", $m[1] ?? [])."\n";
echo "HAS_GENO_CAT=".(strpos($html,'services-category-genotyping')!==false?"YES":"NO")."\n";
echo "HAS_INTERNET_CANON=".(strpos($html,'internet-zavisimost')!==false?"YES":"NO")."\n";
echo "HAS_DUP=".(strpos($html,'lechenie-internet-zavisimosti')!==false?"YES":"NO")."\n";
// child menus sample
echo "HAS_CHILD_MENU=".(strpos($html,'services-category-section-v2__children')!==false || strpos($html,'service-link')!==false?"YES":"NO")."\n";
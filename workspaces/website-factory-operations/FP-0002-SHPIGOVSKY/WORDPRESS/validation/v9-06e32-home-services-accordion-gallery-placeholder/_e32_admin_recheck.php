<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$out = array(
  'nav_field' => acf_get_field('field_fp02_home_service_nav_items'),
  'home_gallery_flag' => acf_get_field('field_fp02_service_show_on_home_gallery'),
  'uslugi_slider' => acf_get_field('field_fp02_service_show_in_slider'),
  'uslugi_text' => acf_get_field('field_fp02_service_show_in_text_list'),
);
$gal_fail=0; $gal_ok=0;
foreach (shpigovsky_get_home_gallery_service_slides() as $s) {
  $code = (int) wp_remote_retrieve_response_code(wp_remote_get($s['url'], array('timeout'=>8)));
  if (200===$code) $gal_ok++; else $gal_fail++;
}
$out['gallery_links_ok']=$gal_ok; $out['gallery_links_fail']=$gal_fail;
file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-admin-recheck.json', wp_json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE));
echo "nav=".($out['nav_field']?'PRESENT':'GONE')." flag=".($out['home_gallery_flag']['label']??'missing')." gal_ok=$gal_ok fail=$gal_fail\n";

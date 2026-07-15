<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$out = array("services"=>array(),"program"=>array(),"routes"=>array());
$services = get_posts(array("post_type"=>"service","post_status"=>array("publish","draft","private","trash"),"posts_per_page"=>-1,"orderby"=>"menu_order","order"=>"ASC"));
foreach ($services as $p) {
  $out["services"][] = array("ID"=>(int)$p->ID,"title"=>$p->post_title,"slug"=>$p->post_name,"status"=>$p->post_status,"parent"=>(int)$p->post_parent,"url"=>get_permalink($p),"slider"=>get_post_meta($p->ID,"service_show_in_slider",true),"text_list"=>get_post_meta($p->ID,"service_show_in_text_list",true));
}
$prog = get_page_by_path("o-centre/programma-lecheniya");
if ($prog) {
  $out["program"]["parent"] = array("ID"=>(int)$prog->ID,"title"=>$prog->post_title,"slug"=>$prog->post_name,"template"=>get_page_template_slug($prog->ID),"url"=>get_permalink($prog));
  $kids = get_posts(array("post_type"=>"page","post_parent"=>(int)$prog->ID,"post_status"=>array("publish","draft","trash"),"posts_per_page"=>50));
  foreach ($kids as $k) {
    $out["program"]["children"][] = array("ID"=>(int)$k->ID,"title"=>$k->post_title,"slug"=>$k->post_name,"status"=>$k->post_status,"template"=>get_page_template_slug($k->ID),"url"=>get_permalink($k));
  }
}
$routes = array("/uslugi/genotipirovanie/","/o-centre/programma-lecheniya/","/o-centre/programma-lecheniya/genotipirovanie/","/uslugi/zavisimosti/lechenie-internet-zavisimosti/","/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/");
foreach ($routes as $r) {
  $resp = wp_remote_get(home_url($r), array("timeout"=>10,"redirection"=>0));
  $code = is_wp_error($resp) ? $resp->get_error_message() : wp_remote_retrieve_response_code($resp);
  $out["routes"][$r] = $code;
}
file_put_contents("X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e31-program-pages-links-validation-before-20260712-223200/service-page-inventory-before.json", wp_json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
echo "INVENTORY_OK services=".count($out["services"])."\n";
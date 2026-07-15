<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";

$routes = array(
  "/",
  "/uslugi/",
  "/uslugi/zavisimosti/",
  "/uslugi/psihicheskoe-zdorovie/",
  "/uslugi/rasstroystva-pischevogo-povedeniya/",
  "/uslugi/genotipirovanie/",
  "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/",
  "/uslugi/zavisimosti/lechenie-internet-zavisimosti/",
  "/uslugi/zavisimosti/kompyuternaya-zavisimost/",
  "/uslugi/zavisimosti/lechenie-opiumnoy-zavisimosti/",
  "/uslugi/psihicheskoe-zdorovie/hronicheskaya-ustalost/",
  "/uslugi/psihicheskoe-zdorovie/stress/",
  "/uslugi/psihicheskoe-zdorovie/nartsissizm/",
  "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/geroin/",
  "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/matadon/",
  "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/soli/",
  "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/lekarstva/",
  "/o-centre/",
  "/blog/",
  "/kontakty/",
);

$out = array();
foreach ($routes as $path) {
  $url = home_url($path);
  $ch = curl_init($url);
  curl_setopt_array($ch, array(
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_TIMEOUT => 20,
    CURLOPT_HEADER => true,
    CURLOPT_NOBODY => false,
  ));
  $resp = curl_exec($ch);
  $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $err = curl_error($ch);
  curl_close($ch);
  $fatal = (is_string($resp) && (false !== stripos($resp, "Fatal error") || false !== stripos($resp, "Uncaught Error")));
  $out[] = array("route"=>$path,"http"=>$code,"fatal"=>$fatal,"err"=>$err);
}

$html = @file_get_contents(home_url("/uslugi/"));
$dom = array(
  "markers" => array(),
  "section_order" => array(),
  "name_links" => 0,
  "child_menu_present" => false,
  "gallery_links" => 0,
  "genotyping_last" => false,
);

if (is_string($html) && $html !== "") {
  if (preg_match_all('/services-category-section-v2__marker[^>]*>\s*([^<]+)/u', $html, $m)) {
    $dom["markers"] = array_map("trim", $m[1]);
  }
  if (preg_match_all('/id="(services-category-[^"]+)"/u', $html, $s)) {
    $dom["section_order"] = $s[1];
  }
  $dom["name_links"] = preg_match_all('/services-category-section-v2__service-name-link/u', $html);
  $dom["child_menu_present"] = (false !== strpos($html, "services-category-section-v2__service-children"));
  $dom["gallery_links"] = preg_match_all('/services-category-section-v2__gallery-link/u', $html);
  $ids = $dom["section_order"];
  $dom["genotyping_last"] = (!empty($ids) && end($ids) === "services-category-genotyping");
  // sample narcotic children
  $dom["has_geroin_link"] = (false !== strpos($html, "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/geroin/"));
  $dom["has_internet_gallery"] = (false !== strpos($html, "/uslugi/zavisimosti/lechenie-internet-zavisimosti/"));
  $dom["has_ustalost_gallery"] = (false !== strpos($html, "/uslugi/psihicheskoe-zdorovie/hronicheskaya-ustalost/"));
}

$evidence = "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e30-services-catalog-child-services-listing-controls";
file_put_contents($evidence . "/e30-http-validation.json", json_encode(array("routes"=>$out,"dom"=>$dom), JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
echo json_encode(array("routes"=>$out,"dom"=>$dom), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES), PHP_EOL;

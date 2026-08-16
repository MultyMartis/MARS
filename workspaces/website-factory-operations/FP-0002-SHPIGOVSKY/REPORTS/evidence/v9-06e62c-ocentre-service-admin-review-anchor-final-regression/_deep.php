<?php
$base = "http://shpigovsky.test";
$routes = array("/", "/uslugi/", "/uslugi/zavisimosti/", "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "/o-centre/", "/kontakty/", "/blog/", "/otzyvy/", "/specyalisty/kostyuk/");
$checks = array();
foreach ($routes as $r) {
  $html = file_get_contents($base . $r);
  $checks[] = array(
    "route" => $r,
    "http" => strlen($html) > 1000 ? 200 : 0,
    "has_header" => strpos($html, "site-header") !== false || strpos($html, "header") !== false ? 1 : 0,
    "has_footer" => strpos($html, "site-footer") !== false || strpos($html, "footer") !== false ? 1 : 0,
    "has_form" => substr_count($html, "<form") ,
    "has_tel_mask_attr" => (strpos($html, "data-mask") !== false || strpos($html, "tel") !== false) ? 1 : 0,
    "has_yandex" => (strpos($html, "yandex") !== false || strpos($html, "constructor") !== false) ? 1 : 0,
    "has_libertinus" => strpos($html, "libertinus") !== false ? 1 : 0,
    "has_lifebuoy" => strpos($html, "lifebuoy") !== false ? 1 : 0,
    "canonical_count" => substr_count($html, 'rel="canonical"'),
    "php_warn" => preg_match("/(Fatal error|Warning:.*\\.php on line)/i", $html) ? 1 : 0,
  );
}
$ev = "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression";
$csv = "route,http,header,footer,forms,tel,yandex,libertinus,lifebuoy,canonicals,php_warn\n";
foreach ($checks as $c) {
  $csv .= implode(",", array($c["route"],$c["http"],$c["has_header"],$c["has_footer"],$c["has_form"],$c["has_tel_mask_attr"],$c["has_yandex"],$c["has_libertinus"],$c["has_lifebuoy"],$c["canonical_count"],$c["php_warn"])) . "\n";
}
file_put_contents("$ev/deep-regression-matrix.csv", $csv);
echo $csv;

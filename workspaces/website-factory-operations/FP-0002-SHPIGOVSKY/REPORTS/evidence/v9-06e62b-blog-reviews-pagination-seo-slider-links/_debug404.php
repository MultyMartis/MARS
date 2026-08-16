<?php
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";

echo "FILTER_REGISTERED=" . (has_filter("redirect_canonical", "shpigovsky_reviews_disable_canonical_redirect_when_out_of_range") ? "yes" : "no") . "\n";
echo "FUNC=" . (function_exists("shpigovsky_reviews_disable_canonical_redirect_when_out_of_range") ? "yes" : "no") . "\n";

// Simulate URL match
$url = "http://shpigovsky.test/otzyvy/page/99/";
$ok = preg_match('#/otzyvy/page/([0-9]+)/?(?:[?#]|$)#', $url, $m);
echo "REGEX=" . ($ok ? $m[1] : "fail") . "\n";

$items = shpigovsky_get_reviews_items(["featured_only"=>false,"limit"=>0]);
$ppp = shpigovsky_get_reviews_per_page();
$total = max(1, (int)ceil(count($items)/$ppp));
echo "COUNT=" . count($items) . " PPP=$ppp TOTAL=$total\n";

// Check runtime file contains URL-based filter
$rt = file_get_contents("X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/inc/reviews-helpers.php");
echo "HAS_URL_REGEX=" . (strpos($rt, "/otzyvy/page/") !== false ? "yes" : "no") . "\n";

// Curl with verbose status
$ch = curl_init($url);
curl_setopt_array($ch, [
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_HEADER => true,
  CURLOPT_FOLLOWLOCATION => false,
  CURLOPT_TIMEOUT => 20,
]);
$raw = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo "HTTP=$code\n";
if (preg_match('/^Location:\s*(\S+)/mi', $raw, $lm)) echo "LOC={$lm[1]}\n";

// Also test via WP request simulation
$_SERVER["REQUEST_URI"] = "/otzyvy/page/99/";
$_SERVER["HTTP_HOST"] = "shpigovsky.test";
// too heavy

// Check if paged vs page on live page 2
$ch = curl_init("http://shpigovsky.test/otzyvy/page/2/");
curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER=>true, CURLOPT_TIMEOUT=>20]);
$body = curl_exec($ch);
curl_close($ch);
echo "PAGE2_HAS_REVIEW11=" . (strpos($body, 'id="review-11"') !== false ? "yes" : "no") . "\n";
echo "PAGE2_HAS_REVIEW21=" . (strpos($body, 'id="review-21"') !== false ? "yes" : "no") . "\n";

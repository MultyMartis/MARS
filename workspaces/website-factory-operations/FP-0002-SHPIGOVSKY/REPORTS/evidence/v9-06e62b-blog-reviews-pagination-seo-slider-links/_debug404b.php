<?php
$url = "http://shpigovsky.test/otzyvy/page/99/";
echo preg_match('~/otzyvy/page/([0-9]+)/?(?:[?#]|$)~', $url, $m) ? ("OK ".$m[1]) : "fail";
echo "\n";
$ch = curl_init($url);
curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER=>true,CURLOPT_HEADER=>true,CURLOPT_FOLLOWLOCATION=>false]);
$raw = curl_exec($ch);
echo "HTTP=".curl_getinfo($ch, CURLINFO_HTTP_CODE)."\n";
if (preg_match('/^Location:\s*(\S+)/mi', $raw, $lm)) echo "LOC={$lm[1]}\n";
if (preg_match('/<title>(.*?)<\/title>/is', $raw, $t)) echo "TITLE=".trim(strip_tags($t[1]))."\n";
curl_close($ch);

// thumbs
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
for ($i=1745;$i<=1754;$i++) {
  $t=(int)get_post_thumbnail_id($i);
  echo "$i\t$t\t".($t?wp_get_attachment_url($t):"")."\n";
}

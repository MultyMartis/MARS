<?php
function probe($path) {
  $ch = curl_init('http://shpigovsky.test'.$path);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER=>true,CURLOPT_HEADER=>true,CURLOPT_FOLLOWLOCATION=>false,CURLOPT_TIMEOUT=>20]);
  $raw = curl_exec($ch);
  $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);
  $headers = explode("\r\n\r\n", $raw, 2)[0] ?? '';
  $body = explode("\r\n\r\n", $raw, 2)[1] ?? '';
  preg_match('/Location:\s*(\S+)/i', $headers, $loc);
  preg_match('/<title[^>]*>(.*?)<\/title>/is', $body, $t);
  preg_match('/rel=["\']canonical["\'][^>]*href=["\']([^"\']+)/i', $body, $c);
  if (!$c) preg_match('/href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']/i', $body, $c);
  $slider = preg_match_all('/data-review-slider-full-link/', $body);
  $anchors = preg_match_all('/id=["\']review-\d+["\']/', $body);
  $imgs200 = 0; $imgsFail=0;
  if (preg_match_all('/class="[^"]*blog-archive-card__media[^"]*"[^>]*>.*?<img[^>]+src=["\']([^"\']+)/is', $body, $im)) {
    foreach ($im[1] as $src) {
      $u = (strpos($src,'http')===0)?$src:('http://shpigovsky.test'.$src);
      $h = curl_init($u); curl_setopt_array($h,[CURLOPT_NOBODY=>true,CURLOPT_RETURNTRANSFER=>true,CURLOPT_TIMEOUT=>10]); curl_exec($h); $sc=curl_getinfo($h,CURLINFO_HTTP_CODE); curl_close($h);
      if ($sc===200) $imgs200++; else $imgsFail++;
    }
  }
  // fallback any featured on blog
  if (!$im && preg_match_all('/wp-content\/uploads\/[^"\']+\.(?:jpg|jpeg|png|webp)/i', $body, $im2)) {
    $uniq = array_unique($im2[0]);
    foreach (array_slice($uniq,0,8) as $src) {
      $u = 'http://shpigovsky.test/'.$src;
      $h = curl_init($u); curl_setopt_array($h,[CURLOPT_NOBODY=>true,CURLOPT_RETURNTRANSFER=>true,CURLOPT_TIMEOUT=>10]); curl_exec($h); $sc=curl_getinfo($h,CURLINFO_HTTP_CODE); curl_close($h);
      if ($sc===200) $imgs200++; else $imgsFail++;
    }
  }
  return [
    'path'=>$path,'status'=>$code,'location'=>$loc[1]??'','title'=>isset($t[1])?trim(html_entity_decode(strip_tags($t[1]))):'','canonical'=>$c[1]??'','slider_full_link_attrs'=>$slider,'review_anchors'=>$anchors,'img200'=>$imgs200,'imgFail'=>$imgsFail
  ];
}
$paths = ['/blog/','/blog/page/2/','/otzyvy/','/otzyvy/page/2/','/otzyvy/page/3/','/otzyvy/page/99/','/','/uslugi/zavisimosti/lechenie-alkogolnoj-zavisimosti/'];
// find alcohol permalink
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$alc = get_permalink(74);
echo "ALCOHOL_PERMALINK=$alc\n";
$paths[] = parse_url($alc, PHP_URL_PATH);
foreach ($paths as $p) {
  if (!$p) continue;
  $r = probe($p);
  echo json_encode($r, JSON_UNESCAPED_UNICODE), "\n";
}
// helper archive urls
if (function_exists('shpigovsky_get_review_archive_url')) {
  echo "URL11=", shpigovsky_get_review_archive_url(11), "\n";
  echo "URL21=", shpigovsky_get_review_archive_url(21), "\n";
  echo "URL1=", shpigovsky_get_review_archive_url(1), "\n";
}

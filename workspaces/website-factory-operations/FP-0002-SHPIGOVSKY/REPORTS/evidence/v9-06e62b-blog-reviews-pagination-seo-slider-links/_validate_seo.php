<?php
$routes = [
  '/',
  '/uslugi/',
  '/o-centre/',
  '/kontakty/',
  '/blog/',
  '/blog/page/2/',
  '/blog/page/3/',
  '/blog/page/99/',
  '/otzyvy/',
  '/otzyvy/page/2/',
  '/otzyvy/page/3/',
  '/otzyvy/page/99/',
  '/uslugi/zavisimosti/',
  '/uslugi/zavisimosti/lechenie-alkogolnoj-zavisimosti/',
];

function fetch_head($path) {
  $url = 'http://shpigovsky.test' . $path;
  $ch = curl_init($url);
  curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => false,
    CURLOPT_HEADER => true,
    CURLOPT_NOBODY => false,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_USERAGENT => 'FP0002-E62B-Validator',
  ]);
  $raw = curl_exec($ch);
  $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $err = curl_error($ch);
  curl_close($ch);
  if ($raw === false) {
    return ['url'=>$url,'status'=>0,'error'=>$err];
  }
  $parts = explode("\r\n\r\n", $raw, 2);
  $body = $parts[1] ?? '';
  $head = '';
  if (preg_match('/<head\b[^>]*>(.*?)<\/head>/is', $body, $m)) {
    $head = $m[1];
  }
  preg_match_all('/rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']/i', $head, $c1);
  preg_match_all('/href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']/i', $head, $c2);
  $canonicals = array_values(array_unique(array_merge($c1[1] ?? [], $c2[1] ?? [])));
  preg_match('/<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)["\']/i', $head, $robots);
  if (!$robots) {
    preg_match('/<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']robots["\']/i', $head, $robots);
  }
  preg_match('/<title[^>]*>(.*?)<\/title>/is', $head, $title);
  preg_match('/property=["\']og:url["\'][^>]+content=["\']([^"\']+)["\']/i', $head, $og);
  $php_warn = (false !== stripos($body, 'Warning:') || false !== stripos($body, 'Notice:') || false !== stripos($body, 'Fatal error'));
  $review_ids = [];
  if (preg_match_all('/id=["\']review-(\d+)["\']/', $body, $rm)) {
    $review_ids = $rm[1];
  }
  $slider_links = 0;
  if (preg_match_all('/data-review-slider-full-link[^>]*href=["\']([^"\']+)["\']/', $body, $sl)) {
    $slider_links = count($sl[1]);
  }
  // also count hidden footers presence
  $thumbs_broken = 0;
  if (preg_match_all('/src=["\']([^"\']+)["\']/', $body, $imgs)) {
    // skip deep check
  }
  return [
    'url' => $url,
    'status' => $code,
    'canonical_count' => count($canonicals),
    'canonical' => $canonicals[0] ?? '',
    'robots' => $robots[1] ?? '',
    'title' => isset($title[1]) ? trim(html_entity_decode(strip_tags($title[1]))) : '',
    'og_url' => $og[1] ?? '',
    'php_warn' => $php_warn ? '1' : '0',
    'review_anchors' => implode('|', $review_ids),
    'slider_full_links_in_html' => (string)$slider_links,
    'head_snip' => substr(preg_replace('/\s+/', ' ', $head), 0, 500),
  ];
}

$rows = [];
foreach ($routes as $r) {
  $rows[] = fetch_head($r);
}

$ev = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62b-blog-reviews-pagination-seo-slider-links';
$fh = fopen($ev . '/seo-canonical-matrix.csv', 'wb');
$headers = array_keys($rows[0]);
fputcsv($fh, $headers);
foreach ($rows as $row) {
  $out = [];
  foreach ($headers as $h) { $out[] = $row[$h]; }
  fputcsv($fh, $out);
}
fclose($fh);

// Save head captures for key routes
foreach (['/blog/','/blog/page/2/','/otzyvy/','/otzyvy/page/2/','/otzyvy/page/3/'] as $r) {
  $data = fetch_head($r);
  $safe = trim(str_replace(['/','\\'], '-', $r), '-');
  file_put_contents($ev . "/head-{$safe}.html", $data['head_snip'] . "\n\nCANONICAL=" . $data['canonical'] . "\nTITLE=" . $data['title'] . "\nSTATUS=" . $data['status'] . "\n");
}

echo json_encode($rows, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT), "\n";

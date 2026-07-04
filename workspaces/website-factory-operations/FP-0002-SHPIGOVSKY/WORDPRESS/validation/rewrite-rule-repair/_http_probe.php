<?php
$urls = [
  "http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
  "http://shpigovsky.test/uslugi/zavisimosti/",
  "http://shpigovsky.test/uslugi/",
];
foreach ($urls as $u) {
  $ch = curl_init($u);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER=>true, CURLOPT_NOBODY=>true, CURLOPT_TIMEOUT=>10]);
  curl_exec($ch);
  echo curl_getinfo($ch, CURLINFO_HTTP_CODE) . " " . $u . "\n";
  curl_close($ch);
}

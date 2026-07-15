<?php
$b = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e47-fix01-service-general-admin-ux-cleanup-before-20260715-125222/frontend";
$a = file_get_contents("$b/home-before.html");
$c = file_get_contents("$b/home-after.html");
// strip volatile
foreach ([$a,$c] as &$x) {
  $x = preg_replace('/ver=\d+(\.\d+)*/', 'ver=X', $x);
  $x = preg_replace('/nonce=["\'][^"\']+["\']/', 'nonce="X"', $x);
  $x = preg_replace('/wp\.apiFetch\.createNonceMiddleware\([^)]+\)/', 'NONCE', $x);
  $x = preg_replace('/"dateModified":"[^"]+"/', '"dateModified":"X"', $x);
  $x = preg_replace('/\s+/', ' ', $x);
}
if ($a === $c) { echo "HOME_EQUAL_AFTER_VOLATILE_STRIP\n"; exit(0); }
// find first diff
$max = min(strlen($a), strlen($c));
for ($i=0;$i<$max;$i++) {
  if ($a[$i] !== $c[$i]) {
    echo "diff@{$i}\n";
    echo "BEFORE: ".substr($a, max(0,$i-40), 120)."\n";
    echo "AFTER:  ".substr($c, max(0,$i-40), 120)."\n";
    break;
  }
}
echo "len a=".strlen($a)." c=".strlen($c)."\n";

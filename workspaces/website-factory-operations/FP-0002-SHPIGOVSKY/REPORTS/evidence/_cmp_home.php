<?php
$a = file_get_contents($argv[1]);
$b = file_get_contents($argv[2]);
$norm = function($t){
  $t = preg_replace('/ver=\d+/', 'ver=X', $t);
  $t = preg_replace('#https?://shpigovsky\.test#', 'ORIGIN', $t);
  $t = preg_replace('/wp-content\/uploads\/[^"\s]+/', 'UPLOAD', $t);
  $t = preg_replace('/\s+/', ' ', $t);
  return $t;
};
$a=$norm($a); $b=$norm($b);
echo 'EQ='.(int)($a===$b)."\n";
echo 'lena='.strlen($a).' lenb='.strlen($b)."\n";
if ($a!==$b) {
  $min=min(strlen($a),strlen($b));
  for ($i=0;$i<$min;$i++) if ($a[$i]!==$b[$i]) { echo 'diff_at='.$i.' ctxA='.substr($a,max(0,$i-40),80)."\n"; echo 'ctxB='.substr($b,max(0,$i-40),80)."\n"; break; }
}